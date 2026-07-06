---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ja
fetched_at: 2026-07-06T05:18:24.467697+00:00
title: "Live API \u6a5f\u80fd\u30ac\u30a4\u30c9 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Live API 機能ガイド

これは、Live API で利用可能な機能と構成について説明する包括的なガイドです。概要と一般的なユースケースのサンプルコードについては、[Live API を使ってみる](https://ai.google.dev/gemini-api/docs/live?hl=ja)をご覧ください。

## 始める前に

- **コアコンセプトを理解する:** まだ読んでいない場合は、まず [Live API を使ってみる](https://ai.google.dev/gemini-api/docs/live?hl=ja) ページをご覧ください。ここでは、Live API の基本原則、仕組み、さまざまな[実装方法](https://ai.google.dev/gemini-api/docs/live?hl=ja#implementation-approach)について説明します。
- **AI Studio で Live API を試す:** 構築を開始する前に、[Google AI Studio](https://aistudio.google.com/app/live?hl=ja) で Live API を試してみることをおすすめします。Google AI Studio で Live API を使用するには、[**ストリーム**] を選択します。

## モデル比較

次の表に、[Gemini 3.1 Flash Live プレビュー版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=ja)モデルと [Gemini 2.5 Flash Live プレビュー版](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=ja)モデルの主な違いをまとめます。

| 機能 | Gemini 3.1 Flash Live プレビュー | Gemini 2.5 Flash ライブ プレビュー |
| --- | --- | --- |
| **[思考モード](#native-audio-output-thinking)** | `thinkingLevel` を使用して、`minimal`、`low`、`medium`、`high` などの設定で思考の深さを制御します。デフォルトは `minimal` で、レイテンシを最小限に抑えるように最適化されています。[思考レベルと予算](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#levels-budgets)をご覧ください。 | `thinkingBudget` を使用して思考トークンの数を設定します。動的思考はデフォルトで有効になっています。無効にするには、`thinkingBudget` を `0` に設定します。[思考レベルと予算](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#levels-budgets)をご覧ください。 |
| **[レスポンスの受信](https://ai.google.dev/api/live?hl=ja#bidigeneratecontentservercontent)** | 1 つのサーバー イベントに複数のコンテンツ部分（`inlineData` や文字起こしなど）を同時に含めることができます。コンテンツが欠落しないように、コードが各イベントのすべての部分を処理するようにしてください。 | 各サーバー イベントにはコンテンツ部分が 1 つだけ含まれます。パーツは個別のイベントで配信されます。 |
| **[クライアント コンテンツ](#incremental-updates)** | `send_client_content` は、初期コンテキスト履歴のシード処理でのみサポートされます（セッション構成で `initial_history_in_client_content` を設定する必要があります）。会話中にテキスト更新を送信するには、代わりに `send_realtime_input` を使用します。 | `send_client_content` は、会話全体でサポートされており、増分コンテンツ更新の送信とコンテキストの確立に使用されます。 |
| **[カバレッジをオンにする](https://ai.google.dev/api/live?hl=ja#turncoverage)** | デフォルトは `TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO` です。モデルのターンには、検出された音声アクティビティとすべての動画フレームが含まれます。 | デフォルトは `TURN_INCLUDES_ONLY_ACTIVITY` です。モデルのターンには、検出されたアクティビティのみが含まれます。 |
| **[カスタム VAD](#disable-automatic-vad)**（`activity_start`/`activity_end`） | サポート対象。自動 VAD を無効にし、`activityStart` メッセージと `activityEnd` メッセージを手動で送信して、ターンの境界を制御します。 | サポート対象。自動 VAD を無効にし、`activityStart` メッセージと `activityEnd` メッセージを手動で送信して、ターンの境界を制御します。 |
| **[VAD の自動構成](#configure-automatic-vad)** | サポート対象。`start_of_speech_sensitivity`、`end_of_speech_sensitivity`、`prefix_padding_ms`、`silence_duration_ms` などのパラメータを構成します。 | サポート対象。`start_of_speech_sensitivity`、`end_of_speech_sensitivity`、`prefix_padding_ms`、`silence_duration_ms` などのパラメータを構成します。 |
| **[非同期関数呼び出し](https://ai.google.dev/gemini-api/docs/live-tools?hl=ja#async-function-calling)**（`behavior: NON_BLOCKING`） | 対象外。関数呼び出しは順次処理のみです。ツール レスポンスを送信するまで、モデルはレスポンスを開始しません。 | サポート対象。関数宣言で `behavior` を `NON_BLOCKING` に設定すると、関数が実行されている間もモデルがインタラクションを継続できます。`scheduling` パラメータ（`INTERRUPT`、`WHEN_IDLE`、`SILENT`）を使用して、モデルがレスポンスを処理する方法を制御します。 |
| **[プロアクティブ音声](#proactive-audio)** | サポート対象外 | サポート対象。有効にすると、入力コンテンツが関連性のない場合、モデルは応答しないことを事前に決定できます。`proactivity` 構成で `proactive_audio` を `true` に設定します（`v1alpha` が必要です）。 |
| **[アフェクティブ ダイアログ](#affective-dialog)** | サポート対象外 | サポート対象。モデルは、入力の表現と口調に合わせて回答のスタイルを調整します。セッション構成で `enable_affective_dialog` を `true` に設定します（`v1alpha` が必要です）。 |

Gemini 2.5 Flash Live から Gemini 3.1 Flash Live に移行するには、[移行ガイド](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=ja#migrating)をご覧ください。

## 接続を確立する

次の例は、API キーを使用して接続を作成する方法を示しています。

### Python

```
import asyncio
from google import genai

client = genai.Client()

model = "gemini-3.1-flash-live-preview"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## インタラクション モダリティ

以降のセクションでは、Live API で使用可能なさまざまな入出力モダリティの例とコンテキストについて説明します。

### 音声を送信する

音声は RAW PCM データ（RAW 16 ビット PCM 音声、16 kHz、リトル エンディアン）として送信する必要があります。

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

### オーディオ形式

Live API の音声データは常に、リトル エンディアンの 16 ビット PCM の未加工データです。オーディオ出力は常に 24 kHz のサンプルレートを使用します。入力音声はネイティブで 16 kHz ですが、必要に応じて Live API がリサンプリングするため、任意のサンプルレートを送信できます。入力音声のサンプルレートを伝えるには、音声を含む各 [Blob](https://ai.google.dev/api/caching?hl=ja#Blob) の MIME タイプを `audio/pcm;rate=16000` などの値に設定します。

### 音声を受信する

モデルの音声応答は、データのチャンクとして受信されます。

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

### テキストを送信しています

テキストは、`send_realtime_input`（Python）または `sendRealtimeInput`（JavaScript）を使用して送信できます。

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

### 動画を送信しています

動画フレームは、特定のフレームレート（最大 1 フレーム / 秒）で個々の画像（JPEG や PNG など）として送信されます。

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

#### コンテンツの増分更新

増分更新を使用して、テキスト入力の送信、セッション コンテキストの確立、セッション コンテキストの復元を行います。コンテキストが短い場合は、ターンバイターンのインタラクションを送信して、イベントの正確なシーケンスを表すことができます。

### Python

```
turns = [
    {"role": "user", "parts": [{"text": "What is the capital of France?"}]},
    {"role": "model", "parts": [{"text": "Paris"}]},
]

await session.send_client_content(turns=turns, turn_complete=False)

turns = [{"role": "user", "parts": [{"text": "What is the capital of Germany?"}]}]

await session.send_client_content(turns=turns, turn_complete=True)
```

### JavaScript

```
let inputTurns = [
  { "role": "user", "parts": [{ "text": "What is the capital of France?" }] },
  { "role": "model", "parts": [{ "text": "Paris" }] },
]

session.sendClientContent({ turns: inputTurns, turnComplete: false })

inputTurns = [{ "role": "user", "parts": [{ "text": "What is the capital of Germany?" }] }]

session.sendClientContent({ turns: inputTurns, turnComplete: true })
```

コンテキストが長い場合は、1 つのメッセージの概要を提供して、後続のインタラクション用にコンテキスト ウィンドウを空けておくことをおすすめします。セッション コンテキストを読み込む別の方法については、[セッションの再開](https://ai.google.dev/gemini-api/docs/live-session?hl=ja#session-resumption)をご覧ください。

### 音声文字起こし

モデルのレスポンスに加えて、オーディオ出力と音声入力の両方の文字起こしを受け取ることもできます。

モデルのオーディオ出力の文字起こしを有効にするには、設定構成で `output_audio_transcription` を送信します。文字起こし言語は、モデルのレスポンスから推測されます。

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "output_audio_transcription": {}
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        message = "Hello? Gemini are you there?"

        await session.send_client_content(
            turns={"role": "user", "parts": [{"text": message}]}, turn_complete=True
        )

        async for response in session.receive():
            if response.server_content.model_turn:
                print("Model turn:", response.server_content.model_turn)
            if response.server_content.output_transcription:
                print("Transcript:", response.server_content.output_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  outputAudioTranscription: {}
};

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  const inputTurns = 'Hello how are you?';
  session.sendClientContent({ turns: inputTurns });

  const turns = await handleTurn();

  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.outputTranscription) {
      console.debug('Received output transcription: %s\n', turn.serverContent.outputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

モデルの音声入力の文字起こしを有効にするには、セットアップ構成で `input_audio_transcription` を送信します。

### Python

```
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "input_audio_transcription": {},
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_data = Path("16000.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_data, mime_type='audio/pcm;rate=16000')
        )

        async for msg in session.receive():
            if msg.server_content.input_transcription:
                print('Transcript:', msg.server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  inputAudioTranscription: {}
};

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("16000.wav");

  // Ensure audio conforms to API requirements (16-bit PCM, 16kHz, mono)
  const wav = new WaveFile();
  wav.fromBuffer(fileBuffer);
  wav.toSampleRate(16000);
  wav.toBitDepth("16");
  const base64Audio = wav.toBase64();

  // If already in correct format, you can use this:
  // const fileBuffer = fs.readFileSync("sample.pcm");
  // const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }
  );

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
    else if (turn.serverContent && turn.serverContent.inputTranscription) {
      console.debug('Received input transcription: %s\n', turn.serverContent.inputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

### 音声と言語を変更する

[ネイティブオーディオ出力](#native-audio-output)モデルは、[テキスト読み上げ（TTS）](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja#voices)モデルで利用可能な音声のいずれかをサポートします。[AI Studio](https://aistudio.google.com/app/live?hl=ja) で、すべての音声を聞くことができます。

音声を指定するには、セッション構成の一部として `speechConfig` オブジェクト内に音声名を設定します。

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "speech_config": {
        "voice_config": {"prebuilt_voice_config": {"voice_name": "Kore"}}
    },
}
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Kore" } } }
};
```

Live API は[複数の言語](#supported-languages)をサポートしています。[ネイティブ オーディオ出力](#native-audio-output)モデルは、適切な言語を自動的に選択し、言語コードの明示的な設定をサポートしていません。

## ネイティブ オーディオ機能

最新のモデルには[ネイティブ オーディオ出力](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=ja)が搭載されており、自然でリアルな音声を提供し、多言語対応のパフォーマンスを向上させます。

### 思考モード

Gemini 3.1 モデルは、`thinkingLevel` を使用して思考の深さを制御します。設定には、`minimal`、`low`、`medium`、`high` などがあります。デフォルトは `minimal` で、レイテンシを最小限に抑えるように最適化されています。Gemini 2.5 モデルは、代わりに `thinkingBudget` を使用して思考トークンの数を設定します。レベルと予算の詳細については、[思考レベルと予算](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#levels-budgets)をご覧ください。

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
    )
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio input and receive audio
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
  },
};

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: ...,
  });

  // Send audio input and receive audio

  session.close();
}

main();
```

また、構成で `includeThoughts` を `true` に設定すると、思考の要約を有効にできます。詳しくは、[思考の要約](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#summaries)をご覧ください。

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
        include_thoughts=True
    )
)
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
    includeThoughts: true,
  },
};
```

### アフェクティブ ダイアログ

この機能を使用すると、Gemini は入力された表現と口調に応じて回答スタイルを調整できます。

アフェクティブ ダイアログを使用するには、セットアップ メッセージで API バージョンを `v1alpha` に設定し、`enable_affective_dialog` を `true` に設定します。

### Python

```
client = genai.Client(http_options={"api_version": "v1alpha"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    enable_affective_dialog=True
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1alpha"} });

const config = {
  responseModalities: [Modality.AUDIO],
  enableAffectiveDialog: true
};
```

### コンテキストに応じた音声にのみ対応

この機能を有効にすると、コンテンツが関連性のない場合、Gemini は応答しないことを事前に判断できます。

これを使用するには、API バージョンを `v1alpha` に設定し、セットアップ メッセージの `proactivity` フィールドを構成して、`proactive_audio` を `true` に設定します。

### Python

```
client = genai.Client(http_options={"api_version": "v1alpha"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={'proactive_audio': True}
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1alpha"} });

const config = {
  responseModalities: [Modality.AUDIO],
  proactivity: { proactiveAudio: true }
}
```

## ライブ翻訳

Live API は、話し言葉の会話のリアルタイムの低レイテンシ翻訳をサポートしています。この機能を使用すると、リアルタイムの音声から音声への翻訳アプリケーションを構築できます。

詳細と例については、[リアルタイム翻訳ガイド](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=ja)をご覧ください。

## 音声アクティビティ検出（VAD）

音声アクティビティ検出（VAD）により、モデルは人が話しているときを認識できます。これは、ユーザーがいつでもモデルを中断できるようにするため、自然な会話を作成するうえで不可欠です。

VAD が中断を検出すると、進行中の生成はキャンセルされ、破棄されます。クライアントにすでに送信された情報だけがセッション履歴に保持されます。その後、サーバーは中断を報告する [`BidiGenerateContentServerContent`](https://ai.google.dev/api/live?hl=ja#bidigeneratecontentservercontent) メッセージを送信します。

Gemini サーバーは、保留中の関数呼び出しを破棄し、キャンセルされた呼び出しの ID を記載した `BidiGenerateContentServerContent` メッセージを送信します。

### Python

```
async for response in session.receive():
    if response.server_content.interrupted is True:
        # The generation was interrupted

        # If realtime playback is implemented in your application,
        # you should stop playing audio and clear queued playback here.
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.interrupted) {
    // The generation was interrupted

    // If realtime playback is implemented in your application,
    // you should stop playing audio and clear queued playback here.
  }
}
```

### 自動 VAD

デフォルトでは、モデルは連続した音声入力ストリームに対して VAD を自動的に実行します。VAD は、[セットアップ構成](https://ai.google.dev/api/live?hl=ja#BidiGenerateContentSetup)の [`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/api/live?hl=ja#RealtimeInputConfig.AutomaticActivityDetection) フィールドで構成できます。

音声ストリームが 1 秒以上一時停止すると（たとえば、ユーザーがマイクをオフにした場合）、キャッシュに保存された音声をフラッシュするために [`audioStreamEnd`](https://ai.google.dev/api/live?hl=ja#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end) イベントが送信されます。クライアントはいつでも音声データの送信を再開できます。

### Python

```
# example audio file to try:
# URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
# !wget -q $URL -O sample.pcm
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_bytes = Path("sample.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
        )

        # if stream gets paused, send:
        # await session.send_realtime_input(audio_stream_end=True)

        async for response in session.receive():
            if response.text is not None:
                print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
// example audio file to try:
// URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
// !wget -q $URL -O sample.pcm
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("sample.pcm");
  const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }

  );

  // if stream gets paused, send:
  // session.sendRealtimeInput({ audioStreamEnd: true })

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

`send_realtime_input` を使用すると、API は VAD に基づいて音声に自動的に応答します。`send_client_content` はメッセージをモデル コンテキストに順番に追加しますが、`send_realtime_input` は応答性を最適化するために、決定論的な順序を犠牲にします。

### VAD の自動構成

VAD アクティビティをより詳細に制御するには、次のパラメータを構成できます。詳しくは、[API リファレンス](https://ai.google.dev/api/live?hl=ja#automaticactivitydetection)をご覧ください。

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {
        "automatic_activity_detection": {
            "disabled": False, # default
            "start_of_speech_sensitivity": types.StartSensitivity.START_SENSITIVITY_LOW,
            "end_of_speech_sensitivity": types.EndSensitivity.END_SENSITIVITY_LOW,
            "prefix_padding_ms": 20,
            "silence_duration_ms": 100,
        }
    }
}
```

### JavaScript

```
import { GoogleGenAI, Modality, StartSensitivity, EndSensitivity } from '@google/genai';

const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: false, // default
      startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_LOW,
      endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_LOW,
      prefixPaddingMs: 20,
      silenceDurationMs: 100,
    }
  }
};
```

### 自動 VAD を無効にする

また、セットアップ メッセージで `realtimeInputConfig.automaticActivityDetection.disabled` を `true` に設定することで、自動 VAD を無効にすることもできます。この構成では、クライアントがユーザーの音声の検出と、適切なタイミングでの [`activityStart`](https://ai.google.dev/api/live?hl=ja#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start) メッセージと [`activityEnd`](https://ai.google.dev/api/live?hl=ja#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end) メッセージの送信を行います。この構成では `audioStreamEnd` は送信されません。代わりに、ストリームの中断は `activityEnd` メッセージでマークされます。

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {"automatic_activity_detection": {"disabled": True}},
}

async with client.aio.live.connect(model=model, config=config) as session:
    # ...
    await session.send_realtime_input(activity_start=types.ActivityStart())
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )
    await session.send_realtime_input(activity_end=types.ActivityEnd())
    # ...
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    }
  }
};

session.sendRealtimeInput({ activityStart: {} })

session.sendRealtimeInput(
  {
    audio: {
      data: base64Audio,
      mimeType: "audio/pcm;rate=16000"
    }
  }

);

session.sendRealtimeInput({ activityEnd: {} })
```

### VAD パラメータとその品質への影響について

自動 VAD を使用する場合、次の 2 つのキー パラメータによって、音声が発話ターンに分割されてモデルに送信される方法が制御されます。

- **`prefixPaddingMs`**: 音声が検出される*前*に含める音声の量。この「ルックバック」により、モデルは音声の完全な開始をキャプチャできます。これには、VAD がトリガーされる前に開始される可能性のある最初の音節も含まれます。`0` の値を使用すると、単語の先頭が切り取られる可能性があります。
- **`silenceDurationMs`**: 発話ターンを終了する前にサーバーが無音状態で待機する時間。これにより、システムが文中の自然な一時停止（思考、呼吸、句の境界など）をどの程度許容するかが決まります。

#### `silenceDurationMs` が音質に与える影響

`silenceDurationMs` 値は、モデルが処理のために受け取る音声チャンクのサイズと完全性に直接影響します。

- **推奨（500 ～ 800 ミリ秒）:** 適切なバランスが取れています。モデルは、レイテンシを妥当な範囲に抑えながら、コンテキストが豊富な完全な音声チャンクを受け取ります。サーバーの内部デフォルトは約 800 ミリ秒です。
- **低すぎる（100 ～ 200 ミリ秒など）:** システムは自然な一時停止中に発話ターンを終了し、1 つの発話を複数の小さな音声フラグメントに分割します。モデルはこれらのフラグメントを個別に受信するため、フラグメント間のコンテキストが失われ、文字起こしとレスポンスの品質が低下します。
- **高すぎる（2,000 ミリ秒以上など）:** ユーザーが発話を停止してからシステムが応答するまでの時間が長くなり、モデルが応答するまでの認識されるレイテンシが増加します。

#### 手動（クライアントサイド）VAD のベスト プラクティス

自動 VAD を無効にして、独自のクライアントサイド音声検出から `activityStart`/`activityEnd` 信号を管理する場合、サーバーの組み込み音声バッファリング メカニズムはバイパスされます。これは次のことを意味します。

1. **音声前のバッファなし:** 検出された音声の開始前に、サーバーが音声を追加しなくなりました。クライアントは、`activityStart` を送信する前に十分な音声コンテキストを含める必要があります。
2. **無音許容度なし:** サーバーは、追加の待機なしで `activityEnd` 信号に即座に対応します。クライアントサイドの VAD がアグレッシブな発話終了しきい値（200 ミリ秒の無音など）を使用している場合、自然な一時停止中に発話が文の途中で途切れることがあります。

手動 VAD で音質を維持するには、クライアントの音声アクティビティ検出器で発話終了の無音しきい値を **500 ミリ秒**以上に設定します。この値より低いしきい値では、音声が断片化し、音声文字変換とモデルのレスポンスの品質が低下することがよくあります。

## トークン数

消費されたトークンの合計数は、返されたサーバー メッセージの [usageMetadata](https://ai.google.dev/api/live?hl=ja#usagemetadata) フィールドで確認できます。

### Python

```
async for message in session.receive():
    # The server will periodically send messages that include UsageMetadata.
    if message.usage_metadata:
        usage = message.usage_metadata
        print(
            f"Used {usage.total_token_count} tokens in total. Response token breakdown:"
        )
        for detail in usage.response_tokens_details:
            match detail:
                case types.ModalityTokenCount(modality=modality, token_count=count):
                    print(f"{modality}: {count}")
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.usageMetadata) {
    console.debug('Used %s tokens in total. Response token breakdown:\n', turn.usageMetadata.totalTokenCount);

    for (const detail of turn.usageMetadata.responseTokensDetails) {
      console.debug('%s\n', detail);
    }
  }
}
```

## メディアの解像度

入力メディアのメディア解像度を指定するには、セッション構成の一部として `mediaResolution` フィールドを設定します。

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "media_resolution": types.MediaResolution.MEDIA_RESOLUTION_LOW,
}
```

### JavaScript

```
import { GoogleGenAI, Modality, MediaResolution } from '@google/genai';

const config = {
    responseModalities: [Modality.AUDIO],
    mediaResolution: MediaResolution.MEDIA_RESOLUTION_LOW,
};
```

## 制限事項

プロジェクトを計画する際は、Live API の次の制限事項を考慮してください。

### レスポンス モダリティ

ネイティブ音声モデルは、`AUDIO レスポンス モダリティのみをサポートしています。モデルのレスポンスをテキストとして取得する必要がある場合は、[出力音声文字起こし](#audio-transcription)機能を使用します。

### クライアント認証

Live API はデフォルトでサーバー間認証のみを提供します。[クライアント / サーバー アプローチ](https://ai.google.dev/gemini-api/docs/live?hl=ja#implementation-approach)を使用して Live API アプリケーションを実装する場合は、[エフェメラル トークン](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=ja)を使用してセキュリティ リスクを軽減する必要があります。

### セッション継続時間

音声のみのセッションは 15 分に制限され、音声と動画のセッションは 2 分に制限されます。ただし、セッション継続時間を無制限に延長するために、さまざまな[セッション管理手法](https://ai.google.dev/gemini-api/docs/live-session?hl=ja)を構成できます。

### コンテキスト ウィンドウ

セッションのコンテキスト ウィンドウの上限は次のとおりです。

- [ネイティブ オーディオ出力](#native-audio-output)モデルの 128,000 トークン
- 他の Live API モデルの 32,000 トークン

## サポートされている言語

Live API は、次の 97 言語をサポートしています。

| 言語 | BCP-47 コード | 言語 | BCP-47 コード |
| --- | --- | --- | --- |
| アフリカーンス語 | `af` | ラトビア語 | `lv` |
| アカン語 | `ak` | リトアニア語 | `lt` |
| アルバニア語 | `sq` | マケドニア語 | `mk` |
| アムハラ語 | `am` | マレー語 | `ms` |
| アラビア語 | `ar` | マラヤーラム語 | `ml` |
| アルメニア語 | `hy` | マルタ語 | `mt` |
| アッサム語 | `as` | マオリ語 | `mi` |
| アゼルバイジャン語 | `az` | マラーティー語 | `mr` |
| バスク語 | `eu` | モンゴル語 | `mn` |
| ベラルーシ語 | `be` | ネパール語 | `ne` |
| ベンガル語 | `bn` | ノルウェー語 | `no` |
| ボスニア語 | `bs` | オディア語 | `or` |
| ブルガリア語 | `bg` | オロモ語 | `om` |
| ビルマ語 | `my` | パシュト語 | `ps` |
| カタルーニャ語 | `ca` | ペルシャ語 | `fa` |
| セブアノ語 | `ceb` | ポーランド語 | `pl` |
| 中国語 | `zh` | ポルトガル語 | `pt` |
| クロアチア語 | `hr` | パンジャブ語 | `pa` |
| チェコ語 | `cs` | ケチュア語 | `qu` |
| デンマーク語 | `da` | ルーマニア語 | `ro` |
| オランダ語 | `nl` | ロマンシュ語 | `rm` |
| 英語 | `en` | ロシア語 | `ru` |
| エストニア語 | `et` | セルビア語 | `sr` |
| フェロー語 | `fo` | シンド語 | `sd` |
| フィリピン語 | `fil` | シンハラ語 | `si` |
| フィンランド語 | `fi` | スロバキア語 | `sk` |
| フランス語 | `fr` | スロベニア語 | `sl` |
| ガリシア語 | `gl` | ソマリ語 | `so` |
| ジョージア語 | `ka` | 南ソト語 | `st` |
| ドイツ語 | `de` | スペイン語 | `es` |
| ギリシャ語 | `el` | スワヒリ語 | `sw` |
| グジャラート語 | `gu` | スウェーデン語 | `sv` |
| ハウサ語 | `ha` | タジク語 | `tg` |
| ヘブライ語 | `iw` | タミル語 | `ta` |
| ヒンディー語 | `hi` | テルグ語 | `te` |
| ハンガリー語 | `hu` | タイ語 | `th` |
| アイスランド語 | `is` | ツワナ語 | `tn` |
| インドネシア語 | `id` | トルコ語 | `tr` |
| アイルランド語 | `ga` | トルクメン語 | `tk` |
| イタリア語 | `it` | ウクライナ語 | `uk` |
| 日本語 | `ja` | ウルドゥー語 | `ur` |
| カンナダ語 | `kn` | ウズベク語 | `uz` |
| カザフ語 | `kk` | ベトナム語 | `vi` |
| クメール語 | `km` | ウェールズ語 | `cy` |
| キニヤルワンダ語 | `rw` | 西フリジア語 | `fy` |
| 韓国語 | `ko` | ウォロフ語 | `wo` |
| クルド語 | `ku` | ヨルバ語 | `yo` |
| キルギス語 | `ky` | ズールー語 | `zu` |
| ラオ語 | `lo` |  |  |

## 次のステップ

- Live API を効果的に使用するための重要な情報については、[ツールの使用](https://ai.google.dev/gemini-api/docs/live-tools?hl=ja)ガイドと[セッション管理](https://ai.google.dev/gemini-api/docs/live-session?hl=ja)ガイドをご覧ください。
- [Google AI Studio](https://aistudio.google.com/app/live?hl=ja) で Live API をお試しください。
- Live API モデルの詳細については、モデルページの [Gemini 2.5 Flash ネイティブ音声](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-2.5-flash-native-audio)をご覧ください。
- [Live API クックブック](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=ja)、[Live API Tools クックブック](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=ja)、[Live API スタートガイド スクリプト](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py)で、他の例も試してみてください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-09 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-09 UTC。"],[],[]]
