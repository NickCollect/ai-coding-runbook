# @modelcontextprotocol/server

## 2.0.0-alpha.2

### Patch Changes

- [#1840](https://github.com/modelcontextprotocol/typescript-sdk/pull/1840) [`424cbae`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`424cbae`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@KKonstantinov)! - tsdown exports resolution
  fix

## 2.0.0-alpha.1

### Major Changes

- [#1389](https://github.com/modelcontextprotocol/typescript-sdk/pull/1389) [`108f2f3`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`108f2f3`) Thanks [@DePasqualeOrg](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@DePasqualeOrg)! - Fix error handling for
  unknown tools and resources per MCP spec.

    **Tools:** Unknown or disabled tool calls now return JSON-RPC protocol errors with code `-32602` (InvalidParams) instead of `CallToolResult` with `isError: true`. Callers who checked `result.isError` for unknown tools should catch rejected promises instead.

    **Resources:** Unknown resource reads now return error code `-32002` (ResourceNotFound) instead of `-32602` (InvalidParams).

    Added `ProtocolErrorCode.ResourceNotFound`.

### Minor Changes

- [#1673](https://github.com/modelcontextprotocol/typescript-sdk/pull/1673) [`462c3fc`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`462c3fc`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@KKonstantinov)! - refactor: extract task
  orchestration from Protocol into TaskManager

    **Breaking changes:**
    - `taskStore`, `taskMessageQueue`, `defaultTaskPollInterval`, and `maxTaskQueueSize` moved from `ProtocolOptions` to `capabilities.tasks` on `ClientOptions`/`ServerOptions`

- [#1689](https://github.com/modelcontextprotocol/typescript-sdk/pull/1689) [`0784be1`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`0784be1`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@felixweinberger)! - Support Standard Schema
  for tool and prompt schemas

    Tool and prompt registration now accepts any schema library that implements the [Standard Schema spec](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/Standard Schema spec): Zod v4, Valibot, ArkType, and others. `RegisteredTool.inputSchema`, `RegisteredTool.outputSchema`, and `RegisteredPrompt.argsSchema` now use
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

### Patch Changes

- [#1758](https://github.com/modelcontextprotocol/typescript-sdk/pull/1758) [`e86b183`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`e86b183`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@KKonstantinov)! - tasks - disallow requesting
  a null TTL

- [#1363](https://github.com/modelcontextprotocol/typescript-sdk/pull/1363) [`0a75810`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`0a75810`) Thanks [@DevJanderson](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@DevJanderson)! - Fix ReDoS vulnerability in
  UriTemplate regex patterns (CVE-2026-0621)

- [#1372](https://github.com/modelcontextprotocol/typescript-sdk/pull/1372) [`3466a9e`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`3466a9e`) Thanks [@mattzcarey](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@mattzcarey)! - missing change for fix(client):
  replace body.cancel() with text() to prevent hanging

- [#1824](https://github.com/modelcontextprotocol/typescript-sdk/pull/1824) [`fcde488`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`fcde488`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@felixweinberger)! - Drop `zod` from
  `peerDependencies` (kept as direct dependency)

    Since Standard Schema support landed, `zod` is purely an internal runtime dependency used for protocol message parsing. User-facing schemas (`registerTool`, `registerPrompt`) accept any Standard Schema library. `zod` remains in `dependencies` and auto-installs; users no
    longer need to install it alongside the SDK.

- [#1761](https://github.com/modelcontextprotocol/typescript-sdk/pull/1761) [`01954e6`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`01954e6`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@felixweinberger)! - Convert remaining
  capability-assertion throws to `SdkError(SdkErrorCode.CapabilityNotSupported, ...)`. Follow-up to #1454 which missed `Client.assertCapability()`, the task capability helpers in `experimental/tasks/helpers.ts`, and the sampling/elicitation capability checks in
  `experimental/tasks/server.ts`.

- [#1433](https://github.com/modelcontextprotocol/typescript-sdk/pull/1433) [`78bae74`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`78bae74`) Thanks [@codewithkenzo](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@codewithkenzo)! - Fix transport errors being
  silently swallowed by adding missing `onerror` callback invocations before all `createJsonErrorResponse` calls in `WebStandardStreamableHTTPServerTransport`. This ensures errors like parse failures, invalid headers, and session validation errors are properly reported via the
  `onerror` callback.

- [#1660](https://github.com/modelcontextprotocol/typescript-sdk/pull/1660) [`689148d`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`689148d`) Thanks [@rechedev9](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@rechedev9)! - fix(server): propagate negotiated
  protocol version to transport in \_oninitialize

- [#1568](https://github.com/modelcontextprotocol/typescript-sdk/pull/1568) [`f1ade75`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`f1ade75`) Thanks [@stakeswky](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@stakeswky)! - Handle stdout errors (e.g. EPIPE)
  in `StdioServerTransport` gracefully instead of crashing. When the client disconnects abruptly, the transport now catches the stdout error, surfaces it via `onerror`, and closes.

- [#1419](https://github.com/modelcontextprotocol/typescript-sdk/pull/1419) [`dcf708d`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`dcf708d`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@KKonstantinov)! - remove deprecated .tool,
  .prompt, .resource method signatures

- [#1388](https://github.com/modelcontextprotocol/typescript-sdk/pull/1388) [`f66a55b`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`f66a55b`) Thanks [@mattzcarey](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@mattzcarey)! - reverting application/json in
  notifications

- [#1534](https://github.com/modelcontextprotocol/typescript-sdk/pull/1534) [`69a0626`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`69a0626`) Thanks [@josefaidt](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@josefaidt)! - remove npm references, use pnpm

- [#1534](https://github.com/modelcontextprotocol/typescript-sdk/pull/1534) [`69a0626`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`69a0626`) Thanks [@josefaidt](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@josefaidt)! - clean up package manager usage, all
  pnpm

- [#1419](https://github.com/modelcontextprotocol/typescript-sdk/pull/1419) [`dcf708d`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`dcf708d`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@KKonstantinov)! - deprecated .tool, .prompt,
  .resource method removal

- [#1279](https://github.com/modelcontextprotocol/typescript-sdk/pull/1279) [`71ae3ac`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/`71ae3ac`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/server/@KKonstantinov)! - Initial 2.0.0-alpha.0
  client and server package
