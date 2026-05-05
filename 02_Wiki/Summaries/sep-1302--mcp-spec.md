---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1302-formalize-working-groups-and-interest-groups-in-mc.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1302-formalize-working-groups-and-interest-groups-in-mc.md
title: "SEP-1302: Formalize Working Groups and Interest Groups"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-08-05 | Author: tadasant**

Formally defines **Working Groups (WGs)** and **Interest Groups (IGs)** introduced by SEP-994. Inspired by W3C's WG/IG distinction.

**Interest Groups (problems-focused)**: facilitate discussion and knowledge-sharing about a topic. Goal is collecting problems that may or may not warrant solving. Examples: Security in MCP, Auth in MCP, Enterprise MCP, Hosting, Client Implementors. Expectations: ≥1 substantive thread/conversation per month and/or live meeting attended by 3+ unaffiliated individuals. Successful IGs live in perpetuity.

**Working Groups (solutions-focused)**: facilitate community collaboration on a specific SEP, themed series of SEPs, or officially endorsed Project. Examples: Registry, Inspector, Tool Filtering, Server Identity. Expectations: monthly progress on a SEP / spec-related implementation OR maintenance responsibilities for a Project. WGs retired when no WIP Issue/PR for ≥1 month or all planned items complete.

**Lifecycle for both**: created via template in `#wg-ig-group-creation` Discord; community moderator calls a 72-hour vote in private moderator channel; majority approves; core+ maintainers can veto. Facilitators (informal, self-nominated) shepherd discussions; Maintainers (optional, MCP steering rep) provide official representation.

**Migration path** spelled out for all existing CWG/Steering groups (e.g., SDK groups → Working Groups; Auth → Interest Group + sub-WGs; Connection Lifetime/Streaming → Retire; UI → Interest Group; etc.).

**Design principles**: clear on-ramp for community (1) join Discord, (2) facilitate calls, (3) join WG work, (4) get nominated as maintainer; minimal changes to existing governance (no new elections, leverages community moderators); alignment with current status quo (lightweight migration); separates WG and IG motivations explicitly; centralized creation point prevents fragmentation; explicit retirement path.

Subsequently superseded in operational detail by SEP-2149 (Group Governance and Charter Template) but the conceptual distinction remains.
