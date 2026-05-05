---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/typescript/claude-api/files-api.md
title: "claude-api skill: Files API — TypeScript"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

TypeScript Files API reference inside the `claude-api` skill. Same constraints as Python version.

**Beta**: pass `betas: ["files-api-2025-04-14"]` in API calls (SDK sets header automatically).

**Key facts**: max 500 MB per file, 100 GB org total, persist until deleted, ops free + content billed as input tokens, NOT on Bedrock or Vertex.

**Upload**: `client.beta.files.upload({ file: await toFile(fs.createReadStream("report.pdf"), undefined, { type: "application/pdf" }), betas: ["files-api-2025-04-14"] })` returns `{id, size_bytes, ...}`.

**Use in messages** — reference uploaded file:
```ts
{
  type: "document",
  source: { type: "file", file_id: uploaded.id },
  title: "Q4 Report",
  citations: { enabled: true }
}
```

**Manage**:
- `client.beta.files.list({ betas: [...] })` → iterate `.data`.
- `client.beta.files.delete(file_id, { betas: [...] })`.
- `client.beta.files.download(file_id, { betas: [...] })` returns `Response`; convert via `Buffer.from(await response.arrayBuffer())` then write with `fs.promises.writeFile`.
