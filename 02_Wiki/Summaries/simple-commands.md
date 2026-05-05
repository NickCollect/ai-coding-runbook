---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/command-development/examples/simple-commands.md
title: "Simple Command Examples"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Plugin]
concepts_referenced: []
---

Cookbook of 10 simple slash command patterns for `.claude/commands/`. Critical guidance: **commands are written FOR Claude (agent consumption), not for users** — they tell Claude what to do, not narrate to the user.

**Examples covered** (each with frontmatter + body):
1. `/review` — code review for quality/issues/best-practices, allowed-tools `Read, Bash(git:*)`.
2. `/security-review` — OWASP-style scan with severity prioritization, `model: sonnet`.
3. `/test-file [test-file]` — run tests for specific file, `argument-hint: [test-file]`, uses `$1` substitution + `` !`npm test $1` `` for context.
4. `/document [source-file]` — generate JSDoc-style docs, uses `@$1` to pull file content.
5. `/git-status` — repo status summary, multiple `` !`git ...` `` injections (branch, status, log, fetch).
6. `/deploy [environment] [version]` — kubectl deployment workflow with pre-deploy checks.
7. `/compare-files [file1] [file2]` — diff analysis using `@$1` and `@$2`.
8. `/quick-fix [issue-description]` — `model: haiku` for simple fixes, uses `$ARGUMENTS`.
9. `/research [topic]` — best-practices research with industry comparison.
10. `/explain [file-or-function]` — line-by-line walkthrough at junior-engineer level.

**Patterns extracted**:
- Read-only analysis: `allowed-tools: Read, Grep`.
- Git operations: `allowed-tools: Bash(git:*)` + `` !`git status` `` injection.
- Single-arg: `argument-hint: [target]` + `$1`.
- Multi-arg: `argument-hint: [source] [target] [options]` + `$1`/`$2`/`$3`.
- Fast execution: `model: haiku`.
- Context gathering: combine `` !`...` `` injections with `@filename` references.

Tips: start basic; single responsibility; use `argument-hint` for autocomplete; descriptive names; handle missing args.
