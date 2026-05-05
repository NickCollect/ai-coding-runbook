---
type: summary
source: 01_Raw/code.claude.com/docs/en/plugin-dependencies.md
source_url: https://code.claude.com/docs/en/plugin-dependencies
title: "Constrain plugin dependency versions"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Plugin-marketplace]
concepts_referenced: []
---

Plugins can depend on other plugins. Without version constraints, dependencies track latest — upstream breaking changes cascade. Version constraints pin to a tested range.

**Requires** Claude Code v2.1.110+.

**Declare** in `plugin.json` `dependencies` array:
```json
{
  "name": "deploy-kit",
  "version": "3.1.0",
  "dependencies": [
    "audit-logger",                                    // bare string, latest
    { "name": "secrets-vault", "version": "~2.1.0" }   // semver range
  ]
}
```

Object fields:
- `name` (required) — resolves within same marketplace by default.
- `version` — semver range (`~2.1.0`, `^2.0`, `>=1.4`, `=2.1.0`). Pre-release versions excluded unless range includes pre-release suffix like `^2.0.0-0`.
- `marketplace` — different marketplace (cross-marketplace blocked unless allowed).

**Cross-marketplace deps**: blocked by default. Root marketplace must list target in `allowCrossMarketplaceDependenciesOn` array in its `marketplace.json`. Trust does NOT chain through intermediate marketplaces. Manual install bypasses constraint.

**Tag releases**: format `{plugin-name}--v{version}` matching `plugin.json` version. Use `claude plugin tag --push` (validates contents, checks plugin.json + marketplace entry agree, requires clean working tree, refuses if tag exists). `--dry-run` to preview. The `--v` separator is parsed as prefix match — handles plugin names with hyphens. Cache dir name includes 12-char commit SHA suffix for safety against tag force-moves.

**Resolution**: Claude Code lists marketplace tags, filters `{name}--v*` prefix, fetches highest version satisfying range. No tag → plugin disabled with error listing available versions.

**npm sources**: tag-based resolution doesn't apply; constraint checked at load time only. Disabled with `dependency-version-unsatisfied` if mismatch.

**Constraint intersection**: when multiple installed plugins constrain same dep, ranges intersected, highest version satisfying all wins. Examples:
- `^2.0` + `>=2.1` → highest `2.x` ≥ 2.1.0
- `~2.1` + `~3.0` → install fails with `range-conflict`
- `=2.1.0` + none → pinned at 2.1.0

Auto-update fetches at highest tag satisfying ALL ranges.

**Orphaned deps cleanup**: `claude plugin prune` (v2.1.121+). User scope by default; `--scope project|local`, `--dry-run`, `-y` to skip confirm. Or `claude plugin uninstall <name> --prune` to clean during uninstall. Plugins you installed yourself are never pruned, only auto-installed deps.

**Errors** (in `claude plugin list`, `/plugin`, `/doctor`):
- `dependency-unsatisfied` — install or enable the dep.
- `range-conflict` — uninstall/update conflicting plugin, fix invalid `version`, simplify `||` chains.
- `dependency-version-unsatisfied` — re-resolve via `claude plugin install`.
- `no-matching-tag` — author hasn't tagged, or relax range.

Programmatic check: `claude plugin list --json` → read `errors` field.
