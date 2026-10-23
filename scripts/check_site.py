#!/usr/bin/env python3
"""Static regression checks for the bilingual personal homepage."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


PALETTE = ("#F5F1E8", "#292823", "#716D64", "#DDD7CC", "#6A6F51")
REQUIRED_SECTIONS = ("about", "education", "interests", "projects", "contact")
LEGACY_PATTERNS = (
    r"\bhero-visual\b",
    r"\borbit(?:-one|-two|-three)?\b",
    r"linear-gradient\s*\(",
    r"radial-gradient\s*\(",
    r"backdrop-filter\s*:",
    r"box-shadow\s*:",
    r"\.tag\b",
    r"\.interest-card\b",
    r"\.project-card\b",
    r"\bsection-index\b",
    r"\bvisual-core\b",
)


class Document(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.fragments: list[str] = []
        self.tags: list[str] = []
        self.h1_count = 0
        self.title_open = False
        self.title_text = ""
        self.link_open = False
        self.link_text: list[str] = []
        self.links: list[tuple[str, str]] = []
        self.lang = ""
        self.skip_link_found = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        self.tags.append(tag)
        if tag == "html":
            self.lang = attrs_dict.get("lang") or ""
        if "id" in attrs_dict:
            self.ids.append(attrs_dict["id"] or "")
        if tag == "h1":
            self.h1_count += 1
        if tag == "title":
            self.title_open = True
        if tag == "a":
            self.link_open = True
            self.link_text = []
            href = attrs_dict.get("href") or ""
            self.links.append((href, attrs_dict.get("class") or ""))
            if href.startswith("#"):
                self.fragments.append(href[1:])
            if "skip-link" in (attrs_dict.get("class") or "").split() and href == "#main-content":
                self.skip_link_found = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.title_open = False
        if tag == "a" and self.link_open:
            self.link_open = False

    def handle_data(self, data: str) -> None:
        if self.title_open:
            self.title_text += data
        if self.link_open:
            self.link_text.append(data)


def relative_luminance(color: str) -> float:
    channels = [int(color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4 for value in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast_ratio(foreground: str, background: str) -> float:
    light, dark = sorted((relative_luminance(foreground), relative_luminance(background)), reverse=True)
    return (light + 0.05) / (dark + 0.05)


def inspect(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"{path}: file does not exist"]

    source = path.read_text(encoding="utf-8")
    lower = source.lower()
    doc = Document()
    doc.feed(source)

    if not source.lstrip().lower().startswith("<!doctype html>"):
        errors.append("missing HTML5 doctype")
    if doc.lang not in ("en", "zh-CN"):
        errors.append(f"unexpected or missing html lang: {doc.lang!r}")
    if not doc.title_text.strip():
        errors.append("missing document title")
    if doc.h1_count != 1:
        errors.append(f"expected exactly one h1, found {doc.h1_count}")
    for landmark in ("header", "main", "footer", "nav"):
        if landmark not in doc.tags:
            errors.append(f"missing semantic {landmark} element")

    duplicates = sorted({item for item in doc.ids if doc.ids.count(item) > 1})
    if duplicates:
        errors.append("duplicate id(s): " + ", ".join(duplicates))

    ids = set(doc.ids)
    for fragment in doc.fragments:
        if fragment and fragment not in ids:
            errors.append(f"unresolved fragment link: #{fragment}")

    required_ids = set(REQUIRED_SECTIONS) | {"main-content", "top"}
    missing_ids = sorted(required_ids - ids)
    if missing_ids:
        errors.append("missing required section/landmark id(s): " + ", ".join(missing_ids))

    if not doc.skip_link_found:
        errors.append("missing skip-to-content link targeting #main-content")
    if ":focus-visible" not in lower:
        errors.append("missing visible keyboard focus styling")
    if "prefers-reduced-motion" not in lower:
        errors.append("missing reduced-motion support")
    if not re.search(r"@media\s*\([^)]*max-width\s*:", source, re.I):
        errors.append("missing responsive max-width media query")

    for color in PALETTE:
        if color.lower() not in lower:
            errors.append(f"missing approved palette color {color}")
    page_color = re.search(r"--page\s*:\s*(#[0-9a-fA-F]{6})", source)
    accent_color = re.search(r"--accent\s*:\s*(#[0-9a-fA-F]{6})", source)
    if not page_color or not accent_color:
        errors.append("could not determine page and accent colors for contrast check")
    elif contrast_ratio(accent_color.group(1), page_color.group(1)) < 4.5:
        errors.append("accent color contrast against page background is below 4.5:1")
    if "fonts.googleapis.com" in lower or "use.typekit.net" in lower:
        errors.append("unexpected remote font dependency")

    for pattern in LEGACY_PATTERNS:
        if re.search(pattern, source, re.I):
            errors.append(f"legacy/template-like visual pattern remains: {pattern}")

    hrefs = [href for href, _ in doc.links]
    if not any(href == "zh.html" for href in hrefs) and doc.lang == "en":
        errors.append("English page is missing the zh.html language switch")
    if not any(href == "index.html" for href in hrefs) and doc.lang == "zh-CN":
        errors.append("Chinese page is missing the index.html language switch")
    if not any(href == "https://github.com/Bogey-man-pro" for href in hrefs):
        errors.append("missing GitHub profile link")
    if not any(href == "https://github.com/Bogey-man-pro/ZixuanZhang.github.io" for href in hrefs):
        errors.append("missing homepage repository link")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path, help="HTML files to validate (default: index.html zh.html)")
    args = parser.parse_args()
    paths = args.files or [Path("index.html"), Path("zh.html")]

    all_errors: list[tuple[Path, str]] = []
    for path in paths:
        errors = inspect(path)
        if errors:
            all_errors.extend((path, error) for error in errors)
        else:
            print(f"PASS {path}")

    if all_errors:
        for path, error in all_errors:
            print(f"FAIL {path}: {error}", file=sys.stderr)
        print(f"{len(all_errors)} check(s) failed.", file=sys.stderr)
        return 1

    print(f"All checks passed for {len(paths)} page(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
