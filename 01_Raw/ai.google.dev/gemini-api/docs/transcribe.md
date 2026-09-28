---
source_url: https://ai.google.dev/gemini-api/docs/transcribe?hl=id
fetched_at: 2026-09-28T06:25:55.156807+00:00
title: "Transkripsi audio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Transkripsi audio

Gemini API mengonversi ucapan dalam file audio menjadi teks menggunakan model Transcribe Gemini 3.5 (`gemini-3.5-transcribe`). Berdasarkan kemampuan pemahaman audio Gemini, API ini memberikan transkripsi yang akurat dengan identifikasi bahasa otomatis, diarisasi penutur, stempel waktu tingkat kata, dan petunjuk kosakata kustom. Fitur ini juga menyediakan mode [transkripsi cerdas](#transcription-modes) yang menampilkan penghapusan ketidaklancaran dan pemformatan cerdas.

Untuk mentranskripsikan file audio, upload audio dan teruskan ke `gemini-3.5-transcribe`:

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

## Ringkasan

Transkripsi Gemini 3.5 dioptimalkan untuk tugas speech-to-text. Model ini menangani beragam aksen, suara bising di latar belakang, dan percakapan multibahasa.

Kemampuan utama meliputi:

- **Pengenalan ucapan otomatis (ASR):** Mendeteksi bahasa secara otomatis di lebih dari [85 lokalitas](#supported-languages). Menangani peralihan kode intra-kalimat dan antar-kalimat tanpa konfigurasi manual.
- **Kosakata kustom:** Membiasakan pengenalan terhadap istilah khusus domain, akronim, dan nama diri dengan meneruskan hingga 1.000 frasa.
- **Diarisasi pembicara:** Membedakan beberapa pembicara dan mengatribusikan segmen yang diucapkan ke label yang berbeda.
- **Stempel waktu tingkat kata:** Membuat offset waktu mulai dan berakhir yang akurat untuk setiap kata yang dikenali.
- **Transkripsi pintar:** Menghapus ketidaklancaran, kata pengisi, pengulangan, dan menerapkan format terstruktur.
- **Pemformatan dan normalisasi:** Menerapkan kapitalisasi, tanda baca, dan normalisasi teks terbalik, seperti mengonversi "dua puluh enam juta dolar" menjadi "$26M".

Untuk penalaran audio umum atau menjawab pertanyaan melalui konten audio, gunakan [Pemahaman audio](https://ai.google.dev/gemini-api/docs/audio?hl=id). Untuk sintesis audio text-to-speech, gunakan [Text-to-speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id).

## Deteksi dan petunjuk bahasa

Secara default, model akan mendeteksi bahasa lisan secara otomatis. Fitur ini beralih antarbahasa secara dinamis saat pembicara melakukan peralihan kode.

Untuk menggunakan deteksi otomatis, hapus `language_codes` atau berikan daftar kosong:

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

Jika Anda mengetahui bahasa sebelumnya, tentukan kode bahasa BCP-47 di `language_codes` untuk meningkatkan akurasi transkripsi (lihat [Bahasa yang didukung](#supported-languages)):

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

## Kosakata kustom

Anda dapat mengarahkan model ucapan ke kata-kata yang tidak umum, jargon teknis, nama merek, atau nama diri. Berikan hingga 1.000 istilah dalam array `custom_vocabulary` (hasil terbaik biasanya dicapai dengan hingga 100 istilah):

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

## Diarisasi pembicara

Diarisasi pembicara mengidentifikasi suara yang berbeda dalam rekaman dan memberi tag pada setiap segmen dengan ID pembicara seperti `spk_1` atau `spk_2`. Hingga 8 pembicara didukung (atribusi untuk 3 pembicara atau lebih bersifat eksperimental).

Aktifkan diarisasi dengan mengonfigurasi `diarization_mode` dalam `mode`:

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

## Stempel waktu tingkat kata

Stempel waktu tingkat kata memberikan offset awal dan akhir yang tepat untuk setiap kata yang dikenali dalam aliran audio.

Aktifkan stempel waktu dengan mengonfigurasi `timestamp_granularities` dalam `mode`:

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

Anda dapat menggabungkan `diarization_mode` dan `timestamp_granularities` di `mode` untuk menerima label pembicara dan stempel waktu kata:

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

## Mode transkripsi

Gemini 3.5 Transcribe mendukung dua mode transkripsi melalui parameter `mode`:

- **`verbatim` (default)**: Menampilkan transkrip kata demi kata yang persis dari semua yang diucapkan, dengan mempertahankan kata pengisi mentah ("um", "eh", "kayak", "tahu"), pengulangan, jeda, dan awal yang salah. Stempel waktu dan diarisasi pembicara dikonfigurasi dalam mode ini (`{"type": "verbatim", ...}`).
- **`smart` (Transkripsi pintar)**: Mengoptimalkan transkrip untuk dibaca dengan menerapkan pasca-pemrosesan cerdas:
  - **Penghapusan ketidaklancaran**: Menghapus kata pengisi percakapan, gagap, dan awal yang salah.
  - **Koreksi mandiri inline**: Menyelesaikan koreksi lisan secara langsung (misalnya, *"Mari bertemu pada hari Selasa, eh tidak, hari Rabu pukul dua"* menjadi *"Mari bertemu pada hari Rabu pukul 14.00"*).
  - **Pemformatan terstruktur otomatis**: Secara otomatis menyusun pemikiran yang diucapkan menjadi paragraf, daftar bernomor, poin-poin, tanggal, mata uang, dan angka yang diformat.
  - **Pembersihan tata bahasa**: Menerapkan tanda baca, kapitalisasi kalimat, dan alur yang alami.

| Audio lisan | `verbatim` output | Output `smart` (Transkripsi cerdas) |
| --- | --- | --- |
| "Um, jadi untuk rapat, saya pikir kita harus, eh, mengundang Alice dan, tunggu, bukan, Bob dan Carol." | "Jadi untuk rapat, saya rasa kita harus mengundang Alice, eh bukan, Bob dan Carol." | "Untuk rapat, sebaiknya kita mengundang Budi dan Ari." |
| "Item pertama tinjau anggaran, item kedua selesaikan linimasa, item ketiga kirim ringkasan" | "tinjau anggaran item pertama selesaikan linimasa item kedua kirim ringkasan item ketiga" | "1. Tinjau anggaran 2. Menyelesaikan linimasa 3. Kirim ringkasan" |

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

## Mengurai output transkripsi

Teks transkrip lengkap ditampilkan di `interaction.output_text`.

Jika `timestamp_granularities` atau `diarization_mode` diaktifkan, API juga akan menampilkan anotasi tingkat kata mendetail yang dilampirkan pada konten interaksi.

Berikut cara mengekstrak dan melakukan iterasi pada stempel waktu kata dan pergantian pembicara:

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

## Bahasa yang didukung

Bahasa dan kode bahasa BCP-47 berikut didukung untuk Transkripsi Gemini 3.5:

| Language | Kode BCP-47 | Language | Kode BCP-47 |
| --- | --- | --- | --- |
| Afrika | `af-ZA` | Jepang | `ja-JP` |
| Amharik | `am-ET` | Jawa | `jv-ID` |
| Arab (Mesir) | `ar-EG` | Kabuverdianu | `kea-CV` |
| Armenia | `hy-AM` | Kannada | `kn-IN` |
| Assam | `as-IN` | Kazak | `kk-KZ` |
| Azerbaijan | `az-AZ` | Korea | `ko-KR` |
| Belarusia | `be-BY` | Kirgiz | `ky-KG` |
| Bengali (Bangladesh) | `bn-BD` | Latvia | `lv-LV` |
| Bengali (India) | `bn-IN` | Lingala | `ln-CD` |
| Bosnia | `bs-BA` | Lituania | `lt-LT` |
| Bulgaria | `bg-BG` | Makedonia | `mk-MK` |
| Bulgaria (Aromania) | `rup-BG` | Melayu | `ms-MY` |
| Burma | `my-MM` | Malayalam | `ml-IN` |
| Kanton (Tradisional) | `yue-Hant-HK` | Malta | `mt-MT` |
| Katalan | `ca-ES` | China Mandarin (Aksara Sederhana) | `cmn-Hans-CN` |
| Cebuano | `ceb` | Marathi | `mr-IN` |
| Khmer Tengah | `km-KH` | Mongolia | `mn-MN` |
| Kroasia | `hr-HR` | Nepal | `ne-NP` |
| Ceko | `cs-CZ` | Norwegia | `nb-NO` |
| Denmark | `da-DK` | Oriya | `or-IN` |
| Belanda | `nl-NL` | Polandia | `pl-PL` |
| Inggris (Britania Raya) | `en-GB` | Portugis (Brasil) | `pt-BR` |
| Inggris (India) | `en-IN` | Portugis (Portugal) | `pt-PT` |
| Inggris (Amerika Serikat) | `en-US` | Punjabi | `pa-IN` |
| Estonia | `et-EE` | Punjabi (skrip Gurmukhi) | `pa-Guru-IN` |
| Persia | `fa-IR` | Rumania | `ro-RO` |
| Filipino | `fil-PH` | Rusia | `ru-RU` |
| Finlandia | `fi-FI` | Serbia | `sr-RS` |
| Prancis | `fr-FR` | Sindhi (skrip Arab) | `sd-Arab-IN` |
| Galisia | `gl-ES` | Slovakia | `sk-SK` |
| Georgia | `ka-GE` | Slovenia | `sl-SI` |
| Jerman | `de-DE` | Spanyol (Amerika Latin) | `es-419` |
| Yunani | `el-GR` | Spanyol (Amerika Serikat) | `es-US` |
| Gujarat | `gu-IN` | Swahili (Kenya) | `sw-KE` |
| Hausa | `ha-NG` | Swedia | `sv-SE` |
| Ibrani | `he-IL` | Tajik | `tg-TJ` |
| Hindi | `hi-IN` | Telugu | `te-IN` |
| Hungaria | `hu-HU` | Thai | `th-TH` |
| Islandia | `is-IS` | Turki | `tr-TR` |
| Inggris India | `en-IN` | Ukraina | `uk-UA` |
| Indonesia | `id-ID` | Uzbek | `uz-UZ` |
| Italia | `it-IT` | Vietnam | `vi-VN` |

## Format audio yang didukung

Transkripsi Gemini 3.5 mendukung jenis MIME format audio berikut:

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

Untuk mengetahui daftar lengkap jenis MIME dan skema parameter yang didukung, lihat [Referensi Interactions API](https://ai.google.dev/api/interactions-api?hl=id#Resource:Content).

## Referensi parameter

Konfigurasi transkripsi dengan menyetel kolom dalam objek `transcription_config` di `generation_config`:

| Kolom | Jenis | Deskripsi |
| --- | --- | --- |
| `language_codes` | Array string | Kode bahasa BCP-47 (misalnya, `["en-US"]`). Jika tidak disertakan atau kosong (`[]`), model akan otomatis mendeteksi bahasa dan menangani pengalihan kode. |
| `custom_vocabulary` | Array string | Hingga 1.000 istilah kustom, akronim, atau nama diri untuk memengaruhi pengenalan ucapan. Tidak kompatibel dengan diarisasi pembicara dan stempel waktu tingkat kata. |
| `mode` | Objek atau String | Konfigurasi mode transkripsi. Menerima `"smart"` atau objek mode kata demi kata (`{"type": "verbatim", ...}`). Secara default, transkripsi kata demi kata. |
| `mode.type` | String | *(Khusus mode kata demi kata)* ID mode. Selalu ditetapkan ke `"verbatim"`. |
| `mode.timestamp_granularities` | Array string | *(Hanya mode Kata demi kata)* Tingkat perincian stempel waktu yang akan ditampilkan. Teruskan `["word"]` untuk mengaktifkan offset awal dan akhir kata. Tidak kompatibel dengan kosakata kustom. |
| `mode.diarization_mode` | String | *(Khusus mode kata demi kata)* Mode diarisasi. Teruskan `"speaker"` untuk mengidentifikasi dan melabeli pembicara yang berbeda. Tidak kompatibel dengan kosakata kustom. |

## Praktik terbaik

- **Berikan audio yang jernih:** Pastikan rekaman audio memiliki pemisahan suara yang jelas dan hindari pemangkasan yang parah.
- **Berikan petunjuk bahasa jika diketahui:** Jika Anda mengetahui bahasa audio sebelumnya, tentukan `language_codes` untuk memaksimalkan akurasi.
- **Targetkan kosakata kustom:** Hanya sertakan istilah domain, nama merek, atau kata benda yang berbeda dalam `custom_vocabulary`, bukan kata-kata umum sehari-hari.
- **Gunakan Files API untuk rekaman berukuran besar:** Untuk file yang berdurasi lebih dari beberapa detik, upload file menggunakan `client.files.upload` dan teruskan URI file yang ditampilkan ke model.

## Batasan

- **Durasi audio:** Permintaan unary standar mendukung file audio hingga 1 jam. Pemrosesan audio dibatasi hingga 30 menit jika fitur seperti diarisasi speaker atau stempel waktu tingkat kata diaktifkan.
- **Stempel waktu tingkat kata:** Mengaktifkan stempel waktu tingkat kata dapat menurunkan akurasi transkripsi secara keseluruhan.
- **Diarisasi pembicara:** Diarisasi pembicara mendukung hingga 8 pembicara. Atribusi speaker untuk 3 speaker atau lebih bersifat eksperimental.
- **Kosakata kustom:** Anda dapat memberikan hingga 1.000 istilah dalam `custom_vocabulary`, tetapi hasil terbaik biasanya dicapai dengan hingga 100 istilah. Anda tidak dapat menggabungkan `custom_vocabulary` dengan diarisasi speaker atau stempel waktu tingkat kata; API menolak permintaan yang menentukan `custom_vocabulary` bersama dengan salah satu fitur tersebut.
- **Kompatibilitas mode:** Transkripsi cerdas (`"smart"`) tidak dapat digabungkan dengan `timestamp_granularities` atau `diarization_mode`.

## Langkah berikutnya

- Streaming audio real-time dengan [Panduan transkripsi langsung](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=id) menggunakan Live API.
- Jelajahi [Pemahaman audio](https://ai.google.dev/gemini-api/docs/audio?hl=id) untuk menganalisis, meringkas, atau membuat kueri konten audio.
- Pelajari cara menyintesis audio dari teks menggunakan [Text-to-speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id).
- Lihat [halaman Harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id#gemini-3.5-transcribe) untuk mengetahui harga model dan batas token.
- Lihat panduan [Files API](https://ai.google.dev/gemini-api/docs/files?hl=id) untuk mengetahui detail tentang cara mengupload dan mengelola file media.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-24 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-24 UTC."],[],[]]
