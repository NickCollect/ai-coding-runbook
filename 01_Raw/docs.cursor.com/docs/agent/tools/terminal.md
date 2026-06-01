---
source_url: https://cursor.com/docs/agent/tools/terminal
fetched_at: 2026-06-01T05:54:48.264842+00:00
fetch_method: mintlify_md
---

# Terminal

Cursor runs shell commands directly in your terminal, with safe sandbox execution on macOS, Linux, and Windows.

## Sandbox

By default, Cursor runs terminal commands in a restricted environment that blocks unauthorized file access and network activity. Commands execute automatically while staying confined to your workspace.

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

If your kernel doesn't meet these requirements, Cursor falls back to asking for approval before running commands.

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

Some commands need full system access and bypass the sandbox. Cursor will indicate when a command runs outside the sandbox and ask for your approval.

### Allowlist

Commands on the allowlist skip sandbox restrictions and run immediately. You can add commands to the allowlist by choosing "Add to allowlist" when prompted after a sandboxed command fails.

When a sandboxed command fails due to restrictions, you can:

| Option               | Description                                                          |
| :------------------- | :------------------------------------------------------------------- |
| **Skip**             | Cancel the command and let Cursor try something else                 |
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

Configure how Cursor runs tools like command execution, MCP, and file writes at **Settings > Cursor Settings > Agents > Run Mode**.

### Run Mode

Choose how Cursor handles tools like command execution, MCP, and file writes:

| Mode                         | Behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :--------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Auto-review**              | Allowlisted calls run immediately. Other calls run in the sandbox when possible. Anything that can't be sandboxed (or isn't on the allowlist) goes through an LLM classifier that returns allow or block based on safety and how well the call matches your intent. On a block, Cursor can try a different approach or ask you to approve the call. The classifier isn't deterministic and isn't a guarantee, so it can make mistakes. Recommended default on Cursor 3.6 and above. |
| **Allowlist**                | Only tools and commands on your allowlist run without approval. Everything else requires your approval.                                                                                                                                                                                                                                                                                                                                                                             |
| **Allowlist (with Sandbox)** | Tools and commands on your allowlist run outside the sandbox. All other tools and commands run in the sandbox where possible. Available on macOS, Linux, and Windows (via WSL2).                                                                                                                                                                                                                                                                                                    |
| **Run Everything**           | Every tool and command runs automatically, with no classifier or sandbox in the loop. Pick this when you want zero prompting and fully deterministic pass-through, and you accept that nothing gets screened first.                                                                                                                                                                                                                                                                 |

Cursor 3.6 introduces **Auto-review** as the new default. Before Cursor 3.5, the same settings appeared as **Run in Sandbox**, **Ask Every Time**, and **Run Everything**. **Run in Sandbox** maps to **Allowlist (with Sandbox)**. **Ask Every Time** is deprecated. Use **Allowlist** with empty allowlists to require approval for every action.

We are currently not charging for the Auto-review classifier token costs.

#### How Auto-review works

**Auto-review** applies to Shell, MCP, and Fetch tool calls on every platform. Every call goes through three checks in order:

1. **Allowlist.** If the call matches your [terminal](https://cursor.com/docs/agent/tools/terminal.md#protection-settings) or [MCP](https://cursor.com/docs/agent/tools/terminal.md#protection-settings) allowlist, it runs immediately.
2. **Sandbox.** If the call can run inside the sandbox, it runs there with the network and filesystem restrictions described above. The sandbox step is only available on macOS, Linux, and Windows (via WSL2); on other platforms the call skips straight to the classifier.
3. **Classifier.** Anything else is sent to an LLM classifier with the current user request and your `autoRun` instructions from [`permissions.json`](https://cursor.com/docs/reference/permissions.md#autorun-configuration). The classifier returns **allow** or **block**.

When the classifier blocks a call, Cursor can pick a different approach or insist and surface a standard approval prompt to you. The classifier adds no extra cost on top of your existing agent usage.

The classifier is non-deterministic and can make mistakes in both directions. It can allow a call you would have blocked, and it can block a call that was safe. Treat **Auto-review** as best-effort convenience, not a security boundary. For strict control, use **Allowlist** and approve calls yourself.

### Run Mode network access

Choose how sandboxed commands access the network:

| Mode                        | Behavior                                                                                             |
| :-------------------------- | :--------------------------------------------------------------------------------------------------- |
| **sandbox.json Only**       | Network is limited to domains in your `sandbox.json` allowlist. No Cursor defaults are added.        |
| **sandbox.json + Defaults** | Your allowlist plus Cursor's built-in defaults (common package managers, etc.). This is the default. |
| **Allow All**               | All network access is allowed in the sandbox, regardless of `sandbox.json`.                          |

### Protection settings

| Setting                      | Description                                                                                                                                                                              |
| :--------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Command Allowlist**        | Terminal commands that run without approval. In **Allowlist (with Sandbox)** mode, these run outside the sandbox; in **Allowlist** mode, they run normally without sandbox restrictions. |
| **MCP Allowlist**            | MCP tools that run without approval. In **Allowlist (with Sandbox)** mode, these run outside the sandbox; in **Allowlist** mode, they run normally without sandbox restrictions.         |
| **Browser Protection**       | Prevent Cursor from automatically running [Browser](https://cursor.com/docs/agent/tools/browser.md) tools.                                                                               |
| **File-Deletion Protection** | Prevent Cursor from deleting files automatically.                                                                                                                                        |
| **Dotfile Protection**       | Prevent Cursor from modifying dot files like .gitignore automatically.                                                                                                                   |
| **External-File Protection** | Prevent Cursor from creating or modifying files outside of the workspace automatically.                                                                                                  |

## Enterprise controls

Only available for Enterprise subscriptions.

Enterprise admins can override editor configurations or change which settings are visible for end users. Navigate to **Settings > Run Mode** in the [web dashboard](https://cursor.com/dashboard/settings) to view and change these settings.

| Setting                        | Description                                                                                                                 |
| :----------------------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| **Run Mode controls**          | Enable controls for Run Mode and allowlists. When disabled, end users get **Allowlist (with Sandbox)** behavior by default. |
| **Sandboxing Mode**            | Control whether **Allowlist (with Sandbox)** is available. When enabled, commands not on the allowlist run in the sandbox.  |
| **Sandbox Networking**         | Choose whether sandboxed commands have network access.                                                                      |
| **Delete File Protection**     | Prevent Cursor from deleting files automatically.                                                                           |
| **MCP Tool Protection**        | Prevent Cursor from automatically running MCP tools.                                                                        |
| **Terminal Command Allowlist** | Commands that run without sandboxing. In **Allowlist (with Sandbox)** mode, all other commands run in the sandbox.          |
| **Enable Run Everything**      | Give end users the ability to enable the **Run Everything** mode.                                                           |

## Troubleshooting

Some shell themes (for example, Powerlevel9k/Powerlevel10k) can interfere with
the inline terminal output. If your command output looks truncated or
misformatted, disable the theme or switch to a simpler prompt when Cursor runs.

### Disable heavy prompts for Cursor sessions

Use the `CURSOR_AGENT` environment variable in your shell config to detect when
Cursor is running and skip initializing fancy prompts/themes.

```zsh
# ~/.zshrc — disable Powerlevel10k when Cursor runs
if [[ -n "$CURSOR_AGENT" ]]; then
  # Skip theme initialization for better compatibility
else
  [[ -r ~/.p10k.zsh ]] && source ~/.p10k.zsh
fi
```

```bash
# ~/.bashrc — fall back to a simple prompt in Cursor sessions
if [[ -n "$CURSOR_AGENT" ]]; then
  PS1='\u@\h \W \$ '
fi
```


---

## Sitemap

[Overview of all docs pages](/llms.txt)
