---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/file-checkpointing.md
source_url: https://code.claude.com/docs/en/agent-sdk/file-checkpointing
title: "Rewind file changes with checkpointing"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Checkpointing, Permission-mode]
concepts_referenced: []
---

Documents the Agent SDK's file checkpointing system, which tracks modifications made via `Write`, `Edit`, and `NotebookEdit` so files can be rewound to any previous state. Bash-mediated changes (`echo > file`, `sed -i`) are NOT tracked — important caveat.

**How it works**: Before any tracked tool modifies a file, the SDK backs up the original content. Each `UserMessage` in the response stream carries a `uuid` that doubles as a checkpoint identifier. Calling `rewindFiles(uuid)` (TS) / `rewind_files(uuid)` (Python) restores files on disk — created files are deleted, modified files revert to their snapshot at that point. **The conversation history is NOT rewound** — only files on disk.

**Enable**: set both `enableFileCheckpointing: true` AND `extraArgs: { "replay-user-messages": null }` (Python: `enable_file_checkpointing=True`, `extra_args={"replay-user-messages": None}`). The `replay-user-messages` flag is required to receive the UUIDs in the stream. Typically combined with `permissionMode: "acceptEdits"` so file edits don't prompt.

**Capture pattern**: iterate the stream, capture `message.uuid` on the first `UserMessage` (full restore point) and `message.session_id` on the `ResultMessage` (needed only if rewinding after the stream completes).

**Rewind pattern**: After the stream ends, resume the session with an empty prompt to reopen the connection, then call rewind once and break:

```python
async with ClaudeSDKClient(
    ClaudeAgentOptions(enable_file_checkpointing=True, resume=session_id)
) as client:
    await client.query("")
    async for message in client.receive_response():
        await client.rewind_files(checkpoint_id)
        break
```

CLI alternative: `claude -p --resume <session-id> --rewind-files <checkpoint-uuid>`.

**Patterns**:
- *Checkpoint before risky operations*: keep only the latest UUID, overwrite each agent turn, rewind on error.
- *Multiple restore points*: store an array of `Checkpoint{id, description, timestamp}` to support partial undo (e.g. keep refactor, undo tests).

**Limitations**: only Write/Edit/NotebookEdit tracked, checkpoints scoped to their session, file content only (directory creation/move/delete not undone), local files only.

**Common errors**:
- "User messages don't have UUIDs" → missing `replay-user-messages` flag.
- "No file checkpoint found for message" → checkpointing wasn't enabled on the original session, or session not completed before resume.
- "ProcessTransport is not ready for writing" → tried rewinding after stream closed; must resume with empty prompt first.
