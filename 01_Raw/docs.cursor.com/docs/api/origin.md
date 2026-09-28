---
source_url: https://cursor.com/docs/api/origin
fetched_at: 2026-09-28T06:10:41.166770+00:00
fetch_method: mintlify_md
---

# Cursor Origin API

> Early Beta reference for the Cursor Origin API. Origin is Cursor's code forge; its public REST API lets apps and tools work with Origin repositories, commits, checks, pull requests, apps, and installations.

The base URL for API requests is `https://api.cursor.com/v1/origin`. The Origin API is in Early Beta and subject to change.

Every link below is a Markdown page. Each reference section, endpoint, and webhook payload has its own page, named by its heading anchor on the web reference: the `#pagination` section is `/docs/api/origin/reference/pagination.md`.

## Docs

- [Full reference (Markdown)](https://cursor.com/docs/api/origin/llms-full.txt): The complete Origin API reference as a single Markdown file.
- [OpenAPI specification](https://cursor.com/docs/api/origin/openapi.yaml): Machine-readable OpenAPI 3.1 spec with request and response schemas.
- [Origin Migration API](https://cursor.com/docs/api/origin/migrations.md): Endpoints for migrating repositories between GitHub and Origin mirrors, called with a user access token.

## Guides

- [Overview](https://cursor.com/docs/api/origin/reference/overview.md)
- [Base URL](https://cursor.com/docs/api/origin/reference/base-url.md)
- [Protocol conventions](https://cursor.com/docs/api/origin/reference/protocol-conventions.md)
- [Preview](https://cursor.com/docs/api/origin/reference/preview.md)
- [Changelog](https://cursor.com/docs/api/origin/changelog.md)
- [Getting started](https://cursor.com/docs/api/origin/reference/getting-started.md)
- [Origin access](https://cursor.com/docs/api/origin/reference/origin-access.md)
- [Origin CLI](https://cursor.com/docs/api/origin/reference/origin-cli.md)
- [Installation](https://cursor.com/docs/api/origin/reference/installation.md)
- [Installation receipt](https://cursor.com/docs/api/origin/reference/installation-receipt.md)
- [Authentication](https://cursor.com/docs/api/origin/reference/authentication.md)
- [Generate an app signing key](https://cursor.com/docs/api/origin/reference/generate-an-app-signing-key.md)
- [App JWT](https://cursor.com/docs/api/origin/reference/app-jwt.md)
- [Installation access token](https://cursor.com/docs/api/origin/reference/installation-access-token.md)
- [Git HTTPS authentication](https://cursor.com/docs/api/origin/reference/git-https-authentication.md)
- [User-authenticated CLI requests](https://cursor.com/docs/api/origin/reference/user-authenticated-cli-requests.md)
- [Discovery and signing keys](https://cursor.com/docs/api/origin/reference/discovery-and-signing-keys.md)
- [Acting on Behalf of Users](https://cursor.com/docs/api/origin/acting-as-users.md)
- [Scopes](https://cursor.com/docs/api/origin/reference/scopes.md)
- [Mirrored repositories](https://cursor.com/docs/api/origin/reference/mirrored-repositories.md)
- [Rate limits](https://cursor.com/docs/api/origin/reference/rate-limits.md)
- [Response headers](https://cursor.com/docs/api/origin/reference/response-headers.md)
- [Exceeding the limit](https://cursor.com/docs/api/origin/reference/exceeding-the-limit.md)
- [Checking remaining quota](https://cursor.com/docs/api/origin/reference/checking-remaining-quota.md)
- [Common conventions](https://cursor.com/docs/api/origin/reference/common-conventions.md)
- [Pagination](https://cursor.com/docs/api/origin/reference/pagination.md)
- [Errors](https://cursor.com/docs/api/origin/reference/errors.md)
- [IDs](https://cursor.com/docs/api/origin/reference/ids.md)
- [Repository paths](https://cursor.com/docs/api/origin/reference/repository-paths.md)
- [Resource references](https://cursor.com/docs/api/origin/reference/resource-references.md)
- [Check runs](https://cursor.com/docs/api/origin/reference/check-runs.md)
- [Attempts and the current attempt](https://cursor.com/docs/api/origin/reference/attempts-and-the-current-attempt.md)
- [Ordering writes](https://cursor.com/docs/api/origin/reference/ordering-writes.md)
- [Timestamps and deadlines](https://cursor.com/docs/api/origin/reference/timestamps-and-deadlines.md)
- [Current limitations](https://cursor.com/docs/api/origin/reference/current-limitations.md)
- [Implementation checklist](https://cursor.com/docs/api/origin/reference/implementation-checklist.md)
- [Endpoint reference](https://cursor.com/docs/api/origin/reference/endpoint-reference.md)

## Apps and installations

- [Apps and installations](https://cursor.com/docs/api/origin/reference/apps-and-installations.md)
- [Get Rate Limit](https://cursor.com/docs/api/origin/reference/get-rate-limit.md)
- [Get Authenticated App](https://cursor.com/docs/api/origin/reference/get-authenticated-app.md)
- [List App Installations](https://cursor.com/docs/api/origin/reference/list-app-installations.md)
- [Get App Installation](https://cursor.com/docs/api/origin/reference/get-app-installation.md)
- [Delete App Installation](https://cursor.com/docs/api/origin/reference/delete-app-installation.md)
- [Create Installation Access Token](https://cursor.com/docs/api/origin/reference/create-installation-access-token.md)
- [Create Installation User Token](https://cursor.com/docs/api/origin/reference/create-installation-user-token.md)
- [List App Installation Repositories](https://cursor.com/docs/api/origin/reference/list-app-installation-repositories.md)
- [List Webhook Deliveries](https://cursor.com/docs/api/origin/reference/list-webhook-deliveries.md)
- [Batch Redeliver Webhook Deliveries](https://cursor.com/docs/api/origin/reference/batch-redeliver-webhook-deliveries.md)
- [Ping Webhook](https://cursor.com/docs/api/origin/reference/ping-webhook.md)
- [Get App](https://cursor.com/docs/api/origin/reference/get-app.md)
- [Update App](https://cursor.com/docs/api/origin/reference/update-app.md)
- [Add App Signing Key](https://cursor.com/docs/api/origin/reference/add-app-signing-key.md)
- [Revoke App Signing Key](https://cursor.com/docs/api/origin/reference/revoke-app-signing-key.md)
- [List Namespace Apps](https://cursor.com/docs/api/origin/reference/list-namespace-apps.md)
- [Create App](https://cursor.com/docs/api/origin/reference/create-app.md)
- [Add App Installation Repositories](https://cursor.com/docs/api/origin/reference/add-app-installation-repositories.md)

## Repositories

- [Repositories](https://cursor.com/docs/api/origin/reference/repositories.md)
- [List Namespaces](https://cursor.com/docs/api/origin/reference/list-namespaces.md)
- [List Repos](https://cursor.com/docs/api/origin/reference/list-repos.md)
- [Get Repo](https://cursor.com/docs/api/origin/reference/get-repo.md)
- [Update Repo](https://cursor.com/docs/api/origin/reference/update-repo.md)
- [Create Repo](https://cursor.com/docs/api/origin/reference/create-repo.md)
- [List Branches](https://cursor.com/docs/api/origin/reference/list-branches.md)
- [Get Repo Tarball](https://cursor.com/docs/api/origin/reference/get-repo-tarball.md)
- [Sync Mirror](https://cursor.com/docs/api/origin/reference/sync-mirror.md)

## Checks

- [Checks](https://cursor.com/docs/api/origin/reference/checks.md)
- [Post Check Run](https://cursor.com/docs/api/origin/reference/post-check-run.md)
- [Batch Upsert Check Runs](https://cursor.com/docs/api/origin/reference/batch-upsert-check-runs.md)
- [Get Check Run](https://cursor.com/docs/api/origin/reference/get-check-run.md)
- [List Check Run Annotations](https://cursor.com/docs/api/origin/reference/list-check-run-annotations.md)
- [Create Check Run Annotations](https://cursor.com/docs/api/origin/reference/create-check-run-annotations.md)
- [Rerequest Check Run](https://cursor.com/docs/api/origin/reference/rerequest-check-run.md)
- [Get Check Suite](https://cursor.com/docs/api/origin/reference/get-check-suite.md)
- [List Check Runs For Suite](https://cursor.com/docs/api/origin/reference/list-check-runs-for-suite.md)
- [List Check Runs For Commit](https://cursor.com/docs/api/origin/reference/list-check-runs-for-commit.md)
- [List Check Suites For Commit](https://cursor.com/docs/api/origin/reference/list-check-suites-for-commit.md)

## Commits and contents

- [Commits and contents](https://cursor.com/docs/api/origin/reference/commits-and-contents.md)
- [List Commits](https://cursor.com/docs/api/origin/reference/list-commits.md)
- [Get Commit](https://cursor.com/docs/api/origin/reference/get-commit.md)
- [List Commit Files](https://cursor.com/docs/api/origin/reference/list-commit-files.md)
- [Compare Commits](https://cursor.com/docs/api/origin/reference/compare-commits.md)
- [List Comparison Files](https://cursor.com/docs/api/origin/reference/list-comparison-files.md)
- [Get Contents](https://cursor.com/docs/api/origin/reference/get-contents.md)
- [Batch Get Contents](https://cursor.com/docs/api/origin/reference/batch-get-contents.md)
- [Grep Contents](https://cursor.com/docs/api/origin/reference/grep-contents.md)

## Git data

- [Git data](https://cursor.com/docs/api/origin/reference/git-data.md)
- [Get Blob](https://cursor.com/docs/api/origin/reference/get-blob.md)
- [Get Git Commit](https://cursor.com/docs/api/origin/reference/get-git-commit.md)
- [Create Commit From Files](https://cursor.com/docs/api/origin/reference/create-commit-from-files.md)
- [Get Git Ref](https://cursor.com/docs/api/origin/reference/get-git-ref.md)
- [Create Git Ref](https://cursor.com/docs/api/origin/reference/create-git-ref.md)
- [Delete Git Ref](https://cursor.com/docs/api/origin/reference/delete-git-ref.md)
- [List Matching Git Refs](https://cursor.com/docs/api/origin/reference/list-matching-git-refs.md)
- [List Matching Git Refs by Path](https://cursor.com/docs/api/origin/reference/list-matching-git-refs-by-path.md)
- [Get Tag](https://cursor.com/docs/api/origin/reference/get-tag.md)
- [Get Tree](https://cursor.com/docs/api/origin/reference/get-tree.md)

## Grants

- [Grants](https://cursor.com/docs/api/origin/reference/grants.md)
- [List Repository Grants](https://cursor.com/docs/api/origin/reference/list-repository-grants.md)
- [Upsert Repository Grant](https://cursor.com/docs/api/origin/reference/upsert-repository-grant.md)
- [Delete Repository Grant](https://cursor.com/docs/api/origin/reference/delete-repository-grant.md)
- [List Namespace Grants](https://cursor.com/docs/api/origin/reference/list-namespace-grants.md)
- [Upsert Namespace Grant](https://cursor.com/docs/api/origin/reference/upsert-namespace-grant.md)
- [Delete Namespace Grant](https://cursor.com/docs/api/origin/reference/delete-namespace-grant.md)

## Grants concepts

- [Grants concepts](https://cursor.com/docs/api/origin/grants-api.md)

## Labels

- [Labels](https://cursor.com/docs/api/origin/reference/labels.md)
- [List Labels](https://cursor.com/docs/api/origin/reference/list-labels.md)
- [Create Label](https://cursor.com/docs/api/origin/reference/create-label.md)
- [Get Label](https://cursor.com/docs/api/origin/reference/get-label.md)
- [Delete Label](https://cursor.com/docs/api/origin/reference/delete-label.md)
- [Update Label](https://cursor.com/docs/api/origin/reference/update-label.md)

## Pull requests

- [Pull requests](https://cursor.com/docs/api/origin/reference/pull-requests.md)
- [List Pull Requests](https://cursor.com/docs/api/origin/reference/list-pull-requests.md)
- [Get Pull Request](https://cursor.com/docs/api/origin/reference/get-pull-request.md)
- [Create Pull Request](https://cursor.com/docs/api/origin/reference/create-pull-request.md)
- [Update Pull Request](https://cursor.com/docs/api/origin/reference/update-pull-request.md)
- [List Pull Request Comments](https://cursor.com/docs/api/origin/reference/list-pull-request-comments.md)
- [Get Pull Request Comment](https://cursor.com/docs/api/origin/reference/get-pull-request-comment.md)
- [Delete Pull Request Comment](https://cursor.com/docs/api/origin/reference/delete-pull-request-comment.md)
- [Create Pull Request Comment](https://cursor.com/docs/api/origin/reference/create-pull-request-comment.md)
- [Update Pull Request Comment](https://cursor.com/docs/api/origin/reference/update-pull-request-comment.md)
- [Update Pull Request Thread](https://cursor.com/docs/api/origin/reference/update-pull-request-thread.md)
- [List Pull Request Commits](https://cursor.com/docs/api/origin/reference/list-pull-request-commits.md)
- [List Pull Request Files](https://cursor.com/docs/api/origin/reference/list-pull-request-files.md)
- [List Pull Request Labels](https://cursor.com/docs/api/origin/reference/list-pull-request-labels.md)
- [Set Pull Request Labels](https://cursor.com/docs/api/origin/reference/set-pull-request-labels.md)
- [Add Pull Request Labels](https://cursor.com/docs/api/origin/reference/add-pull-request-labels.md)
- [Remove All Pull Request Labels](https://cursor.com/docs/api/origin/reference/remove-all-pull-request-labels.md)
- [Remove Pull Request Label](https://cursor.com/docs/api/origin/reference/remove-pull-request-label.md)
- [Merge Pull Request](https://cursor.com/docs/api/origin/reference/merge-pull-request.md)
- [Get Pull Request Mergeability](https://cursor.com/docs/api/origin/reference/get-pull-request-mergeability.md)
- [List Pull Request Requested Reviewers](https://cursor.com/docs/api/origin/reference/list-pull-request-requested-reviewers.md)
- [Request Pull Request Reviewers](https://cursor.com/docs/api/origin/reference/request-pull-request-reviewers.md)
- [Remove Pull Request Requested Reviewers](https://cursor.com/docs/api/origin/reference/remove-pull-request-requested-reviewers.md)
- [List Pull Request Reviews](https://cursor.com/docs/api/origin/reference/list-pull-request-reviews.md)
- [Create Pull Request Review](https://cursor.com/docs/api/origin/reference/create-pull-request-review.md)
- [Update Pull Request Review](https://cursor.com/docs/api/origin/reference/update-pull-request-review.md)
- [Dismiss Pull Request Review](https://cursor.com/docs/api/origin/reference/dismiss-pull-request-review.md)

## Rulesets

- [Rulesets](https://cursor.com/docs/api/origin/reference/rulesets.md)
- [List Rulesets](https://cursor.com/docs/api/origin/reference/list-rulesets.md)
- [Create Ruleset](https://cursor.com/docs/api/origin/reference/create-ruleset.md)
- [Get Ruleset](https://cursor.com/docs/api/origin/reference/get-ruleset.md)
- [Update Ruleset](https://cursor.com/docs/api/origin/reference/update-ruleset.md)
- [Delete Ruleset](https://cursor.com/docs/api/origin/reference/delete-ruleset.md)

## SSH certificate authorities

- [SSH certificate authorities](https://cursor.com/docs/api/origin/reference/ssh-certificate-authorities.md)
- [List SSH Certificate Authorities](https://cursor.com/docs/api/origin/reference/list-ssh-certificate-authorities.md)
- [Add SSH Certificate Authority](https://cursor.com/docs/api/origin/reference/add-ssh-certificate-authority.md)
- [Delete SSH Certificate Authority](https://cursor.com/docs/api/origin/reference/delete-ssh-certificate-authority.md)
- [Set SSH Certificate Requirement](https://cursor.com/docs/api/origin/reference/set-ssh-certificate-requirement.md)

## Webhooks

- [Webhooks](https://cursor.com/docs/api/origin/reference/webhooks.md)
- [Headers](https://cursor.com/docs/api/origin/reference/headers.md)
- [Signature verification](https://cursor.com/docs/api/origin/reference/signature-verification.md)
- [Delivery envelope](https://cursor.com/docs/api/origin/reference/delivery-envelope.md)
- [Retries](https://cursor.com/docs/api/origin/reference/retries.md)
- [Automatic disable](https://cursor.com/docs/api/origin/reference/automatic-disable.md)
- [Recovery](https://cursor.com/docs/api/origin/reference/recovery.md)

## Webhooks reference

- [Webhooks reference](https://cursor.com/docs/api/origin/reference/webhooks-reference.md)
- [Events](https://cursor.com/docs/api/origin/reference/events.md)
- [Event payloads](https://cursor.com/docs/api/origin/reference/event-payloads.md)
- [Repository Created](https://cursor.com/docs/api/origin/reference/repository-created.md)
- [Repository Deleted](https://cursor.com/docs/api/origin/reference/repository-deleted.md)
- [Repository Push](https://cursor.com/docs/api/origin/reference/repository-push.md)
- [Repository Metadata Updated](https://cursor.com/docs/api/origin/reference/repository-metadata-updated.md)
- [Pull Request Events](https://cursor.com/docs/api/origin/reference/pull-request-events.md)
- [Pull Request Label Events](https://cursor.com/docs/api/origin/reference/pull-request-label-events.md)
- [Pull Request Comment](https://cursor.com/docs/api/origin/reference/pull-request-comment.md)
- [Pull Request Comment Reaction Events](https://cursor.com/docs/api/origin/reference/pull-request-comment-reaction-events.md)
- [Pull Request Review Events](https://cursor.com/docs/api/origin/reference/pull-request-review-events.md)
- [Pull Request Reviewer Events](https://cursor.com/docs/api/origin/reference/pull-request-reviewer-events.md)
- [Check Run Events](https://cursor.com/docs/api/origin/reference/check-run-events.md)
- [Check Run Rerequested](https://cursor.com/docs/api/origin/reference/check-run-rerequested.md)
- [Installation Created](https://cursor.com/docs/api/origin/reference/installation-created.md)
- [Installation Updated](https://cursor.com/docs/api/origin/reference/installation-updated.md)
- [Installation Suspended](https://cursor.com/docs/api/origin/reference/installation-suspended.md)
- [Installation Unsuspended](https://cursor.com/docs/api/origin/reference/installation-unsuspended.md)
- [Installation Deleted](https://cursor.com/docs/api/origin/reference/installation-deleted.md)
- [Check Run Annotations](https://cursor.com/docs/api/origin/reference/check-run-annotations.md)


---

## Sitemap

[Origin API docs index](https://cursor.com/docs/api/origin/llms.txt)
