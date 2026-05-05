---
type: summary
source: 01_Raw/github/anthropics/skills/skills/xlsx/SKILL.md
title: "xlsx (anthropics/skills)"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Skill in `anthropics/skills` for spreadsheet workflows (`.xlsx`/`.xlsm`/`.csv`/`.tsv`). Triggers when spreadsheet file is primary input or output (open/read/edit/fix existing, create from scratch, convert tabular formats, clean messy tabular data into proper spreadsheets). Does NOT trigger when primary deliverable is Word doc, HTML report, standalone Python script, DB pipeline, or Google Sheets API integration even if tabular data involved. Note: only first ~80 lines sampled.

**Frontmatter**: `name: xlsx`, `license: Proprietary. LICENSE.txt has complete terms.`

**Output requirements** (all Excel files):
- Professional font (Arial, Times New Roman default)
- **ZERO formula errors** (`#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, `#NAME?`)
- **Preserve existing templates** — match format/style/conventions exactly when modifying; existing template conventions ALWAYS override these guidelines

**Financial models — color coding** (industry-standard):
- Blue text RGB (0,0,255): hardcoded inputs, scenario numbers
- Black text (0,0,0): ALL formulas + calculations
- Green text (0,128,0): cross-worksheet links within same workbook
- Red text (255,0,0): external file links
- Yellow background (255,255,0): key assumptions / cells needing attention

**Number formatting**:
- Years: text strings ("2024" not "2,024")
- Currency: `$#,##0`; specify units in headers ("Revenue ($mm)")
- Zeros: format as "-" via `$#,##0;($#,##0);-`
- Percentages: 0.0% (one decimal)
- Multiples: 0.0x (EV/EBITDA, P/E)
- Negatives: parens `(123)` not minus `-123`

**Formula construction**:
- All assumptions in separate cells (growth, margins, multiples)
- Cell references over hardcoded values: `=B5*(1+$B$6)` not `=B5*1.05`
- Verify cell refs, off-by-one, consistency across periods, edge cases (zero/neg), no unintended circular refs
- Document hardcodes via comments: `Source: [System/Document], [Date], [Specific Reference], [URL]` (e.g., "Source: Company 10-K, FY2024, Page 45, Revenue Note, [SEC EDGAR URL]")

**Tooling**: LibreOffice required for formula recalculation (`scripts/recalc.py`); auto-configures on first run, handles sandboxed envs via `scripts/office/soffice.py`. For data analysis use **pandas**.

(Remainder covers more workflows + tools — not sampled.)
