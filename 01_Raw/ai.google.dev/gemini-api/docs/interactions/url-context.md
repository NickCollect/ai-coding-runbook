---
source_url: https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=tr
fetched_at: 2026-05-25T05:18:43.441366+00:00
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

# URL bağlamı

URL bağlamı aracı, URL'ler şeklinde modellere ek bağlam sağlamanıza olanak tanır. İsteğinize URL'ler ekleyerek model, yanıtını bilgilendirmek ve geliştirmek için bu sayfalardaki içeriğe ([sınırlamalar bölümünde](#limitations) listelenen bir URL türü olmadığı sürece) erişir.

URL bağlamı aracı, aşağıdaki gibi görevler için kullanışlıdır:

- **Veri Ayıklama**: Fiyatlar, adlar veya temel bulgular gibi belirli bilgileri birden fazla URL'den çekin.
- **Belgeleri Karşılaştırma**: Farklılıkları belirlemek ve trendleri takip etmek için birden fazla raporu, makaleyi veya PDF'yi analiz edin.
- **İçerik Sentezleme ve Oluşturma**: Doğru özetler, blog yayınları veya raporlar oluşturmak için çeşitli kaynak URL'lerden gelen bilgileri birleştirin.
- **Kodu ve Dokümanları Analiz Etme**: Kodu açıklamak, kurulum talimatları oluşturmak veya soruları yanıtlamak için bir GitHub deposunu ya da teknik dokümanı işaret edin.

Aşağıdaki örnekte, farklı web sitelerindeki iki tarifin nasıl karşılaştırılacağı gösterilmektedir.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## İşleyiş şekli

URL Bağlamı aracı, hızı, maliyeti ve güncel verilere erişimi dengelemek için iki adımlı bir alma süreci kullanır. Bir URL sağladığınızda araç, önce içeriği dahili bir dizin önbelleğinden getirmeye çalışır. Bu, yüksek düzeyde optimize edilmiş bir önbellek görevi görür. Bir URL dizinde mevcut değilse (ör. çok yeni bir sayfa ise) araç otomatik olarak canlı getirme işlemine geri döner.
Bu araç, içeriğini gerçek zamanlı olarak almak için doğrudan URL'ye erişir.

## Diğer araçlarla birlikte kullanma

Daha güçlü iş akışları oluşturmak için URL bağlamı aracını diğer araçlarla birlikte kullanabilirsiniz.

[Gemini 3 modelleri](#supported-models), yerleşik araçların (ör. URL bağlamı) özel araçlarla (işlev çağrısı) birleştirilmesini destekler. [Araç kombinasyonları](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=tr) sayfasından daha fazla bilgi edinin.

### Arama ile temellendirme

Hem URL bağlamı hem de [Google Arama ile temellendirme](https://ai.google.dev/gemini-api/docs/grounding?hl=tr) etkinleştirildiğinde model, arama özelliklerini kullanarak internette alakalı bilgiler bulabilir ve ardından bulduğu sayfalar hakkında daha ayrıntılı bilgi edinmek için URL bağlamı aracını kullanabilir. Bu yaklaşım, hem geniş kapsamlı arama hem de belirli sayfaların ayrıntılı analizini gerektiren istemler için oldukça etkilidir.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

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

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## Yanıtı anlama

Model, URL bağlam aracını kullandığında metin yanıtı, metin içeriği bloğunda satır içi `url_citation` ek açıklamalar içerir. Her ek açıklama, yanıt metninin bir bölümünü (`start_index` ve `end_index` aracılığıyla) türetildiği kaynak URL'ye bağlar. Bu, uygulamanızda alıntıları göstermenin birincil yoludur. Bunları nasıl çıkaracağınızı öğrenmek için [yukarıdaki ana örneğe](#get-started) bakın.

Yanıtta ayrıca her URL alma girişimiyle ilgili meta verilerin (durum, alınan URL) bulunduğu bir `url_context_result` adımı yer alır. Bu özellik, daha çok hata ayıklama için yararlıdır.

### Güvenlik kontrolleri

Sistem, URL'lerin güvenlik standartlarına uygun olup olmadığını doğrulamak için içerik denetimi yapar. Bir URL bu kontrolü geçemezse ilgili `url_context_result` adımında `"unsafe"` `status` gösterilir.

### Jeton sayısı

İsteminizde belirttiğiniz URL'lerden alınan içerik, giriş jetonları kapsamında sayılır. Jeton sayısını etkileşimin `usage` nesnesinde görebilirsiniz. Aşağıda bir örnek verilmiştir:

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

Jeton başına fiyat, kullanılan modele bağlıdır. Ayrıntılar için [fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) sayfasına bakın.

## Desteklenen modeller

| Model | URL Bağlamı |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=tr) | ✔️ |
| [Gemini 3.1 Pro Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=tr) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr) | ✔️ |
| [Gemini 3.1 Flash-Lite Önizlemesi](https://ai.google.dev/gemini-api/docs/gemini-3.1-flash-lite-preview?hl=tr) | ✔️ |
| [Gemini 3 Flash Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=tr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=tr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=tr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=tr) | ✔️ |

## En İyi Uygulamalar

- **Belirli URL'ler sağlama**: En iyi sonuçları elde etmek için modelin analiz etmesini istediğiniz içeriğe doğrudan URL'ler sağlayın. Model yalnızca sağladığınız URL'lerden içerik alır, iç içe yerleştirilmiş bağlantılardaki içerikleri almaz.
- **Erişilebilirliği kontrol edin**: Sağladığınız URL'lerin, giriş yapılması gereken veya ödeme duvarının arkasında olan sayfalara yönlendirmediğini doğrulayın.
- **Tam URL'yi kullanın**: Protokolü de dahil ederek tam URL'yi girin (ör. yalnızca google.com yerine https://www.google.com).

## Sınırlamalar

- İstek sınırı: Araç, istek başına en fazla 20 URL işleyebilir.
- URL içerik boyutu: Tek bir URL'den alınan içeriklerin maksimum boyutu 34 MB'tır.
- Herkese açık erişim: URL'ler web'de herkesin erişimine açık olmalıdır.
  Localhost adresleri (ör. localhost, 127.0.0.1), özel ağlar ve tünel oluşturma hizmetleri (ör. ngrok, pinggy) desteklenmez.
- Yalnızca Gemini API: URL bağlamı, Gemini Enterprise Agent Platformu üzerinden değil yalnızca Gemini API'de kullanılabilir.

### Desteklenen ve desteklenmeyen içerik türleri

Araç, aşağıdaki içerik türlerine sahip URL'lerden içerik ayıklayabilir:

- Metin (text/html, application/json, text/plain, text/xml, text/css,
  text/javascript , text/csv, text/rtf)
- Resim (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

Aşağıdaki içerik türleri **desteklenmez**:

- Ödeme duvarlı içerik
- YouTube videoları (YouTube URL'lerinin nasıl işleneceğini öğrenmek için [video anlama](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=tr#youtube) bölümüne bakın)
- Google Dokümanları veya e-tablolar gibi Google Workspace dosyaları
- Video ve ses dosyaları

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-19 UTC."],[],[]]
