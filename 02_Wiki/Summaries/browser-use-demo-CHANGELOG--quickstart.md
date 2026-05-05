---
type: summary
source: 01_Raw/github/anthropics/claude-quickstarts/browser-use-demo/CHANGELOG.md
source_url: https://github.com/anthropics/claude-quickstarts/blob/main/browser-use-demo/CHANGELOG.md
title: "Claude Quickstarts — browser-use-demo CHANGELOG (Playwright derivation tracking)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Records modifications to files derived from or inspired by Microsoft Playwright source. Required by the legal notice in the root `CLAUDE.md` (changes to copyright-bearing files must be tracked here).

**Tracked files:**

- `browser_use_demo/browser_tool_utils/browser_dom_script.js` (modified 9/23/25). Original: Playwright `packages/injected/src/ariaSnapshot.ts`. Adapted Playwright's accessibility-tree generation for the browser tools API. Implements accessibility-tree extraction with element-reference tracking, visibility filtering, and YAML-formatted output.
- `browser_use_demo/browser_tool_utils/browser_element_script.js` (modified 9/23/25). Original: Playwright element-interaction patterns. Implements element finding/interaction logic inspired by Playwright's reliable element targeting and coordinate calculation.
- `browser_use_demo/tools/browser.py` — multiple revisions:
  - 9/23/25 — click emulation methods developed with reference to Playwright source for reliable mouse interactions.
  - 10/6/25 — fixed incorrect path to `browser_tool_utils` (parent vs grandparent), missing `cdp_url` initialization in `__init__` causing AttributeError in cleanup, and incorrect import path for `browser_key_map`.
  - 10/14/25 — `_scroll` and `_scroll_to` now return screenshots after scrolling (with 0.5s stabilization delay) for visual feedback to the model after scroll actions, consistent with `navigate`.
  - 12/19/25 — added `hover` action (Playwright `mouse.move()`) for tooltips/dropdowns/hover states, and `execute_js` action (Playwright `page.evaluate()`) returning the result of the last expression.
  - 1/18/26 — added clarifying comment in the `options` property explaining the fixed 1920x1080 dimensions with empirical coordinate correction, and pointing users at the "Handle coordinate scaling" section in the computer-use docs for the recommended client-side downscaling approach.

The file functions as the project's audit trail for Playwright-derived code rather than a release changelog.
