---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool
title: "Bash tool"
summarized_at: 2026-05-05
entities_referenced: [Bash-tool-API, Tool-use, Code-execution-tool, Text-editor-tool]
concepts_referenced: []
---

The [[Bash-tool-API]] enables Claude to execute shell commands in a persistent bash session—a foundational agent capability. On Terminal-Bench 2.0 (real-world terminal tasks with shell-only validation), Claude shows strong performance gains with access to a persistent bash session. **Eligible for ZDR.**

This is a *client-side* tool: the API returns `tool_use` blocks; **your application** is responsible for executing the command and maintaining shell session state. The API itself is stateless.

**Capabilities.** Persistent bash session that maintains state (env vars, working directory) across commands; ability to run any shell command; command chaining and scripting.

**Use cases.** Development workflows (build, test); system automation (scripts, file management); data processing; environment setup (package install).

**Tool definition.** Schema-less tool. The schema is built into the model and cannot be modified.
```json
{"type": "bash_20250124", "name": "bash"}
```

**Parameters.** `command` (required unless restarting): the bash command. `restart` (optional): set to `true` to restart the bash session.

**Implementation pattern.** Wrap a `subprocess.Popen(["/bin/bash"], ...)` and pipe commands through stdin while reading stdout/stderr asynchronously. On each `tool_use` block from the API: if `restart` is true call `bash_session.restart()`, else execute `command` and return output as a `tool_result`.

**Safety.** Use an *allowlist* (e.g. `{"ls", "cat", "echo", "pwd", "grep", "find", "wc", "head", "tail"}`) rather than a blocklist (easy to bypass). Reject shell operators (`&&`, `||`, `|`, `;`, `&`, `>`, `<`, `>>`) and `$`/`` ` `` prefixes that could chain commands or substitute values past the allowlist. For stronger isolation, run with `shell=False` and pass `shlex.split(command)` so the shell never interprets the string.

**Error handling.** Return errors as `tool_result` with `is_error: true`. Common cases: command timeout (`Command timed out after 30 seconds`), command not found, permission denied. Implement `subprocess.run(..., timeout=30)` to prevent hanging commands.

**Best practices.**
- *Maintain session state*: a persistent session keeps env vars and `cd` changes alive across commands.
- *Truncate large outputs* (e.g. >100 lines) to prevent context blowup—prepend "... Output truncated (N total lines) ..." marker.
- *Log all commands* with user_id for audit trail.
- *Sanitize outputs*: regex-strip secrets like `aws_access_key_id` before returning.

**Security.** Direct system access requires defense-in-depth: run inside Docker/VM; allowlist commands; set `ulimit` resource constraints; filter dangerous commands (`sudo`, `rm -rf`); minimal user permissions; log everything.

**Pricing.** The bash tool adds **245 input tokens** to API calls. Additional tokens come from command outputs (stdout/stderr), error messages, and large file contents.

**Common patterns:**
- Dev workflows: `pytest && coverage report`; `npm install && npm run build`.
- *Git-based checkpointing for long agent workflows:* commit the baseline before any agent work; commit per feature for rollback points; reconstruct state at session start by reading `git log` plus a progress file; on failure `git checkout` reverts to the last good commit.
- File ops: `find . -name "*.py" | xargs grep "pattern"`, `tar -czf backup.tar.gz ./data`.
- System tasks: `df -h && free -m`, `ps aux | grep python`.

**Limitations.** No interactive commands (no `vim`, `less`, password prompts); no GUI applications; **session scope is client-side** (the API is stateless—your app maintains the shell between turns); large outputs may be truncated; results returned only after completion (no streaming).

**Combining with other tools.** Most powerful with the [[Text-editor-tool]]. If using alongside the [[Code-execution-tool]], Claude has *two separate execution environments*: your local bash session and Anthropic's sandboxed container. State is not shared between them. Add system-prompt instructions distinguishing the two environments to prevent Claude from confusing them.
