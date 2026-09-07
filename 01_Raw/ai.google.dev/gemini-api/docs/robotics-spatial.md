---
source_url: https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=ja
fetched_at: 2026-09-07T05:46:19.027782+00:00
title: "\u7a7a\u9593\u63a8\u8ad6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# 空間推論

Gemini Robotics ER モデルは、オブジェクトを指し示し、動画内でオブジェクトを追跡し、境界ボックスでオブジェクトを検出し、移動軌跡を生成できます。

実行可能な完全なコードについては、[ロボティクス クックブック](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)をご覧ください。

## オブジェクトを指す

次の例では、画像内の特定のオブジェクトを検出し、正規化された `[y, x]` 座標を返します。

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

出力は、オブジェクトを含む JSON 配列になります。各オブジェクトには、オブジェクトを識別する `point`（正規化された `[y, x]` 座標）と `label` が含まれます。

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

次の図は、これらのポイントを表示する方法の例です。

![画像内のオブジェクトのポイントを表示する例](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=ja)

## 動画内のオブジェクトのトラッキング

Gemini Robotics ER 2 は、動画フレームを分析して、オブジェクトを時間経過とともに追跡することもできます。サポートされている動画形式の一覧については、[動画入力](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja#supported-formats)をご覧ください。

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

## オブジェクト検出と境界ボックス

ポイントに加えて、モデルに 2D 境界ボックスを返すようにプロンプトを設定することもできます。これにより、検出されたオブジェクトの空間的な詳細情報が提供されます。

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

Gemini Robotics ER 2 は、軌跡を定義する一連の点を生成できます。これは、ロボットの動きをガイドするのに役立ちます。

この例では、赤いペンをオーガナイザーに移動する軌跡をリクエストしています。これには、中間経由地の推定値が含まれます。コードはプロンプトのみを表示するように縮小されています。

### Python

```
prompt = """
          Generate a trajectory for the robotic arm to pick up the red pen
          and place it in the organizer. Return a list of waypoints as JSON:
          [{"step": <int>, "point": [y, x], "action": <description>}, ...]
          where coordinates are normalized to 0-1000.
        """
```

## ノートパソコンを置くスペースを確保する

この例は、Gemini Robotics ER が空間について推論する方法を示しています。プロンプトは、別のアイテムのスペースを確保するために移動する必要があるオブジェクトを特定するようにモデルに指示します。

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

レスポンスには、ユーザーの質問に答えるオブジェクトの 2D 座標が含まれています。この場合、ノートパソコンを置くために移動する必要があるオブジェクトです。

```
[
  {"point": [672, 301], "label": "The object that I need to remove to make room for my laptop"}
]
```

![別のオブジェクトのために移動する必要があるオブジェクトを示す例](https://ai.google.dev/static/gemini-api/docs/images/robotics/spatial-reasoning.png?hl=ja)

## お弁当の準備

モデルは、複数ステップのタスクの手順を提供し、各ステップに関連するオブジェクトを指すこともできます。この例では、モデルがランチバッグを詰める一連の手順を計画する方法を示します。

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

このプロンプトのレスポンスは、画像入力からランチバッグを詰める方法に関する手順のセットです。

**入力画像**

![お弁当箱と中に入れるものの画像](https://ai.google.dev/static/gemini-api/docs/images/robotics/packing-lunch.png?hl=ja)

**モデル出力**

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

## 次のステップ

- [エージェント機能](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=ja) - コード実行、計測器の読み取り、画像アノテーション。
- [タスク オーケストレーション](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ja) - カスタム ロボット API を使用した長期的なタスク。
- [ストリーミングを使用したロボティクス](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ja) - リアルタイム双方向ストリーミング（Gemini Robotics ER 2 のみ）。
- [動画の理解](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ja) - 瞬間検出と進捗状況の分類（Gemini Robotics ER 2 のみ）。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-30 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-30 UTC。"],[],[]]
