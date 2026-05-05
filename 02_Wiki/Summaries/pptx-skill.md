---
type: summary
source: 01_Raw/github/anthropics/skills/skills/pptx/SKILL.md
title: "anthropics/skills: pptx SKILL.md"
summarized_at: 2026-05-05
entities_referenced: [Skill, Subagent]
concepts_referenced: []
---

Skill for any task involving `.pptx` files: create/read/edit decks, extract text, work with templates/layouts/speaker notes/comments.

**Quick reference**:
- Read/analyze content → `python -m markitdown presentation.pptx`.
- Edit / create from template → read `editing.md`.
- Create from scratch → read `pptxgenjs.md`.

**Reading content**:
- Text: `python -m markitdown presentation.pptx`.
- Visual overview: `python scripts/thumbnail.py presentation.pptx`.
- Raw XML: `python scripts/office/unpack.py presentation.pptx unpacked/`.

**Design philosophy** ("Don't create boring slides"):
- Pick bold content-informed color palette (would not work swapped into different topic).
- Dominance over equality: one color 60-70% weight, 1-2 supporting, one sharp accent.
- Dark/light contrast: dark for title+conclusion, light content (sandwich).
- Commit to a visual motif (rounded image frames, icons in colored circles, thick single-side borders).

**Provided color palettes** (10): Midnight Executive, Forest & Moss, Coral Energy, Warm Terracotta, Ocean Gradient, Charcoal Minimal, Teal Trust, Berry & Cream, Sage Calm, Cherry Bold — each with primary/secondary/accent hex codes.

**Per-slide rules**: every slide needs visual element; layout options (two-column, icon+text rows, 2x2/2x3 grid, half-bleed image with overlay); data display patterns (large stat callouts 60-72pt, comparison columns, timelines).

**Typography**: pick interesting font pairing (NOT Arial). Examples: Georgia/Calibri, Arial Black/Arial, Cambria/Calibri. Sizes: title 36-44pt bold, section header 20-24pt bold, body 14-16pt, captions 10-12pt muted.

**Spacing**: 0.5" margins, 0.3-0.5" between blocks, leave breathing room.

**Avoid common mistakes**: same layout repeated, centered body text (only center titles), insufficient size contrast, default blue, mixed spacing, partial styling, text-only slides, missing text-box padding, low-contrast elements, **NEVER accent lines under titles** (AI-slop hallmark).

**QA section is REQUIRED** ("Assume there are problems. Your job is to find them. First render is almost never correct.").

**Content QA**: `python -m markitdown output.pptx` — check for missing content, typos, wrong order, leftover placeholder text (`grep -iE "xxxx|lorem|ipsum"`).

**Visual QA**: ⚠️ **USE SUBAGENTS even for 2-3 slides** — fresh eyes catch what tired eyes miss. Convert pptx → images, give subagent detailed prompt: look for overlapping elements, text overflow, decorative lines on wrapped titles, source citations colliding, uneven gaps, low contrast, text boxes too narrow, leftover placeholder.

**Conversion to images**: `python scripts/office/soffice.py --headless --convert-to pdf output.pptx` then `pdftoppm -jpeg -r 150 output.pdf slide`. Re-render specific: `pdftoppm -jpeg -r 150 -f N -l N output.pdf slide-fixed`.

**Verification loop**: generate → convert → inspect → list issues → fix → re-verify → repeat. **Do not declare success until at least one fix-and-verify cycle.**

**Dependencies**: `markitdown[pptx]`, `Pillow`, `pptxgenjs` (npm), LibreOffice `soffice`, Poppler `pdftoppm`.
