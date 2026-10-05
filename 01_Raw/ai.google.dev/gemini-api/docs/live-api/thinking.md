---
source_url: https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=zh-CN
fetched_at: 2026-10-05T06:28:23.031562+00:00
title: "Live API \u7684\u601d\u7ef4\u65b9\u5f0f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Live API 的思维方式

借助 Gemini Live API，您可以与 Gemini 模型进行实时的双向语音对话。

标准语音模型非常适合即时对话。您对模型说话，模型会立即生成语音回复。但当请求需要规划、复杂分析或外部工具时，直接回答会受到限制。模型必须在不进行推理的情况下回答，或者在等待工具完成时静默暂停。

在 Live API (`gemini-3.8-live-extended-thinking`) 中思考可为实时语音会话添加背景推理。模型会在后台规划和调用异步工具，同时说出自然的对话填充语，以保持互动活跃。

此架构通过以下两种主要方式改变了对话生命周期：

- **对话填充内容**：模型在后台执行工具时，会说出中间更新（例如“正在检查航班选项”）。
- **互动状态跟踪**：由于模型可以在单个请求期间多次说话，因此服务器会在后台处理期间发出 `interaction_status: "IN_PROGRESS"`，并在整个任务完成时发出 `interaction_status: "IDLE"`。

下图比较了标准实时语音会话与“边想边推理”之间的互动生命周期：

![Live API 函数调用和状态跟踪比较](https://ai.google.dev/static/gemini-api/docs/images/thinking-model-comparison.svg?hl=zh-cn)

## 选择合适的模型

在 `gemini-3.8-live` 和 `gemini-3.8-live-extended-thinking` 之间做出选择时，请考虑以下三个主要因素：响应延迟时间、任务复杂程度和客户端状态处理。

### Gemini 3.8 Live 的适用场景

对于需要立即轮流对话且任务直接的低延迟对话语音代理，请使用 `gemini-3.8-live`。

- **对话式语音助理**：客户服务分流、语言练习、语音搜索和互动式故事讲述。
- **快速执行工具**：外部工具在几毫秒内返回的工作流（例如读取传感器值或控制智能设备）。
- **简单的客户端逻辑**：应用中每个用户轮次都会收到单个模型响应，并且 `turnComplete: true` 会在会话空闲时可靠地发出信号。

### 何时使用 Gemini 3.8 Live（扩展思考）

如果您的代理必须评估复杂数据、规划多个步骤或处理需要几秒钟才能运行的工具，请使用 `gemini-3.8-live-extended-thinking`。

- **多步骤诊断和支持**：技术支持人员会诊断多个日志、错误代码和配置检查中的系统问题。
- **协调的数据检索**：旅游和预订代理，可搜索航班、查询酒店，并通过并行 API 调用比较价格。
- **STEM 和代码辅导**：在给出解释之前，验证公式、调试代码或处理多步逻辑的教育类智能体。
- **遮盖工具延迟**：在语音体验中，长时间运行的函数可能会导致听众感到尴尬的沉默。

### 主要区别总结

下表总结了这两种型号之间的技术差异：

| 功能 | Gemini 3.8 Live | Gemini 3.8 Live（扩展思考） |
| --- | --- | --- |
| **主要使用场景** | 低延迟语音代理、直接命令、快速工具 | 多步骤问题解决、复杂规划、多工具工作流 |
| **模型端点** | `gemini-3.8-live` | `gemini-3.8-live-extended-thinking` |
| **推理架构** | 具有固定延迟配置的交错推理（不支持 `thinking_level`） | 可配置的后台推理（`thinking_level`：`low`、`medium`、`high`；不支持 `MINIMAL`） |
| **开启边界** | `turnComplete: true` 结束回合并返回到空闲状态 | `turnComplete: true` 完成话语；`interaction_status` 控制会话生命周期 |
| **对话填充词** | 模型在说话之前等待工具执行 | 模型在处理时会流式传输中间对话填充词 |
| **工具执行** | 支持同步 (`BLOCKING`) 和异步 (`NON_BLOCKING`) 工具 | 需要异步 (`NON_BLOCKING`) 工具声明 |

## 迁移和集成路径

请按照以下步骤升级现有的语音应用，或将 Thinking 集成到您的 Live API 会话中。

### 从 Gemini 3.1 Flash Live 升级

对于使用 `gemini-3.1-flash-live-preview` 的现有语音应用，升级到 `gemini-3.8-live` 需要更新模型字符串并从设置配置中省略 `thinking_level`（或 `thinking_config`），因为 `thinking_level` 不受 `gemini-3.8-live` 支持：

```
{
  "setup": {
    "model": "models/gemini-3.8-live"
  }
}
```

回合生命周期和 `turnComplete` 信号保持不变。

### 采用思考

如需采用 `gemini-3.8-live-extended-thinking`，请更新以下三个集成点：

1. **跟踪 `interaction_status` 而不是 `turnComplete`**：在思考会话中，模型可以在推理时发出中间对话填充词。检查传入服务器消息中的 `interaction_status` 字段，以管理界面状态。仅当 `interaction_status` 为 `IDLE` 时返回到空闲状态。

   ### Python

   ```
   status = getattr(message, "interaction_status", None)
   if status == "IDLE":
       # Ready for user input
       set_ui_state("listening")
   elif status == "IN_PROGRESS":
       # Reasoning or executing tools
       set_ui_state("thinking")
   ```

   ### JavaScript

   ```
   if (message.interactionStatus === 'IDLE') {
     // Ready for user input
     setUiState('listening');
   } else if (message.interactionStatus === 'IN_PROGRESS') {
     // Reasoning or executing tools
     setUiState('thinking');
   }
   ```
2. **声明非阻塞函数**：在所有函数声明中设置 `"behavior": "NON_BLOCKING"`。思考模型会在后台异步运行工具，同时以流式方式提供口头更新。同步阻塞工具会返回错误。

   ### Python

   ```
   search_flights = types.FunctionDeclaration(
       name="search_flights",
       description="Searches for available flights.",
       behavior="NON_BLOCKING",
       parameters={
           "type": "OBJECT",
           "properties": {
               "destination": {"type": "STRING"},
           },
           "required": ["destination"],
       },
   )
   ```

   ### JavaScript

   ```
   const searchFlights = {
     name: 'search_flights',
     description: 'Searches for available flights.',
     behavior: 'NON_BLOCKING',
     parameters: {
       type: 'OBJECT',
       properties: {
         destination: { type: 'STRING' },
       },
       required: ['destination'],
     },
   };
   ```
3. **配置推理深度**：在会话配置中设置 `thinking_config` 以调整推理级别（`low`、`medium` 或 `high`；不支持 `MINIMAL`）。

   ### Python

   ```
   config = types.LiveConnectConfig(
       response_modalities=["AUDIO"],
       thinking_config=types.ThinkingConfig(
           thinking_level="low",
       ),
       tools=[types.Tool(function_declarations=[search_flights])],
   )
   ```

   ### JavaScript

   ```
   const config = {
     responseModalities: [Modality.AUDIO],
     thinkingConfig: {
       thinkingLevel: 'low',
     },
     tools: [{ functionDeclarations: [searchFlights] }],
   };
   ```

## 协议对照比较

本部分比较了在实时 API 会话的每个阶段交换的 WebSocket 消息。

### 第 1 步：设置会话

这两个模型都连接到同一 WebSocket 端点：

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent?key=$API_KEY
```

- **相同**：WebSocket 网址和 API 密钥身份验证。
- **模型字符串**：`gemini-3.8-live` 与 `gemini-3.8-live-extended-thinking`。
- **思考配置**：思考会添加 `thinkingConfig` 来调整推理深度。
- **工具行为**：思考需要对函数声明使用 `"behavior": "NON_BLOCKING"`。

### Gemini 3.8 Live

```
{
  "setup": {
    "model": "models/gemini-3.8-live",
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "prebuiltVoiceConfig": {
            "voiceName": "Puck"
          }
        }
      }
    }
  }
}
```

### Gemini 3.8 Live（扩展思考）

```
{
  "setup": {
    "model": "models/gemini-3.8-live-extended-thinking",
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "prebuiltVoiceConfig": {
            "voiceName": "Puck"
          }
        }
      },
      "thinkingConfig": {
        "thinkingLevel": "LOW"
      }
    },
    "tools": [{
      "functionDeclarations": [{
        "name": "searchFlights",
        "description": "Searches for flights between cities.",
        "behavior": "NON_BLOCKING",
        "parameters": {
          "type": "OBJECT",
          "properties": {
            "destination": { "type": "STRING" }
          },
          "required": ["destination"]
        }
      }]
    }]
  }
}
```

两个模型在连接时都会收到相同的服务器确认：

```
{
  "setupComplete": {}
}
```

### 第 2 步：用户音频输入

这两款型号的音频流式传输功能完全相同。使用 `realtimeInput` 流式传输实时 16kHz 原始 PCM 音频块：

```
{
  "realtimeInput": {
    "audio": {
      "data": "UklGRiQAAABXQVZF...",
      "mimeType": "audio/pcm;rate=16000"
    }
  }
}
```

### 第 3 步：模型响应和状态生命周期

两款模型均以 `serverContent.modelTurn` 为单位串流 24kHz PCM 音频块。不过，生命周期管理有所不同：

#### Gemini 3.8 Live 回答流程

1. 服务器会流式传输相应回合的音频块。
2. 服务器发送 `turnComplete: true`，表示模型已完成说话，会话处于空闲状态。

```
// 1. Audio stream chunks
{
  "serverContent": {
    "modelTurn": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "audio/pcm;rate=24000",
            "data": "..."
          }
        }
      ]
    }
  }
}

// 2. Turn completion -> Signals client to switch UI to Idle/Listening
{
  "serverContent": {
    "turnComplete": true
  }
}
```

#### Gemini 3.8 Live 扩展思考回答流程

1. **口语填充**：模型会使用 `turnComplete: true` 和 `interactionStatus: "IN_PROGRESS"` 发出中间语音（例如*“正在查询飞往西雅图的航班…”*）。
2. **异步工具调用**：服务器在 `interactionStatus` 保持 `"IN_PROGRESS"` 的同时发出工具调用，表明服务器正在积极处理多步对话轮次，并等待工具响应。
3. **工具响应**：客户端执行函数并返回输出。
4. **最终回答**：服务器通过 `turnComplete: true` 和 `interactionStatus: "IDLE"` 传递完整答案。

```
// 1. Spoken verbal filler while background reasoning proceeds
{
  "serverContent": {
    "modelTurn": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "audio/pcm;rate=24000",
            "data": "..."
          }
        }
      ]
    },
    "turnComplete": true,
    "interactionStatus": "IN_PROGRESS"
  }
}

// 2. Asynchronous tool call emitted with IN_PROGRESS status
{
  "toolCall": {
    "functionCalls": [
      {
        "id": "call_123",
        "name": "searchFlights",
        "args": {
          "destination": "Seattle"
        }
      }
    ]
  },
  "interactionStatus": "IN_PROGRESS"
}

// 3. Client executes function and returns result
{
  "toolResponse": {
    "functionResponses": [
      {
        "response": {
          "output": {
            "flight": "DL 145",
            "price": "$145"
          }
        },
        "id": "call_123"
      }
    ]
  }
}

// 4. Final spoken answer delivered -> session transitions to IDLE when done
{
  "serverContent": {
    "modelTurn": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "audio/pcm;rate=24000",
            "data": "..."
          }
        }
      ]
    },
    "interactionStatus": "IDLE",
    "turnComplete": true
  }
}
```

## SDK 实现示例

以下示例展示了如何使用 Google GenAI SDK 配置思考并处理 `interaction_status`。

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-live-extended-thinking"

# Define non-blocking function declaration
search_flights = types.FunctionDeclaration(
    name="search_flights",
    description="Searches for available flights to a destination.",
    behavior="NON_BLOCKING",
    parameters={
        "type": "OBJECT",
        "properties": {
            "destination": {"type": "STRING"}
        },
        "required": ["destination"]
    }
)

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    thinking_config=types.ThinkingConfig(
        thinking_level="low"
    ),
    tools=[types.Tool(function_declarations=[search_flights])]
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session connected with Thinking")

        async for message in session.receive():
            # Inspect interaction status for server lifecycle tracking
            status = getattr(message, "interaction_status", None)
            if status:
                print(f"Interaction status: {status}")

            # Handle audio output parts
            if message.server_content and message.server_content.model_turn:
                for part in message.server_content.model_turn.parts:
                    if part.inline_data:
                        # Process 24kHz audio chunk
                        pass

            # Handle asynchronous tool call
            if message.tool_call:
                for call in message.tool_call.function_calls:
                    print(f"Executing tool: {call.name}")
                    # Simulate function execution
                    response = types.FunctionResponse(
                        id=call.id,
                        name=call.name,
                        response={"result": "Flight DL 145 ($145)"}
                    )
                    await session.send_tool_response(
                        function_responses=[response]
                    )

            # Status is IDLE when reasoning and all turns are complete
            if status == "IDLE":
                print("Session is idle and ready for user input.")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live-extended-thinking';

const searchFlights = {
  name: 'search_flights',
  description: 'Searches for available flights to a destination.',
  behavior: 'NON_BLOCKING',
  parameters: {
    type: 'OBJECT',
    properties: {
      destination: { type: 'STRING' }
    },
    required: ['destination']
  }
};

const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low'
  },
  tools: [{ functionDeclarations: [searchFlights] }]
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.log('Session connected'),
      onmessage: async (event) => {
        const message = JSON.parse(event.data);

        if (message.interactionStatus) {
          console.log(`Interaction status: ${message.interactionStatus}`);
        }

        if (message.toolCall) {
          for (const call of message.toolCall.functionCalls) {
            console.log(`Executing tool: ${call.name}`);
            session.sendToolResponse({
              functionResponses: [{
                id: call.id,
                name: call.name,
                response: { result: 'Flight DL 145 ($145)' }
              }]
            });
          }
        }

        if (message.interactionStatus === 'IDLE') {
          console.log('Session is idle and waiting for input.');
        }
      }
    }
  });
}

main();
```

## 后续步骤

- 请参阅 [Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=zh-cn) 和 [Gemini 3.8 Live（扩展思考）](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=zh-cn)模型页面。
- 如需详细比较所有 Live API 模型的功能，请查看[模型对比](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=zh-cn#model-comparison)表。
- 如需详细了解函数调用，请参阅 [Live API 工具使用](https://ai.google.dev/gemini-api/docs/live-api/tools?hl=zh-cn)指南。
- 查看[会话管理](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=zh-cn)，以处理会话恢复和上下文生命周期。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-17。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-17。"],[],[]]
