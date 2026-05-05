---
type: summary
source: 01_Raw/code.claude.com/docs/en/web-quickstart.md
source_url: https://code.claude.com/docs/en/web-quickstart
title: "Get started with Claude Code on the web"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, Permission-mode]
concepts_referenced: []
---

**Research preview** for Pro/Max/Team users + Enterprise with premium or Chat+CC seats. Cloud Claude Code at `claude.ai/code` (browser or mobile app). Anthropic-managed VM clones repo, makes changes, pushes branch for you to review. Sessions persist across devices.

**Best for**: parallel tasks (each in own session/branch), repos you don't have locally, tasks not needing frequent steering, code Q&A/exploration without local checkout.

**Session flow**:
1. Clone + setup script runs
2. Network access set per environment access level
3. Claude works (analyze → edit → run tests → check work). You can watch/steer or step away.
4. Claude pushes branch to GitHub at stopping point. Review diff, leave inline comments, create PR, or message to keep going. **Session doesn't close after PR** — further edits all in same conversation.

**Comparison** (where things run / what config is available):
| | On the web | Remote Control | Terminal CLI | Desktop |
|---|---|---|---|---|
| Code runs on | Anthropic cloud | Your machine | Your machine | Your machine OR cloud |
| Chat from | claude.ai / mobile | claude.ai / mobile | Terminal | Desktop UI |
| Local config | No, repo only | Yes | Yes | Yes for local |
| Requires GitHub | Yes (or `--remote` to bundle local) | No | No | Only for cloud |
| Keeps running on disconnect | Yes | While terminal stays open | No | Depends |
| Permission modes | Auto accept edits, Plan | Ask, Auto accept edits, Plan | All | Depends |

**Setup** (one-time):
1. Visit `claude.ai/code`, sign in
2. Install Claude GitHub App, grant repo access (or create empty GitHub repo first for new project)
3. Create cloud environment (Name + Network access [`Trusted` default = npm/PyPI/RubyGems allowed, general internet blocked] + Env vars in `.env` format [no quotes — kept literally] + optional Setup script [cached])

**From terminal alternative** (`/web-setup` reads local `gh` token, links to Claude account, auto-creates env). NOT available with ZDR. If `gh` not installed/authed, falls back to browser onboarding.

**Start a task**:
1. Select repo + branch (multiple repos in one session OK)
2. Choose permission mode: **Auto accept edits** (default; pushes branch without approval) or **Plan mode**. Cloud has NO Ask, Auto, or Bypass.
3. Describe task specifically: name files/functions, paste error output, describe expected behavior. Each task = own session + branch.

**Pre-fill via URL params** (for issue-tracker integration etc.):
- `prompt` (alias `q`) — text to prefill
- `prompt_url` — URL to fetch (CORS required; ignored if `prompt` set)
- `repositories` (alias `repo`) — comma-sep `owner/repo` slugs
- `environment` — env name or ID
URL-encoded: `https://claude.ai/code?prompt=Fix%20the%20login%20bug&repositories=acme/webapp`

**Review/iterate**: diff indicator (`+42 -18`) opens diff view. Inline comments queue until next message — bundled together so Claude sees "at `src/auth.ts:47`, don't catch the error here" with main instruction. **Create PR** opens it (full / draft / GitHub compose page). Session stays live after PR — paste CI failures or reviewer comments to address. Auto-fix PRs available for monitoring PRs automatically.

**Common issues**:
- No repos after GitHub connect → Settings → Applications → Claude → Configure → verify repo listed (private repos need same auth)
- "Not available for the selected organization" → Enterprise admin must enable
- `/web-setup` "Unknown command" → run inside `claude` CLI not shell; if still fails CLI is older than v2.1.80 OR you're auth'd via API key/third-party
- Session keeps running after closing tab → BY DESIGN. Continues until current task done then idles. Archive or delete to clean up.
