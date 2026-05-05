---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool
title: "Code execution tool"
summarized_at: 2026-05-05
entities_referenced: [Code-execution-tool, Web-search-tool, Web-fetch-tool, Bash-tool-API, Text-editor-tool, Files-API, Skill, Batches-API]
concepts_referenced: []
---

The [[Code-execution-tool]] runs Python and bash code in a sandboxed container so Claude can analyze data, create visualizations, run system commands, create/edit files, and process uploaded files inside an API conversation. **Free when used with [[Web-search-tool]] or [[Web-fetch-tool]]** (no additional charges beyond standard input/output token costs); standard charges apply otherwise. Code execution is a core primitive for building high-performance agents and enables dynamic filtering of web search/fetch results before they reach the context window. **Not eligible for ZDR.**

**Tool versions.** `code_execution_20250825` (Bash + file operations + Python) on all supported models. `code_execution_20260120` (adds REPL state persistence and programmatic tool calling from inside the sandbox) on Opus 4.5+ and Sonnet 4.5+ only. Legacy `code_execution_20250522` (Python only) still available.

**Model compatibility.** Opus 4.7/4.6/4.5, Sonnet 4.6/4.5/3.7 (deprecated), Haiku 4.5/3.5, Opus 4.1/4 (deprecated). Available on Claude API and Microsoft Azure AI Foundry; not on Amazon Bedrock or Google Vertex AI.

**How it works.** Claude evaluates whether code execution would help; the tool provides Bash commands and file operations (create/view/edit). Two sub-tools are exposed: `bash_code_execution` and `text_editor_code_execution`. All operations run in a secure sandbox.

**Multi-environment caveat.** When code execution runs alongside a client-provided [[Bash-tool-API]] or custom REPL, Claude is in a multi-computer environment. Anthropic's sandbox and your local environment are separate; state is not shared. Add a system prompt clarifying the distinction: variables/files do NOT persist between environments, use `code_execution` for general computation, use client-provided tools for the user's local system. This matters especially when combining with web search/fetch (which auto-enable code execution).

**Files.** Upload via the [[Files-API]] (`anthropic-beta: files-api-2025-04-14`) and reference via a `container_upload` content block. Supported types: CSV, Excel (.xlsx/.xls), JSON, XML, images (JPEG/PNG/GIF/WebP), text (.txt/.md/.py). Claude can also create files; retrieve them by walking response content for `bash_code_execution_tool_result` blocks containing `BashCodeExecutionOutputBlock` entries with `file_id`, then download via `client.beta.files.download(file_id)`.

**Container lifecycle.** Each Anthropic container is scoped to an API workspace and expires 30 days after creation. Reuse a container across requests by passing `container: <container_id>` extracted from a previous response—this preserves files between requests.

**Runtime.** Python 3.11.12 on a Linux x86_64 container. **5 GiB RAM, 5 GiB disk, 1 CPU.** **Internet access completely disabled**; no outbound network requests permitted. Pre-installed libs include pandas, numpy, scipy, scikit-learn, statsmodels, matplotlib, seaborn, pyarrow, openpyxl, xlsxwriter, pillow, python-pptx, python-docx, pypdf, pdfplumber, pdf2image, reportlab, sympy, mpmath, tqdm, dateutil, joblib, ripgrep (rg), fd, sqlite, etc.

**Response format.** Bash commands return `bash_code_execution_tool_result` with `stdout`, `stderr`, `return_code`. File operations return `text_editor_code_execution_tool_result` with operation-specific fields: view (`file_type`, `content`, `numLines`, `startLine`, `totalLines`), create (`is_file_update`), edit/`str_replace` (diff fields `oldStart`, `oldLines`, `newStart`, `newLines`, `lines`).

**Error codes.** Common: `unavailable`, `execution_time_exceeded`, `container_expired`, `invalid_tool_input`, `too_many_requests`. Bash-specific: `output_file_too_large`. Text editor-specific: `file_not_found`, `string_not_found` (for `str_replace`).

**Pause turn.** Long-running turns may end with `stop_reason: "pause_turn"`; pass the response back as-is to let Claude continue.

**Pricing (when not bundled with web search/fetch).** Billed by execution time, tracked separately from tokens. Minimum **5 minutes** per execution. Each org gets **1,550 free hours per month**; additional usage at **$0.05 per hour, per container**. If files are included in the request, time is billed even if the tool isn't invoked (preloading cost). Reported in `usage.server_tool_use.code_execution_requests`.

**Streaming.** Code execution events arrive as SSE: `content_block_start` for the `server_tool_use` block, `content_block_delta` with `partial_json` for the code, then a pause while it executes, then a `content_block_start` for the result.

**Other.** Supports the [[Batches-API]]—same per-call price. Container data (artifacts, uploads, outputs) retained 30 days; files created in the [[Files-API]] persist until deleted. The code execution tool also enables Claude to use [[Skill]]s ("Skills are modular capabilities consisting of instructions, scripts, and resources").

**Upgrade path from `code-execution-2025-05-22`.** Change beta header and tool type to the `2025-08-25` versions; existing Python-only workflows continue to work; new Bash + file response block types replace the old `code_execution_result`.
