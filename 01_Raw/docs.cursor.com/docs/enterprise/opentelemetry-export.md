---
source_url: https://cursor.com/docs/enterprise/opentelemetry-export
fetched_at: 2026-11-09T07:30:16.850439+00:00
fetch_method: mintlify_md
---

# OpenTelemetry Export

OpenTelemetry Export streams Cursor usage data for your team to a collector you run. Cursor sends metrics (tokens, tool calls, best-effort cost) and logs (API requests, errors, corrections, skills, hooks, plugins, cloud agent lifecycle events, and recorded Grok Bot actions) to one team-managed destination. Teams can also opt in to [conversation content](https://cursor.com/docs/enterprise/opentelemetry-export.md#conversation-content): the user prompts and assistant responses from Cloud Agents, local agents, and Grok Bot, and the [arguments and results of tool calls](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io): Grok Bot's MCP calls, and Cloud Agent and local agent MCP and builtin calls. Cursor runs the export server-side.

OpenTelemetry Export is available on the [Enterprise plan](https://cursor.com/contact-sales?source=docs-opentelemetry-export). Admins configure it in **Team Settings > OpenTelemetry Export**.

The [Wire Reference](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md) documents every metric, log event, and attribute.

## Prerequisites

- An HTTPS endpoint that accepts **OTLP/HTTP protobuf** on `/v1/metrics` and `/v1/logs`. Datadog Agent OTLP ingest, the OpenTelemetry Collector, and ClickHouse/ClickStack all work.
- A bearer token or API key Cursor can send as a request header.
- Your endpoint must be reachable from the public internet, because Cursor connects to it from the fixed set of [source IPs](https://cursor.com/docs/enterprise/opentelemetry-export.md#source-ips) below.

## Source IPs

Cursor delivers OTLP through a server-side egress proxy. Traffic originates from these static addresses (all `/32`):

| IP address      | CIDR |
| --------------- | ---- |
| 3.218.161.44    | /32  |
| 3.231.18.206    | /32  |
| 35.174.159.35   | /32  |
| 184.73.225.134  | /32  |
| 3.209.66.12     | /32  |
| 52.44.113.131   | /32  |
| 100.63.97.141   | /32  |
| 100.63.144.57   | /32  |
| 18.210.232.136  | /32  |
| 3.208.51.163    | /32  |
| 3.224.130.48    | /32  |
| 3.234.118.132   | /32  |
| 34.197.19.148   | /32  |
| 34.198.251.120  | /32  |
| 34.199.187.247  | /32  |
| 35.170.160.152  | /32  |
| 44.215.226.85   | /32  |
| 52.202.172.69   | /32  |
| 54.81.109.217   | /32  |
| 54.204.61.44    | /32  |
| 54.236.99.119   | /32  |
| 67.202.63.191   | /32  |
| 184.193.125.229 | /32  |
| 184.193.223.40  | /32  |
| 184.194.140.210 | /32  |
| 184.194.175.144 | /32  |
| 184.194.208.56  | /32  |

Cursor gives advance notice before these IPs change. Protect your endpoint with TLS and auth first, and add an IP allowlist on top if your network policy requires one.

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

So the Agent can receive Cursor's export, enable OTLP HTTP ingest and logs in it, then expose the Agent (or a gateway in front of it) over HTTPS:

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

For warehouse destinations like Databricks or ClickHouse, run a collector with an OTLP HTTP receiver and the vendor exporter, or forward over HTTP into your ingest pipeline. The Cursor side is the same: an HTTPS base URL serving protobuf on `/v1/metrics` and `/v1/logs`. Cursor sends metrics as deltas and can deliver a log more than once, so your pipeline should sum the metric deltas and dedupe logs on `cursor.event.id`.

## Enable

In **Team Settings > OpenTelemetry Export**:

1. **Create destination** with the base URL (no `/v1/...`; Cursor appends the paths) and auth headers
2. **Test connection** to check the URL and auth
3. **Enable**. Cursor starts exporting within about a minute.

Each signal and telemetry family has its own toggle. New families default on unless you turn off `auto_enable_new_families`. [Conversation content](https://cursor.com/docs/enterprise/opentelemetry-export.md#conversation-content) is the exception: it stays off until you enable it.

### Conversation content

The `conversation_content` family streams the text of user prompts and assistant responses to your collector as `cursor.conversation.user_message` and `cursor.conversation.assistant_message` logs. It also streams the arguments and results of tool calls as [`cursor.conversation.tool_io`](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io) logs: Grok Bot's MCP calls, and every MCP and builtin tool call a Cloud Agent or local agent makes. It covers Cloud Agents, Grok Bot, and [local agents](https://cursor.com/docs/enterprise/opentelemetry-export.md#local-agent-conversations) in the IDE, Glass, the CLI, the Origin CLI, and the SDK. It is the only family that carries message text or tool payloads. The [Wire Reference](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#conversation-content) documents the record shapes.

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
the arguments and results of tool calls: Grok Bot's MCP calls, and every
MCP and builtin tool call a Cloud Agent or local agent makes. It stays off until
you turn it on, including on destinations that exported conversation
content before tool I/O existed. For Grok Bot, keep
[Action Recording](https://cursor.com/docs/grok-bot/security.md#logging-and-audit) on as
well, so every Grok Bot tool I/O row has an `mcp_tool_call` row to join to. See
[MCP tool I/O](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io) for what it carries.

What ships once the team opt-in and **Conversation content** are on:

- **Two log events.** `cursor.conversation.user_message` carries a user prompt and `cursor.conversation.assistant_message` carries the final assistant response. The event name identifies the role. The body is the message text.
- **Scrubbed and capped.** Cursor scrubs message text before export and caps each message body at 32 KiB. `cursor.conversation.content_truncated` is true when the exported body is a prefix of the redacted text.
- **Tool I/O is separate.** With its toggle on, `cursor.conversation.tool_io` adds the arguments and results of Grok Bot MCP calls and of Cloud Agent and local agent MCP and builtin tool calls, capped at 8 KiB per side. See [MCP tool I/O](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io).
- **Same identity as other logs.** Records carry the same ids as every other log, including the optional `cursor.user.*` [resource attributes](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#resource-attributes).
- **Cloud Agents, local agents, and Grok Bot.** Cloud Agent conversations arrive as `cursor.surface=cloud_agent` and Grok Bot conversations as `cursor.surface=grok_bot`. Local agent conversations arrive as `desktop`, `cli`, or `sdk`; see [Local agent conversations](https://cursor.com/docs/enterprise/opentelemetry-export.md#local-agent-conversations). A Cloud Agent's `Task` subagents export their responses and tool I/O under their own conversation id, but Cursor doesn't export their prompts; see [MCP tool I/O](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io). Grok Bot messages are separate from the [`grok_bot_agent_actions`](https://cursor.com/docs/enterprise/opentelemetry-export.md#what-cursor-exports) family, which needs Action Recording and carries actions rather than messages.

### Local agent conversations

Agent turns your members run locally in the IDE, Glass, the CLI (including headless runs), the [Origin CLI](https://cursor.com/docs/origin/cli.md), and the SDK export `cursor.conversation.user_message`, `cursor.conversation.assistant_message`, and `cursor.conversation.tool_io`. They use the same team opt-in, destination toggles, scrubbing, caps, and attributes as Cloud Agent records. Privacy rules match too: turns from a member on Privacy Mode (Legacy) never export, and turns under Privacy Mode do. Prompts export for every local client, including headless CLI runs and SDK scripts.

`cursor.surface` tells local turns apart from Cloud Agent turns:

| Where the agent ran                              | `cursor.surface` |
| ------------------------------------------------ | ---------------- |
| IDE and Glass                                    | `desktop`        |
| CLI, including headless runs, and the Origin CLI | `cli`            |
| SDK                                              | `sdk`            |
| Cloud Agent                                      | `cloud_agent`    |

`cursor.entrypoint` carries the same value as `cursor.surface` on local agent records. `cursor.conversation.id` is the local conversation id, the same value the turn's `cursor.api.request` logs carry.

Delivery is best effort:

- **Some turns can drop.** Cursor builds a local turn's records after the turn ends, from its own server-side copy of the turn. When part of that copy is missing, or the export doesn't finish within a few seconds, the turn exports some or none of its records.
- **Failed turns export partially.** A turn that ends in an error exports its prompt and the tool calls that finished, but not its partial response. If the turn is resumed, its final response exports under the same message id.
- **Retries can repeat a prompt.** A retried turn is a new request, so its prompt can export again under a new `cursor.conversation.message.id`.

Not exported from local agents:

- Subagents a local agent starts with the `Task` tool. The parent's `Task` call still exports like any other tool call.
- Features outside agent conversations, such as Tab and inline edit.
- Agent turns that run entirely in the client rather than through Cursor's servers.

### MCP tool I/O

The `cursor.grok_bot.mcp_tool_call` log proves a Bot made an MCP call: which server, which tool, whether it succeeded, and how long it took. It never carries what the Bot sent or what came back, so a reviewer can see a Jira transition happened but not which issue moved to which state. `cursor.conversation.tool_io` carries that content, behind the [**Tool I/O** toggle](https://cursor.com/docs/enterprise/opentelemetry-export.md#conversation-content) on the destination.

Before you enable it, a Bot's Jira call shows up in your collector as one `cursor.grok_bot.mcp_tool_call` row whose `cursor.tool.name` names the transition tool and whose `cursor.tool.status` is `success`. After you enable it, the same call also produces two `cursor.conversation.tool_io` rows. The `direction=arguments` row carries the JSON the Bot sent, such as the issue key and the target status. The `direction=result` row carries what Jira returned. To see the call next to its arguments and result, join the three rows on `cursor.grok_bot.tool_call.id`. The two `tool_io` rows also carry the same value as `cursor.tool_call.id`, the key that joins the two sides of a call on every surface.

Cursor exports the same record for every finished tool call a Cloud Agent makes in a turn, MCP and builtin alike: shell commands, file reads and edits, searches, web fetches, subagent `Task` calls, and the rest. Cursor exports them once the turn ends, so they never add latency to a tool call. Each record carries the tool call's completion time, so a long turn can deliver records timestamped well before they arrive. Order by record timestamp, not arrival time. `cursor.tool.kind` (`mcp` or `builtin`) says which kind of tool ran, and `cursor.tool.name` names it (`shell`, `read`, `edit`, `grep`, and so on, for builtins). A builtin record's body is the tool's arguments or result as JSON, scrubbed the same way. Binary fields such as screenshots are left out, and a `Task` result leaves out the subagent's transcript, whose calls arrive as records of their own. The two records of one call share `cursor.tool_call.id`, and `cursor.conversation.id` ties them to the rest of the agent's run. Cloud Agent records carry no `cursor.grok_bot.*` attributes. Each one carries the `cursor.conversation.turn.id` of the turn it ran in, the same value as that turn's prompt and response records.

A subagent a Cloud Agent starts with the `Task` tool is a Cloud Agent of its own, with its own `bc-...` agent id. When it finishes, Cursor exports its `tool_io` and `assistant_message` records under that id, behind the same toggles as the parent. Cursor doesn't export a subagent's user prompts. To join a subagent to its parent, read `success.agentId` in the body of the parent's `Task` `tool_io` result record: it names the subagent's `cursor.conversation.id`. The subagent's records carry no `cursor.subagent.id`. That attribute appears only on calls made by in-process subagents, which Cloud Agents rarely start. Those calls stay under the parent's conversation id and carry the turn that started the subagent.

Scope and limits:

- **Excerpts, not full payloads.** Each side is capped at 8 KiB. A body over the cap is a prefix of the redacted text and does not parse as JSON. `cursor.conversation.content_truncated` flags it, and also flags a body that is still valid JSON but lost the tail of a document the connector had already cut. Check the flag before you parse, so your pipeline doesn't treat an excerpt as the full payload. The head of a write call (object key, target, new value) fits; long read results are cut.
- **Result contents.** On success the result record carries the tool's text and structured content. On failure it carries the error, rejection, or denial message. Cursor replaces image bytes with their MIME type.
- **Secrets redacted, best effort.** Cursor runs the same pattern-based scrubber as shell commands and message text: known credential shapes, PEM blocks, US social security numbers, and email addresses become `[REDACTED: ...]` markers, so an `assignee` address exports as `[REDACTED: Email]` and a `123-45-6789` in a ticket body as `[REDACTED: SSN]`. It also redacts the value of any JSON member whose key names a credential (`password`, `token`, `auth`, `pin`, `api_key`, and similar; the [Wire Reference](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#cursorconversationtool_io) has the rule), whatever the value looks like. An object under such a key keeps its shape, with its metadata members exported and only the secret replaced: `auth: {"type":"oauth2","token":"..."}` exports the `type` and the marker. The same key rules apply to JSON a connector returns as text, the usual MCP reply shape, including JSON nested inside a string at any depth; a document with a redaction in it exports compact. Pattern matching can't recognize every secret or every piece of personal data. A credential behind a key outside the list, split across fields, or in a header row with an unusual member name (`{"k":"Authorization","v":"Basic ..."}`) exports as is, and so does an argument that quotes a teammate's message or a result that carries a connector's response body. Your team owns that residual risk, as with prompts and responses.
- **Which calls produce tool I/O.** On Cloud Agents and [local agents](https://cursor.com/docs/enterprise/opentelemetry-export.md#local-agent-conversations), every finished MCP and builtin tool call does. On Grok Bot, only the MCP calls Cursor runs do (Jira, Slack, Linear, and other hosted servers; their `mcp_tool_call` rows show `cursor.grok_bot.mcp.transport=http`). `stdio` servers on the Bot's computer and the Bot's builtin tools report no payloads yet.

## What Cursor exports

Scope: `cursor.telemetry` `0.1.0`.

Everything below is on by default for a new destination, except `conversation_content`. To stop exporting a family, turn it off in Team Settings.

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
- `cursor.cloud_agent.commit`: a commit a cloud agent pushed to a GitHub repository, with its SHA and change counts
- `cursor.cloud_agent.artifact`
- `cursor.cloud_agent.pull_request`: `opened` / `merged` / `closed` / `creation_failed`, with the repository URL
- `cursor.cloud_agent.mcp_auth_error`: an MCP server rejected the run's credentials
- `cursor.cloud_agent.review_followup`: a pull request comment or review, or Bugbot Autofix, started a cloud agent run on an existing pull request
- `cursor.grok_bot.tool_result`: every builtin tool call a Bot made, with its outcome and duration
- `cursor.grok_bot.tool_decision`: who allowed or refused a Bot tool call (a person, Auto-review, a hook, or no gate)
- `cursor.grok_bot.mcp_tool_call`: a Bot connector (MCP) tool call
- `cursor.grok_bot.shell_command`: a Bot shell command, secrets scrubbed, with exit code and duration
- `cursor.grok_bot.browser_navigation`: a page the Bot browser navigated to
- `cursor.grok_bot.computer_use_session`: a Bot computer use session summary
- `cursor.grok_bot.file_transfer`: a file moved between the Bot's computer and a user machine or cloud account
- `cursor.grok_bot.message_delivery`: a message a Bot sent, where it went, and whether it arrived
- `cursor.grok_bot.routine_run`: a finished routine run
- `cursor.grok_bot.guardrail`: a loop detected, a site blocking the Bot, an approval ask and its wait, or the organization's inference hook refusing a turn
- `cursor.grok_bot.delegation`: work a Bot handed to a subagent or cloud agent, and the result coming back
- `cursor.conversation.user_message`: a user prompt, scrubbed; opt-in
- `cursor.conversation.assistant_message`: an assistant response, scrubbed; opt-in
- `cursor.conversation.tool_io`: one side (arguments or result) of a Grok Bot MCP tool call, scrubbed; opt-in. Cursor exports the same record for Cloud Agent and local agent MCP and builtin calls

The `cursor.grok_bot.*` events, and `cursor.skill.activated` when a Bot reads a skill, carry [Action Recording](https://cursor.com/docs/grok-bot/security.md#logging-and-audit) data. They flow only after a team admin turns on Action Recording on the dashboard Grok Bot page; it is a team setting, off by default, and Privacy Mode (Legacy) forces it off.

Recorded events are metadata about what the Bot did, never the content it worked with. Tool arguments and results, file paths and names, message bodies and recipients, credentials, and card details are never exported on these events; MCP arguments and results ship only as the opt-in [`cursor.conversation.tool_io`](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io) record. Shell command text is exported after secret scrubbing and capped at 8 KiB; browser URLs are stripped of query strings, fragments, and credentials, and a webhook token or share-link token in the path becomes a `[REDACTED: ...]` marker; and where a tool acted on a site, only the bare hostname is reported. The [Wire Reference](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#shared-grok_bot-attributes) lists every attribute per event.

The `cursor.conversation.*` events carry message text or tool payloads and flow only after the team opts in and the destination turns on the toggle for that kind. See [Conversation content](https://cursor.com/docs/enterprise/opentelemetry-export.md#conversation-content) and [MCP tool I/O](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io).

**Families** (admin toggles; all default on except `conversation_content`)

- `model_usage`: token and cost metrics; api.request / api.error / api.correction
- `tool_calls`: tool.calls metric
- `skills_hooks_plugins`: skill / hook / plugin logs, including a Bot's skill activations
- `cloud_agents`: cloud\_agent.\* logs
- `grok_bot_agent_actions`: grok\_bot.\* action logs; requires Action Recording (Enterprise)
- `conversation_content`: conversation.\* message and tool I/O logs; off by default

**Useful attributes**

- Resource: `service.name=cursor`, `cursor.team.id`, surface/entrypoint, the optional `cursor.user.id`, `cursor.user.account_id`, and `cursor.user.email`, and `cursor.project.id` for cloud Project runs; see [Joining sessions](https://cursor.com/docs/enterprise/opentelemetry-export.md#joining-sessions) to attribute records to a person or a Project. Grok Bot traffic exports as `cursor.surface=grok_bot` across all families; `desktop` no longer includes it. A turn a routine started exports `cursor.entrypoint=automation`. An agent the Cursor SDK runs locally exports `cursor.surface=sdk` and `cursor.entrypoint=sdk` on every record; the [Wire Reference](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#sdk-records) covers cloud agents the SDK launched.
- Logs: `cursor.event.id` (dedupe), and `cursor.request.id` / `cursor.conversation.id` / `cursor.usage_event.id` / `cursor.project.name` when present
- Grok Bot logs: `cursor.grok_bot.turn.id`, `cursor.grok_bot.event.sequence`, `cursor.grok_bot.tool_call.id`, and `cursor.grok_bot.decision.id`; see [Joining sessions](https://cursor.com/docs/enterprise/opentelemetry-export.md#joining-sessions)

## Delivery

- Metrics are **at-most-once**. Delta sums can have brief gaps after a failure.
- Logs are **at-least-once**. If you need exactly-once views, dedupe on `cursor.event.id`.
- There is no backfill from before the destination existed.
- Editing the endpoint or credentials keeps the destination. Disabling or deleting it drops in-flight data.

## Auth

Cursor stores headers encrypted. To rotate credentials, edit the destination and save. Changes take effect in about 30 seconds.

## Limitations

- **Cost is not billing.** `cursor.cost.usage` is a best-effort estimate. One series covers both included-quota drawdown and on-demand usage. For BYOK it reflects the **Cursor Token Rate** only, not provider spend. For invoice amounts, use the Admin and billing APIs.
- **Disabling or deleting a destination drops in-flight data.** To rotate credentials without losing in-flight data, edit the destination instead of deleting and re-adding it.
- **Logs can arrive more than once.** Delivery is at-least-once, so dedupe on `cursor.event.id` to count each record once.
- **No prompt content or tool payloads unless you opt in.** Message text and tool call arguments and results ship only through the opt-in `conversation_content` family. Every other log event carries ids, counts, and low-cardinality attributes. See [Conversation content](https://cursor.com/docs/enterprise/opentelemetry-export.md#conversation-content) and [MCP tool I/O](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io).
- **No trace context or historical backfill.** Exported logs don't carry OpenTelemetry `trace_id` or `span_id` fields, and Cursor doesn't send traces. Export starts when you enable the destination.
- **Metric datapoints carry no correlation IDs.** For per-conversation joins, use log attributes instead. See [Joining sessions](https://cursor.com/docs/enterprise/opentelemetry-export.md#joining-sessions).
- **Metrics are delta-only.** Each datapoint is a change, so sum the deltas per series to get totals. A strict delta-to-cumulative processor may drop end-time-inverted points.

## Joining sessions

Metrics (`cursor.token.usage`, `cursor.tool.calls`, `cursor.cost.usage`) are aggregates. Datapoints carry no `conversation.id`, `request.id`, or `usage_event.id`. This keeps metric cardinality bounded. For session- or request-scoped analysis, use logs.

**What each id means**

- `cursor.conversation.id` is the session key. In the IDE and CLI it's the composer chat UUID. For cloud agents it's the customer-visible `bc-...` agent id. For Grok Bot (`grok_bot.*`, and any log with `cursor.surface=grok_bot`) it is the identifier for the Bot, and that value is the Bot's conversation id. The same value appears on that run's `api.request`, `api.error`, `skill.activated`, `hook.execution_complete`, `cloud_agent.*`, `grok_bot.*`, and (when the team opts in) `conversation.*` logs when present.
- `cursor.usage_event.id` is the request-grain key on `api.request`, `api.error`, and `api.correction`. Use it to reconcile against Cursor usage and billing exports and to apply corrections.
- `cursor.request.id` is an optional per-call id on most logs. It never appears on `api.correction`, `cloud_agent.*`, or `grok_bot.*`.
- `cursor.event.id` is a dedupe key only, not a join key across event types.

**Attribute records to a person**

`cursor.user.account_id` is the member's Admin API id. Join it to `id` in the [`GET /teams/members`](https://cursor.com/docs/account/teams/admin-api.md#get-team-members) response to name the person behind a record. `cursor.user.email` names the member directly. Both are optional and appear only alongside `cursor.user.id`, so don't require them on every record. The [resource attributes](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#resource-attributes) table has the presence rules.

Cloud agent records (`cursor.cloud_agent.*`) carry the same user attributes, resolved from the run's owner. A run started with a team API key or a service account has no owner and carries none.

**Group a cloud Project**

Records from a cloud Project's coordinator and every agent in its tree carry the resource attribute `cursor.project.id`, the coordinator's `bc-...` agent id. Group by it to roll a Project's logs and metrics, including token and cost, into one view without joining conversation ids. Most log records from the tree also carry the Project's current display name as `cursor.project.name`; group by the id, since a rename changes the name. `grok_bot.*` records never carry `cursor.project.name`, and `cloud_agent.review_followup` carries neither attribute. The [resource attributes](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#resource-attributes) table has the presence rules.

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

With [conversation content](https://cursor.com/docs/enterprise/opentelemetry-export.md#conversation-content) enabled, the Bot's `cursor.conversation.user_message` and `cursor.conversation.assistant_message` logs carry the same `cursor.conversation.id`. Join on it to place the prompt and response next to the Bot's model requests and recorded actions. Message logs carry their own optional `cursor.conversation.turn.id`. They don't reliably carry `cursor.grok_bot.turn.id` or `cursor.request.id`, so don't build joins on those.

With [MCP tool I/O](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io) enabled, an MCP call adds two `cursor.conversation.tool_io` logs (`direction=arguments` and `direction=result`) that carry the call's `cursor.grok_bot.tool_call.id` (also exported as `cursor.tool_call.id`) and, when present, its `turn.id` and `event.sequence`. Group by `tool_call.id` to put the arguments and result next to the call's `mcp_tool_call` and `tool_decision` rows.

**Recipe: rank sessions by tokens, then attach skills and tools**

1. Take `cursor.api.request` log rows. Sum `cursor.api.request.input_tokens` and `output_tokens` (and the cache fields if you need them) grouped by `cursor.conversation.id`. This gives per-session token totals, which metrics can't provide.
2. Rank conversations by that sum, or by estimated cost.
3. Left-join other logs on the same `cursor.conversation.id`:
   - `cursor.skill.activated` shows which skills ran
   - `cursor.hook.execution_complete` shows hooks
   - `cursor.cloud_agent.*` shows what a cloud agent did (cloud agents only)
   - `cursor.grok_bot.*` shows what a Bot did (Grok Bot only, with Action Recording on)
   - `cursor.conversation.user_message` and `cursor.conversation.assistant_message` show the prompts and responses (Cloud Agents, local agents, and Grok Bot, only with the `conversation_content` opt-in)
   - `cursor.conversation.tool_io` shows what each tool call sent and received (Grok Bot MCP calls, and Cloud Agent and local agent MCP and builtin calls, only with the [tool I/O opt-in](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io))
4. `cursor.tool.calls` is metric-only, so it has no conversation id. Report org-wide tool rates from the metric. For Grok Bot, `cursor.grok_bot.tool_result` and `cursor.grok_bot.mcp_tool_call` give per-Bot and per-turn tool attribution; for other surfaces it is not on the wire yet.

`cursor.cost.usage` is also metric-only. To rank sessions by cost, approximate from `api.request` token totals and your own rates, or pull spend from the Admin and billing APIs and join on `cursor.usage_event.id` where available.

**Recipe: apply a billing correction**

1. Find `cursor.api.correction` logs.
2. Join on `cursor.usage_event.id` to the `api.request` and `api.error` logs sharing that id.
3. Cursor didn't bill that usage, so treat the whole group as not billed.

**Caveats**

- Subagents get their own conversation id. For Grok Bot actions, roll them up with `cursor.grok_bot.root_turn.id`. A Cloud Agent's `Task` subagents export under their own conversation id; join one to its parent through `success.agentId` in the parent's `Task` `tool_io` result. A Cloud Agent's in-process subagents, which are rare, are the exception: their tool I/O records stay under the parent's `cursor.conversation.id` and `cursor.conversation.turn.id`, with `cursor.subagent.id` naming the subagent. Other surfaces don't export parent rollup yet.
- Dedupe log rows on `cursor.event.id` before joining if you need exactly-once views.
- Records from older Grok Bot versions omit `cursor.grok_bot.event.sequence` and `cursor.grok_bot.initiated_by`, so build your pipeline to treat both as optional.

## Change policy

Cursor adds new metrics and events as coverage expands. `auto_enable_new_families` controls whether they turn on automatically for your destination. Cursor gives explicit notice before it renames or removes anything. The [Wire Reference](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md) documents the full attribute surface.

### OpenTelemetry Export is available on the Enterprise plan

Contact our team to stream Cursor usage into your observability stack.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
