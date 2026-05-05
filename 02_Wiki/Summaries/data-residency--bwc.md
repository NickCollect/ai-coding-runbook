---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/data-residency.md
source_url: https://platform.claude.com/docs/en/build-with-claude/data-residency
title: "Data residency"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Workspace, Admin-API, Batches-API, Managed-agent, Enterprise-gateway]
concepts_referenced: []
---

Data residency controls where inference runs and where data is stored at rest. Two independent settings: **inference geo** (per-request) and **workspace geo** (at rest, including image transcoding / code execution). ZDR-eligible.

## Inference geo (`inference_geo`)

Per-request parameter on `POST /v1/messages`.

| Value | Description |
|---|---|
| `"global"` (default) | Any available geo for performance/availability |
| `"us"` | US-based infrastructure only |

Response `usage.inference_geo` confirms where it ran.

**Model availability:** Claude Opus 4.6 and all subsequent models. Older models return 400 if `inference_geo` is set.

**Not available on:** AWS Bedrock, Vertex AI (region determined by endpoint URL / inference profile), OpenAI SDK compatibility endpoint, Claude Managed Agents (but Managed Agents respects workspace geo).

## Workspace-level controls

Configurable via Console or Admin API under `data_residency`:

- **`allowed_inference_geos`** — restricts what geos a workspace can request; mismatched request → error.
- **`default_inference_geo`** — fallback when request omits `inference_geo`. Per-request value overrides.

## Workspace geo

- Set at workspace creation; **immutable**.
- Currently `"us"` only.

## Pricing

- Opus 4.6 and newer: `inference_geo: "us"` priced at **1.1×** standard (across input, output, cache writes, cache reads).
- Global routing: standard pricing.
- Older models unaffected.
- **Priority Tier:** the 1.1× also applies to TPM burndown — each token at `"us"` draws 1.1 tokens against committed TPM.
- 3rd-party platforms have their own regional pricing.

## Batch API support

`inference_geo` supported per-request inside a Batch.

## Migration from legacy opt-out

Orgs that previously opted out of global routing were auto-migrated to `allowed_inference_geos: ["us"]` + `default_inference_geo: "us"`. No code changes required.

## Limitations

- Rate limits shared across geos.
- Only `"us"` and `"global"` available at launch.
- Workspace geo only `"us"`; immutable.
