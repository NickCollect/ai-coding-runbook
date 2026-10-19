---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=tr
fetched_at: 2026-10-19T05:41:24.825952+00:00
title: "Metin okuma \u00fcretimi (TTS) \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hemen oynayabilirsiniz. [Deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=tr).

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/generate-content?hl=tr)

Geri bildirim gönderin

# Metin okuma üretimi (TTS)

Gemini API, Gemini'ın metin okuma (TTS) özelliklerini kullanarak metin girişini tek konuşmacılı veya çok konuşmacılı sese dönüştürebilir.
Metin okuma özelliği *[kontrol edilebilir](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=tr#controllable)*. Yani sesin *stilini*, *aksanını*, *hızını* ve *tonunu* yönlendirmek için yapılandırılmış sıra meta verilerini (`speech_metadata`) ve satır içi ses etiketlerini birleştirebilirsiniz.

[Google AI Studio'da deneyin](https://aistudio.google.com/generate-speech?hl=tr)

TTS özelliği, etkileşimli, yapılandırılmamış ses ve çok formatlı giriş ve çıkışlar için tasarlanmış [Live API](https://ai.google.dev/gemini-api/docs/live?hl=tr) aracılığıyla sağlanan konuşma üretiminden farklıdır. Live API, dinamik sohbet bağlamlarında mükemmel performans gösterirken Gemini API üzerinden TTS, podcast veya sesli kitap oluşturma gibi stil ve ses üzerinde ayrıntılı kontrolle tam metin okuma gerektiren senaryolar için özel olarak tasarlanmıştır.

Bu kılavuzda, [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=tr) (`gemini-3.8-flash-tts`) ve [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=tr) (`gemini-3.8-flash-lite-tts`) kullanarak metinden tek konuşmacılı ve çok konuşmacılı ses üretme adımları açıklanmaktadır.

## Başlamadan önce

[Desteklenen modeller](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=tr#supported-models) bölümünde listelenen bir Gemini TTS modeli kullandığınızdan emin olun. En iyi sonuçları elde etmek için iş yükünüze en uygun modeli seçmek üzere [Hangi model ne zaman kullanılır?](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=tr#when-to-use-which-model) başlıklı makaleyi inceleyin.

Geliştirmeye başlamadan önce [AI Studio'da Gemini TTS modellerini test etmeniz](https://aistudio.google.com/generate-speech?hl=tr) faydalı olabilir.

## Tek konuşmacılı TTS

Metni Gemini 3.8 TTS modelleriyle tek konuşmacılı sese dönüştürmek için `parts[].text` içinde bire bir transkripti iletin, `parts[].speech_metadata` içinde dönüş seviyesinde stil oluşturmayı ekleyin ve `speechConfig.voiceConfig` içinde sesinizi yapılandırın. Önceden oluşturulmuş bir ses adı, Extended Voice Library kimliği, özel [Voice Design](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=tr) kimliği (`voice_...`) veya [ses kopyalama](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=tr) kimliği (`voice_...` ya da isteğe bağlı durum bilgisiz `voicekey_...`) iletebilirsiniz.

Bu örnekte, modelden alınan çıkış sesi bir WAV dosyasına kaydedilir:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.wav
```

## Birden fazla konuşmacı içeren TTS

Birden fazla konuşmacının yer aldığı diyaloglarda, `multiSpeakerVoiceConfig.speakerVoiceConfigs` içinde `prebuiltVoiceConfig` kullanarak iki konuşmacı yapılandırın ve her diyalog sırasını ayrı bir `part` olarak iletin. `speech_metadata` ile hem `speaker` hem de isteğe bağlı sıra düzeyinde `style` belirtin:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [
            {
                "text": "How's it going today Jane?",
                "speech_metadata": {
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                },
            },
            {
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "speech_metadata": {
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                },
            },
        ],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "multi_speaker_voice_config": {
                "speaker_voice_configs": [
                    {
                        "speaker": "Joe",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Puck"}
                        },
                    },
                    {
                        "speaker": "Jane",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Kore"}
                        },
                    },
                ]
            }
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [
            {
               text: "How's it going today Jane?",
               speechMetadata: {
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               },
            },
            {
               text: 'Not too bad, how about you? Ready to test these new voices?',
               speechMetadata: {
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               },
            },
         ],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            multiSpeakerVoiceConfig: {
               speakerVoiceConfigs: [
                  {
                     speaker: 'Joe',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Puck' },
                     },
                  },
                  {
                     speaker: 'Jane',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Kore' },
                     },
                  },
               ],
            },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [
        {
          "text": "How'\''s it going today Jane?",
          "speech_metadata": {
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }
        },
        {
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "speech_metadata": {
            "speaker": "Jane",
            "style": "calm and relaxed"
          }
        }
      ]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "multiSpeakerVoiceConfig": {
          "speakerVoiceConfigs": [
            {
              "speaker": "Joe",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Puck" }
              }
            },
            {
              "speaker": "Jane",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Kore" }
              }
            }
          ]
        }
      }
    }
  }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
      base64 --decode > out.wav
```

## Meta veriler ve etiketlerle konuşma stilini kontrol etme

Gemini 3.8 TTS, `text` alanını tam olarak bir transkript olarak ele alır. Sahne talimatlarının sesli okunmasını kontrol etmek için talimatlarınızı kapsamlarına göre ayırın:

- **Sıra düzeyinde sürekli sunum (`speech_metadata.style`):** Sıranın tamamı için geçerli olan duyguları, sunum stilini, prozodiyi, hızı ve ses seviyesini `speech_metadata.style` içine ekleyin (ör. `"style": "whispered urgently"`, `"style": "out of breath"` veya `"style": "warm and enthusiastic"`).
- **Anlık etkinlikler (satır içi etiketler):** Konuşma dışı anlık ses patlamalarını veya duraklamaları, açılı parantezler kullanarak doğrudan transkriptin içine yerleştirin (ör. `"Wait... <short pause> did you hear that? <sigh>"` veya `"Excuse me <cough> as I was saying..."`).

Kapsamlı en iyi uygulamalar için [İstem kılavuzunu](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=tr#prompting-guide) inceleyin.

## Ses seçenekleri

Gemini 3.8 TTS, ses seçmek veya oluşturmak için dört yöntem sunar:

1. **Hazır stüdyo sesleri:** Aşağıdaki tabloda listelenen 30 seçilmiş ses.
2. **Genişletilmiş Ses Kitaplığı:** `client.voices.list()` (`GET /v1beta/voices`) kullanarak erişebileceğiniz, farklı dillerde, aksanlarda ve karakter arketiplerinde yüzlerce ek ses.
3. **[Ses tasarımı](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=tr):** [Google AI Studio](https://aistudio.google.com/generate-speech?hl=tr)'da doğal dildeki bir açıklamadan veya `POST /v1beta/voices` (`type="prompted"`, `CreateVoice` ve `GetVoice`'de kalıcı bir `voice_...` kimliği ve `sample_audio` WAV önizlemesi döndürür) kullanarak özel bir ses karakteri oluşturun.
4. **[Ses kopyalama](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=tr):**
   [Google AI Studio](https://aistudio.google.com/generate-speech?hl=tr)'da veya `POST /v1beta/voices` (`type="replicated"`, varsayılan olarak kalıcı `store=True` veya isteğe bağlı durum bilgisiz `store=False`) kullanarak referans ve izin sesinden bir konuşmacının sesini kopyalayın.

### Özel ses sınırları ve TTL

| Ses türü | Depolama modu | Kota / sınır | Elde tutma (TTL) |
| --- | --- | --- | --- |
| **Durumlu sesler** (`voice_...`, istemli veya kopyalanmış) | `store=True` | **Proje başına 200 ses** (istemle oluşturulan ve kopyalanan sesler arasında paylaşılır) | **Son kullanımdan itibaren 1 yıl\*** |
| **Durumsuz ses anahtarları** (`voicekey_...`, çoğaltılmış) | `store=False` | İstemci tarafından yönetilen | **7 gün** |

\* **TTL uzantısı:** 1 yıllık saklama penceresi, ses aktif olarak her kullanıldığında (sesle konuşma sentezlenerek veya remiksleme için temel ses olarak kullanılarak) sıfırlanır. 1 yıl boyunca etkinlik olmayan sesler otomatik olarak silinir.

### Önceden oluşturulmuş sesler

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** -- *Neşeli* | **Charon** -- *Bilgilendirici* |
| **Kore** -- *Firm* | **Fenrir** -- *Heyecanlı* | **Leda** -- *Genç* |
| **Orus** -- *Firma* | **Aoede** -- *Breezy* | **Callirrhoe** -- *Sakin* |
| **Autonoe** -- *Parlak* | **Enceladus** -- *Nefesli* | **Iapetus** -- *Temizle* |
| **Umbriel** -- *Rahat* | **Algieba** -- *Pürüzsüz* | **Despina** -- *Pürüzsüz* |
| **Erinome** -- *Temizle* | **Algenib** -- *Gravelly* | **Rasalgethi** -- *Bilgilendirici* |
| **Laomedeia** -- *Neşeli* | **Achernar** -- *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *Yetişkin* | **Pulcherrima** -- *Hevesli* |
| **Achird** -- *Arkadaşça* (Friendly) | **Zubenelgenubi** -- *Gündelik* | **Vindemiatrix** -- *Nazik* |
| **Sadachbia** -- *Lively* | **Sadaltager** -- *Bilgili* | **Sulafat** -- *Sıcak* |

### Genişletilmiş Ses Kitaplığı ve filtreleme

Yukarıdaki tabloda yer alan 30 Studio sesine ek olarak **Genişletilmiş Ses Kitaplığı**'nda diller, bölgesel aksanlar, karakter kişilikleri ve alanlar genelinde yüzlerce ek ses bulunur. [Google AI Studio](https://aistudio.google.com/generate-speech?hl=tr)'da Ses Kitaplığı'nın tamamına göz atabilir, filtreleyebilir ve etkileşimli olarak dinleyebilirsiniz. Alternatif olarak, `client.voices.list()` (`GET /v1beta/voices`, `google-genai` 2.25.0+ / `@google/genai` 2.24.0+) kullanarak programatik olarak sorgulayabilirsiniz.

`ListVoices`, filtre ölçütlerinize uyan hazır katalog seslerinden sonra özel olarak saklanan seslerinizi (en yeni ilk sırada olacak şekilde) döndürür. Bir liste filtresi için birden fazla değer iletildiğinde, bu filtredeki **herhangi** bir değerle eşleşen Voice Match'ler döndürülür (`OR`). Farklı filtre parametreleri ise `AND` ile birleştirilir:

| Parametre | Tür | Açıklama |
| --- | --- | --- |
| `language_code` | `list[str]` | BCP-47 dil etiketleri (ör. `["en-US", "en-GB"]`). Büyük/küçük harfe duyarlı olmayan tam eşleme. |
| `region_code` | `list[str]` | ISO 3166-1 alfa-2 veya UN M.49 bölge kodları (örneğin, `["US", "GB"]`). |
| `accent` | `list[str]` | Bölgesel aksan tanımlayıcıları (ör. `["American", "British"]`). |
| `gender` | `list[str]` | Algılanan cinsiyet sunumu (`"female"`, `"male"` veya `"neutral"`). |
| `pitch` | `list[str]` | Ses perdesi sınıflandırması (`"low"`, `"medium"` veya `"high"`). |
| `persona` | `list[str]` | Ses karakteri veya karakter arketipi (ör. `["Warm, Friendly"]`, `["Narrator"]`). |
| `contexts` (`context` REST'te) | `list[str]` | Optimum kullanım alanı (ör. `["Audiobook", "Conversational", "News"]`). |
| `type` (`type_` Python'da) | `list[str]` | Ses kaynağına göre filtreleyin: `"prebuilt"`, `"prompted"` ([Ses tasarımı](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=tr)) veya `"replicated"` ([Ses kopyalama](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=tr)). |
| `search` | `str` | Serbest metin alt dizesi araması, büyük/küçük harfe duyarlı olmadan hem `display_name` hem de `description` ile eşleşti. |
| `page_size` | `int` | Sayfa başına döndürülen maksimum ses sayısı (varsayılan `50`, maksimum `1000`). |
| `page_token` | `str` | Sonraki sonuç sayfasını getirmek için `response.next_page_token` kullanılan jeton. |

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

## Desteklenen diller

TTS modelleri, giriş dilini otomatik olarak algılar.
[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=tr)
(`gemini-3.8-flash-tts`) **130'dan fazla dili**, [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=tr)
(`gemini-3.8-flash-lite-tts`) ise **100'den fazla dili** destekler:

| Dil | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| Açece (Arap alfabesi) | ✔️ | ✔️ |
| Afrikaanca | ✔️ | ✔️ |
| Akan | ✔️ | ✔️ |
| Amharca | ✔️ | ✔️ |
| Ermenice | ✔️ | ✔️ |
| Assamca | ✔️ | ✔️ |
| Awadhi | ✔️ | ✔️ |
| Bali dili | ✔️ | ✔️ |
| Bengalce | ✔️ | ✔️ |
| Banjar (Arap alfabesi) | ✔️ | — |
| Banjar (Latin alfabesi) | ✔️ | ✔️ |
| Başkurtça | ✔️ | — |
| Baskça | ✔️ | ✔️ |
| Belarusian | ✔️ | ✔️ |
| Bemba | ✔️ | — |
| Bhojpuri | ✔️ | ✔️ |
| Boşnakça | ✔️ | ✔️ |
| Bugi | ✔️ | ✔️ |
| Bulgarca | ✔️ | ✔️ |
| Burmaca | ✔️ | — |
| Kantonca | ✔️ | ✔️ |
| Katalanca | ✔️ | ✔️ |
| Sabuanca | ✔️ | ✔️ |
| Orta Kürtçe | ✔️ | ✔️ |
| Chhattisgarhi | ✔️ | ✔️ |
| Çince (Basitleştirilmiş alfabe) | ✔️ | ✔️ |
| Çince (Hant alfabesi) | ✔️ | ✔️ |
| Kırım Tatarcası | ✔️ | — |
| Hırvatça | ✔️ | ✔️ |
| Çekya | ✔️ | ✔️ |
| Danca | ✔️ | ✔️ |
| Felemenkçe | ✔️ | ✔️ |
| Dyula dili | ✔️ | — |
| Dzongka | ✔️ | — |
| Arapça (Mısır) | ✔️ | ✔️ |
| İngilizce | ✔️ | ✔️ |
| Estonca | ✔️ | ✔️ |
| Filipince | ✔️ | ✔️ |
| Fince | ✔️ | — |
| Fransızca | ✔️ | ✔️ |
| Galiçyaca | ✔️ | ✔️ |
| Ganda | ✔️ | ✔️ |
| Gürcüce | ✔️ | ✔️ |
| Almanca | ✔️ | ✔️ |
| Greek | ✔️ | ✔️ |
| Guarani | ✔️ | — |
| Güceratça | ✔️ | ✔️ |
| Haiti Creole Dili | ✔️ | ✔️ |
| Halh Moğolcası | ✔️ | ✔️ |
| Hausaca | ✔️ | ✔️ |
| İbranice | ✔️ | ✔️ |
| Hintçe | ✔️ | ✔️ |
| Macarca | ✔️ | ✔️ |
| İzlandaca | ✔️ | ✔️ |
| İgbo Dili | ✔️ | — |
| İloko | ✔️ | ✔️ |
| Endonezce | ✔️ | ✔️ |
| İran Farsçası | ✔️ | ✔️ |
| İtalyanca | ✔️ | ✔️ |
| Japonca | ✔️ | ✔️ |
| Cava dili | ✔️ | ✔️ |
| Kabyle | ✔️ | — |
| Kamba | ✔️ | ✔️ |
| Kannada | ✔️ | ✔️ |
| Keşmirce (Arap alfabesi) | ✔️ | ✔️ |
| Keşmirce (Devanagari alfabesi) | ✔️ | ✔️ |
| Kazakça | ✔️ | ✔️ |
| Kmerce | ✔️ | ✔️ |
| Kikuyu | ✔️ | ✔️ |
| Ruandaca | ✔️ | ✔️ |
| Kongo | ✔️ | ✔️ |
| Korece | ✔️ | ✔️ |
| Kırgızca | ✔️ | ✔️ |
| Laoca | ✔️ | ✔️ |
| Latgalian | ✔️ | — |
| Lingala | ✔️ | ✔️ |
| Litvanca | ✔️ | — |
| Luxembourgish | ✔️ | — |
| Makedonca | ✔️ | ✔️ |
| Magahi | ✔️ | ✔️ |
| Maithili dili | ✔️ | ✔️ |
| Malayalamca | ✔️ | ✔️ |
| Maltaca | ✔️ | ✔️ |
| Manipuri | ✔️ | ✔️ |
| Marathi | ✔️ | ✔️ |
| Minangkabau (Arap alfabesi) | ✔️ | ✔️ |
| Minangkabau (Latin alfabesi) | ✔️ | — |
| Mizo | ✔️ | ✔️ |
| Nepalce (bireysel dil) | ✔️ | ✔️ |
| Nijerya'da konuşulan Fulfulde dili | ✔️ | ✔️ |
| Kuzey Azerice | ✔️ | ✔️ |
| Kuzey Sotho dili | ✔️ | ✔️ |
| Kuzey Özbekistan | ✔️ | ✔️ |
| Norveççe Bokmål | ✔️ | ✔️ |
| Yeni Norveççe | ✔️ | ✔️ |
| Nyanja | ✔️ | ✔️ |
| Occitan dili | ✔️ | — |
| Odiya (bireysel dil) | ✔️ | ✔️ |
| Pangasinan | ✔️ | — |
| Farsça (Afganistan) | ✔️ | ✔️ |
| Lehçe | ✔️ | ✔️ |
| Portekizce | ✔️ | ✔️ |
| Pencapça | ✔️ | ✔️ |
| Rumence | ✔️ | ✔️ |
| Rusça | ✔️ | ✔️ |
| Santali | ✔️ | ✔️ |
| Sırpça | ✔️ | ✔️ |
| Sindice | ✔️ | — |
| Seylanca | ✔️ | ✔️ |
| Slovakça | ✔️ | ✔️ |
| Slovence | ✔️ | — |
| Somalice | ✔️ | — |
| Güney Azerice | ✔️ | ✔️ |
| Güney Peştucası | ✔️ | ✔️ |
| Güney Sotho dili | ✔️ | — |
| İspanyolca | ✔️ | ✔️ |
| Standart Arapça (Arap alfabesi) | ✔️ | ✔️ |
| Standart Arapça (Latin alfabesi) | ✔️ | ✔️ |
| Standart Letonca | ✔️ | ✔️ |
| Standart Malayca | ✔️ | ✔️ |
| Svahili (bireysel dil) | ✔️ | — |
| Swazi dili | ✔️ | — |
| İsveççe | ✔️ | — |
| Tacikçe | ✔️ | — |
| Tamilce | ✔️ | ✔️ |
| Telugu dili | ✔️ | ✔️ |
| Tayca | ✔️ | — |
| Tigrinyaca | ✔️ | — |
| Tosk Arnavutçası | ✔️ | — |
| Türkçe | ✔️ | ✔️ |
| Uygurca | ✔️ | — |
| Vietnamca | ✔️ | ✔️ |

## Desteklenen modeller

| Model | Tek konuşmacı | Birden fazla konuşmacı | Ses tasarımı | Ses kopyalama |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=tr) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=tr) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash TTS Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=tr) | ✔️ | ✔️ | — | — |
| [Gemini 2.5 Pro Önizleme TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=tr) | ✔️ | ✔️ | — | — |

### Hangi model ne zaman kullanılır?

Her iki Gemini 3.8 TTS modeli de aynı API şemasını ve istem formatını kullanır. Bu sayede, tek bir parametre değişikliğiyle modeller arasında geçiş yapabilirsiniz:

- Maksimum akustik doğruluk, nüanslı oyunculuk ve etkileyici kontrol en önemli öncelikler olduğunda **[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=tr) (`gemini-3.8-flash-tts`)** kullanın. Stüdyo kalitesinde yaratıcı çalışmalar, birden fazla konuşmacının yer aldığı karmaşık diyaloglar, yoğun ses patlaması etiketleri, zor telaffuzlar, bölgesel veya azınlık lehçeleri ve ses ile oda tonu kararlılığı gerektiren uzun anlatımlar için idealdir.
- **`gemini-3.1-flash-tts-preview` yerine hızlı ve uygun maliyetli bir alternatif olarak [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=tr) (`gemini-3.8-flash-lite-tts`)** kullanın. Yüksek hacimli toplu üretim, etkileşimli sesli temsilci basamakları, sesli okuma özellikleri, güvenilir ses kopyalama ve büyük dillerde günlük tek hoparlörlü konuşma için optimize edilmiştir.

### Geçiş rehberi

Daha önceki önizleme modellerinden (`gemini-3.1-flash-tts-preview` veya `gemini-2.5-pro-preview-tts`) Gemini 3.8 TTS'ye (`gemini-3.8-flash-tts` veya `gemini-3.8-flash-lite-tts`) yükseltme yaparken aşağıdaki beş önemli değişikliği inceleyin:

1. **Stili transkriptten ayırma:** Sürekli oyunculuk, ton, prozodi ve tempolama talimatlarını (ör. `"whispering"`, `"out of breath"` veya `"speaking slowly"`) düz metinden çıkarıp `speech_metadata.style` içine taşıyın.
   `text`, harfi harfine transkript ve satır içi ses etiketleri olarak kalmalıdır.
2. **Ses tasarımını kullanarak önceden tasarım karakterleri oluşturma:** Çok paragraflı `"Audio Profile"` veya `"Director's Notes"` blokları, [Ses tasarımında](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=tr) oluşturulan özel bir sesle değiştirin. Ardından, `voice_...` kimliğini TTS isteklerinizde minimum veya boş `style` dizelerle kullanın.
3. **Yapılandırılmış diyalog sıralarını kullanın:** Birden fazla konuşmacının olduğu diyaloglarda, `Speaker: ...` ön eklerini tek bir metin bloğuna yerleştirmek yerine `speech_metadata.speaker` ile her konuşmacı sırası için bir `part` iletin.
4. **Satır içi vokal etiketleri için köşeli parantez kullanın:** Anlık insan sesleri ve duraklamalar için köşeli parantez (`<laugh>`, `<sigh>`, `<cough>`, `<breath>`, `<short pause>`) kullanın. Vokal olmayan ses efekti etiketlerinden (ör. alkış veya gümbürtü) kaçının.
5. **Tekli isteklerde varsayılan WAV (`AUDIO_WAV`) çıkışını hesaba katın:** Varsayılan olarak başlıksız ham PCM `AUDIO_L16` döndüren `gemini-3.1-flash-tts-preview` modelinin aksine, Gemini 3.8 TTS modelleri tekli isteklerde RIFF başlığı (24 kHz, mono, 16 bit PCM) içeren tam **WAV (`AUDIO_WAV`)** ses döndürür:
   - Kodunuz daha önce ham PCM baytlarını bir WAV başlığına sarmalıyorsa (örneğin, Python'un `wave` modülünü veya Node'un `wav` paketini kullanarak) manuel başlık sarmalayıcıyı kaldırın ve kodu çözülmüş ses baytlarını doğrudan bir `.wav` dosyasına yazın.
   - Mevcut kanalınızın başlık içermeyen ham PCM, mu-law veya A-law ses gerektirmesi durumunda, REST API'yi kullanarak `generationConfig.responseFormat.audio.mimeType` değerini açıkça `"AUDIO_L16"`, `"AUDIO_MULAW"` veya `"AUDIO_ALAW"` olarak ayarlayın (ör. `generateContent` içinde `{"responseFormat": {"audio": {"mimeType": "AUDIO_L16"}}}`; `generateContent` üzerinde özel `responseFormat` geçersiz kılmaları REST API kullanılarak desteklenir. Python ve JavaScript SDK'nın `GenerateContentConfig` üzerinde `response_format` desteği henüz sağlanmamıştır. Alternatif olarak, Etkileşimler API'sinde `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}` kullanın). [Ses çıkış biçimleri](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=tr#audio-output-formats) bölümüne bakın.

## İstem yazma kılavuzu

Gemini 3.8 TTS modelleri, giriş metnini kesinlikle **harfi harfine transkript** olarak ele alır.
Sahne talimatlarının düz metne yerleştirildiği önceki önizleme modellerinin aksine, Gemini 3.8 TTS, sürekli dönüş seviyesindeki talimatları (`speech_metadata`) anlık satır içi sesli etiketlerden ayırır.

### Stil alanı ve satır içi etiketler karşılaştırması

Performans talimatlarınızı kapsama göre ayırın:

- **Sıra düzeyinde sunum (`speech_metadata.style`):** Duygu, prozodi, genel tempo veya sunum tarzı (ör. `"whispering"`, `"out of breath"`, `"muttering"` veya `"sarcastic"`) gibi sürekli sunum özelliklerini `speech_metadata` öğesinin `style` alanına ekleyin. Sıralar arasında tutarlı bir karakter ve performans oluşturmak için karakteri önceden [Ses tasarımı](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=tr) bölümünde tasarlayın ve `style` parametresini yalnızca isteğe bağlı sıra düzeyinde ayarlamalar için kullanın.
- **Anlık etkinlikler (satır içi etiketler):** Konuşma dışı anlık ses patlamalarını, nefesleri veya duraklamaları köşeli parantez (`<cough>`, `<breath>`, `<sigh>`, `<short pause>`) kullanarak transkriptin içine satır içi olarak yerleştirin. En yüksek ses kalitesi için köşeli parantez (`<...>`) kullanın ve ses dışı ses efektleri yerine insan seslerini tercih edin.

| Kapsam | Nereye yerleştirilir? | Örnekler |
| --- | --- | --- |
| **Tur düzeyi** (tur boyunca devam eder) | `speech_metadata.style` | `"angry tone"`, `"speaking rapidly"`, `"out of breath"`, `"whispers"`, `"sarcastic"` |
| **Belirli bir noktada** (belirli bir kelimede gerçekleşir) | `text` (`<...>`) içinde satır içi | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### Tempo ve duraklamalar

Ritim ve sessizliği üç ayrıntı düzeyinde kontrol edebilirsiniz:

- **Noktalama işaretleri ve üç nokta:** Doğal bir konuşma duraksaması için virgül, tire (`--`) ve üç nokta (`...`) kullanın.
- **Satır içi duraklatma etiketleri:** Konuşmacının duraklaması gereken noktalara `<short pause>` veya `<long pause>` etiketlerini ekleyin:
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **Sıra düzeyinde hız:** Tüm sıra boyunca konuşma hızını kontrol etmek için `speech_metadata` içinde `"style": "speaking rapidly"` veya `"style": "speaking slowly"` değerini ayarlayın.

### Prosodi ve perde

Bir sıra boyunca prozodiyi, perdeyi ve tonlamayı kontrol etmek için **`speech_metadata.style`** kullanın (örneğin, `"style": "high pitch, cheerful and excited inflection"` veya `"style": "monotone and flat"`). Duygu veya prozodi diyalog sırasında değişirse senaryoyu her sıra için farklı `style` değerleri olan ayrı sıralara bölün.

### Vurgu

Çeviri yazıda belirli kelimeleri büyük harfle yazın. Noktalama işaretleri ve satır içi vokal etiketleriyle birlikte kullanarak önemli kelimelere doğal bir vokal vurgu ekleyin:

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### Ses patlamaları ve konuşma dışı sesler

Konuşma dışı insan seslerini, sesin duyulması gereken tam noktada köşeli parantez (`<...>`) kullanarak satır içine yerleştirin. Önerilen sesli etiketler şunlardır:

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

### Arka kanallar ve çakışan konuşma

Birden fazla konuşmacının olduğu diyaloglarda, dinleyicinin tepkilerini konuşmacının sırasının içinde dikey çizgi karakterleriyle (`|reaction|`) sarmalayarak her tepki için ayrı bir sıra oluşturmadan doğal geri bildirimler veya üst üste binen konuşmalar oluşturun.

- **Kısa geri bildirim alışverişleri:** Aktif konuşmacının sırası sırasında kısa dinleyici tepkilerini (`|oh hmm|`, `|oh really?|`, `|absolutely|`) katmanlayın:
  - **1. tur (A konuşmacısı):** `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **2. sıra (B konuşmacısı):** `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **3. sıra (A konuşmacısı):** `"Then let's ship it |absolutely| and watch the dashboards."`
- **Çakışan ve aralıklı konuşma:** İki konuşmacı arasındaki eşzamanlı veya aralıklı konuşmayı simüle etmek için birden fazla dikey çizgi segmenti kullanın (`gemini-3.8-flash-tts` ile en iyi şekilde çalışır):
  - **Aynı anda geri sayım/koro:** `"Let's surprise him on three |ok| ready?"` ve `"one. two. three. |happy| happy |birthday| birthday!"`
  - **Tam konuşmacı çakışması:** `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### Nesiller arasında tutarlılık ve kaçınılması gerekenler

Ses kimliğinin sıralar arasında tutarlı kalmasını sağlamak için aşağıdaki yönergeleri uygulayın:

- **Uzun stil blokları yerine ses tasarımında karakterleri önceden tasarlayın:**
  Önceki modellerden taşınan uzun `"Audio Profile"` paragraflar ve çok maddeli `"Director's Notes"`, ses kaymasının en yaygın nedenidir.
  [Ses tasarımında](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=tr), aynı yaratıcı sezgiyi baştan kullanarak kalıcı bir özel `voice_...` karakter oluşturun, ardından bu ses kimliğini TTS çağrılarınızda kullanın.
- **Kararlılık için ses referansını kullanma (meta talimatları atlama):**
  Gemini 3.8 TTS modelleri, öncelikle ses referansını temel alacak şekilde eğitilmiştir.
  Modele sesi sabit tutmasını söyleyen talimatlar (ör. `"do not switch speaker identity"` veya `"maintain identical timbre"`) eklemeyin. Ek istem metni, kaymayı artırır. Gereksiz stil talimatlarını bırakın ve modelin, ses referansıyla sağlanan sabit nokta etrafında doğal olarak değişmesine izin verin.
- **`style` içinde değişmez konuşmacı özelliklerini değiştirmeye çalışmayın:** `speech_metadata.style` içine yaş, cinsiyet, ad veya kalıcı aksan değişiklikleri eklemeyin.
  Bunun yerine, Genişletilmiş Ses Kitaplığı'ndan bölgesel bir ses seçin veya [Ses Tasarımı](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=tr) ile bir ses oluşturun.

### Önerilen iş akışı

1. **Karakteri bir kez oluşturun:** Karakterinizi [Ses tasarımı](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=tr)'nda oluşturun veya Genişletilmiş Ses Kitaplığı'ndan hedef dilinize ve karakterinize uygun bölgesel bir ses seçin.
2. **Konuşma hataları içeren doğal konuşma transkriptleri yazın:** Maksimum doğallık için `text`, doğal konuşma hataları ve tereddütler (örneğin, `"Oh uh yeah I think... hm, so that's interesting"`) içeren gerçek bir konuşma transkripti olarak yazılmalıdır.
3. **Önce düz TTS'yi test edin:** Transkriptinizi önce boş bir `style` alanı ile sentezleyin. Çoğu istek için `style` talimatı gerekmez.
4. **Yalnızca değişiklikler için kısa `style` istemleri ekleyin:** Yalnızca belirli bir sunum ayarlaması gerektiren sıralar için kısa bir `style` dizesi (ör. `"casual, friendly"` veya `"muttering, then reassuring"`) ekleyin ve tutarlı bir temel istediğinizde sıralar arasında tam olarak aynı kısa dizeyi yeniden kullanın.

### Çok turlu diyalog ve sesli ajanlar

Anlık etkileşimli sesli temsilciler veya çok aşamalı etkileşim uygulamaları oluştururken:

- LLM metin parçaları geldikçe **sıra başına bir TTS çağrısı** yapın.
- Yapılandırılmış `voice` (önceden oluşturulmuş, tasarlanmış `voice_...` veya kopyalanmış `voice_...` / `voicekey_...`), konuşmacının kimliğini her sırayla taşısın. Her sırada uzun bir karakter kişiliğini yeniden göndermeyin.
- Sıra başına `style` alanını boş bırakın veya tüm görüşme için kısa ve sabit bir dize (ör. `"casual, friendly"`) gönderin.
- Temsilcinin uzun yanıtlarını daha kısa bölümlere ayırın. Daha güçlü stil istemleri kullanmaya çalışmayın.

## Akış konuşması oluşturma

Oluşturulan ses, model tarafından sentezlenirken ses akışı yapabilirsiniz. Tekli isteklerin aksine (RIFF başlığıyla birlikte eksiksiz bir WAV dosyası döndürür), **akış istekleri varsayılan olarak başlık içermeyen ham 16 bit imzalı little-endian doğrusal PCM (`AUDIO_L16` / `audio/L16;codec=pcm;rate=24000`, 24 kHz, mono) parçaları döndürür**. Bu sayede ses parçaları, kapsayıcı başlıkları olmadan sürekli olarak oynatılabilir veya birleştirilebilir:

### Python

```
from google import genai

client = genai.Client()

response_stream = client.models.generate_content_stream(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

for chunk in response_stream:
    try:
        data = chunk.candidates[0].content.parts[0].inline_data.data
        # data contains raw PCM bytes (24kHz, 1-channel, 16-bit)
    except (IndexError, AttributeError):
        pass
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const ai = new GoogleGenAI({});

   const responseStream = await ai.models.generateContentStream({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   for await (const chunk of responseStream) {
      const data = chunk.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
      if (data) {
         const audioBuffer = Buffer.from(data, 'base64');
         // Process the audio buffer
      }
   }
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }'
```

## Ses çıkışı biçimleri

Gemini 3.8 TTS modelleri, isteğin tekli veya akışlı olmasına bağlı olarak farklı varsayılan ses formatları kullanır:

- **Tekli istekler (`models.generate_content`):** RIFF başlığına sahip (24 kHz, mono, 16 bit imzalı küçük endian PCM) eksiksiz **WAV (`AUDIO_WAV`)** sesini döndürür. Kodu çözülmüş ses baytlarını, manuel olarak WAV kapsayıcısı eklemeden doğrudan bir `.wav` dosyasına yazabilirsiniz.
- **Yayın istekleri (`models.generate_content_stream` / `streamGenerateContent`):**
  Parçaların her birinde kapsayıcı başlıkları olmadan sürekli olarak yayınlanabilmesi veya birleştirilebilmesi için varsayılan olarak **başlıksız ham Linear PCM (`AUDIO_L16`)** parçalarını (24 kHz, mono, 16 bit imzalı little-endian PCM) döndürün.

`generationConfig.responseFormat.audio` kullanarak çıkış ses kodlamasını ve örnek hızını geçersiz kılabilirsiniz:

| `mimeType` değer | Biçim | Açıklama |
| --- | --- | --- |
| `"AUDIO_WAV"` *(tekli varsayılan)* | WAV (`audio/wav`) | RIFF başlığı içeren tam WAV dosyası (24 kHz, mono, 16 bit PCM). |
| `"AUDIO_L16"` *(varsayılan akış)* | Doğrusal PCM (`audio/l16`) | Başlıksız ham 16 bit imzalı little-endian doğrusal PCM. Yayın, özel ses işlem hatları veya çok turlu klipleri birleştirme için en iyisidir. |
| `"AUDIO_MULAW"` | μ-law (`audio/basic` / `audio/mulaw`) | G.711 μ-law companded audio. Kuzey Amerika ve Japonya telefon sistemlerinde yaygın olarak kullanılır (8 kHz). |
| `"AUDIO_ALAW"` | A-law (`audio/alaw`) | G.711 A-law sıkıştırılmış ses. Avrupa ve uluslararası telefon sistemlerinde yaygın olarak kullanılır (8 kHz). |

İsteğe bağlı olarak `sampleRate` da belirtebilirsiniz (ör. `24000`, `16000` veya `8000` Hz; varsayılan değer `24000` Hz'dir).

Aşağıdaki REST örneği, 24 kHz'de başlıksız ham 16 bit PCM (`AUDIO_L16`) ister:

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "responseFormat": {
            "audio": {
              "mimeType": "AUDIO_L16",
              "sampleRate": 24000
            }
          },
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.pcm
```

## Sınırlamalar

- TTS modelleri yalnızca metin girişlerini kabul eder ve yalnızca ses çıkışları üretir.
- Tek istekte birden fazla konuşmacı için metin okuma (`multiSpeakerVoiceConfig`) özelliği, önceden oluşturulmuş sesleri kullanarak 2 konuşmacıyı destekler. Özel olarak tasarlanmış (`voice_...`) veya kopyalanmış (`voice_...` / `voicekey_...`) sesleri çok karakterli diyaloglarda birleştirmek için her konuşmacının sırasını ayrı ayrı sentezleyin.
  Tekli istekler varsayılan olarak 44 baytlık RIFF başlığıyla `audio/wav` döndürdüğünden, 24 kHz PCM ses karelerini birleştirmeden önce ham PCM (`AUDIO_L16`) isteyin veya her sıradan WAV başlığını çıkarın.
- **Özel ses depolama alanı sınırları ve TTL:**
  - **Durumlu sesler (`store=True`, istemli veya kopyalanmış):** **1 yıllık TTL** (geçerlilik süresi) ile proje başına en fazla **200 ses**.
  - **Durum bilgisi içermeyen ses anahtarları (`store=False`, `voicekey_...`):** **7 günlük geçerlilik süresi (TTL)**
- Dil kapsamı için [Desteklenen diller](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=tr#languages) bölümünü inceleyin.

## Sırada ne var?

- [Ses tasarımı](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=tr) ile doğal dilden özel ses karakterleri oluşturun.
- [Ses kopyalama](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=tr)'da mevcut bir konuşmacının sesini kopyalayın.
- [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=tr) ve [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=tr) model sayfalarında model özelliklerini karşılaştırın.
- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=tr) ile etkileşimli çift yönlü ses özelliğini keşfedin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-12 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-12 UTC."],[],[]]
