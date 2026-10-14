# Editable quotations

The source is ordinary HTML and shared CSS. Routine editing and PDF export require no AI, tokens, paid service, web server or package installation. Use VS Code and Chrome or Edge.

## Create a private quotation

1. Create `private/YOUR-PROJECT/` in this repository.
2. Copy `skills/izzul-brand/templates/quotation.html` into it, with a descriptive filename.
3. Change its stylesheet link to `../../skills/izzul-brand/templates/quotation.css`.
4. Replace bracketed placeholders with confirmed issuer details, client information, scope, dates, prices, payment terms and validity. Remove irrelevant sections. Do not invent registration, bank, signature or approval details.
5. Edit HTML text in VS Code, save, then refresh the browser. The browser is a preview, not a persistent editor. Encode literal ampersands as `&amp;` and less-than signs as `&lt;`.
6. Recalculate all line amounts, subtotals, the total in words and milestone amounts after price edits. Nothing automatically calculates or synchronizes repeated amounts. Separate hosting or pass-through charges from milestone fees.

Each `<section class="sheet">` is one A4 page. Duplicate a sheet when content grows, update its heading and footer page numbers, and split tables between pages at sensible section boundaries. Keep table headers on each continued table. Do not shrink the type to squeeze in content. A sheet can overflow if too much content is added: inspect print preview after every change.

## Fonts and portability

The shared style uses Montserrat if installed, otherwise Arial/Helvetica. Install Montserrat from its official, licensed distribution for faithful output. The repository does not redistribute font binaries. For a private portable setup, keep the font and its licence in `private/fonts/` and add an `@font-face` rule pointing to it in the private HTML. A client-specific output may already have this rule. Keep the HTML, stylesheet, tokens and font paths together; send the PDF when a single standalone document is needed. Never extract fonts from the original portfolio PDF.

## Export with the browser

Open the HTML in Chrome or Edge, allow fonts to load, then press Ctrl+P. Choose Save as PDF, A4, portrait, 100% scale, no margins (the CSS supplies internal page margins), headers/footers off, background graphics on. Inspect all preview pages. Save under `private/YOUR-PROJECT/`. Browser versions may expose these controls under More settings.

After export, inspect every page for clipping, orphan headings, split rows, extra blank pages, consistent fonts and correct page labels. Verify that the total and terms agree. Test the fallback font if portability matters.

## Optional Windows export

From the repository root, run:

```powershell
powershell -NoProfile -File scripts/export-quotation.ps1 -Html private/YOUR-PROJECT/Quotation.html -Pdf private/YOUR-PROJECT/Quotation.pdf
```

This uses your installed Chrome or Edge in headless mode. It has no Python, Node or AI dependency. It refuses to overwrite an existing PDF; choose a new output filename when exporting revisions. Use `-Browser` to specify another Chrome/Edge executable. A temporary isolated profile is retained at the printed location and can be removed after the browser exits. Always inspect the PDF; the script does not validate finances or visual layout.

## Public repository boundary

Only reusable templates, shared styles, instructions and brand references belong in Git. Keep source research, completed quotations, personal contacts and financial review notes under `private/`. PDF files, private folders and font binaries are ignored. Do not use `git add -f`. Before publishing, run:

```powershell
python -X utf8 scripts/validate_package.py
git status --short
git diff --cached --stat
git diff --cached
git ls-files
git remote -v
```

Inspect the actual staged content. Ignore rules do not protect files already tracked by Git. Keep an independent backup of private outputs because they are deliberately absent from GitHub.
