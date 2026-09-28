---
source_url: https://cursor.com/docs/enterprise/opentelemetry-export/wire
fetched_at: 2026-09-28T06:10:42.692722+00:00
fetch_method: mintlify_md
---

# OpenTelemetry Export Wire Reference

Companion to [OpenTelemetry Export](https://cursor.com/docs/enterprise/opentelemetry-export.md). Full wire surface: every metric, log event, attribute, enum, and presence rule.

The surface is additive. Tolerate unknown attributes, events, and enum values. Renames and removals get explicit notice.

## Transport and scope

- OTLP/HTTP binary protobuf (`application/x-protobuf`), `POST`
- Endpoints: `<base>/v1/metrics` and `<base>/v1/logs`
- Scope: `cursor.telemetry` / `0.1.0`

## Resource attributes

One resource per (team, user, surface, entrypoint, surface version) grouping.

| Attribute                | Type   | Presence | Values / notes                                                                                                                                                                                                                                    |
| ------------------------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `service.name`           | string | Always   | Constant `cursor`                                                                                                                                                                                                                                 |
| `service.version`        | string | Optional | Client version when source is desktop/CLI; usually absent on `cloud_agent` / `bugbot`                                                                                                                                                             |
| `cursor.team.id`         | int    | Always   | Your team id                                                                                                                                                                                                                                      |
| `cursor.surface`         | string | Always   | `unspecified` \| `desktop` \| `cli` \| `cloud_agent` \| `bugbot` \| `grok_bot`                                                                                                                                                                    |
| `cursor.entrypoint`      | string | Always   | `unspecified` \| `desktop` \| `cli` \| `web` \| `mobile` \| `sdk_ts` \| `sdk_py` \| `api` \| `automation` \| `github_pr`On `grok_bot.*` records, `automation` marks a turn a routine started (`cursor.grok_bot.initiated_by=routine`)             |
| `cursor.user.id`         | int    | Optional | Opaque team-scoped user id when the source has one. Never on `cloud_agent.*` logs today; join those through `cursor.conversation.id` to the run's `api.request` logs, which carry it when a team member started the run. Do not require presence. |
| `cursor.user.account_id` | string | Optional | The member's `user_...` id, the value `GET /teams/members` on the [Admin API](https://cursor.com/docs/account/teams/admin-api.md#get-team-members) returns as `id`. A record carries both this and `cursor.user.id` or neither.                   |
| `cursor.user.email`      | string | Optional | The member's email. Present when `cursor.user.id` is present and the member has an email. Not exported for teams on Privacy Mode (Legacy). Do not require presence.                                                                               |

## Families

Family ids match the toggles in Team Settings. All default on for a new destination except `conversation_content`, which is off until the team opts in and the destination turns on the toggle for each kind (see [Conversation content](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#conversation-content)).

| Family id                | Signals        | Default                                              | Covers                                                                                                                                                                                                                                                                                           |
| ------------------------ | -------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `model_usage`            | metrics + logs | On                                                   | `token.usage`, `cost.usage`; `api.request`, `api.error`, `api.correction`                                                                                                                                                                                                                        |
| `tool_calls`             | metrics        | On                                                   | `tool.calls`                                                                                                                                                                                                                                                                                     |
| `skills_hooks_plugins`   | logs           | On                                                   | `skill.activated` (every surface, Grok Bot included), `hook.execution_complete`, `plugin.installed`                                                                                                                                                                                              |
| `cloud_agents`           | logs           | On                                                   | `cloud_agent.pull_request`, `cloud_agent.setup`, `cloud_agent.artifact`, `cloud_agent.mcp_auth_error`                                                                                                                                                                                            |
| `grok_bot_agent_actions` | logs           | On (needs Action Recording)                          | `grok_bot.mcp_tool_call`, `grok_bot.shell_command`, `grok_bot.browser_navigation`, `grok_bot.computer_use_session`, `grok_bot.tool_result`, `grok_bot.tool_decision`, `grok_bot.file_transfer`, `grok_bot.message_delivery`, `grok_bot.routine_run`, `grok_bot.guardrail`, `grok_bot.delegation` |
| `conversation_content`   | logs           | **Off** (team opt-in + per-kind destination toggles) | `conversation.user_message`, `conversation.assistant_message`, `conversation.tool_io`                                                                                                                                                                                                            |

The `grok_bot_agent_actions` family, and `skill.activated` when a Bot emits it, carry Action Recording data. They flow only after a team admin turns on **Action Recording** on the [Grok Bot page](https://cursor.com/dashboard/bot) of the dashboard. Privacy Mode (Legacy) forces recording off.

## Metrics

All metrics are monotonic **delta** sums. Metric datapoints carry no correlation IDs; those appear on logs only.

Consume metrics as sums of deltas per series. A series is the resource, the metric name, and the exact datapoint attribute set. Windows for the same series can overlap across flushes.

### `cursor.token.usage`

Unit `{token}`. Family `model_usage`.

| Attribute             | Type   | Presence | Values / notes                                                                                                                                                                                                     |
| --------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `cursor.token.type`   | string | Always   | `input` \| `output` \| `cache_read` \| `cache_creation`                                                                                                                                                            |
| `cursor.model.name`   | string | Optional | Requested public model after routed-intent collapse (`auto:` to `Auto`, `thinking:` to `Thinking`, `pro:` to `Pro`, `premium:` to `Premium`; else pass-through). Absent on bugbot or when the source had no model. |
| `cursor.api.status`   | string | Optional | `success` \| `errored` \| `aborted`                                                                                                                                                                                |
| `cursor.api.billable` | bool   | Optional |                                                                                                                                                                                                                    |

### `cursor.tool.calls`

Unit `{call}`. Family `tool_calls`. Value `1` per completed tool call.

| Attribute                | Type   | Presence | Values / notes                                                     |
| ------------------------ | ------ | -------- | ------------------------------------------------------------------ |
| `cursor.tool.kind`       | string | Always   | `builtin` \| `mcp`                                                 |
| `cursor.tool.name`       | string | Always   | Builtin id (e.g. `read`, `shell`) or customer MCP tool name (open) |
| `cursor.tool.status`     | string | Always   | `success` \| `failure` \| `aborted` (MCP never reports `aborted`)  |
| `cursor.mcp.server.name` | string | MCP only | Customer-defined server display name (open)                        |

### `cursor.cost.usage`

Unit `USD` (double). Family `model_usage`. Best-effort estimated cost at event time, **not an invoice**. Subject to `cursor.api.correction`. For BYOK, this is the Cursor Token Rate only, not provider spend.

| Attribute           | Type   | Presence | Values / notes                       |
| ------------------- | ------ | -------- | ------------------------------------ |
| `cursor.model.name` | string | Optional | Same collapse rules as `token.usage` |

## Log events

Severities: INFO=9, WARN=13, ERROR=17.

### Common log attributes

| Attribute                | Type   | Presence | Notes                                                                                                                                                                                                                                                                                                                          |
| ------------------------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `cursor.event.id`        | string | Always   | **Dedupe key.** Opaque. Deterministic across retries, worker restarts, and Cursor Kafka replay. Prefix `customer-telemetry:v1:...` is stable; treat the whole string as opaque.                                                                                                                                                |
| `cursor.source_event.id` | string | Always   | Opaque internal source identity. Several signals may share one value.                                                                                                                                                                                                                                                          |
| `cursor.request.id`      | string | Optional | On `api.request`, `api.error`, `skill.activated` (except Bot activations), `hook.execution_complete`, `plugin.installed`. Never on `api.correction`, `cloud_agent.*`, or `grok_bot.*`. Don't depend on it on `conversation.*`.                                                                                                 |
| `cursor.conversation.id` | string | Optional | IDE/CLI: composer UUID. Cloud agent: customer-visible `bc-...` agent id. Grok Bot (`grok_bot.*`, and any log with `cursor.surface=grok_bot`): the identifier for the Bot. That value is the Bot's conversation id. Join key for session reconstruction across api, skill/hook, cloud\_agent, grok\_bot, and conversation logs. |
| `cursor.usage_event.id`  | string | Optional | `api.request` / `api.error` / `api.correction` only. Request-grain key against Cursor usage and billing exports.                                                                                                                                                                                                               |

### `cursor.api.request`

INFO, body `api_request`. Family `model_usage`.

| Attribute                                  | Type   | Presence                | Notes                                                                                                                                                                                                                                                                 |
| ------------------------------------------ | ------ | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor.api.request.input_tokens`          | int    | Always                  |                                                                                                                                                                                                                                                                       |
| `cursor.api.request.output_tokens`         | int    | Always                  |                                                                                                                                                                                                                                                                       |
| `cursor.api.request.cache_read_tokens`     | int    | Always                  |                                                                                                                                                                                                                                                                       |
| `cursor.api.request.cache_creation_tokens` | int    | Always                  |                                                                                                                                                                                                                                                                       |
| `cursor.model.name`                        | string | Optional                |                                                                                                                                                                                                                                                                       |
| `cursor.api.billable`                      | bool   | Optional                |                                                                                                                                                                                                                                                                       |
| `cursor.grok_bot.turn.id`                  | string | `grok_bot` surface only | Same value as `cursor.request.id`: the Bot turn that made the model call. Join it to the turn's `grok_bot.*` action records. A Grok Bot model call made outside a turn (avatar generation) carries an id here that joins to no action record. Never on other surfaces |

### `cursor.api.error`

ERROR, body `api_error`. Family `model_usage`. No raw error messages. Low-cardinality kind and status attributes are planned; don't depend on them yet.

| Attribute                 | Type   | Presence                | Notes                                                |
| ------------------------- | ------ | ----------------------- | ---------------------------------------------------- |
| `cursor.model.name`       | string | Optional                |                                                      |
| `cursor.api.billable`     | bool   | Optional                |                                                      |
| `cursor.grok_bot.turn.id` | string | `grok_bot` surface only | Same value as `cursor.request.id`; see `api.request` |

### `cursor.api.correction`

WARN, body `api_correction_<kind>`. Family `model_usage`. Billing finalization: the usage event was retroactively **not** billed. Join on `cursor.usage_event.id` and drop the whole group for billing. Deliberately carries no `cursor.model.name`.

| Attribute                    | Type   | Presence | Values                                                      |
| ---------------------------- | ------ | -------- | ----------------------------------------------------------- |
| `cursor.api.correction.kind` | string | Always   | `not_billed_errored` \| `not_billed_aborted_before_timeout` |

### `cursor.skill.activated`

INFO, body `skill_activated`. Family `skills_hooks_plugins`.

| Attribute              | Type   | Presence | Values / notes                                                                 |
| ---------------------- | ------ | -------- | ------------------------------------------------------------------------------ |
| `cursor.skill.name`    | string | Always   | Customer-authored (open)                                                       |
| `cursor.skill.trigger` | string | Always   | `agent_read` \| `manually_attached` \| `skill_name_in_prompt`                  |
| `cursor.skill.source`  | string | Always   | `unspecified` \| `workspace` \| `user` \| `builtin` \| `plugin` \| `claude`    |
| `cursor.plugin.name`   | string | Optional | When the skill came from a plugin. Not exported for Grok Bot activations today |

A Bot reading a `SKILL.md` exports this same event with `cursor.surface=grok_bot`, and the record carries the [shared `grok_bot.*` attributes](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#shared-grok_bot-attributes) so it joins the turn's other actions. `cursor.skill.name` is the skill's folder slug, `cursor.skill.trigger` is `agent_read` or `skill_name_in_prompt` (a skill invoked with `/` or `@` is not recorded yet), and `cursor.skill.source` is `builtin` for Cursor-managed skills, `plugin` for installed plugin skills, `user` for the Bot's own, and otherwise classified as on every other surface. `cursor.grok_bot.tool_call.id` is the id of the Read that activated the skill and joins its `tool_result` row. Bot activations carry `cursor.conversation.id` and never `cursor.request.id`, and they flow only when Action Recording is on.

### `cursor.hook.execution_complete`

INFO (ERROR for `failed` / `timeout`), body `hook_execution_complete`. Family `skills_hooks_plugins`.

| Attribute                 | Type   | Presence | Values / notes                                                                                                                                                                             |
| ------------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `cursor.hook.name`        | string | Always   | Customer-configured (open)                                                                                                                                                                 |
| `cursor.hook.type`        | string | Always   | `pre_tool_use` \| `post_tool_use` \| `post_tool_use_failure` \| `before_submit_prompt` \| `after_agent_response` \| `after_agent_thought` \| `stop` \| `subagent_start` \| `subagent_stop` |
| `cursor.hook.outcome`     | string | Always   | `success` \| `blocked` \| `failed` \| `timeout`                                                                                                                                            |
| `cursor.hook.duration_ms` | int    | Always   |                                                                                                                                                                                            |
| `cursor.plugin.name`      | string | Optional | When the hook came from a plugin                                                                                                                                                           |

### `cursor.plugin.installed`

INFO, body `plugin_installed`. Family `skills_hooks_plugins`. No `conversation.id` (install is not conversation-scoped).

| Attribute             | Type   | Presence | Values / notes                                     |
| --------------------- | ------ | -------- | -------------------------------------------------- |
| `cursor.plugin.name`  | string | Always   | Open                                               |
| `cursor.plugin.scope` | string | Always   | `unspecified` \| `public` \| `private_marketplace` |

### `cursor.cloud_agent.pull_request`

INFO (`opened`) / WARN (`creation_failed`), body `cloud_agent_pull_request_<kind>`. Family `cloud_agents`. `conversation.id` = `bc-...`.

| Attribute                                | Type   | Presence      | Values / notes                |
| ---------------------------------------- | ------ | ------------- | ----------------------------- |
| `cursor.cloud_agent.pull_request.kind`   | string | Always        | `opened` \| `creation_failed` |
| `cursor.cloud_agent.pull_request.number` | int    | `opened` only |                               |
| `cursor.cloud_agent.pull_request.draft`  | bool   | `opened` only |                               |

`creation_failed` is live. `opened` may be sparse while the producer rolls out.

### `cursor.cloud_agent.setup`

INFO (`started` / `completed`) / ERROR (`failed`), body `cloud_agent_setup_<kind>`. Family `cloud_agents`. `conversation.id` = `bc-...`.

| Attribute                              | Type   | Presence                    | Values / notes                                  |
| -------------------------------------- | ------ | --------------------------- | ----------------------------------------------- |
| `cursor.cloud_agent.setup.kind`        | string | Always                      | `started` \| `completed` \| `failed`            |
| `cursor.cloud_agent.setup.duration_ms` | int    | Terminal kinds when present | `completed` / `failed`                          |
| `cursor.cloud_agent.setup.reason`      | string | `failed` only               | Open vocabulary (e.g. `install_command_failed`) |

### `cursor.cloud_agent.artifact`

INFO, body `cloud_agent_artifact_created`. Family `cloud_agents`. `conversation.id` = `bc-...`.

| Attribute                                  | Type   | Presence | Values / notes |
| ------------------------------------------ | ------ | -------- | -------------- |
| `cursor.cloud_agent.artifact.file_name`    | string | Always   | Open           |
| `cursor.cloud_agent.artifact.content_type` | string | Optional | MIME           |

### `cursor.cloud_agent.mcp_auth_error`

ERROR, body `cloud_agent_mcp_auth_error`. Family `cloud_agents`. `conversation.id` = `bc-...`.

An MCP server you connected rejected the run's credentials. That server's tool calls failed while the run continued. ERROR because only you can fix the integration; alert on this to catch Automations and Cloud Agents silently losing an MCP server.

| Attribute                | Type   | Presence | Values / notes                                                                                                               |
| ------------------------ | ------ | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `cursor.mcp.server.name` | string | Always   | Customer-defined server display name (open), e.g. `github`. Same value space as the `cursor.tool.calls` datapoint attribute. |

### Shared `grok_bot.*` attributes

The bot itself is identified by [`cursor.conversation.id`](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#common-log-attributes) on every `grok_bot.*` record, and that value is the Bot's conversation id; `cursor.grok_bot.subagent.id` names a subagent when one acted. The `grok_bot.*` events carry Bot actions from Action Recording. Family `grok_bot_agent_actions`. Every record has `cursor.surface=grok_bot`.

Every event is metadata about an action, never its content. Tool arguments and results, file paths and names, message bodies and recipients, credentials, card details, and the Auto-review classifier's reasoning are never exported on these events; MCP arguments and results ship only as the opt-in [`cursor.conversation.tool_io`](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#cursorconversationtool_io) record. The exceptions are named per event: the shell command text (secret-scrubbed and capped at 8 KiB), the normalized browser URL and page title, and bare hostnames. Every free-text field is scrubbed for credential shapes, payment card numbers, and OAuth tokens before it can reach your collector.

Each event also carries these attributes:

| Attribute                        | Type   | Presence | Values / notes                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor.grok_bot.provenance`     | string | Always   | `client` (reported by the Bot's computer; best-effort) \| `server` (observed by Cursor; cannot be skipped). On a `server` row the correlation fields (`turn.id`, `tool_call.id`, `event.sequence`) still come from the Bot's computer and carry `client` trust                                                                                                                                                                                     |
| `cursor.grok_bot.turn.id`        | string | Optional | Request id of the Bot turn (or subagent request) that performed the action. The same value appears as `cursor.grok_bot.turn.id` on the turn's `api.request` and `api.error` records                                                                                                                                                                                                                                                                |
| `cursor.grok_bot.root_turn.id`   | string | Optional | Request id of the user-facing turn the action serves. Equal to `turn.id` outside subagents; for a subagent's action, the turn that spawned it. Absent on `server` provenance                                                                                                                                                                                                                                                                       |
| `cursor.grok_bot.subagent.id`    | string | Optional | Conversation id of the subagent that performed the action. Absent when the top-level Bot did, and on `server` provenance                                                                                                                                                                                                                                                                                                                           |
| `cursor.grok_bot.box.id`         | string | Optional | Grok Bot computer id. Absent on `server` provenance                                                                                                                                                                                                                                                                                                                                                                                                |
| `cursor.grok_bot.event.sequence` | int    | Optional | Per-turn monotonic sequence number, keyed by `turn.id`. Sort a turn's actions by it instead of by client clocks. Not dense: a turn resumed after an approval wait continues above its last number, and a retry continues from its own block, so retried rows still sort after the first run. Absent from older Grok Bot versions                                                                                                                   |
| `cursor.grok_bot.tool_call.id`   | string | Optional | Tool-call id of the action. Every row one tool call produced carries the same value (its `tool_result`, its `tool_decision` rows, and its tool-specific row such as `mcp_tool_call`), so they join on it. Absent when the action is not attributed to a tool call (a browser navigation, a shell command)                                                                                                                                          |
| `cursor.grok_bot.initiated_by`   | string | Optional | Who started the turn the action belongs to: `user` (a typed message or voice call) \| `agent` (a peer Bot's wake, or a seat's turn in a group room) \| `routine` (a routine fire; such records also carry `cursor.entrypoint=automation`) \| `subagent` (a subagent's own actions inside its parent's turn). Absent on `server` provenance, on system-started turns (an inbound Slack or Teams wake, onboarding), and from older Grok Bot versions |

### `cursor.grok_bot.mcp_tool_call`

INFO (ERROR for `failure` status), body `grok_bot_mcp_tool_call`. Family `grok_bot_agent_actions`. One MCP tool call made by a Bot. This row never carries tool arguments or results. For `http` calls, a team with tool I/O enabled receives them as two [`cursor.conversation.tool_io`](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#cursorconversationtool_io) records, joined to this row on `cursor.grok_bot.tool_call.id`.

| Attribute                         | Type   | Presence | Values / notes                                        |
| --------------------------------- | ------ | -------- | ----------------------------------------------------- |
| `cursor.tool.name`                | string | Always   | Customer-defined MCP tool name (open)                 |
| `cursor.tool.status`              | string | Always   | `success` \| `failure`                                |
| `cursor.grok_bot.mcp.transport`   | string | Always   | `http` (server-observed) \| `stdio` (on the computer) |
| `cursor.grok_bot.mcp.duration_ms` | int    | Always   |                                                       |
| `cursor.mcp.server.name`          | string | Optional | Customer-defined server display name (open)           |

`cursor.grok_bot.tool_call.id` is present on every MCP call. Connector calls, including the browser tools on the Bot's computer, are recorded here and never as `tool_result`, so each tool call is recorded once.

### `cursor.grok_bot.shell_command`

INFO (WARN when blocked), body `grok_bot_shell_command`. Family `grok_bot_agent_actions`. A shell command a Bot ran or was blocked from running. The record is written when the command settles and keeps the issue time as its timestamp, so a long command's record arrives well after its timestamp.

| Attribute                                      | Type      | Presence | Values / notes                                                                                                                                                                     |
| ---------------------------------------------- | --------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor.grok_bot.shell.command`                | string    | Always   | Secret-scrubbed command text, at most 8 KiB (open)                                                                                                                                 |
| `cursor.grok_bot.shell.command_truncated`      | bool      | Always   | True when the source command exceeded the cap                                                                                                                                      |
| `cursor.grok_bot.shell.kind`                   | string    | Always   | `foreground` \| `background`                                                                                                                                                       |
| `cursor.grok_bot.shell.target`                 | string    | Always   | `box` (the Grok Bot computer) \| `user_machine`                                                                                                                                    |
| `cursor.grok_bot.shell.allowed`                | bool      | Always   | Shell policy decision                                                                                                                                                              |
| `cursor.grok_bot.shell.blocked_reason`         | string    | Optional | Policy reason when blocked; secret-scrubbed (open)                                                                                                                                 |
| `cursor.grok_bot.shell.classification_reasons` | string\[] | Optional | At most 10 policy classification reasons; secret-scrubbed (open)                                                                                                                   |
| `cursor.grok_bot.shell.machine_id`             | string    | Optional | `user_machine` target only: the registered user machine the command ran on (open). Only a machine registered at turn start is named                                                |
| `cursor.grok_bot.shell.exit_code`              | int       | Optional | Process exit code; `-1` when killed by a signal or aborted. Absent for `background` commands and when the command never produced an exit (connection lost, rejected before it ran) |
| `cursor.grok_bot.shell.duration_ms`            | int       | Optional | Wall time from issue to settle, including the connection to the computer and any wait before the process started. Present on every `foreground` record, absent on `background`     |

### `cursor.grok_bot.browser_navigation`

INFO, body `grok_bot_browser_navigation`. Family `grok_bot_agent_actions`. `conversation.id` is the identifier for the Bot.

| Attribute                            | Type   | Presence | Values / notes                                                                |
| ------------------------------------ | ------ | -------- | ----------------------------------------------------------------------------- |
| `cursor.grok_bot.browser.url`        | string | Always   | Normalized `scheme://host/path` (open). Non-hierarchical schemes never export |
| `cursor.grok_bot.browser.page_title` | string | Optional | Secret-scrubbed (open)                                                        |

### `cursor.grok_bot.computer_use_session`

INFO, body `grok_bot_computer_use_session`. Family `grok_bot_agent_actions`. Summary of one computer-use subagent session: counts and wall time only. No coordinates, typed text, or screenshots. `cursor.grok_bot.turn.id` is the parent turn that invoked the subagent, `cursor.grok_bot.subagent.id` the subagent itself, `cursor.grok_bot.tool_call.id` the invocation, and `cursor.grok_bot.initiated_by` is always `subagent`.

| Attribute                                           | Type | Presence | Values / notes                                                                                                                                       |
| --------------------------------------------------- | ---- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor.grok_bot.computer_use.action_count`         | int  | Always   |                                                                                                                                                      |
| `cursor.grok_bot.computer_use.duration_ms`          | int  | Always   |                                                                                                                                                      |
| `cursor.grok_bot.computer_use.screenshot_count`     | int  | Always   |                                                                                                                                                      |
| `cursor.grok_bot.computer_use.action_counts.<kind>` | int  | Optional | One attribute per action kind with a positive count. `<kind>` is one of `click`, `drag`, `key`, `mouse_move`, `screenshot`, `scroll`, `type`, `wait` |

### `cursor.grok_bot.tool_result`

INFO (`success` / `cancelled`), WARN (`denied`), ERROR (`error`), body `grok_bot_tool_result`. Family `grok_bot_agent_actions`. One settled builtin tool call made by a Bot (`read`, `web_search`, `send_to_user`, `task`, `shell`, ...). This is the row every builtin tool produces, so no tool a Bot can call goes unrecorded. Connector (MCP) calls are `mcp_tool_call` rows and never appear here.

`cursor.grok_bot.tool_call.id` joins the row to the `tool_decision` rows of the same call. One id can carry two `tool_result` rows when a call re-runs after a transient model-stream failure, so count distinct ids when counting calls.

| Attribute                                    | Type   | Presence | Values / notes                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor.tool.name`                           | string | Always   | Builtin tool id, lowercased; the same value space as the `cursor.tool.calls` builtin `tool.name` dimension (`read`, `shell`, `web_search`, ...)                                                                                                                                                                                   |
| `cursor.grok_bot.tool_result.outcome`        | string | Always   | `success` (the tool returned, including a tool that handed a refusal to the model as text; the call's `tool_decision` rows say whether the action happened) \| `error` \| `denied` (a policy or permission gate refused the call before it ran) \| `cancelled` (the turn was interrupted or the call timed out)                   |
| `cursor.grok_bot.tool_result.duration_ms`    | int    | Always   |                                                                                                                                                                                                                                                                                                                                   |
| `cursor.grok_bot.tool_result.error_category` | string | Optional | Coded reason when `outcome` is not `success`: `invalid_args`, `user_rejected`, `timeout`, `provider_error`, `hook_denied`, or an error class name such as `TimeoutError` (open)                                                                                                                                                   |
| `cursor.grok_bot.tool_result.target_host`    | string | Optional | The bare host a tool acted on, for tools that target a site: `list_credentials` reports the site a credential lookup was scoped to, `request_virtual_card` the merchant. Lowercased, without `www.`, port, path, query, or userinfo. Absent for every other tool, when the call named no site, and when the call never ran (open) |

Read `outcome` as "how the call returned", not "whether the action happened". The shells, browser and computer actions, and local-tool asks the person declined report a refusal as `denied` with `error_category` `user_rejected`. Mail, routine writes, connector file transfers, subagent launches, and cloud agent actions hand a refusal back to the model as text, so their `tool_result` reads `success` while the `tool_decision` row records the refusal.

### `cursor.grok_bot.tool_decision`

INFO (`allowed` / `held`), WARN (`denied` / `timed_out`), body `grok_bot_tool_decision`. Family `grok_bot_agent_actions`. One decision about whether a Bot's tool call may run: who made it, through which approval mode, and what it was. A call can carry several decisions (Auto-review refuses to auto-allow, then a person answers the card), each its own record. They join the call's `tool_result`, `mcp_tool_call`, or `computer_use_session` row on `cursor.grok_bot.tool_call.id`. The classifier's rationale, the card copy, and the arguments never appear here.

| Attribute                                | Type   | Presence | Values / notes                                                                                                                                                                                                                        |
| ---------------------------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor.grok_bot.decision.id`            | string | Always   | Id minted when the decision is made, before any person sees a card. For a `human` decision it is the id of the card or permission ask the person answered, and the value a `guardrail` escalation row of the same call carries (open) |
| `cursor.tool.name`                       | string | Always   | Builtin tool id, lowercased; the same value as the call's `tool_result`. A connector call's decision carries `mcp` while its `mcp_tool_call` row carries the server's tool name                                                       |
| `cursor.grok_bot.decision.source`        | string | Always   | `human` \| `policy` (Auto-review classifier or rule) \| `hook` (pre-tool hook) \| `automatic` (no gate consulted)                                                                                                                     |
| `cursor.grok_bot.decision.approval_mode` | string | Always   | `auto_allow` \| `ask_human` \| `auto_review` \| `local_tool_permission` \| `hook`                                                                                                                                                     |
| `cursor.grok_bot.decision.outcome`       | string | Always   | `allowed` \| `denied` \| `held` (the call waited on a person and the card was withdrawn before they answered) \| `timed_out` (the wait expired unanswered)                                                                            |
| `cursor.grok_bot.decision.rule_id`       | string | Optional | Opaque id of the Auto-review rule that decided; absent until the classifier attributes its verdict to a rule (open)                                                                                                                   |

What the sources mean:

- `policy` is every enforced Auto-review classification, `allowed` or `denied`, on any surface: the shells, connector calls, mail, routine writes, cloud agent and subagent launches. A classifier that fails or misses its deadline is a `policy` `denied`, and so is a review rule that sends a call to a person without classifying.
- `human` is what an Auto-review card ended with (`approval_mode` `auto_review` when the classifier escalated, `ask_human` when the surface always asks, such as product feedback, claiming a mail inbox, placing a phone call, or a Chrome cookie import), or a local-tool permission ask answered on the person's own computer (`local_tool_permission`). "Always" and "never" answers record as `allowed` and `denied` like a one-time answer.
- `hook` is a pre-tool hook's refusal.
- `automatic` is a call no gate spoke about, so every other builtin call that settled carries at least one decision. Three kinds of call carry none: a call the tool itself refused before any gate ran (its `tool_result` reads `denied`); a card the person answers after the turn has ended (a credential fill request, a secret request, or a virtual card request), because the answer arrives in a later turn; and a call cancelled before any gate spoke, since a `cancelled` call carries only the allowances and holds recorded before it was cut off. A virtual card request also ends the turn from inside its own call, so its `tool_result` reads `cancelled`.

A call Auto-review refused and a person then answered carries both rows, `policy` `denied` then `human`, in `event.sequence` order. There is no approver attribute: a Bot's cards are answered only by its owner, who is the record's `cursor.user.id`.

### `cursor.grok_bot.file_transfer`

INFO (`success`), WARN (`denied`), ERROR (`error`), body `grok_bot_file_transfer`. Family `grok_bot_agent_actions`. One file move a Bot tried between its computer and another endpoint: the user's machine, a connected Google Drive, OneDrive, or Gmail account, or a read of a file on the user's machine straight into the Bot's context. Metadata only: which way, the far end, how many bytes moved, and how it settled. The path, the file name, and the content never export. A read of a file on the Bot's own computer is a `tool_result` row, not this event. `cursor.grok_bot.tool_call.id` joins the row to the call's `tool_result` and, for a refused move, to its `tool_decision`.

| Attribute                             | Type   | Presence | Values / notes                                                                                                                                                                                                                                                          |
| ------------------------------------- | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor.grok_bot.file.direction`      | string | Always   | Seen from the Bot's computer: `download` (bytes landed on it) \| `upload` (bytes left it) \| `read` (bytes reached the Bot's context from the user's machine without landing on it; always with `target` `user_machine`)                                                |
| `cursor.grok_bot.file.target`         | string | Always   | `user_machine` (the user's computer) \| `cloud` (a connected cloud service account) \| `box` (another Bot computer; reserved, not produced today)                                                                                                                       |
| `cursor.grok_bot.file.outcome`        | string | Always   | `success` \| `error` (the move failed) \| `denied` (a local-tool permission, a connector review, or the machine's own filesystem refused it before any bytes left)                                                                                                      |
| `cursor.grok_bot.file.bytes`          | int    | Optional | Bytes moved; present when the move completed (an empty file exports `0`). On a `read`, the bytes handed to the Bot, so a ranged read counts its output, not the file's size                                                                                             |
| `cursor.grok_bot.file.error_category` | string | Optional | Coded reason when `outcome` is `error`: `source_missing`, `too_large`, `read_failed`, `write_failed`, `invalid_file`, a connector outcome such as `needs_auth` or `not_found`, an errno such as `ECONNRESET`, or an error class name. One token, never a message (open) |
| `cursor.grok_bot.file.machine_id`     | string | Optional | The user machine at the far end when `target` is `user_machine`: the opaque id the Bot's machine list reports (open). Only a machine registered at turn start is named                                                                                                  |

### `cursor.grok_bot.message_delivery`

INFO (`sent` / `held`), ERROR (`failed`), body `grok_bot_message_delivery`. Family `grok_bot_agent_actions`. One outbound message from a Bot: to its user in the Grok Bot chat, to another of the user's Bots, to a Slack or Discord conversation the Bot was reached through, to outside email recipients, to the user's Mac Messages app, or onto a draft card the user sends or discards themselves. The row says where the message went and whether it got there, never what it said or to whom by name: no body, subject, recipient, attachment name, or length. `cursor.grok_bot.tool_call.id` joins the row to the `tool_result` of the same send call.

| Attribute                                           | Type   | Presence | Values / notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `cursor.grok_bot.message_delivery.destination_type` | string | Always   | `user` (the Bot's own user, in the chat or on a voice call) \| `agent` (another of the user's Bots, or a group of them) \| `email` (outside recipients, from one of the user's Bot addresses) \| `channel` (a Slack or Discord channel, thread, or DM reached through a connector) \| `apple_messages` (the user's Mac Messages app) \| `draft` (an email or Slack message drafted onto a card for the user's approval)                                                                                                  |
| `cursor.grok_bot.message_delivery.destination_id`   | string | Optional | `agent`: the opaque id of the destination Bot; absent when the Bot could not resolve one. `channel`: the first 32 hex characters of the SHA-256 of `<platform>:<chat>[:<thread>]` (for example `slack:C0123ABC:1699999999.000100`), so every row to one conversation carries one value you can compute from an address you hold, while the address itself never leaves. Absent for `user`, `draft`, `email`, and `apple_messages`, so an email address, phone number, or chat id is never exported, hashed or not (open) |
| `cursor.grok_bot.message_delivery.result`           | string | Always   | `sent` \| `held` (accepted but not delivered yet: a low-priority peer message parked in the recipient's inbox, or a draft card awaiting the user's send) \| `failed`                                                                                                                                                                                                                                                                                                                                                     |
| `cursor.grok_bot.message_delivery.failure_category` | string | Optional | Coded reason when `result` is not `sent`, such as `awaiting_user`, `blocked`, `target_not_found`, `forbidden`, `no_inbox`, `sender_not_owned`, `not_approved`, `route_unverified`, `declined`, `permission_denied`, or an error class name (open)                                                                                                                                                                                                                                                                        |
| `cursor.conversation.message.id`                    | string | Optional | When present, the sent message's id on `user`, `channel`, and `draft` rows, in the shape the family's message records use (`<sessionId>/g<generation>/<entryId>`, for example `g0/t3s1`), so the delivery row joins that family's `assistant_message` record on one key. Never on `agent`, `email`, or `apple_messages` rows                                                                                                                                                                                             |

### `cursor.grok_bot.routine_run`

INFO (`success` / `cancelled`), ERROR (`error`), body `grok_bot_routine_run`. Family `grok_bot_agent_actions`. One finished routine run by a Bot: which routine fired, why, how it ended, and how long it took. Cursor records the row when it closes the run (`server` provenance), so a run is recorded whether or not the Bot's computer was watching, and the row carries no `box.id`, `event.sequence`, or `tool_call.id`. It always carries `cursor.grok_bot.initiated_by=routine` and `cursor.entrypoint=automation`. Never the routine's prompt, its name, or the turn's text.

`cursor.grok_bot.turn.id` is the turn the run executed in, so the run's own `tool_result`, `shell_command`, and `mcp_tool_call` rows join on it. A run that executed as a routine subagent, or that failed before a turn was planned, carries no `turn.id`.

| Attribute                                 | Type   | Presence | Values / notes                                                                                                                                                                                  |
| ----------------------------------------- | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor.grok_bot.routine.id`              | string | Always   | The routine's stable id (opaque)                                                                                                                                                                |
| `cursor.grok_bot.routine_run.id`          | string | Always   | The run's id, the same value the routine's run history shows (opaque)                                                                                                                           |
| `cursor.grok_bot.routine_run.trigger`     | string | Always   | `schedule` (a cron schedule fired it) \| `event` (an outside event fired it: Slack, GitHub, email, ...) \| `manual` (reserved, not emitted today; a manual "Run now" reports as `schedule`)     |
| `cursor.grok_bot.routine_run.outcome`     | string | Always   | `success` (the turn completed or paused for the user) \| `error` (the turn failed) \| `cancelled` (the turn was interrupted or superseded by a new message; the run history shows it as failed) |
| `cursor.grok_bot.routine_run.duration_ms` | int    | Always   | Fire to settle, wall time                                                                                                                                                                       |

A run that pauses on an approval and is settled by the resumed turn, and a run that failed before any turn started, are not recorded. Action Recording is a team feature, so runs of a personal (team-less) owner are skipped like every other Bot action.

### `cursor.grok_bot.guardrail`

INFO (`continued`), WARN (`warned` / `stopped`), body `grok_bot_guardrail`. Family `grok_bot_agent_actions`. A guardrail stepping in on a Bot turn: the loop detector tripping on repeated output or tool calls, a site's bot defense refusing the Bot's browser, or Auto-review stopping a tool call to ask a person and the wait that followed. Coded fields only; the classifier's rationale and the card's copy never export. The decision itself (Auto-review's refusal, the person's answer) is a `tool_decision` row and is never repeated here; an escalation row joins it on `cursor.grok_bot.decision.id`.

Rows ride WARN when the guardrail changed the turn (a nudge, a stop, a wait that ended refused or unanswered) and INFO when it only observed or the turn went on. One row per trip: a wall counts once per episode, so a page that stays on the same wall through reloads is one row.

An escalation is two rows for one card, in the order they happened. The `tool_escalation` row is the ask: a card was raised because a call under review could not run without a person. The `pause` row is the end of the wait: the person allowed (`resumed`) or refused (`denied`) the action, or nobody answered before the card expired or was withdrawn (`abandoned`). When the wait ended because a person stopped or redirected the turn instead of answering, the second row is `interrupted`. Both rows carry the escalated tool's `cursor.tool.name`, the call's `cursor.grok_bot.tool_call.id`, and the card's id as `cursor.grok_bot.decision.id`, the same value the `human` `tool_decision` row of that call carries, so the ask, the wait, and the answer join on one key.

| Attribute                               | Type   | Presence | Values / notes                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------- | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor.grok_bot.guardrail.kind`        | string | Always   | `loop_detected` \| `bot_blocked` \| `tool_escalation` (a card was raised for a tool call) \| `pause` (the wait on the card ended: answered or expired) \| `interrupted` (the wait ended because a person stopped or redirected the turn)                                                                                                                                                                                      |
| `cursor.grok_bot.guardrail.detector`    | string | Always   | What tripped, as one `snake_case` token: a loop kind (`single_message_single_line`, `multi_message`, `multi_message_outbound_flood`, ...), a bot-block family (`cloudflare_challenge`, `recaptcha`, `datadome`, `akamai`, ...), or, on the escalation kinds, the Auto-review surface that asked (`host_shell`, `box_shell`, `mcp`, `computer`, `automation_write`, `cloud_agent`, `subagent`, `feedback`, `bot_share`) (open) |
| `cursor.grok_bot.guardrail.action`      | string | Always   | `warned` (the Bot was nudged and kept going) \| `continued` (the guardrail only observed, or the turn went on after a `pause` `resumed`) \| `stopped` (the Bot could not proceed: every `tool_escalation` row, and a `pause` or `interrupted` row whose wait ended `denied` or `abandoned`)                                                                                                                                   |
| `cursor.grok_bot.guardrail.source`      | string | Always   | `runtime` (a detector: `loop_detected`, `bot_blocked`) \| `classifier` (the call went through Auto-review's classifier and escalated to a person; `approval_mode` `auto_review` on the joined `tool_decision`) \| `policy` (a review rule sent the call to a person without classifying; `approval_mode` `ask_human`)                                                                                                         |
| `cursor.grok_bot.guardrail.count`       | int    | Optional | The count that tripped the detector: the repetitions a `loop_detected` row saw. Absent when the detector counts nothing                                                                                                                                                                                                                                                                                                       |
| `cursor.grok_bot.guardrail.target_host` | string | Optional | `bot_blocked` only: the host that refused the Bot, lowercased and without `www.`, port, path, query, or userinfo (open)                                                                                                                                                                                                                                                                                                       |
| `cursor.tool.name`                      | string | Optional | Escalation kinds only: the escalated call's builtin tool id, the same value its `tool_decision` and `tool_result` rows carry                                                                                                                                                                                                                                                                                                  |
| `cursor.grok_bot.guardrail.resolution`  | string | Optional | `pause` and `interrupted` only: `resumed` (the person allowed the action) \| `denied` (the person refused it) \| `abandoned` (nobody answered: the card expired, Auto-review settings changed, or the turn was interrupted or redirected)                                                                                                                                                                                     |
| `cursor.grok_bot.guardrail.duration_ms` | int    | Optional | `pause` and `interrupted` only: the wait, from the card's creation to the answer or the card's retirement. Never negative                                                                                                                                                                                                                                                                                                     |
| `cursor.grok_bot.decision.id`           | string | Optional | Escalation kinds only: the card's id, which is the `decision.id` of the `human` `tool_decision` row the same call settles with (open)                                                                                                                                                                                                                                                                                         |

`cursor.grok_bot.tool_call.id` is present on the escalation kinds and absent on the detections, which are not attributed to one tool call. A call Auto-review refused with no one to ask raises no card and carries only its `tool_decision`.

### `cursor.grok_bot.delegation`

INFO (`dispatched`, `completed` with `success` or `stopped`), ERROR (`completed` with `error`), body `grok_bot_delegation`. Family `grok_bot_agent_actions`. Work a Bot handed to another agent and the result coming back: a background subagent it dispatched, or a Cursor cloud agent it launched or replied to. Ids and outcome only, never the prompt, the result text, or the delegate's own actions. A subagent's tool calls are its own `grok_bot.*` rows with `initiated_by=subagent`; a cloud agent's run is the `cloud_agents` family.

Two records per delegation share `target_id`: `dispatched` when the work was handed over, and `completed` when the result came back to the Bot. `completed` records take the turn that received the result as their `turn.id`, not the dispatching turn's. `cursor.grok_bot.tool_call.id` is the dispatching call (or the stop call on a `subagent_stop` record); it is on the `dispatched` record and on a subagent's `completed` record, and absent on a cloud agent's completion.

| Attribute                                | Type   | Presence         | Values / notes                                                                                                                                                                                                                                                                               |
| ---------------------------------------- | ------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor.grok_bot.delegation.direction`   | string | Always           | `dispatched` \| `completed`                                                                                                                                                                                                                                                                  |
| `cursor.grok_bot.delegation.kind`        | string | Always           | `cloud_agent_launch` \| `cloud_agent_followup` (a reply or steer that starts the agent's next run) \| `subagent_spawn` \| `subagent_stop` (the Bot's own stop ending a delegation before its result came back; always `completed` with outcome `stopped`, one per subagent the stop reached) |
| `cursor.grok_bot.delegation.target`      | string | Always           | `cloud_agent` \| `subagent`; follows from `kind`                                                                                                                                                                                                                                             |
| `cursor.grok_bot.delegation.target_id`   | string | Always           | The cloud agent's id (`bc-...`, the same value the `cloud_agents` family exports as `cursor.conversation.id`) or the subagent's conversation id (`sand-subagent-...`). Opaque                                                                                                                |
| `cursor.grok_bot.delegation.outcome`     | string | `completed` only | `success` \| `error` (aborted or expired cloud agent runs included) \| `stopped` (`subagent_stop` only)                                                                                                                                                                                      |
| `cursor.grok_bot.delegation.duration_ms` | int    | Optional         | Dispatch-to-result wall time on `completed` records. Absent when the delegate ran outside the receiving turn, and on every `dispatched` record                                                                                                                                               |

Known limits:

- Not recorded: a steer injected into a cloud agent's running turn (no new run), a launch or reply Cursor rejected, a cloud agent cancel, a run someone else started that the Bot only watches, and a routine's subagent waking its parent.
- A stopped subagent can still deliver an `error` completion afterwards, so one `target_id` can carry both a `stopped` and an `error` record.
- A cloud agent's `completed` record is best-effort: when the Bot re-watches an agent it launched in an earlier turn, the completion can carry kind `cloud_agent_launch`, and a launch re-watched mid-run can leave its `dispatched` without a `completed`. Pair the two records on `target_id` and tolerate a missing completion.
- Delivery is at-least-once like every `grok_bot.*` row: a launch, reply, or completion retried after a crash can record twice for one `target_id`. Dedupe on `cursor.event.id` first.

### Conversation content

Family `conversation_content`. The `conversation.*` events are the only log records whose body is a payload (message text or one side of an MCP tool call) instead of a constant event name. Route on the log event name, as with every other family. `cursor.conversation.user_message` is a prompt, `cursor.conversation.assistant_message` is a response, and `cursor.conversation.tool_io` is the arguments or the result of an MCP tool call; don't parse the body to tell them apart.

**Body.** Scrubbed text. Messages are capped at 32 KiB and each side of a tool call at 8 KiB. `cursor.conversation.content_truncated` is set whenever the exported body is a prefix of the redacted text, whether the source crossed the cap or redaction pushed it over, and on `tool_io` also when scrubbing left a body within the cap unparseable.

**Identity.** Records carry the [common log attributes](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#common-log-attributes). `cursor.conversation.id` joins them to the conversation's `api.request`, `skill.activated`, `hook.execution_complete`, `cloud_agent.*`, and `grok_bot.*` logs. The only user identifiers are the optional `cursor.user.*` [resource attributes](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#resource-attributes); the log attributes carry none. Don't depend on `cursor.request.id`, `cursor.usage_event.id`, or, on message records, `cursor.grok_bot.turn.id`; `tool_io` carries `turn.id` as a shared `grok_bot.*` attribute.

**Surfaces.** Cloud Agents and Grok Bot only. Cloud Agent conversations arrive with `cursor.surface=cloud_agent` on the resource. Grok Bot conversations arrive with `cursor.surface=grok_bot`, alongside the Bot's `grok_bot.*` action logs when Action Recording is on. `tool_io` is Grok Bot only. IDE, CLI, and desktop conversations are not on this family yet. Filter or route on `cursor.surface`.

**Toggles.** Each event flows only with the team opt-in and its destination toggle on: `user_message` needs **Prompts**, `assistant_message` needs **Responses**, and `tool_io` needs **Tool I/O**. The [setup page](https://cursor.com/docs/enterprise/opentelemetry-export.md#conversation-content) covers the toggles.

All three events are INFO and carry these attributes:

| Attribute                               | Type   | Presence | Values / notes                                                                                                         |
| --------------------------------------- | ------ | -------- | ---------------------------------------------------------------------------------------------------------------------- |
| `cursor.conversation.provenance`        | string | Always   | `server` (observed by Cursor). `client` is reserved; tolerate it.                                                      |
| `cursor.conversation.message.id`        | string | Always   | Message id within the conversation                                                                                     |
| `cursor.conversation.turn.id`           | string | Optional | Turn id within the conversation. Separate from `cursor.grok_bot.turn.id` on message records; equal to it on `tool_io`. |
| `cursor.conversation.content_truncated` | bool   | Always   | True when the body is a prefix of the redacted text, or, on `tool_io`, when scrubbing left it unparseable              |

#### `cursor.conversation.user_message`

INFO. Body: the scrubbed text of a user prompt.

#### `cursor.conversation.assistant_message`

INFO. Body: the scrubbed final assistant text for the response.

#### `cursor.conversation.tool_io`

INFO. Body: the scrubbed compact JSON of one side of an MCP tool call, at most 8 KiB. Two records per Grok Bot MCP tool call executed over `http` transport: the `arguments` record carries the JSON object the Bot sent, and the `result` record carries the connector's reply. On success that is the tool's text and structured content; on failure, the error, rejection, or denial message. Image bytes are replaced with their MIME type. `stdio` calls on the Bot's computer report metadata only and produce no `tool_io` record. Needs the destination's **Tool I/O** toggle in addition to the team opt-in.

Both records carry the shared [`grok_bot.*` correlation attributes](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#shared-grok_bot-attributes) (`provenance`, `turn.id`, `tool_call.id`, `event.sequence`), so `cursor.grok_bot.tool_call.id` is present and joins them to the call's [`cursor.grok_bot.mcp_tool_call`](https://cursor.com/docs/enterprise/opentelemetry-export/wire.md#cursorgrok_botmcp_tool_call) and `cursor.grok_bot.tool_decision` rows. `cursor.tool.name`, `cursor.tool.status`, and `cursor.mcp.server.name` repeat the metadata row's values so each record is readable on its own.

| Attribute                               | Type   | Presence | Values / notes                                                                                                |
| --------------------------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------- |
| `cursor.conversation.tool_io.direction` | string | Always   | `arguments` \| `result`. `cursor.conversation.message.id` on this record is `mcp:<tool_call_id>:<direction>`. |
| `cursor.tool.name`                      | string | Always   | Customer-defined MCP tool name (open)                                                                         |
| `cursor.tool.status`                    | string | Always   | `success` \| `failure`. The same value on both sides of one call.                                             |
| `cursor.mcp.server.name`                | string | Optional | Customer-defined server display name (open)                                                                   |
| `cursor.grok_bot.provenance`            | string | Always   | `server`                                                                                                      |
| `cursor.grok_bot.tool_call.id`          | string | Always   | Join key to the call's `mcp_tool_call` and `tool_decision` rows                                               |
| `cursor.grok_bot.turn.id`               | string | Optional | Same value as `cursor.conversation.turn.id` on this record                                                    |
| `cursor.grok_bot.event.sequence`        | int    | Optional | The sequence number of the call within its turn; absent from older Grok Bot versions                          |

When `cursor.conversation.content_truncated` is true the body does not parse as JSON: it is a prefix of the redacted text, or scrubbing left it unparseable and Cursor exported it flagged instead of exporting a less-scrubbed body. Check the flag before parsing. Both sides pass the same scrubber as message text, plus a key-based pass that redacts the value of any JSON member or assignment whose key names a credential (`password`, `passphrase`, `token`, `api_key`, `secret`, `secret_key`, `access_key`, `authorization`, `cookie`, `private_key`, `credentials`, and compounds such as `client_secret` or `x-api-key`), whatever the value looks like. Header pairs count too: in `[{"name":"Authorization","value":"Basic ..."}]`, the `value` sibling of a `name`, `key`, or `header` member on the list is redacted, as is the second item of a two-item array whose first is on the list (`["password","..."]`). Card fields held as numbers (`"cvc": 123`) become `[REDACTED: Card]`, and ASCII `\uXXXX` escapes are decoded before scrubbing. A private-key block split across the items of one array (lines of a file, text blocks of a result) is redacted from its BEGIN line through its END line; one split across unrelated fields is not. The key-based pass reaches one level into JSON nested inside a string value; deeper re-encoded documents are scrubbed by value shape only. See [MCP tool I/O](https://cursor.com/docs/enterprise/opentelemetry-export.md#mcp-tool-io) for what the scrubber does not catch.

## Identity and joins

| Goal                                       | Field                                       | Coverage                                                                                                                                                                                                                                              |
| ------------------------------------------ | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dedupe logs                                | `cursor.event.id`                           | Every log record                                                                                                                                                                                                                                      |
| Group by session or Bot                    | `cursor.conversation.id`                    | Logs when present. For Grok Bot, this value is the identifier for the Bot (its conversation id).                                                                                                                                                      |
| Group Grok Bot activity by turn            | `cursor.grok_bot.turn.id`                   | `grok_bot.*` logs, Bot `skill.activated` logs, `conversation.tool_io` logs, and `api.request` / `api.error` logs with `cursor.surface=grok_bot`, when present. Don't depend on it on `conversation.user_message` or `conversation.assistant_message`. |
| Order a Bot turn's actions                 | `cursor.grok_bot.event.sequence`            | `grok_bot.*` and `conversation.tool_io` logs from current Grok Bot versions. Sort by it; do not expect it to be dense                                                                                                                                 |
| Group the rows of one Bot tool call        | `cursor.grok_bot.tool_call.id`              | `tool_result`, `tool_decision`, `mcp_tool_call`, `computer_use_session`, `file_transfer`, `message_delivery`, `delegation`, guardrail escalations, Bot `skill.activated`, and, with tool I/O enabled, both `conversation.tool_io` sides               |
| Join an approval ask to its answer         | `cursor.grok_bot.decision.id`               | `tool_decision` and the `tool_escalation` / `pause` / `interrupted` `guardrail` rows of the same call                                                                                                                                                 |
| Roll a subagent's actions up to its parent | `cursor.grok_bot.root_turn.id`              | `grok_bot.*` logs with `client` provenance; `cursor.grok_bot.subagent.id` names the subagent                                                                                                                                                          |
| Attach prompts and responses to a session  | `cursor.conversation.id`                    | `conversation.*` logs (Cloud Agents and Grok Bot), only with the `conversation_content` opt-in                                                                                                                                                        |
| Group prompts and responses by turn        | `cursor.conversation.turn.id`               | `conversation.*` logs when present                                                                                                                                                                                                                    |
| Group by user                              | Resource attribute `cursor.user.account_id` | Logs and metrics when present. Joins to `id` in the Admin API `GET /teams/members` response. `cursor.user.email` on the same resource names the member directly.                                                                                      |
| Reconcile billing                          | `cursor.usage_event.id`                     | `api.request`, `api.error`, and `api.correction` logs                                                                                                                                                                                                 |

Exported logs do not carry OpenTelemetry `trace_id` or `span_id` fields. Use `cursor.conversation.id` and `cursor.grok_bot.turn.id` for Bot and turn correlation. Metrics do not carry correlation ids; use `api.request` logs for per-conversation token totals.

See [Joining sessions](https://cursor.com/docs/enterprise/opentelemetry-export.md#joining-sessions) on the setup page for recipes.

## Delivery semantics

- **Logs** are at-least-once. Transient failures recover automatically for about **7 days**; dedupe on `event.id`. Terminal rejections (persistent 4xx, bad payloads) are **not** replayed.
- **Metrics** are at-most-once. Failed metric requests are not retried or replayed.
- **No ordering guarantee.** Corrections can arrive after the requests they amend; order by record timestamp.
- **OTLP partial success** is honored. Rejected items are not re-sent.
- No backfill from before destination activation. Source retention upstream of export is also about **7 days** (separate from the delivery retry window).


---

## Sitemap

[Overview of all docs pages](/llms.txt)
