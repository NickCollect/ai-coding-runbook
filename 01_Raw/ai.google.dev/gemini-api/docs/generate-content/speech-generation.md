---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=ja
fetched_at: 2026-10-05T06:30:49.349802+00:00
title: "\u30c6\u30ad\u30b9\u30c8\u8aad\u307f\u4e0a\u3052\u751f\u6210\uff08TTS\uff09 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash が利用可能になりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ja)。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs/generate-content?hl=ja)

フィードバックを送信

# テキスト読み上げ生成（TTS）

Gemini API は、Gemini のテキスト読み上げ（TTS）生成機能を使用して、テキスト入力を単一話者または複数話者の音声に変換できます。テキスト読み上げの生成は*[制御可能](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=ja#controllable)*です。つまり、構造化されたターン メタデータ（`speech_metadata`）とインライン音声タグを組み合わせて、音声の*スタイル*、*アクセント*、*ペース*、*トーン*を制御できます。

[Google AI Studio で試す](https://aistudio.google.com/generate-speech?hl=ja)

TTS 機能は、インタラクティブな非構造化音声とマルチモーダルな入力と出力用に設計された [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ja) を介して提供される音声生成とは異なります。Live API は動的な会話コンテキストに優れていますが、Gemini API を介した TTS は、ポッドキャストやオーディオブックの生成など、スタイルやサウンドを細かく制御して正確なテキスト朗読が必要なシナリオ向けに調整されています。

このガイドでは、[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ja)（`gemini-3.8-flash-tts`）と [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ja)（`gemini-3.8-flash-lite-tts`）を使用して、テキストから単一話者と複数話者の音声を生成する方法について説明します。

## 始める前に

[サポートされているモデル](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=ja#supported-models) セクションに記載されている Gemini TTS モデルを使用していることを確認します。最適な結果を得るには、[どのモデルをいつ使用するか](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=ja#when-to-use-which-model)を確認して、ワークロードに最適なモデルを選択してください。

構築を開始する前に、[AI Studio で Gemini TTS モデルをテスト](https://aistudio.google.com/generate-speech?hl=ja)することをおすすめします。

## 単一話者 TTS

Gemini 3.8 TTS モデルを使用してテキストを単一話者の音声に変換するには、`parts[].text` で文字起こしをそのまま渡し、`parts[].speech_metadata` でターンレベルのスタイル設定を適用し、`speechConfig.voiceConfig` で音声を構成します。事前構築済みの音声名、拡張音声ライブラリ ID、カスタムの[音声デザイン](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=ja) ID（`voice_...`）、[ボイス レプリケーション](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=ja) ID（`voice_...`、またはオプションのステートレス `voicekey_...`）を渡すことができます。

この例では、モデルからの出力音声を WAV ファイルに保存します。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.wav
```

## マルチスピーカー TTS

複数の話者の会話の場合、`prebuiltVoiceConfig` を使用して `multiSpeakerVoiceConfig.speakerVoiceConfigs` で 2 人の話者を構成し、各会話のターンを個別の `part` として渡します。`speech_metadata` では、`speaker` とオプションのターンレベルの `style` の両方を指定します。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [
            {
                "text": "How's it going today Jane?",
                "speech_metadata": {
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                },
            },
            {
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "speech_metadata": {
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                },
            },
        ],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "multi_speaker_voice_config": {
                "speaker_voice_configs": [
                    {
                        "speaker": "Joe",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Puck"}
                        },
                    },
                    {
                        "speaker": "Jane",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Kore"}
                        },
                    },
                ]
            }
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [
            {
               text: "How's it going today Jane?",
               speechMetadata: {
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               },
            },
            {
               text: 'Not too bad, how about you? Ready to test these new voices?',
               speechMetadata: {
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               },
            },
         ],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            multiSpeakerVoiceConfig: {
               speakerVoiceConfigs: [
                  {
                     speaker: 'Joe',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Puck' },
                     },
                  },
                  {
                     speaker: 'Jane',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Kore' },
                     },
                  },
               ],
            },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [
        {
          "text": "How'\''s it going today Jane?",
          "speech_metadata": {
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }
        },
        {
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "speech_metadata": {
            "speaker": "Jane",
            "style": "calm and relaxed"
          }
        }
      ]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "multiSpeakerVoiceConfig": {
          "speakerVoiceConfigs": [
            {
              "speaker": "Joe",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Puck" }
              }
            },
            {
              "speaker": "Jane",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Kore" }
              }
            }
          ]
        }
      }
    }
  }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
      base64 --decode > out.wav
```

## メタデータとタグを使用して音声スタイルを制御する

Gemini 3.8 TTS は、`text` フィールドを厳密に文字起こしとして扱います。ト書きを読み上げずに配信を制御するには、スコープごとに指示を分割します。

- **ターンレベルの持続的な配信（`speech_metadata.style`）:** ターン全体に適用される感情、配信スタイル、韻律、ペース、音量を `speech_metadata.style`（`"style": "whispered urgently"`、`"style": "out of breath"`、`"style": "warm and enthusiastic"` など）で指定します。
- **特定の時点のイベント（インライン タグ）:** 一時的な発話以外の音声のバーストやポーズを、山かっこ（`"Wait... <short pause> did you hear that? <sigh>"` や `"Excuse me <cough> as I was saying..."` など）を使用して文字起こしの中に直接配置します。

包括的なベスト プラクティスについては、[プロンプト ガイド](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=ja#prompting-guide)をご覧ください。

## 音声オプション

Gemini 3.8 TTS は、音声を選択または作成する 4 つの方法をサポートしています。

1. **プリビルドのスタジオ音声:** 次の表に記載されている 30 種類の厳選された音声。
2. **拡張音声ライブラリ:** `client.voices.list()`（`GET /v1beta/voices`）を使用してアクセスできる、言語、アクセント、キャラクターのアーキタイプにわたる数百もの追加の音声。
3. **[音声設計](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=ja):** [Google AI Studio](https://aistudio.google.com/generate-speech?hl=ja) の自然言語の説明から、または `POST /v1beta/voices`（`type="prompted"`、永続的な `voice_...` ID と `CreateVoice` および `GetVoice` の `sample_audio` WAV プレビューを返します）を使用して、カスタム音声ペルソナを生成します。
4. **[ボイス レプリケーション](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=ja):**
   [Google AI Studio](https://aistudio.google.com/generate-speech?hl=ja) の参照音声と同意音声から、または `POST /v1beta/voices`（デフォルトでは `type="replicated"`、永続的な `store=True`、またはオプションのステートレス `store=False`）を使用して、話者の音声を複製します。

### カスタム音声の上限と TTL

| 音声タイプ | ストレージ モード | 割り当て / 上限 | 保持（TTL） |
| --- | --- | --- | --- |
| **ステートフル音声**（`voice_...`、プロンプトまたは複製） | `store=True` | **プロジェクトあたり 200 個の音声**（プロンプト音声と複製音声で共有） | **最終使用日から 1 年間\*** |
| **ステートレス音声キー**（`voicekey_...`、複製） | `store=False` | クライアント管理 | **7 日** |

\* **TTL の延長:** 音声がアクティブに使用されるたびに（音声で音声を合成するか、リミックスのベース音声として使用する）、1 年間の保持期間がリセットされます。1 年間アクティビティがない音声は自動的に削除されます。

### 事前構築済みの音声

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** -- *Upbeat* | **Charon** - *Informative* |
| **Kore** -- *Firm* | **Fenrir** -- *興奮しやすい* | **Leda** - *Youthful* |
| **Orus** -- *Firm* | **Aoede** -- *Breezy* | **Callirrhoe** - *おおらか* |
| **Autonoe** -- *Bright* | **Enceladus** -- *Breathy* | **Iapetus** -- *Clear* |
| **Umbriel** -- *Easy-going* | **Algieba** -- *Smooth* | **Despina** - *Smooth* |
| **Erinome** -- *クリア* | **Algenib** - *Gravelly* | **Rasalgethi** - *情報が豊富* |
| **Laomedeia** -- *アップビート* | **Achernar** -- *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *成人向け* | **Pulcherrima** - *Forward* |
| **Achird** -- *Friendly* | **Zubenelgenubi** -- *Casual* | **Vindemiatrix** - *Gentle* |
| **Sadachbia** -- *Lively* | **Sadaltager** -- *Knowledgeable* | **Sulafat** -- *Warm* |

### 拡張音声ライブラリとフィルタリング

上記の表に記載されている 30 種類のスタジオ音声に加えて、**拡張音声ライブラリ**では、言語、地域アクセント、キャラクター ペルソナ、ドメインにわたる数百種類の音声が提供されています。[Google AI Studio](https://aistudio.google.com/generate-speech?hl=ja) で音声ライブラリ全体をインタラクティブに閲覧、フィルタ、試聴したり、`client.voices.list()`（`google-genai` 2.25.0+ / `@google/genai` 2.24.0+ を使用する `GET /v1beta/voices`）を使用してプログラムでクエリしたりできます。

`ListVoices` は、フィルタ条件に一致する事前構築済みカタログ音声の後に、カスタム保存済み音声（新しい順）を返します。リスト フィルタに複数の値が渡された場合、そのフィルタ内の**いずれか**の値に一致する音声が返されます（`OR`）。一方、個別のフィルタ パラメータは `AND` と組み合わされます。

| パラメータ | 型 | 説明 |
| --- | --- | --- |
| `language_code` | `list[str]` | BCP-47 言語タグ（例: `["en-US", "en-GB"]`）。大文字と小文字を区別しない完全一致。 |
| `region_code` | `list[str]` | ISO 3166-1 alpha-2 または国連 M.49 地域コード（`["US", "GB"]` など）。 |
| `accent` | `list[str]` | 地域アクセント記述子（`["American", "British"]` など）。 |
| `gender` | `list[str]` | 認識された性別の表現（`"female"`、`"male"`、`"neutral"`）。 |
| `pitch` | `list[str]` | 音声のピッチ分類（`"low"`、`"medium"`、`"high"`）。 |
| `persona` | `list[str]` | 音声のペルソナまたはキャラクターのアーキタイプ（`["Warm, Friendly"]`、`["Narrator"]` など）。 |
| `contexts`（REST の `context`） | `list[str]` | 最適な使用量ドメイン（例: `["Audiobook", "Conversational", "News"]`）。 |
| `type`（Python の場合は `type_`） | `list[str]` | 音声ソース（`"prebuilt"`、`"prompted"`（[音声デザイン](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=ja)）、`"replicated"`（[ボイス レプリケーション](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=ja)））でフィルタします。 |
| `search` | `str` | フリーテキストの部分文字列検索では、`display_name` と `description` の両方に対して大文字と小文字を区別せずに照合が行われました。 |
| `page_size` | `int` | ページごとに返される音声の最大数（デフォルトは `50`、最大は `1000`）。 |
| `page_token` | `str` | `response.next_page_token` からのトークン。結果の次のページを取得します。 |

### Python

```
from google import genai

client = genai.Client()

# Filter the Voice Library by language, gender, pitch, domain context, and keyword
response = client.voices.list(
    language_code=["en-US", "en-GB"],
    gender=["female"],
    pitch=["medium", "low"],
    contexts=["Audiobook", "Conversational"],
    type_=["prebuilt"],
    search="warm",
    page_size=50,
)

for voice in response.voices or []:
    print(
        f"{voice.id} | {voice.display_name} ({voice.language_code},"
        f" {voice.accent}, {voice.gender}, pitch={voice.pitch}):"
        f" {voice.description}"
    )
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// Filter the Voice Library by language, gender, pitch, domain context, and keyword
const response = await ai.voices.list({
  language_code: ["en-US", "en-GB"],
  gender: ["female"],
  pitch: ["medium", "low"],
  contexts: ["Audiobook", "Conversational"],
  type: ["prebuilt"],
  search: "warm",
  page_size: 50,
});

for (const voice of response.voices ?? []) {
  console.log(
    `${voice.id} | ${voice.display_name} (${voice.language_code}, ${voice.accent}, ${voice.gender}, pitch=${voice.pitch}): ${voice.description}`
  );
}
```

### REST

```
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB" \
  --data-urlencode "gender=female" \
  --data-urlencode "pitch=medium" \
  --data-urlencode "context=Audiobook" \
  --data-urlencode "type=prebuilt" \
  --data-urlencode "search=warm" \
  --data-urlencode "page_size=50"
```

## サポートされている言語

TTS モデルは入力言語を自動的に検出します。[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ja)（`gemini-3.8-flash-tts`）は **130 以上の言語**に対応し、[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ja)（`gemini-3.8-flash-lite-tts`）は **100 以上の言語**に対応しています。

| 言語 | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| アチェ語（アラビア文字） | ✔️ | ✔️ |
| アフリカーンス語 | ✔️ | ✔️ |
| アカン語 | ✔️ | ✔️ |
| アムハラ語 | ✔️ | ✔️ |
| アルメニア語 | ✔️ | ✔️ |
| アッサム語 | ✔️ | ✔️ |
| アワディー語 | ✔️ | ✔️ |
| バリ文字 | ✔️ | ✔️ |
| ベンガル語 | ✔️ | ✔️ |
| バンジャール語（アラビア文字） | ✔️ | — |
| バンジャール語（ラテン文字） | ✔️ | ✔️ |
| バシキール語 | ✔️ | — |
| バスク語 | ✔️ | ✔️ |
| ベラルーシ語 | ✔️ | ✔️ |
| ベンバ語 | ✔️ | — |
| ボージュプリー語 | ✔️ | ✔️ |
| ボスニア語 | ✔️ | ✔️ |
| ブギス文字 | ✔️ | ✔️ |
| ブルガリア語 | ✔️ | ✔️ |
| ビルマ語 | ✔️ | — |
| 広東語 | ✔️ | ✔️ |
| カタルーニャ語 | ✔️ | ✔️ |
| セブアノ語 | ✔️ | ✔️ |
| 中央クルド語 | ✔️ | ✔️ |
| チャッティースガリー語 | ✔️ | ✔️ |
| 中国語（漢字） | ✔️ | ✔️ |
| 中国語（繁体字） | ✔️ | ✔️ |
| クリミア タタール語 | ✔️ | — |
| クロアチア語 | ✔️ | ✔️ |
| チェコ語 | ✔️ | ✔️ |
| デンマーク語 | ✔️ | ✔️ |
| オランダ語 | ✔️ | ✔️ |
| ジュラ語 | ✔️ | — |
| ゾンカ語 | ✔️ | — |
| エジプト アラビア語 | ✔️ | ✔️ |
| 英語 | ✔️ | ✔️ |
| エストニア語 | ✔️ | ✔️ |
| フィリピン語 | ✔️ | ✔️ |
| フィンランド語 | ✔️ | — |
| フランス語 | ✔️ | ✔️ |
| ガリシア語 | ✔️ | ✔️ |
| ガンダ語 | ✔️ | ✔️ |
| ジョージア語 | ✔️ | ✔️ |
| ドイツ語 | ✔️ | ✔️ |
| ギリシャ語 | ✔️ | ✔️ |
| グアラニ語 | ✔️ | — |
| グジャラート語 | ✔️ | ✔️ |
| ハイチ語 | ✔️ | ✔️ |
| ハルハ モンゴル語 | ✔️ | ✔️ |
| ハウサ語 | ✔️ | ✔️ |
| ヘブライ語 | ✔️ | ✔️ |
| ヒンディー語 | ✔️ | ✔️ |
| ハンガリー語 | ✔️ | ✔️ |
| アイスランド語 | ✔️ | ✔️ |
| イボ語 | ✔️ | — |
| イロカノ語 | ✔️ | ✔️ |
| インドネシア語 | ✔️ | ✔️ |
| イランのペルシャ語 | ✔️ | ✔️ |
| イタリア語 | ✔️ | ✔️ |
| 日本語 | ✔️ | ✔️ |
| ジャワ語 | ✔️ | ✔️ |
| カビル語 | ✔️ | — |
| カンバ語 | ✔️ | ✔️ |
| カンナダ語 | ✔️ | ✔️ |
| カシミール語（アラビア文字） | ✔️ | ✔️ |
| カシミール語（デーヴァナーガリー文字） | ✔️ | ✔️ |
| カザフ語 | ✔️ | ✔️ |
| クメール語 | ✔️ | ✔️ |
| キクユ語 | ✔️ | ✔️ |
| キニヤルワンダ語 | ✔️ | ✔️ |
| コンゴ語 | ✔️ | ✔️ |
| 韓国語 | ✔️ | ✔️ |
| キルギス語 | ✔️ | ✔️ |
| ラオ語 | ✔️ | ✔️ |
| ラトガリア語 | ✔️ | — |
| リンガラ語 | ✔️ | ✔️ |
| リトアニア語 | ✔️ | — |
| ルクセンブルク語 | ✔️ | — |
| マケドニア語 | ✔️ | ✔️ |
| マガヒー語 | ✔️ | ✔️ |
| マイティリー語 | ✔️ | ✔️ |
| マラヤーラム語 | ✔️ | ✔️ |
| マルタ語 | ✔️ | ✔️ |
| マニプリ語 | ✔️ | ✔️ |
| マラーティー語 | ✔️ | ✔️ |
| ミナンカバウ語（アラビア文字） | ✔️ | ✔️ |
| ミナンカバウ語（ラテン文字） | ✔️ | — |
| ミゾ語 | ✔️ | ✔️ |
| ネパール語（個別の言語） | ✔️ | ✔️ |
| ナイジェリアン フルフルディ語 | ✔️ | ✔️ |
| 北アゼルバイジャン語 | ✔️ | ✔️ |
| 北ソト語 | ✔️ | ✔️ |
| ウズベク語北部方言 | ✔️ | ✔️ |
| ノルウェー語（ブークモール） | ✔️ | ✔️ |
| ノルウェー語（ニーノシク） | ✔️ | ✔️ |
| ニャンジャ語 | ✔️ | ✔️ |
| オック語 | ✔️ | — |
| オディア語（個別の言語） | ✔️ | ✔️ |
| パンガシナン語 | ✔️ | — |
| ペルシャ語（アフガニスタン） | ✔️ | ✔️ |
| ポーランド語 | ✔️ | ✔️ |
| ポルトガル語 | ✔️ | ✔️ |
| パンジャブ語 | ✔️ | ✔️ |
| ルーマニア語 | ✔️ | ✔️ |
| ロシア語 | ✔️ | ✔️ |
| サンタル語 | ✔️ | ✔️ |
| セルビア語 | ✔️ | ✔️ |
| シンド語 | ✔️ | — |
| シンハラ語 | ✔️ | ✔️ |
| スロバキア語 | ✔️ | ✔️ |
| スロベニア語 | ✔️ | — |
| ソマリ語 | ✔️ | — |
| 南アゼルバイジャン語 | ✔️ | ✔️ |
| 南部パシュトー語 | ✔️ | ✔️ |
| 南ソト語 | ✔️ | — |
| スペイン語 | ✔️ | ✔️ |
| 標準アラビア語（アラビア文字） | ✔️ | ✔️ |
| 標準アラビア語（ラテン文字） | ✔️ | ✔️ |
| 標準ラトビア語 | ✔️ | ✔️ |
| 標準マレー語 | ✔️ | ✔️ |
| スワヒリ語（個別の言語） | ✔️ | — |
| スワート語 | ✔️ | — |
| スウェーデン語 | ✔️ | — |
| タジク語 | ✔️ | — |
| タミル語 | ✔️ | ✔️ |
| テルグ語 | ✔️ | ✔️ |
| タイ語 | ✔️ | — |
| ティグリニャ語 | ✔️ | — |
| トスク アルバニア語 | ✔️ | — |
| トルコ語 | ✔️ | ✔️ |
| ウイグル語 | ✔️ | — |
| ベトナム語 | ✔️ | ✔️ |

## サポートされているモデル

| モデル | 単一話者 | マルチスピーカー | 音声デザイン | ボイス レプリケーション |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ja)（`gemini-3.8-flash-tts`） | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ja)（`gemini-3.8-flash-lite-tts`） | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash TTS プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=ja) | ✔️ | ✔️ | — | — |
| [Gemini 2.5 Pro プレビュー TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=ja) | ✔️ | ✔️ | — | — |

### どのモデルをいつ使用するか

Gemini 3.8 TTS モデルはどちらも同じ API スキーマとプロンプト形式を共有しているため、1 つのパラメータを変更するだけで切り替えることができます。

- **音響忠実度、ニュアンスのある演技、表現力豊かな制御を最優先する場合は、[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ja)（`gemini-3.8-flash-tts`）**を使用します。スタジオ品質のクリエイティブな作業、複数の話者による複雑な会話、大量のボーカル バーストタグ、難しい発音、地域や少数派の言語、音声とルームトーンの安定性が求められる長文のナレーションに最適です。
- **[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ja)（`gemini-3.8-flash-lite-tts`）**を、`gemini-3.1-flash-tts-preview` の高速で費用対効果の高いワークホースの代替として使用します。大量の一括生成、会話型音声エージェントのカスケード、読み上げ機能、信頼性の高いボイス レプリケーション、主要言語での日常的な単一話者の音声に最適化されています。

### 移行ガイド

以前のプレビュー モデル（`gemini-3.1-flash-tts-preview` または `gemini-2.5-pro-preview-tts`）から Gemini 3.8 TTS（`gemini-3.8-flash-tts` または `gemini-3.8-flash-lite-tts`）にアップグレードする場合は、次の 5 つの重要な変更点を確認してください。

1. **スタイルを文字起こしから分離する:** 演技、トーン、韻律、ペースの指示（`"whispering"`、`"out of breath"`、`"speaking slowly"` など）をプレーン テキストから `speech_metadata.style` に移動します。`text` は、文字起こしとインラインの音声タグのみにしてください。
2. **音声設計で事前にペルソナを設計する:** `"Audio Profile"` または `"Director's Notes"` の複数段落のブロックを、[音声設計](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=ja)で作成したカスタム音声に置き換え、その `voice_...` ID を TTS リクエストで `style` 文字列を最小限にするか空にして渡します。
3. **構造化された会話ターンを使用する:** 複数話者の会話の場合、1 つのテキスト ブロック内に `Speaker: ...` 接頭辞を埋め込むのではなく、話者ターンごとに 1 つの `part` を `speech_metadata.speaker` で渡します。
4. **インライン音声タグには山かっこを使用する:** 人間の発声や一時停止の特定の時点には、山かっこ（`<laugh>`、`<sigh>`、`<cough>`、`<breath>`、`<short pause>`）を使用します。音声以外の効果音タグ（拍手やドスンという音など）は避けてください。
5. **単項リクエストのデフォルトの WAV（`AUDIO_WAV`）出力を考慮する:** `gemini-3.1-flash-tts-preview`（デフォルトでヘッダーなしの RAW PCM `AUDIO_L16` を返した）とは異なり、Gemini 3.8 TTS モデルは、単項リクエストで RIFF ヘッダー（24 kHz、モノラル、16 ビット PCM）を含む完全な **WAV（`AUDIO_WAV`）**音声を返します。
   - 以前にコードで未加工の PCM バイトを WAV ヘッダーでラップしていた場合（たとえば、Python の `wave` モジュールや Node の `wav` パッケージを使用していた場合）、手動ヘッダー ラッパーを削除し、デコードされた音声バイトを `.wav` ファイルに直接書き込みます。
   - 既存のパイプラインでヘッダーレスの生の PCM、mu-law、A-law 音声が必要な場合は、`response_format.audio.mime_type` を `"AUDIO_L16"`、`"AUDIO_MULAW"`、`"AUDIO_ALAW"` に明示的に設定します（例: `generateContent` の `{"response_format": {"audio": {"mime_type": "AUDIO_L16"}}}`、Interactions API の `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}`）。[オーディオ出力形式](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=ja#audio-output-formats)をご覧ください。

## プロンプト ガイド

Gemini 3.8 TTS モデルは、入力テキストを厳密に**逐語録**として扱います。以前のプレビュー モデルでは、ト書きがプレーン テキストに埋め込まれていましたが、Gemini 3.8 TTS では、継続的なターンレベルの指示（`speech_metadata`）がポイントインタイムのインライン音声タグから分離されています。

### スタイル フィールドとインライン タグ

パフォーマンスに関する指示をスコープごとに分割します。

- **ターンレベルの配信（`speech_metadata.style`）:** 感情、韻律、全体的なペース、配信スタイル（`"whispering"`、`"out of breath"`、`"muttering"`、`"sarcastic"` など）などの持続的な配信属性を `speech_metadata` の `style` フィールドに入れます。ターン全体で安定したキャラクターとパフォーマンスを作成するには、[音声デザイン](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=ja)でペルソナを事前に設計し、`style` はオプションのターンレベルの調整にのみ使用します。
- **ポイントインタイム イベント（インライン タグ）:** 一瞬の音声以外の発声、呼吸、一時停止を、山かっこ（`<cough>`、`<breath>`、`<sigh>`、`<short pause>`）を使用して文字起こしの中にインラインで挿入します。最高の音質を実現するには、山かっこ（`<...>`）を使用し、音声以外の効果音ではなく、人間の発声に限定します。

| スコープ | 設置場所 | 例 |
| --- | --- | --- |
| **ターンレベル**（ターン全体で維持される） | `speech_metadata.style` | `"angry tone"`、`"speaking rapidly"`、`"out of breath"`、`"whispers"`、`"sarcastic"` |
| **ポイントインタイム**（特定の単語で発生） | `text`（`<...>`）でインライン | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### ペースと一時停止

リズムと無音は、次の 3 つの粒度レベルで制御できます。

- **句読点と省略記号:** カンマ、ダッシュ（`--`）、省略記号（`...`）を使用して、自然な会話の躊躇を表現します。
- **インライン一時停止タグ:** 話者が一時停止するスクリプトの正確な位置に `<short pause>` または `<long pause>` を挿入します。
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **ターンレベルのペース:** `speech_metadata` で `"style": "speaking rapidly"` または `"style": "speaking slowly"` を設定して、ターン全体の発話速度を制御します。

### プロソディとピッチ

**`speech_metadata.style`** を使用して、ターン全体で韻律、ピッチ、イントネーションを制御します（`"style": "high pitch, cheerful and excited inflection"` や `"style": "monotone and flat"` など）。感情や韻律が会話の途中で変化する場合は、スクリプトを別々のターンに分割し、各ターンに異なる `style` 値を設定します。

### 強調

文字起こしで特定の単語を大文字にし、句読点とインライン音声タグを組み合わせて、キーワードに自然な音声の強調を付けます。

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### 発声と会話以外の音声

音声以外の人の発声は、音が鳴る正確な位置に山かっこ（`<...>`）を使用してインラインで配置します。推奨される音声タグは次のとおりです。

|  |  |  |  |
| --- | --- | --- | --- |
| `<argh>` | `<breath>` | `<heavy breath>` | `<exhales>` |
| `<cackle>` | `<cheer>` | `<chuckle>` / `<chuckles>` | `<cough>` |
| `<cry>` | `<gasp>` | `<giggle>` | `<groan>` |
| `<growl>` | `<grunt>` | `<grr>` | `<hiss>` |
| `<laugh>` / `<laughter>` | `<moan>` | `<pant>` | `<pff>` / `<phew>` |
| `<scream>` | `<shout>` | `<shriek>` | `<sigh>` / `<sighs>` |
| `<sneeze>` | `<snicker>` | `<snort>` | `<sob>` |
| `<throat-clearing>` | `<tsk>` | `<whimper>` | `<whispers>` / `<whispering>` |
| `<yawn>` | `<short pause>` | `<long pause>` |  |

### バックチャネルと音声の重複

複数話者の対話では、話者のターン内でリスナーの反応をパイプ文字（`|reaction|`）で囲み、反応ごとに別のターンに分割することなく、自然なバックチャネルや重複する発話を作成します。

- **短いバックチャネルのやり取り:** 発言者のターン内の短いリスナーの反応（`|oh hmm|`、`|oh really?|`、`|absolutely|`）:
  - **ターン 1（スピーカー A）:** `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **ターン 2（スピーカー B）:** `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **ターン 3（話者 A）:** `"Then let's ship it |absolutely| and watch the dashboards."`
- **重複する発話とインターリーブされた発話:** 複数のパイプ セグメントを使用して、2 人の話者の同時発話またはインターリーブされた発話をシミュレートします（`gemini-3.8-flash-tts` で最適に動作します）。
  - **同時カウントダウン/コーラス:** `"Let's surprise him on three |ok| ready?"` の後に `"one. two. three. |happy| happy |birthday| birthday!"`
  - **スピーカーの完全な重複:** `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### 世代間の整合性と避けるべきこと

発話者 ID をターン間で安定させるには、次のガイドラインに沿って操作します。

- **長いスタイル ブロックではなく、音声設計でペルソナを事前に設計する:**
  以前のモデルから引き継がれた長い `"Audio Profile"` 段落と複数の箇条書き `"Director's Notes"` は、音声のずれの最も一般的な原因です。[音声設計](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=ja)で同じクリエイティブな直感を使用して、永続的なカスタム `voice_...` ペルソナを生成し、その音声 ID を TTS 呼び出しに渡します。
- **安定性のために音声リファレンスに依存する（メタ指示を省略）:**
  Gemini 3.8 TTS モデルは、最初に音声リファレンスにアンカーするようにトレーニングされています。音声の安定をモデルに指示する（`"do not switch speaker identity"` や `"maintain identical timbre"` など）指示を含めないでください。プロンプト テキストを追加すると、ドリフトが増加します。不要なスタイル指示を削除し、音声参照によって提供される安定点の周りでモデルが自然に変化するようにします。
- **`style` で不変の発話者特性を変更しようとしない:** 年齢、性別、名前、永続的なアクセントの変更を `speech_metadata.style` に入れないでください。代わりに、拡張音声ライブラリから地域音声を選択するか、[音声デザイン](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=ja)で作成します。

### おすすめのワークフロー

1. **キャラクターを一度作成する:** [音声デザイン](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=ja)でキャラクターを作成するか、ターゲット言語とペルソナに一致する地域音声を選択します。
2. **自然な話し言葉の文字起こしを不流暢さを含めて記述する:** 自然さを最大限に高めるには、`text` を実際の話し言葉の文字起こしとして記述します。会話の不流暢さやためらい（`"Oh uh yeah I think... hm, so that's interesting"` など）も記述します。
3. **まずプレーン TTS をテストする:** まず、空の `style` フィールドを使用して文字起こしを合成します。ほとんどのリクエストでは `style` 指示は必要ありません。
4. **調整のみに短い `style` プロンプトを追加する:** 特定の配信調整が必要なターンにのみ、簡潔な `style` 文字列（`"casual, friendly"` や `"muttering, then reassuring"` など）を追加します。一貫したベースラインが必要な場合は、ターン間で同じ短い文字列を再利用します。

### マルチターンの対話と音声エージェント

リアルタイムの会話型音声エージェントまたはマルチターン アプリケーションを構築する場合:

- LLM テキスト チャンクが到着したら、**ターンごとに 1 回の TTS 呼び出し**を行います。
- 構成された `voice`（事前構築、設計された `voice_...`、複製された `voice_...` / `voicekey_...`）に、発言者の ID をターン間で保持させます。各ターンで長い文字のペルソナを再送信しないでください。
- ターンごとの `style` フィールドを空のままにするか、会話全体に対して 1 つの短い定数文字列（`"casual, friendly"` など）を送信します。
- 強いスタイルのプロンプトを使用するのではなく、長いエージェントのレスポンスを短いターンに分割します。

## ストリーミング音声生成

モデルで合成された生成音声は、合成中にストリーミングできます。単項リクエスト（RIFF ヘッダーを含む完全な WAV ファイルを返す）とは異なり、**ストリーミング リクエストは、デフォルトでヘッダーなしの RAW 16 ビット符号付きリトル エンディアン線形 PCM（`AUDIO_L16` / `audio/L16;codec=pcm;rate=24000`、24 kHz、モノラル）チャンクを返します**。これにより、コンテナ ヘッダーなしで音声チャンクを連続して再生または連結できます。

### Python

```
from google import genai

client = genai.Client()

response_stream = client.models.generate_content_stream(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

for chunk in response_stream:
    try:
        data = chunk.candidates[0].content.parts[0].inline_data.data
        # data contains raw PCM bytes (24kHz, 1-channel, 16-bit)
    except (IndexError, AttributeError):
        pass
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const ai = new GoogleGenAI({});

   const responseStream = await ai.models.generateContentStream({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   for await (const chunk of responseStream) {
      const data = chunk.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
      if (data) {
         const audioBuffer = Buffer.from(data, 'base64');
         // Process the audio buffer
      }
   }
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }'
```

## オーディオ出力形式

Gemini 3.8 TTS モデルは、リクエストが単項かストリーミングかによって、異なるデフォルトの音声形式を使用します。

- **単項リクエスト（`models.generate_content`）:** RIFF ヘッダー（24 kHz、モノラル、16 ビット符号付きリトル エンディアン PCM）を含む完全な **WAV（`AUDIO_WAV`）**音声を返します。WAV コンテナを手動で追加しなくても、デコードされた音声バイトを `.wav` ファイルに直接書き込むことができます。
- **ストリーミング リクエスト（`models.generate_content_stream` / `streamGenerateContent`）:**
  デフォルトで**ヘッダーなしの RAW リニア PCM（`AUDIO_L16`）**チャンク（24 kHz、モノラル、16 ビット符号付きリトル エンディアン PCM）を返します。これにより、各チャンクにコンテナ ヘッダーがなくても、チャンクをストリーミングまたは連続して連結できます。

`generationConfig.responseFormat.audio` を使用して、出力音声のエンコードとサンプルレートをオーバーライドできます。

| `mimeType` 値 | 形式 | 説明 |
| --- | --- | --- |
| `"AUDIO_WAV"` *（単項デフォルト）* | WAV（`audio/wav`） | RIFF ヘッダー付きの完全な WAV ファイル（24 kHz、モノラル、16 ビット PCM）。 |
| `"AUDIO_L16"` *（ストリーミングのデフォルト）* | リニア PCM（`audio/l16`） | ヘッダーなしの RAW 16 ビット符号付きリトル エンディアン リニア PCM。ストリーミング、カスタム音声パイプライン、マルチターンのクリップの連結に最適です。 |
| `"AUDIO_MULAW"` | μ-law（`audio/basic` / `audio/mulaw`） | G.711 μ-law 圧縮音声。北米と日本の電話で一般的に使用されています（8 kHz）。 |
| `"AUDIO_ALAW"` | A-law（`audio/alaw`） | G.711 A-law 圧縮音声。ヨーロッパや国際電話で一般的に使用されています（8 kHz）。 |

必要に応じて `sampleRate`（`24000`、`16000`、`8000` Hz など。デフォルトは `24000` Hz）を指定することもできます。

次の例では、24 kHz でヘッダーなしの RAW 16 ビット PCM（`AUDIO_L16`）をリクエストしています。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "response_format": {
            "audio": {
                "mime_type": "AUDIO_L16",
                "sample_rate": 24000,
            }
        },
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.pcm", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         responseFormat: {
            audio: {
               mimeType: 'AUDIO_L16',
               sampleRate: 24000,
            },
         },
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.pcm', audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "responseFormat": {
            "audio": {
              "mimeType": "AUDIO_L16",
              "sampleRate": 24000
            }
          },
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.pcm
```

## 制限事項

- TTS モデルはテキストのみの入力を受け取り、音声のみの出力を生成します。
- 単一リクエストの複数話者生成（`multiSpeakerVoiceConfig`）では、事前構築済みの音声を使用して最大 2 人の話者をサポートします。カスタム設計（`voice_...`）または複製（`voice_...` / `voicekey_...`）された音声を複数のキャラクターの会話で組み合わせるには、各話者のターンを個別に合成します。単項リクエストはデフォルトで 44 バイトの RIFF ヘッダーを含む `audio/wav` を返すため、未加工の PCM（`AUDIO_L16`）をリクエストするか、24 kHz の PCM 音声フレームを連結する前に各ターンの WAV ヘッダーを削除します。
- **カスタム音声の保存容量の上限と TTL:**
  - **ステートフル音声（`store=True`、プロンプトまたは複製）:** **プロジェクトあたり最大 200 個の音声**、**1 年間の TTL**（有効期間）。
  - **ステートレス音声キー（`store=False`、`voicekey_...`）:** **7 日間の TTL**（有効期間）。
- 言語の対応範囲については、[サポートされている言語](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=ja#languages)のセクションをご覧ください。

## 次のステップ

- [音声デザイン](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=ja)を使用して、自然言語からカスタムの音声ペルソナを作成します。
- [ボイス レプリケーション](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=ja)で既存のスピーカーの音声を複製します。
- [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=ja) モデルページと [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=ja) モデルページで、モデルの仕様を比較します。
- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ja) を使用して、インタラクティブな双方向音声を確認します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-02 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-02 UTC。"],[],[]]
