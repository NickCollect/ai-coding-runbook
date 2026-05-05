---
type: summary
source: 01_Raw/code.claude.com/docs/en/legal-and-compliance.md
source_url: https://code.claude.com/docs/en/legal-and-compliance
title: "Legal and compliance"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Enterprise-gateway]
concepts_referenced: []
---

Short reference page covering legal terms, compliance posture, and authentication-policy distinctions for Claude Code.

**Legal**:
- **Commercial Terms** apply for Team, Enterprise, and Claude API users.
- **Consumer Terms of Service** apply for Free, Pro, and Max users.
- Existing commercial agreements (1P direct API, or 3P via Bedrock/Vertex) automatically extend to Claude Code use unless mutually agreed otherwise.

**Healthcare BAA**: a Business Associate Agreement automatically extends to Claude Code IF the customer has executed a BAA AND has Zero Data Retention (ZDR) activated. ZDR is per-organization — each must enable separately. BAA only covers that org's API traffic flowing through Claude Code.

**Acceptable use**: subject to the Anthropic Usage Policy. Pro and Max usage limits assume **ordinary, individual** use of Claude Code and the Agent SDK.

**Authentication policy** (important compliance distinction):
- **OAuth tokens** are *exclusively* for purchasers of Free/Pro/Max/Team/Enterprise subscription plans, intended for ordinary use of Claude Code and other native Anthropic apps.
- **Developers** building products/services that interact with Claude (including Agent SDK consumers) must use **API key authentication** via Claude Console or a supported cloud provider.
- Anthropic does NOT permit third-party developers to offer Claude.ai login or to route requests through Free/Pro/Max plan credentials on users' behalf. Anthropic reserves the right to enforce without prior notice.

**Security**: vulnerabilities reported via HackerOne (link in raw). Trust posture at Anthropic Trust Center / Transparency Hub.
