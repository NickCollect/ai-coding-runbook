---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/ruby/claude-api.md
title: "claude-api skill: Ruby SDK reference"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: [Tool-use, Prompt-caching]
---

Ruby SDK reference inside the `claude-api` skill. Official Ruby SDK supports Claude API + beta tool runner via `client.beta.messages.tool_runner()`. Agent SDK NOT yet available for Ruby.

**Install**: `gem install anthropic`.

**Client**: `Anthropic::Client.new` (uses `ANTHROPIC_API_KEY`) or `Anthropic::Client.new(api_key: "...")`.

**Basic message**: `client.messages.create(model: :"claude-opus-4-7", max_tokens: 16000, messages: [{role: "user", content: "..."}])`. Content is array of polymorphic blocks. **`.type` is a Symbol — compare with `:text` not `"text"`**. `.text` raises `NoMethodError` on non-TextBlock. Always guard:
```ruby
message.content.each { |block| puts block.text if block.type == :text }
```

**Streaming**: `client.messages.stream(...)` returns object with `.text.each { |t| print(t) }` for incremental output.

**Tool runner (beta)**: define `GetWeatherInput < Anthropic::BaseModel` with `required :location, String, doc: "..."`. Tool class extends `Anthropic::BaseTool`, has `doc "..."`, `input_schema GetWeatherInput`, and `def call(input); ...; end`. Use via `client.beta.messages.tool_runner(...).each_message do |message|`.

**Manual loop**: see `shared/tool-use-concepts.md` for pattern.

**Prompt caching**: `system_:` (trailing underscore — avoids `Kernel#system` shadow). Takes array of text blocks; `cache_control` on last. Plain hashes work via `OrHash` type alias. 1h TTL: `cache_control: { type: "ephemeral", ttl: "1h" }`. Top-level `cache_control:` on `messages.create` auto-places. Verify: `message.usage.cache_creation_input_tokens` / `cache_read_input_tokens`.
