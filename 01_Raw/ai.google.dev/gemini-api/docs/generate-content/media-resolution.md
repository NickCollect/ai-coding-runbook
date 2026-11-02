---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=ja
fetched_at: 2026-11-02T07:16:19.155958+00:00
title: "\u30e1\u30c7\u30a3\u30a2\u306e\u89e3\u50cf\u5ea6 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs/generate-content?hl=ja)

フィードバックを送信

# メディアの解像度

`media_resolution` パラメータは、メディア入力に割り当てられる**トークンの最大数**を決定することで、Gemini API が画像、動画、音声、PDF ドキュメントなどのメディア入力を処理する方法を制御します。これにより、レスポンスの品質とレイテンシ、費用のバランスを調整できます。ビジュアル入力とドキュメント入力では、解像度の設定に基づいてトークンの割り当てがスケーリングされますが、音声入力は、すべての解像度レベルで 1 秒あたり固定レートでトークン化されます。さまざまな設定、デフォルト値、トークンとの対応については、[トークン数](#token-counts)セクションをご覧ください。

メディアの解像度は、次の 2 つの方法で構成できます。

- [パーツごと](#per-part-media-resolution)（Gemini 4 モデルと Gemini 3 モデル）
- `generateContent` リクエスト全体（すべてのマルチモーダル モデル）に対して[グローバル](#global-media-resolution)

## パートごとのメディア解像度（Gemini 4、Gemini 3）

Gemini 4 と Gemini 3 では、リクエスト内の個々のメディア オブジェクトにメディア解像度を設定できるため、トークンの使用量を細かく最適化できます。1 つのリクエストで複数の解像度レベルを混在させることができます。たとえば、複雑な図には高解像度を使用し、コンテキスト画像には低解像度を使用します。この設定は、特定の部分のグローバル構成をオーバーライドします。デフォルト設定については、[トークン数](#token-counts)セクションをご覧ください。

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is available in the v1beta API version.
client = genai.Client(
  http_options={
      'api_version': 'v1beta',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-4-argon'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1beta' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-4-argon';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-4-argon"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## グローバル メディアの解像度

`GenerationConfig` を使用して、リクエスト内のすべてのメディア要素のデフォルト解像度を設定できます。これは、すべてのマルチモーダル モデルでサポートされています。リクエストにグローバル設定と[パートごとの設定](#per-part-media-resolution)の両方が含まれている場合、その特定のアイテムにはパートごとの設定が優先されます。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## 使用可能な解像度の値

Gemini API では、メディアの解像度について次のレベルが定義されています。

- `MEDIA_RESOLUTION_UNSPECIFIED`: デフォルト設定。このレベルのトークン数は、Gemini 3 と以前の Gemini モデルで大きく異なります。
- `MEDIA_RESOLUTION_LOW`: トークン数が少なくなり、処理が高速化され、コストが削減されますが、詳細度は低くなります。
- `MEDIA_RESOLUTION_MEDIUM`: 詳細、費用、レイテンシのバランスが取れています。
- `MEDIA_RESOLUTION_HIGH`: トークン数が多いほど、モデルが処理する詳細情報が増えますが、レイテンシと費用が増加します。
- `MEDIA_RESOLUTION_ULTRA_HIGH`（パート単位のみ）: トークン数が最も多く、[コンピュータの使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)などの特定のユースケースに必要です。

`MEDIA_RESOLUTION_HIGH` はほとんどのユースケースで最適なパフォーマンスを提供します。

これらの各レベルで生成されるトークンの正確な数は、**メディアタイプ**（画像、動画、音声、PDF）と**モデル バージョン**の両方によって異なります。

## トークン数

次の表に、モデル ファミリーごとの各 `media_resolution` 値とメディアタイプの概算トークン数を示します。

**Gemini 3 モデル**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **画像** | **動画** | **音声** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED`（デフォルト） | 1120 | 70 | 25（1 秒あたり） | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 25（1 秒あたり） | 280 + ネイティブ テキスト |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 25（1 秒あたり） | 560 + ネイティブ テキスト |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 25（1 秒あたり） | 1120 + ネイティブ テキスト |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2,240 | なし | なし | なし |

**Gemini 2.5 モデル**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **MediaResolution** | **画像** | **動画** | **音声** | **PDF（スキャン済み）** | **PDF（ネイティブ）** |
| `MEDIA_RESOLUTION_UNSPECIFIED`（デフォルト） | 256 + パン＆スキャン（約 2,048） | 256 | 32（1 秒あたり） | 256 + OCR | 256 + ネイティブ テキスト |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 32（1 秒あたり） | 64 + OCR | 64 + ネイティブ テキスト |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 32（1 秒あたり） | 256 + OCR | 256 + ネイティブ テキスト |
| `MEDIA_RESOLUTION_HIGH` | 256 + パン＆スキャン | 256 | 32（1 秒あたり） | 256 + OCR | 256 + ネイティブ テキスト |

## 適切な解像度の選択

- **デフォルト（`UNSPECIFIED`）:** デフォルトから始めます。最も一般的なユースケースで、品質、レイテンシ、費用のバランスが取れるように調整されています。
- **`LOW`:** 費用とレイテンシが最重要で、詳細な情報はそれほど重要でないシナリオで使用します。
- **`MEDIUM` / `HIGH`:** タスクでメディア内の複雑な詳細を理解する必要がある場合は、解像度を上げます。これは、複雑な視覚分析、グラフの読み取り、高密度のドキュメントの理解によく必要になります。
- **`ULTRA HIGH`** - パーツごとの設定でのみ使用できます。パソコンの使用など、特定のユースケースや、テストで `HIGH` よりも明確な改善が見られる場合に推奨されます。
- **パートごとの制御（Gemini 4 と Gemini 3）:** トークンの使用量を最適化します。たとえば、複数の画像を含むプロンプトでは、複雑な図には `HIGH` を使用し、シンプルなコンテキスト画像には `LOW` または `MEDIUM` を使用します。

**おすすめの設定**

以下に、サポートされている各メディア タイプに推奨されるメディア解像度設定を示します。

|  |  |  |  |
| --- | --- | --- | --- |
| **メディアタイプ** | **推奨設定** | **最大トークン数** | **使用方法** |
| **画像検索** | `MEDIA_RESOLUTION_HIGH` | 1120 | 品質を最大限に高めるために、ほとんどの画像分析タスクに推奨されます。 |
| **PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | ドキュメントの理解に最適です。通常、品質は `medium` で飽和します。`high` に増やしても、標準ドキュメントの OCR 結果が改善されることはほとんどありません。 |
| **動画**（一般） | `MEDIA_RESOLUTION_LOW`（または `MEDIA_RESOLUTION_MEDIUM`） | 70（フレームあたり） | **注:** 動画の場合、コンテキストの使用を最適化するために、`low` と `medium` の設定は同じ（70 トークン）として扱われます。これは、ほとんどのアクション認識タスクと説明タスクに十分です。 |
| **動画**（テキストが多い） | `MEDIA_RESOLUTION_HIGH` | 280（フレームあたり） | ユースケースで、密度の高いテキスト（OCR）や動画フレーム内の小さな詳細を読み取る必要がある場合にのみ必要です。 |
| **音声** | `MEDIA_RESOLUTION_UNSPECIFIED`（デフォルト） | Gemini 3 の場合は 25（/秒）、Gemini 2.5 の場合は 32（/秒） | 音声は、サポートされているすべての解像度設定（`unspecified`、`low`、`medium`、`high`）で、1 秒あたり固定レートでトークン化されます。 |

さまざまな解像度設定が特定のアプリケーションに与える影響を常にテストして評価し、品質、レイテンシ、費用の最適なトレードオフを見つけてください。

## 動画処理モードとの関係

`media_resolution` と処理パラメータは、動画入力のさまざまな側面を制御します。

- `media_resolution` は、各フレームの**解像度**（フレームあたりのトークン数）を制御します。
- `processing` / `media_processing` は、**動画のどのコンテンツ**をコンテキストに読み込むかを制御します。

同じ動画入力に両方を設定できます。たとえば、メディア解像度の低いエージェント処理を使用して、長い動画の合計トークン使用量を最小限に抑えることができます。

動画処理モードの詳細については、[エージェントによる動画理解](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ja#agentic-video-understanding)のガイドをご覧ください。

## バージョンの互換性の概要

- `MediaResolution` 列挙型は、メディア入力をサポートするすべてのモデルで使用できます。
- 各列挙型レベルに関連付けられたトークン数は、Gemini 4 / Gemini 3 モデルと以前の Gemini バージョンで**異なります**。
- 個々の `Part` オブジェクトに `media_resolution` を設定することは、**Gemini 4 モデルと Gemini 3 モデルでサポートされています**。

## 次のステップ

- Gemini API のマルチモーダル機能の詳細については、[画像理解](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=ja)、[動画理解](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ja)、[音声理解](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=ja)、[ドキュメント理解](https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=ja)のガイドをご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-13 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-13 UTC。"],[],[]]
