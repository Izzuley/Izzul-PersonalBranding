# Quality and release checklist

## Brand evidence / approvals
- [ ] User's *latest* directly approved strategy/voice/palette decisions reflected in `brand-decisions.md`.
- [ ] No proposed slogan, positioning label or invented official logo is treated as approved.
- [ ] Navy/gold/Montserrat recognition preserved without importing OrynLab's brand assets.
- [ ] Violet waves are intentional, restrained and never cover important information.

## Professional and factual integrity
- [ ] Headline and services answer client need; proof follows rather than crowding the opening.
- [ ] All client names, fees, terms, deadlines and invoice IDs supplied, not invented.
- [ ] Awards, participation and publications dated and described with accurate status; relevant evidence linked or available.
- [ ] Clinical/research model metrics include cohort, evaluation design, limitations, and date; no claim of treatment benefit from ML prediction alone.
- [ ] No unauthorized clinical advice, medical-device clearance, licensure or patient outcomes claimed.

## Readability and accessibility
- [ ] High contrast (especially gold on white: forbidden as small readable text).
- [ ] Proper H1/H2 sequence, real document titles and semantic table headers.
- [ ] Body text ≥16px web or approximately ≥10pt print unless constrained and reviewed.
- [ ] Website keyboard focus and mobile viewport checked; no content truncated at 320px.
- [ ] PDF print safe margins, no orphan totals or cut-off letterhead/signatures.
- [ ] Slides 16:9 with legible captions, axes/units, labels and limited bullets.
- [ ] Decorative elements hidden from assistive technologies where appropriate.

## Privacy, rights, versioning
- [ ] No source portfolio, private client details, research datasets, patient identifiers, password/token, or private photographs in public repo.
- [ ] License/right to reuse photos or graphics checked before publishing.
- [ ] Montserrat sourced legally, no font binaries copied from PDF.
- [ ] External assets/URLs kept minimal or declared; offline fallback tested.
- [ ] Relevant placeholders replaced before client delivery.
- [ ] Static check `python scripts/validate_package.py` passes.
- [ ] Final exported artifacts reviewed **visually** (not just markdown/CSS lint).
