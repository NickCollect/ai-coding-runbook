---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/java/managed-agents/README.md
title: "Managed Agents — Java SDK"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Managed Agents flows for the `anthropic-java` SDK. Caveat at top: bindings shown here are not exhaustive — for any class/method/field/behavior not shown, WebFetch the Java SDK repo or the Anthropic docs page rather than guess.

**Persistent agent rule**: agents are immutable per version, persistent across sessions. Create once, store the agent ID, reuse for every `sessions.create`. Don't `agents.create` in the request path. Anthropic CLI can create agents/environments from version-controlled YAML.

**Setup**: Maven dependency `com.anthropic:anthropic-java`. Client: `AnthropicOkHttpClient.fromEnv()` reads `ANTHROPIC_API_KEY`.

**Environments**: `client.beta().environments().create(EnvironmentCreateParams.builder().name(...).config(BetaCloudConfigParams.builder().networking(UnrestrictedNetwork.builder().build()).build()).build())`.

**Agents**:
- Create: `client.beta().agents().create(AgentCreateParams.builder().name().model().system().addTool(BetaManagedAgentsAgentToolset20260401Params.builder()...).build())`
- Update (creates new version): `client.beta().agents().update(agent.id(), AgentUpdateParams.builder().version(agent.version()).system(...))`
- Versions: `client.beta().agents().versions().list(agent.id()).autoPager()`
- Archive: `client.beta().agents().archive(agent.id())`

**Sessions**: `client.beta().sessions().create(SessionCreateParams.builder().agent(BetaManagedAgentsAgentParams.builder().type(AGENT).id().version().build()).environmentId().title().build())`.

**Send user message**: `client.beta().sessions().events().send(...)` with `BetaManagedAgentsUserMessageEventParams.builder().addTextContent(...)`.

**Streaming pattern (CRITICAL)**: open the stream BEFORE (or concurrently with) sending the message. Stream-after-send delivers early events as one buffered batch.

```java
try (var stream = client.beta().sessions().events().streamStreaming(session.id())) {
    client.beta().sessions().events().send(...);  // send while stream open
    for (var event : (Iterable<StreamEvents>) stream.stream()::iterator) {
        if (event.isAgentMessage()) { ... }
        else if (event.isAgentToolUse()) { ... }
        else if (event.isSessionStatusIdle()) break;
    }
}
```

**Reconnect + tail**: list past events first to dedupe (read raw `_json()._json().asObject()` for cross-variant `id` field), then tail live events.

**Files**: `client.beta().files().upload(FileUploadParams.builder().file(Path.of("data.csv")).build())` → mount via `BetaManagedAgentsFileResourceParams` in `SessionCreateParams.addResource(...)`. Add/delete resources mid-session via `client.beta().sessions().resources().add/delete()`.

**MCP servers**: agent declares server URL; session attaches a vault containing credentials.

**Vaults**: `client.beta().vaults().create(...)` with `displayName` + `metadata`. Add OAuth credentials via `client.beta().vaults().credentials().create(vaultId, CredentialCreateParams.builder().displayName().auth(BetaManagedAgentsMcpOAuthCreateParams.builder().mcpServerUrl().accessToken().expiresAt().refresh(... clientId .scope .refreshToken .clientSecretPostTokenEndpointAuth .build()).build()).build())`. Rotate via `credentials().update(...)`. Archive vault.

**GitHub repo resource**: `BetaManagedAgentsGitHubRepositoryResourceParams.builder().url().mountPath().authorizationToken().build()`. Multiple repos per session supported. Token rotation via `client.beta().sessions().resources().update(repoResourceId, ResourceUpdateParams.builder().sessionId().authorizationToken().build())`.

**Notes flagged in raw**: `user.custom_tool_result` Java bindings + file list/download Java bindings not yet documented in this skill — refer to the SDK repo.
