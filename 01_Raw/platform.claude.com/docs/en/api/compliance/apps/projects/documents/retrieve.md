---
source_url: https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/retrieve
fetched_at: 2026-05-11T04:55:30.291499+00:00
fetch_method: mintlify_md
---

## Retrieve

**get** `/v1/compliance/apps/projects/documents/{document_id}`

Get detailed information for a specific project document.

Returns:
Project document information including content and metadata

### Path Parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Project document identifier (tagged ID)

- `content: string`

  Document text content

- `created_at: string`

  Document creation timestamp

- `filename: string`

  Document filename

- `user: object { id, email_address }`

  User information for project creator.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```
