---
source_url: https://ai.google.dev/gemini-api/docs/transcribe?hl=de
fetched_at: 2026-09-21T05:50:43.621049+00:00
title: "Audiotranskript \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Audiotranskript

Die Gemini API wandelt Sprache in Audiodateien mit dem Gemini 3.5 Transcribe-Modell (`gemini-3.5-transcribe`) in Text um. Dank der Audio-Analysefunktionen von Gemini bietet sie eine genaue Transkription mit automatischer Spracherkennung, Sprecherzuordnung, Zeitstempeln auf Wortebene und benutzerdefinierten Vokabelhinweisen. Außerdem gibt es einen [intelligenten Transkriptionsmodus](#transcription-modes), in dem Füllwörter entfernt und die Formatierung optimiert wird.

Wenn Sie eine Audiodatei transkribieren möchten, laden Sie die Audiodatei hoch und übergeben Sie sie an `gemini-3.5-transcribe`:

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

## Übersicht

Gemini 3.5 Transcribe ist für Speech-to-Text-Aufgaben optimiert. Sie kann mit verschiedenen Akzenten, Hintergrundgeräuschen und mehrsprachigen Unterhaltungen umgehen.

Zu den wichtigsten Funktionen gehören:

- **Automatische Spracherkennung (ASR)**: Erkennt automatisch Sprachen in [über 85 Regionen](#supported-languages). Es werden Code-Switching innerhalb und zwischen Sätzen ohne manuelle Konfiguration unterstützt.
- **Benutzerdefiniertes Vokabular**:Die Erkennung wird auf fachspezifische Begriffe, Akronyme und Eigennamen ausgerichtet, indem bis zu 1.000 Ausdrücke übergeben werden.
- **Sprecherzuordnung**:Unterscheidet zwischen mehreren Sprechern und weist gesprochene Segmente bestimmten Labels zu.
- **Zeitstempel auf Wortebene**:Generiert genaue Start- und Endzeit-Offsets für jedes erkannte Wort.
- **Intelligente Transkription**:Unflüssigkeiten, Füllwörter und Wiederholungen werden entfernt und eine strukturierte Formatierung wird angewendet.
- **Formatierung und Normalisierung**:Hier werden Großschreibung, Zeichensetzung und inverse Textnormalisierung angewendet, z. B. wird „twenty six million dollars“ in „$26M“ umgewandelt.

Wenn Sie Audioinhalte allgemein analysieren oder Fragen zu Audioinhalten beantworten lassen möchten, verwenden Sie [Audio-Analyse](https://ai.google.dev/gemini-api/docs/audio?hl=de). Für die Audiosynthese mit Text-to-Speech verwenden Sie [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de).

## Spracherkennung und Hinweise

Standardmäßig wird die gesprochene Sprache automatisch erkannt. Die Sprache wird dynamisch gewechselt, wenn die Sprecher die Sprache wechseln.

Wenn Sie die automatische Erkennung verwenden möchten, lassen Sie `language_codes` weg oder geben Sie eine leere Liste an:

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

Wenn Sie die Sprache im Voraus kennen, geben Sie BCP-47-Sprachcodes in `language_codes` an, um die Genauigkeit der Transkription zu verbessern (siehe [Unterstützte Sprachen](#supported-languages)):

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

## Benutzerdefiniertes Vokabular

Sie können das Sprachmodell auf ungewöhnliche Wörter, Fachjargon, Markennamen oder Eigennamen ausrichten. Geben Sie bis zu 1.000 Begriffe im `custom_vocabulary`-Array an. Die besten Ergebnisse werden in der Regel mit bis zu 100 Begriffen erzielt:

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

## Sprecherbestimmung

Bei der Sprecherbestimmung werden verschiedene Stimmen in der Aufnahme identifiziert und jedes Segment wird mit einer Sprecher-ID wie `spk_1` oder `spk_2` getaggt. Es werden bis zu acht Sprecher unterstützt. Die Zuordnung für drei oder mehr Sprecher ist experimentell.

Aktivieren Sie die Sprecherbestimmung, indem Sie `diarization_mode` in `mode` konfigurieren:

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

## Zeitstempel auf Wortebene

Zeitstempel auf Wortebene geben den genauen Start- und End-Offset für jedes erkannte Wort im Audio-Stream an.

Aktivieren Sie Zeitstempel, indem Sie `timestamp_granularities` in `mode` konfigurieren:

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

Sie können `diarization_mode` und `timestamp_granularities` in `mode` kombinieren, um sowohl Sprecherlabels als auch Wortzeitstempel zu erhalten:

### Python

```
generation_config = {
    "transcription_config": {
        "custom_vocabulary": ["Gemini"],
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
    custom_vocabulary: ["Gemini"],
    mode: {
      type: "verbatim",
      diarization_mode: "speaker",
      timestamp_granularities: ["word"],
    },
  },
};
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "custom_vocabulary": ["Gemini"],
      "mode": {
        "type": "verbatim",
        "diarization_mode": "speaker",
        "timestamp_granularities": ["word"]
      }
    }
  }
}
```

## Transkriptionsmodi

Gemini 3.5 Transcribe unterstützt zwei Transkriptionsmodi über den Parameter `mode`:

- **`verbatim` (Standard)**: Gibt ein exaktes Wort-für-Wort-Transkript von allem Gesprochenen zurück, wobei Füllwörter („um“, „äh“, „wie“, „du weißt schon“), Wiederholungen, Pausen und Fehlstarts beibehalten werden. In diesem Modus (`{"type": "verbatim", ...}`) werden Zeitstempel und Sprecherbestimmung konfiguriert.
- **`smart` (Smart Transcription)**: Optimiert das Transkript für die Lesbarkeit durch intelligente Nachbearbeitung:
  - **Entfernen von Füllwörtern**: Füllwörter, Stottern und Fehlstarts werden entfernt.
  - **Inline-Selbstkorrekturen**: Gesprochene Korrekturen werden direkt berücksichtigt (z. B. wird aus *„Lass uns am Dienstag treffen, nein, am Mittwoch um 14:00 Uhr“* *„Lass uns am Mittwoch um 14:00 Uhr treffen“*).
  - **Automatische strukturierte Formatierung**: Gesprochene Gedanken werden automatisch in Absätze, nummerierte Listen, Aufzählungszeichen, formatierte Datumsangaben, Währungen und Zahlen strukturiert.
  - **Grammatische Bereinigung**: Wendet natürliche Zeichensetzung, Groß- und Kleinschreibung und einen natürlichen Fluss an.

| Gesprochene Audioinhalte | `verbatim`-Ausgabe | `smart`-Ausgabe (Smart Transcription) |
| --- | --- | --- |
| „Ähm, also für die Besprechung sollten wir, äh, Alice einladen und, nein, Bob und Carol.“ | „Für die Besprechung sollten wir Alice und äh Bob und Carol einladen.“ | „Ich denke, wir sollten Bob und Carol zu dem Meeting einladen.“ |
| „First item review budget second item finalize timeline third item send recap“ (Erster Punkt: Budget prüfen, zweiter Punkt: Zeitachse fertigstellen, dritter Punkt: Zusammenfassung senden) | „first item review budget second item finalize timeline third item send recap“ (erstes Element: Budget prüfen; zweites Element: Zeitachse fertigstellen; drittes Element: Zusammenfassung senden) | "1. Prüfen Sie das Budget 2. Zeitachse fertigstellen 3. Zusammenfassung senden“ |

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

## Transkriptionsausgabe parsen

Der vollständige Transkripttext wird in `interaction.output_text` zurückgegeben.

Wenn `timestamp_granularities` oder `diarization_mode` aktiviert ist, gibt die API auch detaillierte Anmerkungen auf Wortebene zurück, die an den Interaktionsinhalt angehängt sind.

So extrahieren und durchlaufen Sie Wortzeitstempel und Sprecherwechsel:

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

## Unterstützte Sprachen

Die folgenden Sprachen und BCP-47-Sprachcodes werden für Gemini 3.5 Transcribe unterstützt:

| Sprache | BCP-47-Code | Sprache | BCP-47-Code |
| --- | --- | --- | --- |
| Afrikaans | `af-ZA` | Japanisch | `ja-JP` |
| Amharisch | `am-ET` | Javanisch | `jv-ID` |
| Arabisch (Ägypten) | `ar-EG` | Kabuverdianu | `kea-CV` |
| Armenisch | `hy-AM` | Kannada | `kn-IN` |
| Assamesisch | `as-IN` | Kasachisch | `kk-KZ` |
| Aserbaidschanisch | `az-AZ` | Koreanisch | `ko-KR` |
| Belarussisch | `be-BY` | Kirgisisch | `ky-KG` |
| Bengalisch (Bangladesch) | `bn-BD` | Lettisch | `lv-LV` |
| Bengalisch (Indien) | `bn-IN` | Lingala | `ln-CD` |
| Bosnisch | `bs-BA` | Litauisch | `lt-LT` |
| Bulgarisch | `bg-BG` | Mazedonisch | `mk-MK` |
| Bulgarisch (Aromanisch) | `rup-BG` | Malaiisch | `ms-MY` |
| Burmesisch | `my-MM` | Malayalam | `ml-IN` |
| Kantonesisch (traditionell) | `yue-Hant-HK` | Maltesisch | `mt-MT` |
| Katalanisch | `ca-ES` | Chinesisch (Mandarin, vereinfacht) | `cmn-Hans-CN` |
| Cebuano | `ceb` | Marathi | `mr-IN` |
| Standard-Khmer | `km-KH` | Mongolisch | `mn-MN` |
| Kroatisch | `hr-HR` | Nepalesisch | `ne-NP` |
| Tschechien | `cs-CZ` | Norwegisch | `nb-NO` |
| Dänisch | `da-DK` | Oriya | `or-IN` |
| Niederländisch | `nl-NL` | Polnisch | `pl-PL` |
| Englisch (Vereinigtes Königreich) | `en-GB` | Portugiesisch (Brasilien) | `pt-BR` |
| Englisch (Indien) | `en-IN` | Portugiesisch (Portugal) | `pt-PT` |
| Englisch (USA) | `en-US` | Punjabi | `pa-IN` |
| Estnisch | `et-EE` | Panjabi (Gurmukhi-Schrift) | `pa-Guru-IN` |
| Farsi | `fa-IR` | Rumänisch | `ro-RO` |
| Filipino | `fil-PH` | Russisch | `ru-RU` |
| Finnisch | `fi-FI` | Serbisch | `sr-RS` |
| Französisch | `fr-FR` | Sindhi (arabische Schrift) | `sd-Arab-IN` |
| Galizisch | `gl-ES` | Slowakisch | `sk-SK` |
| Georgisch | `ka-GE` | Slowenisch | `sl-SI` |
| Deutsch | `de-DE` | Spanisch (Lateinamerika) | `es-419` |
| Griechisch | `el-GR` | Spanisch (USA) | `es-US` |
| Gujarati | `gu-IN` | Swahili (Kenia) | `sw-KE` |
| Hausa | `ha-NG` | Schwedisch | `sv-SE` |
| Hebräisch | `he-IL` | Tadschikisch | `tg-TJ` |
| Hindi | `hi-IN` | Telugu | `te-IN` |
| Ungarisch | `hu-HU` | Thailändisch | `th-TH` |
| Isländisch | `is-IS` | Türkisch | `tr-TR` |
| Indisches Englisch | `en-IN` | Ukrainisch | `uk-UA` |
| Indonesisch | `id-ID` | Usbekisch | `uz-UZ` |
| Italienisch | `it-IT` | Vietnamesisch | `vi-VN` |

## Unterstützte Audioformate

Gemini 3.5 Transcribe unterstützt die folgenden MIME-Typen für Audioformate:

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF – `audio/aiff`
- AAC - `audio/aac`
- OGG - `audio/ogg`
- FLAC - `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16 – `audio/l16`
- Opus – `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM - `audio/webm`

Eine vollständige Liste der unterstützten MIME-Typen und Parameterschemas finden Sie in der [Interactions API-Referenz](https://ai.google.dev/api/interactions-api?hl=de#Resource:Content).

## Parameterverweis

Konfigurieren Sie die Transkription, indem Sie Felder im `transcription_config`-Objekt in `generation_config` festlegen:

| Feld | Typ | Beschreibung |
| --- | --- | --- |
| `language_codes` | String-Array | BCP-47-Sprachcodes (z.B. `["en-US"]`). Wenn dieser Parameter weggelassen oder leer ist (`[]`), erkennt das Modell die Sprache automatisch und verarbeitet Sprachwechsel. |
| `custom_vocabulary` | String-Array | Bis zu 1.000 benutzerdefinierte Begriffe, Akronyme oder Eigennamen, um die Spracherkennung zu optimieren. |
| `mode` | Objekt oder String | Konfiguration des Transkriptionsmodus. Akzeptiert `"smart"` oder ein Objekt im Wortlautmodus (`{"type": "verbatim", ...}`). Die Standardeinstellung ist die wortgetreue Transkription. |
| `mode.type` | String | *(Nur Modus „Wort für Wort“)* Modus-ID. Immer auf `"verbatim"` gesetzt. |
| `mode.timestamp_granularities` | String-Array | *(Nur wortwörtlicher Modus)* Granularität der zurückzugebenden Zeitstempel. Übergeben Sie `["word"]`, um den zeitlichen Versatz für Wortanfang und ‑ende zu aktivieren. |
| `mode.diarization_mode` | String | *(Nur wortwörtlicher Modus)* Diarisierungsmodus. Übergeben Sie `"speaker"`, um verschiedene Sprecher zu identifizieren und mit Labels zu versehen. |

## Best Practices

- **Saubere Audioinhalte bereitstellen**:Achten Sie darauf, dass die Sprachaufnahmen klar getrennt sind und es nicht zu starkem Clipping kommt.
- **Sprachhinweise angeben, wenn bekannt**:Wenn Sie die Sprache des Audios im Voraus kennen, geben Sie `language_codes` an, um die Genauigkeit zu maximieren.
- **Benutzerdefiniertes Vokabular für das Zielvorhaben**:Verwenden Sie in `custom_vocabulary` nur eindeutige Fachbegriffe, Markennamen oder Eigennamen und keine gängigen Alltagswörter.
- **Files API für lange Aufnahmen verwenden**:Bei Dateien, die länger als einige Sekunden sind, laden Sie die Datei mit `client.files.upload` hoch und übergeben Sie den zurückgegebenen Datei-URI an das Modell.

## Beschränkungen

- **Audiodauer**:Standardmäßige unäre Anfragen unterstützen Audiodateien mit einer Länge von bis zu einer Stunde. Die Audioverarbeitung ist auf 30 Minuten begrenzt, wenn Funktionen wie die Sprecherbestimmung oder Zeitstempel auf Wortebene aktiviert sind.
- **Zeitstempel auf Wortebene**:Wenn Sie Zeitstempel auf Wortebene aktivieren, kann sich die allgemeine Transkriptionsgenauigkeit verschlechtern.
- **Sprecherbestimmung**:Die Sprecherbestimmung unterstützt bis zu 8 Sprecher. Die Sprecherzuordnung für mindestens drei Sprecher ist eine experimentelle Funktion.
- **Benutzerdefiniertes Vokabular**:Sie können bis zu 1.000 Begriffe in `custom_vocabulary` angeben. Die besten Ergebnisse werden jedoch in der Regel mit bis zu 100 Begriffen erzielt.
- **Moduskompatibilität**:Die intelligente Transkription (`"smart"`) kann nicht mit `timestamp_granularities` oder `diarization_mode` kombiniert werden.

## Nächste Schritte

- Mit der Live API können Sie Audio in Echtzeit streamen. Eine Anleitung dazu finden Sie im [Leitfaden zur Live-Transkription](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=de).
- Mit [Audio-Analyse](https://ai.google.dev/gemini-api/docs/audio?hl=de) können Sie Audioinhalte analysieren, zusammenfassen oder abfragen.
- Hier erfahren Sie, wie Sie mit [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de) Audioinhalte aus Text synthetisieren.
- Informationen zu Modellpreisen und Tokenlimits finden Sie auf der [Seite „Preise“](https://ai.google.dev/gemini-api/docs/pricing?hl=de#gemini-3.5-transcribe).
- Weitere Informationen zum Hochladen und Verwalten von Media-Dateien finden Sie im [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de)-Leitfaden.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-08-28 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-08-28 (UTC)."],[],[]]
