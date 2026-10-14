# Applying the personal brand

Read `skills/izzul-brand/SKILL.md` and its common references before authoring materials. The existing v0.2 strategy, provenance and decision ledger remain the source of truth; latest explicit owner instructions take precedence. Preserve the Claude skill and reference architecture.

Use `skills/izzul-brand/references/design-tokens.css` for colors and typography. For quotations, use `skills/izzul-brand/templates/quotation.html` and `quotation.css`. White A4 pages, navy hierarchy, thin gold rules and generous whitespace are the default. Use Montserrat when separately installed or loaded, with Arial/Helvetica fallbacks. Do not redistribute font binaries or extract fonts from the portfolio. No invented logo, tagline, credentials, legal entity or registration number.

Reusable templates must use placeholders for identity, contacts, clients, scope, amounts and terms. Keep completed quotations, research, financial analysis, PDF exports and private fonts under ignored `private/`. Root research PDFs are also ignored. Never force-add private files. An ignored file already tracked by Git is still tracked: inspect `git ls-files` and the staged diff before any commit or push.

For each quotation, verify item subtotals, grand total, milestone percentages and amounts, and separate pass-through expenses from professional fees. Do not guarantee clinical outcomes. Treat validity, tax treatment, acceptance, IP and regulatory responsibilities as engagement-specific; never invent confirmations or signatures.

HTML is the editable source; no server or AI API is needed. Print at A4 / 100%, with browser headers and footers disabled and background graphics enabled. Each `.sheet` is an explicit page; split long content into another sheet rather than reducing body text. Update all page labels after adding pages. Check every exported PDF page visually and confirm A4 dimensions and font embedding.

Run `python -X utf8 scripts/validate_package.py`, review staged files for privacy, and verify the remote and branch before pushing. Public documentation must not include private client details or commercial amounts.
