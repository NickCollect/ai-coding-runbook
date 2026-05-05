---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/user_profiles.md
source_url: https://platform.claude.com/docs/en/api/beta/user_profiles
title: "User Profiles"
summarized_at: 2026-05-05
entities_referenced: [User-profile]
concepts_referenced: []
---

Beta REST resource for **User Profiles** under `/v1/user_profiles`. A user profile represents an end-user identity that an application's calls to the Anthropic API can act on behalf of (referenced via `user_profile_id` on Messages, etc.).

**Endpoints on this page:**

- `POST /v1/user_profiles` — Create (optional `external_id`, `metadata`).
- `GET /v1/user_profiles` — List.
- `GET /v1/user_profiles/{user_profile_id}` — Retrieve.
- `POST /v1/user_profiles/{user_profile_id}` — Update (`external_id`, `metadata`).
- `POST /v1/user_profiles/{user_profile_id}/enrollment_url` — Create Enrollment URL (returns a one-time URL the end-user can visit to enroll/link the profile).

The user-profile feature is gated by the `user-profiles-2026-03-24` beta header. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
