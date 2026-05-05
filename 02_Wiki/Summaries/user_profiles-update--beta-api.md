---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/user_profiles/update.md
source_url: https://platform.claude.com/docs/en/api/beta/user_profiles/update
title: "Update User Profile"
summarized_at: 2026-05-05
entities_referenced: [User-profile]
concepts_referenced: []
---

`POST /v1/user_profiles/{user_profile_id}` — patch an existing user profile.

**Path param:** `user_profile_id`. **Optional body params:** `external_id`, `metadata`. Returns the updated profile. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
