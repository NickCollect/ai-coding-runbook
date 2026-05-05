---
type: summary
source: 01_Raw/github/anthropics/skills/skills/pptx/editing.md
title: "Editing Presentations (pptx skill)"
summarized_at: 2026-05-05
entities_referenced: [Skill, Subagent]
concepts_referenced: []
---

Reference doc within the `pptx` skill. Covers template-based editing workflow for `.pptx` files.

**7-step template workflow**:
1. **Analyze**: `python scripts/thumbnail.py template.pptx` (visual grid) + `python -m markitdown template.pptx` (placeholder text).
2. **Plan slide mapping**. ⚠️ USE VARIED LAYOUTS — repeating bullet slides is the #1 failure mode. Actively use multi-column, image+text, full-bleed image w/ overlay, quotes, section dividers, stat callouts, icon grids.
3. **Unpack**: `python scripts/office/unpack.py template.pptx unpacked/`.
4. **Build presentation** (do yourself, NOT subagents): delete unwanted slides (remove from `<p:sldIdLst>`), duplicate via `add_slide.py`, reorder. **Complete all structural changes BEFORE step 5.**
5. **Edit content** in each `slide{N}.xml`. **Use subagents in parallel here if available** — separate XML files allow parallel editing.
6. **Clean**: `python scripts/clean.py unpacked/` (remove orphaned files, unreferenced media).
7. **Pack**: `python scripts/office/pack.py unpacked/ output.pptx --original template.pptx`.

**Bundled scripts**:
- `unpack.py` — extract + pretty-print + escape smart quotes.
- `add_slide.py` — duplicate slide or create from layout. Prints `<p:sldId>` to add to `<p:sldIdLst>`.
- `clean.py` — remove unreferenced files.
- `pack.py` — validates, repairs, condenses XML, re-encodes smart quotes.
- `thumbnail.py` — JPG grid (default 3 cols, max 12 per grid). For template analysis ONLY — for visual QA use `soffice` + `pdftoppm` for full-resolution.

**Slide order** lives in `ppt/presentation.xml` `<p:sldIdLst>`. Reorder by rearranging `<p:sldId>`. Delete by removal + `clean.py`. Add only via `add_slide.py` — never manually copy slide files (handles notes refs, Content_Types.xml, relationship IDs).

**Subagent prompt** (when using parallel edits) MUST include: target slide file paths, "Use the Edit tool for all changes", formatting rules + common pitfalls.
