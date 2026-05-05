---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=tr
fetched_at: 2026-05-05T19:51:51.853057+00:00
title: "URL context \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# URL context

URL bağlamı aracı, URL'ler şeklinde modellere ek bağlam sağlamanıza olanak tanır. İsteğinize URL'ler ekleyerek model, yanıtını bilgilendirmek ve geliştirmek için bu sayfalardaki içeriğe ([sınırlamalar bölümünde](#limitations) listelenen bir URL türü olmadığı sürece) erişir.

URL bağlamı aracı, aşağıdaki gibi görevler için kullanışlıdır:

- **Veri Ayıklama**: Fiyatlar, adlar veya temel bulgular gibi belirli bilgileri birden fazla URL'den çekin.
- **Belgeleri Karşılaştırma**: Farklılıkları belirlemek ve trendleri takip etmek için birden fazla raporu, makaleyi veya PDF'yi analiz edin.
- **İçerik Sentezleme ve Oluşturma**: Doğru özetler, blog yayınları veya raporlar oluşturmak için çeşitli kaynak URL'lerden gelen bilgileri birleştirin.
- **Kodu ve Dokümanları Analiz Etme**: Kodu açıklamak, kurulum talimatları oluşturmak veya soruları yanıtlamak için bir GitHub deposunu ya da teknik dokümanı işaret edin.

Aşağıdaki örnekte, farklı web sitelerindeki iki tarifin nasıl karşılaştırılacağı gösterilmektedir.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3-flash-preview"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## İşleyiş şekli

URL Bağlamı aracı, hızı, maliyeti ve güncel verilere erişimi dengelemek için iki adımlı bir alma süreci kullanır. Bir URL sağladığınızda araç, önce içeriği dahili bir dizin önbelleğinden getirmeye çalışır. Bu, yüksek düzeyde optimize edilmiş bir önbellek görevi görür. Bir URL dizinde mevcut değilse (ör. çok yeni bir sayfa ise) araç otomatik olarak canlı getirme işlemine geri döner.
Bu araç, içeriğini gerçek zamanlı olarak almak için doğrudan URL'ye erişir.

## Diğer araçlarla birlikte kullanma

Daha güçlü iş akışları oluşturmak için URL bağlamı aracını diğer araçlarla birlikte kullanabilirsiniz.

[Gemini 3 modelleri](#supported-models), yerleşik araçların (ör. URL bağlamı) özel araçlarla (işlev çağrısı) birleştirilmesini destekler. [Araç kombinasyonları](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) sayfasından daha fazla bilgi edinin.

### Arama ile temellendirme

Hem URL bağlamı hem de [Google Arama ile temellendirme](https://ai.google.dev/gemini-api/docs/grounding?hl=tr) etkinleştirildiğinde model, internette alakalı bilgiler bulmak için arama özelliklerini kullanabilir ve ardından bulduğu sayfaları daha ayrıntılı bir şekilde anlamak için URL bağlamı aracını kullanabilir. Bu yaklaşım, hem geniş kapsamlı arama hem de belirli sayfaların ayrıntılı analizini gerektiren istemler için oldukça etkilidir.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3-flash-preview"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## Yanıtı anlama

Model, URL bağlamı aracını kullandığında yanıtta bir `url_context_metadata` nesnesi yer alır. Bu nesne, modelin içerik aldığı URL'leri ve her alma denemesinin durumunu listeler. Bu bilgiler, doğrulama ve hata ayıklama için yararlıdır.

Aşağıda, yanıtın bu bölümüne ilişkin bir örnek verilmiştir
(yanıtın bazı bölümleri, kısa olması için çıkarılmıştır):

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

Bu nesneyle ilgili tüm ayrıntılar için [`UrlContextMetadata` API referansı](https://ai.google.dev/api/generate-content?hl=tr#UrlContextMetadata) bölümüne bakın.

### Güvenlik kontrolleri

Sistem, URL'de içerik denetimi yaparak güvenlik standartlarına uygun olup olmadığını kontrol eder. Sağladığınız URL bu denetimi geçemezse `url_retrieval_status` `URL_RETRIEVAL_STATUS_UNSAFE` hatası alırsınız.

### Jeton sayısı

İsteminizde belirttiğiniz URL'lerden alınan içerik, giriş jetonları kapsamında sayılır. İsteminizin jeton sayısını ve araç kullanımını model çıkışının [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=tr#UsageMetadata)
nesnesinde görebilirsiniz. Aşağıda örnek bir çıkış verilmiştir:

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

Jeton başına fiyat, kullanılan modele bağlıdır. Ayrıntılar için [fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) sayfasına bakın.

## Desteklenen modeller

| Model | URL Bağlamı |
| --- | --- |
| [Gemini 3.1 Pro Önizlemesi](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=tr) | ✔️ |
| [Gemini 3.1 Flash-Lite Önizlemesi](https://ai.google.dev/gemini-api/docs/gemini-3.1-flash-lite-preview?hl=tr) | ✔️ |
| [Gemini 3 Flash Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=tr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=tr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=tr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=tr) | ✔️ |

## En İyi Uygulamalar

- **Belirli URL'ler sağlama**: En iyi sonuçları elde etmek için modelin analiz etmesini istediğiniz içeriğe doğrudan URL'ler sağlayın. Model yalnızca sağladığınız URL'lerden içerik alır, yerleştirilmiş bağlantılardaki içerikleri almaz.
- **Erişilebilirliği kontrol edin**: Sağladığınız URL'lerin, giriş yapılması gereken veya ödeme duvarının arkasında olan sayfalara yönlendirmediğini doğrulayın.
- **Tam URL'yi kullanın**: Protokolü de dahil ederek tam URL'yi girin (ör. yalnızca google.com yerine https://www.google.com).

## Sınırlamalar

- İşlev çağırma: İşlev çağırma ile araç kullanımı (URL bağlamı, Google Arama ile temellendirme vb.) şu anda desteklenmemektedir.
- İstek sınırı: Araç, istek başına en fazla 20 URL işleyebilir.
- URL içerik boyutu: Tek bir URL'den alınan içeriklerin maksimum boyutu 34 MB'tır.
- Herkese açık erişim: URL'ler web'de herkesin erişimine açık olmalıdır.
  Localhost adresleri (ör. localhost, 127.0.0.1), özel ağlar ve tünel oluşturma hizmetleri (ör. ngrok, pinggy) desteklenmez.
- Yalnızca Gemini API: URL bağlamı, Gemini Enterprise Ajan Platformu üzerinden değil, yalnızca Gemini API'de kullanılabilir.

### Desteklenen ve desteklenmeyen içerik türleri

Araç, aşağıdaki içerik türlerine sahip URL'lerden içerik ayıklayabilir:

- Metin (text/html, application/json, text/plain, text/xml, text/css,
  text/javascript , text/csv, text/rtf)
- Resim (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

Aşağıdaki içerik türleri **desteklenmez**:

- Ödeme duvarlı içerik
- YouTube videoları (YouTube URL'lerinin nasıl işleneceğini öğrenmek için [video anlama](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr#youtube) bölümüne bakın)
- Google Dokümanları veya e-tablolar gibi Google Workspace dosyaları
- Video ve ses dosyaları

## Sırada ne var?

- Daha fazla örnek için [URL bağlamı yemek kitabını](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=tr#url-context) inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-04-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-04-29 UTC."],[],[]]
