---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/RELEASE.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/RELEASE.md
title: "Python SDK release process"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Short release process doc.

**Bumping dependencies**: change version in `pyproject.toml` → `uv lock --resolution lowest-direct`.

**Major or minor release**: create a GitHub release via UI with tag `vX.Y.Z` (release title same), then ask someone to review. Package version is set automatically from the tag.
