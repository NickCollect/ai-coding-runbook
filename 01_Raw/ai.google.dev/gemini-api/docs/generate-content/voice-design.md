---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=tr
fetched_at: 2026-09-28T06:30:31.941664+00:00
title: "Ses tasar\u0131m\u0131 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/generate-content?hl=tr)

Geri bildirim gönderin

# Ses tasarımı

Ses tasarımı, Gemini API Voices uç noktasını (`POST /v1beta/voices`) kullanarak doğal dil açıklamasıyla yepyeni ve kalıcı bir sesli karakter oluşturmanıza olanak tanır. Önceden oluşturulmuş seslerle veya referans ses kaydıyla sınırlı kalmak yerine bir karakterin yaşını, ses tonunu, aksanını ve temel sunumunu açıklayabilir ve projenize kaydedilen, yeniden kullanılabilir bir `voice_...` kimliği alabilirsiniz.

Özel sesleri tasarlamanın, denemenin ve yinelemenin en hızlı yolu, [Google AI Studio](https://aistudio.google.com/generate-speech?hl=tr)'daki etkileşimli **Ses Tasarımı** stüdyosunu kullanmaktır. Metin istemlerinden özel karakterler oluşturabilir, bunları örnek senaryolarla test edebilir ve sonuçtaki `voice_...` kimliğini doğrudan uygulama kodunuza kopyalayabilirsiniz.

[Google AI Studio'da deneme](https://aistudio.google.com/generate-speech?hl=tr)

Hem [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=tr)
(`gemini-3.8-flash-tts`) hem de
[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=tr)
(`gemini-3.8-flash-lite-tts`) Voice tasarımını destekler.

## Tasarlanmış bir ses oluşturma

Metin açıklamasından özel bir ses oluşturmak için Google GenAI SDK'sını (`google-genai` 2.25.0+ / `@google/genai` 2.24.0+) veya REST API'yi kullanın. `"prompted"` sesleri için hem `voices.create` (`CreateVoice`) hem de `voices.get` (`GetVoice`), yalnızca çıkış `sample_audio` alanı (`mime_type: "audio/wav"`, base64 kodlu `data`) döndürür. Böylece, oluşturulan sesi hemen dinleyebilirsiniz:

### Python

```
import base64
from google import genai

client = genai.Client()

# 1. Design a custom voice persona from natural language
created_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Warm British Astronomer",
        "gender": "male",
        "language_code": "en-GB",
        "prompted": {
            "input": (
                "A warm, thoughtful astronomer in his late 60s with a gentle"
                " British accent, speaking with quiet wonder."
            )
        },
    },
)

print(f"Created voice ID: {created_voice.id}")

# Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if created_voice.sample_audio and created_voice.sample_audio.data:
    with open("voice_preview.wav", "wb") as f:
        f.write(base64.b64decode(created_voice.sample_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// 1. Design a custom voice persona from natural language
const createdVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "prompted",
    display_name: "Warm British Astronomer",
    gender: "male",
    language_code: "en-GB",
    prompted: {
      input:
        "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder.",
    },
  },
});

console.log(`Created voice ID: ${createdVoice.id}`);

// Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if (createdVoice.sample_audio?.data) {
  fs.writeFileSync(
    "voice_preview.wav",
    Buffer.from(createdVoice.sample_audio.data, "base64")
  );
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "store": true,
    "voice": {
      "model": "gemini-3.8-flash-tts",
      "type": "prompted",
      "display_name": "Warm British Astronomer",
      "gender": "male",
      "language_code": "en-GB",
      "prompted": {
        "input": "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder."
      }
    }
  }' | tee created_voice.json | jq -r '.sample_audio.data' | base64 --decode > voice_preview.wav
```

## Sesli tasarımın işleyiş şekli

1. **İstemli ses oluşturma:** `type="prompted"` ve `store=True` ile `voices.create` (`POST /v1beta/voices`) numarasını arayın.
2. **Kalıcı bir `voice_id` ve `sample_audio` önizlemesi alma:** API, ses kimliğini oluşturur, projenizde saklar ve ses için oluşturulan önizleme sesini içeren `sample_audio` (`mime_type: "audio/wav"`, base64 kodlu `data`) ile birlikte kalıcı bir kimlik (ör. `voice_abc123...`) döndürür.
3. **Konuşma sentezleme:** `generateContent`'i ararken `speechConfig.voiceConfig.voice` içindeki `voice_id`'ı iletin.

## Tasarladığınız sesle konuşma sentezleme

Arama yaparken döndürülen `id` (`voice_...`) değerini `voiceConfig.voice` içinde iletin
`generateContent`:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "speech_metadata": {"style": "reflective and awe-inspired"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": created_voice.id}
        },
    },
)

audio_bytes = response.candidates[0].content.parts[0].inline_data.data
with open("designed_voice.wav", "wb") as f:
    f.write(audio_bytes)
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash-tts",
  contents: [{
    role: "user",
    parts: [{
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      speechMetadata: { style: "reflective and awe-inspired" },
    }],
  }],
  config: {
    responseModalities: ["AUDIO"],
    speechConfig: {
      voiceConfig: { voice: createdVoice.id },
    },
  },
});

const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
if (data) {
  fs.writeFileSync("designed_voice.wav", Buffer.from(data, "base64"));
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [{
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "speech_metadata": {
          "style": "reflective and awe-inspired"
        }
      }]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "voice": "voice_YOUR_DESIGNED_VOICE_ID"
        }
      }
    }
  }'
```

## Seslerinizi yönetme

Voices API'yi kullanarak kayıtlı seslerinizi istediğiniz zaman listeleyebilir, filtreleyebilir, inceleyebilir ve silebilirsiniz (tüm filtre parametreleri için [Genişletilmiş Ses Kitaplığı ve filtreleme](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=tr#voice-library) bölümüne bakın).

- **Depolama sınırları ve TTL:** Durumlu sesler (`store=True`, istemli ve kopyalanmış sesler arasında paylaşılır) için **proje başına 200 ses** sınırı ve **1 yıllık TTL** (geçerlilik süresi) vardır.
- **`sample_audio` availability:** `voices.create()` (`CreateVoice`) ve `voices.get()` (`GetVoice`), `"prompted"` sesleri için `sample_audio` (`mime_type:
  "audio/wav"`, base64 kodlu `data`) değerini doldurur. Listelemenin hafif olması için `voices.list()` (`ListVoices`), `sample_audio` öğesini atlar (`"replicated"` ve `"prebuilt"` sesleri için `sample_audio` ayarlanmamıştır).

### Python

```
from google import genai

client = genai.Client()

# List stored prompted voices in your project filtered by language
response = client.voices.list(
    type_=["prompted"],
    language_code=["en-US", "en-GB"],
)
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=created_voice.id)

# Delete a stored custom voice
client.voices.delete(id=created_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored prompted voices in your project filtered by language
const response = await ai.voices.list({
  type: ["prompted"],
  language_code: ["en-US", "en-GB"],
});
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(createdVoice.id);

// Delete a stored custom voice
await ai.voices.delete(createdVoice.id);
```

### REST

```
# List stored prompted voices filtered by language
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=prompted" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored custom voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Sesli tasarım için istem yazmayla ilgili en iyi uygulamalar

- **Kalıcı vokal özelliklerini `style` yerine Voice tasarımına yerleştirin:** `voices.create`'da sesi oluştururken yaş, cinsiyet, tını, vokal dokusu ve bölgesel aksan gibi değişmez özellikleri tanımlayın.
- **`speech_metadata.style` karakterini duruma bağlı duygular için kullanın:** Özel sesiniz oluşturulduktan sonra, konuşmacının temel kimliğini değiştirmeden adım adım oyunculuğu yönlendirmek için kısa `style` istemler (örneğin, `"whispered urgently"` veya `"cheerful and energetic"`) kullanın.
- **Net ve kısa olun:** 1-2 cümlelik net bir açıklama (ör. *"30'lu yaşlarında, hafif Orta Batı aksanlı, canlı ve enerjik bir spor spikeri"*) çelişkili veya çok uzun paragraflara kıyasla daha temiz ve tutarlı sonuçlar verir.

## Sırada ne var?

- [Ses kopyalama](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=tr) özelliğinde mevcut bir konuşmacının sesini nasıl kopyalayacağınızı öğrenin.
- [Metin okuma kılavuzunda](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=tr) dönüş seviyesinde stil oluşturma, satır içi etiketler ve birden fazla konuşmacının yer aldığı diyaloglar hakkında bilgi edinin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-24 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-24 UTC."],[],[]]
