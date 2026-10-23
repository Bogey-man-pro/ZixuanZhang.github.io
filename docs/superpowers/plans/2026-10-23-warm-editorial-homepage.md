# Warm Editorial Academic & Technical Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Redesign the English and Chinese static homepages into a warm, restrained editorial profile that serves prospective supervisors, technical peers, and potential collaborators without generic AI-portfolio styling.

**Architecture:** Keep the existing two-page static HTML/CSS architecture. Add a small Python-standard-library validation script for structural, responsive, accessibility, link, and design-regression checks; update each language page independently, then validate both together.

**Tech Stack:** HTML5, CSS, Python 3 standard library for static validation. No runtime dependencies or build step.

**Spec:** docs/superpowers/specs/2026-10-23-warm-editorial-homepage-design.md

## Global Constraints

- Page background: warm ivory, approximately #F5F1E8.
- Main text: charcoal, approximately #292823.
- Secondary text: warm gray, approximately #716D64.
- Rules and borders: paper gray, approximately #DDD7CC.
- Single accent: muted olive, approximately #73785A.
- Use native/system font stacks only; do not add remote font dependencies.
- Do not introduce a frontend framework, build step, analytics, animation library, or unnecessary dependencies.
- Do not add fabricated publications, research results, metrics, project outcomes, endorsements, or contact details.
- Do not expose private repository names, source details, screenshots, or project information on the public site without explicit approval.
- Do not add a stock portrait, AI-generated portrait, or generic abstract hero illustration to fill space.
- Preserve index.html and zh.html and their language-switch links.
- Retain semantic landmarks, meaningful link text, keyboard-visible focus, skip-to-content navigation, sufficient contrast, and reduced-motion support.
- Keep the site static HTML/CSS with no new runtime dependencies.

## Review Focus

1. **Broken internal or language links:** every fragment target exists and each language switch points to the counterpart page. Test in scripts/check_site.py.
2. **Mobile overflow and cramped navigation:** media queries exist and content can stack at narrow widths; inspect CSS rules and validate the narrow viewport layout when browser tooling is available.
3. **Accessibility regressions:** exactly one h1, semantic landmarks, skip link, visible focus, and reduced-motion support remain. Test in scripts/check_site.py.
4. **Design regression to template-like decoration:** orbital art, gradient fills, capsule tags, repeated numbered labels, shadows, and identical card grids are absent. Test in scripts/check_site.py.
5. **Content integrity and privacy:** project claims are grounded in public repository evidence; no private project details or invented achievements are published. Review the copy and every external project link before merge.

---

### Task 1: Add a static homepage validation script

**Files:**
- Create: scripts/check_site.py
- Test: scripts/check_site.py against the current index.html and zh.html

**Interfaces:**
- Consumes: one or more HTML file paths; if omitted, validate index.html and zh.html.
- Produces: a zero exit code on success; non-zero exit code with actionable messages on failure.

- [ ] **Step 1: Write the checker with failing design and structure assertions**

Use only Python standard-library modules: argparse, html.parser, pathlib, re, and sys. Parse each document and check the doctype, language, title, one h1, semantic main/header/footer, unique IDs, resolved fragment links, counterpart language link, GitHub destinations, skip link, focus-visible style, reduced-motion query, responsive media query, and presence of the approved palette. Reject external font dependencies and legacy visual patterns such as orbit/hero-visual artwork, gradients, backdrop filters, shadows, capsule tags, repeated section-number labels, and repetitive interest/project card classes.

- [ ] **Step 2: Run it against the existing pages and confirm the expected failures**

Run: python scripts/check_site.py index.html zh.html
Expected: non-zero exit because the current pages still contain the legacy orbital/gradient/card visual system.

- [ ] **Step 3: Commit the checker**

Commit message: test: add static homepage design checks

### Task 2: Redesign the English homepage

**Files:**
- Modify: index.html
- Test: scripts/check_site.py index.html

**Interfaces:**
- Consumes: approved design specification and scripts/check_site.py.
- Produces: a self-contained English homepage matching the warm editorial system.

- [ ] **Step 1: Replace the English document with the editorial structure**

Use the warm ivory/charcoal/warm-gray/paper-gray/olive palette. Remove the orbit illustration, gradient-heavy surfaces, capsule tags, decorative numbered labels, repeated feature cards, and generic slogan copy. Use a restrained serif/system-sans type pairing, a quiet text navigation, a name-led hero, a short grounded first-person introduction, an education row, plain text interest groups, a compact public-work list, and a simple GitHub contact link.

- [ ] **Step 2: Verify the English page**

Run: python scripts/check_site.py index.html
Expected: PASS for document structure, anchors, links, palette, accessibility hooks, responsive CSS, and removal of legacy visual patterns.

- [ ] **Step 3: Review content claims and links**

Confirm the copy only states verified academic identity and current interests. Link the homepage repository and GitHub profile; do not list private project details or imply publications/results that are not verified.

- [ ] **Step 4: Commit the English page**

Commit message: style: redesign English homepage with warm editorial layout

### Task 3: Redesign the Chinese homepage

**Files:**
- Modify: zh.html
- Test: scripts/check_site.py zh.html and scripts/check_site.py index.html zh.html

**Interfaces:**
- Consumes: the approved design specification, the English page's visual system, and scripts/check_site.py.
- Produces: a naturally written Chinese counterpart with matching hierarchy and styling.

- [ ] **Step 1: Replace the Chinese document with the editorial structure**

Keep the same palette and overall hierarchy as index.html, but tune Chinese line-height, font fallbacks, heading spacing, and paragraph wrapping independently. Use natural first-person Chinese copy; avoid direct translation that sounds like a slogan. Retain the existing English-language switch and GitHub links.

- [ ] **Step 2: Verify each page and both pages together**

Run: python scripts/check_site.py zh.html
Run: python scripts/check_site.py index.html zh.html
Expected: both commands PASS; all local anchors and language-switch targets resolve.

- [ ] **Step 3: Compare the two versions**

Confirm that section order, destination URLs, palette, focus treatment, responsive rules, and semantic structure match while the language-specific text remains natural.

- [ ] **Step 4: Commit the Chinese page**

Commit message: style: redesign Chinese homepage with warm editorial layout

### Task 4: Final verification and integration review

**Files:**
- Review: index.html
- Review: zh.html
- Review: scripts/check_site.py

**Interfaces:**
- Consumes: the completed pages and validation script.
- Produces: verified branch ready for a pull request review.

- [ ] **Step 1: Run the complete static checks**

Run: python scripts/check_site.py index.html zh.html
Expected: PASS with no reported structural, accessibility, link, palette, or design-regression issues.

- [ ] **Step 2: Inspect the final diff**

Confirm that only the two page files and the validation script changed for implementation; the design specification and plan remain available under docs/superpowers.

- [ ] **Step 3: Review against the acceptance criteria**

Verify all eight criteria in docs/superpowers/specs/2026-10-23-warm-editorial-homepage-design.md, especially truthful content, mobile behavior, and removal of the old visual system.

- [ ] **Step 4: Open a pull request for review**

Do not merge until the final diff and checks are reviewed. Verify GitHub Pages after merge rather than claiming deployment success based only on source changes.
