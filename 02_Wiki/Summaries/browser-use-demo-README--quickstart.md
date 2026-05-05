---
type: summary
source: 01_Raw/github/anthropics/claude-quickstarts/browser-use-demo/README.md
source_url: https://github.com/anthropics/claude-quickstarts/blob/main/browser-use-demo/README.md
title: "Claude Quickstarts — browser-use-demo README"
summarized_at: 2026-05-05
entities_referenced: [Computer-use-tool-API]
concepts_referenced: []
---

Reference implementation for building browser automation with Claude using Playwright. Containerized Streamlit interface that gives Claude the ability to navigate websites, interact with DOM elements, extract content, and fill forms.

**Capabilities.** DOM access (read page structure with element references); navigation control (browse URLs, manage history); form manipulation (set input values directly); text extraction; element targeting via `ref` or coordinate parameters; smart scrolling (to specific elements or directions); page search (find and highlight text); visual capture (screenshots, zoomed regions).

**Why element-based over coordinate-based.** Element-based targeting via `ref` works across screen sizes and layouts (pixel coords break on resize); direct DOM manipulation provides structured visibility for dynamic content, hidden elements, and complex SPAs; built-in support for navigation, text extraction, and form completion.

**Quick start.** Docker + Docker Compose required. Clone, `cd claude-quickstarts/browser-use-demo`, `cp .env.example .env` and set `ANTHROPIC_API_KEY`. Display resolution defaults to 1920x1080 (16:9) for coordinate accuracy.

**Run.** `docker-compose up --build` (production), `docker-compose up --build --watch` (dev with file sync).

**Interfaces.** Main UI (Streamlit) at http://localhost:8080, NoVNC browser view at http://localhost:6080, raw VNC at localhost:5900.

**Examples.** "Navigate to news.ycombinator.com and tell me the top 3 stories", "Go to google.com and search for 'Anthropic Claude'", "Visit wikipedia.org and find information about artificial intelligence", "Navigate to github.com and search for 'playwright'". Note: current Playwright implementation hits CAPTCHAs on Google searches — recommend specifying the website in the prompt (e.g. "navigate to Anthropic.com and search for x").

**Safety.** Browser automation poses risks distinct from standard API/chat features, heightened when interacting with the internet. The README recommends running in an isolated VM/container with minimal privileges, restricting access to sensitive data, allowlisting domains, and human-in-the-loop confirmation for consequential actions. Continues with detailed safety guidance and configuration reference.
