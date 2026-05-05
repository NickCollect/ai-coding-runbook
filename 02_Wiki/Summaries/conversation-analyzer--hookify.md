---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/hookify/agents/conversation-analyzer.md
title: "hookify plugin: conversation-analyzer subagent"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Subagent, Hooks]
concepts_referenced: []
---

Subagent definition from `hookify` plugin. Triggered by `/hookify` (no args) or when user asks to identify behaviors worth blocking with hooks.

**Frontmatter**: `name: conversation-analyzer`, `model: inherit`, `color: yellow`, `tools: ["Read", "Grep"]`.

**Purpose**: read conversation transcripts, identify problematic Claude behaviors, output structured findings for hook rule generation.

**Process**:
1. **Search user messages reverse-chronologically** for:
   - Explicit corrections: "Don't use X", "Stop doing Y", "Avoid...", "Never..."
   - Frustrated reactions: "Why did you do X?", "I didn't ask for that", "That was wrong"
   - User reverting/fixing Claude's changes
   - Repeated issues / multiple reminders

2. **Identify tool usage patterns**: which tool (Bash/Edit/Write/MultiEdit), what action, when, why problematic. Extract concrete examples (actual command, code pattern).

3. **Create regex patterns**:
   - Bash: `rm\s+-rf`, `sudo\s+`, `chmod\s+777`
   - Code: `console\.log\(`, `eval\(|new Function\(`, `innerHTML\s*=`
   - Paths: `\.env$`, `/node_modules/`, `dist/|build/`

4. **Categorize severity**:
   - High (block): dangerous commands, security issues, data loss risks.
   - Medium (warn): style violations, wrong file types, missing best practices.
   - Low (optional): preferences, non-critical patterns.

5. **Output format**: structured markdown — per-issue: severity, tool, pattern, occurrences, context, user reaction, suggested rule (name/event/pattern/message). Final summary with counts.

**Edge cases**: don't flag hypotheticals ("what would happen if I used rm -rf?"), teaching moments ("here's what you shouldn't do"), one-time accidents (mark low priority), subjective preferences.

The `/hookify` command consumes this analysis to present findings, ask which rules to create, generate `.local.md` config files in `.claude/`.
