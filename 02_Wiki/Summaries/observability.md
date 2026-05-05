---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/observability.md
source_url: https://code.claude.com/docs/en/agent-sdk/observability
title: "Observability with OpenTelemetry (Agent SDK)"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Hooks]
concepts_referenced: [Agentic-loop]
---

The Claude Agent SDK exports OpenTelemetry traces, metrics, and log events to any OTLP backend (Honeycomb, Datadog, Grafana, Langfuse, self-hosted collector). OTel instrumentation lives in the Claude Code CLI binary the SDK spawns; the SDK passes config through env vars.

Three independent signals, each with its own enable switch:
- **Metrics** (`OTEL_METRICS_EXPORTER`) — counters for tokens, cost, sessions, lines of code, tool decisions.
- **Log events** (`OTEL_LOGS_EXPORTER`) — prompts, API requests, errors, tool results.
- **Traces** (`OTEL_TRACES_EXPORTER` + `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`, beta) — spans for each interaction, model request, tool call, hook.

Master switch: `CLAUDE_CODE_ENABLE_TELEMETRY=1`. Then set OTLP endpoint/headers (e.g. `OTEL_EXPORTER_OTLP_ENDPOINT`, `OTEL_EXPORTER_OTLP_HEADERS`).

Gotcha: Do NOT use the `console` exporter — it collides with the SDK's stdout message channel. Point at a local OTLP collector or Jaeger instead.

Trace span hierarchy:
- `claude_code.interaction` wraps one agent loop turn.
- `claude_code.llm_request` per Claude API call (with token attrs).
- `claude_code.tool` per tool invocation, with `claude_code.tool.blocked_on_user` (permission wait) and `claude_code.tool.execution` children.
- `claude_code.hook` per hook (needs `ENABLE_BETA_TRACING_DETAILED=1` + `BETA_TRACING_ENDPOINT`).

Subagent spawned via Task tool: its spans nest under the parent's `claude_code.tool` span — full delegation chain in one trace.

Trace context propagation: SDK auto-injects W3C `TRACEPARENT` / `TRACESTATE` into the CLI subprocess and into Bash/PowerShell tool commands, so `claude_code.interaction` becomes a child of the caller's span. Set `TRACEPARENT` explicitly to override.

Default export intervals: metrics 60s, traces/logs 5s. Lower via `OTEL_METRIC_EXPORT_INTERVAL` etc. for short-lived calls (data may be lost on hard kill).

Sensitive data is excluded by default. Opt-in vars: `OTEL_LOG_USER_PROMPTS=1`, `OTEL_LOG_TOOL_DETAILS=1`, `OTEL_LOG_TOOL_CONTENT=1` (60 KB cap), `OTEL_LOG_RAW_API_BODIES` (full Messages API JSON, includes conversation history with extended-thinking redacted).

Tag agents via `OTEL_SERVICE_NAME` and `OTEL_RESOURCE_ATTRIBUTES`. Default `service.name` is `claude-code`.
