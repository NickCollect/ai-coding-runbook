---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart
title: "Get started with Agent Skills in the API"
summarized_at: 2026-05-05
entities_referenced: [Skill, Skill-API, Code-execution-tool, Files-API, Messages-API, Anthropic-SDK-Python, Anthropic-SDK-TypeScript]
concepts_referenced: []
---

Tutorial for using pre-built Agent Skills via the Claude API in under 10 minutes. Walks through listing available Skills, creating a PowerPoint presentation, and downloading the generated file.

**Prerequisites.** Claude API key, Python 3.7+ or curl. Pre-built Skills available in the API: `pptx` (PowerPoint), `xlsx` (Excel), `docx` (Word), `pdf` (PDF).

**Step 1: List available Skills.** Use the [[Skill-API]] with `source=anthropic` to enumerate Anthropic-managed Skills. Examples shown in cURL, the `ant` CLI, [[Anthropic-SDK-Python]] (`client.beta.skills.list(source="anthropic")`), and [[Anthropic-SDK-TypeScript]] (`client.beta.skills.list({ source: "anthropic" })`). Required headers: `anthropic-version: 2023-06-01` and `anthropic-beta: skills-2025-10-02`. Returns each Skill's metadata (name, `display_title`). The API call corresponds to **the first level of progressive disclosure**: Claude discovers Skills without loading their full instructions yet.

**Step 2: Create a presentation.** Use [[Messages-API]] with the `container` parameter to specify Skills, plus the [[Code-execution-tool]] in `tools`. Concrete request body:

```json
{
  "model": "claude-opus-4-7",
  "max_tokens": 4096,
  "container": {
    "skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]
  },
  "messages": [{"role": "user", "content": "Create a presentation about renewable energy with 5 slides"}],
  "tools": [{"type": "code_execution_20250825", "name": "code_execution"}]
}
```

Required beta headers: `code-execution-2025-08-25,skills-2025-10-02`. Field meanings: `container.skills` lists which Skills Claude can use; `type: "anthropic"` marks an Anthropic-managed Skill; `skill_id` identifies the specific Skill; `version: "latest"` pins to the most recently published version; `tools` enables the code execution container that Skills run inside. Claude matches the user request to a relevant Skill, loads its instructions (**second level of progressive disclosure**), then executes the Skill's code.

**Step 3: Download the file.** The presentation is created in the code execution container and saved as a file. Extract `file_id` from the response by walking content blocks for `tool_use` blocks where `name == "code_execution"` and finding the inner block with `file_id`. Download via the [[Files-API]]: `GET /v1/files/$FILE_ID/content` with the `files-api-2025-04-14` beta header. SDKs offer `client.beta.files.download(file_id=...)` (Python) and `client.beta.files.download(fileId)` (TypeScript), with `write_to_file` / `arrayBuffer` helpers to persist locally.

**Variations shown.** Same pattern with different `skill_id`:
- `xlsx`: "Create a quarterly sales tracking spreadsheet with sample data"
- `docx`: "Write a 2-page report on the benefits of renewable energy"
- `pdf`: "Generate a PDF invoice template"

All four examples use `model: "claude-opus-4-7"`, `max_tokens: 4096`, the same beta headers, and the same `container` + `code_execution_20250825` tool combination.

**Conceptual emphasis.** The tutorial repeatedly highlights progressive disclosure: Skills' metadata (L1) is preloaded into the system prompt at startup so Claude knows they exist; SKILL.md instructions (L2) only load when Claude triggers the Skill; the Skill's bundled scripts/resources (L3) only load when needed. Token efficiency vs. capability trade-off is the underlying point.

**Next steps offered.** Skills API guide (programmatic Skill management), creating custom Skills via `/v1/skills/create-skill`, authoring best practices, using Skills in Claude Code, and the Skills cookbook for example implementations.
