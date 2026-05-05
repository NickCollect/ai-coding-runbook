---
type: summary
source: 01_Raw/code.claude.com/docs/en/memory.md
source_url: https://code.claude.com/docs/en/memory
title: "How Claude remembers your project"
summarized_at: 2026-05-05
entities_referenced: [Memory, Skill, Subagent, Settings, Hooks]
concepts_referenced: [Context-window]
---

Two memory mechanisms carry knowledge across sessions: **CLAUDE.md** (you write, instructions/rules) and **Auto memory** (Claude writes, learnings/patterns, per-worktree). Both load every session as context (not enforced config).

**CLAUDE.md scopes** (more specific takes precedence):
- Managed policy: `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS), `/etc/claude-code/CLAUDE.md` (Linux/WSL), `C:\Program Files\ClaudeCode\CLAUDE.md` (Win)
- Project: `./CLAUDE.md` or `./.claude/CLAUDE.md`
- User: `~/.claude/CLAUDE.md`
- Local: `./CLAUDE.local.md` (gitignored)

**Loading**: walks up dir tree from cwd → reads each `CLAUDE.md` and `CLAUDE.local.md`. All concatenated (not overriding); ordered filesystem-root → cwd. Within a dir, `CLAUDE.local.md` appended after `CLAUDE.md`. Subdirectory CLAUDE.md files lazy-load when Claude reads files in them. Block-level HTML comments stripped before injection (preserved in code blocks); use to leave maintainer notes.

`--add-dir` files don't load CLAUDE.md unless `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`.

**Effective writing**:
- Target <200 lines per file (longer = worse adherence)
- Markdown headers + bullets (Claude scans structure)
- Specific over vague ("Use 2-space indentation" > "Format properly")
- Periodically review for contradictions across nested files
- `claudeMdExcludes` in settings to skip irrelevant ancestor files (managed policy CLAUDE.md cannot be excluded)

**`@import` syntax**: `@README`, `@docs/git-instructions.md`, `@~/.claude/my-project-instructions.md` (cross-worktree share). Recursive max depth 5. Relative paths resolve to file location, not cwd. First-time external imports trigger approval dialog; if declined, stays disabled silently.

**`AGENTS.md`**: Claude Code reads CLAUDE.md only. Bridge by creating CLAUDE.md with `@AGENTS.md` import + Claude-specific additions below.

**`/init`**: auto-generates starting CLAUDE.md by analyzing codebase. With existing file, suggests improvements rather than overwriting. `CLAUDE_CODE_NEW_INIT=1` enables interactive multi-phase flow (asks which artifacts: CLAUDE.md/skills/hooks → subagent codebase explore → reviewable proposal).

**`.claude/rules/`**: modular `.md` files alongside CLAUDE.md, recursive subdirs OK. Without `paths` frontmatter, loaded at launch like CLAUDE.md. With `paths:` frontmatter (glob patterns like `src/**/*.{ts,tsx}`), only loads when Claude reads matching file. User-level `~/.claude/rules/` loads BEFORE project rules (project = higher priority). Symlinks supported (circular detected).

**For task-specific instructions that don't need to always be in context**, use **skills** instead of rules — skills only load when invoked or when Claude determines relevance.

**Auto memory** (v2.1.59+, on by default):
- Storage: `~/.claude/projects/<project>/memory/` — derived from git repo, all worktrees + subdirs share. Outside git, project root used.
- Customize via `autoMemoryDirectory` in user settings (must be absolute or `~/`-prefixed). Only accepted from user/policy/`--settings`, NOT project/local (security: cloned repo could redirect writes to sensitive paths).
- Layout: `MEMORY.md` index (loaded each session up to 200 lines / 25 KB) + topic files (`debugging.md`, etc., on-demand only).
- Toggle via `/memory` UI or `autoMemoryEnabled: false` in project settings; disable globally with `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`. Set to `0` to force on during gradual rollout.
- Machine-local; not shared across machines/cloud envs. Worktrees of same repo share.
- Plain markdown — edit/delete freely. UI shows "Writing memory" / "Recalled memory" when Claude is reading/writing.

**Subagents** can have their own auto memory.

**Org-wide deployment**: deploy managed CLAUDE.md to OS-level managed-policy paths via MDM/Group Policy/Ansible. Cannot be excluded by `claudeMdExcludes`.

**Settings vs CLAUDE.md split**: settings = technical enforcement (deny tools, sandbox.enabled, env, forceLoginMethod); CLAUDE.md = behavioral guidance (style, compliance reminders, instructions).

**Troubleshooting**:
- Claude not following → run `/memory` to verify file loaded; make instructions more specific; check for contradictions across files
- For system-prompt-level instructions use `--append-system-prompt` (must pass every invocation — better for scripts)
- Use **`InstructionsLoaded` hook** to log which instruction files loaded when and why
- After `/compact`: project-root CLAUDE.md is re-read from disk; nested CLAUDE.md files re-load lazily on next file read in subdir; conversation-only instructions are LOST → write them to CLAUDE.md to persist
