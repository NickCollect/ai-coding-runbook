---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/wif-providers/gcp.md
source_url: https://platform.claude.com/docs/en/build-with-claude/wif-providers/gcp
title: "Use WIF with Google Cloud"
summarized_at: 2026-05-07
entities_referenced: [Workload-Identity-Federation, Service-account, Federation-issuer, Federation-rule, Workspace]
concepts_referenced: [JWT]
---

GCP compute (Cloud Run, Cloud Functions, App Engine, GCE, GKE with Workload Identity) can request Google-signed OIDC identity token from instance metadata server for its attached service account. Token issuer is `https://accounts.google.com`; Anthropic validates via standard discovery — no extra GCP config required.

## Configure Google Cloud

### Cloud Run / Cloud Functions / App Engine / GCE

Attach a dedicated user-managed service account (not Compute Engine default SA). Inside workload, fetch identity token from metadata server with `audience` query param + `format=full` (so response carries `email` claim):

```
GET http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity?audience=https://api.anthropic.com&format=full
Metadata-Flavor: Google
```

Or `gcloud auth print-identity-token --audiences="https://api.anthropic.com" --include-email`.

Decoded payload: `iss = https://accounts.google.com`, `aud = https://api.anthropic.com`, `sub = <numeric-unique-id>` (opaque), `email = <SA-email>` (verified). Match rule on **both** `sub` and `email`.

### GKE with Workload Identity

Enable Workload Identity on cluster + bind K8s SA to Google SA via `iam.gke.io/gcp-service-account` annotation. GKE metadata server returns identical Google-signed token (same issuer, same `email` claim). `format=full` token additionally includes `google.compute_engine.project_id`, `zone`, `instance_name` — usable in CEL conditions to scope to specific cluster / node pool.

Alternative: GKE pods can use cluster's own OIDC issuer (`https://container.googleapis.com/v1/projects/PROJECT/locations/REGION/clusters/CLUSTER`) with projected `serviceAccountToken` — see Kubernetes guide.

## Configure Anthropic

- **Issuer**: `issuer_url: https://accounts.google.com`, `jwks_source: discovery`. Single issuer covers all GCP surfaces — differentiate workloads with rules, not issuers.
- **Rule**: match on both `sub` (numeric unique ID, never reused — protects rule if SA deleted/recreated with same email) and `email`. Find unique ID with `gcloud iam service-accounts describe SA_EMAIL --format='value(uniqueId)'`. Always pin `audience`.

## Acquisition

SDK passed callable token-provider (e.g., `google.oauth2.id_token.fetch_id_token`); SDK re-invokes on each refresh. Google identity tokens expire ~1 hour. Alternative file-based path: container entrypoint writes metadata response to file, set `ANTHROPIC_IDENTITY_TOKEN_FILE`.

## Verification + scope hardening

- Verify: decode metadata-server token with `jq -rR 'split(".")[1] | gsub("-";"+") | gsub("_";"/") | @base64d | fromjson'`; check `iss = https://accounts.google.com`, `aud`, `email` matches rule.
- Most common GCP failure: `email` claim missing — request token with `format=full`.
- Scope: match `sub` exactly (Google `sub` is opaque numeric ID, no stable prefix — never use `subject_prefix` with `*`); pin `email` alongside; pin audience; for GKE `format=full` add `condition` like `claims.google.compute_engine.project_id == "my-project"`.
