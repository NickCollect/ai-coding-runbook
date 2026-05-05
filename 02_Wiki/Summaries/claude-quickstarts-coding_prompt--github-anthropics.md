---
type: summary
source: 01_Raw/github/anthropics/claude-quickstarts/autonomous-coding/prompts/coding_prompt.md
source_url: https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/prompts/coding_prompt.md
title: "claude-quickstarts — Autonomous Coding Agent System Prompt"
summarized_at: 2026-05-05
entities_referenced: ["Anthropic"]
concepts_referenced: ["autonomous coding", "agent prompt", "system prompt", "browser automation", "puppeteer", "feature_list.json", "git workflow"]
---

System prompt for the coding agent in the autonomous coding quickstart (subsequent sessions after initialization).

10-Step Workflow:
1. Get Your Bearings: pwd, ls, read app_spec.txt, feature_list.json, claude-progress.txt, git log
2. Start Servers: run init.sh if present
3. Verification Test (MANDATORY): run 1-2 passing feature tests to catch regressions before new work
4. Choose One Feature: pick highest-priority passes:false item
5. Implement: write frontend + backend code
6. Verify with Browser Automation (CRITICAL): use puppeteer tools — navigate, screenshot, click, fill; no shortcuts
7. Update feature_list.json: ONLY change passes field after verified; never remove/edit test descriptions
8. Commit Progress: descriptive git commit with verification screenshots
9. Update claude-progress.txt: session summary, completion status
10. End Session Cleanly: commit all code, no broken features

Goal: Production-quality app with all 200+ tests passing. Fix broken tests before implementing new features.
