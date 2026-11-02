---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=ja
fetched_at: 2026-11-02T07:11:14.289514+00:00
title: "\u30a8\u30fc\u30b8\u30a7\u30f3\u30c8\u306e\u30d3\u30b8\u30e7\u30f3\u6a5f\u80fd \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs/generate-content?hl=ja)

フィードバックを送信

# エージェントのビジョン機能

Gemini Robotics ER モデルは、Python コードを記述して実行し、画像を操作してロジックを適用してから回答できます。このページでは、コード実行の例として、ズームと切り抜きによるオブジェクト検出、計測器の読み取り、流体の測定、回路基板の読み取り、画像アノテーションについて説明します。

これらの例を独自のユースケースに合わせるには、プロンプト テキストとアップロードした画像ファイルを独自のファイルに置き換えます。また、プロンプトでリクエストされた JSON スキーマを、アプリケーションに必要な出力構造に合わせて調整したり、`system_instruction` を追加して出力形式と精度を強制したりすることもできます。

実行可能な完全なコードについては、
[ロボット工学のクックブック](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)をご覧ください。

## 思考レベル

思考レベルを制御して、レイテンシと精度のバランスを取ることができます。オブジェクト検出などの空間タスクは、思考レベルが低い場合に適切に機能します。カウントや重量推定などの複雑なタスクでは、思考レベルを高くすると効果的です。

次の例では、複雑なカウントタスクの思考レベルを `high` に設定しています。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('scene.jpeg', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        "Identify and count all objects on the table."
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    )
)

print(response.text)
```

詳細については、[思考](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ja)をご覧ください。

## オブジェクト検出（ズームと切り抜き）

次の例は、コード実行を使用して画像をズームして切り抜き、オブジェクトを検出してバウンディング ボックスを返すときに、より鮮明に表示する方法を示しています。

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
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

モデル出力は、次の JSON レスポンスのようになります。

```
[
  {"label": "compostable", "y": 256, "x": 482, "y2": 295, "x2": 546},
  {"label": "compostable", "y": 317, "x": 478, "y2": 350, "x2": 542},
  {"label": "compostable", "y": 586, "x": 556, "y2": 668, "x2": 595},
  {"label": "compostable", "y": 463, "x": 669, "y2": 511, "x2": 718},
  {"label": "compostable", "y": 178, "x": 565, "y2": 250, "x2": 609}
]
```

次の画像は、モデルから返されたボックスを示しています。

![検出されたオブジェクトの境界ボックスを示す例](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-bounding-boxes.png?hl=ja)

## アナログ メーターを読み取り、ロジックを適用する

次の例は、モデルを使用してアナログ メーターを読み取り、時間計算を行う方法を示しています。システム命令を使用して JSON 出力を強制します。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('gauge.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read the current value from this gauge. Then, calculate how long
        it will take at the current rate for the value to reach maximum.
        Reply in JSON: {"current_value": val, "max_value": val,
        "time_to_max_minutes": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## 容器内の流体を測定する

次の例は、コード実行を使用して容器内の流体のレベルを測定する方法を示しています。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('fluid.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Measure the amount of fluid in the container. Reply in JSON:
        {"fluid_level_ml": val, "container_capacity_ml": val,
        "percentage_full": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## 回路基板のマーキングを読み取る

次の例は、コード実行を使用して回路基板のマーキングを読み取る方法を示しています。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('circuit_board.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read all visible component labels and markings on this circuit
        board. Reply in JSON: {"components": [{"label": val,
        "location": [y, x]}]}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

![回路基板のマーキングの例](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-circuit-board.png?hl=ja)

## 画像アノテーション

次の例は、コード実行を使用して画像にアノテーションを付け（廃棄手順を示す矢印を描画するなど）、変更した画像を返す方法を示しています。

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
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

画像入力の例を次に示します。

![時計の読み取りの例](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-image-annotation.png?hl=ja)

モデルの出力は次のようになります。

```
  The annotated image shows the suggested disposal locations for the items on the table:
  - **Green bin (Compost/Organic)**: Green chili, red chili, grapes, and cherries.
  - **Blue bin (Recycling)**: Yellow crushed can and plastic container.
  - **Black bin (Trash)**: Chocolate bar wrapper, Welch's packet, and white tissue.
```

## 次のステップ

- [タスク オーケストレーション](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ja) - カスタム ロボット API を使用した長期的なタスク。
- [ストリーミングによるロボット工学](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ja) - リアルタイムの双方向ストリーミング（Gemini Robotics ER 2 のみ）。
- [動画理解](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ja) - モーメントの検出と進捗状況の分類（Gemini Robotics ER 2 のみ）。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-08 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-08 UTC。"],[],[]]
