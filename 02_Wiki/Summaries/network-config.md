---
type: summary
source: 01_Raw/code.claude.com/docs/en/network-config.md
source_url: https://code.claude.com/docs/en/network-config
title: "Enterprise network configuration"
summarized_at: 2026-05-05
entities_referenced: [Settings, Enterprise-gateway, IDE-integration]
concepts_referenced: []
---

Configure Claude Code for enterprise envs: corporate proxies, custom CAs, mTLS. All env vars below also configurable via `settings.json`.

**Proxy**:
- Standard env vars: `HTTPS_PROXY` (recommended), `HTTP_PROXY`, `NO_PROXY` (space- or comma-separated; `*` to bypass all)
- **No SOCKS proxy support**
- Basic auth: include in URL `http://user:pass@proxy:8080`. For NTLM/Kerberos, use an LLM Gateway

**CA certificates**:
- Default trusts BOTH bundled Mozilla CAs and OS trust store. Enterprise TLS-inspection (CrowdStrike Falcon, Zscaler) works without extra config when root cert is in OS trust store.
- **System CA store integration requires the native binary distribution** — Node.js runtime needs `NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem`
- `CLAUDE_CODE_CERT_STORE` accepts `bundled,system` (comma-sep). Set just `bundled` or `system` to narrow. **No dedicated `settings.json` schema key** — use `env` block.

**mTLS**: `CLAUDE_CODE_CLIENT_CERT`, `CLAUDE_CODE_CLIENT_KEY`, optional `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE`.

**Required URLs to allowlist**:
| URL | For |
|---|---|
| `api.anthropic.com` | Claude API |
| `claude.ai` | claude.ai auth |
| `platform.claude.com` | Console auth |
| `downloads.claude.ai` | Plugin downloads, native installer/auto-updater |
| `storage.googleapis.com` | Native installer/auto-updater pre-v2.1.116 |
| `bridge.claudeusercontent.com` | Claude in Chrome extension WS bridge |

If installed via npm or self-distributed, end users may not need `downloads.claude.ai` / `storage.googleapis.com`.

Telemetry (Statsig, Sentry) is optional — see data-usage doc to disable before finalizing allowlist.

**Provider routing**: Bedrock/Vertex/Foundry route model traffic and auth to the provider, not to Anthropic endpoints. WebFetch still calls `api.anthropic.com` for domain safety check unless `skipWebFetchPreflight: true`.

**Cloud sessions** (Claude Code on the web, Code Review): connect from Anthropic-managed infra. GitHub Enterprise Cloud restricting by IP → enable [IP allow list inheritance for installed GitHub Apps] (Claude GitHub App registers its IP ranges) OR add Anthropic API IPs manually. GHES self-hosted behind firewall → allowlist Anthropic API IPs so the cloud can clone/post comments.
