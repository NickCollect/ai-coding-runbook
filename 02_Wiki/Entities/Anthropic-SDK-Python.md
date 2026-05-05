---
type: entity
name: Anthropic-SDK-Python
aliases: [anthropic Python SDK / pip install anthropic / anthropic-sdk-python]
category: sdk
status: ga
created: 2026-05-05
---

## 一句话定义

Anthropic Python 客户端 —— `pip install anthropic`，访问 Claude API；与 [[Agent-SDK]] 区分（Agent SDK 是更高层 agent harness，Anthropic SDK 是底层 REST client）。

## 关键属性

- **Install**：`pip install anthropic`，需 Python 3.9+；MIT-licensed [[README--anthropic-sdk-py]]
- **基本用法**：
  ```python
  from anthropic import Anthropic
  client = Anthropic(api_key=...)  # 默认读 ANTHROPIC_API_KEY env
  client.messages.create(max_tokens=1024, messages=[{"role": "user", "content": "Hello"}], model="claude-opus-4-6")
  ```
- **Streaming helpers**：`with client.messages.stream(...) as s: for text in s.text_stream`，`s.get_final_message()` 累积 [[helpers--anthropic-sdk-py]] [[Streaming-API]]
- **MCP helpers**：见 `helpers.md`
- **Tool runner**：`@beta_tool` / `@beta_async_tool` decorator 自动从函数 args + docstring 提 JSON schema [[Tool-runner]] [[helpers--anthropic-sdk-py]]
- **Memory tool helper**：`BetaAbstractMemoryTool` 接 file/DB/cloud backend [[Memory-tool]]
- **Beta features**：beta endpoints 通过 `client.beta.messages.create(...)` / `client.beta.files.*` 等
- **Sync + async**：`Anthropic` + `AsyncAnthropic`，async 用 `@beta_async_tool` decorator
- **完整 docs**：`platform.claude.com/docs/en/api/sdks/python` + repo 内 `api.md` / `helpers.md` / `tools.md` / `CONTRIBUTING.md` [[README--anthropic-sdk-py]] [[api--anthropic-sdk-py]] [[helpers--anthropic-sdk-py]] [[tools--anthropic-sdk-py]]
- **CHANGELOG**：repo 内 [[CHANGELOG--anthropic-sdk-py]]
- **Foundry support**：`src/anthropic/lib/foundry.md` 描述 Microsoft Foundry 接入 [[foundry--anthropic-sdk-py]]
- **vs [[Agent-SDK]]**：
  - Agent SDK = `claude_agent_sdk`，**Claude Code 同款 harness**（含 hooks / skills / subagent / plugin / permission mode）
  - Anthropic SDK = `anthropic`，**raw API client**（你自己实现 agent loop）
- **Repo**：`anthropics/anthropic-sdk-python`

## 出现来源

_21 summaries reference this entity_ ——
- [[README--anthropic-sdk-py]] / [[api--anthropic-sdk-py]] / [[helpers--anthropic-sdk-py]] / [[tools--anthropic-sdk-py]] / [[foundry--anthropic-sdk-py]] / [[CHANGELOG--anthropic-sdk-py]] / [[CONTRIBUTING--anthropic-sdk-py]] / [[SECURITY--anthropic-sdk-py]] / [[examples-greeting-SKILL--anthropic-sdk-py]]
- [[streaming--bwc]] / [[get-started--platform]] / [[intro--platform]] / [[tool-runner--at]] / [[memory-tool--at]] / [[create--msg-api]]

## 相关

- [[Agent-SDK]] —— 高层 agent harness（不同 product）
- [[Anthropic-SDK-TypeScript]] —— TS 等价
- [[Tool-runner]] —— SDK 内的 agentic loop helper
- [[Memory-tool]] —— 配 `BetaAbstractMemoryTool`
- [[Messages-API]] / [[Streaming-API]] / [[Files-API]] / [[Batches-API]] / [[MCP-server]] —— SDK 暴露的 features
- [[Enterprise-gateway]] —— Foundry / Bedrock / Vertex 接入
