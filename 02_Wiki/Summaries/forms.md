---
type: summary
source: 01_Raw/github/anthropics/skills/skills/pdf/forms.md
title: "PDF Forms (pdf skill reference)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Reference doc in the `pdf` skill for filling PDF forms. **Critical**: must complete steps in order — no skipping ahead to writing code.

**Step 0 — Check fillable**: `python scripts/check_fillable_fields.py <file.pdf>`. Branch on result.

**Fillable fields path**:
1. `python scripts/extract_form_field_info.py <input.pdf> <field_info.json>` → JSON with field list. Each field has `field_id`, `page` (1-based), `rect` ([left, bottom, right, top] PDF coords with y=0 at bottom), `type` (`text` / `checkbox` / `radio_group` / `choice`).
   - Checkboxes have `checked_value`, `unchecked_value`
   - Radio groups have `radio_options[]` with `value` + `rect` per option
   - Choices have `choice_options[]` with `value` + `text` per option
2. `python scripts/convert_pdf_to_images.py <file.pdf> <output_directory>` → one PNG per page; analyze visually to determine each field's purpose. Convert PDF coords to image coords.
3. Create `field_values.json` with field_id (must match), description, page, value (for checkboxes use `checked_value` from field_info; for radio use one of `radio_options[].value`).
4. `python scripts/fill_fillable_fields.py <input.pdf> <field_values.json> <output.pdf>` — verifies field IDs and values; prints errors to correct.

**Non-fillable path**: add text annotations. First try to extract coordinates from PDF structure (more accurate), then fall back to visual estimation.

(Remainder covers non-fillable details + edge cases — not sampled.)
