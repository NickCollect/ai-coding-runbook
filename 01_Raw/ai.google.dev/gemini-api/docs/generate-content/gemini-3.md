---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/gemini-3?hl=tr
fetched_at: 2026-09-14T05:53:51.005118+00:00
title: "Gemini 3 geli\u015ftirici k\u0131lavuzu \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)

Geri bildirim gönderin

# Gemini 3 geliştirici kılavuzu

Gemini 3, gelişmiş mantık yürütme altyapısıyla geliştirilmiş, bugüne kadarki en akıllı model ailemizdir. Asenkron iş akışlarında, bağımsız kodlamada ve karmaşık çok formatlı görevlerde uzmanlaşarak her fikri hayata geçirmek için tasarlanmıştır.
Bu rehberde, Gemini 3 model ailesinin temel özellikleri ve bu özelliklerden en iyi şekilde nasıl yararlanabileceğiniz açıklanmaktadır.

[Gemini 3.1 Pro Önizlemesi'ni deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=tr)
[Gemini 3 Flash Önizlemesi'ni deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=tr)
[Gemini 3.1 Flash-Lite'ı deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=tr)
[Nano Banana 2'yi deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=tr)

Modelin gelişmiş akıl yürütme, bağımsız kodlama ve karmaşık çok formatlı görevleri nasıl ele aldığını görmek için [Gemini 3 uygulamaları koleksiyonumuzu](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=tr) inceleyin.

Birkaç satır kodla başlayın:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## Gemini 3 serisiyle tanışın

Gemini 3.1 Pro, geniş dünya bilgisi ve farklı formatlarda gelişmiş mantık yürütme gerektiren karmaşık görevler için en iyi seçenektir.

Gemini 3 Flash, 3 serisinin en yeni modelidir. Pro düzeyinde zekaya sahip olan bu model, Flash'in hızı ve fiyatıyla sunulur.

Nano Banana Pro (Gemini 3 Pro Image olarak da bilinir) en yüksek kaliteli görüntü üretme modelimizdir. Nano Banana 2 (Gemini 3.1 Flash Image olarak da bilinir) ise yüksek hacimli, yüksek verimli ve daha düşük fiyatlı bir alternatiftir.

Gemini 3.1 Flash-Lite, maliyet verimliliği ve yüksek hacimli görevler için tasarlanmış modelimizdir.

| Model Kimliği | Bağlam penceresi (içinde / dışında) | Son Güncel Bilgi Tarihi | Fiyatlandırma (Giriş / Çıkış)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1M / 64k | Ocak 2025 | 0,25 ABD doları (metin, resim, video), 0,50 ABD doları (ses) / 1,50 ABD doları |
| **gemini-3.1-flash-image-preview** | 128 bin / 32 bin | Ocak 2025 | 0,25 ABD doları (Metin Girişi) / 0,067 ABD doları (Resim Çıkışı)\*\* |
| **gemini-3.1-pro-preview** | 1M / 64k | Ocak 2025 | 2 ABD doları / 12 ABD doları (<200 bin parça)   4 ABD doları / 18 ABD doları (>200 bin parça) |
| **gemini-3-flash-preview** | 1M / 64k | Ocak 2025 | 0,50 ABD doları / 3 ABD doları |
| **gemini-3-pro-image-preview** | 65 bin / 32 bin | Ocak 2025 | 2 ABD doları (Metin Girişi) / 0,134 ABD doları (Resim Çıkışı)\*\* |

*\* Aksi belirtilmedikçe fiyatlandırma 1 milyon jeton başına yapılır.*
*\*\* Resim fiyatlandırması çözünürlüğe göre değişir. Ayrıntılar için [fiyatlandırma sayfasına](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) göz atın.*

Ayrıntılı sınırlar, fiyatlandırma ve ek bilgiler için [modeller sayfasına](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr) bakın.

## Gemini 3'teki yeni API özellikleri

Gemini 3, geliştiricilere gecikme, maliyet ve çok formatlı doğruluk üzerinde daha fazla kontrol imkanı sunmak için tasarlanmış yeni parametreler sunar.

### Düşünme düzeyi

Gemini 3 serisi modeller, istemleri değerlendirmek için varsayılan olarak dinamik düşünme özelliğini kullanır. Yanıt oluşturmadan önce modelin dahili muhakeme sürecinin **maksimum** derinliğini kontrol eden `thinking_level` parametresini kullanabilirsiniz. Gemini 3, bu seviyeleri katı jeton garantileri yerine düşünme için göreceli izinler olarak değerlendirir.

`thinking_level` belirtilmezse Gemini 3 varsayılan olarak `high` değerini kullanır. Karmaşık akıl yürütme gerekmeyen durumlarda daha hızlı ve daha düşük gecikmeli yanıtlar için modelin düşünce düzeyini `low` ile sınırlayabilirsiniz.

| Düşünme Düzeyi | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Açıklama |
| --- | --- | --- | --- | --- |
| **`minimal`** | Desteklenmiyor | Destekleniyor (Varsayılan) | Destekleniyor | Çoğu sorgu için "düşünme yok" ayarıyla eşleşir. Model, karmaşık kodlama görevleri için çok az düşünebilir. Sohbet veya yüksek gönderim hacmi uygulamalarında gecikmeyi en aza indirir. `minimal`'nın düşünme özelliğinin kapalı olduğunu garanti etmediğini unutmayın. |
| **`low`** | Destekleniyor | Destekleniyor | Destekleniyor | Gecikmeyi ve maliyeti en aza indirir. Basit talimatları uygulamak, sohbet etmek veya yüksek işleme hızlı uygulamalar için en iyisidir. |
| **`medium`** | Destekleniyor | Destekleniyor | Destekleniyor | Çoğu görev için dengeli düşünme |
| **`high`** | Destekleniyor (Varsayılan, Dinamik) | Desteklenir (Dinamik) | Destekleniyor (Varsayılan, Dinamik) | Akıl yürütme derinliğini en üst düzeye çıkarır. Modelin ilk (düşünme içermeyen) çıkış jetonuna ulaşması önemli ölçüde daha uzun sürebilir ancak çıkış daha dikkatli bir şekilde gerekçelendirilir. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### Medya çözünürlüğü

Gemini 3, `media_resolution` parametresiyle çok formatlı görüntü işleme üzerinde ayrıntılı kontrol sağlar. Daha yüksek çözünürlükler, modelin küçük metinleri okuma veya küçük ayrıntıları tanımlama becerisini artırır ancak jeton kullanımını ve gecikmeyi de artırır.
`media_resolution` parametresi, **giriş resim veya video karesi başına ayrılan maksimum jeton sayısını
belirler.**

Artık çözünürlüğü her bir medya bölümü için ayrı ayrı veya genel olarak `media_resolution_low`, `media_resolution_medium`, `media_resolution_high` ya da `media_resolution_ultra_high` olarak ayarlayabilirsiniz (`generation_config` üzerinden; ultra yüksek için genel ayar kullanılamaz). Belirtilmezse model, medya türüne göre en uygun varsayılan değerleri kullanır.

**Önerilen ayarlar**

| Medya Türü | Önerilen Ayar | Maksimum jeton sayısı | Kullanım Yönergeleri |
| --- | --- | --- | --- |
| **Resimler** | `media_resolution_high` | 1120 | Maksimum kaliteyi sağlamak için çoğu görüntü analizi görevinde önerilir. |
| **PDF'ler** | `media_resolution_medium` | 560 | Belge anlamak için idealdir. Kalite genellikle `medium`'da doygunluğa ulaşır. `high`'ya yükseltmek, standart dokümanlar için OCR sonuçlarını nadiren iyileştirir. |
| **Video** (Genel) | `media_resolution_low` (veya `media_resolution_medium`) | 70 (kare başına) | **Not:** Video için `low` ve `medium` ayarları, bağlam kullanımını optimize etmek amacıyla aynı şekilde (70 jeton) değerlendirilir. Bu, çoğu eylem tanıma ve açıklama görevi için yeterlidir. |
| **Video** (Metin ağırlıklı) | `media_resolution_high` | 280 (kare başına) | Yalnızca kullanım alanında yoğun metin okuma (OCR) veya video karelerindeki küçük ayrıntılar yer aldığında gereklidir. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is available in the v1beta API version.
client = genai.Client(http_options={'api_version': 'v1beta'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is available in the v1beta API version.
const ai = new GoogleGenAI({ apiVersion: "v1beta" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### Sıcaklık

Tüm Gemini 3 modellerinde, sıcaklık parametresini `1.0` varsayılan değerinde tutmanızı önemle tavsiye ederiz.

Önceki modellerde yaratıcılık ile determinizm arasındaki dengeyi kontrol etmek için genellikle sıcaklık ayarından yararlanılırdı. Ancak Gemini 3'ün akıl yürütme özellikleri varsayılan ayar için optimize edilmiştir. Sıcaklığı değiştirmek (1, 0'ın altına ayarlamak), özellikle karmaşık matematiksel veya muhakeme görevlerinde döngüye girme ya da performansın düşmesi gibi beklenmedik davranışlara yol açabilir.

### Düşünce imzaları

Gemini 3, API çağrıları arasında muhakeme bağlamını korumak için [Düşünce imzalarını](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=tr) kullanır. Bu imzalar, modelin dahili düşünce sürecinin şifrelenmiş gösterimleridir. Modelin muhakeme yeteneklerini korumasını sağlamak için bu imzaları isteğinizde modele tam olarak alındıkları şekilde geri göndermeniz gerekir:

- **İşlev Çağrısı (Katı):** API, "Mevcut Sıra" üzerinde katı doğrulama uygular. Eksik imzalar 400 hatasına neden olur.
- **Metin/Sohbet:** Doğrulama katı bir şekilde uygulanmaz ancak imzaların atlanması modelin muhakeme ve yanıt kalitesini düşürür.
- **Görüntü üretme/düzenleme (Katı)**: API, `thoughtSignature` dahil olmak üzere tüm Model bölümlerinde katı doğrulama uygular. Eksik imzalar 400 hatasına neden olur.

#### İşlev çağrısı (katı doğrulama)

Gemini, `functionCall` oluştururken sonraki adımda aracın çıktısını doğru şekilde işlemek için `thoughtSignature` kullanır. "Mevcut Tur", son standart **Kullanıcı** `text` mesajından bu yana gerçekleşen tüm Model (`functionCall`) ve Kullanıcı (`functionResponse`) adımlarını içerir.

- **Tek İşlev Çağrısı:** `functionCall` bölümü bir imza içerir. İade etmeniz gerekir.
- **Paralel İşlev Çağrıları:** Listedeki yalnızca ilk `functionCall` bölümü imzayı içerir. Parçaları, alındıkları sırayla iade etmeniz gerekir.
- **Çok Adımlı (Sıralı):** Model bir aracı çağırırsa, sonuç alır ve *başka* bir aracı çağırırsa (aynı dönüş içinde) **her iki** işlev çağrısının da imzası olur. Geçmişte biriken **tüm** imzaları döndürmeniz gerekir.

#### Metin ve canlı yayın

Standart sohbet veya metin oluşturma işlemlerinde imza bulunması garanti edilmez.

- **Akış Olmayan**: Yanıtın son içerik bölümünde `thoughtSignature` bulunabilir ancak bu her zaman geçerli değildir. Bir cihaz iade edilirse en iyi performansı korumak için cihazı geri göndermeniz gerekir.
- **Yayın**: İmza oluşturulursa boş bir metin bölümü içeren son bir parça olarak gelebilir. Akış ayrıştırıcınızın, metin alanı boş olsa bile imzaları kontrol ettiğinden emin olun.

#### Görüntü üretme ve düzenleme

`gemini-3-pro-image-preview` ve `gemini-3.1-flash-image-preview` için düşünce imzaları, sohbete dayalı düzenleme açısından kritik öneme sahiptir. Modelden bir resmi değiştirmesini istediğinizde, orijinal resmin kompozisyonunu ve mantığını anlamak için önceki dönüşteki `thoughtSignature` simgesine dayanır.

- **Düzenleme:** Yanıtın düşüncelerinden sonraki ilk bölümde (`text` veya `inlineData`) ve sonraki her `inlineData` bölümünde imza bulunur. Hataları önlemek için bu imzaların tümünü döndürmeniz gerekir.

#### Kod örnekleri

#### Çok adımlı işlev çağırma (sıralı)

Kullanıcı, tek bir dönüşte iki ayrı adım (Uçuşu Kontrol Et -> Taksi Rezervasyonu Yap) gerektiren bir soru soruyor.   
  
**1. adım: Model, Uçuş Aracı'nı çağırır.**  
Model, imza döndürüyor `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**2. adım: Kullanıcı, uçuş sonucu gönderir**  
Modelin düşünce akışını korumak için `<Sig_A>` yanıtını geri göndermemiz gerekir.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  {
    "role": "model",
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // REQUIRED
      }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**3. adım: Model, Taksi Aracı'nı çağırır**  
Model, `<Sig_A>` aracılığıyla uçuş gecikmesini hatırlar ve şimdi taksi rezervasyonu yapmaya karar verir. *Yeni* bir imza `<Sig_B>` oluşturur.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**4. adım: Kullanıcı, Taksi Sonucu'nu gönderir**  
Sırayı tamamlamak için tüm zinciri (`<Sig_A>` VE `<Sig_B>`) geri göndermeniz gerekir.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### Paralel İşlev Çağırma

Kullanıcı, "Paris ve Londra'daki hava durumunu kontrol et" diye soruyor. Model, tek bir yanıtta iki işlev çağrısı döndürüyor.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### Metin/Bağlam İçinde Akıl Yürütme (Doğrulama Yok)

Kullanıcı, harici araçlar olmadan bağlam içi akıl yürütme gerektiren bir soru soruyor. Kesin olarak doğrulanmamış olsa da imzanın eklenmesi, modelin takip soruları için muhakeme zincirini korumasına yardımcı olur.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### Görüntü üretme ve düzenleme

Resim üretme için imzalar sıkı bir şekilde doğrulanır. Bunlar **ilk bölümde** (metin veya resim) ve **sonraki tüm resim bölümlerinde** gösterilir. Hepsini bir sonraki turda geri vermeniz gerekir.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### Diğer modellerden veri taşıma

Başka bir modelden (ör. Gemini 2.5) sohbet izi aktarıyorsanız veya Gemini 3 tarafından oluşturulmamış özel bir işlev çağrısı ekliyorsanız geçerli bir imzanız olmaz.

Bu belirli senaryolarda katı doğrulamayı atlamak için alanı şu belirli sahte dizeyle doldurun: `"thoughtSignature": "context_engineering_is_the_way
to_go"`

### Araçlarla yapılandırılmış çıkışlar

Gemini 3 modelleri, [Yapılandırılmış Çıkışlar](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr)'ı [Google Arama ile Temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr), [URL Bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr), [Kod Yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) ve [İşlev Çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) gibi yerleşik araçlarla birleştirmenize olanak tanır.

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
    "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
  }
}
},
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Görüntü üretme

Gemini 3.1 Flash Image ve Gemini 3 Pro Image, metin istemlerinden görseller oluşturup düzenlemenize olanak tanır. Bir istemi "düşünmek" için akıl yürütme özelliğini kullanır ve yüksek kaliteli görüntüler oluşturmadan önce [Google Arama](https://ai.google.dev/gemini-api/docs/google-search?hl=tr)'yı temel alarak hava durumu tahminleri veya borsa grafikleri gibi gerçek zamanlı verileri alabilir.

**Yeni ve iyileştirilmiş özellikler:**

- **4K ve metin oluşturma:** 2K ve 4K çözünürlüklerde net ve okunaklı metinler ve diyagramlar oluşturun.
- **Temellendirilmiş üretim:** Gerçek dünyadaki bilgilere dayalı görüntüler oluşturmak ve bilgileri doğrulamak için `google_search` aracını kullanın. Google *Görsel* Arama ile temellendirme, Gemini 3.1 Flash Image için kullanılabilir.
- **Sohbete dayalı düzenleme:** Değişiklikleri (ör. "Arka planı gün batımı yap") isteyerek çok aşamalı etkileşimli görüntü düzenleme. Bu iş akışında, dönüşler arasındaki görsel bağlamı korumak için **Thought Signatures** (Düşünce İmzaları) kullanılır.

En-boy oranları, düzenleme iş akışları ve yapılandırma seçenekleriyle ilgili tüm ayrıntılar için [Görüntü Üretme Kılavuzu](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)'na bakın.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        response_format={"image": {"aspect_ratio": "16:9", "image_size": "4K"}}
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
  }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "responseFormat": {
    "image": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
  }
    }
  }'
```

**Örnek Yanıt**

![Weather Tokyo](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=tr)

### Görüntülerle kod yürütme

Gemini 3 Flash, görme eylemini yalnızca statik bir bakış olarak değil, aktif bir araştırma olarak ele alabilir. Model, akıl yürütmeyi [kod yürütmeyle](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) birleştirerek bir plan oluşturur. Ardından, cevaplarını görsel olarak temellendirmek için görüntüleri adım adım yakınlaştırmak, kırpmak, açıklama eklemek veya başka bir şekilde değiştirmek üzere Python kodu yazar ve yürütür.

**Kullanım alanları:**

- **Yakınlaştırma ve inceleme:** Model, ayrıntıların çok küçük olduğunu (ör. uzaktaki bir ölçüm cihazını veya seri numarasını okuma) algıladığında alanı kırpıp daha yüksek çözünürlükte yeniden incelemek için kodu otomatik olarak yazar.
- **Görsel matematik ve grafik oluşturma:** Model, kod kullanarak çok adımlı hesaplamalar yapabilir (ör. bir makbuzdaki satır öğelerini toplama veya çıkarılan verilerden Matplotlib grafiği oluşturma).
- **Resim açıklaması:** Model, "Bu öğe nereye yerleştirilmeli?" gibi konumsal soruları yanıtlamak için doğrudan resimlerin üzerine oklar, sınırlayıcı kutular veya başka açıklamalar çizebilir.

Görsel düşünmeyi etkinleştirmek için [Kod Yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr)'yi araç olarak yapılandırın. Model, gerektiğinde resimleri değiştirmek için otomatik olarak kod kullanır.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

Resimlerle kod yürütme hakkında daha fazla bilgi için [Kod Yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr#images) başlıklı makaleyi inceleyin.

### Çok formatlı işlev yanıtları

[Çok formatlı işlev çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr#multimodal), kullanıcıların çok formatlı nesneler içeren işlev yanıtları almasına olanak tanıyarak modelin işlev çağırma özelliklerinin daha iyi kullanılmasını sağlar. Standart işlev çağrısı yalnızca metin tabanlı işlev yanıtlarını destekler:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### Yerleşik araçları ve işlev çağrılarını birleştirme

Gemini 3, aynı API çağrısında yerleşik araçların (ör. Google Arama, URL bağlamı ve [daha fazlası](https://ai.google.dev/gemini-api/docs/tools?hl=tr)) ve özel [işlev çağrısı](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) araçlarının kullanılmasına olanak tanıyarak daha karmaşık iş akışları oluşturulmasını sağlar. [Araç kombinasyonları](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) sayfasından daha fazla bilgi edinin.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const response1 = await client.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const response2 = await client.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: history,
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });
}

run();
```

## Gemini 2.5'ten geçiş

Gemini 3, bugüne kadarki en yetenekli model ailemizdir ve Gemini 2.5'e kıyasla kademeli bir iyileşme sunar. Taşıma işlemi yaparken aşağıdakileri göz önünde bulundurun:

- **Düşünen:** Gemini 2.5'i mantık yürütmeye zorlamak için daha önce karmaşık istem mühendisliği (ör. düşünce zinciri) kullanıyorsanız `thinking_level: "high"` ile Gemini 3'ü ve basitleştirilmiş istemleri deneyin.
- **Sıcaklık ayarları:** Mevcut kodunuz sıcaklığı açıkça ayarlıyorsa (özellikle de deterministik çıkışlar için düşük değerlere ayarlıyorsa) olası döngü sorunlarını veya karmaşık görevlerde performans düşüşünü önlemek için bu parametreyi kaldırmanızı ve Gemini 3'ün varsayılan değeri olan 1.0'ı kullanmanızı öneririz.
- **PDF ve belge anlama:**
  Yoğun belge ayrıştırma için belirli bir davranışa güveniyorsanız doğruluğun devamlılığını sağlamak amacıyla yeni `media_resolution_high` ayarını test edin.
- **Jeton tüketimi:** Varsayılan olarak Gemini 3'e geçiş, PDF'ler için jeton kullanımını **artırabilir** ancak videolar için jeton kullanımını **azaltabilir**. Varsayılan çözünürlüklerin yükselmesi nedeniyle istekler artık bağlam penceresini aşıyorsa medya çözünürlüğünü açıkça düşürmenizi öneririz.
- **Görüntü segmentasyonu:** Görüntü segmentasyonu özellikleri (nesneler için piksel düzeyinde maskeler döndürme) Gemini 3 Pro veya Gemini 3 Flash'te desteklenmez. Yerel görüntü segmentasyonu gerektiren iş yükleri için düşünme özelliği devre dışı bırakılmış Gemini 2.5 Flash'i kullanmaya devam etmenizi öneririz.
- **Bilgisayar Kullanımı:** Gemini 3 Pro ve Gemini 3 Flash, [Bilgisayar Kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr)'nı destekler. 2.5 serisinin aksine, Bilgisayar Kullanımı aracına erişmek için ayrı bir model kullanmanız gerekmez.
- **Araç desteği**: [Yerleşik araçları işlev çağrısıyla birleştirme](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) artık Gemini 3 modellerinde destekleniyor. [Haritalar
  temellendirmesi](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr) artık Gemini 3
  modellerinde de destekleniyor.
- **Aday sayısı**: Gemini 3 modelleri `candidateCount > 1` özelliğini desteklemez.
  Bu parametrenin `1` değerinden büyük bir değere ayarlanması 400 hatası döndürür.

## OpenAI uyumluluğu

[OpenAI uyumluluk katmanını](https://ai.google.dev/gemini-api/docs/openai?hl=tr) kullananlar için standart parametreler (OpenAI'ın `reasoning_effort`) otomatik olarak Gemini (`thinking_level`) eşdeğerleriyle eşlenir.

## İstemlerle ilgili en iyi uygulamalar

Gemini 3, istem oluşturma şeklinizi değiştiren bir akıl yürütme modelidir.

- **Net talimatlar:** Giriş istemlerinizde kısa ve öz olun. Gemini 3, doğrudan ve net talimatlara en iyi şekilde yanıt verir. Eski modeller için kullanılan ayrıntılı veya aşırı karmaşık istem mühendisliği tekniklerini aşırı analiz edebilir.
- **Çıkış ayrıntı düzeyi:** Gemini 3 varsayılan olarak daha az ayrıntılıdır ve doğrudan, etkili yanıtlar vermeyi tercih eder. Kullanım alanınız daha sohbet odaklı veya "konuşkan" bir karakter gerektiriyorsa istemde modeli açıkça yönlendirmeniz gerekir (ör. "Bunu arkadaş canlısı, konuşkan bir asistan gibi açıkla").
- **Bağlam yönetimi:** Büyük veri kümeleriyle (ör. kitapların tamamı, kod tabanları veya uzun videolar) çalışırken özel talimatlarınızı ya da sorularınızı istemin sonuna, veri bağlamından sonra ekleyin. Sorunuza "Yukarıdaki bilgilere göre..." gibi bir ifadeyle başlayarak modelin muhakemesini sağlanan verilere dayandırın.

İstem tasarımı stratejileri hakkında daha fazla bilgiyi [istem mühendisliği kılavuzunda](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=tr) bulabilirsiniz.

## SSS

1. **Gemini 3'ün son güncel bilgi tarihi nedir?** Gemini 3 modellerinin son güncel bilgi tarihi Ocak 2025'tir. Daha güncel bilgiler için [Search Grounding](https://ai.google.dev/gemini-api/docs/google-search?hl=tr) aracını kullanın.
2. **Bağlam penceresi sınırları nelerdir?** Gemini 3 modelleri, 1 milyon parçalık giriş bağlam penceresini ve 64 bin parçaya kadar çıkışı destekler.
3. **Gemini 3 için ücretsiz katman var mı?** Gemini API'de Gemini 3 Flash
   `gemini-3-flash-preview` ve 3.1 Flash-Lite `gemini-3.1-flash-lite` için ücretsiz katmanlar bulunur. Google AI Studio'da Gemini 3.1 Pro ve 3 Flash'i ücretsiz olarak deneyebilirsiniz ancak Gemini API'de `gemini-3.1-pro-preview` için ücretsiz katman bulunmamaktadır.
4. **Eski `thinking_budget` kodum çalışmaya devam eder mi?** Evet, `thinking_budget` geriye dönük uyumluluk için hâlâ desteklenmektedir ancak daha öngörülebilir bir performans için `thinking_level`'ye geçmenizi öneririz. Aynı istekte ikisini birden kullanmayın.
5. **Gemini 3, Batch API'yi destekliyor mu?** Evet, Gemini 3, [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr)'yi destekler.
6. **Bağlamı önbelleğe alma özelliği destekleniyor mu?** Evet, Gemini 3'te [Context Caching](https://ai.google.dev/gemini-api/docs/caching?hl=tr) (Bağlam Önbelleğe Alma) desteklenir.
7. **Gemini 3'te hangi araçlar desteklenir?** Gemini 3; [Google Arama](https://ai.google.dev/gemini-api/docs/google-search?hl=tr), [Google Haritalar ile Temellendirme](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr), [Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr), [Kod Yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) ve [URL Bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr)'nı destekler. Ayrıca, kendi özel araçlarınız için ve [yerleşik araçlarla birlikte](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) standart [Function Calling](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)'i destekler.
8. **`gemini-3.1-pro-preview-customtools` nedir?** `gemini-3.1-pro-preview` kullanıyorsanız ve model, bash komutlarını tercih ederek özel araçlarınızı yoksayıyorsa bunun yerine `gemini-3.1-pro-preview-customtools` modelini deneyin. Daha fazla bilgiye [buradan](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=tr#gemini-31-pro-preview-customtools) ulaşabilirsiniz.

## Sonraki adımlar

- [Gemini 3 Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=tr#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)'u kullanmaya başlayın
- [Düşünme düzeyleri](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=tr#gemini3) ve düşünme bütçesinden düşünme düzeylerine nasıl geçileceği hakkında özel Cookbook kılavuzunu inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-07 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-07 UTC."],[],[]]
