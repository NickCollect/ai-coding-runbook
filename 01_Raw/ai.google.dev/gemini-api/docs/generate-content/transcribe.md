---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/transcribe?hl=tr
fetched_at: 2026-09-14T05:46:50.277857+00:00
title: "Ses transkripti \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/generate-content?hl=tr)

Geri bildirim gönderin

# Ses transkripti

Gemini API, Gemini 3.5 Transcribe modelini (`gemini-3.5-transcribe`) kullanarak ses dosyalarındaki konuşmaları metne dönüştürür. Gemini'ın ses anlama özelliklerine dayalı olarak otomatik dil tanımlama, konuşmacı diarizasyonu, kelime düzeyinde zaman damgaları ve özel kelime bilgisi ipuçlarıyla doğru transkriptler sunar. Ayrıca, akıcılığı bozan ifadeleri kaldırma ve akıllı biçimlendirme özelliklerine sahip bir [akıllı metne dönüştürme](#transcription-modes) modu da sunar.

Ses dosyasını metne dönüştürmek için sesi yükleyip `gemini-3.5-transcribe`'a iletin:

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

## Genel Bakış

Gemini 3.5 Transcribe, konuşmayı metne dönüştürme görevleri için optimize edilmiştir. Farklı aksanları, arka plan gürültüsünü ve çok dilli sohbetleri destekler.

Temel özellikler:

- **Otomatik konuşma tanıma (ASR):** [85'ten fazla yerel ayarda](#supported-languages) dilleri otomatik olarak algılar. Cümle içi ve cümleler arası dil değişimini manuel yapılandırma olmadan işler.
- **Özel kelime dağarcığı:** 1.000'e kadar ifade ileterek tanımayı alana özgü terimler, kısaltmalar ve özel adlar yönünde eğilim gösterir.
- **Konuşmacı diarizasyonu:** Birden fazla konuşmacı arasında ayrım yapar ve konuşulan segmentleri farklı etiketlere atfeder.
- **Kelime düzeyinde zaman damgaları:** Tanınan her kelime için tam başlangıç ve bitiş zamanı farkları oluşturur.
- **Akıllı transkripsiyon:** Konuşma akışını bozan unsurları, dolgu kelimelerini ve tekrarları temizler, yapılandırılmış biçimlendirme uygular.
- **Biçimlendirme ve normalleştirme:** Büyük harf kullanımı, noktalama ve ters metin normalleştirme (ör. "yirmi altı milyon dolar"ı "26 milyon TL"ye dönüştürme) uygular.

Ses içeriğiyle ilgili genel sesli akıl yürütme veya soru yanıtlama için [Ses anlama](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=tr)'yı kullanın. Metin okuma ses sentezi için [Text-to-Speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=tr)'i kullanın.

## Dil algılama ve ipuçları

Model, varsayılan olarak konuşulan dili otomatik olarak algılar. Konuşmacılar dil değiştirirken diller arasında dinamik olarak geçiş yapar.

Otomatik algılamayı kullanmak için `language_codes` öğesini atlayın veya boş bir liste sağlayın:

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

Dili önceden biliyorsanız transkripsiyon doğruluğunu artırmak için `language_codes` bölümünde BCP-47 dil kodlarını belirtin (bkz. [Desteklenen diller](#supported-languages)):

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

## Özel kelime dağarcığı

Konuşma modelini, nadir kullanılan kelimeler, teknik jargon, marka adları veya özel isimler yönünde kullanabilirsiniz. `custom_vocabulary` dizisine en fazla 1.000 terim sağlayın (en iyi sonuçlar genellikle 100 terime kadar olan terimlerle elde edilir):

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

## Konuşmacı ayırma

Konuşmacı diarizasyonu, kayıttaki farklı sesleri tanımlar ve her segmenti `spk_1` veya `spk_2` gibi bir konuşmacı tanımlayıcısıyla etiketler. En fazla 8 konuşmacı desteklenir (3 veya daha fazla konuşmacı için atıf deneyseldir).

`diarization` ayarını `True` olarak belirleyerek konuşmacı ayırmayı etkinleştirin:

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

## Kelime düzeyinde zaman damgaları

Kelime düzeyindeki zaman damgaları, ses akışında tanınan her kelime için tam başlangıç ve bitiş zamanlarını sağlar.

`word_timestamp` seçeneğini `True` olarak ayarlayarak zaman damgalarını etkinleştirin:

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

Hem konuşmacı etiketlerini hem de kelime zaman damgalarını almak için tek bir istekte `diarization` ve `word_timestamp` parametrelerini birleştirebilirsiniz:

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

## Metne dönüştürme modları

Gemini 3.5 Transcribe, `mode` parametresi aracılığıyla iki transkripsiyon modunu destekler:

- **`VERBATIM` (varsayılan)**: Konuşulan her şeyin kelimesi kelimesine tam transkriptini döndürür. Bu transkriptte, ham dolgu kelimeleri ("ııı", "şey", "gibi", "biliyorsunuz"), tekrarlar, duraklamalar ve yanlış başlangıçlar korunur. Zaman damgaları veya konuşmacı diarizasyonu kullanılırken gereklidir.
- **`SMART` (Akıllı transkript)**: Akıllı son işlem uygulayarak transkripti okunacak şekilde optimize eder:
  - **Aksaklıkları kaldırma**: Sohbetlerdeki dolgu kelimelerini, kekelemeleri ve yanlış başlangıçları kaldırır.
  - **Satır içi otomatik düzeltmeler**: Konuşma sırasında yapılan düzeltmeleri doğrudan çözer (örneğin, *"Salı günü buluşalım, aslında hayır, Çarşamba günü saat ikide"* ifadesi *"Çarşamba günü saat 14:00'te buluşalım"* olarak değiştirilir).
  - **Otomatik yapılandırılmış biçimlendirme**: Konuşarak ifade edilen düşünceleri otomatik olarak paragraflara, numaralandırılmış listelere, madde işaretlerine, biçimlendirilmiş tarihlere, para birimlerine ve sayılara dönüştürür.
  - **Dil bilgisi temizliği**: Doğal noktalama, cümle büyük harfi ve akış uygular.

| Seslendirilmiş içerik | `VERBATIM` çıkış | `SMART` (Akıllı transkript) çıkışı |
| --- | --- | --- |
| "Şey, toplantıya Ayşe'yi davet etmeliyiz. Hayır, Ali'yi ve Can'ı davet etmeliyiz." | "Yani toplantıya Ayşe'yi davet etmeliyiz. Hayır, Ali'yi ve Canan'ı davet etmeliyiz." | "Toplantıya Bob ve Carol'ı davet etmemiz gerektiğini düşünüyorum." |
| "İlk öğe inceleme bütçesi, ikinci öğe son zaman çizelgesi, üçüncü öğe özet gönderme" | "first item review budget second item finalize timeline third item send recap" (ilk öğe bütçesini incele, ikinci öğe zaman çizelgesini sonlandır, üçüncü öğe özeti gönder) | "1. Bütçeyi inceleyin 2. Zaman çizelgesini sonlandırma 3. Özeti gönder" |

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

## Metne dönüştürme çıktısını ayrıştırma

Transkript metninin tamamı `response.text` içinde döndürülür.

`word_timestamp` veya `diarization` etkinleştirildiğinde API, aday bölümlere eklenmiş ayrıntılı kelime düzeyinde ek açıklamaları ve konuşmacı etiketlerini de döndürür.

Kelime zaman damgalarını ve konuşmacı dönüşlerini ayıklayıp yinelemek için aşağıdaki adımları uygulayın:

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

## Desteklenen diller

Gemini 3.5 Transcribe için aşağıdaki diller ve BCP-47 dil kodları desteklenir:

| Dil | BCP-47 kodu | Dil | BCP-47 kodu |
| --- | --- | --- | --- |
| Afrikaanca | `af-ZA` | Japonca | `ja-JP` |
| Amharca | `am-ET` | Cava dili | `jv-ID` |
| Arapça (Mısır) | `ar-EG` | Kabuverdianu | `kea-CV` |
| Ermenice | `hy-AM` | Kannada | `kn-IN` |
| Assamca | `as-IN` | Kazakça | `kk-KZ` |
| Azerice | `az-AZ` | Korece | `ko-KR` |
| Belarusça | `be-BY` | Kırgızca | `ky-KG` |
| Bengalce (Bangladeş) | `bn-BD` | Letonca | `lv-LV` |
| Bengalce (Hindistan) | `bn-IN` | Lingala | `ln-CD` |
| Boşnakça | `bs-BA` | Litvanca | `lt-LT` |
| Bulgarca | `bg-BG` | Makedonca | `mk-MK` |
| Bulgarca (Aromanca) | `rup-BG` | Malayca | `ms-MY` |
| Burmaca | `my-MM` | Malayalamca | `ml-IN` |
| Kantonca (Geleneksel) | `yue-Hant-HK` | Maltaca | `mt-MT` |
| Katalanca | `ca-ES` | Mandarin Çincesi (Basitleştirilmiş) | `cmn-Hans-CN` |
| Sabuanca | `ceb` | Marathi | `mr-IN` |
| Orta Khmer | `km-KH` | Moğolca | `mn-MN` |
| Hırvatça | `hr-HR` | Nepalce | `ne-NP` |
| Çekya | `cs-CZ` | Norveççe | `nb-NO` |
| Danca | `da-DK` | Oriya dili | `or-IN` |
| Felemenkçe | `nl-NL` | Lehçe | `pl-PL` |
| İngilizce (İngiltere) | `en-GB` | Portekizce (Brezilya) | `pt-BR` |
| İngilizce (Hindistan) | `en-IN` | Portekizce (Portekiz) | `pt-PT` |
| İngilizce (ABD) | `en-US` | Pencapça | `pa-IN` |
| Estonca | `et-EE` | Pencapça (Gurmukhi alfabesi) | `pa-Guru-IN` |
| Farsça | `fa-IR` | Rumence | `ro-RO` |
| Filipince | `fil-PH` | Rusça | `ru-RU` |
| Fince | `fi-FI` | Sırpça | `sr-RS` |
| Fransızca | `fr-FR` | Sindice (Arapça alfabesi) | `sd-Arab-IN` |
| Galiçyaca | `gl-ES` | Slovakça | `sk-SK` |
| Gürcüce | `ka-GE` | Slovence | `sl-SI` |
| Almanca | `de-DE` | İspanyolca (Latin Amerika) | `es-419` |
| Greek | `el-GR` | İspanyolca (Amerika Birleşik Devletleri) | `es-US` |
| Güceratça | `gu-IN` | Swahili (Kenya) | `sw-KE` |
| Hausaca | `ha-NG` | İsveççe | `sv-SE` |
| İbranice | `he-IL` | Tacikçe | `tg-TJ` |
| Hintçe | `hi-IN` | Telugu dili | `te-IN` |
| Macarca | `hu-HU` | Tayca | `th-TH` |
| İzlandaca | `is-IS` | Türkçe | `tr-TR` |
| Hint İngilizcesi | `en-IN` | Ukraynaca | `uk-UA` |
| Endonezce | `id-ID` | Özbekçe | `uz-UZ` |
| İtalyanca | `it-IT` | Vietnamca | `vi-VN` |

## Desteklenen ses biçimleri

Gemini 3.5 Transcribe, aşağıdaki ses biçimi MIME türlerini destekler:

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

Desteklenen MIME türlerinin ve parametre şemalarının tam listesi için [Interactions API referansına](https://ai.google.dev/api/interactions-api?hl=tr#Resource:Content) bakın.

## Parametre referansı

`GenerateContentConfig` içindeki `audio_transcription_config` nesnesinde alanları ayarlayarak transkripsiyonu yapılandırın:

| Alan | Tür | Açıklama |
| --- | --- | --- |
| `language_codes` | Dize dizisi | BCP-47 dil kodları (ör. `["en-US"]`). Atlanırsa veya boş bırakılırsa (`[]`) model, dili otomatik olarak algılar ve kod değiştirmeyi yönetir. |
| `custom_vocabulary` | Dize dizisi | Konuşma tanımayı etkilemek için 1.000'e kadar özel terim, kısaltma veya özel isim. Konuşmacı ayrımı ve kelime düzeyinde zaman damgalarıyla uyumlu değildir. |
| `word_timestamp` | Boole | Kelime başlangıcı ve bitiş ofsetlerini dahil etmek için `True` olarak ayarlayın. Atlanırsa veya `False` ise kelime zaman damgaları döndürülmez. Özel kelime dağarcığıyla uyumlu değildir. |
| `diarization` | Boole | Farklı konuşmacıları tanımlayıp etiketlemek için `True` olarak ayarlayın. Özel kelime dağarcığıyla uyumlu değildir. |
| `mode` | Dize | Metne dönüştürme modu. Desteklenen değerler: `"VERBATIM"` (varsayılan) ve `"SMART"`. Zaman damgaları ve konuşmacı ayrımıyla uyumlu değildir. |

## En iyi uygulamalar

- **Net ses sağlayın:** Ses kayıtlarında net bir ses ayrımı olduğundan emin olun ve ciddi kırpmalardan kaçının.
- **Bilinen durumlarda dil ipuçları verin:** Sesin dilini önceden biliyorsanız doğruluğu en üst düzeye çıkarmak için `language_codes` belirtin.
- **Hedef özel kelime dağarcığı:** `custom_vocabulary` içinde yalnızca farklı alan terimlerini, marka adlarını veya özel adları (gündelik hayatta kullanılan yaygın kelimeler yerine) kullanın.
- **Büyük kayıtlar için Files API'yi kullanın:** Birkaç saniyeden uzun dosyaları `client.files.upload` kullanarak yükleyin ve döndürülen dosyayı model içeriklerine iletin.

## Sınırlamalar

- **Ses süresi:** Standart tekli istekler, 1 saate kadar olan ses dosyalarını destekler. Konuşmacı ayrımı veya kelime düzeyinde zaman damgaları gibi özellikler etkinleştirildiğinde ses işleme 30 dakika ile sınırlıdır.
- **Sözcük düzeyinde zaman damgaları:** Sözcük düzeyinde zaman damgalarının etkinleştirilmesi, genel transkript doğruluğunu düşürebilir.
- **Konuşmacı ayırma:** Konuşmacı ayırma özelliği en fazla 8 konuşmacıyı destekler. 3 veya daha fazla konuşmacı için konuşmacı ilişkilendirme özelliği deneyseldir.
- **Özel kelime dağarcığı:** `custom_vocabulary` içinde 1.000'e kadar terim sağlayabilirsiniz ancak en iyi sonuçlar genellikle 100 terimle elde edilir. `custom_vocabulary`, konuşmacı diarizasyonu veya kelime düzeyinde zaman damgalarıyla birlikte kullanılamaz. API, bu özelliklerden biriyle birlikte `custom_vocabulary` belirtilen istekleri reddeder.
- **Mod uyumluluğu:** Akıllı transkripsiyon (`mode: "SMART"`), `word_timestamp` veya `diarization` ile birlikte kullanılamaz.

## Sırada ne var?

- Live API'yi kullanarak [Canlı transkripsiyon kılavuzu](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=tr) ile anlık ses akışı yapın.
- Ses içeriklerini analiz etmek, özetlemek veya sorgulamak için [Ses yorumlama](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=tr)'yı keşfedin.
- [Metin okuma](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=tr) özelliğini kullanarak metinden ses sentezlemeyi öğrenin.
- Model fiyatlandırması ve jeton sınırları için [Fiyatlandırma sayfasını](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#gemini-3.5-transcribe) inceleyin.
- Medya dosyalarını yükleme ve yönetme hakkında ayrıntılı bilgi için [Files API](https://ai.google.dev/gemini-api/docs/files?hl=tr) kılavuzunu inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-08 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-08 UTC."],[],[]]
