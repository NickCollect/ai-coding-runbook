---
type: summary
source: 01_Raw/github/anthropics/skills/skills/docx/SKILL.md
title: "docx (Anthropic Skills)"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Skill for creating, reading, editing `.docx` Word documents. A `.docx` is a ZIP archive of XML files.

**Quick reference**:
- Read/analyze: `pandoc` or unpack for raw XML.
- Create new: `docx-js` JS library.
- Edit existing: unpack → edit XML → repack.

**Read content**: `pandoc --track-changes=all document.docx -o output.md` for text + tracked changes. Raw XML via `python scripts/office/unpack.py document.docx unpacked/`.

**Convert legacy `.doc` → `.docx`**: `python scripts/office/soffice.py --headless --convert-to docx document.doc`.

**Convert to images**: `soffice.py --convert-to pdf` then `pdftoppm -jpeg -r 150 document.pdf page`.

**Accept tracked changes** (LibreOffice required): `python scripts/accept_changes.py input.docx output.docx`.

**Create new docs** with docx-js — `npm install -g docx`. After creation validate with `python scripts/office/validate.py doc.docx`. If validation fails, unpack/fix XML/repack.

**Page sizing CRITICAL**: docx-js defaults to A4, NOT US Letter. Always set explicit `page.size`. Common sizes in DXA units (1440 DXA = 1 inch):
- US Letter 12240×15840 (content width 9360 with 1" margins).
- A4 (default) 11906×16838.

**Landscape orientation**: docx-js swaps width/height internally — pass PORTRAIT dimensions and set `orientation: PageOrientation.LANDSCAPE`. Content width uses long edge.

**Styles**: use Arial as default font (universally supported). Keep titles black for readability.

(Skill body continues with extensive examples for headings, tables, images, tables of contents, hyperlinks, footnotes, etc.)
