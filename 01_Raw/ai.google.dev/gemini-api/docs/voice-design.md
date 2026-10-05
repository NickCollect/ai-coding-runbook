---
source_url: https://ai.google.dev/gemini-api/docs/voice-design?hl=ja
fetched_at: 2026-10-05T06:32:12.344322+00:00
title: "\u97f3\u58f0\u30c7\u30b6\u30a4\u30f3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# 音声デザイン

音声設計では、Gemini API Voices エンドポイント（`POST /v1beta/voices`）を使用して、自然言語の説明から新しい永続的な音声ペルソナを作成できます。事前構築済みの音声や録音された参照音声に限定されるのではなく、キャラクターの年齢、音色、アクセント、ベースラインの配信を説明して、プロジェクトに保存された再利用可能な `voice_...` ID を受け取ることができます。

カスタム音声の設計、オーディション、反復処理を最速で行うには、[Google AI Studio](https://aistudio.google.com/generate-speech?hl=ja) のインタラクティブな**音声設計**スタジオを使用します。テキスト プロンプトからカスタム ペルソナを生成し、サンプル スクリプトでテストして、結果の `voice_...` ID をアプリケーション コードに直接コピーできます。

[Google AI Studio で試す](https://aistudio.google.com/generate-speech?hl=ja)

[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ja)（`gemini-3.8-flash-tts`）と [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ja)（`gemini-3.8-flash-lite-tts`）の両方で音声設計がサポートされています。

## デザインされた音声を作成する

Google GenAI SDK（`google-genai` 2.25.0 以降 / `@google/genai` 2.24.0 以降）または REST API を使用して、テキストの説明からカスタム音声を作成します。`"prompted"` 音声の場合、`voices.create`（`CreateVoice`）と `voices.get`（`GetVoice`）の両方で出力専用の `sample_audio` フィールド（`mime_type: "audio/wav"`、base64 エンコードされた `data`）が返されるため、生成された音声をすぐに試聴できます。

### Python

```
import base64
from google import genai

client = genai.Client()

# 1. Design a custom voice persona from natural language
created_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Warm British Astronomer",
        "gender": "male",
        "language_code": "en-GB",
        "prompted": {
            "input": (
                "A warm, thoughtful astronomer in his late 60s with a gentle"
                " British accent, speaking with quiet wonder."
            )
        },
    },
)

print(f"Created voice ID: {created_voice.id}")

# Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if created_voice.sample_audio and created_voice.sample_audio.data:
    with open("voice_preview.wav", "wb") as f:
        f.write(base64.b64decode(created_voice.sample_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// 1. Design a custom voice persona from natural language
const createdVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "prompted",
    display_name: "Warm British Astronomer",
    gender: "male",
    language_code: "en-GB",
    prompted: {
      input:
        "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder.",
    },
  },
});

console.log(`Created voice ID: ${createdVoice.id}`);

// Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if (createdVoice.sample_audio?.data) {
  fs.writeFileSync(
    "voice_preview.wav",
    Buffer.from(createdVoice.sample_audio.data, "base64")
  );
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "store": true,
    "voice": {
      "model": "gemini-3.8-flash-tts",
      "type": "prompted",
      "display_name": "Warm British Astronomer",
      "gender": "male",
      "language_code": "en-GB",
      "prompted": {
        "input": "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder."
      }
    }
  }' | tee created_voice.json | jq -r '.sample_audio.data' | base64 --decode > voice_preview.wav
```

## 音声設計の仕組み

1. **プロンプト付き音声を作成する:** `type="prompted"` と `store=True` を使用して `voices.create`（`POST /v1beta/voices`）を呼び出します。
2. **永続的な `voice_id` と `sample_audio` のプレビューを受け取る:** API は音声 ID を生成してプロジェクトに保存し、生成された音声のプレビュー音声を含む `sample_audio`（`mime_type: "audio/wav"`、base64 エンコードされた `data`）とともに永続 ID（`voice_abc123...` など）を返します。
3. **音声を合成する:** 合成リクエストで音声名が受け入れられる場所であれば、どこにでも `voice_id` を渡します。

## 設計した音声で音声を合成する

音声を作成したら、その `id`（`voice_...`）を Interactions API に渡して、音声を生成します。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "annotations": [{
                "type": "speech_metadata",
                "style": "reflective and awe-inspired",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": created_voice.id},
        ]
    },
)

with open("designed_voice.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash-tts",
  input: [{
    type: "user_input",
    content: [{
      type: "text",
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      annotations: [{
        type: "speech_metadata",
        style: "reflective and awe-inspired",
      }],
    }],
  }],
  response_format: { type: "audio" },
  generation_config: {
    speech_config: [
      { voice: createdVoice.id },
    ],
  },
});

fs.writeFileSync("designed_voice.wav", Buffer.from(interaction.output_audio.data, "base64"));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "annotations": [{
          "type": "speech_metadata",
          "style": "reflective and awe-inspired"
        }]
      }]
    }],
    "response_format": {"type": "audio"},
    "generation_config": {
      "speech_config": [
        {"voice": "voice_YOUR_DESIGNED_VOICE_ID"}
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

## 声を管理する

Voices API を使用すると、保存した音声をいつでも一覧表示、フィルタ、検査、削除できます（すべてのフィルタ パラメータについては、[拡張音声ライブラリとフィルタリング](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja#voice-library)をご覧ください）。

- **ストレージの上限と TTL:** ステートフル音声（`store=True`、プロンプト音声と複製音声で共有）には、**プロジェクトあたり 200 音声**の上限と **1 年の TTL**（有効期間）があります。
- **`sample_audio` の可用性:** `voices.create()`（`CreateVoice`）と `voices.get()`（`GetVoice`）は、`"prompted"` 音声の `sample_audio`（`mime_type:
  "audio/wav"`、base64 エンコードされた `data`）を設定します。リストを軽量に保つため、`voices.list()`（`ListVoices`）では `sample_audio` が省略されます（`"replicated"` と `"prebuilt"` の音声では `sample_audio` が設定されていません）。

### Python

```
from google import genai

client = genai.Client()

# List stored prompted voices in your project filtered by language
response = client.voices.list(
    type_=["prompted"],
    language_code=["en-US", "en-GB"],
)
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=created_voice.id)

# Delete a stored custom voice
client.voices.delete(id=created_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored prompted voices in your project filtered by language
const response = await ai.voices.list({
  type: ["prompted"],
  language_code: ["en-US", "en-GB"],
});
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(createdVoice.id);

// Delete a stored custom voice
await ai.voices.delete(createdVoice.id);
```

### REST

```
# List stored prompted voices filtered by language
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=prompted" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored custom voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## 音声設計のプロンプト作成のベスト プラクティス

- **永続的な音声特性は `style` ではなく Voice Design に配置する:** `voices.create` で音声を作成するときに、年齢、性別、音色、声の質感、地域アクセントなどの不変の特性を定義します。
- **状況に応じた感情表現のために `speech_metadata.style` を予約する:** カスタム音声を作成したら、短い `style` プロンプト（`"whispered urgently"` や `"cheerful and energetic"` など）を使用して、話者の核となるアイデンティティを変えることなく、ターンバイターンの演技を指示します。
- **具体的かつ簡潔に:** 1 ～ 2 文の明確な説明（「30 代のキレのある元気なスポーツ アナウンサーで、中西部のアクセントが少しある」など）は、矛盾した段落や長すぎる段落よりも、より明確で一貫性のある結果を生み出します。

## 次のステップ

- 既存のスピーカーの音声を複製する方法については、[ボイス レプリケーション](https://ai.google.dev/gemini-api/docs/voice-replication?hl=ja)をご覧ください。
- [テキスト読み上げガイド](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja)で、ターンレベルのスタイル設定、インライン タグ、複数話者の会話について確認してください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-24 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-24 UTC。"],[],[]]
