---
type: summary
source: 01_Raw/code.claude.com/docs/en/setup.md
source_url: https://code.claude.com/docs/en/setup
title: "Advanced setup"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, IDE-integration, Settings, Sandboxing, Enterprise-gateway]
concepts_referenced: []
---

System requirements + platform install/update/uninstall reference.

**System reqs**: macOS 13+, Windows 10 1809+/Server 2019+, Ubuntu 20.04+, Debian 10+, Alpine 3.19+. 4 GB+ RAM, x64 or ARM64. Bash/Zsh/PowerShell/CMD shell. Native Windows: Git for Windows recommended (else PowerShell fallback). ripgrep usually bundled.

**Install methods** (per platform): Native installer (recommended, auto-updates), Homebrew (`claude-code` stable / `claude-code@latest` latest channel — manual upgrade), WinGet (manual upgrade), Linux apt/dnf/apk (manual upgrade), npm `@anthropic-ai/claude-code` (Node 18+; ships native binary via per-platform optional deps). Don't use `sudo npm install -g`.

Supported npm install platforms: `darwin-arm64`, `darwin-x64`, `linux-x64`, `linux-arm64`, `linux-x64-musl`, `linux-arm64-musl`, `win32-x64`, `win32-arm64`.

**Windows options**:
- Native + Git Bash: works in PS or CMD. If GBash absent, PowerShell tool used. Set `CLAUDE_CODE_GIT_BASH_PATH` if not auto-detected. PowerShell tool optional: `CLAUDE_CODE_USE_POWERSHELL_TOOL=1`.
- WSL 2 (sandboxing supported)
- WSL 1 (no sandboxing)

**Alpine/musl-based**: native installer needs `libgcc`, `libstdc++`, `ripgrep` from package manager + set `USE_BUILTIN_RIPGREP=0`.

**Verify**: `claude --version`, `claude doctor` for full diagnostic.

**Update**:
- Native: auto-updates background.
- `autoUpdatesChannel` setting: `"latest"` (default) or `"stable"` (~1 week behind).
- `minimumVersion` setting: floor for downgrades.
- `DISABLE_AUTOUPDATER=1` stops background check; `DISABLE_UPDATES` blocks all.
- Manual: `claude update`.

**Install specific version**: append channel name or version: `bash -s stable`, `bash -s 2.1.89`. Channel chosen at install becomes default for auto-updates.

**Linux package managers**: signed apt/dnf/apk repos. Key fingerprint: `31DD DE24 DDFA B679 F42D 7BD2 BAA9 29FF 1A7E CACE`. Installs do NOT auto-update via Claude Code.

**Binary integrity**: each release publishes `manifest.json` with SHA256 checksums + GPG signature (from v2.1.89). Signing key at `https://downloads.claude.ai/keys/claude-code.asc`. Verify: import key, fetch manifest + .sig, `gpg --verify`. macOS binaries also code-signed by "Anthropic PBC" + notarized. Windows by "Anthropic, PBC". Linux not individually signed (verify via manifest).

**Uninstall**:
- Native (mac/Linux): `rm -f ~/.local/bin/claude && rm -rf ~/.local/share/claude`.
- Native (Windows): `Remove-Item` equivalents under `$env:USERPROFILE\.local\bin\claude.exe` + `\.local\share\claude`.
- Brew: `brew uninstall --cask claude-code` (or `@latest`).
- WinGet: `winget uninstall Anthropic.ClaudeCode`.
- apt/dnf/apk: package + repo config + key.
- npm: `npm uninstall -g @anthropic-ai/claude-code`.
- Config wipe: `rm -rf ~/.claude && rm ~/.claude.json` plus per-project `.claude/`, `.mcp.json`. Other apps (VS Code ext, JetBrains plugin, Desktop) recreate `~/.claude/`; uninstall those first for full wipe.
