---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=tr
fetched_at: 2026-08-10T03:23:11.741426+00:00
title: "Live API \u00f6zellikleri k\u0131lavuzu \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Live API özellikleri kılavuzu

Bu kapsamlı kılavuzda, Live API ile kullanılabilen özellikler ve yapılandırmalar ele alınmaktadır.
Genel bakış ve yaygın kullanım alanlarına ilişkin örnek kod için [Live API'yi kullanmaya başlama](https://ai.google.dev/gemini-api/docs/live?hl=tr) sayfasına bakın.

## Başlamadan önce

- **Temel kavramlar hakkında bilgi edinin:** Henüz yapmadıysanız önce [Live API'yi kullanmaya başlama](https://ai.google.dev/gemini-api/docs/live?hl=tr)  sayfasını okuyun.
  Bu doküman, Canlı API'nin temel ilkeleri, nasıl çalıştığı ve farklı [uygulama yaklaşımları](https://ai.google.dev/gemini-api/docs/live?hl=tr#implementation-approach) hakkında bilgi verir.
- **Live API'yi AI Studio'da deneyin:** Uygulama geliştirmeye başlamadan önce Live API'yi [Google AI Studio](https://aistudio.google.com/app/live?hl=tr)'da denemeniz faydalı olabilir. Google AI Studio'da Live API'yi kullanmak için **Stream**'i (Yayın) seçin.

## Model karşılaştırma

Aşağıdaki tabloda, [Gemini 3.1 Flash Live Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=tr) ve [Gemini 2.5 Flash Live Preview](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=tr) modelleri arasındaki temel farklılıklar özetlenmiştir:

| Özellik | Gemini 3.1 Flash Live Preview | Gemini 2.5 Flash Live Preview |
| --- | --- | --- |
| **[Düşünme](#native-audio-output-thinking)** | `minimal`, `low`, `medium` ve `high` gibi ayarları kullanarak düşünce derinliğini kontrol etmek için `thinkingLevel`'ı kullanır. En düşük gecikme süresi için optimizasyon amacıyla varsayılan olarak `minimal` seçilir. [Düşünme seviyeleri ve bütçeler](https://ai.google.dev/gemini-api/docs/thinking?hl=tr#levels-budgets) başlıklı makaleyi inceleyin. | Düşünme parçalarının sayısını ayarlamak için `thinkingBudget` kullanılır. Dinamik düşünme özelliği varsayılan olarak etkindir. Devre dışı bırakmak için `thinkingBudget` değerini `0` olarak ayarlayın. [Düşünme seviyeleri ve bütçeler](https://ai.google.dev/gemini-api/docs/thinking?hl=tr#levels-budgets) başlıklı makaleyi inceleyin. |
| **[Yanıt alma](https://ai.google.dev/api/live?hl=tr#bidigeneratecontentservercontent)** | Tek bir sunucu etkinliği aynı anda birden fazla içerik bölümü (ör. `inlineData` ve transkript) içerebilir. İçeriklerin eksik kalmaması için kodunuzun her etkinlikteki tüm bölümleri işlediğinden emin olun. | Her sunucu etkinliği yalnızca bir içerik bölümü içerir. Parçalar ayrı etkinlikler halinde yayınlanır. |
| **[Müşteri içeriği](#incremental-updates)** | `send_client_content` yalnızca ilk bağlam geçmişini başlatmak için desteklenir (oturum yapılandırmasında `initial_history_in_client_content` ayarının yapılması gerekir). Görüşme sırasında metin güncellemeleri göndermek için bunun yerine `send_realtime_input` simgesini kullanın. | `send_client_content`, artımlı içerik güncellemeleri göndermek ve bağlam oluşturmak için görüşme boyunca desteklenir. |
| **[Dönüş kapsamı](https://ai.google.dev/api/live?hl=tr#turncoverage)** | Varsayılan olarak `TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO` değerine ayarlanır. Modelin dönüşü, algılanan ses etkinliğini ve tüm video karelerini içerir. | Varsayılan olarak `TURN_INCLUDES_ONLY_ACTIVITY` değerine ayarlanır. Modelin yanıtı yalnızca algılanan etkinliği içerir. |
| **[Özel VAD](#disable-automatic-vad)** (`activity_start`/`activity_end`) | Desteklenir. Dönüşüm sınırlarını kontrol etmek için otomatik VAD'yi devre dışı bırakın ve `activityStart` ile `activityEnd` mesajlarını manuel olarak gönderin. | Desteklenir. Dönüşüm sınırlarını kontrol etmek için otomatik VAD'yi devre dışı bırakın ve `activityStart` ile `activityEnd` mesajlarını manuel olarak gönderin. |
| **[Otomatik VAD yapılandırması](#configure-automatic-vad)** | Desteklenir. `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms` ve `silence_duration_ms` gibi parametreleri yapılandırın. | Desteklenir. `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms` ve `silence_duration_ms` gibi parametreleri yapılandırın. |
| **[Eşzamansız işlev çağrısı](https://ai.google.dev/gemini-api/docs/live-tools?hl=tr#async-function-calling)** (`behavior: NON_BLOCKING`) | Desteklenmez. İşlev çağrıları yalnızca sıralı olarak yapılabilir. Model, araç yanıtını gönderene kadar yanıt vermeye başlamaz. | Desteklenir. İşlev çalışırken modelin etkileşime devam etmesine izin vermek için işlev tanımlamasında `behavior` değerini `NON_BLOCKING` olarak ayarlayın. `scheduling` parametresiyle (`INTERRUPT`, `WHEN_IDLE` veya `SILENT`) modelin yanıtları nasıl işleyeceğini kontrol edin. |
| **[Proaktif ses](#proactive-audio)** | Desteklenmiyor | Desteklenir. Etkinleştirildiğinde model, giriş içeriği alakalı değilse yanıt vermemeye proaktif olarak karar verebilir. `proactivity` yapılandırmasında `proactive_audio` değerini `true` olarak ayarlayın (`v1beta` gerektirir). |
| **[Duygusal diyalog](#affective-dialog)** (Affective dialogue) | Desteklenmiyor | Desteklenir. Model, yanıt stilini girişin ifadesine ve üslubuna uyacak şekilde uyarlar. Oturum yapılandırmasında `enable_affective_dialog` değerini `true` olarak ayarlayın (`v1beta` gerektirir). |

Gemini 2.5 Flash Live'dan Gemini 3.1 Flash Live'a geçiş yapmak için [taşıma kılavuzuna](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=tr#migrating) bakın.

## Bağlantı kurma

Aşağıdaki örnekte, API anahtarıyla nasıl bağlantı oluşturulacağı gösterilmektedir:

### Python

```
import asyncio
from google import genai

client = genai.Client()

model = "gemini-3.1-flash-live-preview"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## Etkileşim biçimleri

Aşağıdaki bölümlerde, Canlı API'de bulunan farklı giriş ve çıkış biçimleriyle ilgili örnekler ve destekleyici bağlamlar verilmiştir.

### Ses gönderme

Ses, ham PCM verileri (ham 16 bit PCM ses, 16 kHz, little-endian) olarak gönderilmelidir.

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

### Ses biçimleri

Live API'deki ses verileri her zaman ham, little-endian ve 16 bit PCM'dir. Ses çıkışında her zaman 24 kHz örnekleme hızı kullanılır. Giriş sesi, doğal olarak 16 kHz'dir ancak gerekirse Live API yeniden örnekleme yapacağından herhangi bir örnekleme hızı gönderilebilir. Giriş sesinin örnekleme hızını iletmek için ses içeren her [Blob](https://ai.google.dev/api/caching?hl=tr#Blob)'un MIME türünü `audio/pcm;rate=16000` gibi bir değere ayarlayın.

### Ses alma

Modelin sesli yanıtları veri parçaları olarak alınır.

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

### Kısa mesaj gönderiliyor

Metin, `send_realtime_input` (Python) veya `sendRealtimeInput` (JavaScript) kullanılarak gönderilebilir.

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

### Video gönderiliyor

Video kareleri, belirli bir kare hızında (saniyede en fazla 1 kare) ayrı resimler (ör. JPEG veya PNG) olarak gönderilir.

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

#### Artımlı içerik güncellemeleri

Metin girişi göndermek, oturum bağlamı oluşturmak veya oturum bağlamını geri yüklemek için artımlı güncellemeleri kullanın. Kısa bağlamlar için, etkinliklerin tam sırasını temsil etmek üzere adım adım etkileşimler gönderebilirsiniz:

### Python

```
turns = [
    {"role": "user", "parts": [{"text": "What is the capital of France?"}]},
    {"role": "model", "parts": [{"text": "Paris"}]},
]

await session.send_client_content(turns=turns, turn_complete=False)

turns = [{"role": "user", "parts": [{"text": "What is the capital of Germany?"}]}]

await session.send_client_content(turns=turns, turn_complete=True)
```

### JavaScript

```
let inputTurns = [
  { "role": "user", "parts": [{ "text": "What is the capital of France?" }] },
  { "role": "model", "parts": [{ "text": "Paris" }] },
]

session.sendClientContent({ turns: inputTurns, turnComplete: false })

inputTurns = [{ "role": "user", "parts": [{ "text": "What is the capital of Germany?" }] }]

session.sendClientContent({ turns: inputTurns, turnComplete: true })
```

Daha uzun bağlamlarda, sonraki etkileşimler için bağlam penceresini boşaltmak amacıyla tek bir ileti özeti sağlamanız önerilir. Oturum bağlamını yüklemenin başka bir yöntemi için [Oturum Devam Ettirme](https://ai.google.dev/gemini-api/docs/live-session?hl=tr#session-resumption)'ye bakın.

### Sesten dönüştürülen metinler

Model yanıtının yanı sıra hem ses çıkışının hem de ses girişinin transkriptlerini alabilirsiniz.

Modelin ses çıkışının metne dönüştürülmesini etkinleştirmek için kurulum yapılandırmasında `output_audio_transcription` gönderin. Metne dönüştürme dili, modelin yanıtından çıkarılır.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "output_audio_transcription": {}
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        message = "Hello? Gemini are you there?"

        await session.send_client_content(
            turns={"role": "user", "parts": [{"text": message}]}, turn_complete=True
        )

        async for response in session.receive():
            if response.server_content.model_turn:
                print("Model turn:", response.server_content.model_turn)
            if response.server_content.output_transcription:
                print("Transcript:", response.server_content.output_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  outputAudioTranscription: {}
};

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  const inputTurns = 'Hello how are you?';
  session.sendClientContent({ turns: inputTurns });

  const turns = await handleTurn();

  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.outputTranscription) {
      console.debug('Received output transcription: %s\n', turn.serverContent.outputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

Modelin ses girişinin metne dönüştürülmesini etkinleştirmek için kurulum yapılandırmasında `input_audio_transcription` gönderin.

### Python

```
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "input_audio_transcription": {},
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_data = Path("16000.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_data, mime_type='audio/pcm;rate=16000')
        )

        async for msg in session.receive():
            if msg.server_content.input_transcription:
                print('Transcript:', msg.server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  inputAudioTranscription: {}
};

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("16000.wav");

  // Ensure audio conforms to API requirements (16-bit PCM, 16kHz, mono)
  const wav = new WaveFile();
  wav.fromBuffer(fileBuffer);
  wav.toSampleRate(16000);
  wav.toBitDepth("16");
  const base64Audio = wav.toBase64();

  // If already in correct format, you can use this:
  // const fileBuffer = fs.readFileSync("sample.pcm");
  // const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }
  );

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
    else if (turn.serverContent && turn.serverContent.inputTranscription) {
      console.debug('Received input transcription: %s\n', turn.serverContent.inputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

### Sesi ve dili değiştirme

[Yerel ses çıkışı](#native-audio-output) modelleri, [Text-to-Speech (TTS)](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr#voices) modellerimiz için kullanılabilen tüm sesleri destekler. Tüm sesleri [AI Studio](https://aistudio.google.com/app/live?hl=tr)'da dinleyebilirsiniz.

Bir ses belirtmek için oturum yapılandırmasının bir parçası olarak `speechConfig` nesnesinde ses adını ayarlayın:

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "speech_config": {
        "voice_config": {"prebuilt_voice_config": {"voice_name": "Kore"}}
    },
}
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Kore" } } }
};
```

Live API [birden fazla dili](#supported-languages) destekler.
[Yerel ses çıkışı](#native-audio-output) modelleri, uygun dili otomatik olarak seçer ve dil kodunun açıkça ayarlanmasını desteklemez.

## Doğal ses özellikleri

En yeni modellerimizde [doğal ses çıkışı](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=tr) özelliği bulunur. Bu özellik, doğal ve gerçekçi sesler üretir ve çok dilli performansı iyileştirir.

### Düşünen

Gemini 3.1 modelleri, düşünce derinliğini kontrol etmek için `thinkingLevel` kullanır. `minimal`, `low`, `medium` ve `high` gibi ayarlar vardır. En düşük gecikme süresi için varsayılan ayar `minimal`'dır. Gemini 2.5 modelleri, düşünme parçalarının sayısını ayarlamak için `thinkingBudget` kullanır. Seviyeler ve bütçeler hakkında daha fazla bilgi için [Seviyeler ve bütçeler hakkında düşünceler](https://ai.google.dev/gemini-api/docs/thinking?hl=tr#levels-budgets) başlıklı makaleyi inceleyin.

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
    )
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio input and receive audio
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
  },
};

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: ...,
  });

  // Send audio input and receive audio

  session.close();
}

main();
```

Ayrıca, yapılandırmanızda `includeThoughts` seçeneğini `true` olarak ayarlayarak düşünce özetlerini etkinleştirebilirsiniz. Daha fazla bilgi için [düşünce özetleri](https://ai.google.dev/gemini-api/docs/thinking?hl=tr#summaries) bölümüne bakın:

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
        include_thoughts=True
    )
)
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
    includeThoughts: true,
  },
};
```

### Moda uygun diyalog

Bu özellik, Gemini'ın yanıt stilini giriş ifadesine ve tonuna göre uyarlamasını sağlar.

Duygusal diyaloğu kullanmak için API sürümünü `v1beta` olarak ayarlayın ve kurulum mesajında `enable_affective_dialog` değerini `true` olarak ayarlayın:

### Python

```
client = genai.Client(http_options={"api_version": "v1beta"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    enable_affective_dialog=True
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1beta"} });

const config = {
  responseModalities: [Modality.AUDIO],
  enableAffectiveDialog: true
};
```

### Proaktif ses

Bu özellik etkinleştirildiğinde Gemini, içerik alakalı değilse yanıt vermemeye proaktif olarak karar verebilir.

Kullanmak için API sürümünü `v1beta` olarak ayarlayın, kurulum mesajında `proactivity` alanını yapılandırın ve `proactive_audio` değerini `true` olarak ayarlayın:

### Python

```
client = genai.Client(http_options={"api_version": "v1beta"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={'proactive_audio': True}
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1beta"} });

const config = {
  responseModalities: [Modality.AUDIO],
  proactivity: { proactiveAudio: true }
}
```

## Canlı çeviri

Live API, sözlü sohbetlerin gerçek zamanlı ve düşük gecikmeli çevirisini destekler. Bu özellik, anlık sesli çeviri uygulamaları oluşturmanıza olanak tanır.

Daha fazla bilgi ve örnek için [Canlı Çeviri kılavuzuna](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=tr) bakın.

## Ses Etkinliği Algılama (VAD)

Ses Etkinliği Algılama (VAD), modelin bir kişinin konuştuğu zamanı tanımasını sağlar. Bu, kullanıcının modeli istediği zaman kesmesine olanak tanıdığı için doğal sohbetler oluşturmak açısından önemlidir.

VAD bir kesinti algıladığında devam eden oluşturma işlemi iptal edilir ve silinir. Yalnızca istemciye gönderilmiş olan bilgiler oturum geçmişinde saklanır. Ardından sunucu, kesintiyi bildirmek için [`BidiGenerateContentServerContent`](https://ai.google.dev/api/live?hl=tr#bidigeneratecontentservercontent) mesajı gönderir.

Gemini sunucusu, bekleyen işlev çağrılarını siler ve iptal edilen çağrıların kimliklerini içeren bir `BidiGenerateContentServerContent` mesajı gönderir.

### Python

```
async for response in session.receive():
    if response.server_content.interrupted is True:
        # The generation was interrupted

        # If realtime playback is implemented in your application,
        # you should stop playing audio and clear queued playback here.
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.interrupted) {
    // The generation was interrupted

    // If realtime playback is implemented in your application,
    // you should stop playing audio and clear queued playback here.
  }
}
```

### Otomatik VAD

Model, varsayılan olarak sürekli bir ses girişi akışında otomatik olarak VAD gerçekleştirir. VAD, [`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/api/live?hl=tr#RealtimeInputConfig.AutomaticActivityDetection)
[kurulum yapılandırması](https://ai.google.dev/api/live?hl=tr#BidiGenerateContentSetup) alanı ile yapılandırılabilir.

Ses akışı bir saniyeden uzun süre duraklatıldığında (örneğin, kullanıcı mikrofonu kapattığı için) önbelleğe alınan sesleri temizlemek için bir [`audioStreamEnd`](https://ai.google.dev/api/live?hl=tr#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end) etkinliği gönderilmelidir. İstemci, ses verilerini göndermeye istediği zaman devam edebilir.

### Python

```
# example audio file to try:
# URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
# !wget -q $URL -O sample.pcm
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_bytes = Path("sample.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
        )

        # if stream gets paused, send:
        # await session.send_realtime_input(audio_stream_end=True)

        async for response in session.receive():
            if response.text is not None:
                print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
// example audio file to try:
// URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
// !wget -q $URL -O sample.pcm
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        responseQueue.push(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("sample.pcm");
  const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }

  );

  // if stream gets paused, send:
  // session.sendRealtimeInput({ audioStreamEnd: true })

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

`send_realtime_input` ile API, VAD'ye göre sesli yanıtlara otomatik olarak yanıt verir. `send_client_content`, iletileri model bağlamına sırayla eklerken `send_realtime_input`, deterministik sıralama pahasına yanıt verme hızı için optimize edilmiştir.

### Otomatik VAD yapılandırması

VAD etkinliği üzerinde daha fazla kontrol sahibi olmak için aşağıdaki parametreleri yapılandırabilirsiniz. Daha fazla bilgi için [API referansına](https://ai.google.dev/api/live?hl=tr#automaticactivitydetection) bakın.

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {
        "automatic_activity_detection": {
            "disabled": False, # default
            "start_of_speech_sensitivity": types.StartSensitivity.START_SENSITIVITY_LOW,
            "end_of_speech_sensitivity": types.EndSensitivity.END_SENSITIVITY_LOW,
            "prefix_padding_ms": 20,
            "silence_duration_ms": 100,
        }
    }
}
```

### JavaScript

```
import { GoogleGenAI, Modality, StartSensitivity, EndSensitivity } from '@google/genai';

const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: false, // default
      startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_LOW,
      endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_LOW,
      prefixPaddingMs: 20,
      silenceDurationMs: 100,
    }
  }
};
```

### Otomatik VAD'yi devre dışı bırakma

Alternatif olarak, kurulum mesajında `realtimeInputConfig.automaticActivityDetection.disabled` değeri `true` olarak ayarlanarak otomatik VAD devre dışı bırakılabilir. Bu yapılandırmada, istemci kullanıcı konuşmasını algılamaktan ve uygun zamanlarda [`activityStart`](https://ai.google.dev/api/live?hl=tr#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start) ve [`activityEnd`](https://ai.google.dev/api/live?hl=tr#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end) mesajlarını göndermekten sorumludur. Bu yapılandırmada `audioStreamEnd` gönderilmez. Bunun yerine, akışta meydana gelen kesintiler `activityEnd` mesajıyla işaretlenir.

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {"automatic_activity_detection": {"disabled": True}},
}

async with client.aio.live.connect(model=model, config=config) as session:
    # ...
    await session.send_realtime_input(activity_start=types.ActivityStart())
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )
    await session.send_realtime_input(activity_end=types.ActivityEnd())
    # ...
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    }
  }
};

session.sendRealtimeInput({ activityStart: {} })

session.sendRealtimeInput(
  {
    audio: {
      data: base64Audio,
      mimeType: "audio/pcm;rate=16000"
    }
  }

);

session.sendRealtimeInput({ activityEnd: {} })
```

### VAD parametrelerini ve bunların kalite üzerindeki etkisini anlama

Otomatik VAD kullanılırken sesin modele gönderilmeden önce konuşma dönüşlerine nasıl bölüneceğini kontrol eden iki temel parametre vardır:

- **`prefixPaddingMs`**: Konuşma algılanmadan *önce* eklenecek ses miktarı. Bu "geriye bakma" özelliği, modelin konuşmanın başlangıcını (VAD tetiklenmeden önce başlayabilen ilk hece dahil) tam olarak yakalamasını sağlar. `0` değeri, kelimelerin başlangıcının kırpılmasına neden olabilir.
- **`silenceDurationMs`**: Sunucunun, konuşma sırasını sonlandırmadan önce sessizlik boyunca ne kadar bekleyeceği. Bu değer, sistemin cümle ortasındaki doğal duraksamalara (ör. düşünme, nefes alma veya cümle sınırları) ne kadar toleranslı olduğunu belirler.

#### `silenceDurationMs`'nın ses kalitesi üzerindeki etkisi

`silenceDurationMs` değeri, modelin işleme için aldığı ses parçalarının boyutunu ve eksiksizliğini doğrudan etkiler:

- **Önerilen (500 ms-800 ms):** İyi bir denge sağlar. Model, gecikmeyi makul düzeyde tutarken bağlam açısından zengin ve eksiksiz ses parçaları alır. Sunucunun dahili varsayılan değeri yaklaşık 800 ms'dir.
- **Çok düşük (ör. 100 ms-200 ms):** Sistem, doğal duraklamalar sırasında konuşma dönüşlerini sonlandırarak tek bir ifadeyi birden fazla küçük ses parçasına böler. Model bu parçaları ayrı ayrı alır. Bu durumda, parçalar arası bağlam kaybolur ve transkripsiyon ile yanıt kalitesi düşer.
- **Çok yüksek (ör.2000 ms+):** Sistem, kullanıcı konuşmayı bıraktıktan sonra uzun süre bekler. Bu durum, model yanıt vermeden önce algılanan gecikmeyi artırır.

#### Manuel (istemci tarafı) VAD ile ilgili en iyi uygulamalar

Otomatik VAD'yi devre dışı bıraktığınızda ve `activityStart`/`activityEnd` sinyallerini kendi istemci tarafı ses algılama özelliğinizden yönettiğinizde, sunucunun yerleşik ses arabelleğe alma mekanizmalarının atlandığını unutmayın. Bunun anlamı şudur:

1. **Konuşma öncesi arabellek yok:** Sunucu artık algılanan konuşma başlangıcından önce ses eklemiyor. Müşteriniz, `activityStart` göndermeden önce yeterli ses bağlamı eklemelidir.
2. **Sessizliğe tolerans yok:** Sunucu, `activityEnd` sinyalinize ek bekleme olmadan anında yanıt verir. İstemci tarafındaki VAD'niz agresif bir konuşma sonu eşiği kullanıyorsa (ör. 200 ms sessizlik), konuşma doğal duraklamalar sırasında cümlenin ortasında kesilebilir.

Manuel VAD ile ses kalitesini korumak için istemcinizin ses etkinliği algılayıcısında en az **500 ms**'lik bir konuşma sonu sessizlik eşiği kullanın.
Bu değerin altındaki eşikler genellikle transkripsiyon ve model yanıt kalitesini düşüren parçalanmış seslere neden olur.

## Jeton sayısı

Tüketilen jetonların toplam sayısını, döndürülen sunucu mesajının [usageMetadata](https://ai.google.dev/api/live?hl=tr#usagemetadata) alanında bulabilirsiniz.

### Python

```
async for message in session.receive():
    # The server will periodically send messages that include UsageMetadata.
    if message.usage_metadata:
        usage = message.usage_metadata
        print(
            f"Used {usage.total_token_count} tokens in total. Response token breakdown:"
        )
        for detail in usage.response_tokens_details:
            match detail:
                case types.ModalityTokenCount(modality=modality, token_count=count):
                    print(f"{modality}: {count}")
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.usageMetadata) {
    console.debug('Used %s tokens in total. Response token breakdown:\n', turn.usageMetadata.totalTokenCount);

    for (const detail of turn.usageMetadata.responseTokensDetails) {
      console.debug('%s\n', detail);
    }
  }
}
```

## Medya çözünürlüğü

Oturum yapılandırmasının bir parçası olarak `mediaResolution` alanını ayarlayarak giriş medyası için medya çözünürlüğünü belirtebilirsiniz:

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "media_resolution": types.MediaResolution.MEDIA_RESOLUTION_LOW,
}
```

### JavaScript

```
import { GoogleGenAI, Modality, MediaResolution } from '@google/genai';

const config = {
    responseModalities: [Modality.AUDIO],
    mediaResolution: MediaResolution.MEDIA_RESOLUTION_LOW,
};
```

## Sınırlamalar

Projenizi planlarken Canlı API'nin aşağıdaki sınırlamalarını göz önünde bulundurun.

### Yanıt biçimleri

Yerel ses modelleri yalnızca `AUDIO` yanıt biçimini destekler. Model yanıtını metin olarak almak istiyorsanız [çıkış sesini metne dönüştürme](#audio-transcription) özelliğini kullanın.

### İstemci kimlik doğrulaması

Live API, varsayılan olarak yalnızca sunucudan sunucuya kimlik doğrulama sağlar. Live API uygulamanızı [istemciden sunucuya yaklaşımı](https://ai.google.dev/gemini-api/docs/live?hl=tr#implementation-approach) kullanarak uyguluyorsanız güvenlik risklerini azaltmak için [geçici jetonlar](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=tr) kullanmanız gerekir.

### Oturum süresi

Yalnızca sesli oturumlar 15 dakika, sesli ve görüntülü oturumlar ise 2 dakika ile sınırlıdır.
Ancak oturum süresinin sınırsız uzatılması için farklı [oturum yönetimi teknikleri](https://ai.google.dev/gemini-api/docs/live-session?hl=tr) yapılandırabilirsiniz.

### Bağlam penceresi

Bir oturumun bağlam penceresi sınırı şöyledir:

- [Yerel ses çıkışı](#native-audio-output) modelleri için 128.000 jeton
- Diğer Live API modelleri için 32.000 jeton

## Desteklenen diller

Live API aşağıdaki 97 dili destekler.

| Dil | BCP-47 Kodu | Dil | BCP-47 Kodu |
| --- | --- | --- | --- |
| Afrikaanca | `af` | Letonca | `lv` |
| Akan | `ak` | Litvanca | `lt` |
| Arnavutça | `sq` | Makedonca | `mk` |
| Amharca | `am` | Malayca | `ms` |
| Arapça | `ar` | Malayalamca | `ml` |
| Ermenice | `hy` | Maltaca | `mt` |
| Assamca | `as` | Maori | `mi` |
| Azerice | `az` | Marathi | `mr` |
| Baskça | `eu` | Moğolca | `mn` |
| Belarusça | `be` | Nepalce | `ne` |
| Bengalce | `bn` | Norveççe | `no` |
| Boşnakça | `bs` | Oriya | `or` |
| Bulgarca | `bg` | Oromca | `om` |
| Burmaca | `my` | Peştuca | `ps` |
| Katalanca | `ca` | Farsça | `fa` |
| Sabuanca | `ceb` | Lehçe | `pl` |
| Çince | `zh` | Portekizce | `pt` |
| Hırvatça | `hr` | Pencapça | `pa` |
| Çekya | `cs` | Keçuva dili | `qu` |
| Danca | `da` | Rumence | `ro` |
| Felemenkçe | `nl` | Romanşça | `rm` |
| İngilizce | `en` | Rusça | `ru` |
| Estonca | `et` | Sırpça | `sr` |
| Faroese | `fo` | Sindice | `sd` |
| Filipince | `fil` | Seylanca | `si` |
| Fince | `fi` | Slovakça | `sk` |
| Fransızca | `fr` | Slovence | `sl` |
| Galiçyaca | `gl` | Somalice | `so` |
| Gürcüce | `ka` | Güney Sotho dili | `st` |
| Almanca | `de` | İspanyolca | `es` |
| Greek | `el` | Swahili | `sw` |
| Güceratça | `gu` | İsveççe | `sv` |
| Hausaca | `ha` | Tacikçe | `tg` |
| İbranice | `iw` | Tamilce | `ta` |
| Hintçe | `hi` | Telugu dili | `te` |
| Macarca | `hu` | Tayca | `th` |
| İzlandaca | `is` | Tsvana | `tn` |
| Endonezce | `id` | Türkçe | `tr` |
| İrlandaca | `ga` | Türkmence | `tk` |
| İtalyanca | `it` | Ukraynaca | `uk` |
| Japonca | `ja` | Urduca | `ur` |
| Kannada | `kn` | Özbekçe | `uz` |
| Kazakça | `kk` | Vietnamca | `vi` |
| Kmerce | `km` | Galce | `cy` |
| Ruandaca | `rw` | Batı Frizcesi | `fy` |
| Korece | `ko` | Wolof dili | `wo` |
| Kürtçe | `ku` | Yorubaca | `yo` |
| Kırgızca | `ky` | Zulu | `zu` |
| Laoca | `lo` |  |  |

## Sırada ne var?

- Canlı API'yi etkili bir şekilde kullanmayla ilgili temel bilgiler için [Araç Kullanımı](https://ai.google.dev/gemini-api/docs/live-tools?hl=tr) ve [Oturum Yönetimi](https://ai.google.dev/gemini-api/docs/live-session?hl=tr) kılavuzlarını okuyun.
- Live API'yi [Google AI Studio](https://aistudio.google.com/app/live?hl=tr)'da deneyin.
- Live API modelleri hakkında daha fazla bilgi için Modeller sayfasındaki [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-native-audio) bölümüne bakın.
- [Live API çözüm kitabında](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=tr), [Live API Tools çözüm kitabında](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=tr) ve [Live API'yi kullanmaya başlama komut dosyasında](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py) daha fazla örnek deneyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-31 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-31 UTC."],[],[]]
