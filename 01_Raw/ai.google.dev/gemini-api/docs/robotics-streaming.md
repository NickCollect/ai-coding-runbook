---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-CN
fetched_at: 2026-10-19T05:58:08.278629+00:00
title: "\u652f\u6301\u6d41\u5f0f\u4f20\u8f93\u7684\u673a\u5668\u4eba \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 现已上架。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 支持流式传输的机器人

`gemini-robotics-er-2-streaming-preview` 模型端点公开了一个与 [Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=zh-cn) 集成的专用流式传输端点，可实现应用与机器人之间的实时双向互动。因此，它非常适合需要快速反馈环和对环境做出反应式响应的代理。

[在 Google AI Studio 中试用](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=zh-cn)
[从 GitHub 克隆示例应用](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## 使用场景

- **多机器人协调**：多个机器人通过共享会话通信任务状态并委托子任务。
- **持续监控**：观察场景并在发生特定事件（例如容器达到填充水平）时触发操作的机器人。
- **仓储和物流**：可直观地验证商品、跟踪打包进度并从错误中恢复的拣货和打包代理。

## 技术规范

下表列出了 Live API 的技术规范：

| 类别 | 详细信息 |
| --- | --- |
| 输入模态 | 音频（原始 16 位 PCM 音频，16kHz，小端序）、图片（JPEG <= 1FPS）、文本 |
| 输出模态 | 文本 |
| 协议 | 有状态 WebSocket 连接 (WSS) |

## 构建代理式设置

基于 Live API 构建的每个机器人代理都遵循以下三个步骤：

1. **将机器人功能声明为工具。**机器人可以执行的每项操作（导航、抓取、说话）都成为一个函数声明，其中包含名称、说明和参数架构。实体操作必须使用 `"behavior": "BLOCKING"`，这样模型才能在机器人完成操作后选择下一步。
2. **将多模态输入流式传输到持久会话中。**打开 `live.connect` 会话，并在任务的整个生命周期内保持该会话处于打开状态。发送从机器人传感器接收到的视频帧、音频或文本。
3. **在接收循环中处理工具调用。**每次模型选择操作时，都会发送 `tool_call` 消息。您的接收循环针对机器人 SDK 执行该函数，并发送回 `tool_response`。会话保持打开状态，模型会根据结果选择下一个操作。

以下部分展示了如何将这些步骤应用于三种常见模式：基准智能体循环、通过检测信号进行主动场景监控，以及通过 TTS 将语音作为工具进行路由。

## 通过函数调用编排机器人

以下示例展示了如何在一个 Python 脚本中将这三个步骤连接在一起。

第 1 步 - 工具定义 - 将机器人功能声明为函数声明。`navigate` 函数使用 `"behavior": "BLOCKING"`，因此模型会等待机器人到达途经点，然后再调用另一个工具。在同一列表中添加更多函数声明，以公开其他机器人功能。

第 2 步 - 输入辅助函数 - 显示了三个将不同模态输入流式传输到会话中的函数：`send_text` 用于命令，`send_image` 用于包含可选文本提示的相机帧，以及 `send_audio` 用于来自麦克风的原始 PCM 音频。

第 3 步（接收循环）同时运行，并处理两种类型的消息：`server_content` 消息（模型的文本输出）和 `tool_call` 消息（模型请求机器人执行操作）。当工具调用到达时，该循环会调用 `execute_tool`（您用实际的机器人 SDK 替换的桩），然后发送回 `tool_response`，以便模型可以选择下一个操作。

```
import asyncio
from google import genai
from google.genai import types

MODEL = "gemini-robotics-er-2-streaming-preview"

# ── Tool definitions ─────────────────────────────────────────────────────────
tools = [
   {
       "function_declarations": [
           {
               "name": "navigate",
               "description": "Navigate the robot to a named waypoint.",
               "behavior": "BLOCKING",
               "parameters": {
                   "type": "OBJECT",
                   "properties": {"name": {"type": "STRING"}},
                   "required": ["name"],
               },
           },
           # Add more function definitions here
       ]
   }
]

# ── Stub tool executor (replace with real robot SDK calls) ───────────────────
def execute_tool(name: str, args: dict) -> dict:
   print(f"  [Tool] {name}({args})")
   return {"status": "success"}

# ── Input helpers ────────────────────────────────────────────────────────────
def send_text(session, text: str):
   """Send a text turn."""
   return session.send_client_content(
       turns=types.Content(role="user", parts=[types.Part(text=text)]),
       turn_complete=True,
   )

def send_image(session, image_bytes: bytes, prompt: str = ""):
   """Send a JPEG image with an optional text prompt."""
   parts = [
       types.Part(
           inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
       )
   ]
   if prompt:
       parts.append(types.Part(text=prompt))
   return session.send_client_content(
       turns=types.Content(role="user", parts=parts),
       turn_complete=True,
   )

def send_audio(session, audio_chunk: bytes):
   """Stream a chunk of raw PCM audio (16-bit, 16 kHz, mono)."""
   return session.send_realtime_input(
       media=types.Blob(data=audio_chunk, mime_type="audio/pcm;rate=16000")
   )

# ── Receive loop ─────────────────────────────────────────────────────────────
async def receive_loop(session):
   """Print model text and handle tool calls until the session ends."""
   async for message in session.receive():
       if message.server_content:
           sc = message.server_content
           if sc.model_turn and sc.model_turn.parts:
               for part in sc.model_turn.parts:
                   if part.text:
                       print(f"Model: {part.text}", end="", flush=True)
           if sc.turn_complete:
               print("\n[Turn Complete]")
       elif message.tool_call:
           responses = []
           for call in message.tool_call.function_calls:
               print(f"\n[Tool Call] {call.name}({call.args})")
               result = execute_tool(call.name, call.args)
               responses.append(
                   types.FunctionResponse(
                       name=call.name,
                       response=result,
                       id=call.id,
                   )
               )
           await session.send_tool_response(function_responses=responses)

# ── Main ─────────────────────────────────────────────────────────────────────
async def main():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
   config = types.LiveConnectConfig(
       response_modalities=["TEXT"],
       tools=tools,
       system_instruction=types.Content(
           parts=[types.Part(text="You are a robot controller. Use tools to execute commands.")]
       ),
   )
   async with client.aio.live.connect(model=MODEL, config=config) as session:
       recv_task = asyncio.create_task(receive_loop(session))
       # Connect robot perception callbacks and user inputs to the helpers above.
       recv_task.cancel()

asyncio.run(main())
```

在每次工具响应后，接收循环都会保持活跃状态。该模型可构建和修订长时程计划，而无需您预先对整个行动序列进行编码。

## 主动时空推理

Live API 会以流式传输方式接收视频，但仅有视频帧不会触发新的推理轮次。视频帧必须附带文本或音频提示，才能触发模型回答。如需了解详情，请参阅 [Live API 功能](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=zh-cn)。

如需启用主动推理，请实现**心跳**：定期发送最新的相机帧，然后发送一个简短的文本提示，强制模型检查场景并做出明确的决策。视频输入速率限制为每秒一帧。

### 实现心跳

心跳协程在同一会话中作为单独的 `asyncio` 任务运行。
它会在等待每个回合完成 (`er_turn_done`) 时，根据情况将节奏调整为 1 Hz（与视频输入速率限制相符），以避免中断正在进行的推理：

```
async def heartbeat(session, camera, er_turn_done: asyncio.Event):
    TARGET_INTERVAL_SEC = 1.0

    while True:
        start_time = asyncio.get_running_loop().time()

        frame = await camera.latest_jpeg()
        await session.send_realtime_input(
            video=types.Blob(data=frame, mime_type="image/jpeg")
        )
        await session.send_realtime_input(
            text=(
                "[HEARTBEAT] If no task is active, call 'ack' and wait for user"
                " input. If a task is active: observe the scene. If the current"
                " step is progressing correctly, call 'ack'. If the current step"
                " is complete, call 'run_instruction' with the next step. If the"
                " overall goal is achieved, call 'reset' and inform the user."
            )
        )

        # Wait for the model to finish responding before sending the next heartbeat
        await er_turn_done.wait()
        er_turn_done.clear()

        # Sleep only the remaining time to maintain ~1 Hz cadence
        elapsed = asyncio.get_running_loop().time() - start_time
        remaining = TARGET_INTERVAL_SEC - elapsed
        if remaining > 0:
            await asyncio.sleep(remaining)
```

### 更新接收循环

如需在模型完成其回合时发出信号，请更新 `receive_loop` 以设置 `er_turn_done`：

```
# In receive_loop: signal when the model finishes its turn
if sc.turn_complete:
    er_turn_done.set()
```

## 通过外部 TTS 进行音频输出

Gemini Robotics ER 2 返回文本。您的应用通过注入的回调将完成的响应路由到单独的 TTS 提供程序（例如 [Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn)）。这样一来，您就可以控制语音延迟、语音选择和中断行为，并且无需更改代理逻辑即可切换 TTS 后端。

您还可以将 TTS 声明为工具，以便模型将“说点什么”与“移动手臂”同等对待。将以下函数声明添加到第一部分中的 `tools` 列表：

```
TOOLS = [
    {
        "name": "send_message",
        "description": (
            "Speak a message aloud via TTS, then deliver it to the"
            " specified target. Use target='user' to speak directly"
            " to the user, or a peer agent name (e.g., 'duo') to"
            " communicate with another robot."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Recipient: 'user' or a peer agent name.",
                },
                "message": {
                    "type": "string",
                    "description": "The message to speak and deliver.",
                },
            },
            "required": ["target", "message"],
        },
    },
]
```

通过将 TTS 封装在函数声明中，模型可以通过与任何其他机器人操作相同的工具调用路径来处理语音。您的应用通过注入的回调来完成调用。

## GitHub 上的示例

如需查看完整的有效示例，包括 Spot 机器人零食获取演示和 Tinybot 云台“Hello World”演示，请参阅 [Robotics Live API 示例](https://github.com/google-gemini/robotics-samples/tree/main/live-api)。

## 后续步骤

- [视频理解](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=zh-cn) - 时刻查找和进度分类。
- [任务编排](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=zh-cn) - 无需流式传输的长时程任务。
- [Live API 概览](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=zh-cn) - 完整的 Live API 文档。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-16。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-16。"],[],[]]
