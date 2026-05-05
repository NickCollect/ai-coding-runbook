---
type: summary
source: 01_Raw/code.claude.com/docs/en/ultraplan.md
source_url: https://code.claude.com/docs/en/ultraplan
title: "Plan in the cloud with ultraplan"
summarized_at: 2026-05-05
entities_referenced: [Permission-mode, Native-interface]
concepts_referenced: []
---

**Research preview, v2.1.91+**. `/ultraplan` hands a planning task from local CLI to a Claude Code on the web session running in plan mode. Cloud Claude drafts the plan; you keep working in your terminal. Review/comment on the plan in browser, then choose where to execute (cloud or send back to terminal).

**Why use it**: targeted feedback (comment on individual sections), hands-off drafting (terminal stays free), flexible execution (run on web → PR, or teleport back to terminal).

**Requirements**: Claude Code on the web account + GitHub repo. NOT available on Bedrock/Vertex/Foundry. Uses default cloud environment (auto-creates if missing on first launch).

**Three launch paths**:
- Command: `/ultraplan migrate the auth service from sessions to JWTs`
- Keyword: include word `ultraplan` anywhere in a normal prompt
- From local plan: when local plan completes, choose **No, refine with Ultraplan on Claude Code on the web** in the approval dialog (skips confirmation since selection IS the confirmation)

If Remote Control is active, it disconnects when ultraplan starts (both occupy claude.ai/code interface, only one connectable).

**CLI status indicator**:
- `◇ ultraplan` — researching/drafting
- `◇ ultraplan needs your input` — clarifying question; open session link
- `◆ ultraplan ready` — review in browser

`/tasks` → ultraplan entry → detail view with session link, agent activity, **Stop ultraplan** action (archives cloud session, clears indicator, nothing saved to terminal).

**Browser review surface**:
- **Inline comments**: highlight passage → comment → Claude addresses
- **Emoji reactions** for approval/concern signal
- **Outline sidebar** for navigation between sections
- Iterate as many revisions as needed

**Choose where to execute**:
- **Approve Claude's plan and start coding** (browser) — implements in same cloud session; review diff + create PR from web when done
- **Approve plan and teleport back to terminal** (browser) — appears when launched from CLI and terminal still polling; web session archived. Terminal shows **Ultraplan approved** dialog with three options:
  - **Implement here** — inject plan into current conversation, continue
  - **Start new session** — clear current, fresh start with only the plan as context (prints `claude --resume` command for previous convo)
  - **Cancel** — save plan to file without executing; prints file path
