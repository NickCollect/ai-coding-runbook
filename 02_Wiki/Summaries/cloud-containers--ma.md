---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/cloud-containers.md
source_url: https://platform.claude.com/docs/en/managed-agents/cloud-containers
title: "Container reference"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Environment-API]
concepts_referenced: []
---

Reference for pre-installed packages, databases, and utilities in cloud containers used by Claude [[Managed-agent]] sessions. The agent can use these immediately without installation. **Requires beta header `managed-agents-2026-04-01`.**

**Programming languages (pre-installed).**

| Language | Version | Package manager |
|---|---|---|
| Python | 3.12+ | pip, uv |
| Node.js | 20+ | npm, yarn, pnpm |
| Go | 1.22+ | go modules |
| Rust | 1.77+ | cargo |
| Java | 21+ | maven, gradle |
| Ruby | 3.3+ | bundler, gem |
| PHP | 8.3+ | composer |
| C/C++ | GCC 13+ | make, cmake |

**Databases.** SQLite is pre-installed and immediately available. PostgreSQL `psql` and Redis `redis-cli` clients are present for connecting to *external* instances. Database servers themselves are NOT running by default—the container only ships client tooling.

**System utilities.** `git`, `curl`, `wget`, `jq`, `tar`, `zip`/`unzip`, `ssh`, `scp` (require network), `tmux`, `screen`.

**Development tools.** `make`, `cmake`, `docker` (limited availability), `ripgrep` (`rg`), `tree`, `htop`.

**Text processing.** `sed`, `awk`, `grep`, `vim`, `nano`, `diff`, `patch`.

**Container specs.**

| Property | Value |
|---|---|
| OS | Ubuntu 22.04 LTS |
| Architecture | x86_64 (amd64) |
| Memory | Up to 8 GB |
| Disk | Up to 10 GB |
| Network | **Disabled by default** (enable in [[Environment-API]] config) |

This page is a pure reference; no code examples or APIs—just the matrix of what comes baked into the container image.
