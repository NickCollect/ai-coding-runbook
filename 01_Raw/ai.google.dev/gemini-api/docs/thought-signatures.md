---
source_url: https://ai.google.dev/gemini-api/docs/thought-signatures?hl=zh-CN
fetched_at: 2026-06-08T05:35:32.966041+00:00
title: "\u601d\u8def\u7b7e\u540d \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 思路签名

思考签名是模型内部思考过程的加密表示形式，用于在多步交互中保留推理上下文。
使用思考模型（例如 Gemini 3 和 2.5 系列）时，API 可能会
在回答的[内容部分](https://ai.google.dev/api/caching?hl=zh-cn#Part)
中返回 `thoughtSignature` 字段（例如 `text` 或 `functionCall` 部分）。

一般而言，如果您在模型回答中收到思考签名，则应在下一轮中发送对话历史记录时，完全按收到的原样将其传回。**使用 Gemini 3 模型时，您必须在函数调用期间传回思考签名，否则会收到验证错误** （4xx 状态代码）。
这包括为 Gemini 3
Flash 使用 `minimal`
[思考级别](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn#thinking-levels) 设置的情况。

## 运作方式

下图直观地展示了“轮次”和“步骤”的含义，因为它们与
[Gemini API 中的函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)有关。“轮次”是用户与模型之间对话中的一次完整交流。“步骤”是模型执行的更精细的操作，通常是完成轮次的较大过程的一部分。

![函数调用轮次和步骤图](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=zh-cn)

*本文档重点介绍如何处理 Gemini 3 模型的函数调用。如需了解与 2.5 的差异，请参阅
[模型行为](#model-behavior)部分。*

Gemini 3 会为所有包含函数调用的模型回答（来自 API 的回答）返回思考签名。在以下情况下，系统会显示思考签名：

- 如果存在[并行函数](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#parallel_function_calling)
  调用，模型回答返回的第一个函数调用部分将包含
  思考签名。
- 如果存在顺序函数调用（多步），每个函数调用都将包含一个签名，并且您必须传回所有签名。
- 不包含函数调用的模型回答会在模型返回的最后一部分中返回思考签名。

下表直观地展示了多步函数调用，将轮次和步骤的定义与上述引入的签名概念相结合：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **轮次** | **步骤** | **用户请求** | **模型回答** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | 无 |

## 函数调用部分中的签名

当 Gemini 生成 `functionCall` 时，它会依赖 `thought_signature` 在下一轮中正确处理工具的输出。

- **行为**：
  - **单个函数调用**：`functionCall` 部分将包含 `thought_signature`。
  - ****并行函数调用**：如果模型在回答中生成并行函数调用
    ，则 `thought_signature` \*\*仅附加到第一个\*\*
    `functionCall` 部分。**同一回答中的后续 `functionCall` 部分将**不** 包含签名。
- **要求**：您**必须** 在发送对话历史记录时，在收到此签名的确切部分中返回此签名。
- **验证**：系统会对当前轮次中的所有函数调用强制执行严格验证。（仅需要当前轮次；我们不会验证之前的轮次）
  - API 会在历史记录中（从最新到最旧）查找包含标准内容（例如 `text`）（即当前轮次的开头）的最新**用户** 消息。这**be** 会是 `functionResponse`。
  - **所有**模型 `functionCall` 轮次在该特定使用
    消息之后发生，并被视为轮次的一部分。
  - 当前轮次的**每个步骤** 中的**第一个** `functionCall` 部分**必须** 包含其 `thought_signature`。
  - 如果您在当前轮次的任何步骤中省略了第一个 `functionCall` 部分的 `thought_signature`，请求将失败并显示 400 错误。
- **如果未返回正确的签名，您将收到以下错误**
  - Gemini 3 模型：如果未包含签名，将导致 400 错误。措辞将采用以下形式：
    - `<index of contents array>`
      内容块中的函数调用 `<Function Call>` 缺少 `thought_signature`。例如，*函数
      调用 `FC1` 在 `1.` 内容块中缺少 `thought_signature`。*

### 顺序函数调用示例

本部分展示了一个多函数调用示例，其中用户提出了一个需要执行多个任务的复杂问题。

我们来了解一个多轮函数调用示例，其中用户提出了
一个需要执行多个任务的复杂问题：`"Check flight status for AA100 and
book a taxi if delayed"`。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **轮次** | **步骤** | **用户请求** | **模型回答** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

以下代码说明了上表中的序列。

**第 1 轮，第 1 步（用户请求）**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "check_flight",
          "description": "Gets the current status of a flight",
          "parameters": {
            "type": "object",
            "properties": {
              "flight": {
                "type": "string",
                "description": "The flight number to check"
              }
            },
            "required": [
              "flight"
            ]
          }
        },
        {
          "name": "book_taxi",
          "description": "Book a taxi",
          "parameters": {
            "type": "object",
            "properties": {
              "time": {
                "type": "string",
                "description": "time to book the taxi"
              }
            },
            "required": [
              "time"
            ]
          }
        }
      ]
    }
  ]
}
```

**第 1 轮，第 1 步（模型回答）**

```
{
"content": {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>"
          }
        ]
  }
}
```

**第 1 轮，第 2 步（用户回答 - 发送工具输出）** 由于此用户轮次仅包含 `functionResponse`（没有新文本），因此我们仍处于第 1 轮。我们
必须保留 `<Signature_A>`。

```
{
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    },
    {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "check_flight",
              "response": {
                "status": "delayed",
                "departure_time": "12 PM"
                }
              }
            }
        ]
}
```

**第 1 轮，第 2 步（模型）** 模型现在根据上一个工具输出决定预订出租车。

```
{
      "content": {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "book_taxi",
              "args": {
                "time": "10 AM"
              }
            },
            "thoughtSignature": "<Signature B>"
          }
        ]
      }
}
```

**第 1 轮，第 3 步（用户 - 发送工具输出）** 如要发送出租车预订
确认，我们必须包含此循环中**所有** 函数调用的签名
(`<Signature A>` + `<Signature B>`)。

```
{
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    },
    {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "check_flight",
              "response": {
                "status": "delayed",
                "departure_time": "12 PM"
              }
              }
            }
        ]
      },
      {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "book_taxi",
              "args": {
                "time": "10 AM"
              }
            },
            "thoughtSignature": "<Signature B>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "book_taxi",
              "response": {
                "booking_status": "success"
              }
              }
            }
        ]
    }
}
```

### 并行函数调用示例

我们来了解一个并行函数调用示例，其中用户要求
`"Check weather in Paris and London"`，以了解模型在何处进行验证。

| **轮次** | **步骤** | **用户请求** | **模型回答** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 ("Paris") + signature  FC2 ("London") | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  （无 FC） | 无 |

以下代码说明了上表中的序列。

**第 1 轮，第 1 步（用户请求）**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check the weather in Paris and London."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "get_current_temperature",
          "description": "Gets the current temperature for a given location.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco"
              }
            },
            "required": [
              "location"
            ]
          }
        }
      ]
    }
  ]
}
```

**第 1 轮，第 1 步（模型回答）**

```
{
  "content": {
    "parts": [
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "location": "Paris"
          }
        },
        "thoughtSignature": "<Signature_A>"// INCLUDED on First FC
      },
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "location": "London"
          }// NO signature on subsequent parallel FCs
        }
      }
    ]
  }
}
```

**第 1 轮，第 2 步（用户回答 - 发送工具输出）** 我们必须完全按接收时的原样保留第一部分的
`<Signature_A>`。

```
[
  {
    "role": "user",
    "parts": [
      {
        "text": "Check the weather in Paris and London."
      }
    ]
  },
  {
    "role": "model",
    "parts": [
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "city": "Paris"
          }
        },
        "thought_signature": "<Signature_A>" // MUST BE INCLUDED
      },
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "city": "London"
          }
        }
      } // NO SIGNATURE FIELD
    ]
  },
  {
    "role": "user",
    "parts": [
      {
        "functionResponse": {
          "name": "get_current_temperature",
          "response": {
            "temp": "15C"
          }
        }
      },
      {
        "functionResponse": {
          "name": "get_current_temperature",
          "response": {
            "temp": "12C"
          }
        }
      }
    ]
  }
]
```

## 非 `functionCall` 部分中的签名

Gemini 也可能会在非函数调用部分的回答的最后一部分中返回 `thought_signatures`。

- **行为**：模型返回的最后内容部分（`text, inlineData…`）可能包含 `thought_signature`。
- **建议**：**建议**返回这些签名，以确保
  模型保持高质量的推理，特别是对于遵循复杂指令
  或模拟代理工作流的情况。
- **验证**：API **不会** 严格强制验证。如果您省略它们，不会收到阻塞性错误，但性能可能会下降。

### 文本/上下文推理（无验证）

**第 1 轮，第 1 步（模型回答）**

```
{
  "role": "model",
  "parts": [
    {
      "text": "I need to calculate the risk. Let me think step-by-step...",
      "thought_signature": "<Signature_C>" // OPTIONAL (Recommended)
    }
  ]
}
```

**第 2 轮，第 1 步（用户）**

```
[
  { "role": "user", "parts": [{ "text": "What is the risk?" }] },
  {
    "role": "model", 
    "parts": [
      {
        "text": "I need to calculate the risk. Let me think step-by-step...",
        // If you omit <Signature_C> here, no error will occur.
      }
    ]
  },
  { "role": "user", "parts": [{ "text": "Summarize it." }] }
]
```

## 思考保留和 token 用量

**从 Gemini 3.5 Flash 开始**，如果对话历史记录中存在思考签名，模型将使用之前所有轮次的推理上下文。

如需启用思考保留，请在请求的 `contents` 数组中**传递完整且未修改的对话历史记录** （包括之前模型轮次中返回的 `thought_signature` 字段）。

### 管理 token 用量

在多个轮次中保留中间思考会增加后续轮次中的输入 token 数量，因为模型必须解析之前轮次中的思考签名。

如果您的应用执行简单查询，或者您希望在长时间对话中尽可能降低费用，则可以从对话历史记录中清除之前的思考签名。

## OpenAI 兼容性的签名

以下示例展示了如何使用 [OpenAI 兼容性](https://ai.google.dev/gemini-api/docs/openai?hl=zh-cn)处理聊天
补全 API 的思考签名。

### 顺序函数调用示例

这是一个多函数调用示例，其中用户提出了一个需要执行多个任务的复杂问题。

我们来了解一个多轮函数调用示例，其中用户要求 `Check flight status for AA100 and book a taxi if delayed`，您可以了解当用户提出需要执行多个任务的复杂问题时会发生什么情况。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **轮次** | **步骤** | **用户请求** | **模型回答** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

以下代码介绍了给定的序列。

**第 1 轮，第 1 步（用户请求）**

```
{
  "model": "google/gemini-3.1-pro-preview",
  "messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "check_flight",
        "description": "Gets the current status of a flight",
        "parameters": {
          "type": "object",
          "properties": {
            "flight": {
              "type": "string",
              "description": "The flight number to check."
            }
          },
          "required": [
            "flight"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "book_taxi",
        "description": "Book a taxi",
        "parameters": {
          "type": "object",
          "properties": {
            "time": {
              "type": "string",
              "description": "time to book the taxi"
            }
          },
          "required": [
            "time"
          ]
        }
      }
    }
  ]
}
```

**第 1 轮，第 1 步（模型回答）**

```
{
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>"
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1",
            "type": "function"
          }
        ]
    }
```

**第 1 轮，第 2 步（用户回答 - 发送工具输出）**

由于此用户轮次仅包含 `functionResponse`（没有新文本），因此我们
仍处于第 1 轮，并且必须保留 `<Signature_A>`。

```
"messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "check_flight",
      "tool_call_id": "function-call-1",
      "content": "{\"status\":\"delayed\",\"departure_time\":\"12 PM\"}"                 
    }
  ]
```

**第 1 轮，第 2 步（模型）**

模型现在根据上一个工具输出决定预订出租车。

```
{
"role": "model",
"tool_calls": [
{
"extra_content": {
"google": {
"thought_signature": "<Signature B>"
}
            },
            "function": {
              "arguments": "{\"time\":\"10 AM\"}",
              "name": "book_taxi"
            },
            "id": "function-call-2",
            "type": "function"
          }
       ]
}
```

**第 1 轮，第 3 步（用户 - 发送工具输出）**

如要发送出租车预订确认，我们必须包含此循环中所有
函数调用的签名（`<Signature A>` + `<Signature B>`）。

```
"messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1d6a1a61-6f4f-4029-80ce-61586bd86da5",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "check_flight",
      "tool_call_id": "function-call-1d6a1a61-6f4f-4029-80ce-61586bd86da5",
      "content": "{\"status\":\"delayed\",\"departure_time\":\"12 PM\"}"                 
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature B>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"time\":\"10 AM\"}",
              "name": "book_taxi"
            },
            "id": "function-call-65b325ba-9b40-4003-9535-8c7137b35634",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "book_taxi",
      "tool_call_id": "function-call-65b325ba-9b40-4003-9535-8c7137b35634",
      "content": "{\"booking_status\":\"success\"}"
    }
  ]
```

### 并行函数调用示例

我们来了解一个并行函数调用示例，其中用户要求
`"Check weather in Paris and London"`，您可以了解模型在何处进行
验证。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **轮次** | **步骤** | **用户请求** | **模型回答** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

以下代码介绍了给定的序列。

**第 1 轮，第 1 步（用户请求）**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check the weather in Paris and London."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "get_current_temperature",
          "description": "Gets the current temperature for a given location.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco"
              }
            },
            "required": [
              "location"
            ]
          }
        }
      ]
    }
  ]
}
```

**第 1 轮，第 1 步（模型回答）**

```
{
"role": "assistant",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Signature returned
              }
            },
            "function": {
              "arguments": "{\"location\":\"Paris\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
            "type": "function"
          },
          {
            "function": {
              "arguments": "{\"location\":\"London\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
            "type": "function" // No signature on Parallel FC
          }
        ]
}
```

**第 1 轮，第 2 步（用户回答 - 发送工具输出）**

您必须完全按接收时的原样保留第一部分的 `<Signature_A>`。

```
"messages": [
    {
      "role": "user",
      "content": "Check the weather in Paris and London."
    },
    {
      "role": "assistant",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required
              }
            },
            "function": {
              "arguments": "{\"location\":\"Paris\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
            "type": "function"
          },
          {
            "function": { //No Signature
              "arguments": "{\"location\":\"London\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
            "type": "function"
          }
        ]
    },
    {
      "role":"tool",
      "name": "get_current_temperature",
      "tool_call_id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
      "content": "{\"temp\":\"15C\"}"
    },    
    {
      "role":"tool",
      "name": "get_current_temperature",
      "tool_call_id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
      "content": "{\"temp\":\"12C\"}"
    }
  ]
```

## 常见问题解答

1. **如何将历史记录从其他模型转移到 Gemini 3，并在当前轮次和步骤中包含函数调用部分？我需要提供并非由 API 生成的函数调用
   部分，因此这些部分没有关联的
   思考签名？**

   虽然强烈建议不要将自定义函数调用块注入到请求中，但在无法避免的情况下（例如，向模型提供有关客户端确定性执行的函数调用和回答的信息，或从不包含思考签名的其他模型转移跟踪记录），您可以在思考签名字段中设置以下虚拟签名 `"context_engineering_is_the_way_to_go"` 或
   `"skip_thought_signature_validator"`，以跳过验证。
2. **我正在传回交错的并行函数调用和回答，但 API 返回 400。为什么？**

   当 API 返回并行函数调用“FC1 + signature, FC2”时，预期的用户回答为“FC1+ signature, FC2, FR1, FR2”。如果您将它们交错为“FC1 + signature, FR1, FC2, FR2”，API 将返回 400 错误。
3. **在流式传输时，如果模型未返回函数调用，我找不到
   思考签名**

   在模型回答不包含具有流式传输请求的 FC 期间，模型可能会在包含空文本内容部分的部分中返回思考签名。建议您解析整个请求，直到模型返回 `finish_reason`。

## 不同模型的思考签名

[Gemini 3 模型](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn#gemini-3)和 Gemini 2.5 模型
在思考签名方面的行为有所不同：

- **思考保留**：
  - **从 Gemini 3.5 Flash 开始**，如果对话历史记录中存在思考签名，模型将使用之前所有轮次的推理上下文。
  - 之前的模型不会以相同的方式使用之前轮次的推理上下文。
- **如果回答中包含函数调用**:
  - Gemini 3 将始终在第一个函数调用部分中包含签名。
    **必须** 返回该部分。
  - Gemini 2.5 将在第一部分（无论类型如何）中包含签名。**可以选择** 返回该部分。
- **如果回答中不包含函数调用**:
  - 如果模型生成思考，Gemini 3 将在最后一部分中包含签名。
  - Gemini 2.5 不会在任何部分中包含签名。

如需了解更多
比较详情
，请参阅[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn#signatures)页面。对于 Gemini 3 Image 模型，请参阅
[图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn#thinking-process)指南的思考过程部分。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-01。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-01。"],[],[]]
