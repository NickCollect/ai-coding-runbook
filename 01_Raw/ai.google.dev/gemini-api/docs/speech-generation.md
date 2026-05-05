---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419
fetched_at: 2026-05-05T20:02:41.948172+00:00
title: "Generaci\u00f3n de texto a voz (TTS) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Generación de texto a voz (TTS)

La API de Gemini puede transformar la entrada de texto en audio de un solo orador o varios oradores con las capacidades de generación de texto a voz (TTS) de Gemini.
La generación de texto a voz (TTS) es *[controlable](#controllable)*, lo que significa que puedes usar el lenguaje natural para estructurar las interacciones y guiar el *estilo*, el *acento*, el *ritmo* y el *tono* del audio.

[Probar en Google AI Studio](https://aistudio.google.com/apps/bundled/voice-library?showPreview=truew&hl=es-419)

La capacidad de TTS difiere de la generación de voz que proporciona la [API en vivo](https://ai.google.dev/gemini-api/docs/live?hl=es-419), que está diseñada para audio interactivo y no estructurado, y entradas y salidas multimodales. Si bien la API de Live se destaca en contextos conversacionales dinámicos, la API de Gemini ofrece TTS adaptado para situaciones que requieren una recitación de texto exacta con un control detallado sobre el estilo y el sonido, como la generación de podcasts o audiolibros.

En esta guía, se muestra cómo generar audio de un solo interlocutor y de varios interlocutores a partir de texto.

## Antes de comenzar

Asegúrate de usar una variante del modelo de Gemini con capacidades de texto a voz (TTS) de Gemini, como se indica en la sección [Modelos compatibles](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419#supported-models). Para obtener resultados óptimos, considera qué modelo se adapta mejor a tu caso de uso específico.

Antes de comenzar a compilar, te recomendamos que [pruebes los modelos de Gemini TTS en AI Studio](https://aistudio.google.com/generate-speech?hl=es-419).

## TTS de un solo interlocutor

Para convertir texto en audio de un solo orador, establece la modalidad de respuesta en "audio" y pasa un objeto `SpeechConfig` con `VoiceConfig` establecido.
Deberás elegir un nombre de voz de las [voces de salida](#voices) prediseñadas.

En este ejemplo, se guarda el audio de salida del modelo en un archivo wave:

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents="Say cheerfully: Have a wonderful day!",
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: 'Say cheerfully: Have a wonderful day!' }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               voiceConfig: {
                  prebuiltVoiceConfig: { voiceName: 'Kore' },
               },
            },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "parts":[{
            "text": "Say cheerfully: Have a wonderful day!"
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }
        },
        "model": "gemini-3.1-flash-tts-preview",
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode >out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## TTS con varios interlocutores

Para el audio con varios interlocutores, necesitarás un objeto `MultiSpeakerVoiceConfig` con cada interlocutor (hasta 2) configurado como un `SpeakerVoiceConfig`.
Deberás definir cada `speaker` con los mismos nombres que se usan en la [instrucción](#controllable):

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=prompt,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Joe',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Jane',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const ai = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: prompt }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               multiSpeakerVoiceConfig: {
                  speakerVoiceConfigs: [
                        {
                           speaker: 'Joe',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Kore' }
                           }
                        },
                        {
                           speaker: 'Jane',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Puck' }
                           }
                        }
                  ]
               }
            }
      }
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
  "contents": [{
    "parts":[{
      "text": "TTS the following conversation between Joe and Jane:
                Joe: Hows it going today Jane?
                Jane: Not too bad, how about you?"
    }]
  }],
  "generationConfig": {
    "responseModalities": ["AUDIO"],
    "speechConfig": {
      "multiSpeakerVoiceConfig": {
        "speakerVoiceConfigs": [{
            "speaker": "Joe",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }, {
            "speaker": "Jane",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Puck"
              }
            }
          }]
      }
    }
  },
  "model": "gemini-3.1-flash-tts-preview",
}' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
    base64 --decode > out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## Cómo controlar el estilo de voz con instrucciones

Puedes controlar el estilo, el tono, el acento y el ritmo con instrucciones en lenguaje natural o [etiquetas de audio](#transcript-tags) para TTS de uno o varios oradores.
Por ejemplo, en una instrucción de un solo orador, puedes decir lo siguiente:

```
Say in an spooky voice:
"By the pricking of my thumbs... [short pause]
[whisper] Something wicked this way comes"
```

En una instrucción con varios oradores, proporciona al modelo el nombre de cada orador y la transcripción correspondiente. También puedes proporcionar orientación para cada orador de forma individual:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... [yawn] what's on the agenda today?
Speaker2: You're never going to guess!
```

Intenta usar una [opción de voz](#voices) que corresponda al estilo o la emoción que quieras transmitir para enfatizarlo aún más. En la instrucción anterior, por ejemplo, el tono jadeante de *Encélado* podría enfatizar “cansado” y “aburrido”, mientras que el tono alegre de *Puck* podría complementar “emocionado” y “feliz”.

## Generando una instrucción para convertirla en audio

Los modelos de TTS solo generan audio, pero puedes usar [otros modelos](https://ai.google.dev/gemini-api/docs/models?hl=es-419) para generar primero una transcripción y, luego, pasarla al modelo de TTS para que la lea en voz alta.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

transcript = client.models.generate_content(
   model="gemini-3-flash-preview",
   contents="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam.""").text

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=transcript,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Dr. Anya',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Liam',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

# ...Code to handle audio output
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {

const transcript = await ai.models.generateContent({
   model: "gemini-3-flash-preview",
   contents: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const response = await ai.models.generateContent({
   model: "gemini-3.1-flash-tts-preview",
   contents: transcript,
   config: {
      responseModalities: ['AUDIO'],
      speechConfig: {
         multiSpeakerVoiceConfig: {
            speakerVoiceConfigs: [
                   {
                     speaker: "Dr. Anya",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Kore"},
                     }
                  },
                  {
                     speaker: "Liam",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Puck"},
                    }
                  }
                ]
              }
            }
      }
  });
}
// ..JavaScript code for exporting .wav file for output audio

await main();
```

## Opciones de voz

Los modelos de TTS admiten las siguientes 30 opciones de voz en el campo `voice_name`:

|  |  |  |
| --- | --- | --- |
| **Zephyr**: *Brillo* | **Puck**: *Optimista* | **Charon**: *Informativa* |
| **Kore**, *firme* | **Fenrir**: *Excitabilidad* | **Leda**: *Juvenil* |
| **Orus**, *Firme* | **Aoede**: *Breezy* | **Callirrhoe**: *Fácil de llevar* |
| **Autonoe**: *Brillo* | **Enceladus**: *Respiración* | **Iapetus**: *Claro* |
| **Umbriel**: *Tranquilo* | **Algieba**: *Suave* | **Despina**: *Suave* |
| **Erinome**: *Despejado* | **Algenib**: *Arenoso* | **Rasalgethi**: *Informativa* |
| **Laomedeia**: *Optimista* | **Achernar**: *Suave* | **Alnilam**: *Firme* |
| **Schedar**: *Par* | **Gacrux**: *Contenido para mayores* | **Pulcherrima**: *Hacia adelante* |
| **Achird**: *Amistoso* | **Zubenelgenubi**: *Casual* | **Vindemiatrix**: *Suave* |
| **Sadachbia**: *Animada* | **Sadaltager**: *Conocimiento* | **Sulafat**: *Cálida* |

Puedes escuchar todas las opciones de voz en [AI Studio](https://aistudio.google.com/generate-speech?hl=es-419).

## Idiomas admitidos

Los modelos de TTS detectan automáticamente el idioma de entrada. Se admiten los siguientes idiomas:

| Idioma | Código BCP-47 | Idioma | Código BCP-47 |
| --- | --- | --- | --- |
| Árabe | ar | Filipino | fil |
| Bengalí | bn | Finlandés | fi |
| Holandés | nl | Gallego | gl |
| Inglés | en | Georgiano | ka |
| Francés | fr | Griego | el |
| Alemán | de | Gujarati | gu |
| Hindi | hi | Criollo haitiano | ht |
| Indonesio | id | Hebreo | él |
| Italiano | it | Húngaro | hu |
| Japonés | ja | Islandés | es |
| Coreano | ko | Javanés | jv |
| Marathi | mr | Canarés | kn |
| Polaco | pl | Konkani | kok |
| Portugués | pt | Laosiano | lo |
| Rumano | ro | Latín | la |
| Ruso | ru | Letón | lv |
| Español | es | Lituano | lt |
| Tamil | ta | Luxemburgués | lb |
| Telugu | te | Macedonio | mk |
| Tailandés | th | Maithili | mai |
| Turco | tr | Malgache | mg |
| Ucraniano | uk | Malayo | ms |
| Vietnamita | vi | Malayalam | ml |
| Afrikaans | af | Mongol | mn |
| Albanés | sq | Nepalí | ne |
| Amárico | am | Noruego (Bokmal) | nb |
| Armenio | hy | Noruego (Nynorsk) | nn |
| Azerí | az | Oriya | o |
| Vasco | eu | Pastún | ps |
| Bielorruso | be | Persa | fa |
| Búlgaro | bg | Punyabí | pa |
| Birmano | my | Serbio | sr |
| Catalán | ca | Sindhi | sd |
| Cebuano | ceb | Cingalés | si |
| Chino (mandarín) | cmn | Eslovaco | sk |
| Croata | h | Esloveno | sl |
| Checo | cs | Suajili | sw |
| Danés | da | Sueco | sv |
| Estonio | et | Urdu | ur |

## Modelos compatibles

| Modelo | Orador único | Varios oradores |
| --- | --- | --- |
| [Versión preliminar del TTS de Gemini 3.1 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=es-419) | ✔️ | ✔️ |
| [TTS de Gemini 2.5 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=es-419) | ✔️ | ✔️ |
| [TTS de Gemini 2.5 Pro en versión preliminar](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=es-419) | ✔️ | ✔️ |

## Guía de instrucciones

El modelo de **generación de audio nativo de Gemini con texto a voz (TTS)** se diferencia de los modelos de TTS tradicionales porque usa un modelo de lenguaje grande que sabe ***no solo qué decir, sino también cómo decirlo***.

De forma predeterminada, el modelo interpretará una transcripción de forma nativa y determinará cómo se deben transmitir tus palabras. Las transcripciones simples sin indicaciones adicionales suenan naturales. Sin embargo, la función de TTS de Gemini también incluye herramientas que puedes usar para dirigirla.

El objetivo de esta guía es ofrecer orientación fundamental y generar ideas cuando desarrolles experiencias de audio. Comenzaremos con las **etiquetas** para un control rápido intercalado y, luego, exploraremos las **estructuras de instrucciones** avanzadas para una dirección de rendimiento completa.

### Etiquetas de audio

Las etiquetas son modificadores intercalados, como `[whispers]` o `[laughs]`, que te brindan un control detallado sobre la publicación. Puedes usarlos para cambiar el tono, el ritmo y el ambiente emocional de una línea o sección de la transcripción. También puedes usarlos para agregar interjecciones y algunos otros sonidos no verbales a la interpretación, como `[cough]`, `[sighs]` o `[gasp]`.

No hay una lista exhaustiva de las etiquetas que funcionan y las que no. Te recomendamos que experimentes con diferentes emociones y expresiones para ver cómo cambia el resultado.

Si tu transcripción no está en inglés, para obtener mejores resultados, te recomendamos que uses etiquetas de audio en inglés.

**Usa tu creatividad con las etiquetas de audio**

Para mostrar la variabilidad que puedes obtener con las etiquetas de audio, aquí tienes un conjunto de ejemplos que dicen lo mismo, pero la entrega cambia según las etiquetas que se usan.

Puedes cambiar el énfasis de la entrega agregando etiquetas al comienzo de una línea para que el orador se muestre emocionado, aburrido o reacio:

- `[excitedly]` Hola, soy un nuevo modelo de texto a voz y puedo decir cosas de muchas maneras diferentes. ¿En qué puedo ayudarte?
- `[bored]` Hola, soy un nuevo modelo de texto a voz…
- `[reluctantly]` Hola, soy un nuevo modelo de texto a voz…

Las etiquetas también se pueden usar para cambiar el ritmo de la entrega o para combinar el ritmo con el énfasis:

- `[very fast]` Hola, soy un nuevo modelo de texto a voz…
- `[very slow]` Hola, soy un nuevo modelo de texto a voz…
- `[sarcastically, one painfully slow word at a time]` Hola, soy un nuevo modelo de texto a voz…

También tienes un control preciso sobre secciones específicas, lo que significa que puedes susurrar una parte y gritar otra.

- `[whispers]` Hola, soy un nuevo modelo de texto a voz `[shouting]` y puedo decir cosas de muchas maneras diferentes. `[whispers]` ¿En qué puedo ayudarte?

También puedes experimentar con cualquier idea creativa que desees:

- `[like a cartoon dog]` Hola, soy un nuevo modelo de texto a voz…
- `[like dracula]` Hola, soy un nuevo modelo de texto a voz…

Las etiquetas de uso frecuente incluyen las siguientes:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

Las etiquetas te permiten controlar de forma rápida y sencilla la entrega de tu transcripción. Para tener aún más control, puedes combinarlas con una instrucción de contexto para establecer el tono y el ambiente generales de la interpretación.

### Instrucciones avanzadas

Puedes considerar una instrucción avanzada como una instrucción del sistema que el modelo debe seguir. Es una forma de brindarle más contexto al modelo y controlar su rendimiento.

Una instrucción sólida idealmente incluye los siguientes elementos que se combinan para crear un gran rendimiento:

- **Perfil de audio**: Establece un arquetipo para la voz, define una identidad de personaje, un arquetipo y cualquier otra característica, como la edad, el origen, etcétera.
- **Escena**: Establece el contexto. Describe tanto el entorno físico como el "ambiente".
- **Notas del director**: Orientación sobre el rendimiento en la que puedes desglosar qué instrucciones son importantes para que tu talento virtual las tenga en cuenta. Algunos ejemplos son el estilo, la respiración, el ritmo, la articulación y el acento.
- **Contexto de ejemplo**: Le proporciona al modelo un punto de partida contextual, de modo que tu actor virtual ingrese a la escena que configuraste de forma natural.
- **Transcripción**: Es el texto que pronunciará el modelo. Para obtener el mejor rendimiento, recuerda que el tema y el estilo de escritura de la transcripción deben correlacionarse con las instrucciones que das.
- **Etiquetas de audio**: Son modificadores que puedes agregar a una transcripción para cambiar la forma en que se entrega esa parte del texto, como `[whispers]` o `[shouting]`.

Ejemplo de instrucción completa:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

### DIRECTOR'S NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
* Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions — no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
[excitedly] Yes, massive vibes in the studio! You are locked in and it is
absolutely popping off in London right now. If you're stuck on the tube, or
just sat there pretending to work... stop it. Seriously, I see you.
[shouting] Turn this up! We've got the project roadmap landing in three,
two... let's go!
```

### Estrategias de instrucciones detalladas

Desglosemos cada elemento de la instrucción.

#### Perfil de audio

Describe brevemente el arquetipo del personaje.

- **Nombre.** Ponerle un nombre a tu personaje ayuda a fundamentar el modelo y a unir la interpretación. Refiérete al personaje por su nombre cuando definas la escena y el contexto.
- **Rol:** Identidad y arquetipo principales del personaje que se desarrolla en la escena, p. ej., DJ de radio, podcaster, reportero de noticias, etc.

Ejemplos:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### Scene

Establece el contexto de la escena, incluida la ubicación, el ambiente y los detalles ambientales que establecen el tono y la atmósfera. Describe lo que sucede alrededor del personaje y cómo lo afecta. La escena proporciona el contexto ambiental para toda la interacción y guía la actuación de una manera sutil y orgánica.

Ejemplos:

```
## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
```

```
## THE SCENE: Homegrown Studio
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
```

#### Notas de los directores

Esta sección fundamental incluye orientación específica sobre el rendimiento. Puedes omitir todos los demás elementos, pero te recomendamos que incluyas este.

Define solo lo que es importante para el rendimiento y ten cuidado de no especificar demasiado. Demasiadas reglas estrictas limitarán la creatividad de los modelos y pueden generar un rendimiento peor. Equilibra la descripción del rol y la escena con las reglas de interpretación específicas.

Las instrucciones más comunes son **Estilo, ritmo y acento**, pero el modelo no se limita a ellas ni las requiere. No dudes en incluir instrucciones personalizadas para abarcar cualquier detalle adicional importante para tu rendimiento y proporciona tantos o tan pocos detalles como sea necesario.

Por ejemplo:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**Estilo:**

Establece el tono y el estilo del discurso generado. Incluye elementos como alegre, enérgico, relajado, aburrido, etcétera, para guiar la interpretación. Sé descriptivo y proporciona todos los detalles necesarios: *"Entusiasmo contagioso. *La frase "El público debe sentir que forma parte de un evento comunitario masivo y emocionante"* funciona mejor que decir simplemente "enérgico y entusiasta".*

Incluso puedes probar con términos populares en la industria de la voz en off, como "sonrisa vocal". Puedes combinar tantas características de estilo como desees.

Ejemplos:

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

Más profundidad

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

Complejo

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**Acento:**

Describe el acento deseado. Cuanto más específica sea la instrucción, mejores serán los resultados. Por ejemplo, usa "*Acento británico como el que se escucha en Croydon, Inglaterra*" en lugar de "*Acento británico*".

Ejemplos:

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a DJ from Brixton, London
...
```

**Ritmo:**

Ritmo general y variación del ritmo a lo largo de la pieza.

Ejemplos:

Simple

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

Más profundidad

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

Complejo

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

#### Etiquetas de transcripción y audio

La transcripción son las palabras exactas que dirá el modelo. Una etiqueta de audio es una palabra entre corchetes que indica cómo se debe decir algo, un cambio de tono o una interjección.

```
### TRANSCRIPT

I know right, [sarcastically] I couldn't believe it. [whispers] She should have totally left
at that point.

[cough] Well, [sighs] I guess it doesn't matter now.
```

**Pruébelo**

Prueba algunos de estos ejemplos en [AI Studio](https://aistudio.google.com/generate-speech?hl=es-419), experimenta con nuestra [app de TTS](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=es-419) y deja que Gemini te ponga en el lugar del director. Ten en cuenta estas sugerencias para lograr interpretaciones vocales excelentes:

- Recuerda que toda la instrucción debe ser coherente: el guion y la dirección van de la mano para crear una gran actuación.
- No sientas que debes describir todo. A veces, darle espacio al modelo para que complete los vacíos ayuda a que el texto sea más natural. (como un actor talentoso)
- Si alguna vez te sientes bloqueado, pídele ayuda a Gemini para crear tu guion o presentación.

## Limitaciones

- Los modelos de TTS solo pueden recibir entradas de texto y generar salidas de audio.
- Una sesión de TTS tiene un límite de [ventana de contexto](https://ai.google.dev/gemini-api/docs/long-context?hl=es-419) de 32,000 tokens.
- Revisa la sección [Idiomas](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419#languages) para conocer los idiomas admitidos.
- La TTS no admite la transmisión.

Las siguientes restricciones se aplican específicamente cuando se usa el modelo de Gemini 3.1 Flash TTS Preview para la generación de voz:

- **Inconsistencia de voz con las instrucciones de la instrucción:** Es posible que la salida del modelo no siempre coincida estrictamente con el orador seleccionado, lo que hace que el audio suene diferente de lo esperado. Para evitar tonos que no coincidan (como una voz masculina profunda que intenta hablar como una niña), asegúrate de que el tono y el contexto escritos de tu instrucción se alineen de forma natural con el perfil del orador seleccionado.
- **Calidad de los resultados más largos:** La calidad y la coherencia del discurso pueden comenzar a disminuir con los resultados generados que duran más de unos minutos. Te recomendamos que dividas tus transcripciones en fragmentos más pequeños.
- **Devoluciones ocasionales de tokens de texto:** En ocasiones, el modelo devuelve tokens de texto en lugar de tokens de audio, lo que provoca que el servidor rechace la solicitud con un error `500`. Dado que esto ocurre de forma aleatoria en un porcentaje muy pequeño de solicitudes, debes implementar una lógica de reintento automatizada en tu aplicación para controlarlas.
- **Rechazos falsos del clasificador de instrucciones:** Las instrucciones vagas pueden no activar el clasificador de síntesis de voz, lo que genera una solicitud rechazada (`PROHIBITED_CONTENT`) o hace que el modelo lea en voz alta las instrucciones de estilo y las notas del director. Valida tus instrucciones agregando un preámbulo claro que le indique al modelo que sintetice el habla y etiquetando de forma explícita dónde comienza la transcripción hablada real.

## ¿Qué sigue?

- Prueba el [recetario de generación de audio](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb?hl=es-419).
- La [API de Live](https://ai.google.dev/gemini-api/docs/live?hl=es-419) de Gemini ofrece opciones interactivas de generación de audio que puedes intercalar con otras modalidades.
- Para trabajar con *entradas* de audio, consulta la guía de [Comprensión de audio](https://ai.google.dev/gemini-api/docs/audio?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-04-29 (UTC)"],[],[]]
