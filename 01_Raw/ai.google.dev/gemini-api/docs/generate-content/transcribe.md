---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/transcribe?hl=pl
fetched_at: 2026-10-26T05:43:33.175536+00:00
title: "Zapis tekstowy \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs/generate-content?hl=pl)

Prześlij opinię

# Zapis tekstowy

Interfejs Gemini API przekształca mowę w plikach audio na tekst za pomocą modelu Gemini 3.5 Transcribe (`gemini-3.5-transcribe`). Dzięki możliwościom rozumienia dźwięku Gemini zapewnia dokładną transkrypcję z automatycznym rozpoznawaniem języka, rozróżnianiem mówców, znacznikami czasu na poziomie słów i wskazówkami dotyczącymi słownictwa niestandardowego. Oferuje też tryb [inteligentnej transkrypcji](#transcription-modes), który usuwa niepłynności i inteligentnie formatuje tekst.

Aby utworzyć transkrypcję pliku audio, prześlij go i przekaż do `gemini-3.5-transcribe`:

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

## Przegląd

Gemini 3.5 Transcribe jest zoptymalizowany pod kątem zadań związanych z przekształcaniem mowy na tekst. Obsługuje różne akcenty, szumy w tle i rozmowy w wielu językach.

Najważniejsze funkcje:

- **Automatyczne rozpoznawanie mowy (ASR):** automatycznie wykrywa języki w [ponad 85 lokalizacjach](#supported-languages). Obsługuje przełączanie języków w obrębie zdania i między zdaniami bez konieczności ręcznej konfiguracji.
- **Słownictwo niestandardowe:** przekazując do 1000 fraz, możesz zwiększyć prawdopodobieństwo rozpoznania terminów, akronimów i nazw własnych związanych z określoną dziedziną.
- **Rozdzielanie rozmówców:** rozróżnia wielu rozmówców i przypisuje wypowiadane segmenty do różnych etykiet.
- **Sygnatury czasowe na poziomie słów:** generuje dokładne przesunięcia czasu rozpoczęcia i zakończenia każdego rozpoznanego słowa.
- **Inteligentna transkrypcja:** usuwa niepłynności, wypełniacze i powtórzenia oraz stosuje formatowanie strukturalne.
- **Formatowanie i normalizacja:** stosuje wielkie litery, interpunkcję i normalizację tekstu odwrotnego, np. przekształca „twenty six million dollars” na „26 mln USD”.

Jeśli chcesz uzyskać ogólne rozumowanie na podstawie treści audio lub odpowiadanie na pytania dotyczące tych treści, użyj [rozumienia dźwięku](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=pl). Do syntezy dźwięku przy zamianie tekstu na mowę użyj funkcji [Zamiana tekstu na mowę](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=pl).

## Wykrywanie języka i podpowiedzi

Domyślnie model automatycznie wykrywa język, w którym mówisz. Przełącza się między językami dynamicznie, gdy mówcy przechodzą z jednego języka na drugi.

Aby użyć automatycznego wykrywania, pomiń parametr `language_codes` lub podaj pustą listę:

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

Jeśli znasz język z wyprzedzeniem, podaj kody języka w standardzie BCP-47 w `language_codes`, aby zwiększyć dokładność transkrypcji (patrz [Obsługiwane języki](#supported-languages)):

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

## Słownictwo niestandardowe

Możesz nakierować model mowy na rzadko używane słowa, żargon techniczny, nazwy marek lub nazwy własne. Podaj w tablicy `custom_vocabulary` maksymalnie 1000 słów (najlepsze wyniki zwykle uzyskuje się w przypadku maksymalnie 100 słów):

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

## Rozdzielanie rozmówców

Rozdzielanie rozmówców identyfikuje różne głosy w nagraniu i oznacza każdy segment identyfikatorem rozmówcy, np. `spk_1` lub `spk_2`. Obsługiwanych jest maksymalnie 8 głośników (atrybucja w przypadku 3 lub więcej głośników jest eksperymentalna).

Włącz rozdzielanie rozmówców, ustawiając `diarization` na `True`:

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

## Sygnatury czasowe na poziomie słów

Sygnatury czasowe na poziomie słów podają dokładne przesunięcia początku i końca każdego rozpoznanego słowa w strumieniu audio.

Włącz znaczniki czasu, ustawiając `word_timestamp` na `True`:

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

Możesz połączyć `diarization` i `word_timestamp` w jednym żądaniu, aby otrzymać etykiety mówców i sygnatury czasowe słów:

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

## Tryby transkrypcji

Gemini 3.5 Transcribe obsługuje 2 tryby transkrypcji za pomocą parametru `mode`:

- **`VERBATIM` (domyślny):** zwraca dokładny zapis słowo w słowo wszystkiego, co zostało powiedziane, zachowując nieprzetworzone wypełniacze („um”, „uh”, „like”, „you know”), powtórzenia, pauzy i fałszywe starty. Wymagane w przypadku używania sygnatur czasowych lub podziału na mówców.
- **`SMART` (Inteligentna transkrypcja):** optymalizuje transkrypcję pod kątem czytania, stosując inteligentne przetwarzanie końcowe:
  - **Usuwanie zakłóceń:** usuwa wypełniacze, jąkanie i fałszywe starty.
  - **Korekty w tekście:** bezpośrednie rozwiązywanie problemów z korektami w wypowiedzi (np. *„Spotkajmy się we wtorek, a nie, w środę o godzinie 14:00”* staje się *„Spotkajmy się w środę o godzinie 14:00”*).
  - **Automatyczne formatowanie strukturalne:** automatycznie porządkuje wypowiadane myśli w akapitach, listach numerowanych, punktach, sformatowanych datach, walutach i liczbach.
  - **Poprawki gramatyczne:** stosuje naturalną interpunkcję, wielkie litery na początku zdania i płynność.

| Tekst mówiony | `VERBATIM` wynik | `SMART` dane wyjściowe (inteligentna transkrypcja) |
| --- | --- | --- |
| „Um, na spotkanie powinniśmy zaprosić Alicję i … nie, Roberta i Karolinę”. | „Um, na spotkanie powinniśmy zaprosić Alicję i poczekać, nie, Roberta i Karola”. | „Na spotkanie powinniśmy zaprosić Roberta i Karolinę”. |
| „First item review budget second item finalize timeline third item send recap” | „first item review budget second item finalize timeline third item send recap” | „1. Sprawdź budżet 2. Finalizacja osi czasu 3. Wyślij podsumowanie”. |

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

.

## Analizowanie danych wyjściowych transkrypcji

Pełny tekst transkrypcji jest zwracany w `response.text`.

Gdy włączona jest opcja `word_timestamp` lub `diarization`, interfejs API zwraca też szczegółowe adnotacje na poziomie słów i etykiety mówców dołączone do proponowanych części.

Oto jak wyodrębnić sygnatury czasowe słów i zmiany rozmówców oraz po nich iterować:

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
                  "endOffset": "0.400s"
                },
                {
                  "word": "world",
                  "startOffset": "0.500s",
                  "endOffset": "0.800s"
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

## Obsługiwane języki

Gemini 3.5 Transcribe obsługuje te języki i kody języków w standardzie BCP-47:

| Język | Kod BCP-47 | Język | Kod BCP-47 |
| --- | --- | --- | --- |
| afrikaans | `af-ZA` | japoński | `ja-JP` |
| amharski | `am-ET` | jawajski | `jv-ID` |
| arabski (Egipt) | `ar-EG` | kabuverdianu | `kea-CV` |
| ormiański | `hy-AM` | kannada | `kn-IN` |
| asamski | `as-IN` | kazachski | `kk-KZ` |
| azerski | `az-AZ` | koreański | `ko-KR` |
| białoruski | `be-BY` | kirgiski | `ky-KG` |
| bengalski (Bangladesz) | `bn-BD` | łotewski | `lv-LV` |
| bengalski (Indie) | `bn-IN` | lingala | `ln-CD` |
| bośniacki | `bs-BA` | litewski | `lt-LT` |
| bułgarski | `bg-BG` | macedoński | `mk-MK` |
| bułgarski (arumuński), | `rup-BG` | malajski | `ms-MY` |
| birmański | `my-MM` | malajalam | `ml-IN` |
| kantoński (tradycyjny), | `yue-Hant-HK` | maltański | `mt-MT` |
| kataloński | `ca-ES` | chiński mandaryński (uproszczony), | `cmn-Hans-CN` |
| cebuański | `ceb` | marathi | `mr-IN` |
| khmerski | `km-KH` | mongolski | `mn-MN` |
| chorwacki | `hr-HR` | nepalski | `ne-NP` |
| czeski | `cs-CZ` | norweski | `nb-NO` |
| duński | `da-DK` | orija | `or-IN` |
| niderlandzki | `nl-NL` | polski | `pl-PL` |
| angielski (Wielka Brytania) | `en-GB` | portugalski (Brazylia) | `pt-BR` |
| angielski (Indie) | `en-IN` | portugalski (Portugalia) | `pt-PT` |
| angielski (USA) | `en-US` | pendżabski | `pa-IN` |
| estoński | `et-EE` | pendżabski (pismo gurmukhi), | `pa-Guru-IN` |
| perski | `fa-IR` | rumuński | `ro-RO` |
| filipiński | `fil-PH` | rosyjski | `ru-RU` |
| fiński | `fi-FI` | serbski | `sr-RS` |
| francuski | `fr-FR` | sindhi (alfabet arabski) | `sd-Arab-IN` |
| galicyjski | `gl-ES` | słowacki | `sk-SK` |
| gruziński | `ka-GE` | słoweński | `sl-SI` |
| niemiecki | `de-DE` | hiszpański (Ameryka Łacińska) | `es-419` |
| grecki | `el-GR` | hiszpański (Stany Zjednoczone) | `es-US` |
| gudżarati | `gu-IN` | suahili (Kenia) | `sw-KE` |
| hausa | `ha-NG` | szwedzki | `sv-SE` |
| hebrajski | `he-IL` | tadżycki | `tg-TJ` |
| hindi | `hi-IN` | telugu | `te-IN` |
| węgierski | `hu-HU` | tajski | `th-TH` |
| islandzki | `is-IS` | turecki | `tr-TR` |
| indyjski angielski | `en-IN` | ukraiński | `uk-UA` |
| indonezyjski | `id-ID` | uzbecki | `uz-UZ` |
| włoski | `it-IT` | wietnamski | `vi-VN` |

## Obsługiwane formaty audio

Gemini 3.5 Transcribe obsługuje te typy MIME formatów audio:

- WAV - `audio/wav`
- MP3 – `audio/mp3`
- AIFF – `audio/aiff`
- AAC - `audio/aac`
- OGG – `audio/ogg`
- FLAC - `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16 - `audio/l16`
- Opus – `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM – `audio/webm`

Pełną listę obsługiwanych typów MIME i schematów parametrów znajdziesz w [dokumentacji interfejsu Interactions API](https://ai.google.dev/api/interactions-api?hl=pl#Resource:Content).

## Dodatkowe materiały o tym parametrze

Skonfiguruj transkrypcję, ustawiając pola w obiekcie `audio_transcription_config` w `GenerateContentConfig`:

| Pole | Typ | Opis |
| --- | --- | --- |
| `language_codes` | Tablica ciągów znaków | Kody języków w standardzie BCP-47 (np. `["en-US"]`). Jeśli ten parametr zostanie pominięty lub będzie pusty (`[]`), model automatycznie wykryje język i obsłuży przełączanie kodu. |
| `custom_vocabulary` | Tablica ciągów znaków | Maksymalnie 1000 niestandardowych terminów, akronimów lub nazw własnych, które mają wpływać na rozpoznawanie mowy. Nie jest zgodne z rozdzielaniem rozmówców ani sygnaturami czasowymi na poziomie słów. |
| `word_timestamp` | Wartość logiczna | Ustaw na `True`, aby uwzględnić przesunięcia początku i końca słowa. Jeśli ten parametr zostanie pominięty lub będzie miał wartość `False`, sygnatury czasowe słów nie będą zwracane. Niezgodne ze słownikiem niestandardowym. |
| `diarization` | Wartość logiczna | Ustaw na `True`, aby identyfikować poszczególnych rozmówców i oznaczać ich etykietami. Niezgodne ze słownikiem niestandardowym. |
| `mode` | Ciąg znaków | Tryb transkrypcji. Obsługiwane wartości: `"VERBATIM"` (domyślna) i `"SMART"`. Brak zgodności z sygnaturami czasowymi i podziałem na mówców. |

## Sprawdzone metody

- **Zapewnij czysty dźwięk:** zadbaj o to, aby nagrania audio miały wyraźnie oddzielone głosy i unikaj poważnego obcinania dźwięku.
- **Podaj wskazówki dotyczące języka, jeśli jest on znany:** jeśli znasz język dźwięku, podaj `language_codes`, aby zmaksymalizować dokładność.
- **Kierowanie na niestandardowy słownik:** w `custom_vocabulary` umieszczaj tylko unikalne terminy związane z domeną, nazwy marek lub rzeczowniki własne, a nie powszechnie używane słowa.
- **Używaj interfejsu Files API w przypadku długich nagrań:** w przypadku plików trwających dłużej niż kilka sekund prześlij plik za pomocą `client.files.upload` i przekaż zwrócony plik do treści modelu.

## Ograniczenia

- **Czas trwania dźwięku:** standardowe żądania unarne obsługują pliki audio o czasie trwania do 1 godziny. Przetwarzanie dźwięku jest ograniczone do 30 minut, gdy włączone są funkcje takie jak rozdzielanie rozmówców czy sygnatury czasowe na poziomie słów.
- **Sygnatury czasowe na poziomie słów:** włączenie sygnatur czasowych na poziomie słów może obniżyć ogólną dokładność transkrypcji.
- **Rozdzielanie rozmówców:** rozdzielanie rozmówców obsługuje maksymalnie 8 osób. Przypisywanie mówców w przypadku co najmniej 3 osób jest funkcją eksperymentalną.
- **Słownictwo niestandardowe:** możesz podać maksymalnie 1000 terminów w `custom_vocabulary`, ale najlepsze wyniki zwykle uzyskuje się w przypadku maksymalnie 100 terminów. Nie możesz łączyć `custom_vocabulary` z diaryzacją mówców ani sygnaturami czasowymi na poziomie słowa. Interfejs API odrzuca żądania, w których `custom_vocabulary` występuje razem z którąś z tych funkcji.
- **Zgodność trybów:** inteligentna transkrypcja (`mode: "SMART"`) nie może być łączona z `word_timestamp` ani `diarization`.

## Co dalej?

- Przesyłaj strumieniowo dźwięk w czasie rzeczywistym za pomocą [przewodnika po transkrypcji na żywo](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=pl), korzystając z interfejsu Live API.
- Poznaj [rozumienie dźwięku](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=pl), aby analizować, podsumowywać lub wyszukiwać treści audio.
- Dowiedz się, jak zsyntetyzować plik audio z tekstu za pomocą [zamiany tekstu na mowę](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=pl).
- Ceny modeli i limity tokenów znajdziesz na [stronie z cennikiem](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#gemini-3.5-transcribe).
- Szczegółowe informacje o przesyłaniu plików multimedialnych i zarządzaniu nimi znajdziesz w przewodniku po [interfejsie Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-23 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-23 UTC."],[],[]]
