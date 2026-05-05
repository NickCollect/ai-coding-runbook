---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/aistudio-fullstack.md
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack
title: "Gemini API — Full-Stack App Development in AI Studio"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Full-Stack App Development in AI Studio

Source is in Simplified Chinese (crawler localization).

## Overview

AI Studio supports full-stack development beyond client-side prototypes. Server-side runtime lets you manage secrets, connect to external APIs, and build real-time multiplayer experiences.

## Server-Side Runtime (Node.js)

AI Studio apps can now include server-side components powered by Node.js via the Antigravity Agent.

Capabilities:
- **Server-side logic**: Code not exposed to clients
- **npm packages**: Antigravity Agent installs and uses packages from npm ecosystem automatically (no manual `npm install` needed — just tell the Agent what you need)
- **Secrets management**: Securely use API keys and credentials

Example: "Use `axios` to fetch data from an external API" → Agent handles package install and import.

## Multi-player / Real-time

Server-side runtime enables real-time multi-player experiences — shared state across users in the same app session.

## Difference from Build Mode

- Build Mode: AI-assisted development via Antigravity Agent (general vibe coding)
- Fullstack development: Specific capability within AI Studio apps for server-side Node.js logic

## Use Cases

- Apps requiring server-to-server API calls (e.g., calling external databases, CRMs, APIs)
- Apps requiring secrets (e.g., payment APIs, internal enterprise APIs)
- Collaborative real-time applications
- Serverless backend logic

## See Also

- `aistudio-build-mode.md`: Build Mode overview with Antigravity Agent
- Antigravity documentation: `antigravity.google/docs/agent`
