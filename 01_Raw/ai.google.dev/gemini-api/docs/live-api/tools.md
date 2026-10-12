---
source_url: https://ai.google.dev/gemini-api/docs/live-api/tools?hl=ja
fetched_at: 2026-10-12T06:51:14.647056+00:00
title: "Live API \u3067\u306e\u30c4\u30fc\u30eb\u306e\u4f7f\u7528 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Live API でのツールの使用

ツールを使用すると、Live API は会話だけでなく、リアルタイム接続を維持しながら現実世界でアクションを実行したり、外部コンテキストを取得したりできます。
Live API を使用して、[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)
や [Google 検索](https://ai.google.dev/gemini-api/docs/grounding?hl=ja)などのツールを定義できます。

## サポートされているツールの概要

Live API モデルで使用できるツールについて簡単に説明します。

| ツール | Gemini 3.1 Flash Live プレビュー | Gemini 2.5 Flash Live プレビュー |
| --- | --- | --- |
| **検索** | サポート対象 | サポート対象 |
| **関数呼び出し** | サポート対象（同期のみ） | サポート対象（同期と[非同期](#async-function-calling)） |
| **Google マップ** | サポート対象外 | サポート対象外 |
| **コード実行** | サポート対象外 | サポート対象外 |
| **URL コンテキスト** | サポート対象外 | サポート対象外 |

## 関数呼び出し

Live API は、通常のコンテンツ生成リクエストと同様に、関数呼び出しをサポートしています。関数呼び出しを使用すると、Live API は外部データやプログラムとやり取りできるため、アプリケーションでできることが大幅に増えます。

関数宣言は、セッション構成の一部として定義できます。
ツール呼び出しを受信したら、クライアントは `session.send_tool_response` メソッドを使用して、`FunctionResponse` オブジェクトのリストをレスポンスで返す必要があります。

詳しくは、[関数呼び出しのチュートリアル](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)をご覧ください
。

### Python

```
import asyncio
import wave
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.8-live"

# Simple function definitions
turn_on_the_lights = {"name": "turn_on_the_lights"}
turn_off_the_lights = {"name": "turn_off_the_lights"}

tools = [{"function_declarations": [turn_on_the_lights, turn_off_the_lights]}]
config = {"response_modalities": ["AUDIO"], "tools": tools}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        prompt = "Turn on the lights please"
        await session.send_client_content(turns={"parts": [{"text": prompt}]})

        wf = wave.open("audio.wav", "wb")
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)  # Output is 24kHz

        async for response in session.receive():
            if response.data is not None:
                wf.writeframes(response.data)
            elif response.tool_call:
                print("The tool was called")
                function_responses = []
                for fc in response.tool_call.function_calls:
                    function_response = types.FunctionResponse(
                        id=fc.id,
                        name=fc.name,
                        response={ "result": "ok" } # simple, hard-coded function response
                    )
                    function_responses.append(function_response)

                await session.send_tool_response(function_responses=function_responses)

        wf.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';  // npm install wavefile
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';

// Simple function definitions
const turn_on_the_lights = { name: "turn_on_the_lights" } // , description: '...', parameters: { ... }
const turn_off_the_lights = { name: "turn_off_the_lights" }

const tools = [{ functionDeclarations: [turn_on_the_lights, turn_off_the_lights] }]

const config = {
  responseModalities: [Modality.AUDIO],
  tools: tools
}

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
      } else if (message.toolCall) {
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

  const inputTurns = 'Turn on the lights please';
  session.sendClientContent({ turns: inputTurns });

  let turns = await handleTurn();

  for (const turn of turns) {
    if (turn.toolCall) {
      console.debug('A tool was called');
      const functionResponses = [];
      for (const fc of turn.toolCall.functionCalls) {
        functionResponses.push({
          id: fc.id,
          name: fc.name,
          response: { result: "ok" } // simple, hard-coded function response
        });
      }

      console.debug('Sending tool response...\n');
      session.sendToolResponse({ functionResponses: functionResponses });
    }
  }

  // Check again for new messages
  turns = await handleTurn();

  // Combine audio data strings and save as wave file
  const combinedAudio = turns.reduce((acc, turn) => {
      if (turn.data) {
          const buffer = Buffer.from(turn.data, 'base64');
          const intArray = new Int16Array(buffer.buffer, buffer.byteOffset, buffer.byteLength / Int16Array.BYTES_PER_ELEMENT);
          return acc.concat(Array.from(intArray));
      }
      return acc;
  }, []);

  const audioBuffer = new Int16Array(combinedAudio);

  const wf = new WaveFile();
  wf.fromScratch(1, 24000, '16', audioBuffer);  // output is 24kHz
  fs.writeFileSync('audio.wav', wf.toBuffer());

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

モデルは、単一のプロンプトから複数の関数呼び出しと、出力の連結に必要なコードを生成できます。このコードはサンドボックス
環境で実行され、後続の [BidiGenerateContentToolCall](https://ai.google.dev/api/live?hl=ja#bidigeneratecontenttoolcall) メッセージを生成します。

## 非同期関数呼び出し

関数呼び出しはデフォルトで順番に実行されます。つまり、各関数呼び出しの結果が表示されるまで実行は停止します。これにより、順番どおりに処理が行われます。つまり、関数が実行されている間はモデルとのやり取りを続行できません。

会話をブロックしたくない場合は、関数を非同期で実行するようにモデルに指示できます。そのためには、まず関数定義に `behavior` を追加する必要があります。

### Python

```
# Non-blocking function definitions
turn_on_the_lights = {"name": "turn_on_the_lights", "behavior": "NON_BLOCKING"} # turn_on_the_lights will run asynchronously
turn_off_the_lights = {"name": "turn_off_the_lights"} # turn_off_the_lights will still pause all interactions with the model
```

### JavaScript

```
import { GoogleGenAI, Modality, Behavior } from '@google/genai';

// Non-blocking function definitions
const turn_on_the_lights = {name: "turn_on_the_lights", behavior: Behavior.NON_BLOCKING}

// Blocking function definitions
const turn_off_the_lights = {name: "turn_off_the_lights"}

const tools = [{ functionDeclarations: [turn_on_the_lights, turn_off_the_lights] }]
```

`NON-BLOCKING` を指定すると、関数は非同期で実行され、モデルとのやり取りを続行できます。

次に、`scheduling` パラメータを使用して、`FunctionResponse` を受信したときのモデルの動作をモデルに伝える必要があります。次のいずれかになります。

- 実行中の処理を中断して、取得したレスポンスをすぐに通知する
  (`scheduling="INTERRUPT"`)
- 現在実行中の処理が完了するまで待つ
  (`scheduling="WHEN_IDLE"`)
- 何もせず、その知識を後でディスカッションで使用する
  （`scheduling="SILENT"`）

### Python

```
# for a non-blocking function definition, apply scheduling in the function response:
  function_response = types.FunctionResponse(
      id=fc.id,
      name=fc.name,
      response={
          "result": "ok",
          "scheduling": "INTERRUPT" # Can also be WHEN_IDLE or SILENT
      }
  )
```

### JavaScript

```
import { GoogleGenAI, Modality, Behavior, FunctionResponseScheduling } from '@google/genai';

// for a non-blocking function definition, apply scheduling in the function response:
const functionResponse = {
  id: fc.id,
  name: fc.name,
  response: {
    result: "ok",
    scheduling: FunctionResponseScheduling.INTERRUPT  // Can also be WHEN_IDLE or SILENT
  }
}
```

## Google 検索によるグラウンディング

セッション構成の一部として、Google 検索によるグラウンディングを有効にできます。これにより、Live API の精度が向上し、ハルシネーションを防ぐことができます。詳しくは、[グラウンディングのチュートリアル](https://ai.google.dev/gemini-api/docs/grounding?hl=ja)を
ご覧ください。

### Python

```
import asyncio
import wave
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.8-live"

tools = [{'google_search': {}}]
config = {"response_modalities": ["AUDIO"], "tools": tools}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        prompt = "When did the last Brazil vs. Argentina soccer match happen?"
        await session.send_client_content(turns={"parts": [{"text": prompt}]})

        wf = wave.open("audio.wav", "wb")
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)  # Output is 24kHz

        async for chunk in session.receive():
            if chunk.server_content:
                if chunk.data is not None:
                    wf.writeframes(chunk.data)

                # The model might generate and execute Python code to use Search
                model_turn = chunk.server_content.model_turn
                if model_turn:
                    for part in model_turn.parts:
                        if part.executable_code is not None:
                            print(part.executable_code.code)

                        if part.code_execution_result is not None:
                            print(part.code_execution_result.output)

        wf.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';  // npm install wavefile
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live';

const tools = [{ googleSearch: {} }]
const config = {
  responseModalities: [Modality.AUDIO],
  tools: tools
}

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
      } else if (message.toolCall) {
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

  const inputTurns = 'When did the last Brazil vs. Argentina soccer match happen?';
  session.sendClientContent({ turns: inputTurns });

  let turns = await handleTurn();

  let combinedData = '';
  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.modelTurn && turn.serverContent.modelTurn.parts) {
      for (const part of turn.serverContent.modelTurn.parts) {
        if (part.executableCode) {
          console.debug('executableCode: %s\n', part.executableCode.code);
        }
        else if (part.codeExecutionResult) {
          console.debug('codeExecutionResult: %s\n', part.codeExecutionResult.output);
        }
        else if (part.inlineData && typeof part.inlineData.data === 'string') {
          combinedData += atob(part.inlineData.data);
        }
      }
    }
  }

  // Convert the base64-encoded string of bytes into a Buffer.
  const buffer = Buffer.from(combinedData, 'binary');

  // The buffer contains raw bytes. For 16-bit audio, we need to interpret every 2 bytes as a single sample.
  const intArray = new Int16Array(buffer.buffer, buffer.byteOffset, buffer.byteLength / Int16Array.BYTES_PER_ELEMENT);

  const wf = new WaveFile();
  // The API returns 16-bit PCM audio at a 24kHz sample rate.
  wf.fromScratch(1, 24000, '16', intArray);
  fs.writeFileSync('audio.wav', wf.toBuffer());

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## 複数のツールを組み合わせる

Live API 内で複数のツールを組み合わせることで、アプリケーションの機能をさらに強化できます。

### Python

```
prompt = """
Hey, I need you to do two things for me.

1. Use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024?
2. Then turn on the lights

Thanks!
"""

tools = [
    {"google_search": {}},
    {"function_declarations": [turn_on_the_lights, turn_off_the_lights]},
]

config = {"response_modalities": ["AUDIO"], "tools": tools}

# ... remaining model call
```

### JavaScript

```
const prompt = `Hey, I need you to do two things for me.

1. Use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024?
2. Then turn on the lights

Thanks!
`

const tools = [
  { googleSearch: {} },
  { functionDeclarations: [turn_on_the_lights, turn_off_the_lights] }
]

const config = {
  responseModalities: [Modality.AUDIO],
  tools: tools
}

// ... remaining model call
```

## 次のステップ

- Live API でツールを使用するその他の例については、
  [ツールの使用方法のクックブック](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=ja)をご覧ください。
- 機能と構成の詳細については、
  [Live API の機能ガイド](https://ai.google.dev/gemini-api/docs/live-guide?hl=ja)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-17 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-17 UTC。"],[],[]]
