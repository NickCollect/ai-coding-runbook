---
type: summary
source: 01_Raw/github/anthropics/claude-quickstarts/computer-use-demo/README.md
source_url: https://github.com/anthropics/claude-quickstarts/blob/main/computer-use-demo/README.md
title: "Claude Quickstarts — computer-use-demo README"
summarized_at: 2026-05-05
entities_referenced: [Computer-use-tool-API, Computer-use, Enterprise-gateway]
concepts_referenced: []
---

Reference implementation for the Anthropic Computer Use Demo. Latest update adds support for Claude 4 models including Opus 4.5 (`claude-opus-4-5-20251101`), Sonnet 4.5 (`claude-sonnet-4-5-20250929`), Sonnet 4 (`claude-sonnet-4-20250514`), Opus 4 (`claude-opus-4-20250514`), and Haiku 4.5 (`claude-haiku-4-5-20251001`). Includes the updated `str_replace_based_edit_tool` (replaces `str_replace_editor`); `undo_edit` has been removed.

**Beta caveats.** Computer use is a beta feature. The README highlights specific risks: dedicated VM/container with minimal privileges, avoid sensitive data, allowlist internet domains, human-in-the-loop for consequential actions (cookies, financial transactions, terms of service). Claude may follow instructions found in webpage/image content even when they conflict with user instructions — prompt injection precautions are advised. Inform end users and obtain consent. The Beta API in the reference implementation is subject to change; consult API release notes.

**Architecture caveats.** Components are weakly separated — the agent loop runs in the container being controlled by Claude. Single-session use only; restart/reset between sessions if needed.

**What's included.**

- Build files for a Docker container with all deps.
- A computer-use agent loop using Claude API, Bedrock, or Vertex (supports Opus 4.5/4, Sonnet 4.5/4/3.7/3.5, Haiku 4.5).
- Anthropic-defined computer-use tools.
- A Streamlit app for interacting with the agent loop.

**Quickstart — Claude API.** Set `ANTHROPIC_API_KEY` and run:

```bash
docker run -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 -p 8501:8501 -p 6080:6080 -p 8080:8080 \
    -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

**Quickstart — Bedrock.** Requires AWS credentials with appropriate Bedrock model-access permissions. Pass `-e API_PROVIDER=bedrock`, `AWS_PROFILE`, `AWS_REGION`, mount `~/.aws` into the container.

The README continues with Vertex setup, accessing the demo app interfaces (Streamlit, NoVNC, raw VNC), and detailed safety/risk guidance.
