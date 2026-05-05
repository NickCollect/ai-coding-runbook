---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/computer-use.md
source_url: https://ai.google.dev/gemini-api/docs/computer-use
title: "Gemini API — Computer Use"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Computer Use

Source is in Turkish (crawler localization).

## Overview

Computer Use enables building browser control agents. The model "sees" the screen via screenshots and proposes UI actions (mouse clicks, keyboard input). Client code must execute the actions (similar to function calling).

## Use Cases

- Automate repetitive form filling or data entry on websites
- Automated testing of web applications and user flows
- Web research across multiple sites
- E-commerce product info, price, and review aggregation

## Model

`gemini-2.5-computer-use-preview-10-2025` — specialized for browser automation.

## Agent Loop (4 Steps)

1. **Send request**: Include Computer Use tool in request + user's task
2. **Get model response**: Model analyzes screenshot + task → returns `function_call` with UI action (e.g., "click (x,y)") + optional `safety_decision`
3. **Execute action**: Client executes the `function_call`:
   - **Normal/allowed**: Execute directly
   - **Requires confirmation (`require_confirmation`)**: Ask user before executing (risky action)
4. **Capture new state**: Take new screenshot of current GUI + URL → send as `function_response` back to model

Repeat from step 2 until task complete, error, or "blocked" safety decision.

## Safety Decisions

- **Normal/allowed**: Action is safe (also indicated by absence of `safety_decision`)
- **Requires confirmation**: Potentially risky action (e.g., "accept cookie banner") — user must approve
- **Blocked**: Action rejected by safety system

## Prerequisites

- **Secure execution environment**: Run agent in sandbox (VM, container, or dedicated browser profile) with limited permissions.
- Client code responsible for executing actions against target environment (real browser, Playwright, Selenium, etc.).

## Quick Start

- Reference app: https://github.com/google/computer-use-preview/
- Demo environment: http://gemini.browserbase.com
