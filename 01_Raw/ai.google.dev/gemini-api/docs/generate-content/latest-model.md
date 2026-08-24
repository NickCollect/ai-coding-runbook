---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=tr
fetched_at: 2026-08-24T02:26:40.082717+00:00
title: "En yeni Gemini modellerini kullanma \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# En yeni Gemini modellerini kullanma

[Bu sayfa](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=tr)

Gemini 3.6 Flash (`gemini-3.6-flash`) ve Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) genel kullanıma sunuldu ve üretimde kullanılmaya hazır.

- **Gemini 3.6 Flash**: Karmaşık görevlerde ve çok formatlı görevlerde daha güçlü performans sunarken 3.5 Flash'e kıyasla daha düşük bir fiyatla jeton kullanımını azaltır.
- **Gemini 3.5 Flash-Lite**: 3.5 ailesindeki en hızlı ve en düşük maliyetli modeldir. Yüksek işleme hızıyla yürütme için önceki Flash-Lite nesillerinden daha iyi performans gösterir.

Bu kılavuzda, her modeldeki yenilikler, kodunuzu etkileyen API değişiklikleri ve nasıl geçiş yapacağınız açıklanmaktadır.

### Gemini 3.6 Flash

1. Beceriyi yükleyin:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Beceriyi uygulama:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. Beceriyi yükleyin:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Beceriyi uygulama:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## Yeni modeller

| Model | Model Kimliği | Varsayılan düşünme düzeyi | Fiyatlandırma | Açıklama |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | 1,50 ABD doları/1 milyon giriş jetonu ve 7,50 ABD doları/1 milyon çıkış jetonu | Ajan tabanlı ve çok formatlı görevler için hız ile akıl arasında denge kurar. |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | 0,30 ABD doları/1 milyon giriş jetonu ve 2,50 ABD doları/1 milyon çıkış jetonu | Yüksek işleme hızı için en hızlı ve en düşük maliyetli 3.5 modeli. |

Her iki model de 1 milyon parçalık bağlam penceresini, 64 bin maksimum çıkış parçası sayısını, düşünme özelliğini ve [Bilgisayar Kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr) da dahil olmak üzere yerleşik araçların tamamını destekler.

Tam özellikler için model sayfalarına bakın:

- [Gemini 3.6 Flash model sayfası](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=tr)
- [Gemini 3.5 Flash-Lite model sayfası](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=tr)

Ayrıntılı fiyatlandırma bilgileri için [fiyatlandırma sayfasına](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) bakın.

## Hızlı başlangıç kılavuzu

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Write a three.js script that renders an interactive 3D robot.",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Write a three.js script that renders an interactive 3D robot.",
  });
  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }]
  }'
```

## Gemini 3.6 Flash'teki yenilikler

- **Token ve dönüş azaltma:** Çok adımlı iş akışlarını Gemini 3.5'e kıyasla daha az muhakeme adımı, sohbet dönüşü ve araç çağrısıyla tamamlar. Ayrıca yürütme döngüsünün spiral şeklinde ilerlemesini de azaltır.
- **Geliştirilmiş kod oluşturma:** Daha az istenmeyen düzenleme ve daha az hata ayıklama döngüsüyle üretime hazır, daha yüksek kaliteli kodlar üretir.
- **Daha iyi talimat takibi**: Teşhis görevleri sırasında istenmeyen dosya değişikliklerini azaltır.
- **Güçlü çok formatlı ve uzamsal akıl yürütme:** Grafik yorumlama, görsel plan dönüştürme ve çok öğeli web düzeni oluşturma konusunda daha iyi performans.
- **Önceden programatik inceleme:** Değişiklik yapmadan önce teşhis kodu komut dosyalarını Gemini 3.5 Flash'e kıyasla daha sık çalıştırmayı tercih eder. Bu, karmaşık görevlerde doğruluğu artırır ancak basit ön uç çalışmalarında ek keşif adımları ekleyebilir.
- **Bilgisayar Kullanımı desteği:** Ajanlı kullanıcı arayüzü otomasyonu için yerel araç olarak desteklenir.
- **Kullanıcı arayüzü stil tercihi**: İşlevsel kod oluşturma konusunda daha iyi olsa da insan değerlendiriciler görsel düzen ve stil için önceki modelleri tercih etti. Açık tasarım kuralları belirleyerek bu durumu önleyebilirsiniz.
- **Varsayılan düşünme çabası (orta):** Gemini 3.5 Flash ile aynı `medium` varsayılan düşünme düzeyini kullanır.
- **Daha düşük fiyatlandırma**: Daha düşük çıkış jetonu maliyetleri (3.5 Flash için 9,00 ABD doları/1 milyon jeton yerine 7,50 ABD doları/1 milyon jeton). Giriş jetonları 1,50 ABD doları/1 milyon olarak kalır.

## Gemini 3.5 Flash-Lite'taki yenilikler

- **Daha düşük görev yürütme gecikmesi:** Yüksek hacimli veri ayrıştırma ve doküman çıkarma için 3.5 ailesindeki en yüksek işleme hızı.
- **Gelişmiş akıl yürütme ve çok formatlı performans:** HLE (%18,0'a karşı %11,0) gibi akıl yürütme görevlerinde ve CharXIV (%74,5'e karşı %63,7) gibi çok formatlı karşılaştırmalarda daha yüksek puanlar alarak Gemini 2.5 Flash'ten sorunsuz bir şekilde geçiş yapın.
- **Alt aracı düzenleme ve araç güvenilirliği:** Kod yürütme, arama ve MCP iş akışlarında araç yürütme güvenilirliğini artırır. Bağımsız planlama ve karmaşık alt aracı görevleri için düşünme düzeyini artırın.
- **Gelişmiş belge anlama:** Belge ayrıştırma ve yapılandırılmış veri çıkarma işlemlerinde doğruluğu artırır. Belgenin karmaşıklığına bağlı olarak hem minimum hem de yüksek düşünme seviyelerini deneyin.
- **Etkileşimli web kodlama ve tablo verisi işleme:** Basit kod yürütme yoluyla planlama yaparak ön uç JavaScript ve tablo verisi işlemede güçlü bir performans gösterir.
- **Chatbot ve karakter kalıcılığı:** Gemini 3.1 Flash-Lite'a kıyasla çok aşamalı etkileşim talimatlarını daha iyi takip etme ve karakter tutarlılığı.
- **Bilgisayar Kullanımı desteği:** Ajanlı kullanıcı arayüzü otomasyonu için yerel araç olarak desteklenir.

## Doğru Flash veya Flash-Lite modelini seçme

İş yükleriniz için doğru modeli ve taşıma yolunu seçmek üzere bu tabloyu kullanın.

Her iki modelde de desteği sonlandırılan örnekleme parametrelerinin (`temperature`, `top_p`, `top_k`) ve önceden doldurulmuş model dönüşlerinin kaldırılması gerekir. Ayrıntılar için [API değişiklikleri](#api-changes-and-parameter-updates) başlıklı makaleyi inceleyin.

| Model | Birincil kullanım alanları | Önerilen taşıma hedefi |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | Kod oluşturma, uzamsal/çok formatlı akıl yürütme, çok adımlı ajan tabanlı iş akışları | **Gemini 3.5 Flash**, **Gemini 3 Flash (Önizleme)** veya **Gemini 3.1 Pro** |
| **Gemini 3.5 Flash-Lite**  `gemini-3.5-flash-lite` | Bağımsız alt aracı yürütme, yüksek hacimli veri analizi ve doküman çıkarma, yapılandırılmış JSON ayrıştırma | **Gemini 3.1 Flash-Lite** veya **Gemini 2.5 Flash** |

## Antigravity aracısı güncellendi

Gemini 3.6 Flash, performansının iyileştirilmesi sayesinde artık Gemini Yönetilen Ajanlar'daki [Antigravity ajanı](https://ai.google.dev/gemini-api/docs/antigravity-agentn?hl=tr) destekleyen yeni varsayılan model. Bu durum, API'de yeni bir alan ayarlanarak değiştirilebilir.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## API değişiklikleri ve parametre güncellemeleri

Gemini 3.6 Flash ve Gemini 3.5 Flash-Lite'tan itibaren, aşağıdaki API değişiklikleri bu modeller ve gelecekteki tüm Gemini model sürümleri için geçerli olacaktır.

- **Örnekleme parametresinin desteği sonlandırıldı**: `temperature`, `top_p` ve `top_k` parametrelerinin desteği sonlandırıldı. API bu parametreleri yok sayar ve gelecekteki model oluşturma işlemlerinde hata döndürür.
- **Önceden doldurulmuş model dönüşü doğrulama**: Model dönüşlerinin önceden doldurulması artık desteklenmiyor. İstekteki son boş olmayan dönüş bir `model` dönüşüyse API, `400` hatası döndürür.

Aşağıda, her API değişikliğiyle ilgili ayrıntılı açıklamalar ve kod örnekleri verilmiştir.

### 1. Örnekleme parametresinin desteğinin sonlandırılması (`temperature`, `top_p`, `top_k`)

`temperature`, `top_p` ve `top_k` kullanımdan kaldırıldı ve yoksayılıyor. Gelecekteki model nesillerinde bu parametrelerin sağlanması HTTP 400 hatası döndürür. **Bu parametreleri tüm isteklerden kaldırın.**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

Belirleyiciliği artırmak için belirli kullanım alanınıza yönelik açık kurallar içeren bir sistem talimatı tanımlayın.

### 2. Önceden doldurulmuş model dönüşü doğrulama

Boş olmayan bir model rolüyle biten API isteklerine izin verilmez ve **HTTP 400 Hatası** döndürülür.

#### ⚠️ Kullanılmasın

Eski `generateContent` veya ham REST yüklerinde, model rolü dönüşüyle bitenler artık yasaklanmıştır:

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ Önerilen taşıma

Uygulamanız daha önce girişleri bastırmak veya JSON biçimlendirmesini zorlamak için bir model dönüşünü önceden dolduruyorsa bunun yerine `system_instruction` veya [Yapılandırılmış çıkışlar](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr)'ı kullanın.

```
# ✅ RECOMMENDED: Use system_instruction to specify output format
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Translate 'Hello world' to Spanish.",
    config={"system_instruction": "Output only the translation without introductory text."},
)
```

## Taşıma kontrol listesi

### Gemini 3.6 Flash

1. Beceriyi yükleyin:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Beceriyi uygulama:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. Beceriyi yükleyin:

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. Beceriyi uygulama:

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### gemini-3.6-flash'e geçiş yapma

- **Model Kimliğini Güncelle:** Hedef model dizesini `gemini-3.6-flash` olarak değiştirin.
- **Desteği sonlandırılan örnekleme parametrelerini kaldırma:**
  - Üretim yapılandırmalarından `temperature`, `top_p` ve `top_k` öğelerini kaldırın.
  - `thinking_budget` öğesini, `"medium"` veya `"high"` olarak ayarlanmış dize numaralandırması `thinking_level` ile değiştirin.
  - `candidate_count` adlı ülkeyi kaldırın (Gemini 3.x'te desteklenmez).
- **Hamle doğrulama kurallarını zorunlu kılma:**
  - Önceden doldurulmuş model dönüşlerini kaldırın.
  - Son kullanıcı dönüşünün boş olmayan metin içerdiğinden emin olun.
- **İşlev çağrısını denetleme:**
  - Tüm `FunctionResponse` nesnelerinin `call_id` ve `name` içerdiğinden emin olun.
  - Çok formatlı öğeleri yanıt yükünün içine yerleştirin.
  - Satır içi talimatları `\\n\\n` kullanarak biçimlendirin.
  - Araç öncesi metinle ilgili `Malformed_Function_Call` hataları görüyorsanız [Araç öncesi metin koşulları için geçici çözümler](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=tr#workarounds-for-pre-tool-text-requirements) başlıklı makaleyi inceleyin.
- **Temel Gemini 3.x gereksinimleri:** SDK güncellemeleri ve düşünce imzası koruması için [Gemini 3.5'e Geçiş Yapılacaklar Listesi](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=tr#migration)'ne bakın.

### gemini-3.5-flash-lite'a geçiş

- **Model Kimliğini Güncelle:** Hedef model dizesini `gemini-3.5-flash-lite` olarak değiştirin.
- **Düşünme çabası seviyesini yapılandırma:**
  - Yüksek hacimli çıkarma, yönlendirme veya sınıflandırma için: Maksimum işleme hızı elde etmek üzere `thinking_level` değerini `"minimal"` (varsayılan) olarak bırakın.
  - Araç çağrıları, kod yürütme veya çok adımlı akıl yürütme içeren bağımsız alt aracılar için: Erken araç sonlandırmasını önlemek üzere `thinking_level` değerini `"medium"` veya `"high"` olarak ayarlayın.
- **Kullanımdan kaldırılan parametreleri kaldırın ve işlev çağrısını doğrulayın:** [3.6 Flash ile aynı kuralları](#migrate-to-gemini-3-6-flash) uygulayın.
- **Temel Gemini 3.x şartları:** [Gemini 3.5 Geçiş Kontrol Listesi](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=tr#migration)'ne bakın.

## Sonraki adımlar

- [Modellere Genel Bakış](https://ai.google.dev/gemini-api/docs/models?hl=tr) sayfasındaki API spesifikasyonlarını inceleyin.
- [Etkileşimler API Kılavuzu](https://ai.google.dev/gemini-api/docs/interactions?hl=tr)'nda çoklu aracı düzenlemesini keşfedin.
- [Google AI Studio](https://aistudio.google.com/?hl=tr)'da istemleri test edin ve iyileştirin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
