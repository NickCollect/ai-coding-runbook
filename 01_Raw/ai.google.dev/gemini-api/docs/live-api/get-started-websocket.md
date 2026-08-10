---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=it
fetched_at: 2026-08-10T03:15:43.009929+00:00
title: "Inizia a utilizzare l'API Gemini Live con i WebSocket \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Inizia a utilizzare l'API Gemini Live con i WebSocket

L'API Gemini Live consente l'interazione bidirezionale in tempo reale con i modelli Gemini, supportando input audio, video e di testo e output audio nativi. Questa guida spiega come eseguire l'integrazione direttamente con l'API utilizzando WebSocket non elaborati.

[Prova l'API Live in Google AI Studiomic](https://aistudio.google.com/live?hl=it)
[Clona l'app di esempio da GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[Usa le competenze dell'agente di codificaterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=it)

## Panoramica

L'API Gemini Live utilizza WebSocket per la comunicazione in tempo reale. A differenza dell'utilizzo di un SDK, questo approccio prevede la gestione diretta della connessione WebSocket e l'invio/la ricezione di messaggi in un formato JSON specifico definito dall'API.

Concetti chiave:

- **Endpoint WebSocket**: l'URL specifico a cui connettersi.
- **Formato dei messaggi**: tutte le comunicazioni vengono effettuate tramite messaggi JSON conformi alle strutture [`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=it#bidigeneratecontentclientmessage) e [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=it#bidigeneratecontentservermessage).
- **Gestione delle sessioni**: sei responsabile della manutenzione della connessione WebSocket.

## Autenticazione

L'autenticazione viene gestita includendo la chiave API come parametro di query nell'URL WebSocket.

Il formato dell'endpoint è:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

Sostituisci `YOUR_API_KEY` con la tua chiave API effettiva.

## Autenticazione con token effimeri

Se utilizzi [token effimeri](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=it), devi connetterti all'endpoint `v1beta`.
Il token effimero deve essere passato come parametro di query `access_token`.

Il formato dell'endpoint per le chiavi effimere è:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

Sostituisci `{short-lived-token}` con il token effimero effettivo.

## Connettiti all'API Live

Per avviare una sessione live, stabilisci una connessione WebSocket all'endpoint autenticato.
Il primo messaggio inviato tramite WebSocket deve essere un [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=it#bidigeneratecontentsetup) contenente la `config`.
Per le opzioni di configurazione complete, consulta il [Riferimento API Live - API WebSocket](https://ai.google.dev/api/live?hl=it).

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

## Invia testo

Per inviare input di testo, crea un [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=it#bidigeneratecontentrealtimeinput) messaggio con il `text` campo.

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

## Invia audio

L'audio deve essere inviato come dati PCM non elaborati (audio PCM non elaborato a 16 bit, 16 kHz, little-endian). Crea un messaggio [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=it#bidigeneratecontentrealtimeinput) con i dati audio. Il `mimeType` è fondamentale.

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

Per un esempio di come ottenere l'audio dal dispositivo client (ad es. il browser)
consulta l'esempio end-to-end su [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74).

## Invia video

I frame video vengono inviati come singole immagini (ad es. JPEG o PNG). Analogamente all'audio, utilizza `realtimeInput` con un `Blob`, specificando il `mimeType` corretto.

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

Per un esempio di come ottenere il video dal dispositivo client (ad es. il browser)
consulta l'esempio end-to-end su [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222).

## Ricevi le risposte

WebSocket invierà i messaggi [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=it#bidigeneratecontentservermessage). Devi analizzare questi messaggi JSON e gestire diversi tipi di contenuti.

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

Per un esempio di come gestire la risposta, consulta l'esempio end-to-end su [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75).

## Gestisci le chiamate allo strumento

Quando il modello richiede una chiamata allo strumento, il [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=it#bidigeneratecontentservermessage) conterrà un campo `toolCall`. Devi eseguire la funzione localmente e inviare il risultato a WebSocket utilizzando un [`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=it#bidigeneratecontenttoolresponse) messaggio.

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

## Passaggi successivi

- Leggi la guida completa Funzionalità dell'API Live [Funzionalità](https://ai.google.dev/gemini-api/docs/live-guide?hl=it) per funzionalità e configurazioni chiave, tra cui il rilevamento di attività vocale e le funzionalità audio native.
- Leggi la guida [Utilizzo degli strumenti](https://ai.google.dev/gemini-api/docs/live-tools?hl=it) per scoprire come integrare l'API Live con gli strumenti e le chiamate di funzioni.
- Leggi la guida [Gestione delle sessioni](https://ai.google.dev/gemini-api/docs/live-session?hl=it) per gestire le conversazioni a lunga esecuzione.
- Leggi la guida [Token effimeri](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=it) per l'autenticazione sicura nelle applicazioni [client-server](#implementation-approach).
- Per ulteriori informazioni sull'API WebSocket sottostante, consulta il [Riferimento API WebSocket](https://ai.google.dev/api/live?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-23 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-23 UTC."],[],[]]
