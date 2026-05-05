---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/command-development/references/marketplace-considerations.md
title: "Marketplace Considerations for Commands"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Plugin-marketplace, Plugin]
concepts_referenced: []
---

Guidelines for creating slash commands designed for distribution via marketplace. Distribution-grade commands need extra consideration vs personal commands.

**Universal compatibility**:
- Cross-platform `case` on `$(uname)` for Darwin/Linux/MINGW|MSYS|CYGWIN
- Avoid platform-specific commands (e.g., `pbcopy`); use detection chains: `pbcopy` → `xclip` → `clip.exe` → fallback message

**Minimal dependencies**:
- Check required tools with `command -v $tool` loop, fail with helpful install URLs
- Document optional dependencies in HTML comments (Required vs Optional with version numbers)

**Graceful degradation**: feature detection (`command -v gh`, `command -v docker`), adapt behavior based on available features (full vs limited functionality).

**UX for unknown users**:
- **Clear onboarding**: first-run check writing `.claude/command-initialized` marker, welcome explainer with "what this does" + quick start + setup
- **Progressive feature discovery**: tip footers ("Did you know? --fast flag")
- **Comprehensive error handling**: typo detection ("Did you mean: help?"), suggested similar commands when invalid option supplied
- **Helpful diagnostics** on operation failure: dump environment (platform/shell/cwd/command), check common issues (git repo, write perms, required files)

**Distribution best practices**:
- **Namespace awareness**: prefix with plugin name to avoid conflicts (`/plugin-name-command`, `/category-command`, `/verb-noun`)
- **Document naming rationale** in HTML comments
- **Configurability**: load `.claude/plugin-name.local.md` user prefs (verbose, color, max_results), fall back to defaults
- **Sensible defaults via `${VAR:-default}`** — work for 80% use cases
- **Version compatibility**: check plugin version, fail with `/plugin update plugin-name` instructions
- **Deprecation warnings**: emit warning for old flags with deprecation date + migration example, support both during transition

**Marketplace presentation**:
- **Discovery**: descriptive name + description, searchable keywords in HTML comments (`KEYWORDS: security, code-review, quality, validation, audit`)
- **Showcase examples** — embed sample output in command body so marketplace listing previews it
- **Feedback mechanism**: emoji reactions, `/command feedback` route
- **Analytics notes** (privacy-preserving aggregate stats only, opt-out respected)

**Quality standards**:
- **Professional polish**: consistent branding (✨ emoji, "Part of [Plugin] suite"), help/support/community links footer, attention to formatting (column alignment, thousands separators, progress indicators)
- **Reliability — idempotency**: `.claude/operation-completed.flag` check; re-run requires removing flag
- **Atomic operations**: temp dir → validate → atomic `mv` on success, `rm -rf` on failure → safe to retry

**Pre-release checklist** (HTML comment template): functionality (multi-platform, args/errors/edge cases), UX (description/errors/examples/onboarding/docs), distribution (no hardcoded paths, deps documented, config clear, versioned, changelog), quality (no TODO/debug, performance, security, privacy), support (README, troubleshooting, support contact, feedback, license).

**Beta releases**: 🧪 emoji + "BETA STATUS" block with version/stability/known limitations + report-issue / suggest / join-beta hooks.

**Versioning strategy**: major (breaking; document + migration guide), minor (backward compat; announce), patch (bug fixes; security prioritized). Schedule: patches as needed, minors monthly, majors annually.

**Update notifications**: detect newer version, prompt `/plugin update plugin-name` with release notes URL.

Summary principles: universal, self-contained, graceful, forgiving, helpful, discoverable, professional, reliable, maintainable, user-focused, complete, tested, secure, performant, ethical.
