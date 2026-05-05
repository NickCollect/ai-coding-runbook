---
type: summary
source: 01_Raw/code.claude.com/docs/en/quickstart.md
source_url: https://code.claude.com/docs/en/quickstart
title: "Quickstart"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, IDE-integration, Slash-command]
concepts_referenced: []
---

Raw is mostly Mintlify InstallConfigurator JSX (~530 lines of CSS/component definitions). The actual quickstart prose is short.

**Prereqs**: terminal, code project, Claude subscription (Pro/Max/Team/Enterprise) or Console account or supported cloud provider.

**Step 1 — Install**:
- macOS/Linux/WSL: `curl -fsSL https://claude.ai/install.sh | bash`
- Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`
- Windows CMD: `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd`
- Homebrew: `brew install --cask claude-code` (or `claude-code@latest`)
- WinGet: `winget install Anthropic.ClaudeCode`
- Linux: apt/dnf/apk also.

Native installs auto-update; brew/winget require manual upgrade. Git for Windows recommended on native Windows for Bash tool support.

**Step 2 — Login**: `claude` prompts on first use. `/login` to switch later. Login options: Claude subscription (recommended), Claude Console (auto-creates "Claude Code" workspace for cost tracking), Bedrock/Vertex/Foundry.

**Step 3 — Start session**: `cd /path/to/project && claude`. Welcome screen shows session info, recent conversations, updates. `/help` for commands, `/resume` to continue.

**Step 4 — Ask questions**: "what does this project do?", "what technologies does this project use?", "where is the main entry point?", "explain the folder structure". Claude reads files as needed — no manual context.

**Step 5 — First code change**: "add a hello world function to the main file" — Claude finds file, shows proposed changes, asks approval, edits.

**Step 6 — Git**: "what files have I changed?", "commit my changes with a descriptive message", "create a new branch called feature/quickstart", "help me resolve merge conflicts".

**Step 7 — Bug fix / feature**: natural language: "add input validation to the user registration form", "there's a bug where users can submit empty forms - fix it".

**Step 8 — Other workflows**: refactor ("refactor the authentication module to use async/await"), tests ("write unit tests for the calculator functions"), docs ("update the README"), code review.

**Essential commands**: `claude` interactive, `claude "task"` one-time, `claude -p "query"` exit after, `claude -c` continue most recent, `claude -r` resume picker, `/clear`, `/help`, `exit`/Ctrl+D.

**Pro tips**: be specific, break into steps, let Claude explore first ("analyze the database schema"), use shortcuts (`?` keybindings, Tab completion, ↑ history, `/` commands).
