---
source_url: https://platform.claude.com/docs/en/api/files/download
fetched_at: 2026-08-24T02:18:40.775940+00:00
fetch_method: mintlify_md
---

---
title: Download File
url: https://platform.claude.com/docs/en/api/files/download
---

## Download File

**get** `/v1/files/{file_id}/content`

Download File

### Path Parameters

- `file_id: string`

  ID of the File.

### Example

```http
curl https://api.anthropic.com/v1/files/$FILE_ID/content \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```
