---
name: Gemini Code Execution
type: entity
vendor: Gemini
aliases: ["Code Execution", "code_execution tool", "ToolCodeExecution", "Python sandbox"]
created: 2026-05-05
---

# Gemini Code Execution

Gemini 的内置 Python 代码执行工具，让模型可以生成并在沙箱中运行 Python 代码，迭代调整直到得出正确答案；Gemini 3 系列还支持对图像进行代码驱动的视觉分析。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | Google / Gemini |
| 启用方式 | `tools=[Tool(code_execution=ToolCodeExecution)]` |
| 执行语言 | **仅 Python**（可生成其他语言代码但只能执行 Python） |
| 迭代执行 | 支持（生成→执行→观察→调整→再执行） |
| 计费 | 生成代码：output token；执行结果：input token；执行时长不额外收费 |

## 核心功能

### 适用场景

- 数学计算（求和、方程求解）
- 数据处理（统计、分析）
- 算法问题求解
- 图像分析（Gemini 3 专属）

### Response 部分类型

| 部分类型 | 说明 |
|---|---|
| `text` | 内联叙述文本 |
| `executableCode` | 生成的 Python 代码块 |
| `codeExecutionResult` | 代码执行输出 |

### Gemini 3 图像能力（新增）

Gemini 3 Flash 可以编写并执行 Python 来主动操作和检查图像：
- **缩放检视**：检测小细节（如读取仪表盘数值），裁剪后以更高分辨率重新检查
- **视觉数学**：从视觉数据进行多步计算（如汇总发票金额）
- **图像标注**：绘制箭头或标签回答问题

### 预安装 Python 库

沙箱环境预安装了一组 Python 库（数值计算、数据处理等，具体列表见官方文档）。

### 迭代执行机制

模型可在单次请求中多次运行代码：生成 → 执行 → 观察结果 → 调整 → 再执行，直到得出正确答案。所有中间步骤在响应 parts 中可见。

## API 示例

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the sum of the first 50 prime numbers? Generate and run code.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print("文本:", part.text)
    if part.executable_code is not None:
        print("代码:", part.executable_code.code)
    if part.code_execution_result is not None:
        print("执行结果:", part.code_execution_result.output)
```

```javascript
// JavaScript
tools: [{ codeExecution: {} }]
```

```python
# Gemini 3 图像分析
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[image_part, "How many expression pedals are shown?"],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)
```

## 与 Claude 对应物

[[Code-execution-tool]] — Claude 的代码执行工具（Claude Code / Claude.ai 中的 Code tool），功能定位相同；Anthropic 也有用于 tool use 的 Code Execution API（[[code-execution-tool--at]]）。

## 出现来源

- [[code-execution--gemini-docs]]

## 相关

- [[Gemini-API]] — 通过 tools 参数启用
- [[Gemini-Grounding]] — 可与 grounding 组合使用
- [[Code-execution-tool]] — Claude 对应物
