---
type: summary
source: 01_Raw/code.claude.com/docs/en/zero-data-retention.md
source_url: https://code.claude.com/docs/en/zero-data-retention
title: "Zero data retention"
summarized_at: 2026-05-05
entities_referenced: [Settings]
concepts_referenced: []
---

Zero Data Retention (ZDR) for Claude Code on Claude for Enterprise. When enabled, prompts + model responses processed in real-time and not stored by Anthropic after response, except for legal compliance / abuse handling.

ZDR organizations get admin features: per-user cost controls, Analytics dashboard, server-managed settings, audit logs.

**Scope**: covers Anthropic's direct platform only — NOT Bedrock/Vertex/Foundry (those follow their respective vendor policies). **Per-organization** opt-in: each new org needs separate enablement, not auto-inherited.

**ZDR covers**: model inference calls through Claude Code on Claude for Enterprise — all prompts and responses, regardless of model.

**ZDR does NOT cover**:
| Feature | Notes |
|---|---|
| Chat on claude.ai | Web interface chats not covered |
| Cowork | Not covered |
| Claude Code Analytics | Doesn't store prompts/responses but collects metadata (emails, usage stats). Contribution metrics unavailable for ZDR orgs |
| User/seat management | Standard policy retention |
| Third-party integrations | MCP servers etc. follow their own policies |

**Features auto-disabled under ZDR** (require persistent storage):
- Claude Code on the Web — server-side conversation history.
- Remote sessions from Desktop.
- Feedback submission (`/feedback`) — sends conversation to Anthropic.

These are enforced backend-side regardless of client display — attempt → error.

**Policy violation exception**: even with ZDR, Anthropic may retain inputs/outputs for up to 2 years if flagged for Usage Policy violation or required by law.

**Request ZDR**: contact sales / Anthropic account team. All enablement actions audit-logged. Existing pay-as-you-go API key ZDR users can transition to Claude for Enterprise to gain admin features while keeping ZDR.
