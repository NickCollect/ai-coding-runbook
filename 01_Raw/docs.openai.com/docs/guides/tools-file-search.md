# File search

<!-- source: https://platform.openai.com/docs/guides/tools-file-search -->

File search is a hosted tool (managed by OpenAI) available in the Responses API. It enables models to retrieve information from a knowledge base of previously uploaded files through semantic and keyword search via **vector stores**.

You don't need to implement code to handle its execution — when the model decides to use it, it automatically calls the tool, retrieves information, and returns output.

## Setup: create a vector store and upload files

1. Upload the file to the File API
2. Create a vector store
3. Add the file to the vector store
4. Check status (poll until `status: "completed"`)

## Use file search in a response

```python
response = client.responses.create(
    model="gpt-5.5",
    input="What is deep research by OpenAI?",
    tools=[{
        "type": "file_search",
        "vector_store_ids": ["<vector_store_id>"]
    }]
)
```

Response includes two outputs:
1. `file_search_call` — ID of the file search call
2. `message` — model response with file citations in `content[0].annotations`

## Retrieval customization

- **Limit results**: Customize number of results to reduce token usage and latency (may reduce quality)
- **Include search results**: Use `include` parameter to get search results alongside the response
- **Metadata filtering**: Filter by file attributes (set attributes when uploading, define filters in query)

## Supported file formats

.c, .cpp, .cs, .css, .doc, .docx, .go, .html, .java, .js, .json, .md, .pdf, .php, .pptx, .py, .rb, .sh, .tex, .ts, .txt

For `text/` MIME types, encoding must be utf-8, utf-16, or ascii.

## Rate limits

| Tier | Rate limit |
|---|---|
| Tier 1 | 100 RPM |
| Tier 2 and 3 | 500 RPM |
| Tier 4 and 5 | 1000 RPM |

## vs. Assistants API

File search in the Responses API is the modern replacement for the Assistants API file search. Use Responses API for new integrations.
