---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/git/README.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/git/README.md
title: "Git MCP server (read/search/manipulate git repos)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Python MCP server for git repository interaction and automation. Registry: `io.github.modelcontextprotocol/server-git`. Currently in early development — functionality and tools subject to change.

**Tools** (all take `repo_path` as first argument):
- `git_status` — working tree status
- `git_diff_unstaged(context_lines=3)` — unstaged changes
- `git_diff_staged(context_lines=3)` — staged changes
- `git_diff(target, context_lines=3)` — diff vs branch/commit
- `git_commit(message)` — record changes (returns new commit hash)
- `git_add(files: string[])` — stage files
- `git_reset` — unstage all staged changes

(Additional tools beyond this excerpt likely include: `git_log`, `git_create_branch`, `git_checkout`, `git_show`, `git_init`, etc. — see source for full list.)

**Caveat**: per MCP's security trust model (see `SECURITY--mcp-spec`), giving an AI agent unrestricted access to git tools is intentional behavior — you can do destructive operations (force push, reset, etc.) so deploy with appropriate guardrails.
