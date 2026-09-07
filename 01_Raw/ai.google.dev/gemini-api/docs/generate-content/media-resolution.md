---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=ja
fetched_at: 2026-09-07T05:41:47.236796+00:00
title: "\u30e1\u30c7\u30a3\u30a2\u306e\u89e3\u50cf\u5ea6 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# メディアの解像度

`media_resolution` パラメータは、メディア入力に割り当てられる**トークンの最大数** を決定することで、画像、動画、PDF
ドキュメントなどのメディア入力を Gemini API
が処理する方法を制御します。これにより、レスポンスの品質とレイテンシ、費用のバランスを取ることができます。設定が異なる場合、デフォルト値とトークンへの対応については、[トークン数のセクション](#token-counts)をご覧ください。

メディアの解像度は、次の 2 つの方法で構成できます。

- [パートごと](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ja#per-part-media-resolution)（Gemini 3 のみ）
- [グローバルに](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ja#global-media-resolution) `generateContent` リクエスト全体で（すべてのマルチモーダル モデル）

## パートごとのメディアの解像度（Gemini 3 のみ）

Gemini 3 では、リクエスト内の個々のメディア オブジェクトのメディアの解像度を設定できるため、トークンの使用量をきめ細かく最適化できます。1
つのリクエストで解像度レベルを混在させることができます。たとえば、複雑な図には高解像度を使用し、シンプルなコンテキスト画像には低解像度を使用します。この設定は、特定のパートのグローバル構成をオーバーライドします。デフォルト設定については、[トークン数](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ja#token-counts)のセクションをご覧ください。

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

model_name = 'gemini-3.1-pro-preview'

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
    const model_name = 'gemini-3.1-pro-preview';
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

MODEL_ID="gemini-3.1-pro-preview"

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

`GenerationConfig` を使用して、リクエスト内のすべてのメディア パートのデフォルトの解像度を設定できます。これは、すべてのマルチモーダル
モデルでサポートされています。リクエストにグローバル設定と[パートごとの設定](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ja#per-part-media-resolution)の両方が含まれている場合、その特定のアイテムにはパートごとの設定が優先されます。

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
    model='gemini-3.6-flash',
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
      model: 'gemini-3.6-flash',
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
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

Gemini API では、メディアの解像度に対して次のレベルが定義されています。

- `MEDIA_RESOLUTION_UNSPECIFIED`: デフォルト設定。このレベルのトークン数は、Gemini 3 とそれ以前の Gemini モデルで大きく異なります。
- `MEDIA_RESOLUTION_LOW`: トークン数が少ないため、処理が高速になり、費用が削減されますが、詳細度は低くなります。
- `MEDIA_RESOLUTION_MEDIUM`: 詳細度、費用、レイテンシのバランスが取れています。
- `MEDIA_RESOLUTION_HIGH`: トークン数が多く、モデルが処理できる詳細度が高くなりますが、レイテンシと費用が増加します。
- `MEDIA_RESOLUTION_ULTRA_HIGH`（パートごと）: トークン数が最も多く、特定の
  ユースケース（[パソコンの使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)など）で必要になります。

`MEDIA_RESOLUTION_HIGH` は、ほとんどのユースケースで最適なパフォーマンスを提供します。

これらの各レベルで生成されるトークンの正確な数は、**メディアの種類** （画像、動画、PDF）と**モデルのバージョン** の両方によって異なります。

## トークン数

次の表に、モデル ファミリーごとの `media_resolution` の値とメディアの種類のおおよそのトークン数を示します。

**Gemini 3 モデル**

|  |  |  |  |
| --- | --- | --- | --- |
| **MediaResolution** | **画像** | **動画** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` （デフォルト） | 1,120 | 70 | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 280 + ネイティブ テキスト |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 560 + ネイティブ テキスト |
| `MEDIA_RESOLUTION_HIGH` | 1,120 | 280 | 1,120 + ネイティブ テキスト |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2,240 | なし | なし |

**Gemini 2.5 モデル**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **画像** | **動画** | **PDF（スキャン）** | **PDF（ネイティブ）** |
| `MEDIA_RESOLUTION_UNSPECIFIED` （デフォルト） | 256 + パンとスキャン（~2,048） | 256 | 256 + OCR | 256 + ネイティブ テキスト |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 64 + OCR | 64 + ネイティブ テキスト |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 256 + OCR | 256 + ネイティブ テキスト |
| `MEDIA_RESOLUTION_HIGH` | 256 + パンとスキャン | 256 | 256 + OCR | 256 + ネイティブ テキスト |

## 適切な解像度の選択

- **デフォルト（`UNSPECIFIED`）:** デフォルトから始めます。これは、最も一般的なユースケースで品質、レイテンシ、費用のバランスが取れるように調整されています。
- **`LOW`:** 費用とレイテンシが最優先で、詳細な情報が重要でないシナリオで使用します。
- **`MEDIUM` / `HIGH`:** タスクでメディア内の複雑な詳細を理解する必要がある場合は、解像度を上げます。これは、複雑なビジュアル分析、グラフの読み取り、密度の高いドキュメントの理解で必要になることがよくあります。
- **`ULTRA HIGH`** - パートごとの設定でのみ使用できます。パソコンの使用など特定のユースケースや、テストで `HIGH` よりも明確な改善が見られる場合におすすめします。
- **パートごとの制御（Gemini 3）:** トークンの使用量を最適化します。たとえば、複数の画像を含むプロンプトでは、複雑な図には `HIGH` を使用し、シンプルなコンテキスト画像には `LOW` または `MEDIUM` を使用します。

**おすすめの設定**

以下に、サポートされているメディアの種類ごとにおすすめのメディアの解像度設定を示します。

|  |  |  |  |
| --- | --- | --- | --- |
| **メディアの種類** | **おすすめの設定** | **最大トークン数** | **使用上のガイダンス** |
| **画像検索** | `MEDIA_RESOLUTION_HIGH` | 1,120 | 品質を最大限に高めるために、ほとんどの画像分析タスクにおすすめします。 |
| **PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | ドキュメントの理解に最適です。通常、品質は `medium` で飽和します。`high` に上げても、標準ドキュメントの OCR 結果が改善されることはほとんどありません。 |
| **動画** （全般） | `MEDIA_RESOLUTION_LOW` （または `MEDIA_RESOLUTION_MEDIUM`） | 70（フレームごと） | **注:** 動画の場合、コンテキストの使用量を最適化するために、`low` 設定と `medium` 設定は同じように扱われます（70 トークン）。ほとんどのアクション認識と説明のタスクで十分です。 |
| **動画** （テキストが多い） | `MEDIA_RESOLUTION_HIGH` | 280（フレームごと） | ユースケースで、動画フレーム内の密度の高いテキスト（OCR）や細かい部分を読み取る場合にのみ必要です。 |

品質、レイテンシ、費用の最適なトレードオフを見つけるには、特定のアプリケーションに対するさまざまな解像度設定の影響を常にテストして評価してください。

## バージョンの互換性の概要

- `MediaResolution` 列挙型は、メディア入力をサポートするすべてのモデルで使用できます。
- 各列挙型レベルに関連付けられたトークン数は、Gemini 3 モデルとそれ以前の Gemini バージョンで**異なります** 。
- 個々の `Part` オブジェクトに `media_resolution` を設定できるのは**Gemini 3 モデルのみ** です。

## 次のステップ

- Gemini API のマルチモーダル機能について、
  [画像理解](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=ja)、[動画理解](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ja)、
  [ドキュメント理解](https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=ja)のガイドで詳しく学習する。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-30 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-30 UTC。"],[],[]]
