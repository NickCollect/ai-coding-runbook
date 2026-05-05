---
type: summary
source: 01_Raw/code.claude.com/docs/en/desktop-scheduled-tasks.md
source_url: https://code.claude.com/docs/en/desktop-scheduled-tasks
title: "Schedule recurring tasks in Claude Code Desktop"
summarized_at: 2026-05-05
entities_referenced: [Scheduled-task, Routine, Permission-mode, MCP-server, Native-interface]
concepts_referenced: []
---

Desktop's **Routines** page creates local scheduled tasks (and remote routines). Local task = runs on your machine, fires only while app is open + computer awake; remote routine = Anthropic-managed cloud, fires anytime + can trigger on API/GitHub events.

**Three scheduling options compared**:

| | Cloud (Routines) | Desktop (this doc) | `/loop` |
|---|---|---|---|
| Runs on | Anthropic cloud | Your machine | Your machine |
| Machine on required | No | Yes | Yes |
| Open session required | No | No | Yes |
| Persists across restarts | Yes | Yes | Restored on `--resume` if unexpired |
| Local file access | No (fresh clone) | Yes | Yes |
| Min interval | 1 hour | 1 minute | 1 minute |

Use cloud for reliability without your machine; Desktop for local file/tool access; `/loop` for in-session polling.

**Default**: scheduled tasks run against current working-dir state (incl. uncommitted changes). Toggle worktree at creation for isolated Git worktree per run.

**Create**: Routines → New routine → Local. Fields: Name (kebab-case, used as folder), Description, Instructions (with model + permission mode pickers, working folder, worktree toggle), Schedule. Folder must be trusted before saving.

**Schedule presets**: Manual (run-now only), Hourly, Daily (time picker, default 9am local), Weekdays (Daily skipping Sat/Sun), Weekly (time + day pickers). For other intervals (every 15 min, first of month, one-shot at future time), ask Claude in any session in plain language ("schedule a task to run all the tests every 6 hours").

You can also create from chat: "set up a daily code review every morning at 9am" → recurring; "remind me at 3pm tomorrow to check the deploy" → one-time (auto-disables after firing).

**Execution**: Desktop checks schedule every minute while open, fires fresh session at scheduled time. Each task gets a small deterministic delay (a few minutes) to stagger API traffic. Fires desktop notification + new session under "Scheduled" sidebar section. Computer-asleep = run skipped. Enable "Keep computer awake" in Settings → Desktop app → General. **Closing laptop lid still puts computer to sleep.**

**Missed runs**: on app start / wake, Desktop checks last 7 days for misses. Runs ONE catch-up for the most recently missed time, discards older. So a daily task missed 6 days runs once on wake. Notification on catch-up. **Add temporal guardrails to prompts**: "Only review today's commits. If after 5pm, just summarize what was missed."

**Permissions**: per-task permission mode + allow rules from `~/.claude/settings.json`. Ask-mode + un-permitted tool = stall until you approve (session stays open). Mitigate by running once after creation and "always allow" each prompt — future runs auto-approve. Review/revoke from task detail page.

**Manage**: Run now, Status (Active/Paused), Edit, Review history (skipped runs show reason: asleep / previous run still running / other tasks running), Review allowed permissions, Delete (archives sessions).

**Edit prompt on disk**: `~/.claude/scheduled-tasks/<task-name>/SKILL.md` (or under `CLAUDE_CONFIG_DIR`). YAML frontmatter `name`/`description` + body prompt. Schedule/folder/model/enabled state are NOT in this file — only via Edit form or Claude.
