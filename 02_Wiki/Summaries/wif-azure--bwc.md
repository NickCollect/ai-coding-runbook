---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/wif-providers/azure.md
source_url: https://platform.claude.com/docs/en/build-with-claude/wif-providers/azure
title: "Use WIF with Microsoft Azure"
summarized_at: 2026-05-07
entities_referenced: [Workload-Identity-Federation, Service-account, Federation-issuer, Federation-rule, Workspace]
concepts_referenced: [JWT]
---

Azure workloads authenticate to Claude API by presenting a Microsoft Entra ID-issued JWT, then exchanging for an Anthropic access token. Two ways to obtain the Entra-issued token.

## Two acquisition paths

- **Managed identity** (VMs, App Service, Functions, Container Apps): workload calls Azure IMDS at `http://169.254.169.254/metadata/identity/oauth2/token` for a JWT for assigned identity.
- **Entra Workload Identity** (AKS pods): Kubernetes projects an SA token (signed by AKS cluster's OIDC issuer) into pod at `AZURE_FEDERATED_TOKEN_FILE`. Workload exchanges that at Entra for an Entra-issued access token (two-hop).

In both paths the Entra-issued token has tenant-specific issuer `https://login.microsoftonline.com/<TENANT_ID>/v2.0` and carries managed identity's object ID in `sub` and `oid` claims.

(Alternative: AKS pods can skip Entra and present K8s-projected token directly — registers AKS cluster's OIDC issuer with Anthropic instead. See Kubernetes guide.)

## Configure Azure

### VM/App Service/Functions/Container Apps

Enable system-assigned or user-assigned managed identity on Azure resource. Note its **Object (principal) ID** — appears as both `sub` and `oid` claims. IMDS reachable at `169.254.169.254` from inside resource. No further Azure config.

### Entra Workload Identity (AKS)

1. Enable OIDC issuer + workload identity: `az aks update --enable-oidc-issuer --enable-workload-identity ...`.
2. Deploy `azure-workload-identity` mutating webhook.
3. Create user-assigned managed identity + federated credential trusting cluster's OIDC issuer for K8s SA.
4. Label pod `azure.workload.identity/use: "true"`, set `serviceAccountName` to federated SA. Webhook injects `AZURE_FEDERATED_TOKEN_FILE`, `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`.

## Token claims

```json
{
  "iss": "https://login.microsoftonline.com/<TENANT_ID>/v2.0",
  "sub": "<oid>",
  "aud": "https://api.anthropic.com",
  "oid": "<oid>",
  "tid": "<TENANT_ID>",
  "azp": "<CLIENT_ID>"
}
```

`sub` and `oid` identical (managed identity's object ID). `azp` = app/client ID. Match `oid` to authorize one identity, or `azp` for any identity tied to an app registration. `tid` matching = defense in depth (issuer URL already pins tenant).

## Configure Anthropic

- **Issuer**: per-tenant URL `https://login.microsoftonline.com/<TENANT_ID>/v2.0`, `jwks_source: discovery`. Each tenant federated needs own issuer record. Note: depending on token version, `iss` may be `https://sts.windows.net/<TENANT_ID>/` instead — register whichever your decoded token contains. Both share JWKS, discovery works for either.
- **Rule**: match `audience: https://api.anthropic.com` plus `claims.oid` (managed identity object ID) + `claims.tid` (tenant ID).

## Acquisition

SDK-callable token-provider that hits IMDS and returns `access_token` from JSON response. AKS Entra path is two-hop: read `AZURE_FEDERATED_TOKEN_FILE`, POST to `https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/token` with `grant_type=client_credentials` + `scope=https://api.anthropic.com/.default` + `client_assertion=<federated-token>`, take returned Entra `access_token`, then standard Anthropic exchange.

## Verification + scope hardening

- Most common Azure failure: `issuer_url` mismatch with `iss` claim. Decode token to confirm. For managed identity: either `https://login.microsoftonline.com/<TENANT_ID>/v2.0` or `https://sts.windows.net/<TENANT_ID>/`.
- Scope: match `oid` exactly (Azure `oid` is GUID with no stable prefix — never use `subject_prefix` with `*`); pin `tid` defense in depth; pin audience; one rule per managed identity.
