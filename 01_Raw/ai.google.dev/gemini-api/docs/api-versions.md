---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=tr
fetched_at: 2026-09-07T05:32:45.707808+00:00
title: "API s\u00fcr\u00fcmleriyle ilgili a\u00e7\u0131klama \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [API referansı](https://ai.google.dev/api?hl=tr)

Geri bildirim gönderin

# API sürümleriyle ilgili açıklama

Bu belgede, Gemini API'nin `v1` ve `v1beta` sürümleri arasındaki farklarla ilgili üst düzey bir genel bakış sunulmaktadır.

- **v1**: API'nin kararlı sürümü. Kararlı sürümdeki özellikler, ana sürümün kullanım ömrü boyunca tam olarak desteklenir. API'de uyumluluğu bozan değişiklikler varsa API'nin yeni bir ana sürümü oluşturulur ve mevcut sürüm makul bir süre sonra kullanımdan kaldırılır.
  API'de ana sürüm değiştirilmeden uyumluluğu bozmayan değişiklikler yapılabilir. **Etkileşimler API** ve temel özellikleri, `v1`'da genel kullanıma sunulmuştur.
- **v1beta**: Bu sürüm, geliştirilme süreci devam eden erken aşamadaki özellikleri ve işlevleri içerir. `v1beta`'daki özellikler, geri bildirimlere göre iyileştirildikçe değişikliklere tabi olabilir. Ancak bu özellikler, yeni işlevleri kararlı sürüme yükseltilmeden önce denemenize olanak tanır.

## Kapasite ve özellik desteği

Aşağıdaki tabloda, `v1` (GA) ve `v1beta` (Beta) sürümlerindeki özelliklerin kullanılabilirliği ayrıntılı olarak açıklanmaktadır. Aksi belirtilmediği sürece temel API özellikleri ve araçları hem Etkileşimler API'si hem de `generateContent` için geçerlidir:

| Özellik | v1 | v1beta |
| --- | --- | --- |
| **Temel API özellikleri** |  |  |
| [Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=tr) |  |  |
| [İşlev Çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) |  |  |
| [Yapılandırılmış Çıkış](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr) |  |  |
| [Düşünme / Muhakeme Etme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) (Thinking / Reasoning) |  |  |
| [Sistem Talimatları](https://ai.google.dev/gemini-api/docs/system-instructions?hl=tr) |  |  |
| [Ses çıkışı (konuşma yapılandırması)](https://ai.google.dev/gemini-api/docs/audio?hl=tr) |  |  |
| [Hizmet Katmanı (Öncelikli / Esnek)](https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr) |  |  |
| **Araçlar** |  |  |
| [Kod Yürütme Aracı](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) |  |  |
| [Google Arama Temellendirmesi](https://ai.google.dev/gemini-api/docs/google-search?hl=tr) |  |  |
| [Google Haritalar'da Temellendirme](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr) (Google Maps Grounding) |  |  |
| [URL Bağlamı Aracı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr) |  |  |
| [Dosya Arama Aracı](https://ai.google.dev/gemini-api/docs/file-search?hl=tr) |  |  |
| [Bilgisayar Kullanımı Aracı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr) |  |  |
| [MCP Sunucuları Aracı](https://ai.google.dev/gemini-api/docs/eap/remote_mcp?hl=tr) |  |  |
| **Anlık API'ler** |  |  |
| [Live API (WebSockets)](https://ai.google.dev/gemini-api/docs/live-api?hl=tr) |  |  |
| [Live Music API](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=tr) |  |  |
| [Kısa Ömürlü Jetonlar (Canlı API)](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=tr) |  |  |
| **Platform API'leri** |  |  |
| [Models API](https://ai.google.dev/gemini-api/docs/models?hl=tr) |  |  |
| [Dosya Hizmeti Rotası](https://ai.google.dev/gemini-api/docs/files?hl=tr) |  |  |
| [Dosya Arama Mağazaları Rotası](https://ai.google.dev/gemini-api/docs/file-search?hl=tr) |  |  |
| [Agents API](https://ai.google.dev/gemini-api/docs/agents?hl=tr) |  |  |
| [Webhooks API](https://ai.google.dev/gemini-api/docs/webhooks?hl=tr) |  |  |
| [Bağlamı Önbelleğe Alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr) |  |  |

- - Desteklenir

## SDK'da API sürümünü yapılandırma

Gemini API SDK'ları varsayılan olarak `v1beta` sürümünü kullanır ancak aşağıdaki kod örneğinde gösterildiği gibi API sürümünü ayarlayarak sürümleri açıkça belirtebilirsiniz:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.7-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.7-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.HttpOptions;

Client client = Client.builder()
    .httpOptions(HttpOptions.builder().apiVersion("v1").build())
    .build();

CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.6-flash"))
    .input(InteractionsInput.of("Explain how AI works"))
    .build();
var interaction = client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.7-flash",
    "input": "Explain how AI works",
  }'
```

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-01 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-01 UTC."],[],[]]
