# @modelcontextprotocol/core

## 2.0.0-alpha.1

### Minor Changes

- [#1673](https://github.com/modelcontextprotocol/typescript-sdk/pull/1673) [`462c3fc`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`462c3fc`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@KKonstantinov)! - refactor: extract task
  orchestration from Protocol into TaskManager

    **Breaking changes:**
    - `taskStore`, `taskMessageQueue`, `defaultTaskPollInterval`, and `maxTaskQueueSize` moved from `ProtocolOptions` to `capabilities.tasks` on `ClientOptions`/`ServerOptions`

- [#1389](https://github.com/modelcontextprotocol/typescript-sdk/pull/1389) [`108f2f3`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`108f2f3`) Thanks [@DePasqualeOrg](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@DePasqualeOrg)! - Fix error handling for
  unknown tools and resources per MCP spec.

    **Tools:** Unknown or disabled tool calls now return JSON-RPC protocol errors with code `-32602` (InvalidParams) instead of `CallToolResult` with `isError: true`. Callers who checked `result.isError` for unknown tools should catch rejected promises instead.

    **Resources:** Unknown resource reads now return error code `-32002` (ResourceNotFound) instead of `-32602` (InvalidParams).

    Added `ProtocolErrorCode.ResourceNotFound`.

- [#1689](https://github.com/modelcontextprotocol/typescript-sdk/pull/1689) [`0784be1`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`0784be1`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@felixweinberger)! - Support Standard Schema
  for tool and prompt schemas

    Tool and prompt registration now accepts any schema library that implements the [Standard Schema spec](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/Standard Schema spec): Zod v4, Valibot, ArkType, and others. `RegisteredTool.inputSchema`, `RegisteredTool.outputSchema`, and `RegisteredPrompt.argsSchema` now use
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

- [#1735](https://github.com/modelcontextprotocol/typescript-sdk/pull/1735) [`a2e5037`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`a2e5037`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@felixweinberger)! - Abort in-flight request
  handlers when the connection closes. Previously, request handlers would continue running after the transport disconnected, wasting resources and preventing proper cleanup. Also fixes `InMemoryTransport.close()` firing `onclose` twice on the initiating side.

- [#1574](https://github.com/modelcontextprotocol/typescript-sdk/pull/1574) [`379392d`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`379392d`) Thanks [@olaservo](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@olaservo)! - Add missing `size` field to
  `ResourceSchema` to match the MCP specification

- [#1363](https://github.com/modelcontextprotocol/typescript-sdk/pull/1363) [`0a75810`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`0a75810`) Thanks [@DevJanderson](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@DevJanderson)! - Fix ReDoS vulnerability in
  UriTemplate regex patterns (CVE-2026-0621)

- [#1761](https://github.com/modelcontextprotocol/typescript-sdk/pull/1761) [`01954e6`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`01954e6`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@felixweinberger)! - Convert remaining
  capability-assertion throws to `SdkError(SdkErrorCode.CapabilityNotSupported, ...)`. Follow-up to #1454 which missed `Client.assertCapability()`, the task capability helpers in `experimental/tasks/helpers.ts`, and the sampling/elicitation capability checks in
  `experimental/tasks/server.ts`.

- [#1790](https://github.com/modelcontextprotocol/typescript-sdk/pull/1790) [`89fb094`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`89fb094`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@felixweinberger)! - Consolidate per-request
  cleanup in `_requestWithSchema` into a single `.finally()` block. This fixes an abort signal listener leak (listeners accumulated when a caller reused one `AbortSignal` across requests) and two cases where `_responseHandlers` entries leaked on send-failure paths.

- [#1486](https://github.com/modelcontextprotocol/typescript-sdk/pull/1486) [`65bbcea`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`65bbcea`) Thanks [@localden](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@localden)! - Fix InMemoryTaskStore to enforce
  session isolation. Previously, sessionId was accepted but ignored on all TaskStore methods, allowing any session to enumerate, read, and mutate tasks created by other sessions. The store now persists sessionId at creation time and enforces ownership on all reads and writes.

- [#1766](https://github.com/modelcontextprotocol/typescript-sdk/pull/1766) [`48aba0d`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`48aba0d`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@felixweinberger)! - Add explicit
  `| undefined` to optional properties on the `Transport` interface and `TransportSendOptions` (`onclose`, `onerror`, `onmessage`, `sessionId`, `setProtocolVersion`, `setSupportedProtocolVersions`, `onresumptiontoken`).

    This fixes TS2420 errors for consumers using `exactOptionalPropertyTypes: true` without `skipLibCheck`, where the emitted `.d.ts` for implementing classes included `| undefined` but the interface did not.

    Workaround for older SDK versions: enable `skipLibCheck: true` in your tsconfig.

- [#1419](https://github.com/modelcontextprotocol/typescript-sdk/pull/1419) [`dcf708d`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`dcf708d`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@KKonstantinov)! - remove deprecated .tool,
  .prompt, .resource method signatures

- [#1534](https://github.com/modelcontextprotocol/typescript-sdk/pull/1534) [`69a0626`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`69a0626`) Thanks [@josefaidt](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@josefaidt)! - remove npm references, use pnpm

- [#1534](https://github.com/modelcontextprotocol/typescript-sdk/pull/1534) [`69a0626`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`69a0626`) Thanks [@josefaidt](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@josefaidt)! - clean up package manager usage, all
  pnpm

- [#1796](https://github.com/modelcontextprotocol/typescript-sdk/pull/1796) [`d6a02c8`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`d6a02c8`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@felixweinberger)! - Ensure
  `standardSchemaToJsonSchema` emits `type: "object"` at the root, fixing discriminated-union tool/prompt schemas that previously produced `{oneOf: [...]}` without the MCP-required top-level type. Also throws a clear error when given an explicitly non-object schema (e.g.
  `z.string()`). Fixes #1643.

- [#1419](https://github.com/modelcontextprotocol/typescript-sdk/pull/1419) [`dcf708d`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`dcf708d`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@KKonstantinov)! - deprecated .tool, .prompt,
  .resource method removal

- [#1762](https://github.com/modelcontextprotocol/typescript-sdk/pull/1762) [`64897f7`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/`64897f7`) Thanks [@felixweinberger](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/core/@felixweinberger)! -
  `ReadBuffer.readMessage()` now silently skips non-JSON lines instead of throwing `SyntaxError`. This prevents noisy `onerror` callbacks when hot-reload tools (tsx, nodemon) write debug output like "Gracefully restarting..." to stdout. Lines that parse as JSON but fail JSONRPC
  schema validation still throw.
