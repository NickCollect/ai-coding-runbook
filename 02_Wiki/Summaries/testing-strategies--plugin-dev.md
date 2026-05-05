---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/command-development/references/testing-strategies.md
title: "plugin-dev: command-development testing-strategies"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command, Hooks, MCP-server]
concepts_referenced: []
---

Reference doc inside `plugin-dev`'s `command-development` skill. Systematic testing approach for slash commands across 7 levels.

**Levels**:
1. **Syntax/structure validation** — YAML frontmatter has 2 `---` markers, file is `.md` extension, file in correct location, not empty. Provided shell scripts (`validate-command.sh`).
2. **Frontmatter field validation** — model is `sonnet`/`opus`/`haiku`; `description` <60 chars (warn at 80); `allowed-tools` present.
3. **Manual command invocation** — appears in `/help`, executes without errors. Use `claude --debug`, watch `~/.claude/debug-logs/latest`.
4. **Argument testing** — test matrix: no args, single, multi, extra, special chars (spaces in quotes), empty.
5. **File reference testing** — `@` syntax loads contents; non-existent files; large files; multiple refs.
6. **Bash execution testing** — `!` commands execute; output included; failures handled; only allowed commands run.
7. **Integration testing** — works with hooks (PreToolUse validates op), with command sequences (state file across commands), with MCP (server starts, tool calls succeed).

**Automated approaches**:
- Test suite script iterating `commands/*.md` running validators.
- Pre-commit git hook validating any changed `.claude/commands/` files.
- CI/CD workflow (GitHub Actions example) running validation across all command files; fail on TODOs.

**Edge cases to test**: empty args (`""`, `'' ''`), special chars (spaces, dashes, underscores, slashes, quotes), long arguments (10000-char input), unusual file paths (`./`, `../`, `~/`, paths with spaces), bash failures (`exit 1`, `false`, nonexistent commands), special outputs (empty echo, `/dev/null`, `yes | head`).

**Performance testing**: response time per run; resource usage (`watch ps aux | grep claude`).

**UX testing**: usability checklist (intuitive name, clear `/help` desc, well-documented args, helpful errors, readable output, progress for long-running, actionable results, edge case UX). User acceptance testing template.

**Pre-release checklist**: structure (location, .md, YAML, markdown), functionality (in /help, executes, args work, file refs, bash), edge cases, integration (other commands, hooks, MCP, state), quality (perf, security, errors, formatting, docs), distribution (peer-tested, README, examples).

**Debugging common issues**: command not in /help → check location/permissions/syntax/restart; args not substituting → check `\$1`/`\$ARGUMENTS` syntax; bash not executing → `allowed-tools` permission; file refs not working → `@` syntax + file exists.

**Best practices**: test early/often, automate validation, test edge cases not just happy path, get feedback before wide release, document scenarios for regression, monitor in production, iterate.
