---
source_url: https://ai.google.dev/gemini-api/docs/transcribe?hl=pl
fetched_at: 2026-08-31T06:41:18.740556+00:00
title: "Zapis tekstowy \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)

Prześlij opinię

# Zapis tekstowy

Interfejs Gemini API przekształca mowę w plikach audio na tekst za pomocą modelu Gemini 3.5 Transcribe (`gemini-3.5-transcribe`). Dzięki możliwościom Gemini w zakresie rozumienia dźwięku zapewnia dokładną transkrypcję z automatycznym rozpoznawaniem języka, podziałem na mówców, znacznikami czasu na poziomie słów i wskazówkami dotyczącymi słownictwa niestandardowego. Oferuje też tryb [inteligentnej transkrypcji](#transcription-modes), który usuwa niepłynności i inteligentnie formatuje tekst.

Aby utworzyć transkrypcję pliku audio, prześlij go i przekaż do `gemini-3.5-transcribe`:

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

## Przegląd

Gemini 3.5 Transcribe jest zoptymalizowany pod kątem zadań związanych z przekształcaniem mowy na tekst. Obsługuje różne akcenty, szumy w tle i rozmowy w wielu językach.

Najważniejsze funkcje:

- **Automatyczne rozpoznawanie mowy (ASR):** automatycznie wykrywa języki w [ponad 85 lokalizacjach](#supported-languages). Obsługuje przełączanie języków w obrębie zdania i między zdaniami bez konieczności ręcznej konfiguracji.
- **Słownictwo niestandardowe:** przekazując do 1000 frazeologizmów, możesz zwiększyć dokładność rozpoznawania terminów, akronimów i nazw własnych związanych z określoną dziedziną.
- **Rozpoznawanie rozmówców:** rozróżnia poszczególnych rozmówców i przypisuje wypowiadane przez nich segmenty do różnych etykiet.
- **Sygnatury czasowe na poziomie słów:** generuje dokładne przesunięcia czasu początków i końców każdego rozpoznanego słowa.
- **Inteligentna transkrypcja:** usuwa niepłynności, wypełniacze i powtórzenia oraz stosuje formatowanie strukturalne.
- **Formatowanie i normalizacja:** stosuje wielkie litery, interpunkcję i normalizację tekstu odwrotnego, np. przekształca „twenty six million dollars” na „26 mln USD”.

Jeśli chcesz uzyskać ogólne rozumowanie na podstawie treści audio lub odpowiadanie na pytania dotyczące tych treści, użyj [rozumienia dźwięku](https://ai.google.dev/gemini-api/docs/audio?hl=pl). Do syntezy dźwięku przy zamianie tekstu na mowę użyj funkcji [Zamiana tekstu na mowę](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl).

## Wykrywanie języka i podpowiedzi

Domyślnie model automatycznie wykrywa język, w którym mówisz. Przełącza się między językami dynamicznie, gdy mówcy przechodzą z jednego języka na drugi.

Aby użyć automatycznego wykrywania, pomiń parametr `language_codes` lub podaj pustą listę:

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

Jeśli znasz język z wyprzedzeniem, podaj kody języka w standardzie BCP-47 w `language_codes`, aby zwiększyć dokładność transkrypcji (patrz [Obsługiwane języki](#supported-languages)):

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

## Słownictwo niestandardowe

Możesz nakierować model mowy na rzadko używane słowa, żargon techniczny, nazwy marek lub nazwy własne. Podaj w tablicy `custom_vocabulary` maksymalnie 1000 słów (najlepsze wyniki zwykle uzyskuje się w przypadku maksymalnie 100 słów):

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

## Rozdzielanie rozmówców

Rozdzielanie rozmówców identyfikuje różne głosy w nagraniu i oznacza każdy segment identyfikatorem rozmówcy, np. `spk_1` lub `spk_2`. Obsługiwanych jest maksymalnie 8 głośników (atrybucja w przypadku 3 lub więcej głośników jest eksperymentalna).

Włącz rozdzielanie rozmówców, konfigurując `diarization_mode` w obszarze `mode`:

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

## Sygnatury czasowe na poziomie słów

Sygnatury czasowe na poziomie słów podają dokładne przesunięcia początku i końca każdego rozpoznanego słowa w strumieniu audio.

Włącz sygnatury czasowe, konfigurując `timestamp_granularities` w sekcji `mode`:

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

Możesz połączyć `diarization_mode` i `timestamp_granularities` w `mode`, aby otrzymywać zarówno etykiety rozmówców, jak i sygnatury czasowe słów:

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

## Tryby transkrypcji

Gemini 3.5 Transcribe obsługuje 2 tryby transkrypcji za pomocą parametru `mode`:

- **`verbatim` (domyślny):** zwraca dokładny zapis słowo w słowo wszystkiego, co zostało powiedziane, zachowując nieprzetworzone wypełniacze („um”, „uh”, „like”, „you know”), powtórzenia, pauzy i fałszywe starty. W tym trybie (`{"type": "verbatim", ...}`) konfiguruje się sygnatury czasowe i rozdzielanie rozmówców.
- **`smart` (Inteligentna transkrypcja):** optymalizuje transkrypcję pod kątem czytania, stosując inteligentne przetwarzanie końcowe:
  - **Usuwanie zakłóceń:** usuwa wypełniacze, jąkanie i fałszywe starty.
  - **Korekty w tekście:** bezpośrednie rozwiązywanie problemów z korektami w wypowiedzi (np. *„Spotkajmy się we wtorek, a nie, w środę o godzinie 14:00”* staje się *„Spotkajmy się w środę o godzinie 14:00”*).
  - **Automatyczne formatowanie strukturalne:** automatycznie porządkuje wypowiadane myśli w akapitach, listach numerowanych, punktach, sformatowanych datach, walutach i liczbach.
  - **Poprawki gramatyczne:** stosuje naturalną interpunkcję, wielkie litery na początku zdania i płynność.

| Tekst mówiony | `verbatim` wynik | `smart` dane wyjściowe (inteligentna transkrypcja) |
| --- | --- | --- |
| „Na spotkanie powinniśmy zaprosić Alicję i … nie, Roberta i Karolinę”. | „Um, na spotkanie powinniśmy zaprosić Alicję, nie, Roberta i Karola”. | „Na spotkanie powinniśmy zaprosić Roberta i Karolinę”. |
| „First item review budget second item finalize timeline third item send recap” | „first item review budget second item finalize timeline third item send recap” | „1. Sprawdź budżet 2. Finalizacja osi czasu 3. Wyślij podsumowanie”. |

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

## Analizowanie danych wyjściowych transkrypcji

Pełny tekst transkrypcji jest zwracany w `interaction.output_text`.

Gdy włączona jest opcja `timestamp_granularities` lub `diarization_mode`, interfejs API zwraca też szczegółowe adnotacje na poziomie słów dołączone do treści interakcji.

Oto jak wyodrębnić sygnatury czasowe słów i zmiany mówcy oraz iterować po nich:

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
| estoński | `et-EE` | pendżabski (pismo gurmukhi) | `pa-Guru-IN` |
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
- FLAC – `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16 - `audio/l16`
- Opus – `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM – `audio/webm`

Pełną listę obsługiwanych typów MIME i schematów parametrów znajdziesz w [dokumentacji interfejsu Interactions API](https://ai.google.dev/api/interactions-api?hl=pl#Resource:Content).

## Dodatkowe materiały o tym parametrze

Skonfiguruj transkrypcję, ustawiając pola w obiekcie `transcription_config` w `generation_config`:

| Pole | Typ | Opis |
| --- | --- | --- |
| `language_codes` | Tablica ciągów znaków | Kody języków w standardzie BCP-47 (np. `["en-US"]`). Jeśli ten parametr zostanie pominięty lub będzie pusty (`[]`), model automatycznie wykryje język i obsłuży przełączanie kodu. |
| `custom_vocabulary` | Tablica ciągów znaków | Maksymalnie 1000 niestandardowych terminów, akronimów lub nazw własnych, które mają wpływać na rozpoznawanie mowy. |
| `mode` | Obiekt lub ciąg znaków | Konfiguracja trybu transkrypcji. Akceptuje wartość `"smart"` lub obiekt trybu dosłownego (`{"type": "verbatim", ...}`). Domyślnie jest to transkrypcja dosłowna. |
| `mode.type` | Ciąg znaków | *(Tylko w trybie dosłownym)* Identyfikator trybu. Zawsze ustawiona na `"verbatim"`. |
| `mode.timestamp_granularities` | Tablica ciągów znaków | *(Tylko tryb dosłowny)* Szczegółowość sygnatur czasowych do zwrócenia. Przekaż `["word"]`, aby włączyć przesunięcia początku i końca słów. |
| `mode.diarization_mode` | Ciąg znaków | *(Tylko tryb dosłowny)* Tryb diaryzacji. Przekaż `"speaker"`, aby zidentyfikować poszczególnych rozmówców i oznaczyć ich etykietami. |

## Sprawdzone metody

- **Zapewnij czysty dźwięk:** zadbaj o to, aby nagrania audio miały wyraźnie oddzielone głosy i unikaj poważnego obcinania dźwięku.
- **Podaj wskazówki dotyczące języka, jeśli jest on znany:** jeśli znasz język dźwięku, podaj `language_codes`, aby zmaksymalizować dokładność.
- **Kierowanie na niestandardowy słownik:** w `custom_vocabulary` umieszczaj tylko unikalne terminy związane z domeną, nazwy marek lub rzeczowniki własne, a nie powszechnie używane słowa.
- **Używaj interfejsu Files API w przypadku długich nagrań:** w przypadku plików dłuższych niż kilka sekund prześlij plik za pomocą `client.files.upload` i przekaż zwrócony identyfikator URI pliku do modelu.

## Ograniczenia

- **Czas trwania dźwięku:** standardowe żądania unarne obsługują pliki audio o czasie trwania do 1 godziny. Przetwarzanie dźwięku jest ograniczone do 30 minut, gdy włączone są funkcje takie jak rozdzielanie rozmówców czy sygnatury czasowe na poziomie słów.
- **Sygnatury czasowe na poziomie słów:** włączenie sygnatur czasowych na poziomie słów może obniżyć ogólną dokładność transkrypcji.
- **Rozdzielanie rozmówców:** rozdzielanie rozmówców obsługuje maksymalnie 8 osób. Przypisywanie mówców w przypadku co najmniej 3 osób jest funkcją eksperymentalną.
- **Słownictwo niestandardowe:** możesz podać maksymalnie 1000 terminów w `custom_vocabulary`, ale najlepsze wyniki zwykle uzyskuje się w przypadku maksymalnie 100 terminów.
- **Zgodność trybów:** inteligentna transkrypcja (`"smart"`) nie może być łączona z `timestamp_granularities` ani `diarization_mode`.

## Co dalej?

- Przesyłaj strumieniowo dźwięk w czasie rzeczywistym za pomocą [przewodnika po transkrypcji na żywo](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=pl), korzystając z interfejsu Live API.
- Poznaj [rozumienie dźwięku](https://ai.google.dev/gemini-api/docs/audio?hl=pl), aby analizować, podsumowywać lub wyszukiwać treści audio.
- Dowiedz się, jak zsyntetyzować plik audio z tekstu za pomocą [zamiany tekstu na mowę](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl).
- Ceny modeli i limity tokenów znajdziesz na [stronie z cennikiem](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#gemini-3.5-transcribe).
- Szczegółowe informacje o przesyłaniu plików multimedialnych i zarządzaniu nimi znajdziesz w przewodniku po [interfejsie Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-08-28 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-08-28 UTC."],[],[]]
