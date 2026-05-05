---
type: summary
source: 01_Raw/github/anthropics/claude-quickstarts/autonomous-coding/README.md
source_url: https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/README.md
title: "Claude Quickstarts — autonomous-coding README"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Sandboxing, Hooks]
concepts_referenced: [Agentic-loop]
---

Minimal harness demonstrating long-running autonomous coding with the Claude Agent SDK. Implements a two-agent pattern (initializer + coding agent) that builds complete applications across multiple sessions.

**Prerequisites.** Latest `@anthropic-ai/claude-code` (`npm install -g`) and Python deps (`pip install -r requirements.txt`). Verify with `claude --version` and `pip show claude-code-sdk`. Set `ANTHROPIC_API_KEY`.

**Quick start.** `python autonomous_agent_demo.py --project-dir ./my_project`. For testing: `--max-iterations 3`.

**Timing.** First session generates a `feature_list.json` with 200 test cases — takes several minutes and may appear to hang (it is writing all features). Each subsequent coding iteration takes 5–15 minutes. Building all 200 features can take many hours of total runtime across multiple sessions. Reduce features in `prompts/initializer_prompt.md` (e.g., 20–50) for faster demos.

**How it works.** Two-agent pattern:

1. **Initializer (Session 1).** Reads `app_spec.txt`, creates `feature_list.json` with 200 test cases, sets up project structure, initializes git.
2. **Coding Agent (Sessions 2+).** Picks up where the previous session left off, implements features one by one, marks them passing in `feature_list.json`.

Session management: each session runs with a fresh context window; progress persists via `feature_list.json` and git commits; the agent auto-continues between sessions (3 second delay); Ctrl+C pauses and the same command resumes.

**Security model (defense in depth, in `security.py` and `client.py`):**

1. **OS-level sandbox** — Bash commands run in an isolated environment.
2. **Filesystem restrictions** — file operations restricted to the project directory.
3. **Bash allowlist** — only specific commands permitted: file inspection (`ls`, `cat`, `head`, `tail`, `wc`, `grep`), Node.js (`npm`, `node`), version control (`git`), process management (`ps`, `lsof`, `sleep`, `pkill` for dev processes only). Commands not in the allowlist are blocked by the security hook.

The README continues with project structure, customization tips, and troubleshooting.
