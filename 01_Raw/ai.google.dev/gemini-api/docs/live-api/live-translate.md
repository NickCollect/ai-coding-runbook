---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=es-419
fetched_at: 2026-06-29T05:37:34.145159+00:00
title: "Traducci\u00f3n instant\u00e1nea con la API de Gemini Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Traducción instantánea con la API de Gemini Live

La API de Gemini Live admite la traducción de voz a voz en tiempo real y con baja latencia entre más de 70 idiomas con el modelo [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=es-419). Si configuras la API de Live con parámetros de configuración de traducción, puedes transmitir audio en un idioma y recibir la salida de audio traducida en otro idioma, lo que permite una traducción de voz a voz en tiempo real sin problemas.

[Probar Live Translate en Google AI Studiomic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=es-419)
[Clonar la app de ejemplo desde GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Usar las habilidades del agente de programaciónterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=es-419#gemini-live-api-dev)

## Agente en vivo vs. Traducción en vivo

Si bien ambos usan la API de Live, el modelo mental de la Traducción en vivo es diferente de las interacciones conversacionales en tiempo real con agentes.

| Agente en vivo | Traducción instantánea |
| --- | --- |
| **El modelo actúa como asistente.** Escucha, razona y realiza acciones en tu nombre. | **El modelo actúa como intérprete** y se comporta como una canalización de traducción en tiempo real. |
| **Utiliza interacciones basadas en turnos.** Se basa en pausas, detección de intención y controla las interrupciones. | **Utiliza el procesamiento de transmisión continuo.** Traduce mientras el orador habla sin esperar turnos. |
| **Admite herramientas y agentes.** Compatibilidad nativa con llamadas a funciones, la Búsqueda de Google y las instrucciones. | **Solo admite la traducción.** Traducción pura de baja latencia; no se admiten herramientas ni instrucciones. |
| **Es completamente multimodal.** Admite entradas de texto, audio, video e imagen. | **Audio restringido.** La entrada se limita al audio para garantizar umbrales estrictos de latencia en tiempo real. |
| **Configuración detallada:** Usa instrucciones de generación, voz, herramientas y sistema. | **Configuración simplificada:** Establece `target_language_code` y activa o desactiva opciones como `echo_target_language`. |

## Comenzar

En los siguientes ejemplos, se muestra cómo inicializar un cliente y conectarse a la API de Live con una configuración de traducción.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.5-live-translate-preview"
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
    output_audio_transcription=types.AudioTranscriptionConfig(),
    translation_config=types.TranslationConfig(
        target_language_code="pl",
        echo_target_language=True
    )
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started with translation")
        # Start receiving the translated audio stream
        async for response in session.receive():
            if response.server_content:
                if response.server_content.input_transcription:
                    print(f"Input transcript: {response.server_content.input_transcription.text}")
                if response.server_content.output_transcription:
                    print(f"Output transcript: {response.server_content.output_transcription.text}")
                if response.server_content.model_turn:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data:
                            audio_data = part.inline_data.data
                            # Play or process the translated audio chunk
                            print(f"Received audio chunk ({len(audio_data)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-live-translate-preview';
const config = {
    responseModalities: [Modality.AUDIO],
    inputAudioTranscription: {},
    outputAudioTranscription: {},
    translationConfig: {
        targetLanguageCode: 'pl',
        echoTargetLanguage: true
    }
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.debug('Opened'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Input transcript:', content.inputTranscription.text);
        }
        if (content?.outputTranscription) {
          console.log('Output transcript:', content.outputTranscription.text);
        }
        if (content?.modelTurn?.parts) {
          for (const part of content.modelTurn.parts) {
            if (part.inlineData) {
              const audioData = part.inlineData.data;
              // Play or process the translated audio chunk (base64 encoded)
              console.debug(`Received audio chunk (${audioData.length} bytes)`);
            }
          }
        }
      },
      onerror: (e) => console.debug('Error:', e.message),
      onclose: (e) => console.debug('Close:', e.reason),
    },
  });

  console.debug("Session started with translation");
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-live-translate-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['AUDIO'],
        inputAudioTranscription: {},
        outputAudioTranscription: {},
        translationConfig: {
          targetLanguageCode: 'pl',
          echoTargetLanguage: true
        }
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  if (response.serverContent) {
    const content = response.serverContent;
    if (content.inputTranscription) {
      console.log('Input transcript:', content.inputTranscription.text, `(${content.inputTranscription.languageCode})`);
    }
    if (content.outputTranscription) {
      console.log('Output transcript:', content.outputTranscription.text, `(${content.outputTranscription.languageCode})`);
    }
    if (content.modelTurn?.parts) {
      for (const part of content.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data;
          // Play or process the translated audio chunk (base64 encoded)
          console.debug(`Received audio chunk (${audioData.length} bytes)`);
        }
      }
    }
  }
};
```

## Cómo enviar audio

Para transmitir entradas de voz para la traducción, debes enviar audio PCM sin procesar de 16 bits, little-endian.

- **Formato de audio de entrada**: PCM sin procesar de 16 bits a 16 kHz (mono, little-endian).
- **Formato de audio de salida**: PCM sin procesar de 16 bits a 24 kHz (mono, little-endian).
- **Tamaño de fragmento y latencia**: Envía audio en fragmentos de 100 ms.

En los siguientes ejemplos, se muestra cómo enviar fragmentos de audio a la sesión.

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

### WebSockets

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
  }
}
```

## Configuración

Para habilitar la traducción, debes especificar `translationConfig` dentro de `generationConfig` durante la configuración de la sesión.

### Configura los mensajes

`generationConfig` admite los siguientes campos para habilitar las transcripciones:

- **`inputAudioTranscription`**: Es un objeto que, cuando está presente, permite que el modelo envíe transcripciones de texto del audio de entrada.
- **`outputAudioTranscription`**: Es un objeto que, cuando está presente, permite que el modelo envíe transcripciones de texto del audio de salida (traducido).

El objeto `translationConfig` admite los siguientes campos:

- **`targetLanguageCode`**: Es el [código de idioma BCP-47](#supported-languages) del idioma al que deseas que se traduzca el modelo (p.ej., `"pl"` para y `"es"` para español). La configuración predeterminada es `"en"`.
- **`echoTargetLanguage`**: Es un valor booleano que indica cómo se debe controlar el audio de entrada que ya está en el idioma de destino. Si se configura como `true`, el modelo repetirá el audio de entrada que ya está en el idioma de destino. Si se configura como `false`, el modelo permanecerá en silencio cuando el discurso de entrada ya esté en el idioma de destino. El valor predeterminado es `false`.

A continuación, se muestra un ejemplo de la estructura del mensaje de configuración:

```
"setup": {
    "model": "models/gemini-3.5-live-translate-preview",
    "generationConfig": {
      "responseModalities": [
        "AUDIO"
      ],
      "inputAudioTranscription": {},
      "outputAudioTranscription": {},
      "translationConfig": {
        "targetLanguageCode": "pl",
        "echoTargetLanguage": true
      }
    }
}
```

## Tokens efímeros para aplicaciones del cliente

En el caso de las aplicaciones cliente-servidor, puedes usar [tokens efímeros](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=es-419) (actualmente en `v1alpha`) para evitar exponer tu clave de API.

Cuando se usan tokens efímeros con la Traducción instantánea, sucede lo siguiente:

1. Debes usar el extremo `v1alpha`.
2. **Configuración de bloqueo:** De forma predeterminada, debes especificar el `translationConfig` en las restricciones de creación de tokens en tu servidor. Esto garantiza que la configuración de traducción esté bloqueada y que el cliente no pueda manipularla.
3. **Configuración de desbloqueo:** Si deseas poder establecer `translationConfig` en el cliente (por ejemplo, para permitir que un usuario elija su propio idioma objetivo), debes omitirlo en la solicitud de creación de tokens y establecer `"lock_additional_fields": []` en su lugar. Esto desbloqueará `translationConfig` para que se configure en el cliente.

### Cómo crear un token efímero restringido

En los siguientes ejemplos, se muestra cómo crear un token efímero con restricciones de traducción.

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha'}
)

token = client.auth_tokens.create(
    config = {
        'uses': 1,
        'expire_time': now + datetime.timedelta(minutes=30),
        'live_connect_constraints': {
            'model': 'gemini-3.5-live-translate-preview',
            'config': {
                'translation_config': {
                    'target_language_code': 'pl',
                    'echo_target_language': True
                }
            }
        },
        'http_options': {'api_version': 'v1alpha'},
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1,
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.5-live-translate-preview',
            config: {
                responseModalities: ['AUDIO'],
                inputAudioTranscription: {},
                outputAudioTranscription: {},
                translationConfig: {
                    targetLanguageCode: 'pl',
                    echoTargetLanguage: true
                }
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    },
});
```

## Limitaciones

- **Modalidades de entrada**: Solo se admite la entrada de audio para la traducción. No se admite la entrada de texto.
- **Replicación de voz**: La replicación de voz puede ser incoherente. Las voces pueden cambiar después de pausas largas, asignar el género incorrecto según cómo comienza el discurso o quedarse atascadas en una voz durante conversaciones rápidas con varios oradores.
- **Detección de idioma**: La detección de idioma tiene dificultades con los acentos marcados, los idiomas similares (p. ej., español y portugués) o los cambios rápidos de idioma. **Nota:** Esto solo debería afectar la transcripción de entrada. Los códigos de idioma y la traducción final deben seguir siendo precisos.
- **Audio de fondo**: El modelo está diseñado para filtrar el ruido y la música y producir un discurso limpio, pero es posible que no se ignore todo el audio de fondo.
- **Echo Target Language**: Cuando `echoTargetLanguage: true`, el ruido de fondo o la música pueden introducir artefactos en el audio traducido si el audio de entrada ya está en el idioma de destino.

## Idiomas admitidos

Los siguientes idiomas son compatibles con la Traducción instantánea.

| Idioma | Código BCP-47 | Idioma | Código BCP-47 |
| --- | --- | --- | --- |
| Afrikaans | af | Kazajo | kk |
| Akan | ak | Jemer | km |
| Albanés | sq | Kiñarwanda | rw |
| Amárico | am | Coreano | ko |
| Árabe | ar | Laosiano | lo |
| Armenio | hy | Letón | lv |
| Azerí | az | Lituano | lt |
| Vasco | eu | Macedonio | mk |
| Bielorruso | be | Malayo | ms |
| Bengalí | bn | Malayalam | ml |
| Búlgaro | bg | Marathi | mr |
| Birmano (Birmania) | my | Mongol | mn |
| Catalán | ca | Nepalí | ne |
| Chino (simplificado) | zh-Hans | Noruego | no, nb |
| Chino (tradicional) | zh-Hant | Persa | fa |
| Croata | h | Polaco | pl |
| Checo | cs | Portugués (Brasil) | pt-BR |
| Danés | da | Portugués (Portugal) | pt-PT |
| Holandés | nl | Punyabí | pa |
| Inglés | en | Rumano | ro |
| Estonio | et | Ruso | ru |
| Filipino | fil | Serbio | sr |
| Finlandés | fi | Sindhi | sd |
| Francés | fr | Cingalés | si |
| Gallego | gl | Eslovaco | sk |
| Georgiano | ka | Esloveno | sl |
| Alemán | de | Español | es |
| Griego | el | Sundanés | su |
| Gujarati | gu | Suajili | sw |
| Hausa | ha | Sueco | sv |
| Hebreo | él | Tamil | ta |
| Hindi | hi | Telugu | te |
| Húngaro | hu | Tailandés | th |
| Islandés | es | Turco | tr |
| Indonesio | id | Ucraniano | uk |
| Italiano | it | Urdu | ur |
| Japonés | ja | Uzbeko | uz |
| Javanés | jv | Vietnamita | vi |
| Canarés | kn | Zulú | zu |

## ¿Qué sigue?

- Lee la guía completa de [Funciones](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=es-419) de la API de Live.
- Lee la guía [Cómo comenzar a usar el SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=es-419).
- Lee la guía [Comienza a usar WebSockets](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=es-419).
- Lee la guía sobre [tokens efímeros](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=es-419) para obtener información sobre la autenticación segura en aplicaciones cliente-servidor.
- Clona los [ejemplos de la API en vivo](https://github.com/google-gemini/gemini-live-api-examples) desde GitHub.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-09 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-09 (UTC)"],[],[]]
