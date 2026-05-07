---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/wif-providers/aws.md
source_url: https://platform.claude.com/docs/en/build-with-claude/wif-providers/aws
title: "Use WIF with AWS"
summarized_at: 2026-05-07
entities_referenced: [Workload-Identity-Federation, Service-account, Federation-issuer, Federation-rule, Workspace]
concepts_referenced: [JWT]
---

AWS workloads (Lambda, EC2, ECS, EKS) can authenticate to Claude API without static keys via two paths.

## Path 1 (recommended): STS web identity tokens

Works on Lambda/EC2/ECS/EKS using ambient AWS credentials. Calls AWS STS `GetWebIdentityToken` API, returns OIDC token signed by AWS asserting caller's IAM identity.

### Configure AWS

1. **Enable outbound web identity federation** on the account (off by default; account-level flag in **IAM → Account settings**, or `boto3.client('iam').enable_outbound_web_identity_federation()`). If not enabled, `OutboundWebIdentityFederationDisabledException`.
2. **IAM permission**: attach policy to workload's IAM role allowing `sts:GetWebIdentityToken` on `Resource: *`.
3. **Find STS issuer URL**: appears in **IAM → Account settings → Get Token Issuer URL** as `https://<uuid>.tokens.sts.global.api.aws` (per-account). Or via `boto3.client('iam').get_outbound_web_identity_federation_info()`.

### Configure Anthropic (issuer + rule)

- Issuer: per-account STS URL with `discovery` mode (public JWKS).
- Rule: match `subject_prefix` = full IAM role ARN (`arn:aws:iam::<account>:role/<role-name>`), `audience: https://api.anthropic.com`. Token also carries `https://sts.amazonaws.com/` claim with `aws_account`, `org_id`, `principal_id`, plus any `request_tags` — match via `claims` map or CEL `condition`.

### Token acquisition

`aws sts get-web-identity-token --region us-east-1 --audience "https://api.anthropic.com" --signing-algorithm RS256 --duration-seconds 900`. SDK token-provider is a callable; SDK re-invokes STS on each refresh. **Note**: `GetWebIdentityToken` available only on regional STS endpoints — pin with `region_name`.

## Path 2: EKS projected service-account tokens

For pods running in EKS. Skip the STS call; read Kubernetes-projected SA token from disk. Two fewer config steps than STS but only works inside a pod. Same mechanism as generic Kubernetes integration. Requires EKS cluster with [IAM OIDC provider enabled](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html).

### Configure EKS

1. **Find OIDC issuer URL**: `aws eks describe-cluster --name <cluster> --query "cluster.identity.oidc.issuer"`. Format: `https://oidc.eks.us-west-2.amazonaws.com/id/<id>`. Register one issuer per cluster.
2. **Create SA + project Anthropic-audience token**: EKS pod identity webhook auto-projects an IRSA token with `aud: sts.amazonaws.com` (for AWS, exposed at `AWS_WEB_IDENTITY_TOKEN_FILE`). For Anthropic, project a **second** token with `audience: https://api.anthropic.com` at a separate mount path.

```yaml
volumes:
  - name: anthropic-token
    projected:
      sources:
        - serviceAccountToken:
            audience: https://api.anthropic.com
            expirationSeconds: 3600
            path: token
```

3. **Token claims**: `sub` follows `system:serviceaccount:<namespace>:<service-account-name>`; `aud` is `https://api.anthropic.com`. Don't reuse the IRSA default `sts.amazonaws.com` token.

### Configure Anthropic

- Issuer: per-cluster EKS URL with `discovery` mode (public JWKS).
- Rule: `subject_prefix: system:serviceaccount:inference:inference-worker`, `audience: https://api.anthropic.com`.

### Acquisition

Pod spec sets all four env vars (`ANTHROPIC_IDENTITY_TOKEN_FILE`, `_RULE_ID`, `_ORGANIZATION_ID`, `_SERVICE_ACCOUNT_ID`); SDK constructed with no args reads from env.

## Verification + scope hardening

- Verify: exchange STS-issued JWT directly via `curl POST /v1/oauth/token`; success returns `sk-ant-oat01-` token.
- Most common AWS STS failure: `iss` mismatch (per-account URL must match registered `issuer_url` exactly).
- Most common EKS failure: projected token's `aud` doesn't match (project with `audience: https://api.anthropic.com`, not IRSA default).
- Scope: pin full role ARN (no trailing `*`); pin `aws_account` claim as defense in depth; pin namespace + SA on EKS; separate rule per environment.
