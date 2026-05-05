---
source_url: https://cursor.com/docs/agent/tools/terminal
---

# Terminal

Agent runs shell commands directly in your terminal, with safe sandbox execution on macOS, Linux, and Windows.

## Sandbox

By default, Agent runs terminal commands in a restricted environment that blocks unauthorized file access and network activity. Commands execute automatically while staying confined to your workspace.

For a deep dive into how sandboxing is implemented on each platform, see [Implementing a secure sandbox for local agents](/blog/agent-sandboxing).

### Platform requirements

#### macOS

- Cursor v2.0 or later
- Works out of the box with no additional setup

#### Windows

- [WSL2](https://learn.microsoft.com/en-us/windows/wsl/about) must be installed and configured
- The sandbox runs inside WSL2, applying the same restrictions as on Linux

#### Linux

- **Kernel 6.2 or later** with Landlock v3 support (`CONFIG_SECURITY_LANDLOCK=y`)
- **Unprivileged user namespaces** enabled (most distributions enable this by default)

If your kernel doesn't meet these requirements, Agent falls back to asking for approval before running commands.

**AppArmor setup**

Some distributions restrict user namespaces through AppArmor. The Cursor desktop package ships with the required profile, so no extra setup is needed for local installations.

Remote environments and the standalone [CLI](https://cursor.com/docs/cli/overview.md) don't include this profile. If sandbox creation fails with a permissions error related to user namespaces, install the AppArmor package for your distribution:

Debian / Ubuntu:

```bash
curl -fsSL https://downloads.cursor.com/lab/enterprise/cursor-sandbox-apparmor_0.6.0_all.deb -o cursor-sandbox-apparmor.deb
sudo dpkg -i cursor-sandbox-apparmor.deb
```

RHEL / Fedora:

```bash
curl -fsSL https://downloads.cursor.com/lab/enterprise/cursor-sandbox-apparmor-0.6.0-1.noarch.rpm -o cursor-sandbox-apparmor.rpm
sudo rpm -i cursor-sandbox-apparmor.rpm
```

After installing, restart Cursor or your CLI session for the sandbox to work.

### How the sandbox works

The sandbox prevents unauthorized access while allowing workspace operations:

| Access Type         | Description                                                                                                       |
| :------------------ | :---------------------------------------------------------------------------------------------------------------- |
| **File access**     | Read access to the filesystemRead and write access to workspace directories                                       |
| **Network access**  | Blocked by default. Configure with [`sandbox.json`](https://cursor.com/docs/reference/sandbox.md) or in settings. |
| **Temporary files** | Full access to `/tmp/` or equivalent system temp directories                                                      |

The `.cursor` configuration directory stays protected regardless of allowlist settings.

Some commands need full system access and bypass the sandbox. Agent will indicate when a command runs outside the sandbox and ask for your approval.

### Allowlist

Commands on the allowlist skip sandbox restrictions and run immediately. You can add commands to the allowlist by choosing "Add to allowlist" when prompted after a sandboxed command fails.

When a sandboxed command fails due to restrictions, you can:

| Option               | Description                                                          |
| :------------------- | :------------------------------------------------------------------- |
| **Skip**             | Cancel the command and let Agent try something else                  |
| **Run**              | Execute the command without sandbox restrictions                     |
| **Add to allowlist** | Run without restrictions and automatically approve it for future use |

#### Default network allowlist

When network access is enabled, outbound connections are restricted to a curated set of domains. These cover common package registries, cloud providers, and language toolchains so most development workflows work without extra configuration.

### View default allowed domains

```text
*.cloudflarestorage.com
*.docker.com
*.docker.io
*.googleapis.com
*.githubusercontent.com
*.gvt1.com
*.public.blob.vercel-storage.com
*.yarnpkg.com
alpinelinux.org
anaconda.com
apache.org
apt.llvm.org
archive.ubuntu.com
archlinux.org
awscli.amazonaws.com
azure.com
binaries.prisma.sh
bitbucket.org
centos.org
cloudflarestorage.com
cocoapods.org
codeload.github.com
cpan.org
crates.io
debian.org
dl.google.com
docker.com
docker.io
dot.net
dotnet.microsoft.com
eclipse.org
fedoraproject.org
files.pythonhosted.org
fonts.gstatic.com
gcr.io
ghcr.io
github.com
gitlab.com
golang.org
google.com
goproxy.io
gradle.org
haskell.org
hashicorp.com
hex.pm
index.crates.io
java.com
java.net
json-schema.org
json.schemastore.org
k8s.io
launchpad.net
maven.org
mcr.microsoft.com
metacpan.org
microsoft.com
mise.run
nodejs.org
npm.duckdb.org
npmjs.com
npmjs.org
nuget.org
oracle.com
packagecloud.io
packages.microsoft.com
packagist.org
pkg.go.dev
playwright.azureedge.net
ppa.launchpad.net
proxy.golang.org
pub.dev
public.blob.vercel-storage.com
public.ecr.aws
pypa.io
pypi.org
pypi.python.org
pythonhosted.org
quay.io
registry.npmjs.org
registry.yarnpkg.com
repo.maven.apache.org
ruby-lang.org
rubygems.org
rubyonrails.org
rustup.rs
rvm.io
security.ubuntu.com
sh.rustup.rs
sourceforge.net
spring.io
static.crates.io
static.rust-lang.org
sum.golang.org
swift.org
ubuntu.com
visualstudio.com
yarnpkg.com
ziglang.org
```

## Sandbox configuration

Customize sandbox behavior with a `sandbox.json` file placed at `~/.cursor/sandbox.json` (per-user) or `<workspace>/.cursor/sandbox.json` (per-repo). Control network access, filesystem paths, build caches, and more.

See the [`sandbox.json` reference](https://cursor.com/docs/reference/sandbox.md) for the full schema, network pattern syntax, merge behavior, and protected paths.

## Environment variables

Cursor injects environment variables into every sandboxed child process. These are available to your scripts, build tools, and automation running inside the sandbox.

| Variable                         | Platforms             | Description                                                                                                                  |
| :------------------------------- | :-------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| `CURSOR_SANDBOX`                 | macOS, Linux, Windows | Set to `"seatbelt"` (macOS) or `"native"` (Linux/Windows) when the process is running inside the sandbox.                    |
| `CURSOR_ORIG_UID`                | macOS, Linux          | The UID of the user who launched Cursor, captured **before** the sandbox applies any namespace or identity changes.          |
| `CURSOR_ORIG_GID`                | macOS, Linux          | The GID of the user who launched Cursor, captured before sandbox identity changes.                                           |
| `CURSOR_SANDBOX_LANDLOCK_STATUS` | Linux                 | Reports the active sandbox backend: `fully_enforced` (Landlock), `bubblewrap` (Bubblewrap fallback). Useful for diagnostics. |

### Linux: UID inside the sandbox may not match your real user

On Linux, the sandbox creates a user namespace and remaps the process to UID 0
(root) inside that namespace. This means `id -u` and `$UID` inside a sandboxed
command return 0, not your actual user ID. If your scripts or automation need
the real host user — for example, to set file ownership or pass `--user` to
Docker — read `CURSOR_ORIG_UID` and `CURSOR_ORIG_GID` instead.

### Docker and container automation

A common pattern in automation rules and scripts is running Docker containers that need to match the host user's identity. Because the sandbox remaps the UID on Linux, relying on `$(id -u)` produces the wrong value. Use the `CURSOR_ORIG_*` variables instead:

```bash
docker run --rm \
  --user "${CURSOR_ORIG_UID:-$(id -u)}:${CURSOR_ORIG_GID:-$(id -g)}" \
  -v "$PWD:/work" -w /work \
  my-image build
```

The `${CURSOR_ORIG_UID:-$(id -u)}` fallback ensures the command also works outside the sandbox, where the variables are not set.

## Editor configuration

Configure how Agent runs terminal commands at **Settings > Cursor Settings > Agents > Auto-Run**.

### Auto-run mode

Choose how Agent runs tools like command execution, MCP, and file writes:

| Mode               | Behavior                                                                                                      |
| :----------------- | :------------------------------------------------------------------------------------------------------------ |
| **Run in Sandbox** | Tools and commands auto-run in the sandbox where possible. Available on macOS, Linux, and Windows (via WSL2). |
| **Ask Every Time** | All tools and commands require user approval before running.                                                  |
| **Run Everything** | The agent runs all tools and commands automatically without asking for input.                                 |

### Auto-run network access

Choose how sandboxed commands access the network:

| Mode                        | Behavior                                                                                             |
| :-------------------------- | :--------------------------------------------------------------------------------------------------- |
| **sandbox.json Only**       | Network is limited to domains in your `sandbox.json` allowlist. No Cursor defaults are added.        |
| **sandbox.json + Defaults** | Your allowlist plus Cursor's built-in defaults (common package managers, etc.). This is the default. |
| **Allow All**               | All network access is allowed in the sandbox, regardless of `sandbox.json`.                          |

### Protection settings

| Setting                      | Description                                                                                               |
| :--------------------------- | :-------------------------------------------------------------------------------------------------------- |
| **Command Allowlist**        | Commands that can run automatically outside of the sandbox.                                               |
| **MCP Allowlist**            | MCP tools that can run automatically outside of the sandbox.                                              |
| **Browser Protection**       | Prevent Agent from automatically running [Browser](https://cursor.com/docs/agent/tools/browser.md) tools. |
| **File-Deletion Protection** | Prevent Agent from deleting files automatically.                                                          |
| **Dotfile Protection**       | Prevent Agent from modifying dot files like .gitignore automatically.                                     |
| **External-File Protection** | Prevent Agent from creating or modifying files outside of the workspace automatically.                    |

## Enterprise controls

Only available for Enterprise subscriptions.

Enterprise admins can override editor configurations or change which settings are visible for end users. Navigate to **Settings > Auto-Run** in the [web dashboard](https://cursor.com/dashboard/settings) to view and change these settings.

| Setting                        | Description                                                                                                                                        |
| :----------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Auto-Run Controls**          | Enable controls for auto-run and sandbox mode. When disabled, commands auto-run in the sandbox where available, otherwise they ask for permission. |
| **Sandboxing Mode**            | Control whether sandbox is available for end users. When enabled, commands auto-run in the sandbox even if they are not on the allowlist.          |
| **Sandbox Networking**         | Choose whether sandboxed commands have network access.                                                                                             |
| **Delete File Protection**     | Prevent Agent from deleting files automatically.                                                                                                   |
| **MCP Tool Protection**        | Prevent Agent from automatically running MCP tools.                                                                                                |
| **Terminal Command Allowlist** | Commands that can run automatically without sandboxing. When sandbox is enabled, commands not on this list auto-run in sandbox mode.               |
| **Enable Run Everything**      | Give end users the ability to enable the "Run Everything" auto-run mode.                                                                           |

## Troubleshooting

Some shell themes (for example, Powerlevel9k/Powerlevel10k) can interfere with
the inline terminal output. If your command output looks truncated or
misformatted, disable the theme or switch to a simpler prompt when Agent runs.

### Disable heavy prompts for Agent sessions

Use the `CURSOR_AGENT` environment variable in your shell config to detect when
the Agent is running and skip initializing fancy prompts/themes.

```zsh
# ~/.zshrc — disable Powerlevel10k when Cursor Agent runs
if [[ -n "$CURSOR_AGENT" ]]; then
  # Skip theme initialization for better compatibility
else
  [[ -r ~/.p10k.zsh ]] && source ~/.p10k.zsh
fi
```

```bash
# ~/.bashrc — fall back to a simple prompt in Agent sessions
if [[ -n "$CURSOR_AGENT" ]]; then
  PS1='\u@\h \W \$ '
fi
```


---

## Sitemap

[Overview of all docs pages](/llms.txt)
