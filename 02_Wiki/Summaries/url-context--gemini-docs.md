---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/url-context.md
source_url: https://ai.google.dev/gemini-api/docs/url-context
title: "Gemini API — URL Context Tool"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API URL Context Tool

Source is in Simplified Chinese (crawler localization).

## Overview

URL Context tool lets you provide URLs for the model to fetch and analyze as additional context. Model accesses the web page content (unless restricted type) to inform and improve its response.

## Use Cases

- **Data extraction**: Extract prices, names, key findings from multiple URLs
- **Document comparison**: Analyze multiple reports/articles/PDFs to find differences and track trends
- **Content synthesis**: Combine information from multiple source URLs to generate accurate summaries, blog posts, or reports
- **Code and documentation analysis**: Point to GitHub repos or technical docs to explain code, generate setup instructions, answer questions

## Usage

```python
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()

tools = [{"url_context": {}}]
url1 = "https://www.foodnetwork.com/recipes/perfect-roast-chicken"
url2 = "https://www.allrecipes.com/recipe/simple-roast-chicken"

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(tools=tools)
)
print(response.text)
```

## Limitations

- Some URL types are restricted (dynamic pages, paywalled content, login-required pages, etc.)
- Works best with publicly accessible, static web content

## Combination

Can be used together with Google Search Grounding — model can ground on search results AND specific provided URLs in the same request.

## Pricing

Billed as input tokens based on per-model pricing. Retrieved content (text from URLs) is charged as input tokens.
