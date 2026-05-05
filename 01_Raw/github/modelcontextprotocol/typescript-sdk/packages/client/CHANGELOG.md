# @modelcontextprotocol/client

## 2.0.0-alpha.2

### Patch Changes

- [#1840](https://github.com/modelcontextprotocol/typescript-sdk/pull/1840) [`424cbae`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`424cbae`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@KKonstantinov)! - tsdown exports resolution
  fix

## 2.0.0-alpha.1

### Major Changes

- [#1783](https://github.com/modelcontextprotocol/typescript-sdk/pull/1783) [`045c62a`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`045c62a`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@felixweinberger)! - Remove
  `WebSocketClientTransport`. WebSocket is not a spec-defined transport; use stdio or Streamable HTTP. The `Transport` interface remains exported for custom implementations. See #142.

### Minor Changes

- [#1527](https://github.com/modelcontextprotocol/typescript-sdk/pull/1527) [`dc896e1`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`dc896e1`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@felixweinberger)! - Add
  `discoverOAuthServerInfo()` function and unified discovery state caching for OAuth
    - New `discoverOAuthServerInfo(serverUrl)` export that performs RFC 9728 protected resource metadata discovery followed by authorization server metadata discovery in a single call. Use this for operations like token refresh and revocation that need the authorization server
      URL outside of `auth()`.
    - New `OAuthDiscoveryState` type and optional `OAuthClientProvider` methods `saveDiscoveryState()` / `discoveryState()` allow providers to persist all discovery results (auth server URL, resource metadata URL, resource metadata, auth server metadata) across sessions. This
      avoids redundant discovery requests and handles browser redirect scenarios where discovery state would otherwise be lost.
    - New `'discovery'` scope for `invalidateCredentials()` to clear cached discovery state.
    - New `OAuthServerInfo` type exported for the return value of `discoverOAuthServerInfo()`.

- [#1673](https://github.com/modelcontextprotocol/typescript-sdk/pull/1673) [`462c3fc`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`462c3fc`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@KKonstantinov)! - refactor: extract task
  orchestration from Protocol into TaskManager

    **Breaking changes:**
    - `taskStore`, `taskMessageQueue`, `defaultTaskPollInterval`, and `maxTaskQueueSize` moved from `ProtocolOptions` to `capabilities.tasks` on `ClientOptions`/`ServerOptions`

- [#1763](https://github.com/modelcontextprotocol/typescript-sdk/pull/1763) [`6711ed9`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`6711ed9`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@felixweinberger)! - Add
  `reconnectionScheduler` option to `StreamableHTTPClientTransport`. Lets non-persistent environments (serverless, mobile, desktop sleep/wake) override the default `setTimeout`-based SSE reconnection scheduling. The scheduler may return a cancel function that is invoked on
  `transport.close()`.

- [#1443](https://github.com/modelcontextprotocol/typescript-sdk/pull/1443) [`4aec5f7`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`4aec5f7`) Thanks [@NSeydoux](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@NSeydoux)! - The client credentials providers now
  support scopes being added to the token request.

- [#1689](https://github.com/modelcontextprotocol/typescript-sdk/pull/1689) [`0784be1`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`0784be1`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@felixweinberger)! - Support Standard Schema
  for tool and prompt schemas

    Tool and prompt registration now accepts any schema library that implements the [Standard Schema spec](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/Standard Schema spec): Zod v4, Valibot, ArkType, and others. `RegisteredTool.inputSchema`, `RegisteredTool.outputSchema`, and `RegisteredPrompt.argsSchema` now use
    `StandardSchemaWithJSON` (requires both `~standard.validate` and `~standard.jsonSchema`) instead of the Zod-specific `AnySchema` type.

    **Zod v4 schemas continue to work unchanged** — Zod v4 implements the required interfaces natively.

    ```typescript
    import { type } from 'arktype';

    server.registerTool(
        'greet',
        {
            inputSchema: type({ name: 'string' })
        },
        async ({ name }) => ({ content: [{ type: 'text', text: `Hello, ${name}!` }] })
    );
    ```

    For raw JSON Schema (e.g. TypeBox output), use the new `fromJsonSchema` adapter:

    ```typescript
    import { fromJsonSchema, AjvJsonSchemaValidator } from '@modelcontextprotocol/core';

    server.registerTool(
        'greet',
        {
            inputSchema: fromJsonSchema({ type: 'object', properties: { name: { type: 'string' } } }, new AjvJsonSchemaValidator())
        },
        handler
    );
    ```

    **Breaking changes:**
    - `experimental.tasks.getTaskResult()` no longer accepts a `resultSchema` parameter. Returns `GetTaskPayloadResult` (a loose `Result`); cast to the expected type at the call site.
    - Removed unused exports from `@modelcontextprotocol/core`: `SchemaInput`, `schemaToJson`, `parseSchemaAsync`, `getSchemaShape`, `getSchemaDescription`, `isOptionalSchema`, `unwrapOptionalSchema`. Use the new `standardSchemaToJsonSchema` and `validateStandardSchema` instead.
    - `completable()` remains Zod-specific (it relies on Zod's `.shape` introspection).

- [#1710](https://github.com/modelcontextprotocol/typescript-sdk/pull/1710) [`e563e63`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`e563e63`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@felixweinberger)! - Add `AuthProvider` for
  composable bearer-token auth; transports adapt `OAuthClientProvider` automatically
    - New `AuthProvider` interface: `{ token(): Promise<string | undefined>; onUnauthorized?(ctx): Promise<void> }`. Transports call `token()` before every request and `onUnauthorized()` on 401 (then retry once).
    - Transport `authProvider` option now accepts `AuthProvider | OAuthClientProvider`. OAuth providers are adapted internally via `adaptOAuthProvider()` — no changes needed to existing `OAuthClientProvider` implementations.
    - For simple bearer tokens (API keys, gateway-managed tokens, service accounts): `{ authProvider: { token: async () => myKey } }` — one-line object literal, no class.
    - New `adaptOAuthProvider(provider)` export for explicit adaptation.
    - New `handleOAuthUnauthorized(provider, ctx)` helper — the standard OAuth `onUnauthorized` behavior.
    - New `isOAuthClientProvider()` type guard.
    - New `UnauthorizedContext` type.
    - Exported previously-internal auth helpers for building custom flows: `applyBasicAuth`, `applyPostAuth`, `applyPublicAuth`, `executeTokenRequest`.

    Transports are simplified internally — ~50 lines of inline OAuth orchestration (auth() calls, WWW-Authenticate parsing, circuit-breaker state) moved into the adapter's `onUnauthorized()` implementation. `OAuthClientProvider` itself is unchanged.

- [#1614](https://github.com/modelcontextprotocol/typescript-sdk/pull/1614) [`1a78b01`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`1a78b01`) Thanks [@pcarleton](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@pcarleton)! - Apply resolved scope consistently
  to both DCR and the authorization URL (SEP-835)

    When `scopes_supported` is present in the protected resource metadata (`/.well-known/oauth-protected-resource`), the SDK already uses it as the default scope for the authorization URL. This change applies the same resolved scope to the dynamic client registration request
    body, ensuring both use a consistent value.
    - `registerClient()` now accepts an optional `scope` parameter that overrides `clientMetadata.scope` in the registration body.
    - `auth()` now computes the resolved scope once (WWW-Authenticate → PRM `scopes_supported` → `clientMetadata.scope`) and passes it to both DCR and the authorization request.

### Patch Changes

- [#1758](https://github.com/modelcontextprotocol/typescript-sdk/pull/1758) [`e86b183`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`e86b183`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@KKonstantinov)! - tasks - disallow requesting
  a null TTL

- [#1824](https://github.com/modelcontextprotocol/typescript-sdk/pull/1824) [`fcde488`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`fcde488`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@felixweinberger)! - Drop `zod` from
  `peerDependencies` (kept as direct dependency)

    Since Standard Schema support landed, `zod` is purely an internal runtime dependency used for protocol message parsing. User-facing schemas (`registerTool`, `registerPrompt`) accept any Standard Schema library. `zod` remains in `dependencies` and auto-installs; users no
    longer need to install it alongside the SDK.

- [#1761](https://github.com/modelcontextprotocol/typescript-sdk/pull/1761) [`01954e6`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`01954e6`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@felixweinberger)! - Convert remaining
  capability-assertion throws to `SdkError(SdkErrorCode.CapabilityNotSupported, ...)`. Follow-up to #1454 which missed `Client.assertCapability()`, the task capability helpers in `experimental/tasks/helpers.ts`, and the sampling/elicitation capability checks in
  `experimental/tasks/server.ts`.

- [#1632](https://github.com/modelcontextprotocol/typescript-sdk/pull/1632) [`d99f3ee`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`d99f3ee`) Thanks [@matantsach](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@matantsach)! - Continue OAuth metadata discovery
  on 502 (Bad Gateway) responses, matching the existing behavior for 4xx. This fixes MCP servers behind reverse proxies that return 502 for path-aware metadata URLs. Other 5xx errors still throw to avoid retrying against overloaded servers.

- [#1772](https://github.com/modelcontextprotocol/typescript-sdk/pull/1772) [`5276439`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`5276439`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@felixweinberger)! - Always set
  `windowsHide` when spawning stdio server processes on Windows, not just in Electron environments. Prevents unwanted console windows in non-Electron Windows applications.

- [#1390](https://github.com/modelcontextprotocol/typescript-sdk/pull/1390) [`9bc9abc`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`9bc9abc`) Thanks [@DePasqualeOrg](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@DePasqualeOrg)! - Fix
  StreamableHTTPClientTransport to handle error responses in SSE streams

- [#1343](https://github.com/modelcontextprotocol/typescript-sdk/pull/1343) [`4b5fdcb`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`4b5fdcb`) Thanks [@christso](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@christso)! - Fix OAuth error handling for servers
  returning errors with HTTP 200 status

    Some OAuth servers (e.g., GitHub) return error responses with HTTP 200 status instead of 4xx. The SDK now checks for an `error` field in the JSON response before attempting to parse it as tokens, providing users with meaningful error messages.

- [#1534](https://github.com/modelcontextprotocol/typescript-sdk/pull/1534) [`69a0626`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`69a0626`) Thanks [@josefaidt](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@josefaidt)! - remove npm references, use pnpm

- [#1386](https://github.com/modelcontextprotocol/typescript-sdk/pull/1386) [`00249ce`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`00249ce`) Thanks [@PederHP](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@PederHP)! - Respect capability negotiation in list
  methods by returning empty lists when server lacks capability

    The Client now returns empty lists instead of sending requests to servers that don't advertise the corresponding capability:
    - `listPrompts()` returns `{ prompts: [] }` if server lacks prompts capability
    - `listResources()` returns `{ resources: [] }` if server lacks resources capability
    - `listResourceTemplates()` returns `{ resourceTemplates: [] }` if server lacks resources capability
    - `listTools()` returns `{ tools: [] }` if server lacks tools capability

    This respects the MCP spec requirement that "Both parties SHOULD respect capability negotiation" and avoids unnecessary server warnings and traffic. The existing `enforceStrictCapabilities` option continues to throw errors when set to `true`.

- [#1534](https://github.com/modelcontextprotocol/typescript-sdk/pull/1534) [`69a0626`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`69a0626`) Thanks [@josefaidt](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@josefaidt)! - clean up package manager usage, all
  pnpm

- [#1595](https://github.com/modelcontextprotocol/typescript-sdk/pull/1595) [`13a0d34`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`13a0d34`) Thanks [@bhosmer-ant](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@bhosmer-ant)! - Don't swallow fetch `TypeError`
  as CORS in non-browser environments. Network errors (DNS resolution failure, connection refused, invalid URL) in Node.js and Cloudflare Workers now propagate from OAuth discovery instead of being silently misattributed to CORS and returning `undefined`. This surfaces the real
  error to callers rather than masking it as "metadata not found."

- [#1279](https://github.com/modelcontextprotocol/typescript-sdk/pull/1279) [`71ae3ac`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/`71ae3ac`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/client/@KKonstantinov)! - Initial 2.0.0-alpha.0
  client and server package
