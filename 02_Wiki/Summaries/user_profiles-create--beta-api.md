---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/user_profiles/create.md
source_url: https://platform.claude.com/docs/en/api/beta/user_profiles/create
title: "Create User Profile"
summarized_at: 2026-05-05
entities_referenced: [User-profile]
concepts_referenced: []
---

`POST /v1/user_profiles` — create a new end-user profile.

**Optional body params:** `external_id` (your application's stable ID for the user) and `metadata` (KV map). Returns the created `user_profile` object including its `id`. Requires `user-profiles-2026-03-24` beta header. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
