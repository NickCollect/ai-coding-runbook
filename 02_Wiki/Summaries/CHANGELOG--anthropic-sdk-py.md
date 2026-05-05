---
type: summary
source: 01_Raw/github/anthropics/anthropic-sdk-python/CHANGELOG.md
source_url: https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md
title: "Anthropic SDK Python — CHANGELOG"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-Python, Memory-tool, Managed-agent, User-profile, Streaming-API, Advisor-tool, Enterprise-gateway]
concepts_referenced: []
---

Changelog of the `anthropic` Python SDK. Recent significant entries:

**0.97.0 (2026-04-23).** New API feature: CMA Memory public beta. Bug fixes for spec errors and restored missing features. Performance: optimized file structure copying in multipart requests.

**0.96.0 (2026-04-16).** Added `claude-opus-4-7`, token budgets, and `user_profiles` to the API surface.

**0.95.0 (2026-04-14).** Marked Sonnet and Opus 4 models as deprecated. Bedrock: switched mantle client to use auth header.

**0.94.1 (2026-04-13).** Streaming bug fix — added missing events.

**0.94.0 (2026-04-10).** Vertex EU region support. Bug fix to ensure file data is sent as a single parameter. Documentation example improvements.

**0.93.0 (2026-04-09).** Added beta advisor tool support.

**0.92.0 (2026-04-08).** Added support for Claude Managed Agents.

**0.91.0 (2026-04-07).** Created Bedrock Mantle client.

**0.90.0 (2026-04-07).** Added support for `claude-mythos-preview`. Bug fix preserving hardcoded query params when merging with user params.

The file is auto-generated alongside each release-please cut. Earlier entries (0.89.0 and below) extend through the 0.x line, but the entries above represent the headline feature additions and breaking changes from the most recent month of releases.
