---
name: izzul-brand
description: Apply Muhammad Izzul Islam Faisal's evidence-led personal branding, portfolio-derived visual language and document templates to consulting quotations, proposals, technical ML reports, client presentations, professional portfolio websites and branded professional materials. Use for brand creation, visual review, tone checks, document generation or website styling for this individual.
---

# Izzul personal brand system · v0.2

**Identity:** personal professional identity of Muhammad Izzul Islam Faisal, **not OrynLab**. Status: provisional and evidence-backed, pending final strategy/visual approvals.

## Mandatory operating sequence

1. **Identify the output**: quotation / proposal / technical report / presentation / website / brand review.
2. **Load the common rules**: `references/brand-strategy.md`, `references/visual-identity.md`, `references/voice-and-messaging.md`, `references/brand-decisions.md`.
3. **Load the relevant implementation**: `references/design-tokens.css`, `references/component-patterns.md`, and exactly the applicable template(s) in `templates/`.
4. **Apply the decision hierarchy**: latest explicit owner direction > approved ledger decisions > directly observed portfolio evidence > clearly marked working interpretation > suggestions. **Do not promote a proposed motto, positioning label, logo or business title to an approved fact.**
5. **Personalize and validate**: replace or request every required `[PLACEHOLDER]`; do not invent rates, client names, payment terms, testimonials, research results, or publication status.
6. **Export and inspect**: review the actual webpage or final PDF/page/slide rendering, text legibility, mobile responsiveness (where relevant), contrast, missing assets and confidential information. Use `references/quality-checklist.md`.

## Context routing

| Request | Read first | Starting artifact |
|---|---|---|
| Freelance quotation | `references/voice-and-messaging.md` and `references/quality-checklist.md` | `templates/quotation.html` |
| Consulting proposal | Strategy + commercial promises/claims | `templates/proposal.html`, `templates/proposal.md` |
| Research/ML report | Claim status and clinical integrity | `templates/technical-report.html`, `templates/technical-report.md` |
| Pitch/research slides | Presentation composition rules | `templates/presentation.html`, `templates/presentation.md` |
| Website styling | Website integration guide and existing-site constraints | `templates/website-starter.html`, `templates/website.md` |
| New symbol, tagline or design system edit | `references/brand-decisions.md` + `references/source-provenance.md` | Update ledger before treating anything as approved |

## Brand constants (observed, not locked)

- Existing visual source: **deep indigo/navy ground, gold/yellow headings and hairlines, Montserrat, white supporting text, cropped photographs, translucent lavender/violet ribbons and understated geometric layering**.
- The marketing/showcase portfolio is decorative and sometimes crowded. For real client documents, preserve recognition but **reduce intensity**, increase whitespace, prioritize evidence and scannability.
- Default client deliverables: white/light document body, navy hierarchy, gold accent dividers, violet only as a subtle secondary graphic. Deck covers/hero can be dark navy.
- Treat sampled HEX colors as **design approximations**; the Canva source file would be needed to verify original design tokens.
- Typography: Montserrat (supported by PDF font inspection); do not package font binaries. Fallbacks must preserve accessibility.

## Strategy boundaries

User-stated direction: excellence, mastery, discipline, high standards, execution, perseverance, competitive spirit and measurable impact. Translate these into *work quality, demonstrated depth, timelines, integrity and evidence*, not declarations of dominance to clients. Earlier assistant-proposed labels “The High-Performance AI Innovator” and “The Championship Standard,” and the sentence “Excellence is the standard. Mastery is the pursuit. Impact is the measure.” **are unapproved suggestions**. Do not use as an established slogan or public brand name.

Expertise to present when relevant: data science and machine learning, tabular prediction/model validation, SHAP/XAI, and research-oriented clinical/healthcare AI. Do not imply an MD, PhD, hospital credentials, regulatory clinical efficacy or results not independently documented. Healthcare is a differentiation, not an exclusion of non-healthcare clients.

## Red lines

- **Do not copy** OrynLab's Poppins, three-dot logo, monochrome design or plugin content. Its repository informs *packaging architecture only*.
- Do not claim the owner is currently “CEO of OrynLab” based on the older PDF. The owner earlier requested that role be removed from at least one professional application. Ask before reusing.
- Distinguish abstract acceptance, conference presentation, a poster, journal supplement, planned paper, indexed publication, completed external validation and commercial deployment.
- Do not put client data, personal contact identifiers, raw patient data or portfolio portraits into public templates or repositories without approval.
- Do not manufacture a logo or a client success case. A typographic name header is not an official logo.
- Do not silently overhaul the *existing website's information architecture*; adapt its current routes, sections and components and offer design changes separately.

## Repository details

`references/source-provenance.md` logs primary sources, visual page map and confidence. `references/brand-decisions.md` stores what the owner has actually signed off. `references/content-claims.md` provides reusable approved-or-unverified facts. For new approvals, log **date, actual wording and source**. Re-run `python scripts/validate_package.py` for structural validation and visually inspect exported artifacts.
