---
type: summary
source: 01_Raw/github/anthropics/skills/skills/pdf/reference.md
title: "PDF processing advanced reference"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Advanced reference inside the `pdf` skill (`anthropics/skills`). Covers libraries and command-line operations beyond the SKILL.md basics. The skill itself does PDF reading/extraction/merging/splitting/OCR/form filling/encryption operations.

**Python libraries**:
- **pypdfium2** (Apache/BSD) — PDFium binding for fast rendering + image generation. `pdf = pdfium.PdfDocument(...)`, `page.render(scale=, rotation=)`, `bitmap.to_pil().save(...)`. Replacement for PyMuPDF.
- **pdfplumber** — text extraction with **precise coordinates** (`page.chars`, `page.within_bbox(...)`), advanced table extraction with custom settings (`vertical_strategy`, `snap_tolerance`, `intersection_tolerance`), visual debugging via `page.to_image(resolution=150).save(...)`.
- **reportlab** — `SimpleDocTemplate`, `Table` with `TableStyle` for professional reports.
- **pypdf** — `PdfReader` / `PdfWriter` for batch ops, page cropping (`page.mediabox.left/bottom/right/top`).

**JavaScript libraries**:
- **pdf-lib** (MIT) — create + modify PDFs in any JS env. Load existing → add page → draw text/rectangle → save. Supports advanced merge/split (`mergedPdf.copyPages(srcPdf, [0, 2, 4])`).
- **pdfjs-dist** (Apache, Mozilla) — render PDFs in browser via canvas. Extract text WITH coordinates (`item.transform[4]`, `[5]`). Extract annotations and form fields.

**Command-line tools**:
- **poppler-utils**:
  - `pdftotext -bbox-layout document.pdf out.xml` — text + bounding box coords
  - `pdftoppm -png -r 300 doc.pdf prefix` — image conversion (`-f 1 -l 3` for page range, `-jpegopt quality=85` for JPEG)
  - `pdfimages -j -p doc.pdf page_images` — extract embedded images with metadata; `pdfimages -list` to enumerate; `pdfimages -all` for original format
- **qpdf**:
  - `qpdf --split-pages=3 input.pdf output_%02d.pdf`
  - `qpdf input.pdf --pages input.pdf 1,3-5,8,10-end -- extracted.pdf`
  - `qpdf --empty --pages doc1.pdf 1-3 doc2.pdf 5-7 -- combined.pdf`
  - `qpdf --linearize` for web optimization, `--optimize-level=all` for compression
  - `qpdf --check`, `--fix-qdf` for repair
  - Encryption: `qpdf --encrypt user_pass owner_pass 256 --print=none --modify=none -- in.pdf out.pdf`

**Workflows**:
- Figure extraction (pdfimages or pypdfium2 + numpy non-white region detection)
- Batch processing with error handling using glob + try/except
- OCR fallback for scanned PDFs: `pytesseract.image_to_string(convert_from_path(pdf_path)[i])`
- Page cropping via `page.mediabox`
- Memory-managed chunked processing for large PDFs

**Performance tips**:
- Plain text → `pdftotext -bbox-layout` is fastest
- Structured / tables → pdfplumber
- Image extraction → `pdfimages` (much faster than rendering)
- Form filling → pdf-lib preserves form structure best
- Avoid `pypdf.extract_text()` on very large docs

**Troubleshooting**: encrypted PDFs (`reader.is_encrypted` then `reader.decrypt(password)`), corrupted PDFs (`qpdf --check` then `--replace-input`), text extraction failure (fall back to OCR).

License inventory: pypdf BSD, pdfplumber MIT, pypdfium2 Apache/BSD, reportlab BSD, poppler-utils GPL-2, qpdf Apache, pdf-lib MIT, pdfjs-dist Apache.
