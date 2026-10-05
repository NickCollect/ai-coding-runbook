---
source_url: https://cursor.com/docs/enterprise/compliance-and-monitoring
fetched_at: 2026-10-05T06:27:20.391376+00:00
fetch_method: mintlify_md
---

# Compliance and Monitoring

Compliance requires visibility into who did what, when, and why. This documentation covers audit logs, AI code tracking, certifications, and how to meet regulatory requirements.

## Audit logs

Audit logs record who changed what in your team and organization: sign-ins, membership, roles, API keys, settings, integrations, Cloud Agent environments, Grok Bot configuration, and Origin repositories. Every event records the time, and names the actor, client IP, and product surface when a request carried them. Payloads carry identifiers, names, and changed settings, never prompts, agent output, generated code, or credentials. Audit logs are available on the [Enterprise plan](https://cursor.com/contact-sales?source=docs-audit-logs).

### What is not logged

- Agent responses, prompts, and generated code. Use [hooks](https://cursor.com/docs/hooks.md) to log development activity.
- Grok Bot actions such as shell commands and browser navigation. Those are [Action Recording](https://cursor.com/docs/grok-bot/security.md#logging-and-audit) events, delivered over [OpenTelemetry Export](https://cursor.com/docs/enterprise/opentelemetry-export.md).
- Cloud Agent automation runs. `grok_bot_routine` covers Grok Bot routines only.
- Failed sign-in attempts. `login` records successful sign-ins.
- Secret values. `cloud_agent_secret` records the secret name and scope; `cloud_agent_secret_read` records only a count.

### Log format

The Admin API returns one flat object per event:

```json
{
  "event_id": "8a1f0f0e-0d1b-4c7e-9b3a-2f6e1c9d4a55",
  "timestamp": "2026-09-14T18:30:45.123Z",
  "team_id": "12345",
  "ip_address": "203.0.113.42",
  "user_email": "alice@company.com",
  "event_type": "add_user",
  "application_type": "cursor",
  "event_data": {
    "user_email": "bob@company.com",
    "role": "member",
    "source": "invite",
    "invited_by_email": "alice@company.com",
    "invite_id": "3f9a1c2b"
  }
}
```

| Field              | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `event_id`         | UUID for one event. It doesn't group related events.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `timestamp`        | When the action happened, in UTC.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `team_id`          | Team the event belongs to. Only the organization endpoint returns it, and it's empty for organization-level events.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ip_address`       | Client IP of the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `user_email`       | The actor. Members appear as their email. `Api Key: <name>` is an API key with no associated user, `Bot: <owner email>` is a Grok Bot acting during its owner's turn, `SCIM` is a membership change driven by your identity provider, and on Origin events `App: <id>` or `Service Account: <id>` is an installed app or service account acting on its own. When no actor was identified, Grok Bot events show `System` and other events show `unknown`. Changes Cursor Support makes on your behalf appear as `hi@cursor.com` or `Cursor`. |
| `event_type`       | One of the values in [Event types](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#event-types).                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `application_type` | `grok_bot` for Grok Bot; `cursor` for Cursor desktop, iOS, CLI, the Agent SDK, cursor.com, and the Admin API. Empty when the application can't be determined and on rows written before the field existed.                                                                                                                                                                                                                                                                                                                                  |
| `event_data`       | Event-specific fields. `old_value` and `new_value` come back as parsed JSON when the stored value is JSON, otherwise as a string.                                                                                                                                                                                                                                                                                                                                                                                                           |

Streamed events use the raw message shape. The envelope fields are the same, the event id and timestamp sit under `metadata.id` and `metadata.timestamp`, and the event-specific fields sit under a key named after the event type. Streamed messages also carry `metadata.context` (`request_id`, the actor's `auth_id`, and the `ghost_mode` and `privacy_mode` flags in effect) and `customer_actor_display`, which is `Cursor Support` when Cursor Support acted for you, `<email> (performed via App: <id>)` or `<email> (performed via Service Account: <id>)` when a member acted through an app installation or service account on Origin, and empty otherwise:

```json
{
  "metadata": { "id": "8a1f0f0e-0d1b-4c7e-9b3a-2f6e1c9d4a55", "timestamp": "2026-09-14T18:30:45.123Z" },
  "team_id": "12345",
  "org_id": "678",
  "ip_address": "203.0.113.42",
  "user_email": "alice@company.com",
  "application_type": "cursor",
  "add_user": { "user_email": "bob@company.com", "role": "member", "source": "invite" }
}
```

Audit logs don't include OpenTelemetry trace or span ids. To group recorded Grok Bot actions by Bot or turn, use [OpenTelemetry Export](https://cursor.com/docs/enterprise/opentelemetry-export.md#joining-sessions).

### Event types

Field names are keys in Admin API `event_data` and in the equivalent CSV or streamed payload. Values in parentheses are the possible `action` values or enumerations.

#### Authentication and membership

| `event_type`          | When it fires                                                                    | Fields                                                                                                                                                                                                  |
| --------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `login`               | A member signs in                                                                | `success`, `login_type` (`LOGIN_TYPE_WEB`). Use `application_type` to tell the surface apart                                                                                                            |
| `logout`              | A member signs out or revokes their session                                      | none                                                                                                                                                                                                    |
| `add_user`            | A member joins the team                                                          | `user_email`, `role`, `source` (how the member joined), `team_id`, `invited_by_email`, `invited_by_user_id`, `invite_id`                                                                                |
| `remove_user`         | A member is removed                                                              | `user_email`                                                                                                                                                                                            |
| `credentials_revoked` | Emitted with `remove_user`; records what happened to the removed member's access | `user_email`, `sessions` (`revoked`, `retained`, `revoke_failed`), `repo_grants` (`cleared`, `retained`), `cloud_agent_git_tokens` (`denied_on_next_use`, `retained`), `personal_api_keys` (`retained`) |
| `update_user_role`    | A member's role changes                                                          | `old_role`, `new_role` (`OWNER`, `MEMBER`, `FREE_OWNER`; lowercase when Cursor Support made the change), `user_email`                                                                                   |
| `invite_link`         | An admin creates or revokes an invite link                                       | `action` (`create`, `revoke`), `role`, `expires_in_seconds`, `invite_id`, `creator_email`                                                                                                               |
| `invite_email_sent`   | An invite email is sent                                                          | `recipient_email`, `role`, `invite_id`, `sender_email`                                                                                                                                                  |
| `privacy_mode`        | Privacy Mode changes for a member or the team                                    | `old_privacy_mode`, `new_privacy_mode`, `scope` (`user`, `team`)                                                                                                                                        |
| `user_spend_limit`    | A member's spending limit changes                                                | `target_user_email`, `old_limit_cents`, `new_limit_cents`                                                                                                                                               |

`credentials_revoked` with `sessions: retained` or `repo_grants: retained` means the member still belongs to another team in your organization, so their sessions and repository grants stay valid.

#### API keys and service accounts

| `event_type`            | When it fires                                                                                                                                   | Fields                                                                                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `team_api_key`          | A team API key is created or revoked                                                                                                            | `action` (`create`, `revoke`)                                                                                                                      |
| `user_api_key`          | A user API key is created or revoked                                                                                                            | `action` (`create`, `revoke`)                                                                                                                      |
| `organization_api_key`  | An organization API key is created or revoked                                                                                                   | `action` (`create`, `revoke`), `organization_id`, `api_key_id`, `api_key_name`                                                                     |
| `service_account`       | A service account is created, archived, or gets a spend limit                                                                                   | `action` (`create`, `archive`, `set_spend_limit`), `service_account_id`, `service_account_name`, `old_spend_limit_cents`, `new_spend_limit_cents`  |
| `api_key`               | A service account key is created, rotated, or rescoped                                                                                          | `action` (`create`, `rotate`, `update_repo_scope`), `service_account_id`, `service_account_name`, `api_key_id`, `repo_scope`, `repo_scope_enabled` |
| `cloud_agent_sub_token` | A service account key mints a delegated token for a member through `POST /v1/sub-tokens`. `user_email` is the key; the member is in the payload | `subject_user_email`, `service_account_id`, `api_key_id`, `ttl_seconds`                                                                            |

#### Team settings and integrations

| `event_type`                | When it fires                                                                                                                | Fields                                                                                                                                                                                                  |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `team_settings`             | A team-wide setting changes, including changes made through the Admin API                                                    | `setting_name`, `old_value`, `new_value`                                                                                                                                                                |
| `team_rule`                 | A team rule is created, updated, or deleted                                                                                  | `action` (`create`, `update`, `delete`), `rule_id`, `rule_name`, `is_active`, `is_required`                                                                                                             |
| `team_command`              | A custom command is created, updated, or deleted                                                                             | `action` (`create`, `update`, `delete`), `command_id`, `command_name`, `is_active`                                                                                                                      |
| `team_hook`                 | A team hook is created, updated, or deleted. The payload includes the hook's script or prompt text                           | `action` (`create`, `update`, `delete`), `hook_id`, `hook_step`, `hook_type` (`command`, `prompt`), `script_name`, `operating_systems`, `is_active`, `script_content`, `prompt_content`, `prompt_model` |
| `mcp_server_config`         | A user or team MCP server is configured                                                                                      | `action` (`create`, `update`, `rename`, `delete`), `server_name`, `server_type` (`HTTP`, `STDIO`), `scope` (`user`, `team`)                                                                             |
| `mcp_authentication`        | A member authenticates to, disconnects from, or removes an account for an MCP server. An empty `action` means `authenticate` | `server_name`, `scope` (`user`, `service_account`), `service_account_id`, `action` (`authenticate`, `revoke`, `remove_account`)                                                                         |
| `slack_account_link`        | A member links or relinks their Slack account                                                                                | `action` (`link`, `relink`), `slack_team_id`, `slack_user_id`, `workspace_changed`                                                                                                                      |
| `team_marketplace`          | An admin creates, updates, or deletes a plugin marketplace, or adds, removes, pins, links, or reconfigures its plugins       | `action`, `marketplace_id`, `marketplace_name`, `plugin_id`, `plugin_name`, plus before and after values for the changed install mode, access groups, or source repository                              |
| `team_data_export_download` | An admin requests a download link for a team data export. The request is recorded, not the download                          | `task_handle`, `url_ttl_seconds`                                                                                                                                                                        |

`setting_name` on `team_settings` names the setting. Common names, not an exhaustive list, include spending limits (`team_hard_limit_dollars`, `team_hard_limit_per_user_dollars`, `per_user_monthly_limit_dollars`, `admin_only_usage_pricing`), `team_admin_settings`, `team_name`, `default_member_billing_tier`, access controls (`scim_require_user_directory`, `domain_join`, `require_private_workers`, `dashboard_analytics_requires_admin`, `mcp_allowlist_import`, `no_zdr_model_consent`), Origin (`origin_disabled`, `origin_allow_public_repos`), and Slack defaults (`slack_default_repo`, `slack_default_branch`, `slack_default_model`, `slack_share_summary`, `slack_share_summary_in_external_channel`). SSO and organization-level domain join changes are `organization_identity_provider` events.

#### Directory groups and organizations

| `event_type`                         | When it fires                                                                      | Fields                                                                                                                                                                                                                                                                    |
| ------------------------------------ | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `create_directory_group`             | A directory group is created                                                       | `directory_group_id`, `metadata`                                                                                                                                                                                                                                          |
| `update_directory_group`             | A directory group is renamed or updated                                            | `directory_group_id`, `old_value`, `new_value`                                                                                                                                                                                                                            |
| `update_directory_group_permissions` | A directory group's permissions change                                             | `directory_group_id`, `directory_group_name`, `old_value`, `new_value`                                                                                                                                                                                                    |
| `delete_directory_group`             | A directory group is deleted                                                       | `directory_group_id`                                                                                                                                                                                                                                                      |
| `add_user_to_directory_group`        | A member is added to a directory group, including by SCIM                          | `directory_group_id`, `user_email`                                                                                                                                                                                                                                        |
| `remove_user_from_directory_group`   | A member is removed from a directory group, including by SCIM                      | `directory_group_id`, `user_email`                                                                                                                                                                                                                                        |
| `organization_group`                 | An organization group is created or deleted                                        | `action` (`create`, `delete`), `organization_group_id`, `organization_group_name`                                                                                                                                                                                         |
| `organization_group_settings`        | An organization group's name, visibility, spending limit, or admin settings change | `organization_group_id`, `organization_group_name`, `setting_name`, `old_value`, `new_value`                                                                                                                                                                              |
| `organization_identity_provider`     | SSO or domain join is turned on or off, or a domain is added or removed            | `action` (`update_sso_settings`, `set_allow_domain_join`, `add_domain_join`, `remove_domain_join`), `organization_id`, `identity_provider_public_id`, `setting_name` (`allow_sso`, `allow_domain_join`; empty for per-domain changes), `old_value`, `new_value`, `domain` |
| `organization_team_settings_copy`    | Selected settings are copied into a newly created organization team                | `source_team_id`, `target_team_id`, `categories`, `outcomes`                                                                                                                                                                                                              |
| `xai_team_link`                      | An xAI team link is confirmed                                                      | `action` (`confirm`), `organization_id`, `xai_team_id`                                                                                                                                                                                                                    |
| `xai_credit_transfer`                | An xAI credit transfer completes                                                   | `action` (`complete`), `transfer_id`, `organization_id`, `xai_team_id`, `amount_cents`                                                                                                                                                                                    |

`organization_group`, `organization_group_settings`, `organization_team_settings_copy`, `xai_team_link`, and `xai_credit_transfer` are organization-level events. They have an empty `team_id` and appear in the organization feed, not in a team's feed.

#### Telemetry export and LLM Gateway

| `event_type`                        | When it fires                                                                                       | Fields                                                                                                                                                                                                                                                                     |
| ----------------------------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `customer_telemetry_destination`    | An OpenTelemetry export destination is created, updated, or deleted. Header values are never logged | `action` (`create`, `update`, `delete`), `destination_id`, `endpoint_url`, `enabled`, `metrics_enabled`, `logs_enabled`, `credentials_changed`, `enabled_families`, `disabled_families`, `content_prompts_enabled`, `content_responses_enabled`, `content_tool_io_enabled` |
| `customer_telemetry_content_opt_in` | The team turns conversation-content export on or off                                                | `enabled`                                                                                                                                                                                                                                                                  |
| `llm_gateway_settings`              | LLM Gateway settings or credentials change. Credential values and endpoint URLs are never logged    | `action` (`update`, `credential_create`, `credential_replace`, `credential_clear`), `changed_settings`, `enabled`, `audience`, `auth_mode`, `endpoint_families`, `credentials_changed`                                                                                     |

#### Bugbot

| `event_type`                   | When it fires                                                  | Fields                                                                                                               |
| ------------------------------ | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `bugbot_installation`          | A GitHub installation is connected or disconnected             | `action` (`connect`, `disconnect`), `installation_id`, `github_app_type` (`dotcom`, `enterprise`), `github_hostname` |
| `bugbot_installation_settings` | An installation-level setting changes                          | `installation_id`, `setting_name`, `old_value`, `new_value`                                                          |
| `bugbot_repo_settings`         | A repository-level setting changes                             | `repo_url`, `repo_node_id`, `setting_name`, `old_value`, `new_value`                                                 |
| `bugbot_team_settings`         | A Bugbot team setting changes                                  | `setting_name`, `old_value`, `new_value`                                                                             |
| `bugbot_team_rule`             | A Bugbot rule is created, updated, or deleted                  | `action` (`create`, `update`, `delete`), `rule_id`, `rule_name`, `is_active`, `is_required`                          |
| `bugbot_bulk_repo_update`      | Bugbot is enabled or disabled across many repositories at once | `installation_id`, `repos_updated`, `bugbot_enabled`                                                                 |

#### Cloud Agents

| `event_type`                        | When it fires                                                                    | Fields                                                                                                                                                     |
| ----------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cloud_agent_secret`                | A user or team secret is created, updated, or deleted                            | `action` (`create`, `update`, `delete`), `secret_name`, `scope` (`user`, `team`), `scoped_to_repos`                                                        |
| `cloud_agent_secret_read`           | A Cloud Agent run or environment build loads an environment's secrets            | `environment_id`, `secret_count`                                                                                                                           |
| `cloud_agent_user_settings`         | A member's Cloud Agent settings change                                           | `setting_name`, `old_value`, `new_value`, `source` (`ide`, `dashboard`, `slack`)                                                                           |
| `cloud_agent_environment_settings`  | An environment's network egress allowlist or mode changes                        | `environment_id`, `old_allowlist`, `new_allowlist`, `old_egress_mode`, `new_egress_mode`, `source` (`dashboard`, `agent`)                                  |
| `cloud_agent_environment_lifecycle` | An environment is created, updated, or deleted                                   | `environment_id`, `action` (`created`, `updated`, `deleted`), `source` (`dashboard`, `agent`), `repo_url`, `environment_name`, `snapshot_promoted_to_team` |
| `protected_git_scope`               | A protected Git scope is created or deleted. `git_org_owner` is hashed           | `action` (`create`, `delete`), `scope_id`, `git_org_owner`, `git_provider`, `user_id`                                                                      |
| `protected_git_scope_access_check`  | A member's access to a protected Git scope is allowed. `git_org_owner` is hashed | `git_org_owner`, `git_provider`, `result` (`allowed`), `reason`, `user_id`                                                                                 |

#### Grok Bot

Grok Bot payloads carry identifiers and changed field names, never content such as instructions, template bodies, Group Rule or Setup Script text, MCP URLs, or credentials.

| `event_type`                   | When it fires                                                                                                                                          | Fields                                                                                                                                                                                                                                              |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sand_onboarding`              | Grok Bot is enabled or disabled for the team. `new_completed=true` means enabled                                                                       | `old_completed`, `new_completed`, `source`                                                                                                                                                                                                          |
| `grok_bot_created`             | A Bot is created                                                                                                                                       | `agent_id`, `name`, `source` (`direct`, `template`, `agent_sdk`, `system`), `template_id`                                                                                                                                                           |
| `grok_bot_lifecycle`           | A Bot's profile, visibility, or primary status changes, it is published to or unpublished from the team, or it is deleted                              | `agent_id`, `action` (`update`, `rename`, `delete`, `visibility_changed`, `primary_bot_changed`, `published`, `unpublished`), `changed_fields`, `primary_bot_cleared`, `old_visibility`, `new_visibility` (`OWNER`, `TEAM`), `previous_agent_id`    |
| `grok_bot_access_changed`      | Member access to Grok Bot changes. Group lists are the post-change allowlist; empty when mode is `all`                                                 | `old_mode`, `new_mode` (`all`, `limited`), `old_group_ids`, `new_group_ids`, `old_group_names`, `new_group_names`                                                                                                                                   |
| `grok_bot_team_setup_manifest` | A Team Setup manifest is saved or deleted                                                                                                              | `action` (`save`, `delete`), `manifest_id`, `revision`, `entry_count`, `entry_ids`                                                                                                                                                                  |
| `grok_bot_group_settings`      | A group-owned Grok Bot setting changes                                                                                                                 | `group_id`, `group_name`, `setting_name`, `old_value`, `new_value`                                                                                                                                                                                  |
| `grok_bot_group_resource`      | A Group Rule is created, updated, or deleted, or a Group Setup Script is saved or deleted                                                              | `group_id`, `group_name`, `resource` (`rule`, `setup_manifest`), `action` (`create`, `update`, `delete`, `save`), `resource_id`, `resource_name`                                                                                                    |
| `grok_bot_resource`            | A Bot template or room is created, published, deleted, or changes visibility or membership                                                             | `resource_type` (`room`, `template`), `resource_id`, `action` (`create`, `delete`, `membership_changed`, `publish`, `visibility_changed`), `visibility` (`TEAM`, `PUBLIC`), `previous_visibility`                                                   |
| `grok_bot_skill`               | A skill is added to, updated on, or removed from a team Bot                                                                                            | `action` (`add`, `update`, `remove`), `agent_id`, `skill_slug`                                                                                                                                                                                      |
| `grok_bot_machine`             | A local computer is registered or renamed                                                                                                              | `action` (`register`, `rename`), `machine_id`                                                                                                                                                                                                       |
| `grok_bot_vm`                  | A Grok Bot Computer is reset, recreated, upgraded, or killed. `target_user_*` name the member whose computer an admin acted on; empty for self-service | `action` (`image_update_completed`, `reset`, `force_recreate`, `upgrade_scheduled`, `upgrade_rescheduled`, `upgrade_cancelled`, `upgrade_completed`, `kill`), `operation_id`, `schedule_id`, `target_user_id`, `target_user_email`, `deleted_count` |
| `grok_bot_vm_bulk`             | A bulk computer operation completes. Its child operations emit no rows                                                                                 | `action` (`bulk_recreate`, `bulk_kill`, `bulk_permanent_delete`), `operation_id`, `target_count`, `succeeded_count`, `skipped_count`, `failed_count`                                                                                                |
| `grok_bot_routine`             | A routine is created, updated, enabled, disabled, or deleted                                                                                           | `action` (`create`, `update`, `enable`, `disable`, `delete`), `automation_id`, `name`, `sand_agent_id`, `trigger_type`, `creation_source`, `enabled`                                                                                                |

#### Origin

Origin events go to the team that owns the namespace or repository. Payloads carry identifiers, names, refs, and commit SHAs, never file contents or comment bodies. Every row includes `repo_namespace` and `repo_name` (or `namespace_slug` for namespace events).

| `event_type`                                                                                                                                                                                            | When it fires                                                                                                                                                   | Fields                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `origin_repository_created`, `origin_new_repository_synced`                                                                                                                                             | A repository is created on Origin, natively or by syncing from GitHub                                                                                           | `repo_uuid`, `repo_kind`, `mirror_status` (empty for native repositories)                                                                                                                                               |
| `origin_repository_pushed`                                                                                                                                                                              | Refs are pushed                                                                                                                                                 | `repo_uuid`, `ref_update_count`, `ref_updates` (each with `ref`, `before`, `after`, `forced`)                                                                                                                           |
| `origin_repository_pulled`                                                                                                                                                                              | A member clones or fetches a repository. Background autofetches and app or service-account pulls are not recorded                                               | `repo_uuid`, `transport` (`http`, `ssh`)                                                                                                                                                                                |
| `origin_repository_metadata_updated`                                                                                                                                                                    | The default branch changes                                                                                                                                      | `repo_id`, `default_branch`                                                                                                                                                                                             |
| `origin_repo_access_changed`                                                                                                                                                                            | A repository access grant is set or cleared                                                                                                                     | `repo_uuid`, `principal_kind` (`user`, `group`, `team_admins`, `team_members`), `principal_id`, `principal_display`, `operation` (`set`, `clear`), `policy_name`, `group_scope` (`org`, `team`)                         |
| `origin_change_created`, `origin_change_published`, `origin_change_head_ref_pushed`, `origin_change_base_ref_updated`, `origin_change_metadata_updated`, `origin_change_closed`, `origin_change_merged` | A change (pull request) is created, published, pushed to, retargeted, edited, closed, or merged                                                                 | `repo_uuid`, `change_id`, `change_number`, `change_title`, `change_status`, `head_ref`, `base_ref`, `version_number`, `head_sha`; `merge_commit_sha` on merge                                                           |
| `origin_change_approved`                                                                                                                                                                                | A review approves a change                                                                                                                                      | `repo_uuid`, `change_id`, `change_number`, `review_id`, `version_number`, `author_id`, `author_kind`, `verdict`                                                                                                         |
| `origin_comment_created`, `origin_comment_updated`, `origin_comment_deleted`, `origin_comment_thread_resolved`, `origin_comment_thread_reopened`                                                        | A review comment is written, edited, or deleted, or its thread is resolved or reopened                                                                          | `repo_uuid`, `change_id`, `change_number`, `thread_id`, `comment_id`                                                                                                                                                    |
| `origin_check_run_rerequested`                                                                                                                                                                          | Someone asks an app to run a check again                                                                                                                        | `repo_uuid`, `check_run_id`, `check_run_name`, `head_sha`                                                                                                                                                               |
| `origin_namespace_created`                                                                                                                                                                              | A namespace is created                                                                                                                                          | `namespace_slug`                                                                                                                                                                                                        |
| `origin_namespace_access_changed`                                                                                                                                                                       | A namespace access grant is set or cleared, one row per grant                                                                                                   | `namespace_slug`, `grant_id`, `principal_kind` (`user`, `group`, `team_admins`, `team_members`, `installation`, `app`), `principal_id`, `principal_display`, `operation` (`set`, `clear`), `policy_name`, `group_scope` |
| `origin_namespace_ssh_certificate_authority_added`, `origin_namespace_ssh_certificate_authority_removed`                                                                                                | An SSH certificate authority is added to or removed from a namespace                                                                                            | `namespace_slug`, `certificate_authority_id`, `certificate_authority_name`, `algo`, `fingerprint`                                                                                                                       |
| `origin_namespace_ssh_certificate_requirement_changed`                                                                                                                                                  | The namespace starts or stops requiring SSH certificates                                                                                                        | `namespace_slug`, `require_certificates`                                                                                                                                                                                |
| `origin_installation_created`, `origin_installation_updated`, `origin_installation_suspended`, `origin_installation_unsuspended`, `origin_installation_deleted`                                         | An app installation on a namespace is created, is updated (repository selection, re-consent, or a namespace rename), is suspended or unsuspended, or is removed | `namespace_slug`, `installation_id`, `app_id`, `app_display_name`, `app_owner_namespace`, `repo_selection_mode`, `selected_repo_count`                                                                                  |

### Accessing audit logs

View audit logs in the [team dashboard](https://cursor.com/dashboard/audit-log). This requires an Enterprise plan and admin access. Filter by date range, event type, actor, or application, then export the filtered result to CSV. The export includes an Application column.

Pull audit logs programmatically with the Admin API:

- [`GET /teams/audit-logs`](https://cursor.com/docs/account/teams/admin-api.md#get-audit-logs) with a Team API key returns one team's events.
- [`GET /organizations/audit-logs`](https://cursor.com/docs/account/organizations/organization-admin-api.md#get-audit-logs) with an Organization API key (`auditlogs:read` or `admin:*` scope) returns events for every linked team plus organization-level events, or one team when you pass `teamId`.

Both endpoints default to the last 7 days, accept up to a 30-day window and 500 events per page, filter by `eventTypes` and `users`, and return events oldest first. Page through longer periods with consecutive windows.

### Streaming audit logs

Cursor can stream your team's or organization's audit events to a Splunk HTTP Event Collector, Sumo Logic, an HTTPS webhook (including Cribl, SentinelOne, Rapid7, Cortex XDR, and Google Chronicle endpoints), or an S3 bucket. Every destination receives events in the raw message shape shown in [Log format](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#log-format), including `application_type`, with batch framing suited to the destination (gzipped JSON Lines files on S3, HEC events for Splunk, newline-delimited JSON for webhooks, a JSON array per batch for Rapid7, and Cribl deliveries without `team_hook` script and prompt text when the acting member had Privacy Mode on). Contact [hi@cursor.com](mailto:hi@cursor.com) to set up streaming.

### Privacy Mode

Privacy Mode doesn't suppress audit events. Administrative actions are recorded whether or not the acting member has Privacy Mode on, and payloads carry identifiers and setting values, never prompts, agent output, or generated code. The one payload with free text is `team_hook`, which includes the hook's script or prompt.

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
