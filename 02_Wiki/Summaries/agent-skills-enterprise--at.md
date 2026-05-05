---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise
title: "Skills for enterprise"
summarized_at: 2026-05-05
entities_referenced: [Skill, Skill-API, MCP-server]
concepts_referenced: []
---

Governance, security review, evaluation, and organizational guidance for enterprise admins deploying Agent Skills at scale. Companion to the Skills overview (architecture) and best-practices (authoring).

**Two questions to separate.** "Are Skills safe in general?" is platform-level (covered in overview's security section). "How do I vet a specific Skill?" is the enterprise admin's problem—answered with a risk-tier table and a review checklist.

**Risk tier indicators (high concern):**
- *Code execution*: scripts (`*.py`, `*.sh`, `*.js`) in the Skill directory run with full environment access.
- *Instruction manipulation*: directives that tell Claude to ignore safety rules, hide actions, or alter behavior conditionally.
- *MCP server references*: instructions referencing [[MCP-server]] tools (`ServerName:tool_name`) extend access beyond the Skill itself.
- *Network access patterns*: URLs, `fetch`, `curl`, `requests` calls—potential exfiltration vectors.
- *Hardcoded credentials*: API keys/tokens in Skill files leak via Git history and context window.

Medium concern: file-system access scope (paths outside Skill dir, `../` traversal); tool invocations (bash, file ops).

**Review checklist.** Eight steps before deploying any third-party or internal Skill: read all directory content, run scripts in a sandbox, check for adversarial instructions, search for network access patterns, verify no hardcoded credentials (use env vars or credential stores), enumerate tool invocations, confirm redirect destinations, and check for data exfiltration patterns (read-then-write/encode-for-transmission, including via Claude's conversational responses).

> "Never deploy Skills from untrusted sources without a full audit. A malicious Skill can direct Claude to execute arbitrary code, access sensitive files, or transmit data externally. Treat Skill installation with the same rigor as installing software on production systems."

**Evaluation dimensions.** Approval gates should measure: triggering accuracy (right activations, no false fires), isolation behavior (works alone), coexistence (doesn't degrade other Skills), instruction following (no skipped validation), output quality. Authors must submit 3–5 evaluation queries per Skill covering should-trigger, should-not-trigger, and ambiguous edge cases. Test across all models the org uses (Haiku, Sonnet, Opus).

**Lifecycle (Plan → Create/Review → Test → Deploy → Monitor → Iterate/Deprecate).** Separation of duties: authors should not be their own reviewers. Deploy via the [[Skill-API]] for workspace-wide access. The Skills API does not currently expose usage analytics—admins must implement application-level logging to track which Skills are included in requests. Re-run evaluations periodically to detect drift.

**Recall limits.** Each Skill's metadata competes for attention in the system prompt; too many active Skills degrades selection. API requests support a maximum of **8 Skills per request**. If a role needs more, consolidate narrow Skills into broader ones or route requests to different Skill sets by task type. Use evaluations to measure recall accuracy as you add Skills, and stop when performance degrades.

**Start specific, consolidate later.** Encourage narrow workflow-specific Skills initially, then consolidate into role-based bundles when patterns emerge. Example: `formatting-sales-reports` + `querying-pipeline-data` + `updating-crm-records` → consolidate to `sales-operations` only when evals confirm equivalent performance.

**Cataloging.** Maintain an internal registry per Skill: purpose, owner, version, dependencies (MCP servers, packages, external services), evaluation status (last date and results).

**Role-based bundles.** Sales (CRM, pipeline, proposals); Engineering (code review, deployment, incident response); Finance (reporting, validation, audit prep). Keep each role's active Skill set focused.

**Distribution and version control.** Store Skill directories in Git (history, PRs, rollback). Use the Skills API for workspace-scoped distribution. Production: pin Skills to specific versions, run full eval suite before promotion, treat every update as a new deployment requiring full security review. Maintain previous version as immediate rollback. Compute checksums of reviewed Skills and verify at deployment; use signed commits for provenance.

**Cross-surface caveat.** Custom Skills do not sync across surfaces—API uploads aren't available on claude.ai or in Claude Code, and vice versa. Maintain Git as the single source of truth and implement your own synchronization.
