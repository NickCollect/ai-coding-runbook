---
source_url: https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=zh-CN
fetched_at: 2026-09-07T05:43:39.000500+00:00
title: "Agentic Vision \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Agentic Vision

Gemini Robotics ER 模型可以编写和执行 Python 代码，以便在回答之前处理图片和应用逻辑。本页介绍了代码执行示例：使用缩放和裁剪进行对象检测、仪表读数、流体测量、电路板读数和图片注解。

如需根据自己的用例调整这些示例，请将提示文本和上传的图片文件替换为您自己的内容。您还可以调整提示中请求的 JSON 架构，以匹配应用所需的输出结构，或者添加 `system_instruction` 来强制执行输出格式和精度。

如需查看完整的可运行代码，请参阅
[机器人技术 Cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)。

## 思考等级

您可以控制模型的思考等级，以在延迟时间和准确率之间进行权衡。对于对象检测等空间任务，较低的思考等级效果良好。对于计数或重量估计等复杂任务，较高的思考等级效果更好。

以下示例将思考等级设置为 `high`，以执行复杂的计数任务：

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="scene.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": "Identify and count all objects on the table."}
    ],
    generation_config={
        "thinking_level": "high"  # Use "minimal" or "low" for faster spatial tasks
    }
)

print(interaction.output_text)
```

如需了解详情，请参阅[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)。

## 对象检测（缩放和裁剪）

以下示例使用代码执行来缩放和裁剪图片，以便在检测对象和返回边界框时获得更清晰的视图。

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="sorting.jpeg")

prompt = """
Return JSON in the format {label: val, y: val, x: val, y2: val, x2: val} for
the compostable objects in this scene. Please Zoom and crop the image for a
clearer view. Return an annotated image of the final result with the bounding
boxes drawn on it to the API caller as a part of your process.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

模型输出类似于以下 JSON 响应：

```
[
  {"label": "compostable", "y": 256, "x": 482, "y2": 295, "x2": 546},
  {"label": "compostable", "y": 317, "x": 478, "y2": 350, "x2": 542},
  {"label": "compostable", "y": 586, "x": 556, "y2": 668, "x2": 595},
  {"label": "compostable", "y": 463, "x": 669, "y2": 511, "x2": 718},
  {"label": "compostable", "y": 178, "x": 565, "y2": 250, "x2": 609}
]
```

下图显示了模型返回的框。

![显示检测到的对象的边界框的示例](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-bounding-boxes.png?hl=zh-cn)

## 读取模拟仪表并应用逻辑

以下示例演示了如何使用模型读取模拟仪表并执行时间计算。它使用系统指令来强制执行 JSON 输出。

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="gauge.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    system_instruction="Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block).",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": """Read the current value from this gauge. Then, calculate how long
        it will take at the current rate for the value to reach maximum.
        Reply in JSON: {"current_value": val, "max_value": val,
        "time_to_max_minutes": val}"""}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

## 测量容器中的流体

以下示例演示了如何使用代码执行来测量容器中的流体液位。

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="fluid.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    system_instruction="Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block).",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": """Measure the amount of fluid in the container. Reply in JSON:
        {"fluid_level_ml": val, "container_capacity_ml": val,
        "percentage_full": val}"""}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

## 读取电路板上的标记

以下示例演示了如何使用代码执行来读取电路板上的标记。

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="circuit_board.jpeg")

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    system_instruction="Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block).",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": """Read all visible component labels and markings on this circuit
        board. Reply in JSON: {"components": [{"label": val,
        "location": [y, x]}]}"""}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

![显示电路板上标记的示例](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-circuit-board.png?hl=zh-cn)

## 图片注解

以下示例演示了如何使用代码执行来注解图片（例如，绘制箭头以提供处置说明）并返回修改后的图片。

### Python

```
from google import genai

client = genai.Client()

# Load your image
uploaded_file = client.files.upload(file="sorting.jpeg")

prompt = """
Look at this image and return it as an annotated version using arrows of
different colors to represent which items should go in which bins for
disposal. You must return the final image to the API caller.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
    tools=[{"type": "code_execution"}]
)

print(interaction.output_text)
```

以下是输入图片示例。

![显示时钟的示例](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-image-annotation.png?hl=zh-cn)

模型输出类似于以下内容：

```
  The annotated image shows the suggested disposal locations for the items on the table:
  - **Green bin (Compost/Organic)**: Green chili, red chili, grapes, and cherries.
  - **Blue bin (Recycling)**: Yellow crushed can and plastic container.
  - **Black bin (Trash)**: Chocolate bar wrapper, Welch's packet, and white tissue.
```

## 后续步骤

- [任务编排](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=zh-cn) - 使用自定义机器人 API 的长时程任务。
- [使用流式传输的机器人技术](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-cn) - 实时双向流式传输（仅限 Gemini Robotics ER 2）。
- [视频理解](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=zh-cn) - 时刻查找和进度分类（仅限 Gemini Robotics ER 2）。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-04。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-04。"],[],[]]
