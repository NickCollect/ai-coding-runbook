---
type: summary
source: 01_Raw/code.claude.com/docs/en/vs-code.md
source_url: https://code.claude.com/docs/en/vs-code
title: "Use Claude Code in VS Code"
summarized_at: 2026-05-05
entities_referenced: [IDE-integration, Plugin, Plugin-marketplace, MCP-server, Permission-mode, Checkpointing, Settings, Enterprise-gateway, Slash-command]
concepts_referenced: []
---

VS Code (and Cursor) extension for Claude Code. Native graphical panel with diff review, plan editing, @-mention with line ranges, conversation history, multiple session tabs.

**Requirements**: VS Code 1.98.0+. Anthropic account (or third-party provider configured separately).

**Install**: VS Code Extensions search "Claude Code", or [vscode:extension/anthropic.claude-code](vscode:extension/anthropic.claude-code) / [cursor:extension/anthropic.claude-code](cursor:extension/anthropic.claude-code). Bundles the CLI, accessible from integrated terminal.

**Open the panel** — Spark icon (✱):
- Editor toolbar (top-right of editor) — needs file open.
- Activity Bar — sessions list (always visible).
- Command Palette — "Claude Code".
- Status Bar — bottom-right "✱ Claude Code".

**Sign-in**: browser flow on first open. If `ANTHROPIC_API_KEY` is set in shell but you see sign-in prompt, launch VS Code via `code .` from terminal so it inherits env (or sign in with Claude account). `/login` to retry.

**Prompt box features**:
- Permission mode indicator at bottom — switches modes; in Plan mode, VS Code opens plan as full markdown doc with inline comments. `claudeCode.initialPermissionMode` for default.
- `/` command menu — attach files, switch model, toggle extended thinking, `/usage`, `/remote-control`. Customize section: MCP/hooks/memory/permissions/plugins.
- Context indicator shows window usage; `/compact` for manual.
- Extended thinking toggle; `Ctrl+O` to expand/collapse all thinking blocks.
- `Shift+Enter` for newline.

**`@` references**: file, folder (with trailing slash), fuzzy match. PDFs accept page ranges.

**Selection awareness**: Claude sees highlighted text auto. `Option+K` / `Alt+K` inserts `@file.ts#5-10`. Eye-slash icon to hide selection.

**Drag attachments**: `Shift`+drag files into prompt.

**Sessions**: history button at top — Local + Remote tabs. Remote tab shows web-started sessions (only those with GitHub repo); resuming downloads conversation locally (changes don't sync back to claude.ai).

**Workflow customization**:
- Drag panel to secondary sidebar / primary sidebar / editor area.
- Open in New Tab / New Window for parallel conversations. Status dots: blue = pending permission, orange = finished while hidden.
- Switch to terminal mode: `claudeCode.useTerminal: true`.

**Plugin management**: `/plugins` opens GUI. Plugins tab (toggle, search, install), Marketplaces tab (add/refresh/remove). Install scope: User / Project / Local. Same as CLI under the hood.

**Chrome integration**: `@browser` prefix; needs Claude in Chrome extension v1.0.36+. Shares browser login state.

**VS Code commands & shortcuts**:
| Command | Shortcut | Purpose |
|---|---|---|
| Focus Input | `Cmd/Ctrl+Esc` | Toggle editor↔Claude focus |
| Open in New Tab | `Cmd/Ctrl+Shift+Esc` | New conversation tab |
| New Conversation | `Cmd/Ctrl+N` | Needs `enableNewConversationShortcut: true` and Claude focused |
| Insert @-Mention | `Option/Alt+K` | Reference current file+selection |

**URI handler**: `vscode://anthropic.claude-code/open?prompt=...&session=...` — open new tab from shell/script. `prompt` URL-encoded, not auto-submitted. `session` resumes by ID (must belong to current workspace). `claude-cli://` handler for terminal sessions (deep links doc).

**Settings**:
- Extension settings (VS Code): `useTerminal`, `initialPermissionMode`, `preferredLocation` (`sidebar`/`panel`), `autosave`, `useCtrlEnterToSend`, `enableNewConversationShortcut`, `hideOnboarding`, `respectGitIgnore`, `usePythonEnvironment` (activates workspace Python env), `environmentVariables`, `disableLoginPrompt`, `allowDangerouslySkipPermissions`, `claudeProcessWrapper`.
- Claude Code settings (`~/.claude/settings.json`): shared with CLI. Add `"$schema": "https://json.schemastore.org/claude-code-settings.json"` for autocomplete.

**CLI vs Extension**:
- CLI exclusive: `!` bash shortcut, tab completion, full command set.
- Both: checkpoints, MCP (CLI to add, `/mcp` panel to manage existing).
- Switch: extension and CLI share conversation history. `claude --resume` continues an extension chat.
- `@terminal:name` references terminal output by title.

**Checkpointing**: hover any message → rewind options: fork conversation from here / rewind code only / fork+rewind code.

**Built-in IDE MCP server** (`ide`, hidden from `/mcp`):
- Local 127.0.0.1:random-port, fresh auth token per activation written to `~/.claude/ide/` lock file (0600/0700).
- Tools visible to model: `mcp__ide__getDiagnostics` (read-only Problems panel) and `mcp__ide__executeCode` (Jupyter cell exec).
- `executeCode` always shows native Quick Pick **Execute/Cancel** before running. Refuses without active notebook, missing Jupyter extension, or non-Python kernel. Quick Pick is separate from `PreToolUse` hooks — allowlist lets Claude propose, Quick Pick lets it run.

**Third-party providers** (Bedrock/Vertex/Foundry): set `disableLoginPrompt: true`, configure provider in `~/.claude/settings.json` per provider doc.

**Common issues**: extension won't install (check VS Code 1.98+, check workspace trust = not Restricted Mode, disable conflicting AI extensions like Cline/Continue). Spark icon not visible → open a file (not just folder).

**Uninstall** (full clean): `rm -rf ~/.vscode/globalStorage/anthropic.claude-code` after uninstalling extension.
