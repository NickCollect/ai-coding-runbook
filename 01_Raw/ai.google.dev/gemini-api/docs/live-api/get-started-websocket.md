---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=ja
fetched_at: 2026-06-29T05:35:21.258592+00:00
title: "WebSocket \u3092\u4f7f\u7528\u3057\u3066 Gemini Live API \u3092\u4f7f\u3063\u3066\u307f\u308b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# WebSocket を使用して Gemini Live API を使ってみる

Gemini Live API を使用すると、Gemini モデルとのリアルタイムの双方向インタラクションが可能になります。音声、動画、テキストの入力とネイティブ音声出力をサポートしています。このガイドでは、生の WebSocket を使用して API と直接統合する方法について説明します。

[Google AI Studio で Live API を試すmic](https://aistudio.google.com/live?hl=ja)
[GitHub からサンプルアプリをクローンするcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[コーディング エージェントのスキルを使用するterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja)

## 概要

Gemini Live API は、リアルタイム通信に WebSocket を使用します。SDK を使用する場合とは異なり、このアプローチでは、WebSocket 接続を直接管理し、API で定義された特定の JSON 形式でメッセージを送受信します。

クラウド セキュリティの主な概念には、

- **WebSocket エンドポイント**: 接続先の特定の URL。
- **メッセージ形式**: すべての通信は、[`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=ja#bidigeneratecontentclientmessage) 構造と [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=ja#bidigeneratecontentservermessage) 構造に準拠した JSON メッセージを介して行われます。
- **セッション管理**: WebSocket 接続の維持はユーザーの責任となります。

## 認証

認証は、WebSocket URL に API キーをクエリ パラメータとして含めることで処理されます。

エンドポイントの形式は次のとおりです。

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

`YOUR_API_KEY` は実際の API キーに置き換えます。

## 一時トークンによる認証

[エフェメラル トークン](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=ja)を使用している場合は、`v1alpha` エンドポイントに接続する必要があります。エフェメラル トークンは `access_token` クエリ パラメータとして渡す必要があります。

一時鍵のエンドポイントの形式は次のとおりです。

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

`{short-lived-token}` は、実際のエフェメラル トークンに置き換えます。

## Live API への接続

ライブ セッションを開始するには、認証済みエンドポイントへの WebSocket 接続を確立します。WebSocket で送信される最初のメッセージは、`config` を含む [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=ja#bidigeneratecontentsetup) である必要があります。構成オプションの詳細については、[Live API - WebSockets API リファレンス](https://ai.google.dev/api/live?hl=ja)をご覧ください。

### Python

```
import asyncio
import websockets
import json

API_KEY = "YOUR_API_KEY"
MODEL_NAME = "gemini-3.1-flash-live-preview"
WS_URL = f"wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key={API_KEY}"

async def connect_and_configure():
    async with websockets.connect(WS_URL) as websocket:
        print("WebSocket Connected")

        # 1. Send the initial configuration
        setup_message = {
            "setup": {
                "model": f"models/{MODEL_NAME}",
                "responseModalities": ["AUDIO"],
                "systemInstruction": {
                    "parts": [{"text": "You are a helpful assistant."}]
                }
            }
        }
        await websocket.send(json.dumps(setup_message))
        print("Configuration sent")

        # Keep the session alive for further interactions
        await asyncio.sleep(3600) # Example: keep open for an hour

async def main():
    await connect_and_configure()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.1-flash-live-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  // 1. Send the initial configuration
  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      responseModalities: ['AUDIO'],
      systemInstruction: {
        parts: [{ text: 'You are a helpful assistant.' }]
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
  console.log('Configuration sent');
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  console.log('Received:', response);
  // Handle different types of responses here
};

websocket.onerror = (error) => {
  console.error('WebSocket Error:', error);
};

websocket.onclose = () => {
  console.log('WebSocket Closed');
};
```

## テキストを送信しています

テキスト入力を送信するには、`text` フィールドを含む [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=ja#bidigeneratecontentrealtimeinput) メッセージを作成します。

### Python

```
# Inside the websocket context
async def send_text(websocket, text):
    text_message = {
        "realtimeInput": {
            "text": text
        }
    }
    await websocket.send(json.dumps(text_message))
    print(f"Sent text: {text}")

# Example usage: await send_text(websocket, "Hello, how are you?")
```

### JavaScript

```
function sendTextMessage(text) {
  if (websocket.readyState === WebSocket.OPEN) {
    const textMessage = {
      realtimeInput: {
        text: text
      }
    };
    websocket.send(JSON.stringify(textMessage));
    console.log('Text message sent:', text);
  } else {
    console.warn('WebSocket not open.');
  }
}

// Example usage:
sendTextMessage("Hello, how are you?");
```

## 音声を送信する

音声は RAW PCM データ（RAW 16 ビット PCM 音声、16 kHz、リトル エンディアン）として送信する必要があります。音声データを含む [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=ja#bidigeneratecontentrealtimeinput) メッセージを構築します。`mimeType` は重要です。

### Python

```
# Inside the websocket context
async def send_audio_chunk(websocket, chunk_bytes):
    import base64
    encoded_data = base64.b64encode(chunk_bytes).decode('utf-8')
    audio_message = {
        "realtimeInput": {
            "audio": {
                "data": encoded_data,
                "mimeType": "audio/pcm;rate=16000"
            }
        }
    }
    await websocket.send(json.dumps(audio_message))
    # print("Sent audio chunk") # Avoid excessive logging

# Assuming 'chunk' is your raw PCM audio bytes
# await send_audio_chunk(websocket, chunk)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
function sendAudioChunk(chunk) {
  if (websocket.readyState === WebSocket.OPEN) {
    const audioMessage = {
      realtimeInput: {
        audio: {
          data: chunk.toString('base64'),
          mimeType: 'audio/pcm;rate=16000'
        }
      }
    };
    websocket.send(JSON.stringify(audioMessage));
    // console.log('Sent audio chunk');
  }
}
// Example usage: sendAudioChunk(audioBuffer);
```

クライアント デバイス（ブラウザなど）から音声を取得する方法の例については、[GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74) のエンドツーエンドの例をご覧ください。

## 動画を送信しています

動画フレームは個々の画像（JPEG や PNG など）として送信されます。音声と同様に、`Blob` で `realtimeInput` を使用し、正しい `mimeType` を指定します。

### Python

```
# Inside the websocket context
async def send_video_frame(websocket, frame_bytes, mime_type="image/jpeg"):
    import base64
    encoded_data = base64.b64encode(frame_bytes).decode('utf-8')
    video_message = {
        "realtimeInput": {
            "video": {
                "data": encoded_data,
                "mimeType": mime_type
            }
        }
    }
    await websocket.send(json.dumps(video_message))
    # print("Sent video frame")

# Assuming 'frame' is your JPEG-encoded image bytes
# await send_video_frame(websocket, frame)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
function sendVideoFrame(frame, mimeType = 'image/jpeg') {
  if (websocket.readyState === WebSocket.OPEN) {
    const videoMessage = {
      realtimeInput: {
        video: {
          data: frame.toString('base64'),
          mimeType: mimeType
        }
      }
    };
    websocket.send(JSON.stringify(videoMessage));
    // console.log('Sent video frame');
  }
}
// Example usage: sendVideoFrame(jpegBuffer);
```

クライアント デバイス（ブラウザなど）から動画を取得する方法の例については、[GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222) のエンドツーエンドの例をご覧ください。

## 回答の受信

WebSocket は [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=ja#bidigeneratecontentservermessage) メッセージを返送します。これらの JSON メッセージを解析し、さまざまな種類のコンテンツを処理する必要があります。

### Python

```
# Inside the websocket context, in a receive loop
async def receive_loop(websocket):
    async for message in websocket:
        response = json.loads(message)
        print("Received:", response)

        if "serverContent" in response:
            server_content = response["serverContent"]
            # Receiving Audio
            if "modelTurn" in server_content and "parts" in server_content["modelTurn"]:
                for part in server_content["modelTurn"]["parts"]:
                    if "inlineData" in part:
                        audio_data_b64 = part["inlineData"]["data"]
                        # Process or play the base64 encoded audio data
                        # audio_data = base64.b64decode(audio_data_b64)
                        print(f"Received audio data (base64 len: {len(audio_data_b64)})")

            # Receiving Text Transcriptions
            if "inputTranscription" in server_content:
                print(f"User: {server_content['inputTranscription']['text']}")
            if "outputTranscription" in server_content:
                print(f"Gemini: {server_content['outputTranscription']['text']}")

        # Handling Tool Calls
        if "toolCall" in response:
            await handle_tool_call(websocket, response["toolCall"])

# Example usage: await receive_loop(websocket)
```

### JavaScript

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  console.log('Received:', response);

  if (response.serverContent) {
    const serverContent = response.serverContent;
    // Receiving Audio
    if (serverContent.modelTurn?.parts) {
      for (const part of serverContent.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data; // Base64 encoded string
          // Process or play audioData
          console.log(`Received audio data (base64 len: ${audioData.length})`);
        }
      }
    }

    // Receiving Text Transcriptions
    if (serverContent.inputTranscription) {
      console.log('User:', serverContent.inputTranscription.text);
    }
    if (serverContent.outputTranscription) {
      console.log('Gemini:', serverContent.outputTranscription.text);
    }
  }

  // Handling Tool Calls
  if (response.toolCall) {
    handleToolCall(response.toolCall);
  }
};
```

レスポンスの処理方法の例については、[GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75) のエンドツーエンドの例をご覧ください。

## ツール呼び出しの処理

モデルがツール呼び出しをリクエストすると、[`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=ja#bidigeneratecontentservermessage) に `toolCall` フィールドが含まれます。関数をローカルで実行し、[`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=ja#bidigeneratecontenttoolresponse) メッセージを使用して結果を WebSocket に送信する必要があります。

### Python

```
# Placeholder for your tool function
def my_tool_function(args):
    print(f"Executing tool with args: {args}")
    # Implement your tool logic here
    return {"status": "success", "data": "some result"}

async def handle_tool_call(websocket, tool_call):
    function_responses = []
    for fc in tool_call["functionCalls"]:
        # 1. Execute the function locally
        try:
            result = my_tool_function(fc.get("args", {}))
            response_data = {"result": result}
        except Exception as e:
            print(f"Error executing tool {fc['name']}: {e}")
            response_data = {"error": str(e)}

        # 2. Prepare the response
        function_responses.append({
            "name": fc["name"],
            "id": fc["id"],
            "response": response_data
        })

    # 3. Send the tool response back to the session
    tool_response_message = {
        "toolResponse": {
            "functionResponses": function_responses
        }
    }
    await websocket.send(json.dumps(tool_response_message))
    print("Sent tool response")

# This function is called within the receive_loop when a toolCall is detected.
```

### JavaScript

```
// Placeholder for your tool function
function myToolFunction(args) {
  console.log(`Executing tool with args:`, args);
  // Implement your tool logic here
  return { status: 'success', data: 'some result' };
}

function handleToolCall(toolCall) {
  const functionResponses = [];
  for (const fc of toolCall.functionCalls) {
    // 1. Execute the function locally
    let result;
    try {
      result = myToolFunction(fc.args || {});
    } catch (e) {
      console.error(`Error executing tool ${fc.name}:`, e);
      result = { error: e.message };
    }

    // 2. Prepare the response
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }

  // 3. Send the tool response back to the session
  if (websocket.readyState === WebSocket.OPEN) {
    const toolResponseMessage = {
      toolResponse: {
        functionResponses: functionResponses
      }
    };
    websocket.send(JSON.stringify(toolResponseMessage));
    console.log('Sent tool response');
  } else {
    console.warn('WebSocket not open to send tool response.');
  }
}
// This function is called within websocket.onmessage when a toolCall is detected.
```

## 次のステップ

- 音声検出やネイティブ音声機能など、主な機能と構成については、Live API の[機能](https://ai.google.dev/gemini-api/docs/live-guide?hl=ja)ガイドをご覧ください。
- [ツールの使用](https://ai.google.dev/gemini-api/docs/live-tools?hl=ja)ガイドを読んで、Live API をツールや関数呼び出しと統合する方法を確認します。
- 長時間にわたる会話を管理するには、[セッション管理](https://ai.google.dev/gemini-api/docs/live-session?hl=ja)ガイドをご覧ください。
- [クライアントとサーバー間の](#implementation-approach)アプリケーションで安全な認証を行うには、[エフェメラル トークン](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=ja)のガイドをご覧ください。
- 基盤となる WebSockets API について詳しくは、[WebSockets API リファレンス](https://ai.google.dev/api/live?hl=ja)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-09 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-09 UTC。"],[],[]]
