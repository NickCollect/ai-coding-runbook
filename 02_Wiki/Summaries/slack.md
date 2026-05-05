---
type: summary
source: 01_Raw/code.claude.com/docs/en/slack.md
source_url: https://code.claude.com/docs/en/slack
title: "Claude Code in Slack"
summarized_at: 2026-05-05
entities_referenced: [Native-interface]
concepts_referenced: []
---

Claude Code integrated with Slack via the existing Claude for Slack app. `@Claude` mention with coding intent → auto-routes to a Claude Code session on the web.

**Prereqs**: Pro/Max/Team/Enterprise with Claude Code seats; **Claude Code on the web access enabled**; GitHub account connected with at least one authenticated repo; Slack account linked to Claude.

**Setup**:
1. Workspace admin installs Claude app from Slack App Marketplace
2. Authenticate individual account: Claude app → App Home → Connect → browser auth flow
3. Configure Claude Code on the web at `claude.ai/code` (GitHub + repo)
4. Choose Routing Mode: **Code only** (all @mentions go to Claude Code sessions) or **Code + Chat** (Claude analyzes intent and routes to Code or Chat). In Code+Chat, "Retry as Code" / pick-Chat options available per message.
5. Add Claude to channels via `/invite @Claude` (NOT auto-added)

**Important**: Slack integration **only works in channels (public/private), NOT in DMs**.

**How it works**:
- Auto-detection of coding intent
- Context gathering: in threads → all thread messages; in channels → recent channel messages
- Session flow: detection → cloud session created → status updates posted to thread → completion @mention with summary + action buttons
- Action buttons: **View Session** (opens full transcript on web), **Create PR**, **Retry as Code**, **Change Repo**

**Repo selection**: Claude auto-picks based on conversation context; multi-repo possibilities show dropdown.

**Security warning**: when @Claude is invoked, it has access to the conversation context — may follow directions from other messages in context. Use only in trusted Slack conversations.

**Access**:
- Each user runs sessions under their own Claude account (own usage/rate limits)
- Repository access = what user personally connected
- Workspace admins control app install / Enterprise Grid distribution / removal
- Channel-based access control: Claude only responds where invited
- Enterprise/Team accounts: Slack-initiated sessions visible to org

**Limits**: GitHub-only; one PR per session; uses individual rate limits; users without web access only get standard chat.

**Best practices**: be specific (file/function/error names), provide context (repo if not obvious), define success ("done = PR with tests"), use threads.

**When to use Slack vs web**: Slack when context already in discussion / async / collaborative visibility. Web when uploading files / real-time interaction / longer complex tasks.
