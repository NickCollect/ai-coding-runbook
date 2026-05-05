---
type: summary
source: 01_Raw/github/modelcontextprotocol/mcpb/CLI.md
source_url: https://github.com/modelcontextprotocol/mcpb/blob/main/CLI.md
title: "MCPB CLI documentation"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Reference for the `mcpb` CLI (installed via `npm install -g @anthropic-ai/mcpb`), which builds, validates, signs, and inspects MCP Bundles.

**Commands:**

- `mcpb init [directory]` — interactive wizard creating a new `manifest.json`. Prompts for name, author, ID (auto-generated from author + extension name), display name, version (defaults from `package.json` or `1.0.0`), description, server type (Node/Python/Binary), entry point with sensible defaults per server type, tools, keywords, license, repository.
- `mcpb validate <path>` — validates a `manifest.json` against the schema. Accepts either a manifest file path or a directory containing one.
- `mcpb pack <directory> [output]` — packs a directory into a `.mcpb` archive. Auto-validates manifest, excludes common dev files (`.git`, `node_modules/.cache`, `.DS_Store`, etc.), uses ZIP max compression.
- `mcpb sign <mcpb-file>` — signs a bundle with an X.509 certificate. Options: `--cert/-c` (PEM cert, default `cert.pem`), `--key/-k` (PEM private key, default `key.pem`), `--intermediate/-i` (chain certs), `--self-signed` (generate one if absent).
- `mcpb verify <mcpb-file>` — checks signature validity, prints subject/issuer, validity dates, fingerprint, warns if self-signed.
- `mcpb info <mcpb-file>` — shows file size, signature status, certificate details.
- `mcpb unsign <mcpb-file>` — strips signature (dev/testing only).

**Certificate requirements** (for signing): X.509 cert in PEM format with Code Signing extended key usage; matching private key in PEM; optional intermediate certs for proper chain.

**Workflows documented:** quick-start (init → implement → pack → self-sign), development (init → implement → validate → pack → self-sign → verify → info), production (pack → sign with prod cert + intermediates → verify before distribution).

**Excluded files** (auto-skipped at pack time): `.DS_Store`, `Thumbs.db`, `.gitignore`, `.git/`, `*.log`, `.npm/`, `.npmrc`, `.yarnrc`, `.yarn/`, `.pnp.*`, `node_modules/.cache/`, `node_modules/.bin/`, `*.map`, `.env.local`, `.env.*.local`, `package-lock.json`, `yarn.lock`. Custom exclusions via `.mcpbignore` (gitignore-style: globs, dir paths, comments).

**Signature format (technical):** PKCS#7 (DER-encoded SignedData) appended to the ZIP with `MCPB_SIG_V1` and `MCPB_SIG_END` markers and a 4-byte little-endian length prefix. Detached signature — original ZIP content untouched, so unsigned `.mcpb` files remain valid ZIPs (backward compatible). The entire MCPB content excluding the signature block is signed; supports cert chains with intermediates.
