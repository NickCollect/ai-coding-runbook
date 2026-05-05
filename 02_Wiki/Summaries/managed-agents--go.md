---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/go/managed-agents/README.md
title: "Managed Agents — Go"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Go SDK patterns for Anthropic Managed Agents (Beta). Install: `go get github.com/anthropics/anthropic-sdk-go`.

**Persistence model**: agents are persistent — create once via `client.Beta.Agents.New`, store `agent.ID`, reference in every `client.Beta.Sessions.New`. Create-call belongs in setup, not request path. Agent objects are immutable per version; updates via `Beta.Agents.Update` create new versions. List versions via `Beta.Agents.Versions.ListAutoPaging`. Archive via `Beta.Agents.Archive`.

**Required setup steps**: create environment (`Beta.Environments.New` with networking config — `UnrestrictedNetworkParam`) → create agent (with `Model`, `System` prompt, `Tools` like `BetaManagedAgentsAgentToolset20260401Params`) → start session (`Beta.Sessions.New` with `Agent` union — string ID or typed `BetaManagedAgentsAgentParams` with version pin — and `EnvironmentID`).

**Send user message**: `client.Beta.Sessions.Events.Send` with `BetaManagedAgentsUserMessageEventParams` containing text content union.

**Stream events (SSE)**: `client.Beta.Sessions.Events.StreamEvents` returns iterator. **Stream-first pattern**: open stream BEFORE (or concurrently with) sending message — stream only delivers events occurring after open; stream-after-send means buffered batch arrives.

Event union types: `BetaManagedAgentsAgentMessageEvent`, `BetaManagedAgentsAgentToolUseEvent`, `BetaManagedAgentsSessionStatusIdleEvent`, `BetaManagedAgentsSessionErrorEvent`. Switch on `stream.Current().AsAny()`.

**Reconnect/tail**: open stream first (buffers), then list past events via `ListAutoPaging` to dedupe by event ID, then process new events skipping seen IDs.

**Poll events**: `client.Beta.Sessions.Events.ListAutoPaging` for non-streaming.

**Files**: `client.Beta.Files.Upload(ctx, BetaFileUploadParams{File: file})`. Mount in session via `Resources` array with `BetaManagedAgentsFileResourceParams{FileID, MountPath}`. Add/list/delete on existing session via `Beta.Sessions.Resources.Add/List/Delete`.

**Session management**: `Beta.Environments.List/Get/Archive/Delete`, `Beta.Sessions.Delete`. Archive vs delete: archive read-only (existing sessions continue); delete only if no sessions reference it.

**MCP server integration**: agent declares MCP server via `MCPServers: []BetaManagedAgentsUrlmcpServerParams{...}` (URL only, no auth). Session attaches vault(s) holding credentials via `VaultIDs`. Tools include `OfMCPToolset` with `MCPServerName` matching.

**Vaults**: `Beta.Vaults.New` with `DisplayName` + `Metadata`. Add credentials via `Beta.Vaults.Credentials.New` (e.g. `BetaManagedAgentsMCPOAuthCreateParams` with `MCPServerURL`, `AccessToken`, `ExpiresAt`, refresh config including `TokenEndpoint`/`ClientID`/`Scope`/`RefreshToken`/`TokenEndpointAuth`). Rotate via `Beta.Vaults.Credentials.Update`. Archive via `Beta.Vaults.Archive`.

**GitHub repo as resource**: `BetaManagedAgentsGitHubRepositoryResourceParams{URL, MountPath, AuthorizationToken}`. Multiple repos in same session OK. Rotate token via `Beta.Sessions.Resources.Update`.

Notes from README: `user.custom_tool_result` Go bindings not yet documented — refer to `shared/managed-agents-events.md` and SDK repo. Listing/downloading session-written files also not yet documented for Go.
