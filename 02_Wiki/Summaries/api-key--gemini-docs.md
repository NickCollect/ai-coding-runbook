---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/api-key.md
source_url: https://ai.google.dev/gemini-api/docs/api-key
title: "Gemini API — API Keys"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Keys

Source is in Arabic (crawler localization).

## Overview

Gemini API requires an API key. Create and manage keys in Google AI Studio.

## Setup

1. Create/view API keys: `aistudio.google.com/app/apikey`
2. Set as environment variable: `GEMINI_API_KEY`
3. Or pass explicitly when initializing the client

## Usage

```python
# Environment variable (recommended)
# Set: export GEMINI_API_KEY="your-key"
client = genai.Client()  # auto-reads from env

# Explicit (temporary testing only)
client = genai.Client(api_key="your-key")
```

## Google Cloud Projects

- Each API key is linked to a Google Cloud project.
- AI Studio provides a simplified UI for managing Cloud projects.
- New users: AI Studio auto-creates a default project and key.
- Existing Cloud users: must import projects via the Projects dashboard.

## Limits (in AI Studio)

- Max 10 projects created at a time from AI Studio.
- Projects and Keys pages show max 100 keys / 50 projects.
- Only API keys with no restrictions or restricted to Generative Language API are shown.
- For advanced management (editing/restricting keys), go to Google Cloud Console Credentials page.

## Importing Cloud Projects

Search by project name or ID in the "Import Projects" dialog in AI Studio. After importing, create an API key for that project.

## Available Regions

API key access is limited to supported regions. See `available-regions.md` for the full list.
