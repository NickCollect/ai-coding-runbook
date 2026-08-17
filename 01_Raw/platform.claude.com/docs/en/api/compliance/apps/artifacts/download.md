---
source_url: https://platform.claude.com/docs/en/api/compliance/apps/artifacts/download
fetched_at: 2026-08-17T02:15:25.070739+00:00
fetch_method: mintlify_md
---

---
title: Download artifact content
url: https://platform.claude.com/docs/en/api/compliance/apps/artifacts/download
---

## Download artifact content

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
