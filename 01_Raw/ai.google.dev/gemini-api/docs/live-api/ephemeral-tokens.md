---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=tr
fetched_at: 2026-09-14T05:36:18.916834+00:00
title: "Ge\u00e7ici jetonlar \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Geçici jetonlar

Geçici jetonlar, Gemini API'ye [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) üzerinden erişmek için kullanılan kısa ömürlü kimlik doğrulama jetonlarıdır. Bunlar, doğrudan bir kullanıcının cihazından API'ye ([istemciden sunucuya](https://ai.google.dev/gemini-api/docs/live?hl=tr#implementation-approach)
uygulaması) bağlanırken güvenliği artırmak için tasarlanmıştır. Kısa ömürlü jetonlar, standart API anahtarları gibi web tarayıcıları veya mobil uygulamalar gibi istemci tarafı uygulamalardan çıkarılabilir. Ancak kısa ömürlü jetonlar hızlı bir şekilde sona erdiğinden ve kısıtlanabildiğinden üretim ortamındaki güvenlik risklerini önemli ölçüde azaltır. API anahtarı güvenliğini artırmak için bunları, Live API'ye doğrudan istemci tarafı uygulamalarından erişirken kullanmanız gerekir.

## Geçici jetonların işleyiş şekli

Geçici jetonların genel olarak işleyiş şekli:

1. İstemciniz (ör. web uygulaması) arka ucunuzda kimliğini doğrular.
2. Arka ucunuz, Gemini API'nin sağlama hizmetinden kısa ömürlü bir jeton ister.
3. Gemini API, kısa ömürlü bir jeton yayınlar.
4. Arka uçunuz, Live API'ye WebSocket bağlantıları için jetonu istemciye gönderir. Bunu, API anahtarınızı kısa ömürlü bir jetonla değiştirerek yapabilirsiniz.
5. İstemci daha sonra jetonu API anahtarı gibi kullanır.

![Geçici jetonlara genel bakış](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=tr)

Bu, güvenliği artırır. Çünkü jeton, istemci tarafında dağıtılan uzun ömürlü bir API anahtarının aksine, çıkarılsa bile kısa ömürlüdür. İstemci verileri doğrudan Gemini'a gönderdiğinden bu durum gecikmeyi de azaltır ve arka uçlarınızın gerçek zamanlı verileri proxy'lemesi gerekmez.

## Kısa ömürlü jeton oluşturma

Gemini'dan kısa ömürlü jeton alma işleminin basitleştirilmiş bir örneğini aşağıda bulabilirsiniz.
Varsayılan olarak, bu istekteki jetonu (`newSessionExpireTime`) kullanarak yeni Live API oturumları başlatmak için 1 dakikanız, bu bağlantı üzerinden (`expireTime`) mesaj göndermek için ise 30 dakikanız olur.

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
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
    "newSessionExpireTime": "YYYY-MM-DDTHH:MM:SSZ"
  }'
```

`expireTime` değeri kısıtlamaları, varsayılanları ve diğer alan özellikleri için [API referansına](https://ai.google.dev/api/live?hl=tr#ephemeral-auth-tokens) bakın.
`expireTime` zaman aralığında, her 10 dakikada bir aramayı yeniden bağlamanız gerekir (bu işlem, `uses: 1` olsa bile aynı jetonla yapılabilir). [`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=tr#session-resumption)

Geçici jetonları bir dizi yapılandırmaya kilitlemek de mümkündür. Bu, uygulamanızın güvenliğini daha da artırmak ve sistem talimatlarınızı sunucu tarafında tutmak için faydalı olabilir.

### Python

```
from google import genai

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'response_modalities':['AUDIO']
        }
    },
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.1-flash-live-preview',
            config: {
                sessionResumption: {},
                responseModalities: ['AUDIO']
            }
        },
    }
});

// You'll need to pass the value under token.name back to your client to use it
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
      "model": "models/gemini-3.1-flash-live-preview",
      "config": {
        "sessionResumption": {},
        "responseModalities": ["AUDIO"]
      }
    }
  }'
```

Ayrıca, alanların bir alt kümesini de kilitleyebilirsiniz. Daha fazla bilgi için [SDK dokümanlarına](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields) bakın.

## Geçici jetonla Live API'ye bağlanma

Geçici bir jetonunuz olduğunda, bunu API anahtarı gibi kullanırsınız (ancak yalnızca canlı API'de ve yalnızca API'nin `v1beta` sürümünde çalıştığını unutmayın).

Geçici jetonların kullanılması yalnızca [istemciden sunucuya uygulama](https://ai.google.dev/gemini-api/docs/live?hl=tr#implementation-approach) yaklaşımını izleyen uygulamalar dağıtılırken değer katar.

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

Daha fazla örnek için [Live API'yi kullanmaya başlama](https://ai.google.dev/gemini-api/docs/live?hl=tr) bölümüne bakın.

## En iyi uygulamalar

- `expire_time` parametresini kullanarak kısa bir geçerlilik süresi ayarlayın.
- Jetonların süresi dolduğunda temel hazırlık işleminin yeniden başlatılması gerekir.
- Kendi arka uç sisteminiz için güvenli kimlik doğrulamayı doğrulayın. Kısa ömürlü jetonlar yalnızca arka uç kimlik doğrulama yönteminiz kadar güvenlidir.
- Genel olarak, bu yol genellikle güvenli kabul edildiğinden arka uçtan Gemini'a bağlantılar için kısa ömürlü jeton kullanmaktan kaçının.

## Sınırlamalar

Geçici jetonlar şu anda yalnızca [Live API](https://ai.google.dev/gemini-api/docs/live?hl=tr) ile uyumludur.

## Sırada ne var?

- Daha fazla bilgi için Live API [referansındaki](https://ai.google.dev/api/live?hl=tr#ephemeral-auth-tokens) geçici jetonlar bölümünü inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
