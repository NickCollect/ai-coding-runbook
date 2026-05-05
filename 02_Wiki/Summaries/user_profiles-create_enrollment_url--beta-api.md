---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url.md
source_url: https://platform.claude.com/docs/en/api/beta/user_profiles/create_enrollment_url
title: "Create User-Profile Enrollment URL"
summarized_at: 2026-05-05
entities_referenced: [User-profile]
concepts_referenced: []
---

`POST /v1/user_profiles/{user_profile_id}/enrollment_url` — generate an enrollment URL the end-user can visit to complete linking/enrollment for this profile.

**Path param:** `user_profile_id`. No documented body. Returns the generated URL (typically with a short-lived token embedded). Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
