---
type: summary
source: 01_Raw/github/anthropics/skills/skills/pptx/pptxgenjs.md
title: "PptxGenJS Tutorial (pptx skill reference)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Tutorial for `pptxgenjs` (Node library for generating .pptx files) from the `pptx` skill reference. Note: only first ~80 lines sampled.

**Setup**:
```javascript
const pptxgen = require("pptxgenjs");
let pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';  // or LAYOUT_16x10, LAYOUT_4x3, LAYOUT_WIDE
pres.author = 'Your Name';
pres.title = 'Presentation Title';
let slide = pres.addSlide();
slide.addText("Hello World!", { x: 0.5, y: 0.5, fontSize: 36, color: "363636" });
pres.writeFile({ fileName: "Presentation.pptx" });
```

**Layouts** (inches):
- `LAYOUT_16x9`: 10" × 5.625" (default)
- `LAYOUT_16x10`: 10" × 6.25"
- `LAYOUT_4x3`: 10" × 7.5"
- `LAYOUT_WIDE`: 13.3" × 7.5"

**Text + formatting**:
- Basic: `addText("...", { x, y, w, h, fontSize, fontFace, color, bold, align, valign })`
- **Character spacing**: use `charSpacing`, NOT `letterSpacing` (silently ignored)
- **Rich text** via array: `[{text, options: {bold: true}}, ...]`
- **Multi-line**: requires `breakLine: true` on each item except last
- **Internal margin**: text boxes have default margin; set `margin: 0` to align text with shapes/lines/icons

**Lists/bullets**:
- ✅ correct: `[{text, options: {bullet: true, breakLine: true}}, ...]`
- ❌ wrong: `slide.addText("• First item", ...)` — creates double bullets
- Sub-items: `bullet: true, indentLevel: 1`
- Numbered: `bullet: { type: "number" }`

(Remainder covers shapes, images, charts, tables, slide transitions, etc. — not sampled.)
