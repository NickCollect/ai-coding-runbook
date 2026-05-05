---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/2133-extensions.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/2133-extensions.md
title: "SEP-2133: MCP Extensions framework"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-01-21 | Author: Peter Alexander (@pja-ant)**

Establishes the lightweight framework for **extending MCP via optional, composable extensions**. Defines governance for both Official Extensions (maintained by MCP) and Experimental Extensions (incubation pathway for WGs/IGs).

**Definition**: an MCP extension is an optional addition defining capabilities beyond core. Identified by `{vendor-prefix}/{extension-name}` (e.g., `io.modelcontextprotocol/oauth-client-credentials`, `com.example/websocket-transport`). Vendor prefix follows reverse-DNS (Java-package style); breaking changes require a NEW identifier (e.g., `...-v2`).

**Three extension classes**:

1. **Official Extensions** — live in `modelcontextprotocol/ext-*` GitHub repos (e.g., `ext-auth`, `ext-apps`); use `io.modelcontextprotocol` prefix; repository maintainers appointed by core maintainers; SHOULD have an associated WG or IG. Created via Extensions Track SEP (new SEP type).
2. **Experimental Extensions** — `modelcontextprotocol/experimental-ext-*` repos; incubation pathway for WGs/IGs to prototype before formal SEP submission; MUST be associated with a WG or IG; MUST clearly indicate experimental status; published packages MUST use names indicating experimental status.
3. **Unofficial Extensions** — outside MCP org; not recognized by MCP governance.

**Lifecycle**: optionally start as experimental → graduate via Extensions Track SEP (must have ≥1 reference implementation in an official SDK) → MAY eventually graduate to core protocol.

**SDK implementation**: extensions MUST be disabled by default; opt-in only. SDK maintainers have full autonomy over which extensions to support; no obligation; not required for protocol conformance.

**Capability negotiation**: clients/servers advertise via new `extensions` field in `ClientCapabilities` / `ServerCapabilities` (and the upcoming Server Card). Map of extension identifiers → per-extension settings objects. Servers SHOULD check client capabilities before offering extension features. Graceful degradation required (text-only fallback for UI-enabled tools, etc.).

**Legal**: trademark policy (use of MCP marks doesn't imply endorsement); antitrust acknowledgment; Apache 2.0 licensing for official extensions; CLA-style contributor grant.

**Not specified** in this SEP (deferred): mechanism for extensions to advertise schema changes, dependency model between extensions and core protocol versions or other extensions, profiles/grouping.

**Rationale**: start simple, clear governance, refine later. Why repositories instead of standalone extensions: provides natural group/governance structure; avoids incompatible extensions in the same area. Why no core-maintainer review for ongoing changes: avoids bottlenecking on already-slow CM review; iteration stays autonomous.
