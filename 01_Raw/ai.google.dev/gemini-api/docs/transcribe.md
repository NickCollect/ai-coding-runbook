---
source_url: https://ai.google.dev/gemini-api/docs/transcribe?hl=it
fetched_at: 2026-10-19T05:59:11.062475+00:00
title: "Trascrizione audio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Trascrizione audio

L'API Gemini converte il parlato nei file audio in testo utilizzando il modello Gemini 3.5 Transcribe (`gemini-3.5-transcribe`). Grazie alle funzionalità di comprensione dell'audio di Gemini, offre una trascrizione accurata con identificazione automatica della lingua, diarizzazione degli oratori, timestamp a livello di parola e suggerimenti per il vocabolario personalizzato. Offre anche una modalità di [trascrizione intelligente](#transcription-modes) con rimozione di disfluenze e formattazione intelligente.

Per trascrivere un file audio, caricalo e passalo a `gemini-3.5-transcribe`:

### Python

```
from google import genai

client = genai.Client()

audio_file = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const audioFile = await client.files.upload({
  file: "path/to/sample.mp3",
  config: { mime_type: "audio/mp3" },
});

const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
});

console.log(interaction.output_text);
```

### Go

```
package main

import (
    "context"
    "fmt"
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
# First upload the file via the Files API, then pass its URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

## Panoramica

Gemini 3.5 Transcribe è ottimizzato per le attività di sintesi vocale. Gestisce accenti diversi, rumori di fondo e conversazioni in più lingue.

Le sue funzionalità principali includono:

- **Riconoscimento vocale automatico (ASR)**: rileva automaticamente le lingue in oltre [85 impostazioni internazionali](#supported-languages). Gestisce il cambio di codice all'interno della frase e tra le frasi senza configurazione manuale.
- **Vocabolario personalizzato**:orienta il riconoscimento verso termini, acronimi e nomi propri specifici del dominio passando fino a 1000 frasi.
- **Diarizzazione degli speaker**:distingue tra più interlocutori e attribuisce i segmenti parlati a etichette distinte.
- **Timestamp a livello di parola**:genera offset temporali di inizio e di fine precisi per ogni parola riconosciuta.
- **Trascrizione intelligente**:elimina le disfluenze, gli intercalari e le ripetizioni e applica una formattazione strutturata.
- **Formattazione e normalizzazione**:applica maiuscole, punteggiatura e normalizzazione del testo inversa, ad esempio convertendo "ventisei milioni di dollari" in "26 milioni di $".

Per il ragionamento audio generale o la risposta a domande sui contenuti audio, utilizza [Comprensione audio](https://ai.google.dev/gemini-api/docs/audio?hl=it). Per la sintesi audio della sintesi vocale, utilizza [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it).

## Rilevamento della lingua e suggerimenti

Per impostazione predefinita, il modello rileva automaticamente la lingua parlata. Passa da una lingua all'altra in modo dinamico quando gli oratori cambiano lingua.

Per utilizzare il rilevamento automatico, ometti `language_codes` o fornisci un elenco vuoto:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "language_codes": [],
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      language_codes: [],
    },
  },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    LanguageCodes: []string{},
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "language_codes": []
      }
    }
  }'
```

Se conosci la lingua in anticipo, specifica i codici lingua BCP-47 in `language_codes` per migliorare l'accuratezza della trascrizione (vedi [Lingue supportate](#supported-languages)):

### Python

```
generation_config = {
    "transcription_config": {
        "language_codes": ["es-ES"],
    }
}
```

### JavaScript

```
const generationConfig = {
  transcription_config: {
    language_codes: ["es-ES"],
  },
};
```

### Go

```
package main

import (
    "google.golang.org/genai/interactions/models/interactions"
)

func main() {
    generationConfig := &interactions.GenerationConfig{
        TranscriptionConfig: &interactions.TranscriptionConfig{
            LanguageCodes: []string{"es-ES"},
        },
    }
    _ = generationConfig
}
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "language_codes": ["es-ES"]
    }
  }
}
```

## Vocabolario personalizzato

Puoi indirizzare il modello vocale verso parole non comuni, tecnicismi, nomi di brand o nomi propri. Fornisci fino a 1000 termini nell'array `custom_vocabulary` (in genere si ottengono risultati ottimali con un massimo di 100 termini):

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"],
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      custom_vocabulary: ["Gemini", "Kubernetes", "BigQuery"],
    },
  },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    CustomVocabulary: []string{"Gemini", "Kubernetes", "BigQuery"},
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"]
      }
    }
  }'
```

## Diarizzazione degli speaker

La diarizzazione degli interlocutori identifica le diverse voci nella registrazione e tagga ogni segmento con un identificatore dell'interlocutore, ad esempio `spk_1` o `spk_2`. Sono supportati fino a 8 relatori (l'attribuzione per 3 o più relatori è sperimentale).

Abilita la diarizzazione configurando `diarization_mode` in `mode`:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": {
                "type": "verbatim",
                "diarization_mode": "speaker",
            },
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: {
        type: "verbatim",
        diarization_mode: "speaker",
      },
    },
  },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.NewTranscriptionMode(interactions.VerbatimTranscriptionMode{
                        DiarizationMode: genai.Ptr("speaker"),
                    }))),
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": {
          "type": "verbatim",
          "diarization_mode": "speaker"
        }
      }
    }
  }'
```

## Timestamp a livello di parola

I timestamp a livello di parola forniscono offset di inizio e fine esatti per ogni parola riconosciuta nello stream audio.

Attiva i timestamp configurando `timestamp_granularities` in `mode`:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": {
                "type": "verbatim",
                "timestamp_granularities": ["word"],
            },
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: {
        type: "verbatim",
        timestamp_granularities: ["word"],
      },
    },
  },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.NewTranscriptionMode(interactions.VerbatimTranscriptionMode{
                        TimestampGranularities: []string{"word"},
                    }))),
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": {
          "type": "verbatim",
          "timestamp_granularities": ["word"]
        }
      }
    }
  }'
```

Puoi combinare `diarization_mode` e `timestamp_granularities` in `mode` per ricevere sia le etichette di chi parla sia i timestamp a livello di parola:

### Python

```
generation_config = {
    "transcription_config": {
        "mode": {
            "type": "verbatim",
            "diarization_mode": "speaker",
            "timestamp_granularities": ["word"],
        },
    }
}
```

### JavaScript

```
const generationConfig = {
  transcription_config: {
    mode: {
      type: "verbatim",
      diarization_mode: "speaker",
      timestamp_granularities: ["word"],
    },
  },
};
```

### Go

```
package main

import (
    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
)

func main() {
    generationConfig := &interactions.GenerationConfig{
        TranscriptionConfig: &interactions.TranscriptionConfig{
            Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.NewTranscriptionMode(interactions.VerbatimTranscriptionMode{
                DiarizationMode:        genai.Ptr("speaker"),
                TimestampGranularities: []string{"word"},
            }))),
        },
    }
    _ = generationConfig
}
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "mode": {
        "type": "verbatim",
        "diarization_mode": "speaker",
        "timestamp_granularities": ["word"]
      }
    }
  }
}
```

## Modalità di trascrizione

Gemini 3.5 Transcribe supporta due modalità di trascrizione tramite il parametro `mode`:

- **`verbatim` (impostazione predefinita)**: restituisce una trascrizione esatta parola per parola di tutto ciò che viene detto, conservando le parole di riempimento grezze ("um", "uh", "like", "you know"), le ripetizioni, le pause e le false partenze. In questa modalità (`{"type": "verbatim", ...}`) vengono configurati i timestamp e la diarizzazione degli interlocutori.
- **`smart` (Trascrizione intelligente)**: ottimizza la trascrizione per la lettura applicando una post-elaborazione intelligente:
  - **Rimozione delle disfluenze**: elimina le parole di riempimento, le balbuzie e gli avvii errati.
  - **Correzioni automatiche in linea**: risolve direttamente le correzioni vocali (ad esempio, *"Ci vediamo martedì, no, mercoledì alle 14:00"* diventa *"Ci vediamo mercoledì alle 14:00"*).
  - **Formattazione strutturata automatica**: struttura automaticamente i pensieri espressi in paragrafi, elenchi numerati, elenchi puntati, date, valute e numeri formattati.
  - **Pulizia grammaticale**: applica punteggiatura, maiuscole e flusso naturali.

| Audio parlato | `verbatim` output | Output `smart` (Trascrizione intelligente) |
| --- | --- | --- |
| "Allora, per la riunione, penso che dovremmo invitare Alice e, no, aspetta, Bob e Carol". | "Allora, per la riunione penso che dovremmo invitare Alice e no, Bob e Carol". | "Per la riunione, penso che dovremmo invitare Bob e Carol." |
| "First item review budget second item finalize timeline third item send recap" | "first item review budget second item finalize timeline third item send recap" | "1. Controlla il budget 2. Finalizza la sequenza temporale 3. Invia riepilogo" |

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": "smart",
        }
    },
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: "smart",
    },
  },
});
console.log(interaction.output_text);
```

### Go

```
package main

import (
    "context"
    "fmt"
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.TranscriptionConfigModeEnumSmart)),
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": "smart"
      }
    }
  }'
```

## Analisi dell'output della trascrizione

Il testo completo della trascrizione viene restituito in `interaction.output_text`.

Quando `timestamp_granularities` o `diarization_mode` è abilitato, l'API restituisce anche annotazioni dettagliate a livello di parola allegate ai contenuti dell'interazione.

Ecco come estrarre e scorrere i timestamp a livello di parola e i turni di parola:

### Python

```
def extract_word_annotations(interaction):
    words = []
    for step in getattr(interaction, "steps", []) or []:
        for content in getattr(step, "content", []) or []:
            for annotation in getattr(content, "annotations", []) or []:
                if getattr(annotation, "type", None) == "word_info":
                    words.append(annotation)
    return words

words = extract_word_annotations(interaction)

for w in words:
    speaker = f"[{w.speaker}] " if getattr(w, "speaker", None) else ""
    start = getattr(w, "start_offset", "")
    end = getattr(w, "end_offset", "")
    timing = f"({start} -> {end}) " if start and end else ""
    print(f"{speaker}{timing}{w.text}")
```

### JavaScript

```
function extractWordAnnotations(interaction) {
  const words = [];
  for (const step of interaction.steps ?? []) {
    for (const content of step.content ?? []) {
      for (const annotation of content.annotations ?? []) {
        if (annotation.type === "word_info") {
          words.push(annotation);
        }
      }
    }
  }
  return words;
}

const words = extractWordAnnotations(interaction);

for (const w of words) {
  const speaker = w.speaker ? `[${w.speaker}] ` : "";
  const timing = (w.start_offset && w.end_offset) ? `(${w.start_offset} -> ${w.end_offset}) ` : "";
  console.log(`${speaker}${timing}${w.text}`);
}
```

### Go

```
package main

import (
    "fmt"

    "google.golang.org/genai/interactions/models/interactions"
)

func extractWordAnnotations(interaction *interactions.Interaction) []*interactions.WordInfo {
    var words []*interactions.WordInfo
    if interaction == nil {
        return words
    }
    for _, step := range interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    for _, annotation := range content.TextContent.Annotations {
                        if annotation.WordInfo != nil {
                            words = append(words, annotation.WordInfo)
                        }
                    }
                }
            }
        }
    }
    return words
}

func main() {
    var interaction *interactions.Interaction
    words := extractWordAnnotations(interaction)

    for _, w := range words {
        speaker := ""
        if w.Speaker != nil && *w.Speaker != "" {
            speaker = fmt.Sprintf("[%s] ", *w.Speaker)
        }
        timing := ""
        if w.StartOffset != nil && w.EndOffset != nil {
            timing = fmt.Sprintf("(%s -> %s) ", *w.StartOffset, *w.EndOffset)
        }
        fmt.Printf("%s%s%s\n", speaker, timing, w.GetText())
    }
}
```

### REST

```
{
  "id": "interactions/abc123xyz",
  "status": "completed",
  "steps": [
    {
      "id": "step_001",
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Hello world",
          "annotations": [
            {
              "type": "word_info",
              "text": "Hello",
              "speaker": "spk_1",
              "start_offset": "0.100s",
              "end_offset": "0.450s"
            },
            {
              "type": "word_info",
              "text": "world",
              "speaker": "spk_1",
              "start_offset": "0.500s",
              "end_offset": "0.850s"
            }
          ]
        }
      ]
    }
  ]
}
```

## Lingue supportate

Le seguenti lingue e i seguenti codici lingua BCP-47 sono supportati per Gemini 3.5 Transcribe:

| Lingua | Codice BCP-47 | Lingua | Codice BCP-47 |
| --- | --- | --- | --- |
| Afrikaans | `af-ZA` | Giapponese | `ja-JP` |
| Amarico | `am-ET` | Giavanese | `jv-ID` |
| Arabo (Egitto) | `ar-EG` | Kabuverdianu | `kea-CV` |
| Armeno | `hy-AM` | Kannada | `kn-IN` |
| Assamese | `as-IN` | Kazako | `kk-KZ` |
| Azero | `az-AZ` | Coreano | `ko-KR` |
| Bielorusso | `be-BY` | Kirgizo | `ky-KG` |
| Bengalese (Bangladesh) | `bn-BD` | Lettone | `lv-LV` |
| Bengalese (India) | `bn-IN` | Lingala | `ln-CD` |
| Bosniaco | `bs-BA` | Lituano | `lt-LT` |
| Bulgaro | `bg-BG` | Macedone | `mk-MK` |
| Bulgaro (aromeno) | `rup-BG` | Malese | `ms-MY` |
| Birmano | `my-MM` | Malayalam | `ml-IN` |
| Cantonese (tradizionale) | `yue-Hant-HK` | Maltese | `mt-MT` |
| Catalano | `ca-ES` | Cinese mandarino (semplificato) | `cmn-Hans-CN` |
| Cebuano | `ceb` | Marathi | `mr-IN` |
| Khmer centrale | `km-KH` | Mongolo | `mn-MN` |
| Croato | `hr-HR` | Nepalese | `ne-NP` |
| Ceco | `cs-CZ` | Norvegese | `nb-NO` |
| Danese | `da-DK` | Oriya | `or-IN` |
| Olandese | `nl-NL` | Polacco | `pl-PL` |
| Inglese (Gran Bretagna) | `en-GB` | Portoghese (Brasile) | `pt-BR` |
| Inglese (India) | `en-IN` | Portoghese (Portogallo) | `pt-PT` |
| Inglese (Stati Uniti) | `en-US` | Punjabi | `pa-IN` |
| Estone | `et-EE` | Punjabi (alfabeto gurmukhi) | `pa-Guru-IN` |
| Farsi | `fa-IR` | Rumeno | `ro-RO` |
| Filippino | `fil-PH` | Russo | `ru-RU` |
| Finlandese | `fi-FI` | Serbo | `sr-RS` |
| Francese | `fr-FR` | Sindhi (alfabeto arabo) | `sd-Arab-IN` |
| Galiziano | `gl-ES` | Slovacco | `sk-SK` |
| Georgiano | `ka-GE` | Sloveno | `sl-SI` |
| Tedesco | `de-DE` | Spagnolo (America Latina) | `es-419` |
| Greek | `el-GR` | Spagnolo (Stati Uniti) | `es-US` |
| Gujarati | `gu-IN` | Swahili (Kenya) | `sw-KE` |
| Hausa | `ha-NG` | Svedese | `sv-SE` |
| Ebraico | `he-IL` | Tagico | `tg-TJ` |
| Hindi | `hi-IN` | Telugu | `te-IN` |
| Ungherese | `hu-HU` | Thailandese | `th-TH` |
| Islandese | `is-IS` | Turco | `tr-TR` |
| Inglese indiano | `en-IN` | Ucraino | `uk-UA` |
| Indonesiano | `id-ID` | Uzbeco | `uz-UZ` |
| Italiano | `it-IT` | Vietnamita | `vi-VN` |

## Formati audio supportati

Gemini 3.5 Transcribe supporta i seguenti tipi MIME di formati audio:

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG - `audio/ogg`
- FLAC - `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16 - `audio/l16`
- Opus - `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM - `audio/webm`

Per l'elenco completo dei tipi MIME e degli schemi dei parametri supportati, consulta il [riferimento API Interactions](https://ai.google.dev/api/interactions-api?hl=it#Resource:Content).

## Riferimento al parametro

Configura la trascrizione impostando i campi all'interno dell'oggetto `transcription_config` in `generation_config`:

| Campo | Tipo | Descrizione |
| --- | --- | --- |
| `language_codes` | Array di stringhe | Codici lingua BCP-47 (ad es. `["en-US"]`). Se omesso o vuoto (`[]`), il modello rileva automaticamente la lingua e gestisce il cambio di codice. |
| `custom_vocabulary` | Array di stringhe | Fino a 1000 termini personalizzati, acronimi o nomi propri per orientare il riconoscimento vocale. Non compatibile con la diarizzazione degli interlocutori e i timestamp a livello di parola. |
| `mode` | Oggetto o stringa | Configurazione della modalità di trascrizione. Accetta `"smart"` o un oggetto in modalità letterale (`{"type": "verbatim", ...}`). Il valore predefinito è la trascrizione letterale. |
| `mode.type` | Stringa | *(Solo modalità Verbatim)* Identificatore della modalità. Sempre impostato su `"verbatim"`. |
| `mode.timestamp_granularities` | Array di stringhe | *(solo modalità Verbatim)* Granularità dei timestamp da restituire. Passa `["word"]` per abilitare gli offset di inizio e fine delle parole. Non compatibile con il vocabolario personalizzato. |
| `mode.diarization_mode` | Stringa | *(Solo modalità letterale)* Modalità di diarizzazione. Passa `"speaker"` per identificare ed etichettare le diverse persone che parlano. Incompatibile con il vocabolario personalizzato. |

## Best practice

- **Fornisci audio pulito**:assicurati che le registrazioni audio abbiano una separazione vocale chiara ed evita il clipping eccessivo.
- **Fornisci suggerimenti sulla lingua quando è nota**:se conosci la lingua dell'audio in anticipo, specifica `language_codes` per massimizzare l'accuratezza.
- **Vocabolario personalizzato di destinazione**:includi solo termini di dominio, nomi di brand o nomi propri distinti in `custom_vocabulary` anziché parole comuni di uso quotidiano.
- **Utilizza l'API Files per le registrazioni di grandi dimensioni**:per i file più lunghi di pochi secondi, carica il file utilizzando `client.files.upload` e passa l'URI del file restituito al modello.

## Limitazioni

- **Durata audio**:le richieste unarie standard supportano file audio fino a 1 ora. L'elaborazione audio è limitata a 30 minuti quando sono attivate funzionalità come la diarizzazione degli interlocutori o i timestamp a livello di parola.
- **Timestamp a livello di parola**:l'attivazione dei timestamp a livello di parola potrebbe ridurre l'accuratezza complessiva della trascrizione.
- **Diarizzazione degli interlocutori**:la diarizzazione degli interlocutori supporta fino a 8 interlocutori. L'attribuzione degli speaker per 3 o più speaker è sperimentale.
- **Vocabolario personalizzato**:puoi fornire fino a 1000 termini in `custom_vocabulary`, ma in genere i risultati migliori si ottengono con un massimo di 100 termini. Non puoi combinare `custom_vocabulary` con la diarizzazione degli oratori o i timestamp a livello di parola; l'API rifiuta le richieste che specificano `custom_vocabulary` insieme a una delle due funzionalità.
- **Compatibilità delle modalità**:la trascrizione intelligente (`"smart"`) non può essere combinata con `timestamp_granularities` o `diarization_mode`.

## Passaggi successivi

- Trasmetti audio in tempo reale con la [guida alla trascrizione in tempo reale](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=it) utilizzando l'API Live.
- Esplora [Comprensione dell'audio](https://ai.google.dev/gemini-api/docs/audio?hl=it) per analizzare, riepilogare o interrogare i contenuti audio.
- Scopri come sintetizzare l'audio dal testo utilizzando [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it).
- Consulta la [pagina dei prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#gemini-3.5-transcribe) per i prezzi dei modelli e i limiti dei token.
- Consulta la guida all'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it) per informazioni dettagliate sul caricamento e sulla gestione dei file multimediali.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-24 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-24 UTC."],[],[]]
