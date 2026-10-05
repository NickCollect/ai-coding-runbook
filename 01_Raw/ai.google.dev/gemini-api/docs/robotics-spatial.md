---
source_url: https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=zh-TW
fetched_at: 2026-10-05T06:51:13.680462+00:00
title: "\u7a7a\u9593\u63a8\u8ad6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 空間推論

Gemini Robotics ER 模型可以指向物件、在影片中追蹤物件、以定界框偵測物件，以及生成移動軌跡。

如需完整的可執行程式碼，請參閱「[機器人食譜](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)」。

## 對準物件

以下範例會在圖片中尋找特定物件，並傳回標準化的 `[y, x]` 座標：

### Python

```
from google import genai

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

image_response = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": PROMPT}
    ],
    generation_config={"thinking_level": "high"},
)

print(image_response.output_text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-robotics-er-2-preview",
    "input": {
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
    },
    "generation_config": {
      "thinking_config": {
        "thinking_level": "high"
      }
    }
  }'
```

輸出內容會是包含物件的 JSON 陣列，每個物件都有 `point` (標準化 `[y, x]` 座標) 和用於識別物件的 `label`。

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

下圖顯示這些點的範例：

![顯示圖片中物體點的範例](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=zh-tw)

## 追蹤影片中的物件

Gemini Robotics ER 2 也能分析影片影格，追蹤一段時間內的物體。如需支援的影片格式清單，請參閱「[影片輸入](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-tw#supported-formats)」。

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="my-video.mp4")

prompt = """
          Point to the red ball in every frame where it appears.
          The answer should follow the json format: [{"point": [y, x],
          "label": <label>}, ...]. The points are in [y, x] format
          normalized to 0-1000. Return one entry per frame that contains
          the object.
        """

image_response = client.interactions.create(
  model="gemini-robotics-er-2-preview",
  input=[
    {
        "type": "video",
        "uri": uploaded_file.uri,
        "mime_type": uploaded_file.mime_type
    },
    {"type": "text", "text": prompt}
  ],
)

print(image_response.output_text)
```

## 物件偵測和定界框

除了點之外，您也可以提示模型傳回 2D 定界框，為偵測到的物件提供更多空間細節。

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

prompt = """
          Detect all objects in this image and return bounding boxes.
          The answer should follow the JSON format:
          [{"label": <label>, "y": <y_min>, "x": <x_min>,
            "y2": <y_max>, "x2": <x_max>}, ...]
          where coordinates are normalized to 0-1000.
        """

image_response = client.interactions.create(
  model="gemini-robotics-er-2-preview",
  input=[
    {
        "type": "image",
        "uri": uploaded_file.uri,
        "mime_type": uploaded_file.mime_type
    },
    {"type": "text", "text": prompt}
  ],
)

print(image_response.output_text)
```

## 軌跡

Gemini Robotics ER 2 可生成定義軌跡的點序列，有助於引導機器人移動。

這個範例要求將紅筆移動到收納盒的軌跡，包括中間路徑點的估計值。程式碼已縮減，只顯示提示。

### Python

```
prompt = """
          Generate a trajectory for the robotic arm to pick up the red pen
          and place it in the organizer. Return a list of waypoints as JSON:
          [{"step": <int>, "point": [y, x], "action": <description>}, ...]
          where coordinates are normalized to 0-1000.
        """
```

## 為筆電騰出空間

這個範例顯示 Gemini Robotics ER 如何推論空間。提示會要求模型找出需要移動的物件，以便為其他項目騰出空間。

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/image-with-objects.jpg")

prompt = """
          Point to the object that I need to remove to make room for my laptop
          The answer should follow the JSON format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000.
        """

image_response = client.interactions.create(
  model="gemini-robotics-er-2-preview",
  input=[
    {
        "type": "image",
        "uri": uploaded_file.uri,
        "mime_type": uploaded_file.mime_type
    },
    {"type": "text", "text": prompt}
  ],
)

print(image_response.output_text)
```

回覆內容包含可回答使用者問題的物體 2D 座標，在本例中，該物體應移動，為筆電騰出空間。

```
[
  {"point": [672, 301], "label": "The object that I need to remove to make room for my laptop"}
]
```

![範例：顯示另一個物件需要移動的物件](https://ai.google.dev/static/gemini-api/docs/images/robotics/spatial-reasoning.png?hl=zh-tw)

## 準備午餐

模型也能提供多步驟工作的操作說明，並指出每個步驟的相關物件。這個範例說明模型如何規劃一系列步驟來打包午餐袋。

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/image-of-lunch.jpg")

prompt = """
          Explain how to pack the lunch box and lunch bag. Point to each
          object that you refer to. Each point should be in the format:
          [{"point": [y, x], "label": }], where the coordinates are
          normalized between 0-1000.
        """

image_response = client.interactions.create(
  model="gemini-robotics-er-2-preview",
  input=[
    {
        "type": "image",
        "uri": uploaded_file.uri,
        "mime_type": uploaded_file.mime_type
    },
    {"type": "text", "text": prompt}
  ],
)

print(image_response.output_text)
```

這個提示詞的回覆內容是一組逐步說明，教導如何包裝圖片輸入內容中的午餐袋。

**輸入圖片**

![午餐盒和要放入其中的物品圖片](https://ai.google.dev/static/gemini-api/docs/images/robotics/packing-lunch.png?hl=zh-tw)

**模型輸出內容**

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

## 後續步驟

- [代理能力](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=zh-tw)：執行程式碼、讀取儀器、標註圖片。
- [工作流程協調](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=zh-tw)：使用自訂機器人 API 執行長期任務。
- [串流機器人](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-tw)：即時雙向串流 (僅限 Gemini Robotics ER 2)。
- [影片理解](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=zh-tw)：尋找特定時刻和進度分類 (僅限 Gemini Robotics ER 2)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-09-08 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-09-08 (世界標準時間)。"],[],[]]
