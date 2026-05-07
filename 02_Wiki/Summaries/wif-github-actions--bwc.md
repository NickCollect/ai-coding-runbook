---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/wif-providers/github-actions.md
source_url: https://platform.claude.com/docs/en/build-with-claude/wif-providers/github-actions
title: "Use WIF with GitHub Actions"
summarized_at: 2026-05-07
entities_referenced: [Workload-Identity-Federation, Service-account, Federation-issuer, Federation-rule, API-key]
concepts_referenced: [JWT]
---

Every GitHub Actions workflow run can request a signed identity token from GitHub's hosted issuer at `https://token.actions.githubusercontent.com`. WIF lets workflow exchange it for short-lived Anthropic access token — no `ANTHROPIC_API_KEY` secret stored in repo.

## Token `sub` claim formats

- Branch push: `repo:<owner>/<repo>:ref:refs/heads/<branch>`
- Pull request: `repo:<owner>/<repo>:pull_request`
- Environment-gated deploy: `repo:<owner>/<repo>:environment:<name>`

Federation rule matches on this claim plus `repository_owner`, `ref`, etc.

## Configure workflow

Workflow / job needs `id-token: write` permission:

```yaml
permissions:
  id-token: write
  contents: read
```

Job runner exposes `ACTIONS_ID_TOKEN_REQUEST_URL` and `ACTIONS_ID_TOKEN_REQUEST_TOKEN`. Call request URL with request token as bearer + audience query param, write returned JWT to file:

```bash
curl -sS -H "Authorization: Bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" \
  "$ACTIONS_ID_TOKEN_REQUEST_URL&audience=https://api.anthropic.com" \
  | jq -r .value > /tmp/gha-jwt
```

Or in JavaScript via `actions/github-script@v8`: `core.getIDToken('https://api.anthropic.com')`.

Decoded token includes `iss`, `sub`, `aud`, `repository`, `repository_owner`, `ref`, `sha`, `workflow`, `actor`, `event_name`. See [GitHub's OIDC subject claim reference](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-subject-claims) for full `sub` formats.

## Configure Anthropic

- **Issuer**: `issuer_url: https://token.actions.githubusercontent.com`, `jwks_source: discovery` (GitHub publishes discovery + JWKS publicly; Anthropic auto-refreshes when GitHub rotates keys).
- **Rule**: match `subject_prefix` for narrowest scope (e.g., `repo:your-org/your-repo:ref:refs/heads/main`), `audience: https://api.anthropic.com`, and `claims.repository_owner` as defense in depth.

## Acquisition

Workflow sets 4 env vars (`ANTHROPIC_FEDERATION_RULE_ID/_ORGANIZATION_ID/_SERVICE_ACCOUNT_ID/_IDENTITY_TOKEN_FILE`). `Anthropic()` zero-arg client picks up federation, exchanges JWT on first request, refreshes before expiry.

## Token lifetime quirk

GitHub-issued identity token expires ~5 minutes after issuance. The token-request endpoint stays valid for entire job — can fetch fresh token any time. SDK exchanges on first use and caches Anthropic access token. For jobs longer than Anthropic token lifetime, SDK re-reads `ANTHROPIC_IDENTITY_TOKEN_FILE` on each refresh — re-run the fetch step periodically (or in background loop) to keep file current. Alternative: pass token-provider callback that calls `ACTIONS_ID_TOKEN_REQUEST_URL` directly.

## Verification + scope hardening

- Most common GitHub Actions failure: `sub` claim format mismatch (trailing segment varies between `ref:...`, `environment:...`, `pull_request`).
- Scope: pin to single repo (`subject_prefix: repo:your-org/your-repo:*`); pin to protected branch (`claims.ref: refs/heads/main` so PR runs and feature branches don't match); pin `repository_owner` defense in depth; pin to deployment environment for deploy jobs (gate that environment with required reviewers in GitHub).
- **Critical warning**: a `subject_prefix: repo:your-org/*` alone matches every repo in org, **and without a `ref` constraint also matches `pull_request` runs from forks** — anyone who can open a PR against a matching repo could obtain a federated token.
