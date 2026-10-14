# Validation report — 14 October 2026

## Completed checks

- **Static structural validation:** `python scripts/validate_package.py` — PASS.
- **Repository:** standalone Claude Code `skills/izzul-brand/SKILL.md` plus `plugin.json` / optional marketplace metadata — present and JSON-parseable.
- **Referenced assets:** every local CSS link used by HTML templates resolves inside the package.
- **Privacy:** deliberately excludes the original portfolio PDF, photographs, private contact details and font binaries.
- **Source discipline:** user-stated themes distinguishable from assistant-proposed brand labels; no tagline declared approved.
- **HTML→PDF smoke tests** via WeasyPrint (proof of layout, not equivalent to Claude installation):
  - `quotation.html` → one A4 page.
  - `proposal.html` → two A4 pages, with explicit section break.
  - `technical-report.html` → two A4 pages, with explicit section break.
  - `presentation.html` → four 16:9 pages at 960×540 PDF points.
  - `website-starter.html` → HTML source renderable to PDF, but **website is meant for browser rendering**, not A4 printing.

## Limitations (not tested or not certified)

- Claude Code plugin installation/skill invocation and actual Jira or MCP integrations were **not live-tested**; this package does not need Jira.
- Native browser mobile interaction and performance were **not tested** because a headless Chromium runtime wasn't available. Mobile CSS and semantics are implemented but must be verified on the owner's actual portfolio project.
- Color values are sampled approximations from a rasterized PDF, not original editable Canva tokens.
- Montserrat fonts were not embedded. PDF smoke tests may fall back to a compatible system font.
- Client legal terms, sales promises, academic awards, publication status, clinical validation, web accessibility compliance and print color fidelity require final per-project owner review.

## Required release hygiene

Replace all bracketed template fields, visually inspect client exports, update the `brand-decisions.md` ledger when strategy is approved, and re-run structural checks after edits.
