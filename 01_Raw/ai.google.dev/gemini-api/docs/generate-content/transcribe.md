---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/transcribe?hl=ja
fetched_at: 2026-08-31T06:43:09.215471+00:00
title: "\u97f3\u58f0\u6587\u5b57\u5909\u63db \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)

フィードバックを送信

# 音声文字変換

Gemini API は、Gemini 3.5 Transcribe モデル（`gemini-3.5-transcribe`）を使用して、音声ファイル内の音声をテキストに変換します。Gemini の音声理解機能に基づいて、自動言語識別、話者ダイアリゼーション、単語レベルのタイムスタンプ、カスタム語彙ヒントを使用して、正確な文字起こしを提供します。また、言い淀みの削除やスマートな書式設定などの機能を備えた[スマート文字起こし](#transcription-modes)モードも用意されています。

音声ファイルを文字起こしするには、音声をアップロードして `gemini-3.5-transcribe` に渡します。

### Python

```
from google import genai

client = genai.Client()

audio_file = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const audioFile = await ai.files.upload({
  file: "path/to/sample.mp3",
  mimeType: "audio/mp3",
});

const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
});

console.log(response.text);
```

### REST

```
# First upload the file via the Files API, then pass its URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ]
  }'
```

## 概要

Gemini 3.5 Transcribe は、音声文字変換タスク用に最適化されています。さまざまなアクセント、背景雑音、多言語の会話に対応しています。

主な機能は次のとおりです。

- **自動音声認識（ASR）:** [85 以上の言語 / 地域](#supported-languages)で言語を自動的に検出します。手動で構成しなくても、文内と文間のコードスイッチングを処理します。
- **カスタム語彙:** 最大 1,000 個のフレーズを渡すことで、分野固有の用語、頭字語、固有名詞の認識を優先します。
- **話者ダイアリゼーション:** 複数の話者を区別し、発話セグメントを個別のラベルに関連付けます。
- **単語レベルのタイムスタンプ:** 認識された各単語の正確な開始時間と終了時間のオフセットを生成します。
- **スマート文字起こし:** 語句の言い直し、つなぎ言葉、繰り返しを削除し、構造化された書式設定を適用します。
- **書式設定と正規化:** 大文字と小文字の区別、句読点、逆テキスト正規化（「2,600 万ドル」を「$26M」に変換するなど）を適用します。

音声コンテンツに関する一般的な音声推論や質問応答には、[音声理解](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=ja)を使用します。テキスト読み上げの音声合成には、[テキスト読み上げ](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=ja)を使用します。

## 言語の検出とヒント

デフォルトでは、モデルは音声言語を自動的に検出します。話者がコードスイッチングを行うと、言語が動的に切り替わります。

自動検出を使用するには、`language_codes` を省略するか、空のリストを指定します。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            language_codes=[],
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      languageCodes: [],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "languageCodes": []
      }
    }
  }'
```

言語が事前にわかっている場合は、`language_codes` で BCP-47 言語コードを指定して、文字起こしの精度を高めます（[サポートされている言語](#supported-languages)をご覧ください）。

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    languageCodes: ["es-ES"],
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "languageCodes": ["es-ES"]
    }
  }
}
```

## カスタム語彙

一般的でない単語、専門用語、ブランド名、固有名詞を音声モデルが認識しやすくすることができます。`custom_vocabulary` 配列に最大 1,000 個の用語を指定します（通常、100 個までの用語で最適な結果が得られます）。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      customVocabulary: ["Gemini", "Kubernetes", "BigQuery"],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "customVocabulary": ["Gemini", "Kubernetes", "BigQuery"]
      }
    }
  }'
```

## 話者ダイアライゼーション

話者ダイアライゼーションは、録音内の異なる音声を識別し、各セグメントに `spk_1` や `spk_2` などの話者識別子でタグ付けします。最大 8 人のスピーカーがサポートされています（3 人以上のスピーカーの帰属は試験運用版です）。

`diarization` を `True` に設定して、ダイアライゼーションを有効にします。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            diarization=True,
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      diarization: true,
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "diarization": true
      }
    }
  }'
```

## 単語レベルのタイムスタンプ

単語レベルのタイムスタンプは、音声ストリームで認識された各単語の正確な開始オフセットと終了オフセットを提供します。

`word_timestamp` を `True` に設定して、タイムスタンプを有効にします。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            word_timestamp=True,
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      wordTimestamp: true,
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "wordTimestamp": true
      }
    }
  }'
```

1 つのリクエストで `diarization` と `word_timestamp` を組み合わせて、スピーカー ラベルと単語のタイムスタンプの両方を取得できます。

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        diarization=True,
        word_timestamp=True,
        custom_vocabulary=["Gemini"],
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    diarization: true,
    wordTimestamp: true,
    customVocabulary: ["Gemini"],
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "diarization": true,
      "wordTimestamp": true,
      "customVocabulary": ["Gemini"]
    }
  }
}
```

## 文字起こしモード

Gemini 3.5 Transcribe は、`mode` パラメータを介して次の 2 つの文字起こしモードをサポートしています。

- **`VERBATIM`（デフォルト）**: 発言された内容をそのまま文字起こしし、フィラーワード（「えー」、「あー」、「～みたいな」、「～だよね」）、繰り返し、一時停止、言い直しをそのまま返します。タイムスタンプまたは話者ダイアライゼーションを使用する場合は必須です。
- **`SMART`（スマート文字起こし）**: インテリジェントな後処理を適用して、文字起こしを読みやすくします。
  - **発話の乱れの除去**: 会話のフィラー、どもり、誤った開始を削除します。
  - **インラインの自己修正**: 発言の修正を直接解決します（たとえば、「火曜日に会いましょう。いや、水曜日の 2 時にしましょう」は「水曜日の午後 2 時に会いましょう」になります）。
  - **構造化された形式の自動適用**: 発言された考えを段落、番号付きリスト、箇条書き、日付、通貨、数値の形式に自動的に構造化します。
  - **文法的なクリーンアップ**: 自然な句読点、文のケース、流れを適用します。

| 音声 | `VERBATIM` の出力 | `SMART`（スマート文字起こし）の出力 |
| --- | --- | --- |
| 「えっと、会議にはアリスを招待するべきだと思います。あ、いや、ボブとキャロルです。」 | 「えっと、会議にはアリスを招待すべきだと思います。いや、ボブとキャロルを招待すべきです。」 | 「会議には、ボブとキャロルを招待した方がいいと思います。」 |
| 「First item review budget second item finalize timeline third item send recap」 | 「first item review budget second item finalize timeline third item send recap」 | 「1. 予算を確認します。 2. タイムラインを確定する 3. ダイジェストを送信」 |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            mode="SMART",
        )
    ),
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      mode: "SMART",
    },
  },
});
console.log(response.text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "mode": "SMART"
      }
    }
  }'
```

## 文字起こし出力の解析

完全な文字起こしテキストが `response.text` で返されます。

`word_timestamp` または `diarization` が有効になっている場合、API は候補部分に付加された単語レベルの詳細なアノテーションとスピーカー ラベルも返します。

単語のタイムスタンプと話者の切り替えを抽出して反復処理する方法は次のとおりです。

### Python

```
def extract_word_transcriptions(response):
    words = []
    for candidate in getattr(response, "candidates", []) or []:
        content = getattr(candidate, "content", None)
        for part in getattr(content, "parts", []) or []:
            transcription = getattr(part, "audio_transcription", None)
            if transcription:
                speaker = getattr(transcription, "speaker_label", "")
                for word_info in getattr(transcription, "words", []) or []:
                    word = getattr(word_info, "word", "")
                    start = getattr(word_info, "start_offset", "")
                    end = getattr(word_info, "end_offset", "")
                    words.append({
                        "word": word,
                        "speaker": speaker,
                        "start_offset": start,
                        "end_offset": end,
                    })
    return words

words = extract_word_transcriptions(response)

for w in words:
    speaker = f"[{w['speaker']}] " if w["speaker"] else ""
    timing = f"({w['start_offset']} -> {w['end_offset']}) " if w["start_offset"] and w["end_offset"] else ""
    print(f"{speaker}{timing}{w['word']}")
```

### JavaScript

```
function extractWordTranscriptions(response) {
  const words = [];
  for (const candidate of response.candidates ?? []) {
    for (const part of candidate.content?.parts ?? []) {
      const transcription = part.audioTranscription;
      if (transcription) {
        const speaker = transcription.speakerLabel ?? "";
        for (const wordInfo of transcription.words ?? []) {
          words.push({
            word: wordInfo.word ?? "",
            speaker: speaker,
            startOffset: wordInfo.startOffset ?? "",
            endOffset: wordInfo.endOffset ?? "",
          });
        }
      }
    }
  }
  return words;
}

const words = extractWordTranscriptions(response);

for (const w of words) {
  const speaker = w.speaker ? `[${w.speaker}] ` : "";
  const timing = (w.startOffset && w.endOffset) ? `(${w.startOffset} -> ${w.endOffset}) ` : "";
  console.log(`${speaker}${timing}${w.word}`);
}
```

### REST

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "audioTranscription": {
              "speakerLabel": "spk_1",
              "words": [
                {
                  "word": "Hello",
                  "startOffset": "0.100s",
                  "endOffset": "0.450s"
                },
                {
                  "word": "world",
                  "startOffset": "0.500s",
                  "endOffset": "0.850s"
                }
              ]
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP"
    }
  ]
}
```

## サポートされている言語

Gemini 3.5 Transcribe では、次の言語と BCP-47 言語コードがサポートされています。

| 言語 | BCP-47 コード | 言語 | BCP-47 コード |
| --- | --- | --- | --- |
| アフリカーンス語 | `af-ZA` | 日本語 | `ja-JP` |
| アムハラ語 | `am-ET` | ジャワ語 | `jv-ID` |
| アラビア語（エジプト） | `ar-EG` | カーボベルデ語 | `kea-CV` |
| アルメニア語 | `hy-AM` | カンナダ語 | `kn-IN` |
| アッサム語 | `as-IN` | カザフ語 | `kk-KZ` |
| アゼルバイジャン語 | `az-AZ` | 韓国語 | `ko-KR` |
| ベラルーシ語 | `be-BY` | キルギス語 | `ky-KG` |
| ベンガル語（バングラデシュ） | `bn-BD` | ラトビア語 | `lv-LV` |
| ベンガル語（インド） | `bn-IN` | リンガラ語 | `ln-CD` |
| ボスニア語 | `bs-BA` | リトアニア語 | `lt-LT` |
| ブルガリア語 | `bg-BG` | マケドニア語 | `mk-MK` |
| ブルガリア語（アルーマニア語） | `rup-BG` | マレー語 | `ms-MY` |
| ビルマ語 | `my-MM` | マラヤーラム語 | `ml-IN` |
| 広東語（繁体字） | `yue-Hant-HK` | マルタ語 | `mt-MT` |
| カタルーニャ語 | `ca-ES` | 標準中国語（簡体） | `cmn-Hans-CN` |
| セブアノ語 | `ceb` | マラーティー語 | `mr-IN` |
| 中央クメール語 | `km-KH` | モンゴル語 | `mn-MN` |
| クロアチア語 | `hr-HR` | ネパール語 | `ne-NP` |
| チェコ語 | `cs-CZ` | ノルウェー語 | `nb-NO` |
| デンマーク語 | `da-DK` | オリヤ語 | `or-IN` |
| オランダ語 | `nl-NL` | ポーランド語 | `pl-PL` |
| 英語（英国） | `en-GB` | ポルトガル語（ブラジル） | `pt-BR` |
| 英語（インド） | `en-IN` | ポルトガル語（ポルトガル） | `pt-PT` |
| 英語（米国） | `en-US` | パンジャブ語 | `pa-IN` |
| エストニア語 | `et-EE` | パンジャブ語（グルムキー文字） | `pa-Guru-IN` |
| ペルシア語 | `fa-IR` | ルーマニア語 | `ro-RO` |
| フィリピン語 | `fil-PH` | ロシア語 | `ru-RU` |
| フィンランド語 | `fi-FI` | セルビア語 | `sr-RS` |
| フランス語 | `fr-FR` | シンド語（アラビア文字） | `sd-Arab-IN` |
| ガリシア語 | `gl-ES` | スロバキア語 | `sk-SK` |
| ジョージア語 | `ka-GE` | スロベニア語 | `sl-SI` |
| ドイツ語 | `de-DE` | スペイン語（ラテンアメリカ） | `es-419` |
| ギリシャ語 | `el-GR` | スペイン語（米国） | `es-US` |
| グジャラート語 | `gu-IN` | スワヒリ語（ケニア） | `sw-KE` |
| ハウサ語 | `ha-NG` | スウェーデン語 | `sv-SE` |
| ヘブライ語 | `he-IL` | タジク語 | `tg-TJ` |
| ヒンディー語 | `hi-IN` | テルグ語 | `te-IN` |
| ハンガリー語 | `hu-HU` | タイ語 | `th-TH` |
| アイスランド語 | `is-IS` | トルコ語 | `tr-TR` |
| インド英語 | `en-IN` | ウクライナ語 | `uk-UA` |
| インドネシア語 | `id-ID` | ウズベク語 | `uz-UZ` |
| イタリア語 | `it-IT` | ベトナム語 | `vi-VN` |

## サポートされているオーディオ形式

Gemini 3.5 Transcribe は、次の音声形式の MIME タイプをサポートしています。

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG - `audio/ogg`
- FLAC - `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16 - `audio/l16`
- Opus - `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM - `audio/webm`

サポートされている MIME タイプとパラメータ スキーマの完全なリストについては、[Interactions API リファレンス](https://ai.google.dev/api/interactions-api?hl=ja#Resource:Content)をご覧ください。

## パラメータ リファレンス

`GenerateContentConfig` の `audio_transcription_config` オブジェクト内のフィールドを設定して、文字起こしを構成します。

| フィールド | タイプ | 説明 |
| --- | --- | --- |
| `language_codes` | 文字列の配列 | BCP-47 言語コード（例: `["en-US"]`）。省略または空（`[]`）の場合、モデルは言語を自動的に検出し、コード切り替えを処理します。 |
| `custom_vocabulary` | 文字列の配列 | 音声認識にバイアスをかけるためのカスタム用語、頭字語、固有名詞を最大 1,000 個。 |
| `word_timestamp` | ブール値 | 単語の開始オフセットと終了オフセットを含めるには `True` に設定します。省略した場合、または `False` の場合、単語のタイムスタンプは返されません。 |
| `diarization` | ブール値 | 個別の話し手を識別してラベル付けするには、`True` に設定します。 |
| `mode` | 文字列 | 音声文字変換モード。サポートされている値: `"VERBATIM"`（デフォルト）、`"SMART"`。タイムスタンプとダイアライゼーションには対応していません。 |

## ベスト プラクティス

- **クリアな音声を提供する:** 音声録音で音声がはっきりと分離され、クリッピングがひどくならないようにします。
- **言語がわかっている場合は言語ヒントを指定する:** 音声の言語がわかっている場合は、`language_codes` を指定して精度を最大限に高めます。
- **カスタム語彙のターゲット:** 一般的な日常用語ではなく、個別のドメイン用語、ブランド名、固有名詞のみを `custom_vocabulary` に含めます。
- **大きな録音には Files API を使用する:** 数秒を超えるファイルの場合は、`client.files.upload` を使用してファイルをアップロードし、返されたファイルをモデル コンテンツに渡します。

## 制限事項

- **音声の長さ:** 標準の単項リクエストでは、最大 1 時間の音声ファイルがサポートされます。話者ダイアライゼーションや単語レベルのタイムスタンプなどの機能が有効になっている場合、音声処理は 30 分に制限されます。
- **単語レベルのタイムスタンプ:** 単語レベルのタイムスタンプを有効にすると、文字起こし全体の精度が低下する可能性があります。
- **話者ダイアライゼーション:** 話者ダイアライゼーションは最大 8 人の話者をサポートします。3 人以上の話者の話者属性は試験運用版です。
- **カスタム語彙:** `custom_vocabulary` で最大 1,000 個の用語を指定できますが、通常は 100 個までの用語で最適な結果が得られます。
- **モードの互換性:** スマート文字起こし（`mode: "SMART"`）は `word_timestamp` または `diarization` と組み合わせることはできません。

## 次のステップ

- Live API を使用して、[リアルタイム音声文字変換ガイド](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=ja)でリアルタイム音声をストリーミングします。
- [音声理解](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=ja)を使用して、音声コンテンツの分析、要約、クエリを行います。
- [テキスト読み上げ](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=ja)を使用してテキストから音声を合成する方法を学習する。
- モデルの料金とトークン上限については、[料金ページ](https://ai.google.dev/gemini-api/docs/pricing?hl=ja#gemini-3.5-transcribe)をご覧ください。
- メディア ファイルのアップロードと管理について詳しくは、[Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja) のガイドをご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-08-28 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-08-28 UTC。"],[],[]]
