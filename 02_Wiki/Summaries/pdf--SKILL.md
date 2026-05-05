---
type: summary
source: 01_Raw/github/anthropics/skills/skills/pdf/SKILL.md
title: "pdf (Anthropic Skills)"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Skill for PDF processing — read, extract text/tables, merge, split, rotate, watermark, create, fill forms, encrypt/decrypt, extract images, OCR scanned PDFs. References sibling docs: `REFERENCE.md` for advanced features + JS libraries; `FORMS.md` for form filling.

**Python libraries**:
- **`pypdf`** — basic ops:
  - Read: `PdfReader("doc.pdf")`, iterate `reader.pages` and call `page.extract_text()`.
  - Merge: `PdfWriter()` + add each `reader.pages` from each input PDF, then `writer.write()`.
  - Split: per-page `PdfWriter` + `add_page` + write `page_N.pdf`.
  - Metadata: `reader.metadata.title`/`author`/`subject`/`creator`.
  - Rotate: `page.rotate(90)` then add to new writer.
- **`pdfplumber`** — text + table extraction:
  - Text with layout: `with pdfplumber.open(...) as pdf` → iterate `pdf.pages` → `page.extract_text()`.
  - Tables: `page.extract_tables()` returns nested lists.
  - Combined with `pandas` for `DataFrame` + Excel export.

(Skill body continues with watermarks, OCR, form filling, JS libraries via REFERENCE.md.)
