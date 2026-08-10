---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=tr
fetched_at: 2026-08-10T03:24:16.266037+00:00
title: "Live API ile oturum y\u00f6netimi \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Live API ile oturum yönetimi

Live API'de oturum, giriş ve çıkışın aynı bağlantı üzerinden sürekli olarak yayınlandığı kalıcı bir bağlantıyı ifade eder ([İşleyiş şekli](https://ai.google.dev/gemini-api/docs/live?hl=tr) hakkında daha fazla bilgi edinin).
Bu benzersiz oturum tasarımı, düşük gecikme süresi sağlar ve benzersiz özellikleri destekler. Ancak oturum süresi sınırları ve erken sonlandırma gibi zorluklara da yol açabilir.
Bu kılavuzda, Canlı API'yi kullanırken ortaya çıkabilecek oturum yönetimi zorluklarının üstesinden gelmeye yönelik stratejiler ele alınmaktadır.

## Oturum ömrü

Sıkıştırma olmadan yalnızca sesli oturumlar 15 dakika, sesli ve görüntülü oturumlar ise 2 dakika ile sınırlıdır. Bu sınırların aşılması oturumu (ve dolayısıyla bağlantıyı) sonlandırır ancak oturumları sınırsız süreye uzatmak için [bağlam penceresi sıkıştırmasını](#context-window-compression) kullanabilirsiniz.

Bağlantı ömrü de yaklaşık 10 dakika ile sınırlıdır. Bağlantı sonlandırıldığında oturum da sonlandırılır. Bu durumda, [oturum devam ettirme](#session-resumption) özelliğini kullanarak tek bir oturumu birden fazla bağlantıda etkin kalacak şekilde yapılandırabilirsiniz.
Ayrıca, bağlantı sona ermeden önce [GoAway mesajı](#goaway-message) alırsınız. Bu mesaj, daha fazla işlem yapmanıza olanak tanır.

## Bağlam penceresi sıkıştırması

Daha uzun oturumlar sağlamak ve bağlantının aniden sonlandırılmasını önlemek için oturum yapılandırmasının bir parçası olarak [contextWindowCompression](https://ai.google.dev/api/live?hl=tr#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression) alanını ayarlayarak bağlam penceresi sıkıştırmasını etkinleştirebilirsiniz.

[ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=tr#contextwindowcompressionconfig) bölümünde, [kayan pencere mekanizması](https://ai.google.dev/api/live?hl=tr#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window) ve sıkıştırmayı tetikleyen [jeton sayısını](https://ai.google.dev/api/live?hl=tr#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens) yapılandırabilirsiniz.

### Python

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        # Configures compression with default parameters.
        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  contextWindowCompression: { slidingWindow: {} }
};
```

## Oturum devam ettirme

Sunucu, WebSocket bağlantısını düzenli olarak sıfırladığında oturumun sonlandırılmasını önlemek için [kurulum yapılandırması](https://ai.google.dev/api/live?hl=tr#BidiGenerateContentSetup) içindeki [sessionResumption](https://ai.google.dev/api/live?hl=tr#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption) alanını yapılandırın.

Bu yapılandırmanın iletilmesi, sunucunun [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=tr#SessionResumptionUpdate) mesajları göndermesine neden olur. Bu mesajlar, oturumu devam ettirmek için kullanılabilir. Oturum devam ettirmek için son devam ettirme jetonu, sonraki bağlantının [`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=tr#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle) olarak iletilir.

Devam ettirme jetonları, son oturumun sonlandırılmasından sonraki 2 saat boyunca geçerlidir.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

async def main():
    print(f"Connecting to the service with handle {previous_session_handle}...")
    async with client.aio.live.connect(
        model=model,
        config=types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            session_resumption=types.SessionResumptionConfig(
                # The handle of the session to resume is passed here,
                # or else None to start a new session.
                handle=previous_session_handle
            ),
        ),
    ) as session:
        while True:
            await session.send_client_content(
                turns=types.Content(
                    role="user", parts=[types.Part(text="Hello world!")]
                )
            )
            async for message in session.receive():
                # Periodically, the server will send update messages that may
                # contain a handle for the current state of the session.
                if message.session_resumption_update:
                    update = message.session_resumption_update
                    if update.resumable and update.new_handle:
                        # The handle should be retained and linked to the session.
                        return update.new_handle

                # For the purposes of this example, placeholder input is continually fed
                # to the model. In non-sample code, the model inputs would come from
                # the user.
                if message.server_content and message.server_content.turn_complete:
                    break

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

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

console.debug('Connecting to the service with handle %s...', previousSessionHandle)
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
  config: {
    responseModalities: [Modality.AUDIO],
    sessionResumption: { handle: previousSessionHandle }
    // The handle of the session to resume is passed here, or else null to start a new session.
  }
});

const inputTurns = 'Hello how are you?';
session.sendClientContent({ turns: inputTurns });

const turns = await handleTurn();
for (const turn of turns) {
  if (turn.sessionResumptionUpdate) {
    if (turn.sessionResumptionUpdate.resumable && turn.sessionResumptionUpdate.newHandle) {
      let newHandle = turn.sessionResumptionUpdate.newHandle
      // ...Store newHandle and start new session with this handle here
    }
  }
}

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## Oturum bağlantısı kesilmeden önce ileti alma

Sunucu, mevcut bağlantının yakında sonlandırılacağını belirten bir [GoAway](https://ai.google.dev/api/live?hl=tr#GoAway) mesajı gönderir. Bu mesaj, kalan süreyi belirten [timeLeft](https://ai.google.dev/api/live?hl=tr#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left) değerini içerir ve bağlantı ABORTED olarak sonlandırılmadan önce başka işlemler yapmanıza olanak tanır.

### Python

```
async for response in session.receive():
    if response.go_away is not None:
        # The connection will soon be terminated
        print(response.go_away.time_left)
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.goAway) {
    console.debug('Time left: %s\n', turn.goAway.timeLeft);
  }
}
```

## Oluşturma işlemi tamamlandığında mesaj alma

Sunucu, modelin yanıt oluşturmayı tamamladığını belirten bir [generationComplete](https://ai.google.dev/api/live?hl=tr#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete) mesajı gönderir.

### Python

```
async for response in session.receive():
    if response.server_content.generation_complete is True:
        # The generation is complete
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.generationComplete) {
    // The generation is complete
  }
}
```

## Sırada ne var?

Live API ile çalışmanın diğer yollarını öğrenmek için [Özellikler](https://ai.google.dev/gemini-api/docs/live?hl=tr) kılavuzunun tamamını, [Araç kullanımı](https://ai.google.dev/gemini-api/docs/live-tools?hl=tr) sayfasını veya [Live API yemek kitabını](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=tr) inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-01 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-01 UTC."],[],[]]
