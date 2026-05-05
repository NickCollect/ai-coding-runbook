---
source_url: https://code.claude.com/docs/en/permission-modes
fetched_at: 2026-05-04T15:06:32.429374+00:00
fetch_method: mintlify_md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Choose a permission mode

> Control whether Claude asks before editing files or running commands. Cycle modes with Shift+Tab in the CLI or use the mode selector in VS Code, Desktop, and claude.ai.

When Claude wants to edit a file, run a shell command, or make a network request, it pauses and asks you to approve the action. Permission modes control how often that pause happens. The mode you pick shapes the flow of a session: default mode has you review each action as it comes, while looser modes let Claude work in longer uninterrupted stretches and report back when done. Pick more oversight for sensitive work, or fewer interruptions when you trust the direction.

## Available modes

Each mode makes a different tradeoff between convenience and oversight. The table below shows what Claude can do without a permission prompt in each mode.

| Mode                                                                | What runs without asking                                                               | Best for                                |
| :------------------------------------------------------------------ | :------------------------------------------------------------------------------------- | :-------------------------------------- |
| `default`                                                           | Reads only                                                                             | Getting started, sensitive work         |
| [`acceptEdits`](https://code.claude.com/docs/en/`acceptEdits`)     | Reads, file edits, and common filesystem commands (`mkdir`, `touch`, `mv`, `cp`, etc.) | Iterating on code you're reviewing      |
| [`plan`](https://code.claude.com/docs/en/`plan`)                   | Reads only                                                                             | Exploring a codebase before changing it |
| [`auto`](https://code.claude.com/docs/en/`auto`)                         | Everything, with background safety checks                                              | Long tasks, reducing prompt fatigue     |
| [`dontAsk`](https://code.claude.com/docs/en/`dontAsk`)       | Only pre-approved tools                                                                | Locked-down CI and scripts              |
| [`bypassPermissions`](https://code.claude.com/docs/en/`bypassPermissions`) | Everything                                                                             | Isolated containers and VMs only        |

In every mode except `bypassPermissions`, writes to [protected paths](https://code.claude.com/docs/en/protected paths) are never auto-approved, guarding repository state and Claude's own configuration against accidental corruption.

Modes set the baseline. Layer [permission rules](https://code.claude.com/docs/en/permission rules) on top to pre-approve or block specific tools in any mode except `bypassPermissions`, which skips the permission layer entirely.

## Switch permission modes

You can switch modes mid-session, at startup, or as a persistent default. The mode is set through these controls, not by asking Claude in chat. Select your interface below to see how to change it.

<Tabs>
  <Tab title="CLI">
    **During a session**: press `Shift+Tab` to cycle `default` → `acceptEdits` → `plan`. The current mode appears in the status bar. Not every mode is in the default cycle:

    * `auto`: appears when your account meets the [auto mode requirements](https://code.claude.com/docs/en/auto mode requirements); cycling to auto shows an opt-in prompt until you accept it, or select **No, don't ask again** to remove auto from the cycle
    * `bypassPermissions`: appears after you start with `--permission-mode bypassPermissions`, `--dangerously-skip-permissions`, or `--allow-dangerously-skip-permissions`; the `--allow-` variant adds the mode to the cycle without activating it
    * `dontAsk`: never appears in the cycle; set it with `--permission-mode dontAsk`

    Enabled optional modes slot in after `plan`, with `bypassPermissions` first and `auto` last. If you have both enabled, you will cycle through `bypassPermissions` on the way to `auto`.

    **At startup**: pass the mode as a flag.

    ```bash theme={null}
    claude --permission-mode plan
    ```

    **As a default**: set `defaultMode` in [settings](https://code.claude.com/docs/en/settings).

    ```json theme={null}
    {
      "permissions": {
        "defaultMode": "acceptEdits"
      }
    }
    ```

    The same `--permission-mode` flag works with `-p` for [non-interactive runs](https://code.claude.com/docs/en/non-interactive runs).
  </Tab>

  <Tab title="VS Code">
    **During a session**: click the mode indicator at the bottom of the prompt box.

    **As a default**: set `claudeCode.initialPermissionMode` in VS Code settings, or use the Claude Code extension settings panel.

    The mode indicator shows these labels, mapped to the mode each one applies:

    | UI label           | Mode                |
    | :----------------- | :------------------ |
    | Ask before edits   | `default`           |
    | Edit automatically | `acceptEdits`       |
    | Plan mode          | `plan`              |
    | Auto mode          | `auto`              |
    | Bypass permissions | `bypassPermissions` |

    Auto mode appears in the mode indicator after you enable **Allow dangerously skip permissions** in the extension settings, but it stays unavailable until your account meets every requirement listed in the [auto mode section](https://code.claude.com/docs/en/auto mode section). The `claudeCode.initialPermissionMode` setting does not accept `auto`; to start in auto mode by default, set `defaultMode` in your Claude Code [`settings.json`](https://code.claude.com/docs/en/`settings.json`) instead.

    Bypass permissions also requires the **Allow dangerously skip permissions** toggle before it appears in the mode indicator.

    See the [VS Code guide](https://code.claude.com/docs/en/VS Code guide) for extension-specific details.
  </Tab>

  <Tab title="JetBrains">
    The JetBrains plugin runs Claude Code in the IDE terminal, so switching modes works the same as in the CLI: press `Shift+Tab` to cycle, or pass `--permission-mode` when launching.
  </Tab>

  <Tab title="Desktop">
    Use the mode selector next to the send button. Auto and Bypass permissions appear only after you enable them in Desktop settings. See the [Desktop guide](https://code.claude.com/docs/en/Desktop guide).
  </Tab>

  <Tab title="Web and mobile">
    Use the mode dropdown next to the prompt box on [claude.ai/code](https://code.claude.com/docs/en/claude.ai/code) or in the mobile app. Permission prompts appear in claude.ai for approval. Which modes appear depends on where the session runs:

    * **Cloud sessions** on [Claude Code on the web](https://code.claude.com/docs/en/Claude Code on the web): Auto accept edits and Plan mode. Ask permissions, Auto, and Bypass permissions are not available.
    * **[Remote Control](https://code.claude.com/docs/en/Remote Control) sessions** on your local machine: Ask permissions, Auto accept edits, and Plan mode. Auto and Bypass permissions are not available.

    For Remote Control, you can also set the starting mode when launching the host:

    ```bash theme={null}
    claude remote-control --permission-mode acceptEdits
    ```
  </Tab>
</Tabs>

## Auto-approve file edits with acceptEdits mode

`acceptEdits` mode lets Claude create and edit files in your working directory without prompting. The status bar shows `⏵⏵ accept edits on` while this mode is active.

In addition to file edits, `acceptEdits` mode auto-approves common filesystem Bash commands: `mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, and `sed`. These commands are also auto-approved when prefixed with safe environment variables such as `LANG=C` or `NO_COLOR=1`, or process wrappers such as `timeout`, `nice`, or `nohup`. Like file edits, auto-approval applies only to paths inside your working directory or `additionalDirectories`. Paths outside that scope, writes to [protected paths](https://code.claude.com/docs/en/protected paths), and all other Bash commands still prompt.

When the [PowerShell tool](https://code.claude.com/docs/en/PowerShell tool) is enabled, `acceptEdits` mode also auto-approves `Set-Content`, `Add-Content`, `Clear-Content`, and `Remove-Item` on in-scope paths, along with their common aliases. The same scope and protected-path rules apply.

Use `acceptEdits` when you want to review changes in your editor or via `git diff` after the fact rather than approving each edit inline. Press `Shift+Tab` once from default mode to enter it, or start with it directly:

```bash theme={null}
claude --permission-mode acceptEdits
```

## Analyze before you edit with plan mode

Plan mode tells Claude to research and propose changes without making them. Claude reads files, runs shell commands to explore, and writes a plan, but does not edit your source. Permission prompts still apply the same as default mode.

Enter plan mode by pressing `Shift+Tab` or prefixing a single prompt with `/plan`. You can also start in plan mode from the CLI:

```bash theme={null}
claude --permission-mode plan
```

Press `Shift+Tab` again to leave plan mode without approving a plan.

### Review and approve a plan

When the plan is ready, Claude presents it and asks how to proceed. From that prompt you can:

* Approve and start in auto mode
* Approve and accept edits
* Approve and review each edit manually
* Keep planning with feedback
* Refine with [Ultraplan](https://code.claude.com/docs/en/Ultraplan) for browser-based review

Press `Ctrl+G` to open the proposed plan in your default text editor and edit it directly before Claude proceeds. When [`showClearContextOnPlanAccept`](https://code.claude.com/docs/en/`showClearContextOnPlanAccept`) is enabled, each approve option also offers to clear the planning context first.

Accepting a plan also names the session from the plan content automatically, unless you've already set a name with `--name` or `/rename`.

### Set plan mode as the default

To make plan mode the default for a project, set `defaultMode` in `.claude/settings.json`:

```json theme={null}
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

## Eliminate prompts with auto mode

<Note>
  Auto mode requires Claude Code v2.1.83 or later.
</Note>

Auto mode lets Claude execute without permission prompts. A separate classifier model reviews actions before they run, blocking anything that escalates beyond your request, targets unrecognized infrastructure, or appears driven by hostile content Claude read.

<Warning>
  Auto mode is a research preview. It reduces prompts but does not guarantee safety. Use it for tasks where you trust the general direction, not as a replacement for review on sensitive operations.
</Warning>

Auto mode is available only when your account meets all of these requirements:

* **Plan**: Max, Team, Enterprise, or API. Not available on Pro.
* **Admin**: on Team and Enterprise, an admin must enable it in [Claude Code admin settings](https://code.claude.com/docs/en/Claude Code admin settings) before users can turn it on. Admins can also lock it off by setting `permissions.disableAutoMode` to `"disable"` in [managed settings](https://code.claude.com/docs/en/managed settings).
* **Model**: Claude Sonnet 4.6, Opus 4.6, or Opus 4.7 on Team, Enterprise, and API plans; Claude Opus 4.7 only on Max plans. Other models, including Haiku and claude-3 models, are not supported.
* **Provider**: Anthropic API only. Not available on Bedrock, Vertex, or Foundry.

If Claude Code reports auto mode as unavailable, one of these requirements is unmet; this is not a transient outage. A separate message that names a model and says auto mode "cannot determine the safety" of an action is a transient classifier outage; see the [error reference](https://code.claude.com/docs/en/error reference).

### What the classifier blocks by default

The classifier trusts your working directory and your repo's configured remotes. Everything else is treated as external until you [configure trusted infrastructure](https://code.claude.com/docs/en/configure trusted infrastructure).

**Blocked by default**:

* Downloading and executing code, like `curl | bash`
* Sending sensitive data to external endpoints
* Production deploys and migrations
* Mass deletion on cloud storage
* Granting IAM or repo permissions
* Modifying shared infrastructure
* Irreversibly destroying files that existed before the session
* Force push, or pushing directly to `main`

**Allowed by default**:

* Local file operations in your working directory
* Installing dependencies declared in your lock files or manifests
* Reading `.env` and sending credentials to their matching API
* Read-only HTTP requests
* Pushing to the branch you started on or one Claude created

Sandbox network access requests are routed through the classifier rather than allowed by default. Run `claude auto-mode defaults` to see the full rule lists. If routine actions get blocked, an administrator can add trusted repos, buckets, and services via the `autoMode.environment` setting: see [Configure auto mode](https://code.claude.com/docs/en/Configure auto mode).

### Boundaries you state in conversation

The classifier treats boundaries you state in the conversation as a block signal. If you tell Claude "don't push" or "wait until I review before deploying", the classifier blocks matching actions even when the default rules would allow them. A boundary stays in force until you lift it in a later message. Claude's own judgment that a condition was met does not lift it.

Boundaries are not stored as rules. The classifier re-reads them from the transcript on each check, so a boundary can be lost if [context compaction](https://code.claude.com/docs/en/context compaction) removes the message that stated it. For a hard guarantee, add a [deny rule](https://code.claude.com/docs/en/deny rule) instead.

### When auto mode falls back

Each denied action shows a notification and appears in `/permissions` under the Recently denied tab, where you can press `r` to retry it with a manual approval.

If the classifier blocks an action 3 times in a row or 20 times total, auto mode pauses and Claude Code resumes prompting. Approving the prompted action resumes auto mode. These thresholds are not configurable. Any allowed action resets the consecutive counter, while the total counter persists for the session and resets only when its own limit triggers a fallback.

In [non-interactive mode](https://code.claude.com/docs/en/non-interactive mode) with the `-p` flag, repeated blocks abort the session since there is no user to prompt.

Repeated blocks usually mean the classifier is missing context about your infrastructure. Use `/feedback` to report false positives, or have an administrator [configure trusted infrastructure](https://code.claude.com/docs/en/configure trusted infrastructure).

<AccordionGroup>
  <Accordion title="How the classifier evaluates actions">
    Each action goes through a fixed decision order. The first matching step wins:

    1. Actions matching your [allow or deny rules](https://code.claude.com/docs/en/allow or deny rules) resolve immediately
    2. Read-only actions and file edits in your working directory are auto-approved, except writes to [protected paths](https://code.claude.com/docs/en/protected paths)
    3. Everything else goes to the classifier
    4. If the classifier blocks, Claude receives the reason and tries an alternative

    On entering auto mode, broad allow rules that grant arbitrary code execution are dropped:

    * Blanket `Bash(*)` or `PowerShell(*)`
    * Wildcarded interpreters like `Bash(python*)`
    * Package-manager run commands
    * `Agent` allow rules

    Narrow rules like `Bash(npm test)` carry over. Dropped rules are restored when you leave auto mode.

    The classifier sees user messages, tool calls, and your CLAUDE.md content. Tool results are stripped, so hostile content in a file or web page cannot manipulate it directly. A separate server-side probe scans incoming tool results and flags suspicious content before Claude reads it. For more on how these layers work together, see the [auto mode announcement](https://code.claude.com/docs/en/auto mode announcement) and the [engineering deep dive](https://code.claude.com/docs/en/engineering deep dive).
  </Accordion>

  <Accordion title="How auto mode handles subagents">
    The classifier checks [subagent](https://code.claude.com/docs/en/subagent) work at three points:

    1. Before a subagent starts, the delegated task description is evaluated, so a dangerous-looking task is blocked at spawn time.
    2. While the subagent runs, each of its actions goes through the classifier with the same rules as the parent session, and any `permissionMode` in the subagent's frontmatter is ignored.
    3. When the subagent finishes, the classifier reviews its full action history; if that return check flags a concern, a security warning is prepended to the subagent's results.
  </Accordion>

  <Accordion title="Cost and latency">
    The classifier runs on a server-configured model that is independent of your `/model` selection, so switching models does not change classifier availability. Classifier calls count toward your token usage. Each check sends a portion of the transcript plus the pending action, adding a round-trip before execution. Reads and working-directory edits outside protected paths skip the classifier, so the overhead comes mainly from shell commands and network operations.
  </Accordion>
</AccordionGroup>

## Allow only pre-approved tools with dontAsk mode

`dontAsk` mode auto-denies every tool call that would otherwise prompt. Only actions matching your `permissions.allow` rules and [read-only Bash commands](https://code.claude.com/docs/en/read-only Bash commands) can execute; explicit `ask` rules are denied rather than prompting. This makes the mode fully non-interactive for CI pipelines or restricted environments where you pre-define exactly what Claude may do.

Set it at startup with the flag:

```bash theme={null}
claude --permission-mode dontAsk
```

## Skip all checks with bypassPermissions mode

`bypassPermissions` mode disables permission prompts and safety checks so tool calls execute immediately. As of v2.1.126 this includes writes to [protected paths](https://code.claude.com/docs/en/protected paths), which earlier versions still prompted for. Removals targeting the filesystem root or home directory, such as `rm -rf /` and `rm -rf ~`, still prompt as a circuit breaker against model error. Only use this mode in isolated environments like containers, VMs, or dev containers without internet access, where Claude Code cannot damage your host system.

You cannot enter `bypassPermissions` from a session that was started without one of the enabling flags; restart with one to enable it:

```bash theme={null}
claude --permission-mode bypassPermissions
```

The `--dangerously-skip-permissions` flag is equivalent.

<Warning>
  `bypassPermissions` offers no protection against prompt injection or unintended actions. For background safety checks without prompts, use [auto mode](https://code.claude.com/docs/en/auto mode) instead. Administrators can block this mode by setting `permissions.disableBypassPermissionsMode` to `"disable"` in [managed settings](https://code.claude.com/docs/en/managed settings).
</Warning>

## Protected paths

Writes to a small set of paths are never auto-approved, in every mode except `bypassPermissions`. This prevents accidental corruption of repository state and Claude's own configuration. In `default`, `acceptEdits`, and `plan` these writes prompt; in `auto` they route to the classifier; in `dontAsk` they are denied; in `bypassPermissions` they are allowed.

Protected directories:

* `.git`
* `.vscode`
* `.idea`
* `.husky`
* `.claude`, except for `.claude/commands`, `.claude/agents`, `.claude/skills`, and `.claude/worktrees` where Claude routinely creates content

Protected files:

* `.gitconfig`, `.gitmodules`
* `.bashrc`, `.bash_profile`, `.zshrc`, `.zprofile`, `.profile`
* `.ripgreprc`
* `.mcp.json`, `.claude.json`

## See also

* [Permissions](https://code.claude.com/docs/en/Permissions): allow, ask, and deny rules; managed policies
* [Configure auto mode](https://code.claude.com/docs/en/Configure auto mode): tell the classifier which infrastructure your organization trusts
* [Hooks](https://code.claude.com/docs/en/Hooks): custom permission logic via `PreToolUse` and `PermissionRequest` hooks
* [Ultraplan](https://code.claude.com/docs/en/Ultraplan): run plan mode in a Claude Code on the web session with browser-based review
* [Security](https://code.claude.com/docs/en/Security): safeguards and best practices
* [Sandboxing](https://code.claude.com/docs/en/Sandboxing): filesystem and network isolation for Bash commands
* [Non-interactive mode](https://code.claude.com/docs/en/Non-interactive mode): run Claude Code with the `-p` flag
