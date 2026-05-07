---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/wif-providers/kubernetes.md
source_url: https://platform.claude.com/docs/en/build-with-claude/wif-providers/kubernetes
title: "Use WIF with Kubernetes"
summarized_at: 2026-05-07
entities_referenced: [Workload-Identity-Federation, Service-account, Federation-issuer, Federation-rule]
concepts_referenced: [JWT]
---

Self-managed Kubernetes clusters (kubeadm, k3s, OpenShift, on-prem) sign OIDC JWTs for every pod via [projected service account tokens](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#serviceaccount-token-volume-projection). Cluster's API server acts as OIDC issuer. Each token's `sub` follows `system:serviceaccount:<namespace>:<service-account>`. Native to Kubernetes — underlies every distribution. Find issuer URL: `kubectl get --raw /.well-known/openid-configuration | jq -r .issuer`.

## Prerequisites

- Cluster with `--service-account-issuer` flag on API server (kubeadm typically uses `https://kubernetes.default.svc.cluster.local`).
- Either: JWKS endpoint reachable from public internet over HTTPS port 443, **or** can fetch JWKS from inside cluster and register `inline`.

## Configure Kubernetes (project token)

```yaml
spec:
  serviceAccountName: inference-worker
  volumes:
    - name: anthropic-token
      projected:
        sources:
          - serviceAccountToken:
              audience: https://api.anthropic.com
              expirationSeconds: 3600
              path: token
  containers:
    - env:
        - name: ANTHROPIC_IDENTITY_TOKEN_FILE
          value: /var/run/secrets/anthropic.com/token
        - name: ANTHROPIC_FEDERATION_RULE_ID
          value: fdrl_...
        - name: ANTHROPIC_ORGANIZATION_ID
          value: 00000000-0000-0000-0000-000000000000
        - name: ANTHROPIC_SERVICE_ACCOUNT_ID
          value: svac_...
      volumeMounts:
        - name: anthropic-token
          mountPath: /var/run/secrets/anthropic.com
          readOnly: true
```

`serviceAccountToken` projection writes fresh JWT to mount path, rotates before `expirationSeconds` elapses. Token: `sub: system:serviceaccount:inference:inference-worker`, `aud: ["https://api.anthropic.com"]`.

## Configure Anthropic

### Issuer

- If issuer URL is publicly reachable → `discovery` mode (omit `jwks_keys`).
- If internal-only (e.g. `https://kubernetes.default.svc.cluster.local`) → `inline` mode. Fetch keys: `kubectl get --raw /openid/v1/jwks`. Paste contents of the returned `keys` array (not the `{"keys": [...]}` wrapper). In `inline` mode `issuer_url` is only string-compared against JWT `iss`; Anthropic never dials it.
- **Inline mode warning**: no automatic key refresh. When cluster rotates SA signing key, must update issuer or all exchanges fail signature verification (rare, typically only during cluster upgrades).

### Rule

Match `subject_prefix: system:serviceaccount:inference:inference-worker` + `audience: https://api.anthropic.com`. Loosen to `system:serviceaccount:inference:*` only if every SA in namespace should map to same Anthropic SA.

## Acquisition

Pod spec sets all 4 env vars; SDK reads from disk on every exchange and refreshes auto.

## Verification + scope hardening

- Most common K8s failure: JWKS key mismatch — for `inline`, re-fetch with `kubectl get --raw /openid/v1/jwks` and update issuer.
- Scope: pin namespace + SA name (no trailing `*`); **always set audience** on rule and matching one on pod's `serviceAccountToken` projection (otherwise default-audience tokens — which every pod has — match); separate rule per namespace; scope inline-JWKS issuers to one cluster.
