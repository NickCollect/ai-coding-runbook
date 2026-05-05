---
source_url: https://cursor.com/docs/cli/installation
fetched_at: 2026-05-05T19:55:37.068959+00:00
fetch_method: mintlify_md
---

# Installation

## Installation

### macOS, Linux and Windows (WSL)

Install Cursor CLI with a single command:

```bash
curl https://cursor.com/install -fsS | bash
```

### Windows (native)

Install Cursor CLI on Windows using PowerShell:

```powershell
irm 'https://cursor.com/install?win32=true' | iex
```

### Verification

After installation, verify that Cursor CLI is working correctly:

```bash
agent --version
```

## Post-installation setup

1. **Add \~/.local/bin to your PATH:**

   For bash:

   ```bash
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

   For zsh:

   ```bash
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

2. **Start using Cursor Agent:**
   ```bash
   agent
   ```

## Updates

Cursor CLI will try to auto-update by default to ensure you always have the latest version.

To manually update Cursor CLI to the latest version:

```bash
agent update
```


---

## Sitemap

[Overview of all docs pages](/llms.txt)
