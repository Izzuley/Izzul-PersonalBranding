# Cross-media patterns · production guidance

Use semantic names from `design-tokens.css`; do not set random hex values per document. These are **recommended patterns inspired by the visual source**, not components literally present in its original Canva design.

## Shared elements

1. **Name header:** typographic full name, small role descriptor if approved; never label it “logo”.
2. **Gold hairline:** 2–4px or print-equivalent under page title/cover, but never instead of an actual section label.
3. **Dark cover / hero:** navy background, readable white type, one prominent gold type or rule; violet ribbon optional and low-opacity.
4. **Light content page:** white/off-white, dark readable ink, Montserrat; clear max width, whitespace, tables and captions.
5. **Evidence section:** who/what, method, metric with denominator and date, caveats; no untethered “99% accuracy”.
6. **Client terms/footer:** small but accessible, unobscured by graphics.

## Breakpoints and dimensions

- Web: 320px narrow layouts to desktop, `max-width: 1100px`, proper semantics, visible focus rings, no content relying on hover.
- Quotation/proposals/reports: printable A4 with at least 12–16mm page margins; avoid cutting totals and signatures across pages.
- Presentation: 16:9, font >=20px for dense short sentences when possible; do not transpose original portfolio's tiny lists directly into slides.

## Accessibility

- **Gold on white fails readability as small text**; use as shape only or gold text on navy.
- Navy on white and white on navy are preferred core text combinations.
- Decorative violet background cannot reduce core content contrast; `aria-hidden="true"` for decorative shapes.
- Link appearance needs more than color; focus visible; body size >=16px on screen; print generally >=10pt.
- Prefer SVG/PNG graphs exported at sharp resolution with axes, units and uncertainty explained in nearby prose.

## Website integration

Import `references/design-tokens.css` into the current global CSS or map tokens into its existing theme configuration. **Don't replace existing routes, project pages, scroll navigation, or established components solely to make the demo website match this example.** `templates/website-starter.html` is a styling demonstration, not a mandate to rebuild the site.

## Font delivery

The PDF embeds Montserrat subsets; they are **not copied here**. `font-family: Montserrat, Arial, Helvetica, sans-serif` uses Montserrat if locally installed, otherwise falls back. For web, use the appropriately licensed font through the website's own font pipeline (e.g. next/font), not by embedding restricted binaries in this repo.
