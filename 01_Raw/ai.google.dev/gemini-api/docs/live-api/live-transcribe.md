---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=tr
fetched_at: 2026-10-19T05:38:23.588852+00:00
title: "Gemini Live API ile canl\u0131 transkripsiyon \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hemen oynayabilirsiniz. [Deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=tr).

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini Live API ile canlı transkripsiyon

Gemini Live API, [`gemini-3.5-transcribe-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=tr) modelini kullanarak düşük gecikmeli, anlık sesle yazma transkriptini destekler. WebSocket'ler üzerinden Live API'ye bağlanarak veya Google Gen AI SDK'yı kullanarak sürekli ses girişi yayınlayabilir ve konuşma gerçekleşirken artımlı, gerçek zamanlı metin transkriptleri alabilirsiniz.

[Google AI Studio'da Canlı Transkript'i deneyinmic](https://aistudio.google.com/live?model=gemini-3.5-transcribe-live&hl=tr)
[Colab çözüm kitabını açıncode](https://github.com/google-gemini/cookbook)
[Kodlama ajan becerilerini kullanınterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=tr#gemini-live-api-dev)

Gemini Live API'den yararlanan [Agora](https://docs.agora.io/en/ai/models/asr/gemini), [Fishjam](https://docs.fishjam.io/tutorials/gemini-live-integration), [LiveKit](https://docs.livekit.io/agents/models/stt/gemini/), [Pipecat](https://docs.pipecat.ai/api-reference/server/services/stt/google), [Vercel](https://vercel.com/docs/ai-gateway/modalities/speech-to-text) ve [Vision Agents](https://visionagents.ai/integrations/stt/gemini) gibi geliştirici platformları, geliştiricilerin yüksek performanslı sesle çalışan arayüzleri kolayca oluşturup dağıtmasına olanak tanır. Bu platformlar, arka planda karmaşık gerçek zamanlı medya akışı altyapısını yönetir ve geliştiricilerin tamamen kullanıcı deneyimini oluşturmaya odaklanmasına olanak tanır.

## Canlı müşteri temsilcisi ve canlı transkript

Her ikisi de Live API çift yönlü yayın bağlantısını kullanırken Canlı Transkript, sohbet aracısı yerine özel, düşük gecikmeli bir konuşma tanıma hattı olarak çalışır.

| Özellik | Canlı Müşteri Temsilcisi | Canlı Olarak Metne Dönüştürme |
| --- | --- | --- |
| **Birincil rol** | Dinleyen, akıl yürüten ve yanıt veren etkileşimli bir asistan. | Gelen sesleri metne dönüştüren gerçek zamanlı sesle yazma ardışık düzeni. |
| **Yanıt biçimi** | Seslendirilmiş içerik ve metin (`response_modalities=["AUDIO"]`). | Yayın metni transkripsiyonları (`response_modalities=["TEXT"]`) |
| **Etkileşim stili** | Duraklatma algılama ve kesintilerle dönüşümlü diyalog. | Konuşmacı konuşurken sürekli akış işleme. |
| **Desteklenen özellikler** | İşlev çağırma, Google Arama, sistem talimatları. | Konuşma önyargısı (`custom_vocabulary`), dil algılama, manuel ve karma VAD, Akıllı Metne Dönüştürme. |
| **Giriş akışı** | Çok formatlı: ses, video, resimler, metin. | Ses girişi (ham 16 bit PCM). |

## Başlayın

Aşağıdaki örneklerde, `gemini-3.5-transcribe-live` ile çift yönlü bir akış oturumunun nasıl açılacağı ve anlık transkripsiyonların nasıl alınacağı gösterilmektedir.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.5-transcribe-live"

config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],  # Automatic language detection
    ),
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session established with Live Transcription")

        # Receive transcription events
        async for response in session.receive():
            server_content = response.server_content
            if server_content and server_content.input_transcription:
                print("Transcript:", server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-transcribe-live';

const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [], // Automatic language detection
  },
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.log('Connected to Live Transcription'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Transcript:', content.inputTranscription.text);
        }
      },
      onerror: (e) => console.error('Error:', e.message),
      onclose: (e) => console.log('Connection closed:', e.reason),
    },
  });
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-transcribe-live";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['TEXT'],
      },
      inputAudioTranscription: {
        languageCodes: []
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.inputTranscription) {
    console.log('Transcript:', content.inputTranscription.text);
  }
};
```

## Geçici ve son transkriptler

Ses, Live API'ye aktarılırken sunucu, `server_content` içinde iki tamamlayıcı transkripsiyon alanı yayar:

- **`interim_input_transcription`**: Düşük gecikmeli, konuşmacı aktif olarak konuşurken güncellenen spekülatif kısmi hipotezler. Bu kısmi güncellemeler, çok kısa bir gecikmeyle hızlı bir şekilde gerçekleşir. Duyarlı canlı kullanıcı arayüzü altyazılarını oluşturmak veya altyazıları önizlemek için `interim_input_transcription` simgesini kullanın.
- **`input_transcription`**: Konuşmacı durakladığında, konuşma sırası tamamlandığında veya konuşma sonlandırıldığında oluşturulan son transkript. Bu metin, yayınlandıktan sonra modelin söz konusu konuşma segmentinin yetkili transkripsiyonunu temsil eder. Akıllı transkripsiyon modunda, temizlenmiş ve biçimlendirilmiş yanıt da dahil edilir.

Aşağıdaki örnekte, akışla ilgili geçici kısmi sonuçların nasıl görüntüleneceği ve son transkriptlerin nasıl gönderileceği gösterilmektedir:

### Python

```
async def receive_transcripts(session):
    async for response in session.receive():
        server_content = response.server_content
        if not server_content:
            continue

        # Real-time interim hypothesis (updates dynamically as user speaks)
        if server_content.interim_input_transcription:
            interim_text = server_content.interim_input_transcription.text
            print(f"\r[Interim] {interim_text}", end="", flush=True)

        # Finalized transcript (emitted on speech completion)
        if server_content.input_transcription:
            final_text = server_content.input_transcription.text
            print(f"\n[Final] {final_text}")
```

### JavaScript

```
onmessage: (message) => {
  const content = message.serverContent;
  if (!content) return;

  if (content.interimInputTranscription) {
    // Update live subtitle preview on screen
    renderInterimPreview(content.interimInputTranscription.text);
  }

  if (content.inputTranscription) {
    // Append final committed transcript to chat history
    commitFinalTranscript(content.inputTranscription.text);
  }
};
```

### WebSockets

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.interimInputTranscription) {
    console.log('[Interim]:', content.interimInputTranscription.text);
  }
  if (content?.inputTranscription) {
    console.log('[Final]:', content.inputTranscription.text);
  }
};
```

## Ses gönderme

Ses parçalarını, etkin bağlantı üzerinden ham 16 bit PCM ses olarak aktarır.

- **Ses biçimi:** 16 kHz'de (mono, little-endian) ham 16 bit PCM.
- **Parça boyutu:** Sesleri 100 ms'lik parçalar halinde (1.024 ila 2.048 kare) gönderin.
- **MIME türü:** `audio/pcm;rate=16000` (veya eşleşen örnekleme hızı).

### Python

```
# Stream a raw PCM audio chunk
await session.send_realtime_input(
    audio=types.Blob(
        data=audio_chunk_bytes,
        mime_type="audio/pcm;rate=16000"
    )
)

# Signal the end of the audio stream when finished
await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
// Send base64-encoded PCM audio chunk
session.sendRealtimeInput({
  audio: {
    data: audioChunkBase64,
    mimeType: 'audio/pcm;rate=16000'
  }
});

// Signal stream end
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSockets

```
// Send base64-encoded PCM audio chunk
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: {
      data: audioChunkBase64,
      mimeType: 'audio/pcm;rate=16000'
    }
  }
}));

// Signal stream end
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

## Metne dönüştürme özellikleri

### Otomatik dil algılama

Varsayılan olarak, `language_codes` öğesinin atlanması veya `language_codes=[]` öğesinin ayarlanması otomatik dil tanımlamayı etkinleştirir. Model, çok dilli sohbetler ve dil değiştirme dahil olmak üzere ifadelerdeki konuşulan dili dinamik olarak algılar.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### Belirli bir dilde ipucu

Tanımanın belirli dillerde daha iyi çalışması için açık BCP-47 dil kodları (örneğin, İspanyolca için `["es-ES"]` veya Fransızca için `["fr-FR"]`) sağlayın (bkz. [Desteklenen diller](#supported-languages)).

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: ['es-ES'],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: ['es-ES'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### Özel kelime seçimi önyargısı

Konuşma tanıma özelliğini belirli terminolojiye yönlendirmek için `custom_vocabulary` içinde 1.000'e kadar kelime öbeği, özel isim, marka adı veya teknik terim listesi sağlayın (en iyi sonuçlar genellikle 100 terime kadar elde edilir).

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
        custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
    customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
      customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### Akıllı transkript

`input_audio_transcription` içindeki `mode` parametresini kullanarak transkripsiyon çıkış biçimlendirmesini yapılandırın:

- **`VERBATIM` (varsayılan)**: Konuşulan her şeyin bire bir transkriptini oluşturur. Ham dolgu kelimelerini ("ııı", "eee", "gibi"), tekrarları ve yanlış başlangıçları korur.
- **`SMART` (Akıllı transkript)**: Okunabilirlik için transkripti temizler ve yapılandırır:

  - **Aksaklıkları kaldırma**: Gereksiz kelimeleri, kekemeliği ve yanlış başlangıçları kaldırır.
  - **Satır içi kendi kendine düzeltmeler**: Konuşma sırasında yapılan düzeltmeleri doğal bir şekilde çözer.
  - **Yapılandırılmış biçimlendirme**: Listeleri, madde işaretlerini, sayıları, tarihleri ve paragraf sonlarını otomatik olarak biçimlendirir.
  - **Dil bilgisi ve büyük/küçük harf kullanımı**: Doğal büyük harf kullanımı ve noktalama işaretleri uygular.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        mode="SMART",
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    mode: 'SMART',
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      mode: 'SMART',
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

## Ses Etkinliği Algılama (VAD) stratejileri

### Otomatik VAD (varsayılan)

Varsayılan olarak, sunucu tarafında otomatik ses etkinliği algılama özelliği, konuşmacının konuşmaya başlayıp durduğunu algılar.

### Hibrit VAD

[Hibrit VAD](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=tr#hybrid-vad), sıfır gecikmeyle dönüşü sonlandırmak için sunucu tarafında otomatik konuşma başlangıcı algılamayı istemci tarafında konuşma sonu algılamayla birleştirir:

1. Ön ek ses dolgusuyla konuşma başlangıçlarını doğru şekilde algılamak ve ilk kelimeyi kesmeyi önlemek için **sunucu taraflı otomatik VAD etkin kalır**.
2. **İstemci tarafı VAD, sessizliği algılıyor**: Cihaz üzerinde yerel bir VAD, konuşmacının konuşmayı bıraktığını algıladığında istemci hemen bir `audio_stream_end` sinyali gönderir.
3. **Hızlı sonlandırma**: Sunucu, `audio_stream_end` karakterini anında sonlandırma istemi olarak değerlendirir. Varsayılan sunucu tarafı sessizlik bekleme süresini atlayarak sonlandırılmış transkripti minimum gecikmeyle döndürür.
4. **Yedek**: İstemci VAD'si tetiklenmezse sunucu tarafı VAD'si otomatik yedek olarak işlev görür.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Stream audio chunks...
    await session.send_realtime_input(
        audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000")
    )

    # When client-side VAD detects end of speech, send audio_stream_end:
    await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {},
};

// Stream audio...
session.sendRealtimeInput({
  audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
});

// When client VAD detects end of speech, send audioStreamEnd:
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
  }
}));

// When client VAD detects end of speech, send audioStreamEnd:
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

### Manuel VAD (Bas-Konuş)

Telsiz arayüzleri veya konuşmak için bas düğmeleri için otomatik VAD'yi tamamen devre dışı bırakın ve `activity_start` ile `activity_end` kullanarak konuşma sırası sınırlarını açıkça kontrol edin:

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    realtime_input_config=types.RealtimeInputConfig(
        automatic_activity_detection=types.AutomaticActivityDetection(
            disabled=True
        )
    ),
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Button pressed: signal speech start
    await session.send_realtime_input(activity_start=types.ActivityStart())

    # Stream audio chunks...
    await session.send_realtime_input(audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000"))

    # Button released: signal speech end
    await session.send_realtime_input(activity_end=types.ActivityEnd())
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    },
  },
  inputAudioTranscription: {},
};

// Signal speech start
session.sendRealtimeInput({ activityStart: {} });

// Stream audio...

// Signal speech end
session.sendRealtimeInput({ activityEnd: {} });
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    realtimeInputConfig: {
      automaticActivityDetection: {
        disabled: true,
      },
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Button pressed: signal speech start
websocket.send(JSON.stringify({
  realtimeInput: {
    activityStart: {},
  },
}));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' },
  },
}));

// Button released: signal speech end
websocket.send(JSON.stringify({
  realtimeInput: {
    activityEnd: {},
  },
}));
```

## İstemci uygulamalarındaki kısa ömürlü jetonlar

Doğrudan mikrofondan yayın yapan mobil veya web uygulamaları gibi istemciden sunucuya uygulamalarda, API anahtarınızı istemci kodunda göstermemek için [geçici jetonlar](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=tr) kullanın.

İstemci bağlantısını başlatmadan önce sunucunuzda sınırlı bir kısa ömürlü jeton oluşturun:

### Python

```
import datetime
from google import genai

client = genai.Client()
expire_time = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=30)

token = client.auth_tokens.create(
    config={
        "uses": 1,
        "expire_time": expire_time,
        "live_connect_constraints": {
            "model": "gemini-3.5-transcribe-live",
            "config": {
                "response_modalities": ["TEXT"],
                "input_audio_transcription": {
                    "language_codes": [],
                },
            },
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
  config: {
    uses: 1,
    expireTime: expireTime,
    liveConnectConstraints: {
      model: 'gemini-3.5-transcribe-live',
      config: {
        responseModalities: ['TEXT'],
        inputAudioTranscription: {
          languageCodes: [],
        },
      },
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
      "model": "models/gemini-3.5-transcribe-live",
      "config": {
        "responseModalities": ["TEXT"],
        "inputAudioTranscription": {
          "languageCodes": []
        }
      }
    }
  }'
```

## Desteklenen diller

Gemini 3.5 Transcribe Live'da aşağıdaki diller ve BCP-47 dil kodları desteklenir:

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

## Parametre referansı

`input_audio_transcription` ve `realtime_input_config` alanlarını kullanarak canlı altyazıyı yapılandırın:

| Parametre | Tür | Açıklama |
| --- | --- | --- |
| `language_codes` | Dize dizisi | BCP-47 dil kodları (ör. `["en-US"]`). Atlanırsa veya boş bırakılırsa (`[]`) model, dili otomatik olarak algılar ve çok dilli konuşmayı işler. |
| `custom_vocabulary` | Dize dizisi | Konuşma tanımayı etkilemek için 1.000'e kadar özel terim, kısaltma, marka adı veya özel isim. |
| `mode` | Dize | Metne dönüştürme modu: `"VERBATIM"` (varsayılan) veya `"SMART"` (Akıllı metne dönüştürme). `"SMART"` olarak ayarlandığında model, gereksiz kelimeleri kaldırır, listeleri biçimlendirir ve akıcılık sorunlarını düzeltir. |
| `automatic_activity_detection.disabled` | Boole | Otomatik ses etkinliği algılamayı devre dışı bırakmak ve `activityStart` ile `activityEnd` sinyallerini manuel olarak göndermek için `true` olarak ayarlayın. |

### Sunucu yanıtı alanları

| Alan | Açıklama |
| --- | --- |
| `server_content.interim_input_transcription` | Kullanıcı aktif olarak konuşurken sürekli olarak yayınlanan, düşük gecikmeli, geçici kısmi transkripsiyon hipotezi. |
| `server_content.input_transcription` | Konuşma sırası bittiğinde sonlandırılmış, yetkili giriş transkripti yayınlanır. |

## Sınırlamalar

- **Oturum süresi:** Canlı metne dönüştürme oturumları, 10 dakikaya kadar kesintisiz yayını destekler.
- **Konuşmacı diarizasyonu:** Konuşmacı diarizasyonu, canlı yayın oturumlarında desteklenmez. Konuşmacı ayrımı için akış olmayan [Ses transkripsiyonu](https://ai.google.dev/gemini-api/docs/transcribe?hl=tr#speaker-diarization) uç noktasını kullanın.
- **Kelime düzeyinde zaman damgaları:** Kelime düzeyinde zaman damgaları, Live API üzerinden desteklenmez. Live API, ifade düzeyinde zaman damgaları (`interim_input_transcription` ve `input_transcription`) yayar.
- **Özel kelime dağarcığı:** `custom_vocabulary` içinde 1.000'e kadar terim sağlayabilirsiniz ancak en iyi sonuçlar genellikle 100 terimle elde edilir.
- **Mod uyumluluğu:** Akıllı transkripsiyon (`"mode": "SMART"`), dolgu kelimelerini kaldırır ve amaca yönelik metni biçimlendirir ancak kelime notlarıyla birlikte kullanılamaz.

## Sırada ne var?

- Akış olmayan ses dosyaları için [Gemini Transcribe belgelerini](https://ai.google.dev/gemini-api/docs/transcribe?hl=tr) okuyun.
- Sohbet eden sesli temsilciler için [Live API'ye genel bakış](https://ai.google.dev/gemini-api/docs/live-api?hl=tr) başlıklı makaleyi inceleyin.
- Anlık konuşma çevirisi için [Canlı Çeviri kılavuzunu](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=tr) okuyun.
- Live API akış fiyatlandırması için [Fiyatlandırma sayfası](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#gemini-3.5-transcribe-live)'nı kontrol edin.
- [Live API özellikleri kılavuzunu](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=tr) inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-10 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-10 UTC."],[],[]]
