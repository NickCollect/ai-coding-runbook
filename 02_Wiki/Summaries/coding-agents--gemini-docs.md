---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/coding-agents.md
source_url: https://ai.google.dev/gemini-api/docs/coding-agents
title: "Gemini API — Setting Up Coding Assistants with Gemini MCP and Skills"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Setting Up Coding Assistants with Gemini MCP and Skills

Source is in Traditional Chinese (crawler localization).

## Problem

AI coding assistants have knowledge cutoff dates, so they may suggest deprecated patterns for the Gemini API and miss new features. These tools address this gap.

## Solution: Two Complementary Tools

### 1. Gemini Docs MCP

Public MCP server hosted at `https://gemini-api-docs-mcp.dev`.

Install:
```bash
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

Adds `search_documentation` function for agents to fetch live API definitions and integration patterns from official Gemini docs.

### 2. Gemini API Skills

Built-in rules and best practices directly in the assistant environment. Works with MCP for doc generation; falls back to fetching `llms.txt` from `ai.google.dev` if MCP not installed.

Installation via supported tools:

**skills.sh** (recommended — open standard for portable agent behavior):
```bash
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

**Context7** (for users in the Context7 ecosystem):
```bash
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

## Available Skills

- **`gemini-api-dev`**: Foundation skill for general-purpose Gemini app development. Covers: current models (Gemini 3.1 Pro/Flash), multimodal prompting, function calling, structured output, common integration patterns. Avoids deprecated models.

## When to Use

Set up both tools if using AI coding assistants (Cursor, Windsurf, GitHub Copilot, Claude Code, etc.) for Gemini API development. Ensures the assistant knows current model names, API patterns, and SDK versions.
