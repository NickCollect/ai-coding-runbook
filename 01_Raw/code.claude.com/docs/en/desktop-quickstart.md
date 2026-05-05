---
source_url: https://code.claude.com/docs/en/desktop-quickstart
fetched_at: 2026-05-04T15:05:21.297066+00:00
fetch_method: mintlify_md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get started with the desktop app

> Install Claude Code on desktop and start your first coding session

The desktop app gives you Claude Code with a graphical interface built for running multiple sessions side by side: a sidebar for managing parallel work, a drag-and-drop layout with an integrated terminal and file editor, visual diff review, live app preview, GitHub PR monitoring with auto-merge, and scheduled tasks. No terminal required.

<CardGroup cols={2}>
  <Card title="Download for macOS" icon="apple" href="https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect?utm_source=claude_code&utm_medium=docs">
    Universal build for Intel and Apple Silicon
  </Card>

  <Card title="Download for Windows" icon="windows" href="https://claude.ai/api/desktop/win32/x64/setup/latest/redirect?utm_source=claude_code&utm_medium=docs">
    For x64 processors
  </Card>
</CardGroup>

For Windows ARM64, download the [ARM64 installer](https://code.claude.com/docs/en/ARM64 installer). The desktop app is not available on Linux; use the [CLI](https://code.claude.com/docs/en/CLI) instead.

<Note>
  Claude Code requires a [Pro, Max, Team, or Enterprise subscription](https://code.claude.com/docs/en/Pro, Max, Team, or Enterprise subscription).
</Note>

This page walks through installing the app and starting your first session. If you're already set up, see [Use Claude Code Desktop](https://code.claude.com/docs/en/Use Claude Code Desktop) for the full reference.

The desktop app has three tabs:

* **Chat**: General conversation with no file access, similar to claude.ai.
* **Cowork**: An autonomous background agent that works on tasks in a cloud VM with its own environment. It can run independently while you do other work.
* **Code**: An interactive coding assistant with direct access to your local files. You review and approve each change in real time.

Chat and Cowork are covered in the [Claude Desktop support articles](https://code.claude.com/docs/en/Claude Desktop support articles). This page focuses on the **Code** tab.

## Install

<Steps>
  <Step title="Install and sign in">
    Download the installer for your platform from the links above and run it. Launch Claude from your Applications folder on macOS or the Start menu on Windows, then sign in with your Anthropic account.
  </Step>

  <Step title="Open the Code tab">
    Click the **Code** tab at the top center. If clicking Code prompts you to upgrade, you need to [subscribe to a paid plan](https://code.claude.com/docs/en/subscribe to a paid plan) first. If it prompts you to sign in online, complete the sign-in and restart the app. If you see a 403 error, see [authentication troubleshooting](https://code.claude.com/docs/en/authentication troubleshooting).
  </Step>
</Steps>

The desktop app includes Claude Code. You don't need to install Node.js or the CLI separately. To use `claude` from the terminal, install the CLI separately. See [Get started with the CLI](https://code.claude.com/docs/en/Get started with the CLI).

## Start your first session

With the Code tab open, choose a project and give Claude something to do.

<Steps>
  <Step title="Choose an environment and folder">
    Select **Local** to run Claude on your machine using your files directly. Click **Select folder** and choose your project directory.

    <Tip>
      Start with a small project you know well. It's the fastest way to see what Claude Code can do. On Windows, [Git](https://code.claude.com/docs/en/Git) must be installed for local sessions to work. Most Macs include Git by default.
    </Tip>

    You can also select:

    * **Remote**: Run sessions on Anthropic's cloud infrastructure that continue even if you close the app. Remote sessions use the same infrastructure as [Claude Code on the web](https://code.claude.com/docs/en/Claude Code on the web).
    * **SSH**: Connect to a remote machine over SSH, such as your own servers, cloud VMs, or dev containers. Desktop installs Claude Code on the remote machine automatically the first time you connect.
  </Step>

  <Step title="Choose a model">
    Select a model from the dropdown next to the send button. See [models](https://code.claude.com/docs/en/models) for a comparison of Opus, Sonnet, and Haiku. You can change the model later from the same dropdown.
  </Step>

  <Step title="Tell Claude what to do">
    Type what you want Claude to do:

    * `Find a TODO comment and fix it`
    * `Add tests for the main function`
    * `Create a CLAUDE.md with instructions for this codebase`

    A [session](https://code.claude.com/docs/en/session) is a conversation with Claude about your code. Each session tracks its own context and changes, so you can work on multiple tasks without them interfering with each other.
  </Step>

  <Step title="Review and accept changes">
    By default, the Code tab starts in [Ask permissions mode](https://code.claude.com/docs/en/Ask permissions mode), where Claude proposes changes and waits for your approval before applying them. You'll see:

    1. A [diff view](https://code.claude.com/docs/en/diff view) showing exactly what will change in each file
    2. Accept/Reject buttons to approve or decline each change
    3. Real-time updates as Claude works through your request

    If you reject a change, Claude will ask how you'd like to proceed differently. Your files aren't modified until you accept.
  </Step>
</Steps>

## Now what?

You've made your first edit. For the full reference on everything Desktop can do, see [Use Claude Code Desktop](https://code.claude.com/docs/en/Use Claude Code Desktop). Here are some things to try next.

**Interrupt and steer.** You can interrupt Claude at any point. If it's going down the wrong path, click the stop button or type your correction and press **Enter**. Claude stops what it's doing and adjusts based on your input. You don't have to wait for it to finish or start over.

**Give Claude more context.** Type `@filename` in the prompt box to pull a specific file into the conversation, attach images and PDFs using the attachment button, or drag and drop files directly into the prompt. The more context Claude has, the better the results. See [Add files and context](https://code.claude.com/docs/en/Add files and context).

**Use skills for repeatable tasks.** Type `/` or click **+** → **Slash commands** to browse [built-in commands](https://code.claude.com/docs/en/built-in commands), [custom skills](https://code.claude.com/docs/en/custom skills), and plugin skills. Skills are reusable prompts you can invoke whenever you need them, like code review checklists or deployment steps.

**Review changes before committing.** After Claude edits files, a `+12 -1` indicator appears. Click it to open the [diff view](https://code.claude.com/docs/en/diff view), review modifications file by file, and comment on specific lines. Claude reads your comments and revises. Click **Review code** to have Claude evaluate the diffs itself and leave inline suggestions.

**Adjust how much control you have.** Your [permission mode](https://code.claude.com/docs/en/permission mode) controls the balance. Ask permissions (default) requires approval before every edit. Auto accept edits auto-accepts file edits for faster iteration. Plan mode lets Claude map out an approach without touching any files, which is useful before a large refactor.

**Add plugins for more capabilities.** Click the **+** button next to the prompt box and select **Plugins** to browse and install [plugins](https://code.claude.com/docs/en/plugins) that add skills, agents, MCP servers, and more.

**Arrange your workspace.** Drag the chat, diff, terminal, file, and preview panes into whatever layout you want. Open the terminal with **Ctrl+\`** to run commands alongside your session, or click a file path to open it in the file pane. See [Arrange your workspace](https://code.claude.com/docs/en/Arrange your workspace).

**Preview your app.** Click the **Preview** dropdown to run your dev server directly in the desktop. Claude can view the running app, test endpoints, inspect logs, and iterate on what it sees. See [Preview your app](https://code.claude.com/docs/en/Preview your app).

**Track your pull request.** After opening a PR, Claude Code monitors CI check results and can automatically fix failures or merge the PR once all checks pass. See [Monitor pull request status](https://code.claude.com/docs/en/Monitor pull request status).

**Put Claude on a schedule.** Set up [scheduled tasks](https://code.claude.com/docs/en/scheduled tasks) to run Claude automatically on a recurring basis: a daily code review every morning, a weekly dependency audit, or a briefing that pulls from your connected tools.

**Scale up when you're ready.** Open [parallel sessions](https://code.claude.com/docs/en/parallel sessions) from the sidebar to work on multiple tasks at once, each in its own Git worktree, and open the [tasks pane](https://code.claude.com/docs/en/tasks pane) to watch the subagents and background commands a session has running. Open a [side chat](https://code.claude.com/docs/en/side chat) to ask a question without derailing the main thread. Send [long-running work to the cloud](https://code.claude.com/docs/en/long-running work to the cloud) so it continues even if you close the app, or [continue a session on the web or in your IDE](https://code.claude.com/docs/en/continue a session on the web or in your IDE) if a task takes longer than expected. [Connect external tools](https://code.claude.com/docs/en/Connect external tools) like GitHub, Slack, and Linear to bring your workflow together.

## Coming from the CLI?

Desktop runs the same engine as the CLI with a graphical interface. You can run both simultaneously on the same project, and they share configuration (CLAUDE.md files, MCP servers, hooks, skills, and settings). For a full comparison of features, flag equivalents, and what's not available in Desktop, see [CLI comparison](https://code.claude.com/docs/en/CLI comparison).

## What's next

* [Use Claude Code Desktop](https://code.claude.com/docs/en/Use Claude Code Desktop): permission modes, parallel sessions, diff view, connectors, and enterprise configuration
* [Troubleshooting](https://code.claude.com/docs/en/Troubleshooting): solutions to common errors and setup issues
* [Best practices](https://code.claude.com/docs/en/Best practices): tips for writing effective prompts and getting the most out of Claude Code
* [Common workflows](https://code.claude.com/docs/en/Common workflows): tutorials for debugging, refactoring, testing, and more
