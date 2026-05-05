---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/python/claude-api/files-api.md
title: "claude-api skill: Files API — Python"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Python Files API reference inside the `claude-api` skill. Files API uploads files for use in Messages API requests; reference via `file_id` in content blocks.

**Beta header**: `files-api-2025-04-14` (SDK sets automatically when you pass `betas=["files-api-2025-04-14"]`).

**Key facts**:
- Max file size: 500 MB.
- Total org storage: 100 GB.
- Files persist until deleted.
- Operations (upload/list/delete) free; content used in messages billed as input tokens.
- **NOT available on Bedrock or Vertex**.

**Upload**: `client.beta.files.upload(file=("name.pdf", open(...), "application/pdf"))` returns object with `id`, `size_bytes`.

**Use in messages** — wrap content block as document:
```python
{
  "type": "document",
  "source": {"type": "file", "file_id": uploaded.id},
  "title": "Q4 Report",                # optional
  "citations": {"enabled": True}        # optional, enables citations
}
```
Or image: `{"type": "image", "source": {"type": "file", "file_id": image_file.id}}`.

**Manage**:
- `client.beta.files.list()` → `files.data` iterable.
- `client.beta.files.retrieve_metadata(file_id)`.
- `client.beta.files.delete(file_id)`.
- `client.beta.files.download(file_id).write_to_file("output.txt")` — only works for files created by code execution tool or skills, NOT user-uploaded files.

**End-to-end pattern**: upload contract.pdf once, ask N questions referencing same `file_id`, delete when done. Avoids re-upload across calls.
