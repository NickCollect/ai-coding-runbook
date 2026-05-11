---
source_url: https://platform.claude.com/docs/en/api/compliance/apps/artifacts/content
fetched_at: 2026-05-11T04:55:30.341557+00:00
fetch_method: mintlify_md
---

## Content

**get** `/v1/compliance/apps/artifacts/{artifact_version_id}/content`

Download the content of an artifact version for compliance purposes.

Returns the full text content of the artifact version.

### Path Parameters

- `artifact_version_id: string`

  The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```
