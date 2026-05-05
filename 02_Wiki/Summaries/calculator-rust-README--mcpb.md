---
type: summary
source: 01_Raw/github/modelcontextprotocol/mcpb/examples/calculator-rust/README.md
source_url: https://github.com/modelcontextprotocol/mcpb/blob/main/examples/calculator-rust/README.md
title: "MCPB example: calculator-rust (binary server type)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Demonstrates packaging a compiled Rust binary as an MCP Bundle using `server.type = "binary"`. Based on the official Rust MCP SDK calculator example.

**Binary server type rationale**: unlike `node` or `uv` types where source is bundled and run by a runtime, `binary` packages a pre-compiled native executable — useful for Rust/Go/C/C++ MCP servers, perf-sensitive workloads, or servers with no runtime deps. Tradeoff: binaries are platform-specific, requiring a separate build per OS/architecture.

**Structure**: `manifest.json` (server.type = "binary"), `Cargo.toml`, `.mcpbignore`, `src/main.rs` (~80 LOC). The `server/` directory is created post-build with the compiled binary inside.

**Build steps** (requires Rust 1.85+): `cargo build --release`, then `mkdir -p server && cp target/release/mcp-calculator server/`.

**Pack**: `mcpb pack examples/calculator-rust`. The `.mcpbignore` ensures only `manifest.json` and `server/mcp-calculator` end up in the bundle — source and build artifacts are excluded.

**Testing** is shown via shell pipes feeding JSON-RPC messages (`initialize`, `notifications/initialized`, `tools/call`) directly to the binary's stdin and reading from stdout — confirming MCP stdio transport works without a host.

**Tools exposed**: `sum` (sum of two numbers), `sub` (difference of two numbers).

**Notes**: ~2.5 MB binary (stripped, LTO enabled); `Cargo.toml` uses `edition = "2024"` (Rust 1.85+); logs go to stderr via `tracing` to avoid corrupting MCP's stdio transport; uses the official `rmcp` crate.
