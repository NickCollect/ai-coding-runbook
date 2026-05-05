---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/hookify/examples/require-tests-stop.local.md
title: "Hookify example: require-tests-run"
summarized_at: 2026-05-05
entities_referenced: [Hooks]
concepts_referenced: []
---

Example hookify rule shipped in `hookify/examples/`. Demonstrates a `stop`-event rule with `block` action and a `not_contains` condition on the session transcript.

```yaml
---
name: require-tests-run
enabled: false
event: stop
action: block
conditions:
  - field: transcript
    operator: not_contains
    pattern: npm test|pytest|cargo test
---
```

Body message instructs Claude that no test commands were detected in the transcript, listing `npm test`, `pytest`, `cargo test` as examples.

**Effect**: blocks Claude from stopping the session if no test command appears in the transcript. Disabled by default (`enabled: false`) — enable only when strict test enforcement is desired.
