---
source_url: https://ai.google.dev/gemini-api/docs/safety-settings?hl=tr
fetched_at: 2026-05-11T05:02:21.835784+00:00
title: "G\u00fcvenlik ayarlar\u0131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Güvenlik ayarları

Gemini API, uygulamanızın daha kısıtlayıcı veya daha az kısıtlayıcı bir güvenlik yapılandırması gerektirip gerektirmediğini belirlemek için prototip oluşturma aşamasında ayarlayabileceğiniz güvenlik ayarları sunar. Belirli içerik türlerini kısıtlamak veya bunlara izin vermek için bu ayarları dört filtre kategorisinde düzenleyebilirsiniz.

Bu kılavuzda, Gemini API'nin güvenlik ayarlarını ve filtrelemeyi nasıl işlediği ve uygulamanızın güvenlik ayarlarını nasıl değiştirebileceğiniz açıklanmaktadır.

## Güvenlik filtreleri

Gemini API'nin ayarlanabilir güvenlik filtreleri aşağıdaki kategorileri kapsar:

| Kategori | Açıklama |
| --- | --- |
| Taciz | Kimliği ve/veya korunan özellikleri hedef alan olumsuz veya zararlı yorumlar |
| Nefret söylemi | Kaba, saygısız veya küfürlü içerik |
| Müstehcen | Cinsel eylemlere veya diğer müstehcen içeriklere referanslar içeriyor. |
| Tehlikeli | Zararlı eylemleri teşvik eden, kolaylaştıran veya destekleyen içerikler |

Bu kategoriler [`HarmCategory`](https://ai.google.dev/api/rest/v1/HarmCategory?hl=tr) içinde tanımlanır. Kullanım alanınıza göre ayarlamalar yapmak için bu filtreleri kullanabilirsiniz. Örneğin, video oyunu diyaloğu oluşturuyorsanız oyunun doğası gereği *Tehlikeli* olarak derecelendirilen daha fazla içeriğe izin vermeyi kabul edebilirsiniz.

Ayarlanabilir güvenlik filtrelerine ek olarak, Gemini API'de çocukların güvenliğini tehlikeye atan içerikler gibi temel zararlara karşı yerleşik korumalar bulunur.
Bu tür zararlar her zaman engellenir ve ayarlanamaz.

### İçerik güvenliği filtreleme düzeyi

Gemini API, içeriğin güvenli olmama olasılık düzeyini `HIGH`, `MEDIUM`, `LOW` veya `NEGLIGIBLE` olarak sınıflandırır.

Gemini API, içeriğin güvenli olmama olasılığına göre içeriği engeller. İçeriğin ne kadar zararlı olduğu dikkate alınmaz. Zararın ciddiyeti yüksek olsa bile bazı içeriklerin güvenli olmama olasılığı düşük olabilir. Bu nedenle, bu durumu göz önünde bulundurmak önemlidir. Örneğin, şu cümleleri karşılaştıralım:

1. Robot bana yumruk attı.
2. Robot beni kesti.

İlk cümle güvenli olmama olasılığı daha yüksek olsa da ikinci cümlenin şiddet açısından daha ciddi olduğunu düşünebilirsiniz.
Bu nedenle, son kullanıcılara zarar vermeyi en aza indirirken temel kullanım alanlarınızı desteklemek için uygun engelleme düzeyinin ne olduğunu dikkatlice test etmeniz ve değerlendirmeniz önemlidir.

### İstek başına güvenlik filtreleme

API'ye yaptığınız her istek için güvenlik ayarlarını düzenleyebilirsiniz. İstek gönderdiğinizde içerik analiz edilir ve içeriğe güvenlik derecesi atanır. Güvenlik derecelendirmesi, zarar sınıflandırmasının kategorisini ve olasılığını içerir. Örneğin, içerik taciz kategorisinin yüksek olasılıkla güvenli olmaması nedeniyle engellendiyse döndürülen güvenlik derecelendirmesinde kategori `HARASSMENT`'ya eşit olur ve zarar olasılığı `HIGH` olarak ayarlanır.

Modelin doğasında bulunan güvenlik nedeniyle ek filtreler varsayılan olarak **Kapalı**'dır.
Bu ayarları etkinleştirmeyi seçerseniz sistemi, güvenli olmama olasılığına göre içerikleri engelleyecek şekilde yapılandırabilirsiniz. Varsayılan model davranışı çoğu kullanım alanını kapsar. Bu nedenle, bu ayarları yalnızca uygulamanızda tutarlılık gerekiyorsa değiştirmeniz gerekir.

Aşağıdaki tabloda, her kategori için ayarlayabileceğiniz engelleme ayarları açıklanmaktadır. Örneğin, **Nefret söylemi** kategorisi için engelleme ayarını **Birkaçını engelle** olarak belirlerseniz nefret söylemi içeriği olma olasılığı yüksek olan her şey engellenir. Ancak olasılığı daha düşük olan her şeye izin verilir.

| Eşik (Google AI Studio) | Eşik (API) | Açıklama |
| --- | --- | --- |
| Kapalı | `OFF` | Güvenlik filtresini devre dışı bırakma |
| Hiçbirini engelleme | `BLOCK_NONE` | Güvenli olmayan içerik olasılığına bakılmaksızın her zaman göster |
| Birkaçını engelle | `BLOCK_ONLY_HIGH` | İçeriğin güvenli olmama olasılığı yüksekse engelle |
| Bazılarını engelleme | `BLOCK_MEDIUM_AND_ABOVE` | İçeriğin güvenli olmama olasılığı orta veya yüksekse engelle |
| Çoğunu engelle | `BLOCK_LOW_AND_ABOVE` | İçeriğin güvenli olmama olasılığı düşük, orta veya yüksekse engelle |
| Yok | `HARM_BLOCK_THRESHOLD_UNSPECIFIED` | Eşik belirtilmediyse varsayılan eşik kullanılarak engelleme yapılır. |

Eşik ayarlanmazsa Gemini 2.5 ve 3 modelleri için varsayılan engelleme eşiği **Kapalı** olur.

Bu ayarları, üretken hizmete yaptığınız her istek için belirleyebilirsiniz.
Ayrıntılar için [`HarmBlockThreshold`](https://ai.google.dev/api/generate-content?hl=tr#harmblockthreshold) API referansına bakın.

### Güvenlikle ilgili geri bildirim

[`generateContent`](https://ai.google.dev/api/generate-content?hl=tr#method:-models.generatecontent)
güvenlik geri bildirimi içeren
[`GenerateContentResponse`](https://ai.google.dev/api/generate-content?hl=tr#generatecontentresponse) döndürür.

İstem geri bildirimi, [`promptFeedback`](https://ai.google.dev/api/generate-content?hl=tr#promptfeedback)'e dahil edilir. `promptFeedback.blockReason` ayarlanmışsa istemin içeriği engellenmiştir.

Yanıt adayı geri bildirimi, [`Candidate.finishReason`](https://ai.google.dev/api/generate-content?hl=tr#candidate) ve [`Candidate.safetyRatings`](https://ai.google.dev/api/generate-content?hl=tr#candidate)'a dahil edilir. Yanıt içeriği engellendiyse ve `finishReason` `SAFETY` ise daha fazla bilgi için `safetyRatings` öğesini inceleyebilirsiniz. Engellenen içerik geri yüklenmez.

## Güvenlik ayarlarını düzenleme

Bu bölümde, hem Google AI Studio'da hem de kodunuzda güvenlik ayarlarının nasıl düzenleneceği açıklanmaktadır.

### Google AI Studio

Güvenlik ayarlarını Google AI Studio'da yapabilirsiniz.

**Çalıştırma ayarları** panelindeki **Gelişmiş ayarlar** bölümünde **Güvenlik ayarları**'nı tıklayarak **Çalıştırma
güvenlik ayarları** modalını açın. Modalda, kaydırma çubuklarını kullanarak güvenlik kategorisine göre içerik filtreleme düzeyini ayarlayabilirsiniz:

![](https://ai.google.dev/static/gemini-api/docs/images/safety_settings_ui.png?hl=tr)

İstek gönderdiğinizde (ör. modele soru sorarak) isteğin içeriği engellenirse warning
**İçerik engellendi** mesajı gösterilir. Daha fazla ayrıntı görmek için işaretçiyi **İçerik engellendi** metninin üzerine getirin. Böylece kategori ve zararlı olma olasılığı sınıflandırmasını görebilirsiniz.

### Kod örnekleri

Aşağıdaki kod snippet'inde, `GenerateContent` görüşmenizde güvenlik ayarlarının nasıl yapılacağı gösterilmektedir. Bu, nefret söylemi (`HARM_CATEGORY_HATE_SPEECH`) kategorisinin eşiğini belirler. Bu kategoriyi `BLOCK_LOW_AND_ABOVE` olarak ayarladığınızda, nefret söylemi olma olasılığı düşük veya yüksek olan tüm içerikler engellenir. Eşik ayarlarını anlamak için [İstek başına güvenlik filtreleme](#safety-filtering-per-request) başlıklı makaleyi inceleyin.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Some potentially unsafe prompt",
    config=types.GenerateContentConfig(
      safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
      ]
    )
)

print(response.text)
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        SafetySettings: []*genai.SafetySetting{
            {
                Category:  "HARM_CATEGORY_HATE_SPEECH",
                Threshold: "BLOCK_LOW_AND_ABOVE",
            },
        },
    }

    response, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Some potentially unsafe prompt."),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(response.Text())
}
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const safetySettings = [
  {
    category: "HARM_CATEGORY_HATE_SPEECH",
    threshold: "BLOCK_LOW_AND_ABOVE",
  },
];

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Some potentially unsafe prompt.",
    config: {
      safetySettings: safetySettings,
    },
  });
  console.log(response.text);
}

await main();
```

### Java

```
SafetySetting hateSpeechSafety = new SafetySetting(HarmCategory.HATE_SPEECH,
    BlockThreshold.LOW_AND_ABOVE);

GenerativeModel gm = new GenerativeModel(
    "gemini-3-flash-preview",
    BuildConfig.apiKey,
    null, // generation config is optional
    Arrays.asList(hateSpeechSafety)
);

GenerativeModelFutures model = GenerativeModelFutures.from(gm);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "safetySettings": [
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_LOW_AND_ABOVE"}
    ],
    "contents": [{
        "parts":[{
            "text": "'\''Some potentially unsafe prompt.'\''"
        }]
    }]
}'
```

## Sonraki adımlar

- API'nin tamamı hakkında daha fazla bilgi edinmek için [API referansına](https://ai.google.dev/api?hl=tr) bakın.
- LLM'lerle geliştirme yaparken güvenlikle ilgili dikkat edilmesi gereken noktalar hakkında genel bir bakış için [güvenlik kılavuzunu](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=tr) inceleyin.
- [Jigsaw ekibinin](https://developers.perspectiveapi.com/s/about-the-api-score) olasılık ve önem düzeyini değerlendirme hakkındaki makalesinden daha fazla bilgi edinin.
- [Perspective API](https://medium.com/jigsaw/reducing-toxicity-in-large-language-models-with-perspective-api-c31c39b7a4d7) gibi güvenlik çözümlerine katkıda bulunan ürünler hakkında daha fazla bilgi edinin.
  \* Bu güvenlik ayarlarını kullanarak toksisite sınıflandırıcı oluşturabilirsiniz. Başlamak için [sınıflandırma
  örneğine](https://ai.google.dev/examples/train_text_classifier_embeddings?hl=tr) bakın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-04-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-04-29 UTC."],[],[]]
