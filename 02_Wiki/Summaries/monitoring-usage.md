---
type: summary
source: 01_Raw/code.claude.com/docs/en/monitoring-usage.md
source_url: https://code.claude.com/docs/en/monitoring-usage
title: "Monitoring (OpenTelemetry reference)"
summarized_at: 2026-05-05
entities_referenced: [Settings, Subagent, Hooks]
concepts_referenced: [Agentic-loop, Prompt-caching]
---

The OpenTelemetry reference for Claude Code (CLI). Companion to the Agent SDK observability guide — same instrumentation, since the SDK runs the CLI.

**Three signals** (each with its own enable/exporter):
- **Metrics** — counters for tokens, cost, sessions, lines of code, tool decisions. `OTEL_METRICS_EXPORTER=otlp|prometheus|console|none`.
- **Logs/events** — prompts, API requests, errors, tool results. `OTEL_LOGS_EXPORTER=otlp|console|none`.
- **Traces (beta)** — distributed spans linking each user prompt to API requests + tool executions + hook executions. Requires `CLAUDE_CODE_ENABLE_TELEMETRY=1` AND `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` AND `OTEL_TRACES_EXPORTER`.

**Quick start env vars**:
```
CLAUDE_CODE_ENABLE_TELEMETRY=1
OTEL_METRICS_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp
OTEL_EXPORTER_OTLP_PROTOCOL=grpc
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer your-token"
```

**Default export intervals**: metrics 60s, logs 5s, traces 5s. Lower for short-lived sessions.

**Admin distribution**: enterprise admins put env vars in managed `settings.json` `env` block — high precedence, users can't override. Distributed via MDM.

**Per-signal protocol/endpoint overrides**: `OTEL_EXPORTER_OTLP_METRICS_PROTOCOL`/`_ENDPOINT`, same for logs/traces. mTLS via `OTEL_EXPORTER_OTLP_METRICS_CLIENT_KEY` / `_CLIENT_CERTIFICATE`.

**Sensitive-data opt-in vars** (off by default):
- `OTEL_LOG_USER_PROMPTS=1` — prompt text on `user_prompt` events and `interaction` span.
- `OTEL_LOG_TOOL_DETAILS=1` — Bash commands, MCP server/tool names, skill names, tool input args, plus custom command names on user_prompt events.
- `OTEL_LOG_TOOL_CONTENT=1` — full tool input/output bodies as span events on `claude_code.tool` (60 KB cap; needs tracing).
- `OTEL_LOG_RAW_API_BODIES=1` (or `file:<dir>`) — full Anthropic Messages API request/response JSON. Includes entire conversation history. Implies all the others.

**Metrics cardinality controls**: `OTEL_METRICS_INCLUDE_SESSION_ID` (default true), `OTEL_METRICS_INCLUDE_VERSION` (default false), `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` (default true). Lower cardinality = better backend perf.

**Span hierarchy**:
```
claude_code.interaction          (one per user prompt turn)
├── claude_code.llm_request      (each Claude API call, with model/duration/tokens/request_id)
├── claude_code.hook             (requires detailed beta tracing)
└── claude_code.tool
    ├── claude_code.tool.blocked_on_user
    ├── claude_code.tool.execution
    └── (Task tool) subagent's llm_request/tool spans nest here
```

**Trace context propagation**:
- Bash and PowerShell subprocesses inherit `TRACEPARENT` env var → can parent their own spans into the trace.
- Agent SDK / `claude -p` reads inbound `TRACEPARENT` + `TRACESTATE` so `interaction` becomes child of caller's span.
- Interactive sessions IGNORE inbound `TRACEPARENT` (avoid CI/container ambient leaks).

**Span attributes** include OpenTelemetry GenAI semantic convention: `gen_ai.system=anthropic`, `gen_ai.request.model`, `gen_ai.response.id`, `gen_ai.response.finish_reasons`. Plus Claude-specific: `request_id`, `client_request_id`, `attempt`, `success`, `stop_reason`, `cache_read_tokens`, `cache_creation_tokens`, `ttft_ms`, `query_source`, `speed`, `llm_request.context`. Tool spans add `tool_name`, `duration_ms`, `result_tokens`, plus gated `file_path`/`full_command`/`skill_name`/`subagent_type`.

Note: the `console` exporter conflicts with the SDK's stdout message channel — don't use under SDK; only safe in interactive CLI use.
