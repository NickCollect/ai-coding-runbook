---
source_url: https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=tr
fetched_at: 2026-05-18T05:18:54.753220+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini API hızlı başlangıç kılavuzu

Bu hızlı başlangıç kılavuzunda, [kitaplıklarımızı](https://ai.google.dev/gemini-api/docs/libraries?hl=tr) nasıl yükleyeceğiniz ve Etkileşimler API'sini kullanarak ilk Gemini API isteğinizi nasıl yapacağınız gösterilmektedir.

## Başlamadan önce

Gemini API'yi kullanmak için isteklerinizin kimliğini doğrulayacak, güvenlik sınırlarını uygulayacak ve hesabınızdaki kullanımı izleyecek bir API anahtarına sahip olmanız gerekir.

Başlamak için AI Studio'da ücretsiz olarak bir tane oluşturun:

[Gemini API anahtarı oluşturma](https://aistudio.google.com/app/apikey?hl=tr)

## Google GenAI SDK'yı yükleme

### Python

[Python 3.9+](https://www.python.org/downloads/) kullanarak aşağıdaki [pip komutunu](https://packaging.python.org/en/latest/tutorials/installing-packages/) kullanarak [`google-genai` paketini](https://pypi.org/project/google-genai/) yükleyin:

```
pip install -q -U google-genai
```

### JavaScript

[Node.js v18+](https://nodejs.org/en/download/package-manager)'ı kullanarak aşağıdaki [npm komutunu](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) kullanarak [TypeScript ve JavaScript için Google Gen AI SDK](https://www.npmjs.com/package/@google/genai)'yı yükleyin:

```
npm install @google/genai
```

## İlk isteğinizi gönderme

Gemini API'ye istek göndermek için kullanabileceğiniz iki yöntem vardır:

- ***(Önerilen)*** [Interactions API](https://ai.google.dev/api/interactions-api?hl=tr), çok adımlı araç kullanımı, düzenleme ve türü belirlenmiş yürütme adımları aracılığıyla karmaşık akıl yürütme akışları için yerel destek sunan yeni bir temeldir. Bundan sonra, ana mainline ailesinin ötesindeki yeni modellerin yanı sıra yeni ajan tabanlı yetenekler ve araçları yalnızca Interactions API'de kullanıma sunulacak.
- [`generateContent`](https://ai.google.dev/api/generate-content?hl=tr#method:-models.generatecontent), modelden basit ve durum bilgisiz bir yanıt oluşturmanın bir yolunu sunar. Etkileşimler API'sini kullanmanızı önersek de `generateContent` tamamen desteklenir.

Bu örnekte, Gemini 3 Flash modelini kullanarak Gemini API'ye istek göndermek için Etkileşimler API'si kullanılmaktadır.

[API anahtarınızı](https://ai.google.dev/gemini-api/docs/interactions/api-key?hl=tr#set-api-env-var) `GEMINI_API_KEY` ortam değişkeni olarak ayarlarsanız [Gemini API kitaplıkları](https://ai.google.dev/gemini-api/docs/libraries?hl=tr) kullanılırken istemci tarafından otomatik olarak alınır.
Aksi takdirde, istemciyi başlatırken [API anahtarınızı bağımsız değişken olarak iletmeniz](https://ai.google.dev/gemini-api/docs/interactions/api-key?hl=tr#provide-api-key-explicitly) gerekir.

Gemini API belgelerindeki tüm kod örneklerinde `GEMINI_API_KEY` ortam değişkenini ayarladığınız varsayılır.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview", 
    input="Explain how AI works in a few words"
)

# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

// The client gets the API key from the environment variable `GEMINI_API_KEY`.
const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain how AI works in a few words",
  });

  const modelStep = interaction.steps.find(s => s.type === 'model_output');
  if (modelStep) {
    for (const contentBlock of modelStep.content) {
      if (contentBlock.type === 'text') console.log(contentBlock.text);
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain how AI works in a few words"
  }'
```

### Durumsuz mod

Varsayılan olarak, `previous_interaction_id` kullanırken Interactions API, görüşme durumunu sunucu tarafında yönetir. Konuşma geçmişini istemci tarafında kendiniz yönetmeyi tercih ederseniz `store=false` değerini ayarlayıp sonraki isteklerin `input` alanında birikmiş adımları ileterek durum bilgisiz modu etkinleştirebilirsiniz.

Ayrıntılı bilgi ve tam çok turlu durum bilgisi içermeyen örnekler için [Metin oluşturma kılavuzu](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=tr#stateless-conversations)'na bakın.

## Sırada ne var?

İlk API isteğinizi gönderdiğinize göre, Gemini'ın nasıl çalıştığını gösteren aşağıdaki kılavuzları inceleyebilirsiniz:

- [Metin oluşturma](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=tr)
- [Görüntü üretme](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=tr)
- [Görüntü anlama](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=tr)
- [Düşünme](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=tr) (Thinking)
- [İşlev çağırma](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=tr)
- [Uzun bağlam](https://ai.google.dev/gemini-api/docs/long-context?hl=tr)
- [Yerleştirmeler](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr)

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-12 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-12 UTC."],[],[]]
