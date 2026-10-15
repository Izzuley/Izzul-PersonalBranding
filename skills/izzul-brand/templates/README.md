# Template guidance

These are **working starter files**, not finalized legal or clinical documents. HTML prototypes can be opened in a browser and printed/exported to PDF; Markdown templates serve as content architecture/generation prompts.

| Template | Intended use | Notes |
|---|---|---|
| `quotation.html` | A4 customer quotation | User supplies currency, amounts, client, scope, validity, payment terms |
| `quotation-allocations.html` | A4 development, infrastructure and maintenance quotation | Separate issuer/representative, one-time and recurring fees, cloud consumption, support limits and reconciliation |
| `proposal.html` / `proposal.md` | A4 proposal | Business value first, explicit acceptance criteria and exclusions |
| `technical-report.html` / `technical-report.md` | Research/ML report | Validation/evaluation/limitations, not unverified medical conclusions |
| `presentation.html` / `presentation.md` | 16:9 slides | Slide-style HTML; browser print to PDF; not a `.pptx` master |
| `website-starter.html` / `website.md` | Visual mockup and integration guide | Non-invasive integration guidance; **not** a replacement for existing site |

### Customizing and exporting

1. Copy the selected template and keep its stylesheet paths valid. Quotations use `quotation.css`, which imports `../references/design-tokens.css`; other templates link directly to the token file. See [the quotation workflow](../../../docs/quotation-workflow.md) for private output paths and export settings.
2. Replace every `[PLACEHOLDER]`, including client and financial terms. Treat demo CSS colors as provisional tokens.
3. Open the HTML locally in a browser and inspect. Print with **background graphics enabled** to preserve navy/gold covers.
4. For websites, import tokens into the current app theme. The sample has no backend, build framework or routing.
5. Review exports visually, check mobile/print and data privacy. A static preview is not evidence of regulatory/legal compliance.

**No font binaries, no real client data, no invented case studies or logos are included.**
