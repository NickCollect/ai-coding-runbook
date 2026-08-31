---
source_url: https://platform.claude.com/docs/en/api/files/download
fetched_at: 2026-08-31T06:29:36.767855+00:00
fetch_method: mintlify_md
---

# Download File

**GET** `/v1/files/{file_id}/content`

Download File

## Path parameters

- `file_id: string`

  ID of the File.

## Example

```bash
curl https://api.anthropic.com/v1/files/$FILE_ID/content \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```
