# Warm Editorial Academic & Technical Homepage — Design Specification

- Date: 2026-10-23
- Status: Proposed; awaiting approval
- Target files: index.html, zh.html
- Audience: prospective supervisors and laboratories, technical peers, and potential collaborators

## Intent

Make the site feel like a thoughtful personal homepage rather than a generic AI-generated tech portfolio. It should communicate a real materials-science background and an ongoing interest in AI-agent/software work with quiet confidence. The design should feel warm, editorial, and tactile through typography, spacing, and restrained surfaces—not through decorative effects.

## Goals

1. Make identity, academic background, current interests, and public work understandable within a short visit.
2. Balance academic credibility with evidence of technical curiosity and hands-on practice.
3. Reduce common template signals: decorative orbital artwork, blue-to-teal gradients, repeated rounded cards, capsule tags, repetitive numbered section labels, and generic slogan copy.
4. Keep Chinese and English pages visually consistent while allowing each language to read naturally.
5. Preserve a lightweight, accessible, responsive static site.

## Non-goals and anti-goals

- Do not introduce a frontend framework, build step, analytics, animation library, or unnecessary dependencies.
- Do not add fabricated publications, research results, metrics, project outcomes, endorsements, or contact details.
- Do not expose private repository names, source details, screenshots, or project information on the public site without explicit approval.
- Do not add a stock portrait, AI-generated portrait, or generic abstract hero illustration to fill space.
- Do not equate sophistication with more visual effects, more cards, or more copy.
- Do not remove existing language routes or break the GitHub Pages URLs.

## Approaches considered

### A. Academic-first
Lead with academic identity and interests, followed by education, work, and contact. Strong for supervisors, but can underplay technical practice.

### B. Project-first
Lead with concrete projects and implementation details. Strong for technical peers, but risks overclaiming or feeling thin if there are not enough public projects to show.

### C. Editorial fusion — selected
Lead with a concise personal introduction, then present education and current interests, followed by a carefully curated public-work section and contact links. This keeps the site useful to all three audiences without making it resemble a CV template or a product landing page.

## Visual system

### Palette

- Page: warm ivory, approximately #F5F1E8
- Main text: charcoal, approximately #292823
- Secondary text: warm gray, approximately #716D64
- Rules and borders: paper gray, approximately #DDD7CC
- Single accent: muted olive, approximately #6A6F51

Use the accent sparingly for links, small markers, and focus states. Its contrast against the page background must be at least 4.5:1 for normal text. Avoid blue/teal gradients, neon, glow, glass effects, strong drop shadows, and multiple competing accent colors. A subtle paper impression should come from warm color and restrained borders, not a heavy texture overlay.

### Typography

- Use a restrained serif face for the name and selected major headings, with system sans-serif for body copy and navigation.
- Use native/system font stacks only; do not add remote font dependencies.
- Tune Chinese and English font stacks, line-height, and wrapping separately.
- Keep body text comfortable to read and line lengths moderate; use whitespace to establish hierarchy.

### Layout and components

- Header: simple wordmark/name, compact text navigation, and a plain language switch. Avoid a heavy sticky/glass header.
- Hero: name, current academic identity, a short concrete introduction, and one or two quiet text links. Remove the abstract orbital graphic and decorative badge/tag row.
- Education: a simple editorial row or timeline-like text grouping, not a floating card.
- Interests: three plain text groupings or ruled rows for materials science, AI-agent/software practice, and scientific/engineering computing. Avoid identical feature cards.
- Public work: a compact list with title, factual one- or two-sentence description, and direct link. Only include content that is public and verified. If there is not enough material, show a restrained GitHub link instead of inventing a project showcase.
- Contact: a simple closing paragraph and GitHub link. Do not invent an email address.
- Use fine horizontal rules, variable spacing, and limited alignment asymmetry to give the page a natural editorial rhythm.
- Keep mobile layouts single-column, with no horizontal overflow and clear tap targets.

## Content direction

### Chinese hero copy — proposed

张子轩 / Zixuan Zhang  
安徽工业大学 · 材料科学与工程

“我在学习材料科学与工程，也持续关注 AI 智能体与软件工具。我希望把对材料问题的理解与计算和自动化实践联系起来，并在具体项目中验证这些工具能做什么。”

### English hero copy — proposed

Zixuan Zhang  
Materials Science and Engineering · Anhui University of Technology

"I'm an undergraduate in Materials Science and Engineering at Anhui University of Technology. Outside my coursework, I explore AI-agent tools and software, with an interest in how computation can support technical work."

Treat these as draft copy; retain a grounded, first-person voice and avoid inflated claims such as “bridging disciplines,” “pushing boundaries,” or “shaping the future.”

### Section order

1. Personal introduction
2. Education
3. Research and technical interests
4. Selected public work / GitHub
5. Contact

Education should be easy to find for academic readers; technical work should be easy to reach for peers. Neither audience should have to scan decorative cards to understand the page.

## References and interpretation

Use the following real sites as directional references, not templates to copy:

- Lauren Waller — https://lauren-waller.com/ : restraint, typography, and whitespace.
- Hira Javed — https://hirajaved.com/ : personal voice and experience-led presentation.
- Madeline Eppley — https://www.madeline-eppley.com/ : academic context and clear personal information.
- Anthony Fu — https://antfu.me/ : technical work and public projects as the substance of a developer profile.

The result should not imitate any single reference. It should keep the content density and tone appropriate to an undergraduate whose public portfolio is still developing.

## Technical and accessibility constraints

- Preserve index.html and zh.html and their language-switch links.
- Preserve responsive behavior and test at narrow mobile, tablet, and desktop widths.
- Retain semantic landmarks, meaningful link text, keyboard-visible focus, skip-to-content navigation, sufficient contrast, and reduced-motion support.
- Avoid relying on color alone to communicate meaning.
- Keep external links accurate and clearly labeled.

## Acceptance criteria

1. The orbital hero illustration, gradient-heavy surfaces, capsule tags, and repetitive card grid are removed.
2. The page uses the warm ivory/charcoal/one-accent palette with restrained borders and whitespace.
3. The name and academic identity are the clearest elements in the first viewport.
4. Education, interests, public work, and contact have distinct but not mechanically identical layouts.
5. Copy is specific, first-person, and truthful; no unsupported achievements or private project details appear.
6. Both language versions remain aligned in hierarchy, navigation, links, and accessibility.
7. Internal anchors resolve, language switching works, and no horizontal overflow appears at mobile widths.
8. The site remains static HTML/CSS with no new dependencies.

## Implementation boundary

This specification does not authorize a production edit by itself. After approval, create an implementation plan, then make the changes on an isolated branch and verify both pages before proposing integration.
