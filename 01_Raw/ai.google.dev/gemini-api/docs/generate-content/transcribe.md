---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/transcribe?hl=it
fetched_at: 2026-09-21T05:46:06.644986+00:00
title: "Trascrizione audio \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs/generate-content?hl=it)

Invia feedback

# Trascrizione audio

L'API Gemini converte il parlato nei file audio in testo utilizzando il modello Gemini 3.5 Transcribe (`gemini-3.5-transcribe`). Grazie alle funzionalità di comprensione audio di Gemini, offre una trascrizione accurata con identificazione automatica della lingua, diarizzazione degli oratori, timestamp a livello di parola e suggerimenti per il vocabolario personalizzato. Offre anche una modalità di [trascrizione intelligente](#transcription-modes) con rimozione delle disfluenze e formattazione intelligente.

Per trascrivere un file audio, caricalo e passalo a `gemini-3.5-transcribe`:

### Python

```
from google import genai

client = genai.Client()

audio_file = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const audioFile = await ai.files.upload({
  file: "path/to/sample.mp3",
  mimeType: "audio/mp3",
});

const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
});

console.log(response.text);
```

### REST

```
# First upload the file via the Files API, then pass its URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ]
  }'
```

## Panoramica

Gemini 3.5 Transcribe è ottimizzato per le attività di sintesi vocale. Gestisce accenti diversi, rumori di fondo e conversazioni in più lingue.

Le sue funzionalità principali includono:

- **Riconoscimento vocale automatico (ASR)**: rileva automaticamente le lingue in oltre [85 impostazioni internazionali](#supported-languages). Gestisce il cambio di codice all'interno della frase e tra le frasi senza configurazione manuale.
- **Vocabolario personalizzato**:orienta il riconoscimento verso termini, acronimi e nomi propri specifici del dominio passando fino a 1000 frasi.
- **Diarizzazione degli oratori**:distingue tra più oratori e attribuisce i segmenti parlati a etichette distinte.
- **Timestamp a livello di parola**:genera offset temporali di inizio e di fine precisi per ogni parola riconosciuta.
- **Trascrizione intelligente**:elimina le disfluenze, gli intercalari e le ripetizioni e applica una formattazione strutturata.
- **Formattazione e normalizzazione**:applica maiuscole, punteggiatura e normalizzazione del testo inversa, ad esempio convertendo "ventisei milioni di dollari" in "26 milioni di $".

Per il ragionamento audio generale o la risposta a domande sui contenuti audio, utilizza [Comprensione audio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=it). Per la sintesi audio della sintesi vocale, utilizza [Text-to-Speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=it).

## Rilevamento della lingua e suggerimenti

Per impostazione predefinita, il modello rileva automaticamente la lingua parlata. Passa da una lingua all'altra in modo dinamico quando gli oratori cambiano codice.

Per utilizzare il rilevamento automatico, ometti `language_codes` o fornisci un elenco vuoto:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            language_codes=[],
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      languageCodes: [],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "languageCodes": []
      }
    }
  }'
```

Se conosci la lingua in anticipo, specifica i codici lingua BCP-47 in `language_codes` per migliorare l'accuratezza della trascrizione (vedi [Lingue supportate](#supported-languages)):

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    languageCodes: ["es-ES"],
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "languageCodes": ["es-ES"]
    }
  }
}
```

## Vocabolario personalizzato

Puoi indirizzare il modello vocale verso parole insolite, tecnicismi, nomi di brand o nomi propri. Fornisci fino a 1000 termini nell'array `custom_vocabulary` (in genere i risultati migliori si ottengono con un massimo di 100 termini):

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      customVocabulary: ["Gemini", "Kubernetes", "BigQuery"],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "customVocabulary": ["Gemini", "Kubernetes", "BigQuery"]
      }
    }
  }'
```

## Diarizzazione degli speaker

La diarizzazione degli interlocutori identifica le diverse voci nella registrazione e tagga ogni segmento con un identificatore dell'interlocutore, ad esempio `spk_1` o `spk_2`. Sono supportati fino a 8 relatori (l'attribuzione per 3 o più relatori è sperimentale).

Attiva la diarizzazione impostando `diarization` su `True`:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            diarization=True,
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      diarization: true,
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "diarization": true
      }
    }
  }'
```

## Timestamp a livello di parola

I timestamp a livello di parola forniscono offset di inizio e fine esatti per ogni parola riconosciuta nello stream audio.

Attiva i timestamp impostando `word_timestamp` su `True`:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            word_timestamp=True,
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      wordTimestamp: true,
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "wordTimestamp": true
      }
    }
  }'
```

Puoi combinare `diarization` e `word_timestamp` in un'unica richiesta per ricevere sia le etichette di chi parla sia i timestamp delle parole:

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        diarization=True,
        word_timestamp=True,
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    diarization: true,
    wordTimestamp: true,
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "diarization": true,
      "wordTimestamp": true
    }
  }
}
```

## Modalità di trascrizione

Gemini 3.5 Transcribe supporta due modalità di trascrizione tramite il parametro `mode`:

- **`VERBATIM` (predefinito)**: restituisce una trascrizione esatta parola per parola di tutto ciò che viene detto, conservando le parole di riempimento grezze ("um", "uh", "like", "you know"), le ripetizioni, le pause e le false partenze. Obbligatorio se utilizzi timestamp o la diarizzazione degli speaker.
- **`SMART` (Trascrizione intelligente)**: ottimizza la trascrizione per la lettura applicando una post-elaborazione intelligente:
  - **Rimozione delle disfluenze**: elimina le parole di riempimento, le balbuzie e i falsi inizi.
  - **Correzioni automatiche in linea**: risolve direttamente le correzioni vocali (ad esempio, *"Ci vediamo martedì, no, mercoledì alle 14:00"* diventa *"Ci vediamo mercoledì alle 14:00"*).
  - **Formattazione strutturata automatica**: struttura automaticamente i pensieri espressi in paragrafi, elenchi numerati, elenchi puntati, date, valute e numeri formattati.
  - **Pulizia grammaticale**: applica punteggiatura, maiuscole e flusso naturali.

| Audio parlato | `VERBATIM` output | Output `SMART` (Trascrizione intelligente) |
| --- | --- | --- |
| "Ehm, quindi per la riunione, penso che dovremmo invitare Alice e, no, aspetta, Roberto e Carolina." | "Allora, per la riunione penso che dovremmo invitare Alice, no, Bob e Carol." | "Per la riunione, penso che dovremmo invitare Roberto e Carla." |
| "First item review budget second item finalize timeline third item send recap" | "first item review budget second item finalize timeline third item send recap" | "1. Esamina il budget 2. Finalizza la sequenza temporale 3. Invia riepilogo" |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            mode="SMART",
        )
    ),
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      mode: "SMART",
    },
  },
});
console.log(response.text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "mode": "SMART"
      }
    }
  }'
```

## Analisi dell'output della trascrizione

Il testo completo della trascrizione viene restituito in `response.text`.

Quando `word_timestamp` o `diarization` è abilitato, l'API restituisce anche annotazioni dettagliate a livello di parola ed etichette di chi parla associate alle parti candidate.

Ecco come estrarre e scorrere i timestamp a livello di parola e i turni di parola:

### Python

```
def extract_word_transcriptions(response):
    words = []
    for candidate in getattr(response, "candidates", []) or []:
        content = getattr(candidate, "content", None)
        for part in getattr(content, "parts", []) or []:
            transcription = getattr(part, "audio_transcription", None)
            if transcription:
                speaker = getattr(transcription, "speaker_label", "")
                for word_info in getattr(transcription, "words", []) or []:
                    word = getattr(word_info, "word", "")
                    start = getattr(word_info, "start_offset", "")
                    end = getattr(word_info, "end_offset", "")
                    words.append({
                        "word": word,
                        "speaker": speaker,
                        "start_offset": start,
                        "end_offset": end,
                    })
    return words

words = extract_word_transcriptions(response)

for w in words:
    speaker = f"[{w['speaker']}] " if w["speaker"] else ""
    timing = f"({w['start_offset']} -> {w['end_offset']}) " if w["start_offset"] and w["end_offset"] else ""
    print(f"{speaker}{timing}{w['word']}")
```

### JavaScript

```
function extractWordTranscriptions(response) {
  const words = [];
  for (const candidate of response.candidates ?? []) {
    for (const part of candidate.content?.parts ?? []) {
      const transcription = part.audioTranscription;
      if (transcription) {
        const speaker = transcription.speakerLabel ?? "";
        for (const wordInfo of transcription.words ?? []) {
          words.push({
            word: wordInfo.word ?? "",
            speaker: speaker,
            startOffset: wordInfo.startOffset ?? "",
            endOffset: wordInfo.endOffset ?? "",
          });
        }
      }
    }
  }
  return words;
}

const words = extractWordTranscriptions(response);

for (const w of words) {
  const speaker = w.speaker ? `[${w.speaker}] ` : "";
  const timing = (w.startOffset && w.endOffset) ? `(${w.startOffset} -> ${w.endOffset}) ` : "";
  console.log(`${speaker}${timing}${w.word}`);
}
```

### REST

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "audioTranscription": {
              "speakerLabel": "spk_1",
              "words": [
                {
                  "word": "Hello",
                  "startOffset": "0.100s",
                  "endOffset": "0.450s"
                },
                {
                  "word": "world",
                  "startOffset": "0.500s",
                  "endOffset": "0.850s"
                }
              ]
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP"
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
| Estone | `et-EE` | Punjabi (Gurmukhi script) | `pa-Guru-IN` |
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

## Riferimento ai parametri

Configura la trascrizione impostando i campi all'interno dell'oggetto `audio_transcription_config` in `GenerateContentConfig`:

| Campo | Tipo | Descrizione |
| --- | --- | --- |
| `language_codes` | Array di stringhe | Codici lingua BCP-47 (ad es. `["en-US"]`). Se omesso o vuoto (`[]`), il modello rileva automaticamente la lingua e gestisce il cambio di codice. |
| `custom_vocabulary` | Array di stringhe | Fino a 1000 termini personalizzati, acronimi o nomi propri per favorire il riconoscimento vocale. Non compatibile con la diarizzazione degli interlocutori e i timestamp a livello di parola. |
| `word_timestamp` | Booleano | Imposta su `True` per includere gli offset di inizio e fine delle parole. Se omesso o `False`, non vengono restituiti timestamp delle parole. Incompatibile con il vocabolario personalizzato. |
| `diarization` | Booleano | Imposta su `True` per identificare ed etichettare i diversi interlocutori. Incompatibile con il vocabolario personalizzato. |
| `mode` | Stringa | Modalità di trascrizione. Valori supportati: `"VERBATIM"` (predefinito) e `"SMART"`. Incompatibile con i timestamp e la diarizzazione. |

## Best practice

- **Fornisci audio pulito**:assicurati che le registrazioni audio abbiano una separazione vocale chiara ed evita il clipping eccessivo.
- **Fornisci suggerimenti sulla lingua quando è nota**:se conosci la lingua dell'audio in anticipo, specifica `language_codes` per massimizzare l'accuratezza.
- **Vocabolario personalizzato di destinazione**:includi in `custom_vocabulary` solo termini di dominio, nomi di brand o nomi propri distinti, anziché parole comuni di uso quotidiano.
- **Utilizza l'API Files per le registrazioni di grandi dimensioni**:per i file più lunghi di pochi secondi, carica il file utilizzando `client.files.upload` e passa il file restituito ai contenuti del modello.

## Limitazioni

- **Durata audio**:le richieste unarie standard supportano file audio fino a 1 ora. L'elaborazione audio è limitata a 30 minuti quando sono attive funzionalità come la diarizzazione degli interlocutori o i timestamp a livello di parola.
- **Timestamp a livello di parola:** l'attivazione dei timestamp a livello di parola potrebbe ridurre l'accuratezza complessiva della trascrizione.
- **Diarizzazione degli interlocutori**:la diarizzazione degli interlocutori supporta fino a 8 interlocutori. L'attribuzione degli oratori per 3 o più oratori è sperimentale.
- **Vocabolario personalizzato**:puoi fornire fino a 1000 termini in `custom_vocabulary`, ma in genere i risultati migliori si ottengono con un massimo di 100 termini. Non puoi combinare `custom_vocabulary` con la diarizzazione degli oratori o i timestamp a livello di parola; l'API rifiuta le richieste che specificano `custom_vocabulary` insieme a una delle due funzionalità.
- **Compatibilità delle modalità**:la trascrizione intelligente (`mode: "SMART"`) non può essere combinata con `word_timestamp` o `diarization`.

## Passaggi successivi

- Trasmetti audio in tempo reale con la [guida alla trascrizione in tempo reale](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=it) utilizzando l'API Live.
- Esplora la sezione [Comprensione dell'audio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=it) per analizzare, riepilogare o interrogare i contenuti audio.
- Scopri come sintetizzare l'audio dal testo utilizzando [Text-to-Speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=it).
- Consulta la [pagina dei prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#gemini-3.5-transcribe) per i prezzi dei modelli e i limiti dei token.
- Consulta la guida all'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it) per informazioni dettagliate sul caricamento e sulla gestione dei file multimediali.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-08 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-08 UTC."],[],[]]
