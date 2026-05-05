---
type: summary
source: 01_Raw/docs.cursor.com/docs--cli--headless.md
source_url: https://cursor.com/docs/cli/headless
title: "Headless CLI（脚本/自动化使用）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

在脚本和自动化工作流中使用 Cursor CLI 进行代码分析、生成和重构，核心是 print 模式 (`-p`)。

**关键 flag**：`-p/--print`（非交互 print 模式）；`--force`/`--yolo`（允许实际修改文件，不加则只提议不执行）；`--output-format`（`text`/`json`/`stream-json`）；`--stream-partial-output`（实时增量流输出）。

**典型用法**：
```bash
agent -p --force "重构认证模块使用 JWT"  # 执行文件修改
agent -p "分析代码"  # 只分析不修改
find src/ -name "*.js" | while read f; do agent -p --force "添加 JSDoc: $f"; done  # 批处理
```

**认证**：非交互环境设 `CURSOR_API_KEY` 环境变量（服务账号 API Key），无需浏览器登录。

**输出格式**：`text`（默认，干净的最终答案）；`json`（结构化分析）；`stream-json`（含 type/subtype 的实时流，适合进度追踪）。

**图片/媒体**：在 prompt 中直接引用文件路径，Agent 通过工具调用自动读取，支持相对/绝对路径。
