---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=es-419
fetched_at: 2026-10-26T05:52:04.128161+00:00
title: "Comienza a usar la API de Gemini Live con el SDK de IA generativa de Google \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Comienza a usar la API de Gemini Live con el SDK de IA generativa de Google

La API de Gemini Live permite la interacción bidireccional en tiempo real con los modelos de Gemini, admite entradas de audio, video y texto, y salidas de audio nativas. En esta guía, se explica cómo realizar la integración con la API mediante el SDK de Google GenAI en tu servidor.

[Prueba la API de Live en Google AI Studiomic](https://aistudio.google.com/live?hl=es-419)
[Clona la app de ejemplo desde GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[Usa las habilidades del agente de codificaciónterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=es-419)

## Descripción general

La API de Gemini Live usa WebSockets para la comunicación en tiempo real. El SDK de `google-genai` proporciona una interfaz asíncrona de alto nivel para administrar estas conexiones.

Conceptos clave:

- **Sesión**: Es una conexión persistente al modelo.
- **Configuración**: Es la configuración de modalidades (audio/texto), voz y las instrucciones del sistema.
- **Entrada en tiempo real**: Es el envío de fotogramas de audio y video como objetos binarios grandes.

## Cómo conectarse a la API de Live

Inicia una sesión de la API de Live con una clave de API:

### Python

```
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

model = "gemini-3.8-live"
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
const model = 'gemini-3.8-live';
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

## Cómo enviar texto

El texto se puede enviar con `send_realtime_input` (Python) o `sendRealtimeInput` (JavaScript).

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

## Cómo enviar audio

El audio debe enviarse como datos PCM sin procesar (audio PCM sin procesar de 16 bits, 16 kHz, little-endian).

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

Para ver un ejemplo de cómo obtener el audio del dispositivo cliente (p.ej., el navegador)
consulta el ejemplo de extremo a extremo en [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70).

## Cómo enviar video

Los fotogramas de video se envían como imágenes individuales (p.ej., JPEG o PNG) a una velocidad de fotogramas específica (máximo 1 fotograma por segundo).

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

Para ver un ejemplo de cómo obtener el video del dispositivo cliente (p.ej., el navegador)
consulta el ejemplo de extremo a extremo en [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120).

## Cómo recibir audio

Las respuestas de audio del modelo se reciben como fragmentos de datos.

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

Consulta la app de ejemplo en GitHub para aprender a [recibir el audio en tu servidor](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98) y [reproducirlo en el navegador](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174).

## Cómo recibir texto

Las transcripciones de la entrada del usuario y el resultado del modelo están disponibles en el contenido del servidor.

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

## Cómo controlar las llamadas a herramientas

La API admite llamadas a herramientas (llamadas a funciones). Cuando el modelo solicita una llamada a herramienta, debes ejecutar la función y enviar la respuesta.

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

## ¿Qué sigue?

- Lee la guía completa de capacidades de la API de Live [Capabilities](https://ai.google.dev/gemini-api/docs/live-guide?hl=es-419) para conocer las capacidades y configuraciones clave, incluidas la detección de actividad de voz y las funciones de audio nativas.
- Lee la [guía de uso de herramientas](https://ai.google.dev/gemini-api/docs/live-tools?hl=es-419) para aprender a integrar la API de Live con herramientas y llamadas a funciones.
- Lee la guía de [administración de sesiones](https://ai.google.dev/gemini-api/docs/live-session?hl=es-419) para administrar conversaciones de larga duración.
- Lee la guía de [tokens efímeros](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=es-419) para obtener información sobre la autenticación segura en aplicaciones de [cliente a servidor](https://ai.google.dev/gemini-api/docs/live-api?hl=es-419#implementation-approach).
- Para obtener más información sobre la API de WebSockets subyacente, consulta la [referencia de la API de WebSockets](https://ai.google.dev/api/live?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-17 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-17 (UTC)"],[],[]]
