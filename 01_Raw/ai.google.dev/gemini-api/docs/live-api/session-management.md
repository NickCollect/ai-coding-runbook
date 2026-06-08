---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=es-419
fetched_at: 2026-06-08T05:26:57.980957+00:00
title: "Administraci\u00f3n de sesiones con la API de Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Administración de sesiones con la API de Live

En la API de Live, una sesión hace referencia a una conexión persistente
en la que la entrada y la salida se transmiten de forma continua a través de la misma
conexión (obtén más información sobre [cómo funciona](https://ai.google.dev/gemini-api/docs/live?hl=es-419)).
Este diseño de sesión único permite una latencia baja y admite funciones únicas, pero también puede presentar desafíos, como límites de tiempo de sesión y finalización anticipada.
En esta guía, se describen estrategias para superar los desafíos de administración de sesiones que pueden surgir cuando se usa la API de Live.

## Duración de la sesión

Sin compresión, las sesiones solo de audio se limitan a 15 minutos y las sesiones de audio y video se limitan a 2 minutos. Si se superan estos límites
se finalizará la sesión (y, por lo tanto, la conexión), pero puedes usar
[la compresión de la ventana de contexto](#context-window-compression) para extender las sesiones por
un tiempo ilimitado.

La duración de una conexión también está limitada a unos 10 minutos. Cuando finaliza la conexión, también finaliza la sesión. En este caso, puedes
configurar una sola sesión para que permanezca activa en varias conexiones mediante la
[reanudación de la sesión](#session-resumption).
También recibirás un [mensaje de GoAway](#goaway-message) antes de que finalice la
conexión, lo que te permitirá realizar más acciones.

## Compresión de la ventana de contexto

Para habilitar sesiones más largas y evitar la finalización abrupta de la conexión, puedes
habilitar la compresión de la ventana de contexto configurando el campo [contextWindowCompression](https://ai.google.dev/api/live?hl=es-419#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression)
como parte de la configuración de la sesión.

En [ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=es-419#contextwindowcompressionconfig), puedes configurar un
[mecanismo de ventana deslizante](https://ai.google.dev/api/live?hl=es-419#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window)
y la [cantidad de tokens](https://ai.google.dev/api/live?hl=es-419#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens)
que activan la compresión.

### Python

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        # Configures compression with default parameters.
        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  contextWindowCompression: { slidingWindow: {} }
};
```

## Reanudación de sesión

Para evitar la finalización de la sesión cuando el servidor restablece periódicamente la conexión WebSocket, configura el campo [sessionResumption](https://ai.google.dev/api/live?hl=es-419#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption)
dentro de la [configuración de configuración](https://ai.google.dev/api/live?hl=es-419#BidiGenerateContentSetup).

Si pasas esta configuración, el
servidor enviará mensajes de [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=es-419#SessionResumptionUpdate)
, que se pueden usar para reanudar la sesión pasando el último token de reanudación
como el [`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=es-419#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle)
de la conexión posterior.

Los tokens de reanudación son válidos durante 2 horas después de la finalización de la última sesión.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

async def main():
    print(f"Connecting to the service with handle {previous_session_handle}...")
    async with client.aio.live.connect(
        model=model,
        config=types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            session_resumption=types.SessionResumptionConfig(
                # The handle of the session to resume is passed here,
                # or else None to start a new session.
                handle=previous_session_handle
            ),
        ),
    ) as session:
        while True:
            await session.send_client_content(
                turns=types.Content(
                    role="user", parts=[types.Part(text="Hello world!")]
                )
            )
            async for message in session.receive():
                # Periodically, the server will send update messages that may
                # contain a handle for the current state of the session.
                if message.session_resumption_update:
                    update = message.session_resumption_update
                    if update.resumable and update.new_handle:
                        # The handle should be retained and linked to the session.
                        return update.new_handle

                # For the purposes of this example, placeholder input is continually fed
                # to the model. In non-sample code, the model inputs would come from
                # the user.
                if message.server_content and message.server_content.turn_complete:
                    break

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

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

console.debug('Connecting to the service with handle %s...', previousSessionHandle)
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
  config: {
    responseModalities: [Modality.AUDIO],
    sessionResumption: { handle: previousSessionHandle }
    // The handle of the session to resume is passed here, or else null to start a new session.
  }
});

const inputTurns = 'Hello how are you?';
session.sendClientContent({ turns: inputTurns });

const turns = await handleTurn();
for (const turn of turns) {
  if (turn.sessionResumptionUpdate) {
    if (turn.sessionResumptionUpdate.resumable && turn.sessionResumptionUpdate.newHandle) {
      let newHandle = turn.sessionResumptionUpdate.newHandle
      // ...Store newHandle and start new session with this handle here
    }
  }
}

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## Cómo recibir un mensaje antes de que se desconecte la sesión

El servidor envía un mensaje de [GoAway](https://ai.google.dev/api/live?hl=es-419#GoAway) que indica que la conexión actual finalizará pronto. Este mensaje incluye [timeLeft](https://ai.google.dev/api/live?hl=es-419#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left),
que indica el tiempo restante y te permite realizar más acciones antes de que la
conexión finalice como ABORTED.

### Python

```
async for response in session.receive():
    if response.go_away is not None:
        # The connection will soon be terminated
        print(response.go_away.time_left)
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.goAway) {
    console.debug('Time left: %s\n', turn.goAway.timeLeft);
  }
}
```

## Cómo recibir un mensaje cuando se completa la generación

El servidor envía un mensaje de [generationComplete](https://ai.google.dev/api/live?hl=es-419#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete)
que indica que el modelo terminó de generar la respuesta.

### Python

```
async for response in session.receive():
    if response.server_content.generation_complete is True:
        # The generation is complete
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.generationComplete) {
    // The generation is complete
  }
}
```

## ¿Qué sigue?

Explora más formas de trabajar con la API de Live en la guía completa de
[capacidades](https://ai.google.dev/gemini-api/docs/live?hl=es-419),
la página [Uso de herramientas](https://ai.google.dev/gemini-api/docs/live-tools?hl=es-419) o el
[libro de recetas de la API de Live](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-01 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-01 (UTC)"],[],[]]
