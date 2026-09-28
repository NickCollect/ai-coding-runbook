---
source_url: https://cursor.com/docs/enterprise/opentelemetry-export
fetched_at: 2026-09-28T06:10:42.666060+00:00
fetch_method: mintlify_md
---

# OpenTelemetry Export

OpenTelemetry Export streams Cursor usage data for your team to a collector you run. Cursor sends metrics (tokens, tool calls, best-effort cost) and logs (API requests, errors, corrections, skills, hooks, plugins, cloud agent lifecycle events, and recorded Grok Bot actions) to one team-managed destination. Teams can also opt in to [conversation content](https://cursor.com/docs/enterprise/opentelemetry-export.md#conversation-content): the user prompts and assistant responses from Cloud Agents and Grok Bot, and the [arguments and results of Grok Bot MCP tool calls](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io). Export runs server-side.

OpenTelemetry Export is available on the [Enterprise plan](https://cursor.com/contact-sales?source=docs-opentelemetry-export). Admins configure it in **Team Settings > OpenTelemetry Export**.

The [Wire Reference](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md) documents every metric, log event, and attribute.

## Prerequisites

- An HTTPS endpoint that accepts **OTLP/HTTP protobuf** on `/v1/metrics` and `/v1/logs`. Datadog Agent OTLP ingest, the OpenTelemetry Collector, and ClickHouse/ClickStack all work.
- A bearer token or API key Cursor can send as a request header.
- The endpoint must be reachable from the public internet. Cursor egresses from a fixed set of source IPs.

## Source IPs

Cursor delivers OTLP through a server-side egress proxy. Traffic originates from these static addresses (all `/32`):

| IP address     | CIDR |
| -------------- | ---- |
| 3.218.161.44   | /32  |
| 3.231.18.206   | /32  |
| 35.174.159.35  | /32  |
| 184.73.225.134 | /32  |
| 3.209.66.12    | /32  |
| 52.44.113.131  | /32  |

These IPs don't rotate without advance notice. Use TLS and auth as the primary control. Add IP allowlisting if your network requires it.

## Collector recipes

Cursor pushes to your collector over **OTLP/HTTP binary protobuf**. gRPC and JSON are not supported. Enter the HTTPS base URL in Team Settings without a `/v1` suffix; Cursor appends `/v1/metrics` and `/v1/logs`.

### Minimal OpenTelemetry Collector

```yaml
receivers:
  otlp:
    protocols:
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:

exporters:
  # Swap for your sink (datadog, clickhouse, logging, etc.)
  logging:
    verbosity: basic

service:
  pipelines:
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [logging]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [logging]
```

Terminate TLS in front of the collector with a load balancer, ingress, or the otelcol TLS settings. Enter `https://otel.example.com` in Cursor, not `https://otel.example.com:4318/v1`. For auth, terminate at the load balancer or configure a static header for Cursor to send, such as `Authorization: Bearer <token>`.

### Datadog Agent (OTLP ingest)

Enable OTLP HTTP ingest and logs in the Agent, then expose the Agent (or a gateway in front of it) over HTTPS:

```yaml
logs_enabled: true

otlp_config:
  receiver:
    protocols:
      http:
        endpoint: 0.0.0.0:4318
  logs:
    enabled: true
```

The env-var equivalents are `DD_OTLP_CONFIG_RECEIVER_PROTOCOLS_HTTP_ENDPOINT=0.0.0.0:4318`, `DD_LOGS_ENABLED=true`, and `DD_OTLP_CONFIG_LOGS_ENABLED=true`. Expose port `4318`, or terminate TLS on 443 and proxy to 4318.

In Cursor, the base URL is the public `https://` endpoint in front of that listener. Add `DD-API-KEY` or site headers only if your gateway expects them; the Agent already has `api_key` configured locally.

See [OTLP ingest in the Datadog Agent](https://docs.datadoghq.com/opentelemetry/setup/otlp_ingest_in_the_agent/) for Agent configuration details.

### Databricks and warehouse-style sinks

For warehouse destinations like Databricks or ClickHouse, run a collector with an OTLP HTTP receiver and the vendor exporter, or forward over HTTP into your ingest pipeline. The Cursor side is the same: an HTTPS base URL serving protobuf on `/v1/metrics` and `/v1/logs`. Consume metrics as sums of deltas and dedupe logs on `cursor.event.id`.

## Enable

In **Team Settings > OpenTelemetry Export**:

1. **Create destination** with the base URL (no `/v1/...`; Cursor appends the paths) and auth headers
2. **Test connection** to check the URL and auth
3. **Enable**. Export starts within about a minute.

Each signal and telemetry family has its own toggle. New families default on unless you turn off `auto_enable_new_families`. [Conversation content](https://cursor.com/docs/enterprise/opentelemetry-export.md#conversation-content) is the exception: it stays off until you enable it.

### Conversation content

The `conversation_content` family streams the text of user prompts and assistant responses to your collector as `cursor.conversation.user_message` and `cursor.conversation.assistant_message` logs. It also streams the arguments and results of Grok Bot MCP tool calls as [`cursor.conversation.tool_io`](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io) logs. Today it covers Cloud Agents and Grok Bot only. IDE, CLI, and desktop conversations are not on this family yet. It is the only family that carries message text or tool payloads. The [Wire Reference](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#conversation-content) documents the record shapes.

Conversation content is off by default. Turn on the team opt-in and the
destination toggles below before any message text or tool payload is
exported. Turning a toggle off stops that export; turning it back on does
not backfill earlier messages or tool calls. Teams on Privacy Mode (Legacy)
can't turn on **Allow conversation content export**; the control is
unavailable.

### Allow conversation content export for the team

In **Team Settings > OpenTelemetry Export**, turn on **Allow conversation
content export**. It sits above the destination family toggles. Cursor
confirms with **Conversation content export enabled**.

### Turn on Conversation content on the destination

On the destination, turn on **Conversation content**. Three toggles
appear under it: **Prompts**, **Responses**, and **Tool I/O**. Turning
**Conversation content** on sets **Prompts** and **Responses** on and
leaves **Tool I/O** off. Turning it off clears all three.

### Turn on Tool I/O (optional)

Under **Conversation content**, turn on **Tool I/O** to also receive
the arguments and results of Grok Bot MCP tool calls. It stays off until
you turn it on, including on destinations that exported conversation
content before tool I/O existed. Keep
[Action Recording](https://cursor.com/docs/grok-bot/security.md#logging-and-audit) on as
well, so every tool I/O row has an `mcp_tool_call` row to join to. See
[MCP tool I/O](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io) for what it carries.

What ships once the team opt-in and **Conversation content** are on:

- **Two log events.** `cursor.conversation.user_message` carries a user prompt and `cursor.conversation.assistant_message` carries the final assistant response. The event name identifies the role. The body is the message text.
- **Scrubbed and capped.** Cursor scrubs message text before export and caps each message body at 32 KiB. `cursor.conversation.content_truncated` is true when the exported body is a prefix of the redacted text.
- **Tool I/O is separate.** With its toggle on, `cursor.conversation.tool_io` adds the arguments and results of Grok Bot MCP calls, capped at 8 KiB per side. See [MCP tool I/O](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io).
- **Same identity as other logs.** Records carry the same ids as every other log, including the optional `cursor.user.*` [resource attributes](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#resource-attributes).
- **Cloud Agents and Grok Bot only.** Cloud Agent conversations arrive as `cursor.surface=cloud_agent` and Grok Bot conversations as `cursor.surface=grok_bot`. IDE, CLI, and desktop conversations are not exported by this family yet. Grok Bot messages are separate from the [`grok_bot_agent_actions`](https://cursor.com/docs/enterprise/opentelemetry-export.md#what-cursor-exports) family, which needs Action Recording and carries actions rather than messages.

### MCP tool I/O

The `cursor.grok_bot.mcp_tool_call` log proves a Bot made an MCP call: which server, which tool, whether it succeeded, and how long it took. It never carries what the Bot sent or what came back, so a reviewer can see a Jira transition happened but not which issue moved to which state. `cursor.conversation.tool_io` carries that content, behind the [**Tool I/O** toggle](https://cursor.com/docs/enterprise/opentelemetry-export.md#conversation-content) on the destination.

Before you enable it, a Bot's Jira call shows up in your collector as one `cursor.grok_bot.mcp_tool_call` row whose `cursor.tool.name` names the transition tool and whose `cursor.tool.status` is `success`. After you enable it, the same call also produces two `cursor.conversation.tool_io` rows. The `direction=arguments` row carries the JSON the Bot sent, such as the issue key and the target status. The `direction=result` row carries what Jira returned. Join the three rows on `cursor.grok_bot.tool_call.id`.

Scope and limits:

- **Excerpts, not full payloads.** Each side is capped at 8 KiB. A cut body is a prefix of the redacted text, flagged with `cursor.conversation.content_truncated`, and does not parse as JSON. The head of a write call (object key, target, new value) fits; long read results are cut.
- **Result contents.** On success the result record carries the tool's text and structured content. On failure it carries the error, rejection, or denial message. Cursor replaces image bytes with their MIME type.
- **Secrets redacted, best effort.** Cursor runs the same pattern-based scrubber as shell commands and message text: known credential shapes, PEM blocks, and email addresses become `[REDACTED: ...]` markers, so an `assignee` address exports as `[REDACTED: Email]`. It also redacts the value of any JSON member whose key names a credential (`password`, `token`, `api_key`, and similar; the [Wire Reference](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#cursorconversationtool_io) lists them), whatever the value looks like. Pattern matching can't recognize every secret or every piece of personal data. A credential behind a key outside the list, split across fields, or in a header row with an unusual member name (`{"k":"Authorization","v":"Basic ..."}`) exports as is, and so does an argument that quotes a teammate's message or a result that carries a connector's response body. Your team owns that residual risk, as with prompts and responses.
- **Hosted connector calls only.** Grok Bot MCP calls Cursor runs (Jira, Slack, Linear, and other hosted servers; their `mcp_tool_call` rows show `cursor.grok_bot.mcp.transport=http`) produce tool I/O. `stdio` servers on the Bot's computer, builtin tools, and Cloud Agent, IDE, and CLI tool calls report no payloads yet.

## What Cursor exports

Scope: `cursor.telemetry` `0.1.0`.

Everything below is on by default for a new destination, except `conversation_content`. Turn individual families off in Team Settings.

**Metrics** (delta temporality)

- `cursor.token.usage`: by `cursor.token.type` (`input` / `output` / `cache_read` / `cache_creation`)
- `cursor.tool.calls`: builtin and MCP (`cursor.tool.kind`)
- `cursor.cost.usage`: best-effort USD estimate, not an invoice

**Logs**

- `cursor.api.request`: model call summary
- `cursor.api.error`: error event (no raw messages)
- `cursor.api.correction`: billing finalization; join on `cursor.usage_event.id`
- `cursor.skill.activated`
- `cursor.hook.execution_complete`
- `cursor.plugin.installed`
- `cursor.cloud_agent.setup`: `started` / `completed` / `failed`
- `cursor.cloud_agent.artifact`
- `cursor.cloud_agent.pull_request`: `opened` / `creation_failed`
- `cursor.cloud_agent.mcp_auth_error`: an MCP server rejected the run's credentials
- `cursor.grok_bot.tool_result`: every builtin tool call a Bot made, with its outcome and duration
- `cursor.grok_bot.tool_decision`: who allowed or refused a Bot tool call (a person, Auto-review, a hook, or no gate)
- `cursor.grok_bot.mcp_tool_call`: a Bot connector (MCP) tool call
- `cursor.grok_bot.shell_command`: a Bot shell command, secrets scrubbed, with exit code and duration
- `cursor.grok_bot.browser_navigation`: a page the Bot browser navigated to
- `cursor.grok_bot.computer_use_session`: a Bot computer use session summary
- `cursor.grok_bot.file_transfer`: a file moved between the Bot's computer and a user machine or cloud account
- `cursor.grok_bot.message_delivery`: a message a Bot sent, where it went, and whether it arrived
- `cursor.grok_bot.routine_run`: a finished routine run
- `cursor.grok_bot.guardrail`: a loop detected, a site blocking the Bot, or an approval ask and its wait
- `cursor.grok_bot.delegation`: work a Bot handed to a subagent or cloud agent, and the result coming back
- `cursor.conversation.user_message`: a user prompt, scrubbed; opt-in
- `cursor.conversation.assistant_message`: an assistant response, scrubbed; opt-in
- `cursor.conversation.tool_io`: one side (arguments or result) of a Grok Bot MCP tool call, scrubbed; opt-in

The `cursor.grok_bot.*` events, and `cursor.skill.activated` when a Bot reads a skill, carry [Action Recording](https://cursor.com/docs/grok-bot/security.md#logging-and-audit) data. They flow only after a team admin turns on Action Recording on the dashboard Grok Bot page; it is a team setting, off by default, and Privacy Mode (Legacy) forces it off.

Recorded events are metadata about what the Bot did, never the content it worked with. Tool arguments and results, file paths and names, message bodies and recipients, credentials, and card details are never exported on these events; MCP arguments and results ship only as the opt-in [`cursor.conversation.tool_io`](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io) record. Shell command text is exported after secret scrubbing and capped at 8 KiB; browser URLs are stripped of query strings, fragments, and credentials; and where a tool acted on a site, only the bare hostname is reported. The [Wire Reference](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#shared-grok_bot-attributes) lists every attribute per event.

The `cursor.conversation.*` events carry message text or tool payloads and flow only after the team opts in and the destination turns on the toggle for that kind. See [Conversation content](https://cursor.com/docs/enterprise/opentelemetry-export.md#conversation-content) and [MCP tool I/O](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io).

**Families** (admin toggles; all default on except `conversation_content`)

- `model_usage`: token and cost metrics; api.request / api.error / api.correction
- `tool_calls`: tool.calls metric
- `skills_hooks_plugins`: skill / hook / plugin logs, including a Bot's skill activations
- `cloud_agents`: cloud\_agent.\* logs
- `grok_bot_agent_actions`: grok\_bot.\* action logs; requires Action Recording (Enterprise)
- `conversation_content`: conversation.\* message and tool I/O logs; off by default

**Useful attributes**

- Resource: `service.name=cursor`, `cursor.team.id`, surface/entrypoint, and the optional `cursor.user.id`, `cursor.user.account_id`, and `cursor.user.email`; see [Joining sessions](https://cursor.com/docs/enterprise/opentelemetry-export.md#joining-sessions) to attribute records to a person. Grok Bot traffic exports as `cursor.surface=grok_bot` across all families; `desktop` no longer includes it. A turn a routine started exports `cursor.entrypoint=automation`.
- Logs: `cursor.event.id` (dedupe), and `cursor.request.id` / `cursor.conversation.id` / `cursor.usage_event.id` when present
- Grok Bot logs: `cursor.grok_bot.turn.id`, `cursor.grok_bot.event.sequence`, `cursor.grok_bot.tool_call.id`, and `cursor.grok_bot.decision.id`; see [Joining sessions](https://cursor.com/docs/enterprise/opentelemetry-export.md#joining-sessions)

## Delivery

- Metrics are **at-most-once**. Delta sums can have brief gaps after a failure.
- Logs are **at-least-once**. Dedupe on `cursor.event.id` for exactly-once views.
- There is no backfill from before the destination existed.
- Editing the endpoint or credentials keeps the destination. Disabling or deleting it drops in-flight data.

## Auth

Cursor stores headers encrypted. To rotate credentials, edit the destination and save. Changes take effect in about 30 seconds.

## Limitations

- **Cost is not billing.** `cursor.cost.usage` is a best-effort estimate. One series covers both included-quota drawdown and on-demand usage. For BYOK it reflects the **Cursor Token Rate** only, not provider spend. Use the Admin and billing APIs for invoices.
- **Disabling or deleting a destination drops in-flight data.** Rotate credentials by editing the destination instead of deleting and re-adding it.
- **Logs can arrive more than once.** Delivery is at-least-once. Dedupe on `cursor.event.id`.
- **No prompt content or tool payloads unless you opt in.** Message text and MCP tool arguments and results ship only through the opt-in `conversation_content` family. Every other log event carries ids, counts, and low-cardinality attributes. See [Conversation content](https://cursor.com/docs/enterprise/opentelemetry-export.md#conversation-content) and [MCP tool I/O](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io).
- **No trace context or historical backfill.** Exported logs don't carry OpenTelemetry `trace_id` or `span_id` fields, and Cursor doesn't send traces. Export starts when you enable the destination.
- **Metric datapoints carry no correlation IDs.** Use log attributes for per-conversation joins. See [Joining sessions](https://cursor.com/docs/enterprise/opentelemetry-export.md#joining-sessions).
- **Metrics are delta-only.** Sum deltas per series. A strict delta-to-cumulative processor may drop end-time-inverted points.

## Joining sessions

Metrics (`cursor.token.usage`, `cursor.tool.calls`, `cursor.cost.usage`) are aggregates. Datapoints carry no `conversation.id`, `request.id`, or `usage_event.id`. This keeps metric cardinality bounded. For session- or request-scoped analysis, use logs.

**What each id means**

- `cursor.conversation.id` is the session key. In the IDE and CLI it's the composer chat UUID. For cloud agents it's the customer-visible `bc-...` agent id. For Grok Bot (`grok_bot.*`, and any log with `cursor.surface=grok_bot`) it is the identifier for the Bot, and that value is the Bot's conversation id. The same value appears on that run's `api.request`, `api.error`, `skill.activated`, `hook.execution_complete`, `cloud_agent.*`, `grok_bot.*`, and (when the team opts in) `conversation.*` logs when present.
- `cursor.usage_event.id` is the request-grain key on `api.request`, `api.error`, and `api.correction`. Use it to reconcile against Cursor usage and billing exports and to apply corrections.
- `cursor.request.id` is an optional per-call id on most logs. It never appears on `api.correction`, `cloud_agent.*`, or `grok_bot.*`.
- `cursor.event.id` is a dedupe key only, not a join key across event types.

**Attribute records to a person**

`cursor.user.account_id` is the member's Admin API id. Join it to `id` in the [`GET /teams/members`](https://cursor.com/docs/account/teams/admin-api.md#get-team-members) response to name the person behind a record. `cursor.user.email` names the member directly. Both are optional and appear only alongside `cursor.user.id`, so don't require them on every record. The [resource attributes](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#resource-attributes) table has the presence rules.

**Group Grok Bot activity**

| Goal          | Group by                                    | Coverage                                                                                                                                                                                                                                                                                                   |
| ------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| One Bot       | `cursor.conversation.id`                    | The Bot's identifier (its conversation id). Action Recording and model request logs for the Bot                                                                                                                                                                                                            |
| One turn      | `cursor.grok_bot.turn.id`                   | Action Recording logs from the turn, the Bot's `skill.activated` logs, and the turn's `api.request` / `api.error` logs                                                                                                                                                                                     |
| One tool call | `cursor.grok_bot.tool_call.id`              | Every row one tool call produced: its `tool_result`, its `tool_decision` rows, its tool-specific row (`mcp_tool_call`, `file_transfer`, `message_delivery`, ...), and, with [MCP tool I/O](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io) on, its two `conversation.tool_io` rows |
| One approval  | `cursor.grok_bot.decision.id`               | The `tool_decision` row of a person's answer and the `guardrail` rows for the ask and the wait                                                                                                                                                                                                             |
| One user      | Resource attribute `cursor.user.account_id` | Logs and metrics when present; see [Attribute records to a person](https://cursor.com/docs/enterprise/opentelemetry-export.md#joining-sessions)                                                                                                                                                            |

Four attributes tie a Bot's records together. `cursor.grok_bot.turn.id` names the turn: it appears on every Action Recording log from the turn and, for `cursor.surface=grok_bot`, on the turn's `api.request` and `api.error` logs too, so model calls join to actions per turn. Within a turn, `cursor.grok_bot.event.sequence` orders the actions without trusting client clocks; sort by it, not by timestamp, and don't expect it to be dense. `cursor.grok_bot.tool_call.id` groups the rows of one tool call, and `cursor.grok_bot.decision.id` joins an approval ask, the wait on it, and the person's answer.

Subagent actions carry their own `cursor.grok_bot.turn.id` and `cursor.grok_bot.subagent.id`, plus `cursor.grok_bot.root_turn.id`, the user-facing turn they serve. Group by `root_turn.id` to roll a subagent's actions up to the turn that spawned it.

For example, a turn in which the Bot ran a command that Auto-review escalated to the user can produce these records:

| Log event                       | `cursor.grok_bot.turn.id` | `cursor.grok_bot.event.sequence` | `cursor.grok_bot.tool_call.id` | `cursor.grok_bot.decision.id` |
| ------------------------------- | ------------------------- | -------------------------------- | ------------------------------ | ----------------------------- |
| `cursor.api.request`            | `turn-1`                  | Not present                      | Not present                    | Not present                   |
| `cursor.grok_bot.tool_decision` | `turn-1`                  | 3                                | `call-7`                       | `dec-1` (`policy`, `denied`)  |
| `cursor.grok_bot.guardrail`     | `turn-1`                  | 4                                | `call-7`                       | `card-2` (`tool_escalation`)  |
| `cursor.grok_bot.guardrail`     | `turn-1`                  | 5                                | `call-7`                       | `card-2` (`pause`, `resumed`) |
| `cursor.grok_bot.tool_decision` | `turn-1`                  | 6                                | `call-7`                       | `card-2` (`human`, `allowed`) |
| `cursor.grok_bot.tool_result`   | `turn-1`                  | 7                                | `call-7`                       | Not present                   |

All rows share the Bot's `cursor.conversation.id`. Group by `turn-1` to reconstruct the turn, including its model calls. Group by `call-7` to follow the one shell call: Auto-review refused it, a card asked the user, the user allowed it, and the tool ran and returned `success`. `card-2` ties the ask and its wait to the answer. The command text itself is on the turn's `cursor.grok_bot.shell_command` row, which carries no `tool_call.id`. These fields are custom log attributes, not OpenTelemetry trace or span ids.

With [conversation content](https://cursor.com/docs/enterprise/opentelemetry-export.md#conversation-content) enabled, the Bot's `cursor.conversation.user_message` and `cursor.conversation.assistant_message` logs carry the same `cursor.conversation.id`. Join on it to place the prompt and response next to the Bot's model requests and recorded actions. Message logs carry their own optional `cursor.conversation.turn.id`. Don't depend on `cursor.grok_bot.turn.id` or `cursor.request.id` on them.

With [MCP tool I/O](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io) enabled, an MCP call adds two `cursor.conversation.tool_io` logs (`direction=arguments` and `direction=result`) that carry the call's `cursor.grok_bot.tool_call.id` and, when present, its `turn.id` and `event.sequence`. Group by `tool_call.id` to put the arguments and result next to the call's `mcp_tool_call` and `tool_decision` rows.

**Recipe: rank sessions by tokens, then attach skills and tools**

1. Take `cursor.api.request` log rows. Sum `cursor.api.request.input_tokens` and `output_tokens` (and the cache fields if you need them) grouped by `cursor.conversation.id`. This gives per-session token totals, which metrics can't provide.
2. Rank conversations by that sum, or by estimated cost.
3. Left-join other logs on the same `cursor.conversation.id`:
   - `cursor.skill.activated` shows which skills ran
   - `cursor.hook.execution_complete` shows hooks
   - `cursor.cloud_agent.*` shows setup, pull requests, artifacts, and MCP auth failures (cloud agents only)
   - `cursor.grok_bot.*` shows what a Bot did (Grok Bot only, with Action Recording on)
   - `cursor.conversation.user_message` and `cursor.conversation.assistant_message` show the prompts and responses (Cloud Agents and Grok Bot, only with the `conversation_content` opt-in)
   - `cursor.conversation.tool_io` shows what each Grok Bot MCP call sent and received (Grok Bot, only with the [tool I/O opt-in](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io))
4. `cursor.tool.calls` is metric-only, so it has no conversation id. Report org-wide tool rates from the metric. For Grok Bot, `cursor.grok_bot.tool_result` and `cursor.grok_bot.mcp_tool_call` give per-Bot and per-turn tool attribution; for other surfaces it is not on the wire yet.

`cursor.cost.usage` is also metric-only. To rank sessions by cost, approximate from `api.request` token totals and your own rates, or pull spend from the Admin and billing APIs and join on `cursor.usage_event.id` where available.

**Recipe: apply a billing correction**

1. Find `cursor.api.correction` logs.
2. Join on `cursor.usage_event.id` to the `api.request` and `api.error` logs sharing that id.
3. Treat the whole group as not billed.

**Caveats**

- Subagents get their own conversation id. For Grok Bot actions, roll them up with `cursor.grok_bot.root_turn.id`; for other surfaces, parent rollup is not exported yet.
- Dedupe log rows on `cursor.event.id` before joining if you need exactly-once views.
- Records from older Grok Bot versions omit `cursor.grok_bot.event.sequence` and `cursor.grok_bot.initiated_by`. Treat both as optional.

## Change policy

New metrics and events may appear as coverage expands. `auto_enable_new_families` controls whether they turn on automatically. Renames and removals get explicit notice. The [Wire Reference](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md) documents the full attribute surface.

### OpenTelemetry Export is available on the Enterprise plan

Contact our team to stream Cursor usage into your observability stack.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
