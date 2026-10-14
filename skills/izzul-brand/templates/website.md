# Existing personal website — non-destructive brand integration guide

**This is NOT a replacement sitemap or new web app brief.** The user is already developing a portfolio that should serve Upwork/direct clients, hiring managers, researchers and general audiences. Adapt the existing codebase's architecture; don't force 16 A4 PDF pages into a scroll-by-page website.

## How to integrate

1. Audit current routes, sections, global styles, font loading and Tailwind/theme configuration.
2. Map new **semantic tokens** from `../references/design-tokens.css` into the site's existing globals. Do not override dark/light themes blindly.
3. Apply deep navy and restrained gold in hero, section headings, rules and CTAs. Keep reading sections light for accessibility. Use violet decor sparingly.
4. Preserve existing scroll navigation, deep links to projects, and detailed project pages unless the owner approves changes.
5. Prioritize direct evidence for selected projects: problem → method → results → limitations → your contribution → supporting link.
6. Keep pathways for freelance clients (services/CTA), academic collaborators (research), hiring teams (experience) and general visitors (leadership/highlights) without forcing identical emphasis.
7. Test at 320, 375, 768, 1024 and 1440 CSS px; keyboard and screen reader semantics; avoid decorative overlaps.

`website-starter.html` is a standalone **visual proof-of-concept** with the derived palette and example sections. Its hero headline is demo copy, not a finalized tagline.

## Content truth conditions

- Check latest graduation/position and publication statuses immediately before publishing.
- Treat healthcare claims conservatively; do not imply medical regulatory approval or clinical deployment unless proven.
- Source photography separately and ensure use rights. The original private PDF is not shipped.
- OrynLab company brand and personal identity are different systems.
