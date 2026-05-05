---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/oauth.md
source_url: https://ai.google.dev/gemini-api/docs/oauth
title: "Gemini API — OAuth Authentication"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API OAuth Authentication

Source is in Traditional Chinese (crawler localization).

## Overview

For stricter access control beyond API keys, use OAuth. This guide covers OAuth setup for testing environments (not full production setup).

## When to Use OAuth vs. API Key

- **API key**: Simplest, recommended for most use cases
- **OAuth**: When stricter access control is needed (user-scoped permissions, enterprise scenarios)

## Setup Steps

### 1. Enable the API
Enable Google Generative Language API in Google Cloud Console.

### 2. Configure OAuth Consent Screen
Set up OAuth consent screen in Google Cloud Console → Google Auth Platform → Overview. Add yourself as a test user.

### 3. Create OAuth 2.0 Credentials
Create OAuth 2.0 client credentials (Desktop app type for local testing).

### 4. Configure Application Default Credentials
```bash
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever"
```

### 5. Use in Code
OAuth credentials are auto-detected by the `google-genai` client when no API key is set.

## Prerequisites

- Google Cloud project
- gcloud CLI installed locally

## Notes

- For production, review authentication and authorization best practices.
- API key is almost always simpler and sufficient.
- OAuth is mainly needed for user-scoped operations (e.g., accessing user-specific resources, Workspace integration).
