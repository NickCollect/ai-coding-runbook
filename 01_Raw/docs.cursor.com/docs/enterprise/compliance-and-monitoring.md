---
source_url: https://cursor.com/docs/enterprise/compliance-and-monitoring
fetched_at: 2026-09-28T06:10:42.476318+00:00
fetch_method: mintlify_md
---

# Compliance and Monitoring

Compliance requires visibility into who did what, when, and why. This documentation covers audit logs, AI code tracking, certifications, and how to meet regulatory requirements.

## Audit logs

Audit logs provide a record of security events and administrative actions. Available on the [Enterprise plan](https://cursor.com/contact-sales?source=docs-audit-logs), audit logs help you meet compliance requirements and investigate security incidents.

We log the following events:

- **Authentication events:** Logins and logouts
- **User management:** User additions (via SSO, invite, signup, team creation, or auto-enrollment), removals, role changes, and individual spend limits
- **API key management:** Team and user API key creation and revocation
- **Team settings:** Team-wide and per-user spending limits, admin settings, team name changes, Slack integration settings, and repository mappings
- **Repository management:** Repository creation, deletion, and settings updates
- **Cloud Agent environments:** Environment creation, updates, restores, and lifecycle changes
- **Directory groups:** Directory group creation, updates, deletion, membership changes, and permission modifications
- **Privacy settings:** Privacy Mode changes at user or team level
- **Team rules:** Team rule management (including Bugbot rules) for custom workflows
- **Team commands:** Custom command creation, updates, and deletion
- **Grok Bot:** Team enablement, Bot creation, member access changes, Team Setup manifests, Bot templates, computers, and routines
- **Integrations:** MCP server configuration, authentication, and Slack account links

We do not log agent responses or generated code content.

Instead, we recommend using [hooks](https://cursor.com/docs/hooks.md) to log prompts and code.

### Accessing audit logs

View audit logs in the [team dashboard](https://cursor.com/dashboard/audit-log). This is available on Enterprise plans, and requires admin access.

### Streaming audit logs

For compliance and security monitoring, stream audit logs to your existing systems:

- SIEM systems (Splunk, Sumo Logic, Datadog, etc.)
- Webhook endpoints for custom processing
- S3 buckets for long-term retention
- Log aggregators like Elasticsearch or CloudWatch

Please contact [hi@cursor.com](mailto:hi@cursor.com) if you would like to receive streaming audit logs. Streamed events include `application_type`.

### Log format

Audit logs are delivered as JSON and include metadata and event-specific fields:

```json
{
  "metadata": {
    "timestamp": "2024-10-14T18:30:45Z",
    "event_id": "evt_abc123xyz789"
  },
  "team_id": "team_xyz789",
  "ip_address": "203.0.113.42",
  "user_email": "alice@company.com",
  "application_type": "grok_bot",
  "event": { /* event-specific fields */ }
}
```

Audit logs do not include OpenTelemetry trace or span ids. `metadata.event_id` identifies one audit event; it does not group related events. To group recorded Grok Bot actions by Bot or turn, use [OpenTelemetry Export](https://cursor.com/docs/enterprise/opentelemetry-export.md#joining-sessions).

`application_type` is the product that performed the action: `grok_bot` for Grok Bot, or `cursor` for Cursor desktop, iOS, CLI, the Agent SDK, cursor.com, and the Admin API. It is an empty string when the application cannot be determined, and on rows written before the field existed. Older rows are not backfilled.

The `event_type` values include:

For entries that list fields, those names are keys in Admin API `event_data` and the equivalent CSV or SIEM payload.

- `login` - User login events (web or app)
- `logout` - User logout events
- `add_user` - User additions (with source: `sso`, `invite`, `signup`, `createTeam`, or `autoEnroll`)
- `remove_user` - User removals from team
- `update_user_role` - Role changes (OWNER, ADMIN, MEMBER)
- `user_spend_limit` - Individual user spending limit changes
- `team_api_key` - Team API key actions (create, revoke)
- `user_api_key` - User API key actions (create, revoke)
- `team_settings` - Team setting modifications, including:
- `team_hard_limit_dollars` - Team-wide spending hard limit
- `team_hard_limit_per_user_dollars` - Per-user hard limit
- `per_user_monthly_limit_dollars` - Monthly spending limits per user
- `admin_only_usage_pricing` - Admin-only usage pricing settings
- `team_admin_settings` - General admin settings
- `team_name` - Team name changes
- `slack_default_repo` - Slack integration repository settings
- `slack_default_branch` - Slack integration branch settings
- `slack_default_model` - Slack integration model settings
- `slack_share_summary` - Slack summary sharing settings
- `slack_share_summary_in_external_channel` - External channel sharing
- `slack_channel_repo_mappings` - Slack channel to repository mappings
- `mcp_server_config` - MCP server configuration changes (`create`, `update`, `rename`, `delete`). Fields: `action`, `server_name`, `server_type`, `scope`
- `team_repo` - Repository actions (create, delete, update\_settings)
- `create_directory_group` - Directory group creation
- `update_directory_group` - Directory group updates
- `update_directory_group_permissions` - Directory group permission changes
- `delete_directory_group` - Directory group deletion
- `add_user_to_directory_group` - Adding users to directory groups
- `remove_user_from_directory_group` - Removing users from directory groups
- `privacy_mode` - Privacy Mode changes (scope: "user" or "team")
- `team_rule` - Team rule management (create, update, delete)
- `team_hook` - Team hooks management (create, update, delete)
- `bugbot_installation` - Bugbot installation events
- `bugbot_installation_settings` - Bugbot installation settings changes
- `bugbot_repo_settings` - Bugbot repository settings changes
- `bugbot_team_rule` - Bugbot-specific rule management (create, update, delete)
- `bugbot_team_settings` - Bugbot team settings changes
- `bugbot_bulk_repo_update` - Bugbot bulk repository update events
- `team_command` - Custom team command management (create, update, delete)
- `grok_bot_created` - Bot creation. Fields: `agent_id`, `name`, `source`, `template_id`
- `grok_bot_lifecycle` - Bot profile and lifecycle changes (`update`, `rename`, `delete`, `primary_bot_changed`). Fields: `agent_id`, `action`, `changed_fields`, `primary_bot_cleared`, `previous_agent_id`
- `sand_onboarding` - Team Grok Bot enablement changes (`new_completed=true` means enabled; `false` means disabled). Fields: `old_completed`, `new_completed`, `source`
- `grok_bot_access_changed` - Member access changes. Fields: `old_mode`, `new_mode`, `old_group_ids`, `new_group_ids`, `old_group_names`, `new_group_names`
- `grok_bot_team_setup_manifest` - Team Setup manifest changes (`save`, `delete`). Fields: `action`, `manifest_id`, `revision`, `entry_count`, `entry_ids`
- `grok_bot_group_settings` - Group-owned Grok Bot setting changes. Fields: `group_id`, `group_name`, `setting_name`, `old_value`, `new_value`
- `grok_bot_group_resource` - Group Rule changes (`create`, `update`, `delete`) and Group Setup Script changes (`save`, `delete`). Fields: `group_id`, `group_name`, `resource`, `action`, `resource_id`, `resource_name`
- `mcp_authentication` - MCP OAuth authentication, disconnection, and account removal (`authenticate`, `revoke`, `remove_account`). An empty `action` means `authenticate`. Fields: `server_name`, `scope`, `service_account_id`, `action`
- `slack_account_link` - Slack account linking (`link`, `relink`). Fields: `action`, `slack_team_id`, `slack_user_id`, `workspace_changed`. Dashboard titles for these rows stay unsuffixed
- `grok_bot_resource` - Bot template changes (`create`, `publish`, `visibility_changed`, `delete`). Fields: `resource_type`, `resource_id`, `action`, `visibility`, `previous_visibility`

PUBLIC template rows go to the affected team, the request's team, or the member's sole team; no row is recorded when a team cannot be determined uniquely.

- `grok_bot_machine` - Registered local computer changes (`register`, `rename`). Fields: `action`, `machine_id`
- `grok_bot_vm` - Grok Bot Computer changes (`image_update_completed`, `reset`, `force_recreate`, `kill`). Fields: `action`, `tenant_id`, `operation_id`, `target_user_id`, `target_user_email`, `deleted_count`
- `grok_bot_vm_bulk` - Grok Bot Computer changes across multiple members (`bulk_recreate`, `bulk_kill`, `bulk_permanent_delete`). Fields: `action`, `operation_id`, `target_count`, `succeeded_count`, `skipped_count`, `failed_count`
- `grok_bot_routine` - Routine changes (`create`, `update`, `enable`, `disable`, `delete`). Fields: `action`, `automation_id`, `name`, `execution_runtime`, `sand_agent_id`, `trigger_type`, `creation_source`, `scope`, `enabled`

In the **User** column, signed-in members and admins appear as their email; `Bot: <owner email>` means the Bot performed the change during its owner's conversation turn, `Api Key: <name>` identifies an API key without an associated user, and `System` means no member, API key, or Bot was identified.

Grok Bot payloads carry identifiers and changed field names, never content such as instructions, template bodies, Group Rule or Setup Script text, MCP URLs, or credentials.

### Searching and filtering

Filter audit logs in the dashboard by:

- Date range
- Event type (authentication, user management, settings)
- Actor (specific user)
- Application (all applications, or Grok Bot)

Export filtered results to CSV for analysis or compliance reports. The export includes an Application column.

## Usage telemetry over OpenTelemetry

Audit logs cover administrative and security events. If you want usage or activity data instead, such as token, tool call, and cost metrics, API request and cloud agent logs, and recorded Grok Bot actions (with [Action Recording](https://cursor.com/docs/grok-bot/security.md#logging-and-audit) enabled) delivered over OTLP to your own collector, use [OpenTelemetry Export](https://cursor.com/docs/enterprise/opentelemetry-export.md). It's a separate pipeline from audit-log SIEM streaming and is available on the Enterprise plan.

## Using hooks for compliance logging

Audit logs track administrative actions, but some compliance requirements need logging of development activity. Use hooks to log:

### Prompts submitted hook

```bash
#!/bin/bash
input=$(cat)
prompt=$(echo "$input" | jq -r '.prompt')
user_id=$(echo "$input" | jq -r '.user_id')

# Log to your compliance system
curl -X POST "https://compliance.company.com/log" \
  -H "Content-Type: application/json" \
  -d "{\"type\":\"prompt\",\"user\":\"$user_id\",\"timestamp\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}"

cat << EOF
{
  "continue": true
}
EOF
```

### Code generated hook

```bash
#!/bin/bash
input=$(cat)
file_path=$(echo "$input" | jq -r '.file_path')
edits=$(echo "$input" | jq -r '.edits')

# Log the code generation event (not the actual code)
curl -X POST "https://compliance.company.com/log" \
  -H "Content-Type: application/json" \
  -d "{\"type\":\"generation\",\"file\":\"$file_path\",\"timestamp\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}"

exit 0
```

**Important:** Be careful logging actual code or prompts. They may contain sensitive information. Log metadata (who, when, what file) rather than content when possible.

See [Hooks](https://cursor.com/docs/hooks.md) for hook implementation details.

## Certifications and compliance

Cursor maintains compliance with industry standards, including SOC 2 Type II, GDPR, and more.

Access compliance documentation through the [Trust Center](https://trust.cursor.com/) including:

- SOC 2 reports
- Penetration test summaries
- Security architecture documentation
- Data flow diagrams

## Responsible disclosure

If you discover a security vulnerability in Cursor, report it through our responsible disclosure program:

Email [security-reports@cursor.com](mailto:security-reports@cursor.com) with the following information:

1. A detailed description of the vulnerability
2. Steps to reproduce the issue
3. Any relevant screenshots or proof of concept

### Audit logs are available on the Enterprise plan

Contact our team to learn more about compliance features.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
