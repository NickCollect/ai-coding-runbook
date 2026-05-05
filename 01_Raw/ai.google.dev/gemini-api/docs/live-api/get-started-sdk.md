---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=it
fetched_at: 2026-05-05T20:07:28.280065+00:00
title: "Get started with Gemini Live API using the Google GenAI SDK \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Get started with Gemini Live API using the Google GenAI SDK

L'API Gemini Live consente un'interazione bidirezionale in tempo reale con i modelli Gemini, supportando input audio, video e di testo e output audio nativi. Questa guida spiega come eseguire l'integrazione con l'API utilizzando l'SDK Google GenAI sul server.

[Prova l'API Live in Google AI Studiomic](https://aistudio.google.com/live?hl=it)
[Clona l'app di esempio da GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[Usa le competenze dell'agente di codiceterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=it)

## Panoramica

L'API Gemini Live utilizza i WebSocket per la comunicazione in tempo reale. L'SDK `google-genai` fornisce un'interfaccia asincrona di alto livello per la gestione di queste connessioni.

Concetti chiave:

- **Sessione**: una connessione persistente al modello.
- **Configurazione**: configurazione di modalità (audio/testo), voce e istruzioni di sistema.
- **Input in tempo reale**: invio di frame audio e video come blob.

## Connessione all'API Live

Avvia una sessione dell'API Live con una chiave API:

### Python

```
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

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

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY"});
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

## Invio di testo

Il testo può essere inviato utilizzando `send_realtime_input` (Python) o `sendRealtimeInput` (JavaScript).

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

## Invio di audio

L'audio deve essere inviato come dati PCM non elaborati (audio PCM a 16 bit non elaborato, 16 kHz, little-endian).

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

Per un esempio di come ottenere l'audio dal dispositivo client (ad es. il browser)
consulta l'esempio end-to-end su [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70).

## Invio di video

I frame video vengono inviati come singole immagini (ad es. JPEG o PNG) a una frequenza fotogrammi specifica (max 1 frame al secondo).

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

Per un esempio di come ottenere il video dal dispositivo client (ad es. il browser)
consulta l'esempio end-to-end su [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120).

## Ricezione di audio

Le risposte audio del modello vengono ricevute come blocchi di dati.

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

Consulta l'app di esempio su GitHub per scoprire come [ricevere l'audio sul server](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98) e [riprodurlo nel browser](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174).

## Ricezione di testo

Le trascrizioni sia dell'input dell'utente sia dell'output del modello sono disponibili nei contenuti del server.

### Python

```
async for response in session.receive():
    content = response.server_content
    if content:
        if content.input_transcription:
            print(f"User: {content.input_transcription.text}")
        if content.output_transcription:
            print(f"Gemini: {content.output_transcription.text}")
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.inputTranscription) {
  console.log('User:', content.inputTranscription.text);
}
if (content?.outputTranscription) {
  console.log('Gemini:', content.outputTranscription.text);
}
```

## Gestione delle chiamate allo strumento

L'API supporta la chiamata allo strumento (chiamata di funzioni). Quando il modello richiede una chiamata allo strumento, devi eseguire la funzione e inviare la risposta.

### Python

```
async for response in session.receive():
    if response.tool_call:
        function_responses = []
        for fc in response.tool_call.function_calls:
            # 1. Execute the function locally
            result = my_tool_function(**fc.args)

            # 2. Prepare the response
            function_responses.append(types.FunctionResponse(
                name=fc.name,
                id=fc.id,
                response={"result": result}
            ))

        # 3. Send the tool response back to the session
        await session.send_tool_response(function_responses=function_responses)
```

### JavaScript

```
// Inside the onmessage callback
if (response.toolCall) {
  const functionResponses = [];
  for (const fc of response.toolCall.functionCalls) {
    const result = myToolFunction(fc.args);
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }
  session.sendToolResponse({ functionResponses });
}
```

## Passaggi successivi

- Leggi la guida completa alle [funzionalità](https://ai.google.dev/gemini-api/docs/live-guide?hl=it) dell'API Live per le funzionalità e le configurazioni chiave, tra cui il rilevamento dell'attività vocale e le funzionalità audio native.
- Leggi la guida all'[utilizzo degli strumenti](https://ai.google.dev/gemini-api/docs/live-tools?hl=it) per scoprire come integrare l'API Live con gli strumenti e la chiamata di funzioni.
- Leggi la guida alla [gestione delle sessioni](https://ai.google.dev/gemini-api/docs/live-session?hl=it) per gestire le conversazioni a lunga esecuzione.
- Leggi la guida ai [token effimeri](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=it) per l'autenticazione sicura nelle applicazioni [client-server](#implementation-approach).
- Per ulteriori informazioni sull'API WebSocket sottostante, consulta la [documentazione di riferimento dell'API WebSocket](https://ai.google.dev/api/live?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-04-29 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-04-29 UTC."],[],[]]
