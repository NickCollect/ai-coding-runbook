---
type: summary
source: 01_Raw/docs.cursor.com/docs--agent--tools--search.md
source_url: https://cursor.com/docs/agent/tools/search
title: "Semantic & Agentic Search"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Agent 组合使用精确匹配和语义搜索两种策略，根据提示词自动选择最优工具，找到代码库中的相关代码。

**Instant Grep**：精确匹配（函数名、变量名、错误字符串、正则），Cursor 自研搜索引擎，大型代码库性能优于 ripgrep，自动启用无需配置。

**语义搜索**：用自然语言描述意图，通过向量嵌入找到含义相关但字面不匹配的代码（研究表明比单独用 grep 准确率高 12.5%，在 1000+ 文件代码库提升最显著）。工作区打开时自动开始索引，达到 80% 时可用，每 5 分钟自动同步变更文件。

**隐私**：文件路径加密传输，代码内容仅在内存中处理后丢弃，从不以明文存储；客户端侧解密。索引超过 6 周不活跃后删除。

**工具选择逻辑**：已知符号/字符串 → Grep；概念/行为 → 语义搜索 + Grep；复杂探索 → 多轮搜索链式调用。

**Explore Subagent**：Agent 可生成独立的 Explore 子 Agent，在独立上下文窗口中用更快的模型执行大量并行搜索，只返回相关结果摘要，避免污染主对话上下文。
