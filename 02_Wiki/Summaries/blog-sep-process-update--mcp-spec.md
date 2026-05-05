---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/content/posts/2025-11-28-sep-process-update.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2025-11-28-sep-process-update.md
title: "Blog post: SEPs Are Moving to Pull Requests (2025-11-28)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

David Soria Parra announces the **SEP submission process change**: Specification Enhancement Proposals are no longer GitHub Issues — they're now PRs adding files to the `seps/` directory. Inspired by Python's PEP process.

**Why the change**: with issues, proposal text lived in the issue body while implementation often ended up in a separate PR — splitting discussion across two numbers referring to the same SEP. Issues also lacked file revision history, making it hard to see what changed and when.

**New workflow**:
1. Draft as `0000-your-feature.md` using the SEP template
2. Open a pull request adding the file to `seps/`
3. Once PR exists, rename file using PR number (e.g., `1850-your-feature.md`) and push the rename commit — **the PR number becomes the SEP number**
4. Find a sponsor from the maintainer list to shepherd the proposal
5. Iterate on feedback in the PR

**Status management**: now the **sponsor** updates the `Status` field in the SEP markdown file (in addition to applying PR labels). Same statuses: `Draft` → `In-Review` → `Accepted` → `Final`.

**Migration path for existing issue-based SEPs**: continue with current workflow OR migrate by creating a new markdown SEP, opening a PR, renaming with the new PR number, and closing the original issue with a link to the new PR. New PR gets a fresh SEP number; valuable context from the original discussion should be summarized or linked.

Direct outcome of contributor feedback from the SEP process so far.
