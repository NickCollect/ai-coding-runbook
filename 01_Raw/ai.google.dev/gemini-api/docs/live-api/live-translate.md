---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=tr
fetched_at: 2026-08-24T02:34:29.066602+00:00
title: "Gemini Live API ile canl\u0131 \u00e7eviri \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini Live API ile canlı çeviri

Gemini Live API, [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=tr) modelini kullanarak 70'ten fazla dil arasında düşük gecikmeli, anlık sesli çeviri yapılmasını destekler. Live API'yi çeviri ayarlarıyla yapılandırarak sesi bir dilde yayınlayabilir ve çevrilmiş ses çıkışını başka bir dilde alabilirsiniz. Böylece, anlık ve sorunsuz bir şekilde sesli çeviri yapabilirsiniz.

[Google AI Studio'da Anında Çeviri'yi deneyinmic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=tr)
[Örnek uygulamayı GitHub'dan klonlayıncode](https://github.com/google-gemini/gemini-live-api-examples)
[Kodlama aracısı becerilerini kullanınterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=tr#gemini-live-api-dev)

## Canlı Müşteri Temsilcisi ve Canlı Çeviri

Her ikisi de Live API'yi kullanırken Canlı Çeviri'nin zihinsel modeli, sohbet tarzında anlık temsilci etkileşimlerinden farklıdır.

| Canlı Müşteri Temsilcisi | Canlı Çeviri |
| --- | --- |
| **Model, asistan olarak hareket eder.** Dinler, akıl yürütür ve sizin adınıza işlem yapar. | **Model, çevirmen gibi davranır.** Gerçek zamanlı çeviri ardışık düzeni gibi çalışır. |
| **Sıra tabanlı etkileşimler kullanır.** Duraklamalara, amaç algılamaya dayanır ve kesintileri yönetir. | **Sürekli akış işleme kullanır.** Konuşmacının konuşmasını beklemeden, konuşma sırasında çeviri yapar. |
| **Araçları ve temsilcileri destekler.** İşlev çağrısı, Google Arama ve talimatlar için yerel destek. | **Yalnızca çeviriyi destekler.** Tamamen düşük gecikmeli çeviri; araçlar veya talimatlar desteklenmez. |
| **Tamamen çok formatlı.** Metin, ses, video ve resim girişlerini destekler. | **Ses kısıtlanmış.** Sıkı anlık gecikme eşiklerini sağlamak için giriş yalnızca sesle sınırlıdır. |
| **Ayrıntılı yapılandırma.** Üretim, konuşma, araçlar ve sistem talimatlarını kullanır. | **Basitleştirilmiş yapılandırma.** `target_language_code` ve `echo_target_language` gibi açma/kapatma düğmelerini ayarlayın. |

## Başlayın

Aşağıdaki örneklerde, bir istemcinin nasıl başlatılacağı ve çeviri yapılandırmasıyla Live API'ye nasıl bağlanılacağı gösterilmektedir.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.5-live-translate-preview"
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
    output_audio_transcription=types.AudioTranscriptionConfig(),
    translation_config=types.TranslationConfig(
        target_language_code="pl",
        echo_target_language=True
    )
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started with translation")
        # Start receiving the translated audio stream
        async for response in session.receive():
            if response.server_content:
                if response.server_content.input_transcription:
                    print(f"Input transcript: {response.server_content.input_transcription.text}")
                if response.server_content.output_transcription:
                    print(f"Output transcript: {response.server_content.output_transcription.text}")
                if response.server_content.model_turn:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data:
                            audio_data = part.inline_data.data
                            # Play or process the translated audio chunk
                            print(f"Received audio chunk ({len(audio_data)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-live-translate-preview';
const config = {
    responseModalities: [Modality.AUDIO],
    inputAudioTranscription: {},
    outputAudioTranscription: {},
    translationConfig: {
        targetLanguageCode: 'pl',
        echoTargetLanguage: true
    }
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.debug('Opened'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Input transcript:', content.inputTranscription.text);
        }
        if (content?.outputTranscription) {
          console.log('Output transcript:', content.outputTranscription.text);
        }
        if (content?.modelTurn?.parts) {
          for (const part of content.modelTurn.parts) {
            if (part.inlineData) {
              const audioData = part.inlineData.data;
              // Play or process the translated audio chunk (base64 encoded)
              console.debug(`Received audio chunk (${audioData.length} bytes)`);
            }
          }
        }
      },
      onerror: (e) => console.debug('Error:', e.message),
      onclose: (e) => console.debug('Close:', e.reason),
    },
  });

  console.debug("Session started with translation");
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-live-translate-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['AUDIO'],
        inputAudioTranscription: {},
        outputAudioTranscription: {},
        translationConfig: {
          targetLanguageCode: 'pl',
          echoTargetLanguage: true
        }
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  if (response.serverContent) {
    const content = response.serverContent;
    if (content.inputTranscription) {
      console.log('Input transcript:', content.inputTranscription.text, `(${content.inputTranscription.languageCode})`);
    }
    if (content.outputTranscription) {
      console.log('Output transcript:', content.outputTranscription.text, `(${content.outputTranscription.languageCode})`);
    }
    if (content.modelTurn?.parts) {
      for (const part of content.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data;
          // Play or process the translated audio chunk (base64 encoded)
          console.debug(`Received audio chunk (${audioData.length} bytes)`);
        }
      }
    }
  }
};
```

## Ses gönderme

Çeviri için ses girişlerini yayınlamak üzere ham, little-endian, 16 bit PCM ses gönderirsiniz.

- **Giriş ses biçimi**: 16 kHz'de (mono, little-endian) ham 16 bit PCM.
- **Çıkış ses biçimi**: 24 kHz'de (mono, little-endian) ham 16 bit PCM.
- **Yığın Boyutu ve Gecikme**: Sesleri 100 ms'lik yığınlar halinde gönderin.

Aşağıdaki örneklerde, ses parçalarının oturuma nasıl gönderileceği gösterilmektedir.

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

### WebSockets

```
// Assuming 'chunk' is a Buffer of raw PCM audio
function sendAudioChunk(chunk) {
  if (websocket.readyState === WebSocket.OPEN) {
    const audioMessage = {
      realtimeInput: {
        audio: {
          data: chunk.toString('base64'),
          mimeType: 'audio/pcm;rate=16000'
        }
      }
    };
    websocket.send(JSON.stringify(audioMessage));
  }
}
```

## Yapılandırma

Çeviriyi etkinleştirmek için oturum kurulumu sırasında `translationConfig` öğesini `generationConfig` içinde belirtmeniz gerekir.

### Kurulum mesajı yapılandırması

`generationConfig`, transkriptleri etkinleştirmek için aşağıdaki alanları destekler:

- **`inputAudioTranscription`**: Mevcut olduğunda modelin, giriş sesinin metin transkriptlerini göndermesini sağlayan bir nesne.
- **`outputAudioTranscription`**: Mevcut olduğunda modelin, çıkış (çevrilmiş) sesin metin transkriptlerini göndermesini sağlayan bir nesne.

`translationConfig` aşağıdaki alanları destekler:

- **`targetLanguageCode`**: Modelin çevirmesini istediğiniz dilin [BCP-47 dil kodu](#supported-languages) (ör. Lehçe için `"pl"`, İspanyolca için `"es"`). Varsayılan olarak `"en"` değerine ayarlanır.
- **`echoTargetLanguage`**: Hedef dildeki giriş sesinin nasıl işleneceğini belirten bir boole. `true` olarak ayarlanırsa model, hedef dildeki giriş sesini tekrarlar. `false` olarak ayarlanırsa model, giriş konuşması zaten hedef dilde olduğunda sessiz kalır. Varsayılan olarak `false` değerine ayarlanır.

Aşağıda, kurulum mesajı yapısı örneği verilmiştir:

```
"setup": {
    "model": "models/gemini-3.5-live-translate-preview",
    "generationConfig": {
      "responseModalities": [
        "AUDIO"
      ],
      "inputAudioTranscription": {},
      "outputAudioTranscription": {},
      "translationConfig": {
        "targetLanguageCode": "pl",
        "echoTargetLanguage": true
      }
    }
}
```

## İstemci tarafı uygulamalarda kısa ömürlü jetonları kullanma

İstemciden sunucuya uygulamalarda, API anahtarınızı açığa çıkarmamak için [kısa ömürlü jetonlar](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=tr) (şu anda `v1beta` aşamasında) kullanabilirsiniz.

Canlı Çeviri ile geçici jetonlar kullanılırken:

1. `v1beta` uç noktasını kullanmanız gerekir.
2. **Kilitleme yapılandırması:** Varsayılan olarak, sunucunuzdaki jeton oluşturma kısıtlamalarında `translationConfig` değerini belirtmeniz gerekir. Bu sayede çeviri yapılandırması kilitlenir ve istemci tarafından değiştirilemez.
3. **Yapılandırmanın kilidini açma:** `translationConfig` değerini istemci tarafında ayarlayabilmek istiyorsanız (ör. kullanıcının kendi hedef dilini seçmesine izin vermek için) bu değeri jeton oluşturma isteğinden çıkarmanız ve bunun yerine `"lock_additional_fields": []` değerini ayarlamanız gerekir. Bu işlem, `translationConfig` öğesinin istemci tarafında ayarlanabilmesini sağlar.

### Kısıtlanmış geçici jeton oluşturma

Aşağıdaki örneklerde, çeviri kısıtlamaları içeren geçici jetonun nasıl oluşturulacağı gösterilmektedir.

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
        'uses': 1,
        'expire_time': now + datetime.timedelta(minutes=30),
        'live_connect_constraints': {
            'model': 'gemini-3.5-live-translate-preview',
            'config': {
                'translation_config': {
                    'target_language_code': 'pl',
                    'echo_target_language': True
                }
            }
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1,
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.5-live-translate-preview',
            config: {
                responseModalities: ['AUDIO'],
                inputAudioTranscription: {},
                outputAudioTranscription: {},
                translationConfig: {
                    targetLanguageCode: 'pl',
                    echoTargetLanguage: true
                }
            }
        },
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.5-live-translate-preview",
      "config": {
        "responseModalities": ["AUDIO"],
        "inputAudioTranscription": {},
        "outputAudioTranscription": {},
        "translationConfig": {
          "targetLanguageCode": "pl",
          "echoTargetLanguage": true
        }
      }
    }
  }'
```

## Sınırlamalar

- **Giriş Biçimleri**: Çeviri için yalnızca ses girişi desteklenir. Metin girişi desteklenmez.
- **Ses Çoğaltma**: Ses çoğaltma tutarsız olabilir. Sesler, uzun aralardan sonra değişebilir, konuşmanın başlangıcına göre yanlış cinsiyet atanabilir veya hızlı çok konuşmacılı sohbetlerde tek bir seste takılabilir.
- **Dil algılama**: Dil algılama, yoğun aksanlar, benzer diller (ör. İspanyolca ve Portekizce) veya hızlı dil geçişleri konusunda zorlanır. **Not:** Bu durum yalnızca giriş transkriptini etkiler. Dil kodları ve nihai çeviri doğru olmalıdır.
- **Arka plan sesi**: Model, temiz konuşma üretmek için gürültüyü ve müziği filtreleyecek şekilde tasarlanmıştır ancak tüm arka plan sesleri göz ardı edilmeyebilir.
- **Hedef Dili Tekrar Et**: `echoTargetLanguage: true` seçildiğinde, giriş sesi zaten hedef dildeyse arka plan gürültüsü veya müzik, çevrilen seste yapaylıklar oluşturabilir.

## Desteklenen diller

Canlı Çeviri için aşağıdaki diller desteklenir.

| Dil | BCP-47 Kodu | Dil | BCP-47 Kodu |
| --- | --- | --- | --- |
| Afrikaanca | af | Kazakça | kk |
| Akan | ak | Kmerce | km |
| Arnavutça | sq | Ruandaca | rw |
| Amharca | öö | Korece | ko |
| Arapça | ar | Laoca | lo |
| Ermenice | hy | Letonca | lv |
| Azerbaycanca | az | Litvanca | lt |
| Baskça | eu | Makedonca | mk |
| Belarusça | be | Malayca | ms |
| Bengali | bn | Malayalam | ml |
| Bulgarca | bg | Marathi | mr |
| Birmanca (Myanmar) | my | Moğolca | mn |
| Katalanca | ca | Nepalce | ne |
| Çince (Basitleştirilmiş) | zh-Hans | Norwegian | no, nb |
| Çince (Geleneksel) | zh-Hant | Farsça | fa |
| Hırvatça | s | Lehçe | pl |
| Çekya | cs | Portekizce (Brezilya) | pt-BR |
| Danca | da | Portekizce (Portekiz) | pt-PT |
| Felemenkçe | nl | Punjabi | pa |
| İngilizce | en | Rumence | ro |
| Estonca | et | Rusça | ru |
| Filipince | fil | Sırpça | sr |
| Finnish | fi | Sindice | sd |
| Fransızca | fr | Seylanca | si |
| Galiçyaca | gl | Slovakça | sk |
| Gürcüce | ka | Slovence | sl |
| Almanca | de | İspanyolca | es |
| Greek | el | Sundaca | su |
| Güceratça | gu | Swahili | sw |
| Hausaca | ha | İsveççe | sv |
| İbranice | o | Tamilce | ta |
| Hindi | hi | Telugu dili | te |
| Macarca | hu | Tayca | th |
| İzlandaca | is | Türkçe | tr |
| Endonezce | id | Ukraynaca | uk |
| Italian | it | Urduca | UR |
| Japonca | ja | Özbekçe | uz |
| Cavaca | jv | Vietnamca | vi |
| Kannada | kn | Zulu | zu |

## Sırada ne var?

- Live API [Özellikleri](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=tr) kılavuzunun tamamını okuyun.
- [SDK'yı kullanmaya başlama](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=tr) kılavuzunu okuyun.
- [WebSocket'leri kullanmaya başlama](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=tr) kılavuzunu okuyun.
- İstemciden sunucuya uygulamalarda güvenli kimlik doğrulama için [Geçici jetonlar](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=tr) kılavuzunu okuyun.
- GitHub'dan [Live API examples](https://github.com/google-gemini/gemini-live-api-examples)'ı (Canlı API örnekleri) kopyalayın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-23 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-23 UTC."],[],[]]
