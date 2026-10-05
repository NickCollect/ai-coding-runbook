---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=de
fetched_at: 2026-10-05T06:38:16.053495+00:00
title: "Sprachausgabe \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Sprachausgabe

Mit der Gemini API kann Texteingabe mithilfe der Gemini-Text-zu-Sprache-Funktionen (TTS) in Audioinhalte mit einem oder mehreren Sprechern umgewandelt werden.
Die Sprachsynthese ist *[steuerbar](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de#controllable)*. Das bedeutet, dass Sie strukturierte Metadaten für die einzelnen Äußerungen (`speech_metadata`) und Inline-Sprachtags kombinieren können, um *Stil*, *Akzent*, *Tempo* und *Ton* des Audios zu steuern.

Die TTS-Funktion unterscheidet sich von der Sprachgenerierung über die [Live API](https://ai.google.dev/gemini-api/docs/live?hl=de), die für interaktive, unstrukturierte Audio- sowie multimodale Ein- und Ausgaben konzipiert ist. Während die Live API sich hervorragend für dynamische Konversationskontexte eignet, ist TTS über die Gemini API auf Szenarien zugeschnitten, in denen eine genaue Textrezitation mit detaillierter Steuerung von Stil und Klang erforderlich ist, z. B. bei der Generierung von Podcasts oder Hörbüchern.

In dieser Anleitung erfahren Sie, wie Sie mit [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=de) (`gemini-3.8-flash-tts`) und [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=de) (`gemini-3.8-flash-lite-tts`) Audio für einen einzelnen Sprecher und für mehrere Sprecher aus Text generieren.

## Hinweis

Achten Sie darauf, dass Sie ein Gemini-TTS-Modell verwenden, das im Abschnitt [Unterstützte Modelle](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de#supported-models) aufgeführt ist, und aktualisieren Sie auf das neueste Google GenAI SDK (`google-genai >= 2.25.0` für Python oder `@google/genai >= 2.24.0` für JavaScript/TypeScript) oder verwenden Sie die REST API.
Die besten Ergebnisse erzielen Sie, wenn Sie [Wann welches Modell verwendet werden sollte](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de#when-to-use-which-model) lesen, um das beste Modell für Ihre Arbeitslast auszuwählen.

Es kann hilfreich sein, die [Gemini TTS-Modelle in AI Studio zu testen](https://aistudio.google.com/generate-speech?hl=de), bevor Sie mit der Entwicklung beginnen.

## TTS für einen einzelnen Sprecher

Wenn Sie mit Gemini 3.8 TTS-Modellen Text in Audioinhalte mit einem einzelnen Sprecher umwandeln möchten, übergeben Sie das wörtliche Transkript in `input`, fügen Sie mit der Annotation `speech_metadata` Formatierungen auf Turn-Ebene hinzu und konfigurieren Sie die Stimme in `generation_config.speech_config`. Sie können eine Stimme aus den vordefinierten
[Sprachoptionen](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de#voices), der Extended Voice
Library (`GET /v1beta/voices`), einer benutzerdefinierten
[Voice Design](https://ai.google.dev/gemini-api/docs/voice-design?hl=de)-ID (`voice_...`) oder einer
[Voice Replication](https://ai.google.dev/gemini-api/docs/voice-replication?hl=de)-ID (`voice_...` oder
optional zustandslos `voicekey_...`) auswählen.

In diesem Beispiel wird die standardmäßige WAV-Audioausgabe (`audio/wav`) des Modells direkt in einer Datei gespeichert:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### Ok

```
package main

import (
    "context"
    "encoding/base64"
    "encoding/binary"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func saveWaveFile(filename string, pcmData []byte) error {
    f, err := os.Create(filename)
    if err != nil {
        return err
    }
    defer f.Close()

    sampleRate := uint32(24000)
    numChannels := uint16(1)
    bitsPerSample := uint16(16)
    byteRate := sampleRate * uint32(numChannels) * uint32(bitsPerSample/8)
    blockAlign := numChannels * (bitsPerSample / 8)
    dataSize := uint32(len(pcmData))

    f.WriteString("RIFF")
    binary.Write(f, binary.LittleEndian, uint32(36+dataSize))
    f.WriteString("WAVEfmt ")
    binary.Write(f, binary.LittleEndian, uint32(16))
    binary.Write(f, binary.LittleEndian, uint16(1))
    binary.Write(f, binary.LittleEndian, numChannels)
    binary.Write(f, binary.LittleEndian, sampleRate)
    binary.Write(f, binary.LittleEndian, byteRate)
    binary.Write(f, binary.LittleEndian, blockAlign)
    binary.Write(f, binary.LittleEndian, bitsPerSample)
    f.WriteString("data")
    binary.Write(f, binary.LittleEndian, dataSize)
    _, err = f.Write(pcmData)
    return err
}

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Voice: genai.Ptr("Kore")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput("Say cheerfully: Have a wonderful day!"),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        pcmBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := saveWaveFile("out.wav", pcmBytes); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

In den Python- und JavaScript-SDKs können Sie generierte Audiodaten mit der Convenience-Property `interaction.output_audio` abrufen. Diese gibt den zuletzt generierten Audioblock zurück. In REST-JSON-Rohantworten wird das base64-codierte Audio in `steps[].content[].data` gespeichert. Weitere Informationen zu Convenience-Properties finden Sie in der [Übersicht zu Interaktionen](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de#convenience-properties).

## TTS mit mehreren Sprechern

Bei Dialogen mit mehreren Sprechern konfigurieren Sie zwei Sprecher in `speech_config.speakers` und übergeben jeden Sprecherbeitrag als separates Textelement mit einer `speech_metadata`-Anmerkung, in der `speaker` und optional `style` auf Beitragsebene angegeben werden. Beachten Sie, dass `speech_config` ein Array (`[{"voice": "..."}]`) für die Generierung mit einem einzelnen Sprecher und ein Objekt (`{"speakers": [...]}`) für die Generierung mit mehreren Sprechern akzeptiert:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [
            {
                "type": "text",
                "text": "How's it going today Jane?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                }],
            },
            {
                "type": "text",
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                }],
            },
        ],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": {
            "speakers": [
                {"speaker": "Joe", "voice": "Puck"},
                {"speaker": "Jane", "voice": "Kore"},
            ],
        }
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [
            {
               type: 'text',
               text: "How's it going today Jane?",
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               }],
            },
            {
               type: 'text',
               text: 'Not too bad, how about you? Ready to test these new voices?',
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               }],
            },
         ],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: {
            speakers: [
               { speaker: 'Joe', voice: 'Puck' },
               { speaker: 'Jane', voice: 'Kore' },
            ],
         },
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### Ok

```
package main

import (
    "context"
    "encoding/base64"
    "encoding/binary"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func saveWaveFile(filename string, pcmData []byte) error {
    f, err := os.Create(filename)
    if err != nil {
        return err
    }
    defer f.Close()

    sampleRate := uint32(24000)
    numChannels := uint16(1)
    bitsPerSample := uint16(16)
    byteRate := sampleRate * uint32(numChannels) * uint32(bitsPerSample/8)
    blockAlign := numChannels * (bitsPerSample / 8)
    dataSize := uint32(len(pcmData))

    f.WriteString("RIFF")
    binary.Write(f, binary.LittleEndian, uint32(36+dataSize))
    f.WriteString("WAVEfmt ")
    binary.Write(f, binary.LittleEndian, uint32(16))
    binary.Write(f, binary.LittleEndian, uint16(1))
    binary.Write(f, binary.LittleEndian, numChannels)
    binary.Write(f, binary.LittleEndian, sampleRate)
    binary.Write(f, binary.LittleEndian, byteRate)
    binary.Write(f, binary.LittleEndian, blockAlign)
    binary.Write(f, binary.LittleEndian, bitsPerSample)
    f.WriteString("data")
    binary.Write(f, binary.LittleEndian, dataSize)
    _, err = f.Write(pcmData)
    return err
}

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := "TTS the following conversation between Joe and Jane:\n" +
        "Joe: How's it going today Jane?\n" +
        "Jane: Not too bad, how about you?"

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Speaker: genai.Ptr("Joe"), Voice: genai.Ptr("Kore")},
            {Speaker: genai.Ptr("Jane"), Voice: genai.Ptr("Puck")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput(prompt),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        pcmBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := saveWaveFile("out.wav", pcmBytes); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [
        {
          "type": "text",
          "text": "How'\''s it going today Jane?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }]
        },
        {
          "type": "text",
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Jane",
            "style": "calm and relaxed"
          }]
        }
      ]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": {
        "mode": "conversational",
        "speakers": [
          { "speaker": "Joe", "voice": "Puck" },
          { "speaker": "Jane", "voice": "Kore" }
        ]
      }
    }
  }'
```

## Sprachstil mit Metadaten und Tags steuern

Bei Gemini 3.8 TTS wird das Feld `text` ausschließlich als wörtliches Transkript behandelt. Wenn Sie die Ausführung steuern möchten, ohne dass Regieanweisungen vorgelesen werden, teilen Sie Ihre Anweisungen nach Umfang auf:

- **Kontinuierliche Bereitstellung auf Turn-Ebene (`speech_metadata.style`)**: Geben Sie Emotionen, Vortragsstil, Prosodie, Tempo und Lautstärke, die für einen gesamten Turn gelten, im Feld `style` an (z. B. `"style": "whispered urgently"`, `"style": "out of breath"` oder `"style": "warm and enthusiastic"`).
- **Zeitpunktbezogene Ereignisse (Inline-Tags)**: Platzieren Sie kurze nicht sprachliche Vokalbursts oder Pausen direkt im Transkript mithilfe von spitzen Klammern (z. B. `"Wait... <short pause> did you hear that? <sigh>"` oder `"Excuse me <cough> as I was saying..."`).

Umfassende Best Practices finden Sie im [Leitfaden für Prompts](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de#prompting-guide).

### Ok

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    transcriptRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(
                "Generate a short transcript around 100 words that reads " +
                    "like it was clipped from a podcast by excited herpetologists. " +
                    "The hosts names are Dr. Anya and Liam.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    var transcript string
    if transcriptRes.Interaction.OutputText != nil {
        transcript = *transcriptRes.Interaction.OutputText
    }

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Speaker: genai.Ptr("Dr. Anya"), Voice: genai.Ptr("Kore")},
            {Speaker: genai.Ptr("Liam"), Voice: genai.Ptr("Puck")},
        })),
    }

    ttsRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput(transcript),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = ttsRes
}
```

## Streaming-Sprachgenerierung

Sie können die generierte Audioausgabe streamen, während sie synthetisiert wird, indem Sie `stream: true` festlegen. Im Gegensatz zu unären Anfragen, bei denen eine vollständige WAV-Datei mit einem RIFF-Header zurückgegeben wird, **werden bei Streaminganfragen standardmäßig Header-lose Roh-Chunks im linearen PCM-Format (`audio/l16`, 24 kHz, Mono) mit 16 Bit und Little-Endian-Vorzeichen zurückgegeben**. Audiotracks können also ohne Containerheader kontinuierlich abgespielt oder verkettet werden.

### Python

```
import base64
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "audio":
            audio_data = base64.b64decode(event.delta.data)
            # Process the audio chunk (e.g. play it or write to a file)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const stream = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
      stream: true,
   });

   for await (const event of stream) {
      if (event.event_type === 'step.delta') {
         if (event.delta.type === 'audio') {
            const audioBuffer = Buffer.from(event.delta.data, 'base64');
            // Process the audio buffer
         }
      }
   }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    },
    "stream": true
  }'
```

## Audioausgabeformate

Gemini 3.8-TTS-Modelle verwenden je nach Art der Anfrage (unär oder Streaming) unterschiedliche Standardaudioformate:

- **Unäre Anfragen (`stream=False`)**: Gib vollständiges **WAV-Audio (`audio/wav`)** mit einem Standard-RIFF-Header (24 kHz, Mono, 16-Bit-PCM mit Vorzeichen und Little-Endian) zurück. Sie können die decodierten Audio-Bytes direkt in einer `.wav`-Datei speichern, ohne manuell einen WAV-Header voranzustellen.
- **Streaminganfragen (`stream=True`)**: Standardmäßig werden **headerlose Rohdaten-Chunks im linearen PCM-Format (`audio/l16`)** (24 kHz, Mono, 16-Bit-PCM mit Vorzeichen und Little-Endian-Byte-Reihenfolge) zurückgegeben, damit die Chunks kontinuierlich gestreamt oder verkettet werden können, ohne dass jeder Chunk Container-Header enthält.

Wenn Sie eine andere Audio-Codierung oder Abtastrate anfordern möchten, konfigurieren Sie `mime_type` und optional `sample_rate` in `response_format`:

| Format | `mime_type` Wert | Beschreibung |
| --- | --- | --- |
| **WAV** *(unärer Standard)* | `"audio/wav"` | Unkomprimierte WAV-Datei mit einem RIFF-Header (16-Bit-PCM mit Vorzeichen, Little Endian, Mono, 24 kHz als Standard). Standardeinstellung für unäre Anfragen. |
| **Raw PCM (L16)** *(Streaming-Standard)* | `"audio/l16"` | Unkomprimiertes, headerloses lineares 16-Bit-PCM-Audio mit Vorzeichen und Little Endian (24 kHz, Mono). Standard für Streaminganfragen. |
| **Mu-law** | `"audio/mulaw"` | 8-Bit-Audio mit G.711-Mu-Law-Codierung (wird häufig in nordamerikanischen und japanischen Telefonie-/IVR-Systemen verwendet). |
| **A-law** | `"audio/alaw"` | 8-Bit-Audio mit G.711-A-Law-Codierung (wird häufig in europäischen und internationalen Telefoniesystemen verwendet). |

Sie können auch `sample_rate` in Hertz angeben, z. B. `24000`, `16000` oder `8000`.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={
        "type": "audio",
        "mime_type": "audio/l16",  # "audio/wav" (default), "audio/l16", "audio/mulaw", or "audio/alaw"
        "sample_rate": 24000,
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.pcm", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: {
         type: 'audio',
         mime_type: 'audio/l16', // 'audio/wav' (default), 'audio/l16', 'audio/mulaw', or 'audio/alaw'
         sample_rate: 24000,
      },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.pcm', audioBuffer);
}
await main();
```

### Ok

```
package main

import (
    "context"
    "encoding/base64"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Voice: genai.Ptr("Kore")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash-tts"),
            Input: interactions.NewInteractionsInput("Say cheerfully: Have a wonderful day!"),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
            Stream:           genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if audioDelta := stepDelta.GetDeltaAudio(); audioDelta != nil && audioDelta.Data != nil {
                audioData, err := base64.StdEncoding.DecodeString(*audioDelta.Data)
                if err != nil {
                    log.Fatal(err)
                }
                // Process the audio chunk (e.g. play it or write to a file)
                _ = audioData
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio",
      "mime_type": "audio/l16",
      "sample_rate": 24000
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

## Stimmoptionen

Gemini 3.8 TTS unterstützt vier Möglichkeiten zum Auswählen oder Erstellen von Stimmen:

1. **Vorgefertigte Studio-Stimmen**:30 ausgewählte Stimmen, die in der folgenden Tabelle aufgeführt sind.
2. **Erweiterte Stimmenbibliothek**:Hunderte zusätzlicher Stimmen in verschiedenen Sprachen, Akzenten und Charakterarchetypen, die über `client.voices.list()` (`GET /v1beta/voices`) verfügbar sind.
3. **[Stimmdesign](https://ai.google.dev/gemini-api/docs/voice-design?hl=de)**:Generieren Sie eine benutzerdefinierte stimmliche Persona aus einer natürlichsprachlichen Beschreibung in [Google AI Studio](https://aistudio.google.com/generate-speech?hl=de) oder mit `POST /v1beta/voices` (`type="prompted"`, die eine dauerhafte `voice_...`-ID und eine `sample_audio`-WAV-Vorschau in `CreateVoice` und `GetVoice` zurückgibt).
4. **[Stimmreplikation](https://ai.google.dev/gemini-api/docs/voice-replication?hl=de)**:Die Stimme eines Sprechers kann anhand von Referenz- und Einwilligungs-Audioinhalten in [Google AI Studio](https://aistudio.google.com/generate-speech?hl=de) oder mit `POST /v1beta/voices` (`type="replicated"`, standardmäßig persistent `store=True` oder optional zustandslos `store=False`) repliziert werden.

### Benutzerdefinierte Sprachlimits und TTL

| Stimmtyp | Speichermodus | Kontingent / Limit | Aufbewahrung (TTL) |
| --- | --- | --- | --- |
| **Zustandsorientierte Stimmen** (`voice_...`, per Prompt oder repliziert) | `store=True` | **200 Stimmen pro Projekt** (aufgefordert und repliziert) | **1 Jahr nach der letzten Nutzung\*** |
| **Zustandslose Sprachschlüssel** (`voicekey_...`, repliziert) | `store=False` | Kundenverwaltet | **7 Tage** |

\* **Verlängerung der TTL**:Der Aufbewahrungszeitraum von einem Jahr wird jedes Mal zurückgesetzt, wenn die Stimme aktiv verwendet wird (entweder durch Synthetisieren von Sprache mit der Stimme oder durch Verwendung als Basisstimme für das Remixen). Stimmen, die seit einem Jahr nicht mehr verwendet wurden, werden automatisch gelöscht.

### Vordefinierte Stimmen

|  |  |  |
| --- | --- | --- |
| **Zephyr** – *Hell* | **Puck** – *Upbeat* | **Charon** – *Informative* |
| **Kore** – *Fest* | **Fenrir** – *Leicht erregbar* | **Leda** – *Jugendlich* |
| **Orus** – *Firm* | **Aoede** – *Breezy* | **Callirrhoe** – *Gelassen* |
| **Autonoe** – *Hell* | **Enceladus** – *Breathy* | **Iapetus** – *Löschen* |
| **Umbriel** – *Entspannt* | **Algieba** – *Smooth* | **Despina** – *Smooth* |
| **Erinome** – *Löschen* | **Algenib** – *Kiesig* | **Rasalgethi** – *Informativ* |
| **Laomedeia** – *Upbeat* | **Achernar** – *Weich* | **Alnilam** – *Firm* |
| **Schedar** – *Gerade* | **Gacrux** – *Nicht jugendfrei* | **Pulcherrima** – *Vorwärts* |
| **Achird** – *Freundlich* | **Zubenelgenubi** – *Informell* | **Vindemiatrix** – *Sanft* |
| **Sadachbia** – *Lively* | **Sadaltager** – *Sachkundig* | **Sulafat** – *Warm* |

### Erweiterte Voice Library und Filterung

Neben den 30 Studio-Stimmen in der Tabelle oben bietet die **erweiterte Stimmenbibliothek** Hunderte von zusätzlichen Stimmen in verschiedenen Sprachen, regionalen Akzenten, Charakteren und Bereichen. Sie können die gesamte Voice Library interaktiv in [Google AI Studio](https://aistudio.google.com/generate-speech?hl=de) durchsuchen, filtern und testen oder sie programmatisch mit `client.voices.list()` abfragen (`GET /v1beta/voices`, mit `google-genai` 2.25.0+ / `@google/genai` 2.24.0+).

`ListVoices` gibt Ihre benutzerdefinierten gespeicherten Stimmen (neueste zuerst) und dann die vorgefertigten Katalogstimmen zurück, die Ihren Filterkriterien entsprechen. Wenn mehrere Werte für einen Listenfilter übergeben werden, werden Stimmen zurückgegeben, die **einem beliebigen** Wert in diesem Filter entsprechen (`OR`). Unterschiedliche Filterparameter werden mit `AND` kombiniert:

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| `language_code` | `list[str]` | BCP-47-Sprachtag(s) (z. B. `["en-US", "en-GB"]`). Es wird nicht zwischen Groß- und Kleinschreibung unterschieden. |
| `region_code` | `list[str]` | ISO 3166-1 Alpha-2- oder UN M.49-Regionscode(s) (z. B. `["US", "GB"]`). |
| `accent` | `list[str]` | Deskriptoren für regionale Akzente (z. B. `["American", "British"]`). |
| `gender` | `list[str]` | Wahrgenommene Geschlechtsdarstellung (`"female"`, `"male"` oder `"neutral"`) |
| `pitch` | `list[str]` | Klassifizierung der Tonhöhe (`"low"`, `"medium"` oder `"high"`) |
| `persona` | `list[str]` | Gesangspersönlichkeit oder Charakterarchetyp (z. B. `["Warm, Friendly"]`, `["Narrator"]`). |
| `contexts` (`context` in REST) | `list[str]` | Optimale Nutzungsdomain (z. B. `["Audiobook", "Conversational", "News"]`). |
| `type` (`type_` in Python) | `list[str]` | Nach Sprachquelle filtern: `"prebuilt"`, `"prompted"` ([Voice Design](https://ai.google.dev/gemini-api/docs/voice-design?hl=de)) oder `"replicated"` ([Voice Replication](https://ai.google.dev/gemini-api/docs/voice-replication?hl=de)). |
| `search` | `str` | Bei der Freitext-Teilstringsuche wurde die Groß-/Kleinschreibung sowohl bei `display_name` als auch bei `description` nicht berücksichtigt. |
| `page_size` | `int` | Maximale Anzahl der Stimmen, die pro Seite zurückgegeben werden (Standardwert: `50`, Maximum: `1000`). |
| `page_token` | `str` | Token aus `response.next_page_token` zum Abrufen der nächsten Ergebnisseite. |

### Python

```
from google import genai

client = genai.Client()

# Filter the Voice Library by language, gender, pitch, domain context, and keyword
response = client.voices.list(
    language_code=["en-US", "en-GB"],
    gender=["female"],
    pitch=["medium", "low"],
    contexts=["Audiobook", "Conversational"],
    type_=["prebuilt"],
    search="warm",
    page_size=50,
)

for voice in response.voices or []:
    print(
        f"{voice.id} | {voice.display_name} ({voice.language_code},"
        f" {voice.accent}, {voice.gender}, pitch={voice.pitch}):"
        f" {voice.description}"
    )
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// Filter the Voice Library by language, gender, pitch, domain context, and keyword
const response = await ai.voices.list({
  language_code: ["en-US", "en-GB"],
  gender: ["female"],
  pitch: ["medium", "low"],
  contexts: ["Audiobook", "Conversational"],
  type: ["prebuilt"],
  search: "warm",
  page_size: 50,
});

for (const voice of response.voices ?? []) {
  console.log(
    `${voice.id} | ${voice.display_name} (${voice.language_code}, ${voice.accent}, ${voice.gender}, pitch=${voice.pitch}): ${voice.description}`
  );
}
```

### REST

```
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB" \
  --data-urlencode "gender=female" \
  --data-urlencode "pitch=medium" \
  --data-urlencode "context=Audiobook" \
  --data-urlencode "type=prebuilt" \
  --data-urlencode "search=warm" \
  --data-urlencode "page_size=50"
```

## Unterstützte Sprachen

Die TTS-Modelle erkennen die Eingabesprache automatisch.
[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=de) (`gemini-3.8-flash-tts`) unterstützt **über 130 Sprachen** und [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=de) (`gemini-3.8-flash-lite-tts`) unterstützt **über 100 Sprachen**:

| Sprache | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| Achinesisch (arabische Schrift) | ✔️ | ✔️ |
| Afrikaans | ✔️ | ✔️ |
| Akan | ✔️ | ✔️ |
| Amharisch | ✔️ | ✔️ |
| Armenisch | ✔️ | ✔️ |
| Assamesisch | ✔️ | ✔️ |
| Awadhi | ✔️ | ✔️ |
| Balinesisch | ✔️ | ✔️ |
| Bengalisch | ✔️ | ✔️ |
| Banjaresisch (arabische Schrift) | ✔️ | – |
| Banjaresisch (lateinische Schrift) | ✔️ | ✔️ |
| Baschkirisch | ✔️ | – |
| Baskisch | ✔️ | ✔️ |
| Belarusian | ✔️ | ✔️ |
| Bemba | ✔️ | – |
| Bhojpuri | ✔️ | ✔️ |
| Bosnisch | ✔️ | ✔️ |
| Buginesisch | ✔️ | ✔️ |
| Bulgarisch | ✔️ | ✔️ |
| Burmesisch | ✔️ | – |
| Kantonesisch | ✔️ | ✔️ |
| Katalanisch | ✔️ | ✔️ |
| Cebuano | ✔️ | ✔️ |
| Sorani | ✔️ | ✔️ |
| Chhattisgarhi | ✔️ | ✔️ |
| Chinesisch (Hans-Schrift) | ✔️ | ✔️ |
| Chinesisch (Hant-Schrift) | ✔️ | ✔️ |
| Krimtatarisch | ✔️ | – |
| Kroatisch | ✔️ | ✔️ |
| Tschechien | ✔️ | ✔️ |
| Dänisch | ✔️ | ✔️ |
| Niederländisch | ✔️ | ✔️ |
| Dioula | ✔️ | – |
| Dzongkha | ✔️ | – |
| Arabisch (Ägypten) | ✔️ | ✔️ |
| Englisch | ✔️ | ✔️ |
| Estnisch | ✔️ | ✔️ |
| Filipino | ✔️ | ✔️ |
| Finnisch | ✔️ | – |
| Französisch | ✔️ | ✔️ |
| Galizisch | ✔️ | ✔️ |
| Ganda | ✔️ | ✔️ |
| Georgisch | ✔️ | ✔️ |
| Deutsch | ✔️ | ✔️ |
| Griechisch | ✔️ | ✔️ |
| Guarani | ✔️ | – |
| Gujarati | ✔️ | ✔️ |
| Haitianisch | ✔️ | ✔️ |
| Halch-Mongolisch | ✔️ | ✔️ |
| Hausa | ✔️ | ✔️ |
| Hebräisch | ✔️ | ✔️ |
| Hindi | ✔️ | ✔️ |
| Ungarisch | ✔️ | ✔️ |
| Isländisch | ✔️ | ✔️ |
| Igbo | ✔️ | – |
| Ilokano | ✔️ | ✔️ |
| Indonesisch | ✔️ | ✔️ |
| Iranisches Persisch | ✔️ | ✔️ |
| Italienisch | ✔️ | ✔️ |
| Japanisch | ✔️ | ✔️ |
| Javanisch | ✔️ | ✔️ |
| Kabylisch | ✔️ | – |
| Kikamba | ✔️ | ✔️ |
| Kannada | ✔️ | ✔️ |
| Kashmiri (arabische Schrift) | ✔️ | ✔️ |
| Kashmiri (Deva-Schrift) | ✔️ | ✔️ |
| Kasachisch | ✔️ | ✔️ |
| Khmer | ✔️ | ✔️ |
| Kikuyu | ✔️ | ✔️ |
| Kinyarwanda | ✔️ | ✔️ |
| Kongo | ✔️ | ✔️ |
| Koreanisch | ✔️ | ✔️ |
| Kirgisisch | ✔️ | ✔️ |
| Lao | ✔️ | ✔️ |
| Lettgallisch | ✔️ | – |
| Lingala | ✔️ | ✔️ |
| Litauisch | ✔️ | – |
| Luxemburgisch | ✔️ | – |
| Mazedonisch | ✔️ | ✔️ |
| Magahi | ✔️ | ✔️ |
| Maithili | ✔️ | ✔️ |
| Malayalam | ✔️ | ✔️ |
| Maltesisch | ✔️ | ✔️ |
| Meitei | ✔️ | ✔️ |
| Marathi | ✔️ | ✔️ |
| Minangkabauisch (arabische Schrift) | ✔️ | ✔️ |
| Minangkabauisch (lateinische Schrift) | ✔️ | – |
| Mizo | ✔️ | ✔️ |
| Nepalesisch (einzelne Sprache) | ✔️ | ✔️ |
| Nigerianisches Fulfulde | ✔️ | ✔️ |
| Nordaserbaidschanisch | ✔️ | ✔️ |
| Nord-Sotho | ✔️ | ✔️ |
| Nordusbekisch | ✔️ | ✔️ |
| Norwegisch Bokmål | ✔️ | ✔️ |
| Norwegisch (Nynorsk) | ✔️ | ✔️ |
| Chichewa | ✔️ | ✔️ |
| Okzitanisch | ✔️ | – |
| Odia (einzelne Sprache) | ✔️ | ✔️ |
| Pangasinensisch | ✔️ | – |
| Persisch (Afghanistan) | ✔️ | ✔️ |
| Polish | ✔️ | ✔️ |
| Portugiesisch | ✔️ | ✔️ |
| Punjabi | ✔️ | ✔️ |
| Rumänisch | ✔️ | ✔️ |
| Russisch | ✔️ | ✔️ |
| Santali | ✔️ | ✔️ |
| Serbisch | ✔️ | ✔️ |
| Sindhi | ✔️ | – |
| Singhalesisch | ✔️ | ✔️ |
| Slowakisch | ✔️ | ✔️ |
| Slowenisch | ✔️ | – |
| Somali | ✔️ | – |
| Südaserbaidschanisch | ✔️ | ✔️ |
| Südliches Paschtu | ✔️ | ✔️ |
| Sesotho | ✔️ | – |
| Spanisch | ✔️ | ✔️ |
| Standardarabisch (arabische Schrift) | ✔️ | ✔️ |
| Standardarabisch (lateinische Schrift) | ✔️ | ✔️ |
| Standard-Lettisch | ✔️ | ✔️ |
| Standard-Malaiisch | ✔️ | ✔️ |
| Swahili (einzelne Sprache) | ✔️ | – |
| Siswati | ✔️ | – |
| Schwedisch | ✔️ | – |
| Tadschikisch | ✔️ | – |
| Tamil | ✔️ | ✔️ |
| Telugu | ✔️ | ✔️ |
| Thailändisch | ✔️ | – |
| Tigrinya | ✔️ | – |
| Toskisch | ✔️ | – |
| Turkish | ✔️ | ✔️ |
| Uigurisch | ✔️ | – |
| Vietnamesisch | ✔️ | ✔️ |

## Unterstützte Modelle

| Modell | Einzelner Sprecher | Mehrere Sprecher | Sprachdesign | Stimmen-Replikation |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=de) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=de) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash TTS (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=de) | ✔️ | ✔️ | – | – |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=de) | ✔️ | ✔️ | – | – |

### Wann welches Modell verwendet werden sollte

Beide Gemini 3.8-TTS-Modelle haben dasselbe API-Schema und Prompting-Format. Sie können also mit einer einzigen Parameteränderung zwischen ihnen wechseln:

- **Verwenden Sie [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=de) (`gemini-3.8-flash-tts`)**, wenn maximale akustische Wiedergabetreue, nuancierte Darstellung und ausdrucksstarke Steuerung oberste Priorität haben. Sie eignet sich ideal für kreative Arbeiten in Studioqualität, komplexe Dialoge mit mehreren Sprechern, Tags für starke Gesangspassagen, schwierige Aussprachen, regionale oder Minderheitendialekte und lange Erzählungen, die eine stabile Stimme und einen stabilen Raumton erfordern.
- **[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=de) (`gemini-3.8-flash-lite-tts`)** als schnelles, kostengünstiges Arbeitstier anstelle von `gemini-3.1-flash-tts-preview` verwenden. Sie ist für die Massenproduktion in großem Umfang, Konversations-Voice-Agent-Kaskaden, Vorlesefunktionen, zuverlässige Sprachreplikation und alltägliche Einzelsprecher-Sprache in wichtigen Sprachen optimiert.

### Migrationsanleitung

Wenn Sie von Gemini TTS-Modellen der Version `gemini-3.1-flash-tts-preview` oder früher zu Gemini 3.8 TTS migrieren:

1. **Anweisungen auf Turn-Ebene in `speech_metadata` verschieben**:Bei Gemini 3.8 TTS wird der eingegebene Text streng als wörtliches Transkript behandelt. Verschieben Sie Anweisungen zur kontinuierlichen Bereitstellung (`style`, z. B. `"whispering"`, `"out of breath"` oder `"speaking slowly"`) und Sprecherlabels (`speaker`) in strukturierte `speech_metadata`-Anmerkungen, anstatt Regieanweisungen in den Transkripttext einzubetten.
2. **Winkelklammer-Inlinetags nur für stimmliche Ereignisse zu einem bestimmten Zeitpunkt verwenden**:Momentane stimmliche Äußerungen und Pausen, die keine Sprache sind, mit Winkelklammern (z. B. `<laugh>`, `<sigh>`, `<cough>`, `<breath>` oder `<short pause>`) in das Transkript einfügen. Soundeffekt-Tags (z. B. für Applaus oder dumpfe Geräusche) vermeiden und Vortragsstile in `speech_metadata.style` setzen.
3. **`speaker` in jeder Äußerung in Anfragen mit mehreren Sprechern angeben**:Jede Äußerung in einer Anfrage mit mehreren Sprechern muss `speaker` innerhalb von `speech_metadata` enthalten, das mit einem der konfigurierten Sprecher übereinstimmt.
4. **Design-Personas im Voraus mit Voice Design erstellen**:Ersetzen Sie `"Audio Profile"`- oder `"Director's Notes"`-Blöcke mit mehreren Absätzen durch eine benutzerdefinierte Stimme, die in [Voice Design](https://ai.google.dev/gemini-api/docs/voice-design?hl=de) erstellt wurde. Übertragen Sie dann die `voice_...`-ID in Ihre TTS-Anfragen mit minimalen oder leeren `style`-Strings.
5. **Standard-WAV-Ausgabe (`audio/wav`) bei unären Anfragen berücksichtigen**:Im Gegensatz zu `gemini-3.1-flash-tts-preview` und früheren TTS-Modellen (die standardmäßig headerloses rohes PCM `audio/l16` zurückgegeben haben) gibt Gemini 3.8 TTS standardmäßig WAV-Audio (`audio/wav`) mit einem Standard-RIFF-Header für unäre Anfragen zurück.
   - Wenn Ihr Code zuvor Roh-PCM-Bytes in einen WAV-Header eingeschlossen hat (z. B. mit dem `wave`-Modul oder `ffmpeg` von Python), entfernen Sie den manuellen Header-Wrapper und schreiben Sie die zurückgegebenen Bytes direkt in eine `.wav`-Datei.
   - Wenn für Ihre Pipeline unkomprimiertes PCM-Audio ohne Header, Mu-Law- oder A-Law-Audio erforderlich ist, legen Sie `response_format.mime_type` explizit auf `"audio/l16"`, `"audio/mulaw"` oder `"audio/alaw"` fest (z. B. `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}` in der Interactions API oder `AUDIO_L16` in `generateContent`). Weitere Informationen finden Sie unter [Audioausgabeformate](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de#audio-output-formats).

## Leitfaden für Prompts

Gemini 3.8 TTS-Modelle behandeln Eingabetext ausschließlich als **wortwörtliches Transkript**.
Im Gegensatz zu früheren Vorschauversionen, in denen Regieanweisungen in Nur-Text eingebettet waren, trennt Gemini 3.8 TTS anhaltende Anweisungen auf Turn-Ebene (`speech_metadata`) von Inline-Vocal-Tags für bestimmte Zeitpunkte.

### Stilfeld im Vergleich zu Inline-Tags

Teilen Sie Ihre Leistungsanweisungen nach Umfang auf:

- **Lieferung auf Turn-Ebene (`speech_metadata.style`)**: Attribute für die kontinuierliche Bereitstellung, z. B. Emotion, Prosodie, allgemeines Tempo oder Bereitstellungsstil (z. B. `"whispering"`, `"out of breath"`, `"muttering"` oder `"sarcastic"`), werden in das Feld `style` von `speech_metadata` eingefügt. Damit die Figur und die Leistung über die verschiedenen Züge hinweg stabil bleiben, sollten Sie die Persona im Voraus im [Voice Design](https://ai.google.dev/gemini-api/docs/voice-design?hl=de) entwerfen und `style` nur für optionale Anpassungen auf Zugebene verwenden.
- **Zeitpunktbezogene Ereignisse (Inline-Tags)**: Setzen Sie kurze nicht sprachliche Vokalbursts, Atemzüge oder Pausen mit spitzen Klammern (`<cough>`, `<breath>`, `<sigh>`, `<short pause>`) in den Transkripttext ein. Verwenden Sie spitze Klammern (`<...>`) für die höchste Audioqualität und beschränken Sie sich auf menschliche Vokalisationen anstelle von nicht vokalen Soundeffekten.

| Bereich | Platzierung | Beispiele |
| --- | --- | --- |
| **Auf Ebene des Zuges** (während des gesamten Zuges) | `speech_metadata.style` | `"angry tone"`, `"speaking rapidly"`, `"out of breath"`, `"whispers"`, `"sarcastic"` |
| **Zu einem bestimmten Zeitpunkt** (tritt bei einem bestimmten Wort auf) | Inline in `text` (`<...>`) | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### Tempo und Pausen

Sie können Rhythmus und Stille auf drei Detaillierungsebenen steuern:

- **Satzzeichen und Auslassungspunkte**:Verwenden Sie Kommas, Gedankenstriche (`--`) und Auslassungspunkte (`...`), um natürliche Gesprächspausen zu erzeugen.
- **Inline-Pausen-Tags**:Fügen Sie `<short pause>` oder `<long pause>` an den genauen Stellen im Skript ein, an denen ein Sprecher pausieren soll:
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **Geschwindigkeit auf Zugebene**:Legen Sie in `speech_metadata` `"style": "speaking rapidly"` oder `"style": "speaking slowly"` fest, um die Sprechgeschwindigkeit für den gesamten Zug zu steuern.

### Prosodie und Tonhöhe

Verwenden Sie **`speech_metadata.style`**, um Prosodie, Tonhöhe und Betonung in einem Zug zu steuern (z. B. `"style": "high pitch, cheerful and excited inflection"` oder `"style": "monotone and flat"`). Wenn sich die Emotion oder Prosodie während des Dialogs ändert, teilen Sie das Skript in separate Züge mit unterschiedlichen `style`-Werten für jeden Zug auf.

### Schwerpunkt

Sie können bestimmte Wörter im Transkript großschreiben und Satzzeichen und Inline-Vocal-Tags verwenden, um wichtige Wörter natürlich zu betonen:

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### Vocal-Bursts und Geräusche

Nicht sprachliche menschliche Äußerungen werden inline mit spitzen Klammern (`<...>`) an der genauen Stelle platziert, an der das Geräusch auftreten soll. Empfohlene Gesangstags:

|  |  |  |  |
| --- | --- | --- | --- |
| `<argh>` | `<breath>` | `<heavy breath>` | `<exhales>` |
| `<cackle>` | `<cheer>` | `<chuckle>`/`<chuckles>` | `<cough>` |
| `<cry>` | `<gasp>` | `<giggle>` | `<groan>` |
| `<growl>` | `<grunt>` | `<grr>` | `<hiss>` |
| `<laugh>`/`<laughter>` | `<moan>` | `<pant>` | `<pff>`/`<phew>` |
| `<scream>` | `<shout>` | `<shriek>` | `<sigh>`/`<sighs>` |
| `<sneeze>` | `<snicker>` | `<snort>` | `<sob>` |
| `<throat-clearing>` | `<tsk>` | `<whimper>` | `<whispers>`/`<whispering>` |
| `<yawn>` | `<short pause>` | `<long pause>` |  |

### Backchannels und sich überschneidende Sprache

Bei Dialogen mit mehreren Sprechern können Sie Reaktionen des Zuhörers in Pipe-Zeichen (`|reaction|`) innerhalb des Sprecherbeitrags einschließen, um natürliche Backchannels oder überlappende Sprache zu erzeugen, ohne dass für jede Reaktion ein separater Beitrag erforderlich ist.

- **Kurze Backchannel-Reaktionen**:Füge kurze Reaktionen des Zuhörers (`|oh hmm|`, `|oh really?|`, `|absolutely|`) in den Beitrag des aktiven Sprechers ein:
  - **Runde 1 (Sprecher A):** `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **Runde 2 (Sprecher B):** `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **Turn 3 (Speaker A):** `"Then let's ship it |absolutely| and watch the dashboards."`
- **Überlappende und verschachtelte Sprache**:Verwenden Sie mehrere Pipe-Segmente, um gleichzeitige oder verschachtelte Sprache zwischen zwei Sprechern zu simulieren. Das funktioniert am besten mit `gemini-3.8-flash-tts`:
  - **Gleichzeitiger Countdown/Refrain**:`"Let's surprise him on three |ok| ready?"` gefolgt von `"one. two. three. |happy| happy |birthday| birthday!"`
  - **Vollständige Sprecherüberschneidung**:`"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### Konsistenz über Generationen hinweg und was Sie vermeiden sollten

Beachten Sie die folgenden Richtlinien, um die Stabilität der stimmlichen Identität über mehrere Turns hinweg zu gewährleisten:

- **Design-Personas im Voice-Design vorab anstelle von langen Stilblöcken:**
  Lange `"Audio Profile"`-Absätze und `"Director's Notes"`-Listen mit mehreren Aufzählungszeichen, die aus früheren Modellen übernommen wurden, sind die häufigste Ursache für Voice-Drift.
  Nutzen Sie diese kreative Intuition von Anfang an beim [Stimmendesign](https://ai.google.dev/gemini-api/docs/voice-design?hl=de), um eine dauerhafte benutzerdefinierte `voice_...`-Identität zu generieren, und verwenden Sie diese Stimm-ID dann in Ihren TTS-Aufrufen.
- **Für Stabilität auf die Sprachreferenz verlassen (Meta-Anweisungen weglassen)**:
  Gemini 3.8-TTS-Modelle sind so trainiert, dass sie sich zuerst an der Audio-Referenz orientieren.
  Fügen Sie keine Anweisungen hinzu, die das Modell anweisen, die Stimme konstant zu halten, z. B. `"do not switch speaker identity"` oder `"maintain identical timbre"`. Zusätzlicher Prompt-Text erhöht die Abweichung. Lassen Sie unnötige Stilanweisungen weg und lassen Sie das Modell natürlich um den stabilen Punkt variieren, der durch die Sprachreferenz vorgegeben wird.
- **Unveränderliche Sprechermerkmale in `style` nicht ändern:** Geben Sie in `speech_metadata.style` keine Änderungen des Alters, Geschlechts, Namens oder des Akzents an.
  Wählen Sie stattdessen eine regionale Stimme aus der erweiterten Stimmenbibliothek aus oder erstellen Sie eine mit [Stimmendesign](https://ai.google.dev/gemini-api/docs/voice-design?hl=de).

### Empfohlener Workflow

1. **Charakter einmal erstellen**:Erstellen Sie Ihren Charakter unter [Voice Design](https://ai.google.dev/gemini-api/docs/voice-design?hl=de) oder wählen Sie eine regionale Stimme aus der erweiterten Stimmenbibliothek aus, die Ihrer Zielsprache und Persona entspricht.
2. **Natürliche gesprochene Transkripte mit Unflüssigkeiten schreiben**:Für maximale Natürlichkeit schreiben Sie das `text` als echtes gesprochenes Transkript – einschließlich natürlicher Unflüssigkeiten und Zögern (z. B. `"Oh uh yeah I think... hm, so that's interesting"`).
3. **Einfache TTS zuerst testen**:Synthetisieren Sie Ihr Transkript zuerst mit einem leeren `style`-Feld. Für die meisten Anfragen ist überhaupt keine `style`-Anweisung erforderlich.
4. **Fügen Sie kurze `style`-Prompts nur für Anpassungen hinzu**:Fügen Sie einen kurzen `style`-String (z. B. `"casual, friendly"` oder `"muttering, then reassuring"`) nur für Turns hinzu, die eine bestimmte Anpassung erfordern. Verwenden Sie diesen kurzen String für alle Turns, wenn Sie eine einheitliche Baseline wünschen.

### Mehrfachdialog und Sprachagenten

Wenn Sie Echtzeit-Sprachagenten oder Mehrfachdialog-Anwendungen entwickeln:

- Führen Sie **einen TTS-Aufruf pro Runde** aus, wenn LLM-Textblöcke eingehen.
- Lassen Sie die konfigurierte `voice` (vorgefertigt, entworfen `voice_...` oder repliziert `voice_...` / `voicekey_...`) die Identität des Sprechers über mehrere Turns hinweg beibehalten. Senden Sie niemals bei jedem Turn eine lange Charakter-Persona neu.
- Lassen Sie das Feld `style` pro Zug leer oder senden Sie für die gesamte Unterhaltung einen kurzen konstanten String (z. B. `"casual, friendly"`).
- Teilen Sie lange Antworten des Kundenservicemitarbeiters in kürzere Abschnitte auf, anstatt stärkere Stil-Prompts zu verwenden.

## Beschränkungen

- TTS-Modelle akzeptieren nur Texteingaben und generieren nur Audioausgaben.
- Die Generierung mit mehreren Sprechern in einer einzelnen Anfrage (`speech_config.speakers`) unterstützt bis zu zwei Sprecher mit vordefinierten Stimmen. Wenn Sie benutzerdefinierte (`voice_...`) oder replizierte (`voice_...` / `voicekey_...`) Stimmen in einem Dialog mit mehreren Figuren kombinieren möchten, müssen Sie die Äußerung jedes Sprechers einzeln synthetisieren.
  Da bei unären Anfragen standardmäßig `audio/wav` mit einem 44 Byte großen RIFF-Header zurückgegeben wird, müssen Sie rohes PCM (`{"type": "audio", "mime_type": "audio/l16"}`) anfordern oder den WAV-Header aus jedem Turn entfernen, bevor Sie die 24 kHz-PCM-Audio-Frames verketten.
- **Speicherlimits und TTL für benutzerdefinierte Stimmen:**
  - **Statusbehaftete Stimmen (`store=True`, per Prompt erstellt oder repliziert)**: Maximal **200 Stimmen pro Projekt** mit einer **Gültigkeitsdauer von 1 Jahr** (Time-to-Live).
  - **Zustandslose Sprachschlüssel (`store=False`, `voicekey_...`)**: **Gültigkeitsdauer (TTL) von 7 Tagen**.
- Informationen zur Sprachabdeckung finden Sie im Abschnitt [Unterstützte Sprachen](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de#languages).

## Nächste Schritte

- Mit [Voice Design](https://ai.google.dev/gemini-api/docs/voice-design?hl=de) können Sie benutzerdefinierte Gesangspersonas aus natürlicher Sprache erstellen.
- Die Stimme eines vorhandenen Sprechers in der [Stimmreplikation](https://ai.google.dev/gemini-api/docs/voice-replication?hl=de) replizieren
- Vergleichen Sie die Modellspezifikationen auf den Modellseiten [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=de) und [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=de).
- Mit der [Live API](https://ai.google.dev/gemini-api/docs/live?hl=de) können Sie interaktive bidirektionale Audiofunktionen nutzen.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-10-02 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-10-02 (UTC)."],[],[]]
