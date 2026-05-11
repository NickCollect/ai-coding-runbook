---
source_url: https://platform.claude.com/docs/en/api/compliance/apps/chats/files/delete
fetched_at: 2026-05-11T04:55:30.036311+00:00
fetch_method: mintlify_md
---

## Delete

**delete** `/v1/compliance/apps/chats/files/{claude_file_id}`

Permanently deletes a specific file. This is a destructive
operation that cannot be undone.

### Path Parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the file that was deleted

- `type: optional "claude_file_deleted"`

  Constant string confirming deletion

  - `"claude_file_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```
