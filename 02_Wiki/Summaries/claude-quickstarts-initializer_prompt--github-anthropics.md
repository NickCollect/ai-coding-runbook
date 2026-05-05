---
type: summary
source: 01_Raw/github/anthropics/claude-quickstarts/autonomous-coding/prompts/initializer_prompt.md
source_url: https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/prompts/initializer_prompt.md
title: "claude-quickstarts — Autonomous Coding Initializer Agent System Prompt"
summarized_at: 2026-05-05
entities_referenced: ["Anthropic"]
concepts_referenced: ["autonomous coding", "initializer agent", "system prompt", "feature_list.json", "init.sh", "git initialization"]
---

System prompt for the first (initializer) agent in the autonomous coding quickstart.

Four primary tasks:
1. Create feature_list.json: Based on app_spec.txt; minimum 200 test cases with category (functional/style), description, steps, passes:false; at least 25 tests with 10+ steps; never modify existing features in future sessions
2. Create init.sh: Environment setup script (install deps, start servers, print access info)
3. Initialize Git: First commit with feature_list.json, init.sh, README.md
4. Create Project Structure: Based on app_spec.txt stack spec

Before session ends: commit all work, create claude-progress.txt with session summary.
