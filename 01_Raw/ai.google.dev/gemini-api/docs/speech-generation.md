---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja
fetched_at: 2026-05-05T13:15:13.739814+00:00
title: "\u30c6\u30ad\u30b9\u30c8\u8aad\u307f\u4e0a\u3052\u751f\u6210\uff08TTS\uff09 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

- [ホーム](https://ai.google.dev/gemini-api/docs/ホーム)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [ドキュメント](https://ai.google.dev/gemini-api/docs/ドキュメント)

フィードバックを送信

# テキスト読み上げ生成（TTS）

Gemini API は、Gemini のテキスト読み上げ（TTS）生成機能を使用して、テキスト入力を単一話者または複数話者の音声に変換できます。*テキスト読み上げ（TTS）の生成は制御可能です。つまり、自然言語を使用してインタラクションを構造化し、音声の*スタイル*、*アクセント*、*ペース*、*トーン*をガイドできます。*

[Google AI Studio で試す](https://ai.google.dev/gemini-api/docs/Google AI Studio で試す)

TTS 機能は、インタラクティブな非構造化音声とマルチモーダルな入力と出力用に設計された [Live API](https://ai.google.dev/gemini-api/docs/Live API) を介して提供される音声生成とは異なります。Live API は動的な会話コンテキストに優れていますが、Gemini API を介した TTS は、ポッドキャストやオーディオブックの生成など、スタイルやサウンドを細かく制御して正確なテキスト朗読が必要なシナリオ向けに調整されています。

このガイドでは、テキストから単一話者と複数話者の音声を生成する方法について説明します。

## 始める前に

[サポートされているモデル](https://ai.google.dev/gemini-api/docs/サポートされているモデル) セクションに記載されているように、Gemini テキスト読み上げ（TTS）機能を備えた Gemini モデル バリアントを使用してください。最適な結果を得るには、特定のユースケースに最適なモデルを検討してください。

構築を開始する前に、[AI Studio で Gemini TTS モデルをテスト](https://ai.google.dev/gemini-api/docs/AI Studio で Gemini TTS モデルをテスト)することをおすすめします。

## 単一話者 TTS

テキストを 1 人のスピーカーの音声に変換するには、レスポンス モダリティを「音声」に設定し、`VoiceConfig` を設定した `SpeechConfig` オブジェクトを渡します。事前構築済みの[出力音声](https://ai.google.dev/gemini-api/docs/出力音声)から音声名を選択する必要があります。

この例では、モデルからの出力音声を wave ファイルに保存します。

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents="Say cheerfully: Have a wonderful day!",
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: 'Say cheerfully: Have a wonderful day!' }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               voiceConfig: {
                  prebuiltVoiceConfig: { voiceName: 'Kore' },
               },
            },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "parts":[{
            "text": "Say cheerfully: Have a wonderful day!"
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }
        },
        "model": "gemini-3.1-flash-tts-preview",
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode >out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## マルチスピーカー TTS

マルチスピーカー オーディオの場合は、各スピーカー（最大 2 つ）が `SpeakerVoiceConfig` として構成された `MultiSpeakerVoiceConfig` オブジェクトが必要です。各 `speaker` は、[プロンプト](https://ai.google.dev/gemini-api/docs/プロンプト)で使用されている名前と同じ名前で定義する必要があります。

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=prompt,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Joe',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Jane',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const ai = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: prompt }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               multiSpeakerVoiceConfig: {
                  speakerVoiceConfigs: [
                        {
                           speaker: 'Joe',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Kore' }
                           }
                        },
                        {
                           speaker: 'Jane',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Puck' }
                           }
                        }
                  ]
               }
            }
      }
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
  "contents": [{
    "parts":[{
      "text": "TTS the following conversation between Joe and Jane:
                Joe: Hows it going today Jane?
                Jane: Not too bad, how about you?"
    }]
  }],
  "generationConfig": {
    "responseModalities": ["AUDIO"],
    "speechConfig": {
      "multiSpeakerVoiceConfig": {
        "speakerVoiceConfigs": [{
            "speaker": "Joe",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }, {
            "speaker": "Jane",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Puck"
              }
            }
          }]
      }
    }
  },
  "model": "gemini-3.1-flash-tts-preview",
}' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
    base64 --decode > out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## プロンプトで話し方を制御する

単一話者と複数話者の両方の TTS で、自然言語プロンプトまたは[音声タグ](https://ai.google.dev/gemini-api/docs/音声タグ)を使用して、スタイル、トーン、アクセント、ペースを制御できます。たとえば、1 人のスピーカーのプロンプトでは、次のように言います。

```
Say in an spooky voice:
"By the pricking of my thumbs... [short pause]
[whisper] Something wicked this way comes"
```

複数話者のプロンプトでは、各話者の名前と対応する文字起こしをモデルに提供します。スピーカーごとに個別にガイダンスを提供することもできます。

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... [yawn] what's on the agenda today?
Speaker2: You're never going to guess!
```

伝えたいスタイルや感情に対応する[音声オプション](https://ai.google.dev/gemini-api/docs/音声オプション)を使用すると、さらに強調できます。たとえば、前のプロンプトでは、*エンケラドゥス*の息遣いが「疲れた」や「退屈」を強調し、*パック*の明るいトーンが「興奮」や「幸せ」を補完する可能性があります。

## 音声に変換するプロンプトを生成しています

TTS モデルは音声のみを出力しますが、[他のモデル](https://ai.google.dev/gemini-api/docs/他のモデル)を使用して最初に文字起こしを生成し、その文字起こしを TTS モデルに渡して読み上げることができます。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

transcript = client.models.generate_content(
   model="gemini-3-flash-preview",
   contents="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam.""").text

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=transcript,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Dr. Anya',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Liam',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

# ...Code to handle audio output
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {

const transcript = await ai.models.generateContent({
   model: "gemini-3-flash-preview",
   contents: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const response = await ai.models.generateContent({
   model: "gemini-3.1-flash-tts-preview",
   contents: transcript,
   config: {
      responseModalities: ['AUDIO'],
      speechConfig: {
         multiSpeakerVoiceConfig: {
            speakerVoiceConfigs: [
                   {
                     speaker: "Dr. Anya",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Kore"},
                     }
                  },
                  {
                     speaker: "Liam",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Puck"},
                    }
                  }
                ]
              }
            }
      }
  });
}
// ..JavaScript code for exporting .wav file for output audio

await main();
```

## 音声オプション

TTS モデルは、`voice_name` フィールドで次の 30 種類の音声オプションをサポートしています。

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** - *Upbeat* | **Charon** - *情報が豊富* |
| **Kore** -- *Firm* | **Fenrir** -- *Excitable* | **Leda** -- *Youthful* |
| **Orus** -- *Firm* | **Aoede** -- *Breezy* | **Callirrhoe** - *Easy-going* |
| **Autonoe** -- *Bright* | **Enceladus** - *Breathy* | **Iapetus** -- *クリア* |
| **Umbriel** -- *Easy-going* | **Algieba** -- *Smooth* | **Despina** -- *Smooth* |
| **Erinome** -- *クリア* | **Algenib** -- *Gravelly* | **Rasalgethi** - *情報が豊富* |
| **Laomedeia** - *アップビート* | **Achernar** -- *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *成人向け* | **Pulcherrima** -- *転送* |
| **Achird** -- *フレンドリー* | **Zubenelgenubi** -- *カジュアル* | **Vindemiatrix** - *Gentle* |
| **Sadachbia** -- *Lively* | **Sadaltager** -- *知識が豊富* | **Sulafat** -- *Warm* |

[AI Studio](https://ai.google.dev/gemini-api/docs/AI Studio) で、すべての音声オプションを聞くことができます。

## サポートされている言語

TTS モデルは入力言語を自動的に検出します。サポートされている言語は次のとおりです。

| 言語 | BCP-47 コード | 言語 | BCP-47 コード |
| --- | --- | --- | --- |
| アラビア語 | ar | フィリピン語 | fil |
| ベンガル語 | bn | フィンランド語 | fi |
| オランダ語 | nl | ガリシア語 | gl |
| 英語 | en | ジョージア語 | ka |
| フランス語 | fr | ギリシャ語 | el |
| ドイツ語 | de | グジャラート語 | gu |
| ヒンディー語 | hi | ハイチ語 | ht |
| インドネシア語 | id | ヘブライ語 | 彼 |
| イタリア語 | it | ハンガリー語 | hu |
| 日本語 | ja | アイスランド語 | = |
| 韓国語 | ko | ジャワ語 | jv |
| マラーティー語 | mr | カンナダ語 | kn |
| ポーランド語 | pl | コンカニ語 | kok |
| ポルトガル語 | pt | ラオ語 | lo |
| ルーマニア語 | ro | ラテン語 | la |
| ロシア語 | ru | ラトビア語 | lv |
| スペイン語 | es | リトアニア語 | lt |
| タミル語 | ta | ルクセンブルク語 | lb |
| テルグ語 | te | マケドニア語 | mk |
| タイ語 | th | マイティリー語 | mai |
| トルコ語 | tr | マラガシ語 | mg |
| ウクライナ語 | uk | マレー語 | ミリ秒 |
| ベトナム語 | vi | マラヤーラム語 | ml |
| アフリカーンス語 | af | モンゴル語 | mn |
| アルバニア語 | sq | ネパール語 | ne |
| アムハラ語 | am | ノルウェー語（ブークモール） | nb |
| アルメニア語 | hy | ノルウェー語、ニーノシク | nn |
| アゼルバイジャン語 | az | オディア語 | または |
| バスク語 | eu | パシュト語 | ps |
| ベラルーシ語 | be | ペルシャ語 | fa |
| ブルガリア語 | bg | パンジャブ語 | pa |
| ビルマ語 | my | セルビア語 | sr |
| カタルーニャ語 | ca | シンド語 | sd |
| セブアノ語 | ceb | シンハラ語 | si |
| 中国語（標準語） | cmn | スロバキア語 | sk |
| クロアチア語 | 時間 | スロベニア語 | sl |
| チェコ語 | cs | スワヒリ語 | sw |
| デンマーク語 | da | スウェーデン語 | sv |
| エストニア語 | et | ウルドゥー語 | ur |

## サポートされているモデル

| モデル | 単一話者 | マルチスピーカー |
| --- | --- | --- |
| [Gemini 3.1 Flash TTS プレビュー](https://ai.google.dev/gemini-api/docs/Gemini 3.1 Flash TTS プレビュー) | ✔️ | ✔️ |
| [Gemini 2.5 Flash プレビュー TTS](https://ai.google.dev/gemini-api/docs/Gemini 2.5 Flash プレビュー TTS) | ✔️ | ✔️ |
| [Gemini 2.5 Pro プレビュー TTS](https://ai.google.dev/gemini-api/docs/Gemini 2.5 Pro プレビュー TTS) | ✔️ | ✔️ |

## プロンプト ガイド

**Gemini ネイティブ音声生成テキスト読み上げ（TTS）**モデルは、***何を言うかだけでなく、どのように言うかも知っている***大規模言語モデルを使用することで、従来の TTS モデルと差別化されています。

このモデルは、トランスクリプトをネイティブに解釈し、単語の配信方法を決定します。追加のプロンプトなしのシンプルな文字起こしは自然な印象になります。ただし、Gemini TTS には、操作に使用できるツールも用意されています。

このガイドの目的は、オーディオ エクスペリエンスを開発する際に基本的な方向性を示し、アイデアを生み出すことです。まず、インラインで簡単に制御できる**タグ**から始め、次にパフォーマンスを最大限に引き出すための高度な**プロンプト構造**について説明します。

### 音声タグ

タグは、配信を細かく制御できる `[whispers]` や `[laughs]` などのインライン修飾子です。これらを使用して、文字起こしの行やセクションのトーン、ペース、感情的な雰囲気を変更できます。また、`[cough]`、`[sighs]`、`[gasp]` などの間投詞やその他の非言語音をパフォーマンスに追加することもできます。

タグの有効性に関する包括的なリストはありません。さまざまな感情や表現を試して、出力がどのように変化するかを確認することをおすすめします。

文字起こしが英語でない場合でも、最適な結果を得るには英語の音声タグを使用することをおすすめします。

**音声タグをクリエイティブに活用する**

音声タグで得られるバリエーションを示すために、それぞれ同じことを言っているが、使用されているタグに基づいて配信が変化する一連の例を以下に示します。

行の先頭にタグを追加して、話者が興奮している、退屈している、嫌がっているなどの感情を表現することで、配信の強調を変更できます。

- `[excitedly]` こんにちは。私は新しいテキスト読み上げモデルです。さまざまな方法で発言できます。ご用件をお聞かせください。
- `[bored]` こんにちは。私は新しいテキスト読み上げモデルです。
- `[reluctantly]` こんにちは。私は新しいテキスト読み上げモデルです。

タグを使用して、配信のペースを変更したり、ペースと強調を組み合わせたりすることもできます。

- `[very fast]` こんにちは。私は新しいテキスト読み上げモデルです。
- `[very slow]` こんにちは。私は新しいテキスト読み上げモデルです。
- `[sarcastically, one painfully slow word at a time]` こんにちは。私は新しいテキスト読み上げモデルです。

特定のセクションを正確に制御することもできます。つまり、ある部分を小声（機能）で、別の部分を大声（機能）で話すことができます。

- `[whispers]` こんにちは。私は新しいテキスト読み上げモデルの `[shouting]` です。さまざまな方法で発言できます。`[whispers]` 本日はどのようなご用件でしょうか？

また、次のようなクリエイティブなアイデアを試すこともできます。

- `[like a cartoon dog]` こんにちは。私は新しいテキスト読み上げモデルです。
- `[like dracula]` こんにちは。私は新しいテキスト読み上げモデルです。

よく使用されるタグは次のとおりです。

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

タグを使用すると、文字起こしの配信をすばやく簡単に制御できます。さらに細かく制御するには、コンテキスト プロンプトと組み合わせて、パフォーマンスの全体的なトーンと雰囲気を設定します。

### 高度なプロンプト

高度なプロンプトは、モデルが従うシステム指示と考えることができます。これは、モデルにコンテキストを追加し、パフォーマンスを制御する方法です。

堅牢なプロンプトには、優れたパフォーマンスを実現するための次の要素が含まれていることが理想的です。

- **音声プロファイル** - 音声のペルソナを確立し、キャラクターのアイデンティティ、アーキタイプ、年齢や背景などのその他の特徴を定義します。
- **Scene** - 状況を設定します。物理的な環境と「雰囲気」の両方を説明します。
- **ディレクターズ ノート** - 仮想タレントが注意すべき重要な指示を分類できるパフォーマンス ガイダンス。例: スタイル、呼吸、ペース、発音、アクセント。
- **コンテキストのサンプル** - モデルにコンテキストの開始点を与え、設定したシーンに仮想アクターが自然に登場できるようにします。
- **Transcript** - モデルが読み上げるテキスト。最適なパフォーマンスを得るには、文字起こしのトピックと文体が、指示内容と関連している必要があります。
- **音声タグ** - 文字起こしに挿入して、テキストのその部分の配信方法を変更できる修飾子（`[whispers]` や `[shouting]` など）。

プロンプトの例:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

### DIRECTOR'S NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
* Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions — no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
[excitedly] Yes, massive vibes in the studio! You are locked in and it is
absolutely popping off in London right now. If you're stuck on the tube, or
just sat there pretending to work... stop it. Seriously, I see you.
[shouting] Turn this up! We've got the project roadmap landing in three,
two... let's go!
```

### 詳細なプロンプト戦略

プロンプトの各要素を分解して見ていきましょう。

#### 音声プロファイル

キャラクターのペルソナを簡単に説明します。

- **名前。**キャラクターに名前を付けると、モデルとパフォーマンスが密接に結びつきます。シーンとコンテキストを設定するときは、名前でキャラクターを参照してください。
- **ロール。**シーンで演じているキャラクターの核となるアイデンティティとアーキタイプ。例: ラジオ DJ、ポッドキャスト配信者、ニュース レポーターなど。

例:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### シーン

シーンのコンテキストを設定します。これには、トーンと雰囲気を確立する場所、ムード、環境の詳細が含まれます。キャラクターの周囲で何が起こっているか、それがキャラクターにどのような影響を与えているかを説明します。シーンは、インタラクション全体の環境コンテキストを提供し、演技のパフォーマンスを微妙かつ有機的な方法でガイドします。

例:

```
## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
```

```
## THE SCENE: Homegrown Studio
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
```

#### 監督のメモ

この重要なセクションには、パフォーマンスに関する具体的なガイダンスが含まれています。他の要素はすべてスキップできますが、この要素を含めることをおすすめします。

パフォーマンスにとって重要なものだけを定義し、過剰な指定をしないように注意してください。厳格なルールが多すぎると、モデルの創造性が制限され、パフォーマンスが低下する可能性があります。役柄と場面の説明と、具体的な演技のルールとのバランスを取ります。

最も一般的な指示は**スタイル、ペース、アクセント**ですが、モデルはこれらに限定されず、これらを必要としません。パフォーマンスに重要な追加の詳細を説明するカスタム手順を自由に追加できます。必要なだけ詳細に説明してください。

次に例を示します。

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**スタイル:**

生成される音声のトーンとスタイルを設定します。パフォーマンスをガイドするために、アップビート、エネルギッシュ、リラックス、退屈などの要素を含めます。説明的で、必要なだけ詳細な情報を提供します。*「伝染性の熱意。「リスナーが大規模でエキサイティングなコミュニティ イベントに参加しているように感じられるようにする」*は、「エネルギッシュで熱狂的」と言うよりも効果的です。

「ボーカル スマイル」など、ナレーション業界でよく使われる用語を試してみることもできます。スタイル特性は、必要なだけ重ねることができます。

例:

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

奥行きを増やす

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

複雑

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**アクセント:**

希望するアクセントを説明します。プロンプトが具体的であるほど、より良い結果が得られます。たとえば、「*英国のクロイドンで聞かれる英国英語のアクセント*」と「*英国のアクセント*」のようにします。

例:

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a DJ from Brixton, London
...
```

**ペース:**

作品全体のペースとペースのバリエーション。

例:

シンプル

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

詳細

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

複雑

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

#### 文字起こしと音声タグ

文字起こしは、モデルが話す正確な単語です。音声タグは、発言方法、トーンの変化、間投詞のいずれかを示す角かっこ内の単語です。

```
### TRANSCRIPT

I know right, [sarcastically] I couldn't believe it. [whispers] She should have totally left
at that point.

[cough] Well, [sighs] I guess it doesn't matter now.
```

**まずはお試しください**

[AI Studio](https://ai.google.dev/gemini-api/docs/AI Studio) でこれらの例を試したり、[TTS アプリ](https://ai.google.dev/gemini-api/docs/TTS アプリ)で遊んだりして、Gemini に監督の椅子に座らせてみましょう。素晴らしいボーカル パフォーマンスを実現するためのヒントを以下に示します。

- プロンプト全体の一貫性を保つようにしてください。スクリプトと演出は、優れたパフォーマンスを生み出すために不可欠です。
- すべてを説明する必要はありません。モデルがギャップを埋める余地を残すことで、自然な文章になります。（才能のある俳優のように）
- 行き詰まったときは、Gemini に手伝ってもらって、脚本やパフォーマンスを作成しましょう。

## 制限事項

- TTS モデルはテキスト入力のみを受け取り、音声出力を生成します。
- TTS セッションの[コンテキスト ウィンドウ](https://ai.google.dev/gemini-api/docs/コンテキスト ウィンドウ)の上限は 32,000 トークンです。
- 言語のサポートについては、[言語](https://ai.google.dev/gemini-api/docs/言語)セクションをご覧ください。
- TTS はストリーミングをサポートしていません。

Gemini 3.1 Flash TTS プレビュー モデルを音声生成に使用する場合は、次の制約が適用されます。

- **プロンプトの指示と音声の不一致:** モデルの出力が選択した話者と厳密に一致しない場合があり、音声が想定と異なる場合があります。トーンの不一致（若い女性のような話し方をしようとする男性の低い声など）を避けるため、プロンプトの文面のトーンとコンテキストが、選択した話者のプロフィールと自然に一致するようにしてください。
- **長い出力の品質:** 数分を超える生成出力では、音声の品質と一貫性が低下する可能性があります。文字起こしを小さなチャンクに分割することをおすすめします。
- **テキスト トークンが返されることがある:** モデルが音声トークンの代わりにテキスト トークンを返すことがあり、サーバーが `500` エラーでリクエストに失敗します。このエラーはリクエストのほんのわずかな割合でランダムに発生するため、アプリケーションに自動再試行ロジックを実装して、このエラーを処理する必要があります。
- **プロンプト分類子の誤った拒否:** 曖昧なプロンプトでは、音声合成分類子がトリガーされず、リクエストが拒否（`PROHIBITED_CONTENT`）されたり、モデルがスタイル指示や監督のメモを読み上げたりする可能性があります。モデルに音声の合成を指示する明確なプリアンブルを追加し、実際の音声文字起こしが始まる場所を明示的にラベル付けして、プロンプトを検証します。

## 次のステップ

- [音声生成クックブック](https://ai.google.dev/gemini-api/docs/音声生成クックブック)を試す。
- Gemini の [Live API](https://ai.google.dev/gemini-api/docs/Live API) は、他のモダリティとインターリーブできるインタラクティブな音声生成オプションを提供します。
- 音声*入力*の操作については、[音声認識](https://ai.google.dev/gemini-api/docs/音声認識)ガイドをご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://ai.google.dev/gemini-api/docs/クリエイティブ・コモンズの表示 4.0 ライセンス)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://ai.google.dev/gemini-api/docs/Apache 2.0 ライセンス)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://ai.google.dev/gemini-api/docs/Google Developers サイトのポリシー)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-04-29 UTC。

ご意見をお聞かせください
