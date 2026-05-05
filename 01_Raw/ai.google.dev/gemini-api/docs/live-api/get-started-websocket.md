---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=tr
fetched_at: 2026-05-05T19:52:27.935021+00:00
title: "Get started with Gemini Live API using WebSockets \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Get started with Gemini Live API using WebSockets

Gemini Live API, Gemini modelleriyle gerçek zamanlı ve çift yönlü etkileşime olanak tanır. Ses, video ve metin girişlerinin yanı sıra doğal ses çıkışlarını destekler. Bu kılavuzda, ham WebSocket'ler kullanarak API ile doğrudan nasıl entegrasyon yapılacağı açıklanmaktadır.

[Google AI Studio'da Live API'yi deneyinmic](https://aistudio.google.com/live?hl=tr)
[Örnek uygulamayı GitHub'dan klonlayıncode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[Kodlama aracısı becerilerini kullanınterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=tr)

## Genel Bakış

Gemini Live API, anlık iletişim için WebSocket'leri kullanır. Bu yaklaşımda, SDK kullanmanın aksine WebSocket bağlantısı doğrudan yönetilir ve API tarafından tanımlanan belirli bir JSON biçiminde mesaj gönderilip alınır.

Temel kavramlar:

- **WebSocket Uç Noktası**: Bağlanılacak URL.
- **Mesaj Biçimi**: Tüm iletişim, [`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=tr#bidigeneratecontentclientmessage) ve [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=tr#bidigeneratecontentservermessage) yapılarına uygun JSON mesajları aracılığıyla yapılır.
- **Oturum Yönetimi**: WebSocket bağlantısını sürdürmek sizin sorumluluğunuzdadır.

## Kimlik doğrulama

Kimlik doğrulama, API anahtarınızın WebSocket URL'sine sorgu parametresi olarak eklenmesiyle yapılır.

Uç nokta biçimi şöyledir:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

`YOUR_API_KEY` kısmını gerçek API anahtarınızla değiştirin.

## Kısa Ömürlü Jetonlarla Kimlik Doğrulama

[Kısa ömürlü jetonlar](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=tr) kullanıyorsanız `v1alpha` uç noktasına bağlanmanız gerekir.
Geçici jeton, `access_token` sorgu parametresi olarak iletilmelidir.

Kısa ömürlü anahtarların uç nokta biçimi şöyledir:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

`{short-lived-token}` değerini gerçek geçici jetonla değiştirin.

## Live API'ye bağlanma

Canlı oturum başlatmak için kimliği doğrulanmış uç noktaya bir WebSocket bağlantısı oluşturun.
WebSocket üzerinden gönderilen ilk mesaj, `config` değerini içeren bir [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=tr#bidigeneratecontentsetup) olmalıdır.
Tüm yapılandırma seçenekleri için [Live API - WebSockets API referansı](https://ai.google.dev/api/live?hl=tr) başlıklı makaleyi inceleyin.

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
        config_message = {
            "config": {
                "model": f"models/{MODEL_NAME}",
                "responseModalities": ["AUDIO"],
                "systemInstruction": {
                    "parts": [{"text": "You are a helpful assistant."}]
                }
            }
        }
        await websocket.send(json.dumps(config_message))
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
  const configMessage = {
    config: {
      model: `models/${MODEL_NAME}`,
      responseModalities: ['AUDIO'],
      systemInstruction: {
        parts: [{ text: 'You are a helpful assistant.' }]
      }
    }
  };
  websocket.send(JSON.stringify(configMessage));
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

## Kısa mesaj gönderiliyor

Metin girişi göndermek için `text` alanıyla bir [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=tr#bidigeneratecontentrealtimeinput) mesajı oluşturun.

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

## Ses gönderme

Ses, ham PCM verileri (ham 16 bit PCM ses, 16 kHz, little-endian) olarak gönderilmelidir. Ses verileriyle [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=tr#bidigeneratecontentrealtimeinput) mesajı oluşturun. `mimeType` çok önemlidir.

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

İstemci cihazdan (ör. tarayıcı) ses alma örneği için [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74)'daki uçtan uca örneğe bakın.

## Video gönderiliyor

Video kareleri ayrı resimler (ör. JPEG veya PNG) olarak gönderilir. Sesle benzer şekilde, doğru `mimeType` değerini belirterek `realtimeInput` ile birlikte `Blob` kullanın.

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

Videoyu istemci cihazdan (ör. tarayıcı) alma örneği için [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222)'daki uçtan uca örneğe bakın.

## Yanıt alma

WebSocket, [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=tr#bidigeneratecontentservermessage) mesajlarını geri gönderir. Bu JSON mesajlarını ayrıştırmanız ve farklı içerik türlerini işlemeniz gerekir.

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

Yanıtın nasıl işleneceğine dair bir örnek için [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75)'daki uçtan uca örneğe bakın.

## Araç çağrılarını işleme

Model bir araç çağrısı istediğinde [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=tr#bidigeneratecontentservermessage), `toolCall` alanını içerir. İşlevi yerel olarak yürütmeli ve sonucu [`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=tr#bidigeneratecontenttoolresponse) mesajı kullanarak WebSocket'a geri göndermelisiniz.

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

## Sırada ne var?

- Konuşma Etkinliği Algılama ve yerel ses özellikleri de dahil olmak üzere temel özellikler ve yapılandırmalar için Live API [Özellikleri](https://ai.google.dev/gemini-api/docs/live-guide?hl=tr) kılavuzunun tamamını okuyun.
- Live API'yi araçlarla ve işlev çağrısıyla nasıl entegre edeceğinizi öğrenmek için [Araç kullanımı](https://ai.google.dev/gemini-api/docs/live-tools?hl=tr) kılavuzunu okuyun.
- Uzun süren görüşmeleri yönetmek için [Oturum yönetimi](https://ai.google.dev/gemini-api/docs/live-session?hl=tr) kılavuzunu okuyun.
- [İstemciden sunucuya](#implementation-approach) uygulamalarda güvenli kimlik doğrulama için [Geçici jetonlar](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=tr) kılavuzunu okuyun.
- Temel alınan WebSockets API hakkında daha fazla bilgi için [WebSockets API referansı](https://ai.google.dev/api/live?hl=tr) başlıklı makaleyi inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-04-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-04-29 UTC."],[],[]]
