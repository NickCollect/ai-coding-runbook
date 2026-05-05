---
type: summary
source: 01_Raw/code.claude.com/docs/en/troubleshoot-install.md
source_url: https://code.claude.com/docs/en/troubleshoot-install
title: "Troubleshoot installation and login"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, Settings, Enterprise-gateway]
concepts_referenced: []
---

Lookup-table-style troubleshooting for install + login errors. Major failure modes:

**Install issues**:
- `command not found: claude` → install dir not in PATH. Native install: `~/.local/bin/claude` (mac/Linux), `%USERPROFILE%\.local\bin\claude.exe` (Windows). Add to PATH via `~/.zshrc`/`~/.bashrc` or Windows User PATH env var.
- HTML returned by install URL (`syntax error near unexpected token '<'`, `Invoke-Expression: Missing argument`) → app unavailable in region OR network/regional routing issue. Try Homebrew/WinGet alternative.
- `curl: (56) Failure writing output to destination` → connection break mid-download. Retry, test `downloads.claude.ai` reachability, try alternative installer.
- `Killed` on Linux install → OOM. Add 2GB swap (`fallocate`+`mkswap`+`swapon`). Min 4GB RAM required.
- TLS/SSL errors → update CA certs, enable TLS 1.2 on Windows (`Net.ServicePointManager.SecurityProtocol = Tls12`), set `--cacert` for corporate CA, or `--ssl-revoke-best-effort` for revocation-blocked networks. Once installed, set `NODE_EXTRA_CA_CERTS` for runtime API requests.
- Behind proxy → set `HTTPS_PROXY` / `HTTP_PROXY` before installer.
- Windows wrong shell: `irm not recognized` → in CMD; `&& not valid` → in PowerShell; `bash not recognized` → ran macOS installer. Use the right command per shell.
- Windows file-in-use during install → close other PS, wait for AV, delete `%USERPROFILE%\.claude\downloads`, retry.
- Docker install hangs → `WORKDIR /tmp` before installer (avoids full FS scan). Or `--memory=4g`.
- Claude Desktop overrides `claude` cmd on Windows → update Desktop.
- Windows 32-bit error → opened "PowerShell (x86)"; use the regular `Windows PowerShell`. CC requires 64-bit.
- musl/glibc mismatch → `ldd --version` to check; may need correct binary or `apk add libgcc libstdc++ ripgrep` on Alpine.
- `Illegal instruction` → architecture mismatch OR missing AVX (pre-2013 CPU / VM hypervisor not passing AVX). No native workaround. Track GitHub issue #50384.
- `dyld: cannot load` / `Symbol not found: _ubrk_clone` on macOS → macOS too old (need 13.0+). Update macOS.
- `Exec format error` on WSL1 → known regression (#38788). Convert to WSL2 (`wsl --set-version <distro> 2`) or use `/lib64/ld-linux-x86-64.so.2 ... claude` wrapper.
- WSL npm: `npm config set os linux` then `--force`. Don't `sudo`. nvm conflicts: load nvm in shell, prepend Linux Node path.
- `Could not find native binary package` after npm install → optional deps disabled (remove `--omit=optional` etc.) OR unsupported platform OR corporate npm mirror missing platform packages.

**Login**:
- Reset: `/logout`, restart, `claude`. Press `c` to copy OAuth URL if browser doesn't open.
- `OAuth error: Invalid code` → expired/truncated. Retry quickly.
- `403 Forbidden` → check subscription active (Pro/Max), Console role assignment ("Claude Code"/"Developer"), proxy interference.
- `This organization has been disabled` despite active sub → `ANTHROPIC_API_KEY` env overriding. `unset ANTHROPIC_API_KEY`, remove from shell profile. In `-p` mode, key always used.
- WSL2/SSH/container OAuth: paste code into `Paste code here if prompted` prompt, or `BROWSER=...` env var, or use `claude auth login` (reads code from stdin).
- Token expired → `/login`. macOS Keychain locked → `security unlock-keychain ~/Library/Keychains/login.keychain-db`.
- Bedrock/Vertex/Foundry: `aws sts get-caller-identity` / `gcloud auth application-default login` / `az login` (or `ANTHROPIC_FOUNDRY_API_KEY`). IDE not inheriting shell env → set vars in IDE settings or launch IDE from shell with vars exported.

**Diagnostics**: `claude doctor`, `which -a claude` / `where.exe claude` (find conflicting installs), `ldd "$(command -v claude)" | grep "not found"` (missing libs).
