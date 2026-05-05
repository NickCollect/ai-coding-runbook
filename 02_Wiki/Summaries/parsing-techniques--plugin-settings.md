---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/plugin-settings/references/parsing-techniques.md
title: "Settings File Parsing Techniques (plugin-settings skill)"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Hooks, Settings]
concepts_referenced: []
---

Reference for parsing `.claude/plugin-name.local.md` files (markdown with YAML frontmatter) in bash scripts. Used by hookify-style plugins that store user config alongside body content.

**File structure**: YAML frontmatter between `---` markers, then markdown body.

**Extract frontmatter block**:
```bash
FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$FILE")
```

**Extract body** (handles `---` appearing inside body):
```bash
BODY=$(awk '/^---$/{i++; next} i>=2' "$FILE")
```

**Field extraction patterns**:
- String: `grep '^field:' | sed 's/field: *//'` then strip quotes via `sed 's/^"\(.*\)"$/\1/'`.
- Boolean: same extraction; check `[[ "$ENABLED" == "true" ]]`.
- Numeric: extract + validate `[[ "$N" =~ ^[0-9]+$ ]]`.
- Lists: simple substring check OR use `yq -o json` + `jq -r '.[]'` for proper iteration.

**Atomic updates** (prevents corruption):
```bash
TEMP_FILE="${FILE}.tmp.$$"
sed "s/^field: .*/field: $NEW/" "$FILE" > "$TEMP_FILE"
mv "$TEMP_FILE" "$FILE"
```

**Validation techniques**: file exists/readable check; count `---` markers (`grep -c '^---$' >= 2`); enum validation via `case` statement; numeric range `[[ $N -lt 1 ]] || [[ $N -gt 10000 ]]`.

**Edge cases**:
- Quotes in values: handle both quoted (`"value"`) and unquoted forms via two `sed` strips (double-quote and single-quote).
- `---` appearing in body — `awk` counter pattern handles this.
- Empty/null values — check `[[ -z "$VALUE" || "$VALUE" == "null" ]]` and apply defaults.
- Special characters — always quote variables when using.

**Performance**: cache parsed `FRONTMATTER` once and extract multiple fields from cache; lazy-load (do quick stdin checks before reading settings file).

**Safe JSON construction** with parsed user content: use `jq -n --arg prompt "$PROMPT" '{decision:"block", reason:$prompt}'` instead of string concatenation.

**Alternative: yq** (`brew install yq`) for proper YAML parsing — better for complex structures and lists. Trade-off: extra dependency, may not be on all systems. Recommendation: sed/grep for simple fields, yq for complex.

Includes complete example template combining defaults, validation, error recovery, and mode-based dispatch.
