---
source_url: https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/download
fetched_at: 2026-08-17T02:15:24.820046+00:00
fetch_method: mintlify_md
---

---
title: Download a Claude-generated file
url: https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/download
---

## Download a Claude-generated file

**get** `/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`

Downloads the binary content of a file the assistant created via tool use.

### Path Parameters

- `claude_gen_file_id: string`

  The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude_chat_id}/messages.

### Header Parameters

- `"x-api-key": optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```
