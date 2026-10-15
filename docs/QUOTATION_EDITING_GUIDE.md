# Editing a quotation with three financial allocations

Use `skills/izzul-brand/templates/quotation-allocations.html` for separate development, cloud infrastructure and recurring support. The original `quotation.html` remains available for simpler engagements. Both use `quotation.css`, which imports the existing brand tokens.

1. Copy the template into an ignored folder such as `private/YOUR-PROJECT/`. Update its stylesheet link to `../../skills/izzul-brand/templates/quotation.css`. A further nested folder needs one more `../`.
2. Edit the HTML directly in VS Code. Replace the issuer, registration details, representative, contacts, client, issue date, validity, scope, durations, prices and terms. Use only confirmed details. Remove unused placeholders and sections.
3. Update every repeated amount. Values are manual, not automatically calculated. Sum development rows; sum hosting and licensing; sum monthly maintenance rows; multiply each by the maintenance months; reconcile all three full-term allocations. Distinguish provider fees from institution-paid cloud consumption.
4. Record the warranty period and maintenance start conditions. Confirm included support hours, coverage hours, additional-work rates, exclusions and billing terms. Do not infer SLAs or contractual authority.
5. Save and refresh Chrome or Edge. Each `.sheet` is one A4 page. If content grows, add a sheet and update footer numbers rather than shrinking the text. Check all tables and page boundaries.

## Fonts and PDF export

Use locally installed Montserrat, or an appropriately licensed private font loaded by `@font-face`. Arial/Helvetica are fallbacks. Keep linked CSS, tokens and fonts in their relative locations; the HTML is editable but is not a standalone asset bundle. Font binaries are not committed.

In Chrome/Edge press Ctrl+P, select Save as PDF, A4 portrait, 100% scale, no margins, browser headers/footers off and background graphics on. The CSS supplies the page margins and document footers. Inspect every page, then save inside the private project folder. No AI, server or paid API is required.

Optional export from the repository root:

```powershell
powershell -NoProfile -File scripts/export-quotation.ps1 -Html private/YOUR-PROJECT/Quotation.html -Pdf private/YOUR-PROJECT/Quotation.pdf
```

The helper refuses to overwrite an existing file. Export to a new revision filename, inspect it, and replace the earlier PDF after closing any viewer holding it open. Retain earlier commercial versions privately when needed.

## Before sending or publishing

Check issuer authorization, required vendor details, tax/invoicing treatment, payment arrangements, agreed scope and approval status. Keep open commercial decisions in private review notes. A proposed quotation is not evidence of client acceptance.

Run `python -X utf8 scripts/validate_package.py`. Review `git diff --cached` and `git ls-files` before publishing. Only generic templates, CSS and instructions belong in the public repository. Research, completed quotations, registration/contact details supplied for a client and private financial notes stay under ignored `private/`.
