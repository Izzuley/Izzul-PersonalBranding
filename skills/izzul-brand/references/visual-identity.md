# Visual identity: measured source → practical system

**Visual reference:** owner's 16-page Canva PDF `Portfolio_Izzul.pdf`, inspected at full-page scale (1–16).  
**Status:** observed design patterns + **provisional** derived tokens, **not official Canva colors**.

## 1. What is visibly present

- **Format:** tall A4 portrait pages, mostly full-bleed deep indigo/night-navy background (pp. 1–15). Page 16 closes on full-width personal portrait with white overlay type.
- **Dominant palette:** dark royal navy/indigo, bright yellow-gold hierarchy, white supporting copy; lavender/pink-violet luminous folds/ribbon overlays; mid-indigo translucent media and structural accents.
- **Typography:** Montserrat embedded in PDF (`Regular`, `Bold`, `BoldItalic`, `Italic`). Oversized uppercase cover title, smaller all-caps section headings, extra tracking in names, subtitles and some body lines.
- **Layout:** near-full-bleed branded field; slim gold horizontal rules on cover; fine upper-center gold vertical line on section pages; upper-centered headings; mixed left-aligned compact text blocks; edge-cropped overlapping photographs and translucent geometric shapes. Some spreads display torn-edge/clipped image crops.
- **Graphic vocabulary:** flowing lavender/violet ribbon/wave across corners/footers (pp. 1–3, 5–7, 10, 13–15); subtle technical/architectural linework; gold rules; visual evidence photos; diagonal image crops; **no standalone personal logo confirmed**.
- **Photo direction:** real talks, research and competitions, award portraits, groups and sport; evidence-led rather than generic stock photography (pp. 1–3, 7–9, 11–16). Permissions for any public publishing are not established by the PDF.

## 2. Derived palette and confidence

The following are **production approximations** sampled/selected against a rendered JPG copy of the PDF, not exact original Canva source colors; anti-aliasing, lighting and compression change pixels. All should remain editable until owner approval.

| Design token | Working value | Confidence | Use |
|---|---|---|---|
| `--izzul-navy` | `#100B4D` | approximate sampled background (pp. 1–15) | dark cover, hero and main headings |
| `--izzul-navy-deep` | `#0E094B` | approximate sampled background (p. 1 upper-left and recurring pages) | overlays/gradient |
| `--izzul-gold` | `#F8DE63` | sampled displayed heading highlight (multiple section pages) | dark cover headings, separators and slim accents |
| `--izzul-violet` | `#9041B8` | sampled decorative wave (p. 10 bottom) | tertiary decorative use, not tiny text |
| `--izzul-lavender` | `#C786E0` | sampled decorative wave (p. 1 lower-left) | restrained decor only |
| `--izzul-white` | `#FFFFFF` | observed white/light type | body surfaces / reversed headlines |
| `--izzul-paper` | `#F8F9FC` | **new recommendation**, not observed source | softer document canvas |
| `--izzul-ink` | `#1E2140` | **new recommendation**, not observed source | print/web body copy |
| `--izzul-muted` | `#5F6375` | **new recommendation**, not observed source | metadata |

**Color integrity:** `navy` / `gold` carry recognition; violet is an *optional motif*, not a competing primary. Never set gold body copy on white. Use gold as line/shape on white or as type against deep navy only. Do not rely on hue alone for interpreting graphs, alerts or QA status.

## 3. Typography and hierarchy

- Family: **Montserrat** (PDF-verified). The repo uses a system fallback rather than shipping a licensed font binary. Install/source Montserrat independently to reproduce exactly.
- Personal brand identity: use the full professional name in text. **No fabricated monogram or official logo.**
- Main page/slide title: Montserrat Bold, strong hierarchy; uppercase may fit covers and chapter pages.
- Section headings: Montserrat Bold; permit uppercase + 0.04–0.08em tracking, but not 1+ letter gaps on dense reporting pages.
- Body: Montserrat Regular, sentence case, standard kerning and line-height; aim 16px+ on web, 10–11pt+ on print, 20px+ on slides as context permits.
- Dense technical sections: prioritize tables, indentation, bullets and visual hierarchy over giant tracked uppercase typography.

## 4. Usage by context

| Context | Keep from PDF | Adapt |
|---|---|---|
| Website hero / about | navy field, gold line, approved image | adequate contrast, fast/mobile-responsive text, simpler violet corners |
| Personal showcase / speaking slides | dark title cards, media evidence | fewer collages, larger text, sourced charts |
| Formal quotation | navy identity, fine gold rule | **white A4 page**, clearly defined scope/pricing/validity |
| Consulting proposal | navy and gold hierarchy | client problem first, sections and whitespace |
| Scientific report | navy section heads, modest accents | mostly white, reproducible figures, data tables, method details |
| Research talk / pitch | strong dark cover | light content slides, legible charts, clear limitations |

## 5. Components (recommended, not observed as an actual component library)

- Text name header (no logo claim)
- Eyebrow label and headline
- Thin gold separator line
- Plain evidence/case-study card
- Project scope table
- Accessible metric row (with denominators and sources)
- Research figure caption and limitations callout
- Lavender decorative corner, **only where there is whitespace**

## 6. Common mistakes to avoid

1. Reproducing the PDF's visually dense pages in formal proposals and reports.
2. Blending portfolio name typography into paragraph body text, causing poor readability.
3. Using gold on white for important small text.
4. Adding random blues, neon tech gradients or OrynLab's dot mark/Poppins.
5. Equating decorative themes with medical reliability; medical decisions need evidence, not appearance.
6. Presenting the illustrative palette swatch as an official logo or final approved brand.

## 7. Traceability

`references/source-provenance.md` inventories every page; `assets/palette-reference.svg` is a non-official vector illustration of the derived system. No copyrighted fonts or original PDF portraits are bundled.
