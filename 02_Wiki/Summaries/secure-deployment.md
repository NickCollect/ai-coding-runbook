---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/secure-deployment.md
source_url: https://code.claude.com/docs/en/agent-sdk/secure-deployment
title: "Securely deploying AI agents"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Sandboxing, Permission-mode, MCP-server, Enterprise-gateway]
concepts_referenced: []
---

Threat-model + isolation playbook for deploying Claude Code / Agent SDK. Explains why agents are different from traditional software (actions are dynamically generated and influenced by content they process — i.e., prompt injection from READMEs, files, web pages), and walks through controls layered for defense in depth.

**Built-in features**:
- **Permissions system** (allow/block/prompt with glob patterns, org-wide policies)
- **Bash command parsing**: commands are parsed into AST and matched against rules; unparsable or unmatched → require approval. `eval` always requires approval. *Note*: it's a permission gate, NOT a sandbox — does not infer danger from path or effect.
- **Web search summarization**: results summarized rather than dumped raw, mitigating prompt injection from web content.
- **Sandbox mode**: bash runs in OS-level FS/network isolation.

**Security principles**: trust-boundary separation (sensitive resources outside agent boundary, e.g., proxy injects API keys agent never sees), least privilege (per-resource restriction table for FS / network / credentials / Linux capabilities), defense in depth.

**Isolation tiers** (strength vs. overhead):
| Technology | Isolation | Overhead | Complexity |
|---|---|---|---|
| sandbox-runtime | Good | Very low | Low |
| Docker containers | Setup-dependent | Low | Medium |
| gVisor (`runsc`) | Excellent | Medium/High | Medium |
| VMs (Firecracker, QEMU) | Excellent | High | Medium/High |

- **sandbox-runtime** (`@anthropic-ai/sandbox-runtime`): bubblewrap (Linux) / sandbox-exec (macOS); built-in proxy via network namespace removal / Seatbelt. Caveats: shares host kernel; no TLS inspection (domain fronting risk).
- **Hardened Docker example** documents flags: `--cap-drop ALL`, `--security-opt no-new-privileges`, `--security-opt seccomp=`, `--read-only`, `--tmpfs`, `--network none` (route all traffic over a Unix socket to host proxy), `--memory`, `--pids-limit`, `--user 1000:1000`, read-only `:ro` mounts. Warns against mounting `~/.ssh`, `~/.aws`, `~/.config`.
- **gVisor** intercepts syscalls in userspace; CPU-bound ~0% overhead, file-I/O 10-200× slower.
- **Firecracker** microVMs boot <125ms with <5 MiB overhead; communication via `vsock` to host proxy.
- **Cloud**: combine isolation with private subnet + cloud firewall + Envoy proxy (`credential_injector`) + minimal IAM + audit logging.

**Credential management — the proxy pattern**: agent sends requests without credentials; proxy injects them outside the agent boundary. Two methods to wire up Claude Code: `ANTHROPIC_BASE_URL` (sampling-only, plaintext) and `HTTP_PROXY`/`HTTPS_PROXY` (system-wide; HTTPS uses opaque CONNECT tunnel unless TLS-terminating). For non-Anthropic services, prefer **custom tools / MCP servers** (no TLS interception needed) OR set up a TLS-terminating proxy with custom CA in agent's trust store. Note: Node.js `fetch()` ignores proxy vars by default — set `NODE_USE_ENV_PROXY=1` (Node 24+) or use `proxychains` / iptables transparent proxy.

Recommended proxies: Envoy, mitmproxy, Squid, LiteLLM.

**Filesystem**: read-only code mounts, but warn about credential files commonly in source trees (`.env`, `~/.git-credentials`, `~/.aws/credentials`, `~/.kube/config`, `*.pem`, etc.). For writable workspaces use `tmpfs` mounts (ephemeral) or overlay FS (review-then-apply).
