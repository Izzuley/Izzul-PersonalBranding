# Personal brand design system — Muhammad Izzul Islam Faisal

**Version:** 0.2.0 (working, not a finalized corporate identity)  
**Prepared:** 14 October 2026  
**Purpose:** One maintainable, AI-readable source of truth for personal consulting deliverables, client documents, research reports, slides and a professional website.

This repo is a **standalone Claude Code skill packaged as an optional Claude Code plugin**. It is *not* a website application or a generated logo. The visual reference is the owner's 16-page Canva portfolio PDF; the primary palette, typography and graphic vocabulary are extracted and adapted for more legible everyday business use. OrynLab's GitHub repository is a packaging precedent only, **not the owner's personal identity**.

## Reusable quotation workflow

Edit `skills/izzul-brand/templates/quotation.html` with shared `quotation.css`, which imports the existing brand tokens. Copy completed work into ignored `private/` folders. Follow [the editing and PDF guide](docs/quotation-workflow.md) for client fields, calculations, pagination, fonts and Chrome/Edge export. An optional Windows export helper is available at `scripts/export-quotation.ps1`; routine use needs no AI or paid service.

Codex users should follow the root `AGENTS.md` and the existing brand skill. Original strategy, references, source provenance and Claude plugin files are preserved. Private research, client outputs and font binaries are excluded from publication.

For separate development, cloud consumption and recurring maintenance, use `skills/izzul-brand/templates/quotation-allocations.html`. Its overview gives each allocation equal prominence and reconciles the full-term values. Follow [the concise editing guide](docs/QUOTATION_EDITING_GUIDE.md) for issuer/representative details, manual calculations and PDF export.

## Repository contents

| Folder | What it provides |
|---|---|
| `skills/izzul-brand/SKILL.md` | AI instructions: when to invoke, which reference to read, decision hierarchy and quality gates |
| `skills/izzul-brand/references/` | Brand strategy, visual identity, voice, CSS tokens, claims, evidence, QA, outstanding approvals |
| `skills/izzul-brand/templates/` | Working HTML prototypes and content structures for quotations, proposals, technical reports, slides and the website |
| `skills/izzul-brand/assets/` | Illustrative **non-logo** palette SVG; no third-party, personal or private photos |
| `.claude-plugin/` | Standalone plugin and optional marketplace metadata |
| `scripts/validate_package.py` | Standard-library structural checks for content and HTML/CSS references |
| `.github/workflows/validate.yml` | GitHub Actions structural check |

## Install in Claude Code

### Simple local skill install (best for personal use)

After cloning/extracting, copy `skills/izzul-brand/` into your Claude Code skills directory at `~/.claude/skills/izzul-brand/`. Keep the **whole directory**, not just `SKILL.md`, so all references/templates resolve. On Windows, use your user's `.claude/skills/izzul-brand/` directory.

Alternatively, keep the repo as the workspace and refer to `skills/izzul-brand/SKILL.md` directly, or copy the skill folder into a project's `.claude/skills/` directory for project-scoped use.

### Plugin marketplace (optional)

If this is hosted as `https://github.com/YOUR-USERNAME/YOUR-REPO`, the repository is already structured for:

```bash
claude plugin marketplace add https://github.com/YOUR-USERNAME/YOUR-REPO.git
claude plugin install izzul-brand@izzul-personal-brand
```

Replace the URL with your actual repository; these commands are **not live-tested** here. Claude Code's plugin commands/marketplace rules may evolve; verify them in your installed version. The root plugin metadata is in `.claude-plugin/plugin.json`.

## Example prompts

- “Use my **izzul-brand** skill to produce a quotation for a scoped tabular ML project. Ask me for the client details and price.”
- “Create a client proposal using my brand, leading with the client's problem rather than a list of awards.”
- “Create a 5-slide project pitch using `templates/presentation.html` and the approved brand constraints.”
- “Apply the visual tokens to my current portfolio website **without redesigning its content architecture**.”
- “Check this client report for style, evidence quality, accessibility, and private information.”

## Important distinctions

1. **Evidence vs decisions:** colors measured from a rendered PDF are approximate; strategy labels proposed in another chat are **not approved taglines**. See `references/source-provenance.md` and `references/brand-decisions.md`.
2. **Use the right visual density:** the existing PDF is an expressive, achievement-focused showcase. The client-facing templates intentionally use cleaner, mostly white layouts with navy/gold accents.
3. **Personal brand ≠ OrynLab:** do not copy its monochrome/Poppins identity, three-dot logo, Jira integration or website.
4. **Safe for public GitHub:** this package **does not include the original 29 MB PDF, its portraits, emails, phone numbers, or private client data**. The original portfolio remains a separate private reference. This repository is public-safe **by design**, but review any edits before publishing.
5. **No fabricated testimonials, case-study metrics, prices, legal terms or medical claims.** Every example uses conspicuous placeholders.
6. **No bundled font binaries:** Montserrat is source-confirmed by the PDF's embedded font metadata but must be installed or loaded separately for faithful rendering.

## Quality check

```bash
python scripts/validate_package.py
```

This checks structure, manifests, relative CSS paths, templates, and known placeholder constraints. It is **not** a Claude runtime installation test or comprehensive accessibility/medical compliance audit. Generate real documents and check the printed/exported result before sending to clients.

## Source inventory

- **Private primary visual source:** `Portfolio_Izzul.pdf`, 16 pages, created with Canva (inspected visually, text and fonts reviewed). Not distributed here.
- **Personal-brand strategy discussion:** summary retrieved on 14 Oct 2026; explicit user themes and assistant proposals separated. Does **not** represent the other chat's full transcript.
- **Structural reference:** `https://github.com/Amjadh23/OrynGithub`, `main` at `2ea84f2133f58314c7d1c6436ebf55d095ac6a3a` (reviewed 14 Oct 2026).

See `references/source-provenance.md` for a page-by-page visual inventory and `references/brand-decisions.md` for what requires approval.
