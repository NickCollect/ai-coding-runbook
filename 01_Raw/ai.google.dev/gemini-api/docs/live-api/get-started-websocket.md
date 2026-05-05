---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=id
fetched_at: 2026-05-05T20:05:00.529379+00:00
title: "Get started with Gemini Live API using WebSockets \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Get started with Gemini Live API using WebSockets

Gemini Live API memungkinkan interaksi dua arah secara real-time dengan model Gemini, yang mendukung input audio, video, dan teks serta output audio native. Panduan ini menjelaskan cara berintegrasi langsung dengan API menggunakan WebSockets mentah.

[Coba Live API di Google AI Studiomic](https://aistudio.google.com/live?hl=id)
[Clone aplikasi contoh dari GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[Gunakan keterampilan agen codingterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=id)

## Ringkasan

Gemini Live API menggunakan WebSockets untuk komunikasi real-time. Tidak seperti penggunaan SDK, pendekatan ini melibatkan pengelolaan koneksi WebSocket secara langsung dan pengiriman/penerimaan pesan dalam format JSON tertentu yang ditentukan oleh API.

Konsep utama:

- **WebSocket Endpoint**: URL spesifik untuk terhubung.
- **Format Pesan**: Semua komunikasi dilakukan melalui pesan JSON yang sesuai dengan struktur [`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=id#bidigeneratecontentclientmessage) dan [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=id#bidigeneratecontentservermessage).
- **Pengelolaan Sesi**: Anda bertanggung jawab untuk mempertahankan koneksi WebSocket.

## Autentikasi

Autentikasi ditangani dengan menyertakan kunci API Anda sebagai parameter kueri di URL WebSocket.

Format endpointnya adalah:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

Ganti `YOUR_API_KEY` dengan kunci API Anda yang sebenarnya.

## Autentikasi dengan Token Sementara

Jika Anda menggunakan [token sementara](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=id), Anda harus terhubung ke endpoint `v1alpha`.
Token sementara harus diteruskan sebagai parameter kueri `access_token`.

Format endpoint untuk kunci sementara adalah:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

Ganti `{short-lived-token}` dengan token sementara yang sebenarnya.

## Menghubungkan ke Live API

Untuk memulai sesi live, buat koneksi WebSocket ke endpoint yang diautentikasi.
Pesan pertama yang dikirim melalui WebSocket harus berupa [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=id#bidigeneratecontentsetup) yang berisi `config`.
Untuk mengetahui opsi konfigurasi lengkap, lihat [Referensi API Live - WebSockets API](https://ai.google.dev/api/live?hl=id).

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

## Mengirim SMS

Untuk mengirim input teks, buat pesan [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=id#bidigeneratecontentrealtimeinput) dengan kolom `text`.

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

## Mengirim audio

Audio harus dikirim sebagai data PCM mentah (audio PCM 16-bit mentah, 16 kHz, little-endian). Buat pesan [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=id#bidigeneratecontentrealtimeinput) dengan data audio. `mimeType` sangat penting.

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

Untuk contoh cara mendapatkan audio dari perangkat klien (misalnya, browser), lihat contoh end-to-end di [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74).

## Mengirim video

Frame video dikirim sebagai gambar individual (misalnya, JPEG atau PNG). Mirip dengan audio, gunakan `realtimeInput` dengan `Blob`, yang menentukan `mimeType` yang benar.

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

Untuk contoh cara mendapatkan video dari perangkat klien (misalnya, browser),
lihat contoh end-to-end di [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222).

## Menerima respons

WebSocket akan mengirim kembali pesan [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=id#bidigeneratecontentservermessage). Anda perlu mengurai pesan JSON ini dan menangani berbagai jenis konten.

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

Untuk contoh cara menangani respons, lihat contoh end-to-end di [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75).

## Menangani panggilan alat

Saat model meminta panggilan alat, [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=id#bidigeneratecontentservermessage) akan berisi kolom `toolCall`. Anda harus menjalankan fungsi secara lokal dan mengirimkan hasilnya kembali ke WebSocket menggunakan pesan [`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=id#bidigeneratecontenttoolresponse).

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

## Langkah berikutnya

- Baca panduan [Kemampuan](https://ai.google.dev/gemini-api/docs/live-guide?hl=id) Live API lengkap untuk mengetahui kemampuan dan konfigurasi utama; termasuk Deteksi Aktivitas Suara dan fitur audio bawaan.
- Baca panduan [Penggunaan alat](https://ai.google.dev/gemini-api/docs/live-tools?hl=id) untuk mempelajari cara mengintegrasikan Live API dengan alat dan panggilan fungsi.
- Baca panduan [Pengelolaan sesi](https://ai.google.dev/gemini-api/docs/live-session?hl=id) untuk mengelola percakapan yang berjalan lama.
- Baca panduan [Token sementara](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=id) untuk autentikasi yang aman di aplikasi [klien ke server](#implementation-approach).
- Untuk mengetahui informasi selengkapnya tentang WebSockets API yang mendasarinya, lihat [Referensi WebSockets API](https://ai.google.dev/api/live?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-04-29 UTC."],[],[]]
