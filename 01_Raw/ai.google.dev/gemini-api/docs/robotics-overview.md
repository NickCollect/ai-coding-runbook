---
source_url: https://ai.google.dev/gemini-api/docs/robotics-overview?hl=zh-CN
fetched_at: 2026-07-27T04:46:07.174055+00:00
title: "Gemini Robotics-ER 1.6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini Robotics-ER 1.6

Gemini Robotics-ER 1.6 是一款视觉-语言模型 (VLM)，可将 Gemini 的智能体功能引入机器人技术领域。它专为在物理世界中进行高级推理而设计，可让机器人解读复杂的视觉数据、执行空间推理，并根据自然语言命令规划行动。

请注意，如果您之前使用的是 Gemini Robotics-ER 1.5，只需在 API 调用中将模型名称从 `model="gemini-robotics-er-1.5-preview"` 替换为 `model="gemini-robotics-er-1.6-preview"`，即可开始使用 1.6 模型。

主要功能和优势：

- **增强的自主性**：机器人可以推理、适应并响应开放式环境中的变化。
- **自然语言互动**：通过使用自然语言分配复杂任务，让机器人更易于使用。
- **任务编排**：将自然语言命令分解为子任务，并与现有的机器人控制器和行为集成，以完成长时程任务。
- **功能多样**：可定位和识别对象、了解对象关系、规划抓取和轨迹，以及解读动态场景。

本文档介绍了[模型的功能](#how-it-works)，并提供了多个[示例](#standard-spatial-reasoning)来突出展示模型的主动性能力。

如果您想立即开始使用，可以在 Google AI Studio 中试用该模型。

[在 Google AI Studio 中试用](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-1.6-preview&hl=zh-cn)

## 安全

虽然 Gemini Robotics-ER 1.6 在设计时就考虑到了安全性，但您仍有责任确保机器人周围的环境安全。生成式 AI 模型可能会出错，而实体机器人可能会造成损坏。安全是我们的首要考虑因素，在将生成式 AI 模型与现实世界中的机器人技术结合使用时，确保其安全性是我们当前研究的一个重要领域。如需了解详情，请访问 [Google DeepMind 机器人安全页面](https://deepmind.google/models/gemini-robotics/safety?hl=zh-cn)。

## 入门：查找场景中的对象

以下示例展示了一个常见的机器人技术用例。此示例展示了如何使用 [`generateContent`](https://ai.google.dev/api/generate-content?hl=zh-cn#method:-models.generatecontent) 方法将图片和文本提示传递给模型，以获取包含已识别对象及其相应 2D 点的列表。该模型会返回其在图片中识别出的商品的点，并返回这些商品的归一化 2D 坐标和标签。

您可以将此输出与机器人 API 搭配使用，也可以调用视觉语言动作 (VLA) 模型或任何其他第三方用户定义的函数，以生成供机器人执行的动作。

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

# Load your image
with open("my-image.png", 'rb') as f:
    image_bytes = f.read()

image_response = client.models.generate_content(
    model="gemini-robotics-er-1.6-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
        PROMPT
    ],
    config = types.GenerateContentConfig(
        temperature=1.0,
        thinking_config=types.ThinkingConfig(thinking_budget=0)
    )
)

print(image_response.text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-1.6-preview:generateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "'"${IMAGE_BASE64}"'"
            }
          },
          {
            "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
          }
        ]
      }
    ],
    "generationConfig": {
      "temperature": 0.5,
      "thinkingConfig": {
        "thinkingBudget": 0
      }
    }
  }'
```

输出将是一个包含对象的 JSON 数组，每个对象都包含一个 `point`（归一化的 `[y, x]` 坐标）和一个用于标识对象的 `label`。

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

下图展示了如何显示这些点：

![显示图片中对象点的示例](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=zh-cn)

## 运作方式

Gemini Robotics-ER 1.6 可让机器人利用空间理解能力在物理世界中了解上下文并开展工作。它可接收图片/视频/音频输入和自然语言提示，以执行以下操作：

- **了解对象和场景背景信息**：识别对象，并推理对象与场景的关系，包括其可供性。
- **理解任务指令**：解读以自然语言给出的任务，例如“找到香蕉”。
- **在空间和时间上进行推理**：了解动作序列以及对象在场景中随时间推移的互动方式。
- **提供结构化输出**：返回表示对象位置的坐标（点或边界框）。

这样，机器人就可以通过编程方式“看到”并“理解”周围环境。

Gemini Robotics-ER 1.6 也是代理模型，这意味着它可以将复杂任务（例如“将苹果放入碗中”）分解为子任务，从而编排长期任务：

- **子任务排序**：将命令分解为一系列逻辑步骤。
- **函数调用/代码执行**：通过调用现有的机器人函数/工具或执行生成的代码来执行步骤。

如需详细了解如何使用 Gemini 进行函数调用，请参阅[函数调用页面](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=zh-cn#how-it-works)。

### 将思考预算与 Gemini Robotics-ER 1.6 搭配使用

Gemini Robotics-ER 1.6 具有灵活的思考预算，可让您控制延迟与准确性之间的权衡。对于物体检测等空间理解任务，模型只需少量思考预算即可实现高性能。对于计数和重量估计等更复杂的推理任务，较大的思考预算会带来更好的效果。这样，您就可以在需要低延迟响应的任务和需要高准确度结果的任务之间取得平衡。

如需详细了解思考预算，请参阅[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)核心功能页面。

## 标准空间推理

以下示例演示了如何使用自然语言提示完成**机器人感知**和空间推理任务，包括在图像中指明和查找对象，以及规划轨迹。为简单起见，这些示例中的代码段已简化，仅显示提示和对 `generate_content` API 的调用。

完整的可运行代码以及其他示例可在 [Robotics cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb) 中找到。

### 指向对象

在机器人技术中，视觉和语言模型 (VLM) 的常见应用场景是在图片或视频帧中指明并找到对象。以下示例要求模型查找图片中的特定对象并返回其坐标。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image and set up your prompt
with open('path/to/image-with-objects.jpg', 'rb') as f:
    image_bytes = f.read()

queries = [
    "bread",
    "starfruit",
    "banana",
]

prompt = f"""
    Get all points matching the following objects: {', '.join(queries)}. The
    label returned should be an identifying name for the object detected.
    The answer should follow the json format:

    [{{"point": , "label": }}, ...]. The points are in

    [y, x] format normalized to 0-1000.
    """

image_response = client.models.generate_content(
  model="gemini-robotics-er-1.6-preview",
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/jpeg',
    ),
    prompt
  ],
  config = types.GenerateContentConfig(
      temperature=1.0,
      thinking_config=types.ThinkingConfig(thinking_budget=0)
  )
)

print(image_response.text)
```

输出将与“入门”示例类似，是一个包含所找到对象的坐标及其标签的 JSON。

```
[
  {"point": [671, 317], "label": "bread"},
  {"point": [738, 307], "label": "bread"},
  {"point": [702, 237], "label": "bread"},
  {"point": [629, 307], "label": "bread"},
  {"point": [833, 800], "label": "bread"},
  {"point": [609, 663], "label": "banana"},
  {"point": [770, 483], "label": "starfruit"}
]
```

![一个示例，用于显示图片中识别出的对象的点](https://ai.google.dev/static/gemini-api/docs/images/robotics/pointing-objects.png?hl=zh-cn)

使用以下提示，让模型解读“水果”等抽象类别，而不是具体对象，并找到图片中的所有实例。

### Python

```
prompt = f"""
        Get all points for fruit. The label returned should be an identifying
        name for the object detected.
        """ + """The answer should follow the json format:
        [{"point": <point>, "label": <label1>}, ...]. The points are in
        [y, x] format normalized to 0-1000."""
```

如需了解其他图片处理技术，请访问[图片理解](https://ai.google.dev/gemini-api/docs/image-understanding?hl=zh-cn)页面。

### 跟踪视频中的对象

Gemini Robotics-ER 1.6 还可以分析视频帧，以跟踪一段时间内的对象。如需查看支持的视频格式列表，请参阅[视频输入](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn#supported-formats)。

以下是用于在模型分析的每个帧中查找特定对象的基本提示：

### Python

```
# Define the objects to find
queries = [
    "pen (on desk)",
    "pen (in robot hand)",
    "laptop (opened)",
    "laptop (closed)",
]

base_prompt = f"""
  Point to the following objects in the provided image: {', '.join(queries)}.
  The answer should follow the json format:

  [{{"point": , "label": }}, ...].

  The points are in [y, x] format normalized to 0-1000.
  If no objects are found, return an empty JSON list [].
  """
```

输出结果显示了在视频帧中跟踪笔和笔记本电脑的过程。

![一个示例，展示了如何在 GIF 中跨帧跟踪对象](https://ai.google.dev/static/gemini-api/docs/images/robotics/object-tracking.gif?hl=zh-cn)

如需查看完整的可运行代码，请参阅[机器人技术食谱](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)。

### 对象检测和边界框

除了单个点之外，该模型还可以返回 2D 边界框，提供包含对象的矩形区域。

此示例请求获取桌面上可识别对象的 2D 边界框。系统指示模型将输出限制为 25 个对象，并为多个实例指定唯一名称。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image and set up your prompt
with open('path/to/image-with-objects.jpg', 'rb') as f:
    image_bytes = f.read()

prompt = """
      Return bounding boxes as a JSON array with labels. Never return masks
      or code fencing. Limit to 25 objects. Include as many objects as you
      can identify on the table.
      If an object is present multiple times, name them according to their
      unique characteristic (colors, size, position, unique characteristics, etc..).
      The format should be as follows: [{"box_2d": [ymin, xmin, ymax, xmax],
      "label": <label for the object>}] normalized to 0-1000. The values in
      box_2d must only be integers
      """

image_response = client.models.generate_content(
  model="gemini-robotics-er-1.6-preview",
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/jpeg',
    ),
    prompt
  ],
  config = types.GenerateContentConfig(
      temperature=1.0,
      thinking_config=types.ThinkingConfig(thinking_budget=0)
  )
)

print(image_response.text)
```

以下内容显示了模型返回的方框。

![一个示例，显示了检测到的对象的边界框](https://ai.google.dev/static/gemini-api/docs/images/robotics/bounding-boxes.png?hl=zh-cn)

如需查看完整的可运行代码，请参阅 [Robotics cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)。
[图像理解](https://ai.google.dev/gemini-api/docs/image-understanding?hl=zh-cn)页面还提供了其他视觉任务示例，例如对象检测和边界框示例。

### 轨迹

Gemini Robotics-ER 1.6 可以生成定义轨迹的点序列，有助于引导机器人运动。

此示例请求将红笔移动到整理器的轨迹，包括起点和一系列中间点。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image and set up your prompt
with open('path/to/image-with-objects.jpg', 'rb') as f:
    image_bytes = f.read()

points_data = []
prompt = """
        Place a point on the red pen, then 15 points for the trajectory of
        moving the red pen to the top of the organizer on the left.
        The points should be labeled by order of the trajectory, from '0'
        (start point at left hand) to <n> (final point)
        The answer should follow the json format:
        [{"point": <point>, "label": <label1>}, ...].
        The points are in [y, x] format normalized to 0-1000.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-1.6-preview",
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/jpeg',
    ),
    prompt
  ],
  config = types.GenerateContentConfig(
      temperature=1.0,
  )
)

print(image_response.text)
```

响应是一组坐标，用于描述红色笔应遵循的轨迹，以完成将其移动到整理器顶部的任务：

```
[
  {"point": [550, 610], "label": "0"},
  {"point": [500, 600], "label": "1"},
  {"point": [450, 590], "label": "2"},
  {"point": [400, 580], "label": "3"},
  {"point": [350, 550], "label": "4"},
  {"point": [300, 520], "label": "5"},
  {"point": [250, 490], "label": "6"},
  {"point": [200, 460], "label": "7"},
  {"point": [180, 430], "label": "8"},
  {"point": [160, 400], "label": "9"},
  {"point": [140, 370], "label": "10"},
  {"point": [120, 340], "label": "11"},
  {"point": [110, 320], "label": "12"},
  {"point": [105, 310], "label": "13"},
  {"point": [100, 305], "label": "14"},
  {"point": [100, 300], "label": "15"}
]
```

![显示计划轨迹的示例](https://ai.google.dev/static/gemini-api/docs/images/robotics/trajectories.png?hl=zh-cn)

## 智能体功能

以下示例展示了如何使用模型的主动能力（尤其是**代码执行**）进行高级**机器人推理**。在这些场景中，模型可以决定编写和执行 Python 代码来处理图片（例如放大、裁剪或旋转），以消除歧义或提高精度，然后再回答问题。

### 对象检测（缩放和裁剪）

以下示例演示了如何使用代码执行功能在检测到对象并返回边界框时缩放和裁剪图片，以便更清晰地查看。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Return JSON in the format {label: val, y: val, x: val, y2: val, x2: val} for
the compostable objects in this scene. Please Zoom and crop the image for a
clearer view. Return an annotated image of the final result with the bounding
boxes drawn on it to the API caller as a part of your process.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-1.6-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        temperature=1.0,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

模型输出将类似如下所示：

```
[
  {"label": "compostable", "y": 256, "x": 482, "y2": 295, "x2": 546},
  {"label": "compostable", "y": 317, "x": 478, "y2": 350, "x2": 542},
  {"label": "compostable", "y": 586, "x": 556, "y2": 668, "x2": 595},
  {"label": "compostable", "y": 463, "x": 669, "y2": 511, "x2": 718},
  {"label": "compostable", "y": 178, "x": 565, "y2": 250, "x2": 609}
]
```

以下内容显示了模型返回的方框。

![一个示例，显示了检测到的对象的边界框](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-bounding-boxes.png?hl=zh-cn)

### 读取模拟仪表并应用逻辑

以下示例演示了如何使用该模型读取模拟表盘并执行时间计算。它使用系统指令来强制生成 JSON 输出。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('clock.jpg', 'rb') as f:
    image_bytes = f.read()

q_time = """
Tell me what the value is. Please respond in the following JSON format:\n {\n "hours": X,\n  "minutes": Y,\n}. Zoom in or crop as necessary to confirm location of the clock hands.
"""

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-1.6-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        system_instruction + " " + q_time
    ],
    config = types.GenerateContentConfig(
        temperature=1.0,
    )
)

print(response.text)
```

以下是输入图片的示例。

![显示时钟的示例](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-clock-reading.png?hl=zh-cn)

模型输出将类似如下所示：

```
Time Response:  {
  "hours": 12,
  "minutes": 44
 }
```

### 测量容器中的液体

以下示例展示了如何使用代码执行功能读取仪表并计算液位百分比。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('meter.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
How full is the meter of liquid?
To read it,
1) Find the points for the top of the sight window, bottom of the sight window and the liquid level, formatted as [y, x] with values ranging from 0-1000;
2) Use math to determine the liquid level as a percentage;
3) Output "Answer: ??" on a separate line, where ?? is a number without % or unit.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-1.6-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        temperature=1.0,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

下图是输入的放大版。

![显示时钟的示例](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-fluid-container.png?hl=zh-cn)

### 读取电路板上的标记

以下示例演示了如何使用代码执行功能读取电路板芯片上的文字，从而让模型能够根据需要缩放、裁剪和旋转图片。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('circuit_board.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = "What is the number on the ESMT chip? Zoom, crop, and rotate if needed."

response = client.models.generate_content(
    model="gemini-robotics-er-1.6-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        temperature=1.0,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

下图是输入的放大版。

![显示时钟的示例](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-circuit-board.png?hl=zh-cn)

### 图片注释

以下示例演示了如何使用代码执行功能来注释图片（例如，绘制箭头以指示处置说明），并返回修改后的图片。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Look at this image and return it as an annotated version using arrows of
different colors to represent which items should go in which bins for
disposal. You must return the final image to the API caller.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-1.6-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        temperature=1.0,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

以下是输入图片的示例。

![显示时钟的示例](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-image-annotation.png?hl=zh-cn)

模型输出将类似如下所示：

```
The annotated image shows the suggested disposal locations for the items on the table:
- **Green bin (Compost/Organic)**: Green chili, red chili, grapes, and cherries.
- **Blue bin (Recycling)**: Yellow crushed can and plastic container.
- **Black bin (Trash)**: Chocolate bar wrapper, Welch's packet, and white tissue.
```

## 编排

Gemini Robotics-ER 1.6 可以执行**任务规划**和更高级别的空间推理，根据上下文理解来推断动作或确定最佳位置，从而编排长时程任务。

### 为笔记本电脑腾出空间

此示例展示了 Gemini Robotics-ER 如何对空间进行推理。此提示要求模型确定需要移动哪个对象才能为另一项物品腾出空间。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image and set up your prompt
with open('path/to/image-with-objects.jpg', 'rb') as f:
    image_bytes = f.read()

prompt = """
          Point to the object that I need to remove to make room for my laptop
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-1.6-preview",
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/jpeg',
    ),
    prompt
  ],
  config = types.GenerateContentConfig(
      temperature=1.0,
      thinking_config=types.ThinkingConfig(thinking_budget=0)
  )
)

print(image_response.text)
```

响应包含回答用户问题的对象的二维坐标，在本例中，该对象应移动以腾出空间放置笔记本电脑。

```
[
  {"point": [672, 301], "label": "The object that I need to remove to make room for my laptop"}
]
```

![一个示例，显示了需要移动哪个对象才能移动另一个对象](https://ai.google.dev/static/gemini-api/docs/images/robotics/spatial-reasoning.png?hl=zh-cn)

### 打包午餐

该模型还可以为多步骤任务提供指令，并指出每个步骤的相关对象。此示例展示了模型如何规划一系列步骤来打包午餐袋。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image and set up your prompt
with open('path/to/image-of-lunch.jpg', 'rb') as f:
    image_bytes = f.read()

prompt = """
          Explain how to pack the lunch box and lunch bag. Point to each
          object that you refer to. Each point should be in the format:
          [{"point": [y, x], "label": }], where the coordinates are
          normalized between 0-1000.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-1.6-preview",
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/jpeg',
    ),
    prompt
  ],
  config = types.GenerateContentConfig(
      temperature=1.0,
      thinking_config=types.ThinkingConfig(thinking_budget=0)
  )
)

print(image_response.text)
```

此提示的回答是一组关于如何打包图片输入中的午餐袋的分步说明。

**输入图片**

![图片：一个午餐盒以及要放入其中的物品](https://ai.google.dev/static/gemini-api/docs/images/robotics/packing-lunch.png?hl=zh-cn)

**模型输出**

```
Based on the image, here is a plan to pack the lunch box and lunch bag:

1.  **Pack the fruit into the lunch box.** Place the [apple](apple), [banana](banana), [red grapes](red grapes), and [green grapes](green grapes) into the [blue lunch box](blue lunch box).
2.  **Add the spoon to the lunch box.** Put the [blue spoon](blue spoon) inside the lunch box as well.
3.  **Close the lunch box.** Secure the lid on the [blue lunch box](blue lunch box).
4.  **Place the lunch box inside the lunch bag.** Put the closed [blue lunch box](blue lunch box) into the [brown lunch bag](brown lunch bag).
5.  **Pack the remaining items into the lunch bag.** Place the [blue snack bar](blue snack bar) and the [brown snack bar](brown snack bar) into the [brown lunch bag](brown lunch bag).

Here is the list of objects and their locations:
*   [{"point": [899, 440], "label": "apple"}]
*   [{"point": [814, 363], "label": "banana"}]
*   [{"point": [727, 470], "label": "red grapes"}]
*   [{"point": [675, 608], "label": "green grapes"}]
*   [{"point": [706, 529], "label": "blue lunch box"}]
*   [{"point": [864, 517], "label": "blue spoon"}]
*   [{"point": [499, 401], "label": "blue snack bar"}]
*   [{"point": [614, 705], "label": "brown snack bar"}]
*   [{"point": [448, 501], "label": "brown lunch bag"}]
```

### 调用自定义机器人 API

此示例演示了如何使用自定义机器人 API 进行任务编排。它引入了一个专为放置操作设计的模拟 API。任务是拿起一个蓝色积木，然后将其放入橙色碗中：

![方块和碗的图片](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png?hl=zh-cn)

与本页上的其他示例类似，完整的可运行代码可在 [Robotics cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb) 中找到。

第一步是使用以下提示找到这两个商品：

### Python

```
prompt = """
            Locate and point to the blue block and the orange bowl. The label
            returned should be an identifying name for the object detected.
            The answer should follow the json format: [{"point": <point>, "label": <label1>}, ...].
            The points are in [y, x] format normalized to 0-1000.
          """
```

模型响应包含积木和碗的归一化坐标：

```
[
  {"point": [389, 252], "label": "orange bowl"},
  {"point": [727, 659], "label": "blue block"}
]
```

此示例使用以下模拟机器人 API：

### Python

```
def move(x, y, high):
  print(f"moving to coordinates: {x}, {y}, {15 if high else 5}")

def setGripperState(opened):
  print("Opening gripper" if opened else "Closing gripper")

def returnToOrigin():
  print("Returning to origin pose")
```

下一步是调用一系列 API 函数，其中包含执行操作所需的逻辑。以下提示包含机器人 API 的说明，模型在编排此任务时应使用该 API。

### Python

```
prompt = f"""
    You are a robotic arm with six degrees-of-freedom. You have the
    following functions available to you:

    def move(x, y, high):
      # moves the arm to the given coordinates. The boolean value 'high' set
      to True means the robot arm should be lifted above the scene for
      avoiding obstacles during motion. 'high' set to False means the robot
      arm should have the gripper placed on the surface for interacting with
      objects.

    def setGripperState(opened):
      # Opens the gripper if opened set to true, otherwise closes the gripper

    def returnToOrigin():
      # Returns the robot to an initial state. Should be called as a cleanup
      operation.

    The origin point for calculating the moves is at normalized point
    y={robot_origin_y}, x={robot_origin_x}. Use this as the new (0,0) for
    calculating moves, allowing x and y to be negative.
    Perform a pick and place operation where you pick up the blue block at
    normalized coordinates ({block_x}, {block_y}) (relative coordinates:
    {block_relative_x}, {block_relative_y}) and place it into the orange
    bowl at normalized coordinates ({bowl_x}, {bowl_y})
    (relative coordinates: {bowl_relative_x}, {bowl_relative_y}).
    Provide the sequence of function calls as a JSON list of objects, where
    each object has a "function" key (the function name) and an "args" key
    (a list of arguments for the function).
    Also, include your reasoning before the JSON output.
    For example:
    Reasoning: To pick up the block, I will first move the arm to a high
    position above the block, open the gripper, move down to the block,
    close the gripper, lift the arm, move to a high position above the bowl,
    move down to the bowl, open the gripper, and then lift the arm back to
    a high position.
"""
```

以下内容展示了模型基于提示和模拟机器人 API 的可能输出。输出包括模型思考过程以及由此规划的任务。它还显示了模型按顺序排列的机器人函数调用的输出。

```
Reasoning: To perform the pick and place operation, I will first move the
robotic arm to a high position above the blue block to ensure clearance. Then, I
will open the gripper in preparation for grasping. Next, I will lower the arm to
the surface level to position the gripper around the block and close the gripper
to secure it. After picking up the block, I will lift the arm to clear the
surface and move towards the orange bowl, maintaining a high position to avoid
collisions. Once positioned above the bowl, I will lower the arm to place the
block inside. I will then open the gripper to release the block. Finally, I will
lift the arm out of the bowl and call `returnToOrigin` to reset the robot's
state.

[
  {
    "function": "move",
    "args": [
      163,
      427,
      true
    ]
  },
  {
    "function": "setGripperState",
    "args": [
      true
    ]
  },
  {
    "function": "move",
    "args": [
      163,
      427,
      false
    ]
  },
  {
    "function": "setGripperState",
    "args": [
      false
    ]
  },
  {
    "function": "move",
    "args": [
      163,
      427,
      true
    ]
  },
  {
    "function": "move",
    "args": [
      -247,
      90,
      true
    ]
  },
  {
    "function": "move",
    "args": [
      -247,
      90,
      false
    ]
  },
  {
    "function": "setGripperState",
    "args": [
      true
    ]
  },
  {
    "function": "move",
    "args": [
      -247,
      90,
      true
    ]
  },
  {
    "function": "returnToOrigin",
    "args": []
  }
]

Executing Function Calls:
moving to coordinates: 163, 427, 15
Opening gripper
moving to coordinates: 163, 427, 5
Closing gripper
moving to coordinates: 163, 427, 15
moving to coordinates: -247, 90, 15
moving to coordinates: -247, 90, 5
Opening gripper
moving to coordinates: -247, 90, 15
Returning to origin pose
```

## 最佳做法

为了优化机器人应用的性能和准确性，务必要了解如何有效地与 Gemini 模型互动。本部分概述了有关如何精心设计提示、处理视觉数据和构建任务的最佳实践和关键策略，以获得最可靠的结果。

1. 使用清晰简洁的语言。

   - **使用自然语言**：Gemini 模型旨在理解自然对话语言。以语义清晰的方式构建提示，并模仿人们自然给出指令的方式。
   - **使用日常用语**：选择常用日常用语，而非技术性或专业术语。如果模型对某个特定术语的回答不尽如人意，请尝试使用更常见的同义词重新措辞。
2. 优化视觉输入。

   - **放大以查看细节**：如果拍摄对象较小或在广角镜头中难以辨别，请使用边界框功能来隔离感兴趣的对象。然后，您可以根据此选择框剪裁图片，并将剪裁后的新图片发送给模型，以进行更详细的分析。
   - **尝试不同的光线和颜色**：模型对图像的感知可能会受到光线条件不佳和颜色对比度差的影响。
3. 将复杂的问题分解为较小的步骤。通过单独处理每个较小的步骤，您可以引导模型获得更精确、更成功的结果。
4. 通过共识提高准确性。对于需要高精确度的任务，您可以多次使用同一提示查询模型。通过对返回的结果求平均值，您可以得出通常更准确、更可靠的“共识”。

## 限制

使用 Gemini Robotics-ER 1.6 进行开发时，请考虑以下限制：

- **预览版状态**：该模型目前处于**预览版**阶段。API 和功能可能会发生变化，未经全面测试，可能不适合用于对生产至关重要的应用。
- **延迟时间**：复杂的查询、高分辨率输入或广泛的 `thinking_budget` 可能会导致处理时间增加。
- **幻觉**：与所有大语言模型一样，Gemini Robotics-ER 1.6 有时也会产生“幻觉”或提供不正确的信息，尤其是在提示不明确或输入超出分布范围时。
- **对提示质量的依赖性**：模型输出的质量高度依赖于输入提示的清晰度和具体性。模糊不清或结构不合理的提示可能会导致结果不理想。
- **计算成本**：运行模型（尤其是使用视频输入或高 `thinking_budget` 时）会消耗计算资源并产生费用。如需了解详情，请参阅[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)页面。
- **输入类型**：如需详细了解每种模式的限制，请参阅以下主题。
  - [图片输入](https://ai.google.dev/gemini-api/docs/image-understanding?hl=zh-cn#technical-details-image)
  - [视频输入](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn#supported-formats)
  - [音频输入](https://ai.google.dev/gemini-api/docs/audio?hl=zh-cn#supported-formats)

## 隐私权声明

您确认，本文档中提及的模型（以下简称“机器人模型”）会利用视频和音频数据来运行您的硬件并按照您的指令移动。因此，您可能会操作机器人模型，以便机器人模型收集可识别个人的数据，例如语音、图像和肖像数据（“个人数据”）。如果您选择以会收集个人数据的方式操作机器人模型，则表示您同意，除非且直到可识别身份的个人充分了解并同意其个人数据可能会按照 [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=zh-cn)（以下简称“条款”）中所述的方式提供给 Google 并由 Google 使用（包括按照标题为“Google 如何使用您的数据”的部分中所述的方式），否则您不得允许任何可识别身份的个人与机器人模型互动或出现在机器人模型周围的区域。您应确保此类通知允许按照本条款的规定收集和使用个人数据，并且您将尽商业上合理的努力，通过使用面部模糊处理等技术以及在不包含可识别人员的区域内操作机器人模型，尽可能减少个人数据的收集和分发。

## 价格

如需详细了解价格和可用地区，请参阅[价格](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)页面。

## 模型版本

### Robotics-ER 1.6 预览版

| 属性 | 说明 |
| --- | --- |
| id\_card 模型代码 | `gemini-robotics-er-1.6-preview` |
| 保存支持的数据类型 | **输入源**  文本、图片、视频、音频  **输出**  文本 |
| token\_auto令牌限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn) | **输入 token 限制**  131,072  **输出 token 限制**  65536 |
| handyman功能 | **[音频生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn)**  不受支持  **[缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)**  支持  **[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)**  支持  **[计算机使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)**  支持  **[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)**  支持  **[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)**  支持  **[依托 Google 地图进行接地](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn)**  支持  **[图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)**  不受支持  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-cn)**  不受支持  **[搜索接地](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)**  支持  **[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)**  支持  **[思考型](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)**  支持  **[网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)**  支持 |
| speed使用选项 | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn)**  支持  **[灵活推理](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-cn)**  支持  **[优先推断](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-cn)**  支持 |
| 123 版本 | 如需了解详情，请参阅[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#model-versions)。  - 预览：`gemini-robotics-er-1.6-preview` |
| calendar\_month最新更新 | 2025 年 12 月 |
| cognition\_2知识截点 | 2025 年 1 月 |

## 后续步骤

- 探索其他功能，并继续尝试使用不同的提示和输入，以发现 Gemini Robotics-ER 1.6 的更多应用。
  如需查看更多示例，请参阅 [Robotics 入门 Colab](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)。
- 如需了解 Gemini 机器人模型在构建时如何考虑安全性，请访问 [Google DeepMind 机器人安全页面](https://deepmind.google/models/gemini-robotics/safety?hl=zh-cn)。
- 如需了解 Gemini Robotics 模型的最新更新，请访问 [Gemini Robotics 着陆页](https://deepmind.google/robotics?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-13。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-13。"],[],[]]
