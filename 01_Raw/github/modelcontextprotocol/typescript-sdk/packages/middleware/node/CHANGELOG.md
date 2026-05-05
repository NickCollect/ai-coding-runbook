# @modelcontextprotocol/node

## 2.0.0-alpha.2

### Patch Changes

- [#1840](https://github.com/modelcontextprotocol/typescript-sdk/pull/1840) [`424cbae`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`424cbae`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/@KKonstantinov)! - tsdown exports resolution
  fix

- Updated dependencies [[`424cbae`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/[`424cbae`)]:
    - @modelcontextprotocol/server@2.0.0-alpha.2

## 2.0.0-alpha.1

### Patch Changes

- [#1504](https://github.com/modelcontextprotocol/typescript-sdk/pull/1504) [`327243c`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`327243c`) Thanks [@corvid-agent](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/@corvid-agent)! - Add missing `hono` peer
  dependency to `@modelcontextprotocol/node`. The package already depends on `@hono/node-server` which requires `hono` at runtime, but `hono` was only listed in the workspace root, not as a peer dependency of the package itself.

- [#1410](https://github.com/modelcontextprotocol/typescript-sdk/pull/1410) [`9296459`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`9296459`) Thanks [@mattzcarey](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/@mattzcarey)! - Prevent Hono from overriding
  global Response object by passing `overrideGlobalObjects: false` to `getRequestListener()`. This fixes compatibility with frameworks like Next.js whose response classes extend the native Response.

- [#1419](https://github.com/modelcontextprotocol/typescript-sdk/pull/1419) [`dcf708d`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`dcf708d`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/@KKonstantinov)! - remove deprecated .tool,
  .prompt, .resource method signatures

- [#1534](https://github.com/modelcontextprotocol/typescript-sdk/pull/1534) [`69a0626`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`69a0626`) Thanks [@josefaidt](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/@josefaidt)! - remove npm references, use pnpm

- [#1534](https://github.com/modelcontextprotocol/typescript-sdk/pull/1534) [`69a0626`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`69a0626`) Thanks [@josefaidt](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/@josefaidt)! - clean up package manager usage, all
  pnpm

- [#1419](https://github.com/modelcontextprotocol/typescript-sdk/pull/1419) [`dcf708d`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`dcf708d`) Thanks [@KKonstantinov](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/@KKonstantinov)! - deprecated .tool, .prompt,
  .resource method removal

- Updated dependencies [[`e86b183`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/[`e86b183`), [`0a75810`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`0a75810`),
  [`3466a9e`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`3466a9e`), [`fcde488`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`fcde488`),
  [`462c3fc`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`462c3fc`), [`01954e6`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`01954e6`),
  [`78bae74`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`78bae74`), [`689148d`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`689148d`),
  [`f1ade75`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`f1ade75`), [`108f2f3`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`108f2f3`),
  [`dcf708d`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`dcf708d`), [`f66a55b`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`f66a55b`),
  [`69a0626`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`69a0626`), [`69a0626`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`69a0626`),
  [`dcf708d`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`dcf708d`), [`0784be1`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`0784be1`),
  [`71ae3ac`](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/packages/middleware/node/`71ae3ac`)]:
    - @modelcontextprotocol/server@2.0.0-alpha.1
