---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/files.md
source_url: https://platform.claude.com/docs/en/managed-agents/files
title: "Adding files"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Files-API, Session-API]
concepts_referenced: []
---

How to provide files to a [[Managed-agent]] by uploading via the [[Files-API]] and mounting them in the session's container. **Requires `managed-agents-2026-04-01` beta header.**

**Two-step process:**

1. **Upload via Files API.** Upload your file (CSV, document, dataset, etc.) using `POST /v1/files`—this returns a `file_id`. SDK example: `client.beta.files.upload(file=Path("data.csv"))`. Same Files API used elsewhere in the platform; works with any file type the agent might need to read.

2. **Mount in session via `resources` array.** When creating a [[Session-API]] session, add the file to the `resources` array:
```json
{
  "agent": "agent_id",
  "environment_id": "env_id",
  "resources": [
    {"type": "file", "file_id": "file_xxx", "mount_path": "/workspace/data.csv"}
  ]
}
```

**`mount_path` is optional.** When omitted, the agent still sees the file but the canonical path is auto-assigned. The doc tip recommends using a descriptive uploaded filename (e.g., `data.csv` not `file_001.csv`) so the agent knows what it's looking for, especially if you skip `mount_path`.

**File availability.** Once the session starts, mounted files appear at the specified `mount_path` (or auto-assigned path) inside the container. The agent can read and process them with bash commands, the Python interpreter, or any of the pre-installed runtimes.

**Pattern.** This page is mostly the upload + mount mechanic—language-specific examples in cURL, ant CLI, Python, TypeScript, C#, Go, Java, PHP, Ruby for both the upload step and the session-create-with-resources step.

The session-side counterpart for *output* files (those the agent creates during execution): writes go to `/mnt/session/outputs/` inside the container, then can be retrieved via `GET /v1/files?scope_id={session_id}` after the session is idle (covered separately in the Define outcomes / Session APIs documentation).
