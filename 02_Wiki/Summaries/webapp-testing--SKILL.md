---
type: summary
source: 01_Raw/github/anthropics/skills/skills/webapp-testing/SKILL.md
title: "webapp-testing (Anthropic Skills)"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Skill for interacting with and testing local web applications using **Playwright** (Python). Verifies frontend functionality, debugs UI behavior, captures browser screenshots, views browser logs.

Helper script: `scripts/with_server.py` (manages server lifecycle, supports multiple servers). **Run with `--help` first** — DO NOT read source unless customization absolutely necessary (these scripts can pollute context window).

**Decision tree**:
- Static HTML → read file directly to identify selectors → write Playwright script.
- Dynamic webapp + server not running → use `with_server.py --help` then helper.
- Dynamic webapp + server running → reconnaissance-then-action: navigate → wait for `networkidle` → screenshot/inspect DOM → identify selectors → execute actions.

**Multi-server example**:
```bash
python scripts/with_server.py \
  --server "cd backend && python server.py" --port 3000 \
  --server "cd frontend && npm run dev" --port 5173 \
  -- python your_automation.py
```

**Automation script template**: pure Playwright (servers managed by helper). Always launch chromium headless. CRITICAL: `page.wait_for_load_state('networkidle')` after `page.goto(...)` for dynamic apps before any DOM inspection.

**Reconnaissance pattern**:
```python
page.screenshot(path='/tmp/inspect.png', full_page=True)
content = page.content()
page.locator('button').all()
```

**Common pitfall**: inspecting DOM before `networkidle` on dynamic apps.

**Best practices**: bundled scripts as black boxes (use `--help`, don't ingest source); `sync_playwright()` for sync scripts; always close browser; descriptive selectors (`text=`, `role=`, CSS, IDs); appropriate waits (`wait_for_selector`, `wait_for_timeout`).

**Reference files** (`examples/`): `element_discovery.py`, `static_html_automation.py`, `console_logging.py`.
