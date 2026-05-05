---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/workspaces.md
source_url: https://platform.claude.com/docs/en/build-with-claude/workspaces
title: "Workspaces"
summarized_at: 2026-05-05
entities_referenced: [Workspace, Admin-API, API-key, Files-API, Batches-API, Skill-API, Prompt-caching, Rate-limit-API, Usage-report, Cost-report]
concepts_referenced: []
---

Workspaces partition API usage within an organization for separating projects, environments, or teams while keeping centralized billing/admin. Every org has a **Default Workspace** (cannot rename/archive/delete; no ID; doesn't appear in list endpoints).

## Key characteristics

- IDs prefixed `wrkspc_` (e.g., `wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ`).
- **Maximum 100 workspaces per org** (archived ones don't count).
- Default Workspace usage shows `null` for `workspace_id` in API responses.
- API keys are scoped to a single workspace and can only access resources within it.

## Workspace roles

| Role | Permissions |
|---|---|
| Workspace User | Workbench only |
| Workspace Limited Developer | Create/manage API keys, use API. **Cannot access session traces or download files.** |
| Workspace Developer | Create/manage API keys, use API |
| Workspace Admin | Full control of workspace settings + members |
| Workspace Billing | View workspace billing (inherited from org billing role; cannot be manually assigned) |

### Role inheritance

- Org admins → auto Workspace Admin in all workspaces.
- Org billing members → auto Workspace Billing in all workspaces.
- Org users / developers → must be **explicitly added** to each workspace.

Org admins/billing cannot be removed from workspaces while they hold those org roles.

## Resources scoped per workspace

- Files (Files API)
- Message Batches (Batch API)
- Skills (Skills API)
- **Prompt caches** — starting **February 5, 2026**, prompt caches will be isolated per workspace (Claude API and Azure only).

## Workspace limits

- **Spend limits:** monthly cap.
- **Rate limits:** RPM, input TPM, output TPM per model tier.
- Cannot be set on Default Workspace.
- If unset: workspace inherits org-level limits.
- Org-wide limits always apply, even if workspace limits sum to more.

## Admin API endpoints

- `POST /v1/organizations/workspaces` — create
- `GET /v1/organizations/workspaces?limit=&include_archived=` — list
- `POST /v1/organizations/workspaces/{workspace_id}/archive` — archive (immediately revokes all keys; **not undoable**)
- Member CRUD: `POST/DELETE /v1/organizations/workspaces/{workspace_id}/members[/{user_id}]` with `workspace_role` body field.

## Console actions

Created via Console at Settings → Workspaces. Edit name/color via ellipsis menu. Add members via Members tab. Limits in Limits tab.

## Common use cases

- Environment separation: Dev / Staging / Prod.
- Team or department isolation (Engineering / Data Science / Support).
- Project-based organization for usage tracking + cost allocation.
