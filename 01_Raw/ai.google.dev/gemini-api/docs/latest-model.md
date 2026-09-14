---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=tr
fetched_at: 2026-09-14T05:41:23.800655+00:00
title: "Gemini 3.8 Flash'teki yenilikler \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)

Geri bildirim gönderin

# Gemini 3.8 Flash'teki yenilikler

[Tüm modelleri göster](https://ai.google.dev/gemini-api/docs/models?hl=tr)

Gemini 3.8 Flash (`gemini-3.8-flash`) genel kullanıma sunuldu (GK) ve üretimde kullanılmaya hazır. Bu model, uzun vadeli yazılım mühendisliği, otonom ajanlar ve karmaşık kurumsal iş akışları için tasarlanmış en akıllı Flash modelimizdir.

Bu rehberde Gemini 3.8 Flash'teki yenilikler, API değişiklikleri, kod örnekleri ve taşıma yönergeleri açıklanmaktadır.

## Yeni model

| Model | Model Kimliği | Varsayılan düşünme düzeyi | Fiyatlandırma | Açıklama |
| --- | --- | --- | --- | --- |
| Gemini 3.8 Flash | `gemini-3.8-flash` | `medium` | 3.8 Flash, yıl sonuna kadar 0,75 ABD doları/1 milyon giriş jetonu ve 3,75 ABD doları/1 milyon çıkış jetonu tanıtım fiyatıyla kullanılabilir. Daha fazla bilgi için [fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) bölümüne bakın. | Uzun vadeli yazılım mühendisliği, otonom ajanlar ve karmaşık kurumsal iş akışları için tasarlanmış en akıllı Flash modelimiz. |

Gemini 3.8 Flash, 1 milyon parçalık bağlam penceresini, 64 bin maksimum çıkış parçacığını, ayarlanabilir düşünme düzeylerini (`low`, `medium`, `high`) ve aynı kapsamlı yerleşik araç paketini destekler.

Tüm özellikler için [Gemini 3.8 Flash model sayfasına](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=tr) bakın. Tanıtım fiyatlandırmasıyla ilgili ayrıntılar için aşağıdaki [fiyatlandırma bölümüne](#pricing) veya [fiyatlandırma sayfasına](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#gemini-3.8-flash) bakın.

## Hızlı başlangıç kılavuzu

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Write a three.js script that renders a realistic 3D black hole."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Write a three.js script that renders a realistic 3D black hole.",
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("Hello world"))
    .build();
Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Write a three.js script that renders a realistic 3D black hole."
  }'
```

## Gemini 3.8 Flash'teki yenilikler

- **Uzun vadeli yazılım mühendisliği:** Gerçek dünyadaki kodlama kıyaslamalarında, karmaşık çok dosyalı yeniden düzenlemelerde ve deterministik araç yürütmede güçlü sonuçlar verir. Ayrıntılar için [değerlendirme metodolojisine](https://deepmind.google/models/evals-methodology/gemini-3-8-flash/?hl=tr) bakın.
- **Özerk ajanlar:** Dayanıklı çok adımlı planlama ve araç düzenleme iş akışları oluşturmanıza olanak tanır. Böylece başarısız döngüler ve hatalar önemli ölçüde azalır.
- **Karmaşık kurumsal iş akışları:** Zorlu alan görevleri ve büyük ölçekli veri ardışık düzenlerinde üstün doğruluk, derinlemesine muhakeme ve yüksek düzeyde olgusal kesinlik sağlar.
- **Yönetilen ajanlar için varsayılan model:** Yönetilen ajanlar için varsayılan ajan olan [Antigravity ajanı](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr) artık Gemini 3.8 Flash'i kullanıyor. [Antigravity SDK](https://antigravity.google/docs/sdk/overview/?hl=tr) da varsayılan olarak Gemini 3.8 Flash'i kullanır.
- **Tanıtım fiyatı:** Gemini 3.8 Flash, 31 Aralık 2026'ya kadar 0,75 ABD doları/1 milyon giriş jetonu ve 3,75 ABD doları/1 milyon çıkış jetonu tanıtım fiyatıyla kullanılabilir. 1 Ocak 2027'den itibaren 1,50 ABD doları/1 milyon giriş jetonu ve 7,50 ABD doları/1 milyon çıkış jetonu standart fiyatlandırması geçerli olacaktır.

Gemini 3.8 Flash, tasarım gereği daha uzun süren ve karmaşık görevlerde daha fazla jeton kullanabilir. Model, zorlu ve çok adımlı hedeflerde daha kaliteli sonuçlar sunmak için daha küçük muhakeme adımları atar, araçları yinelemeli olarak çağırır ve bu süreçte yaptığı işi doğrular. Her iş akışının bu düzeyde doğrulamaya ihtiyacı yoktur. Günlük görevler için jeton tüketimini azaltmak amacıyla [muhakeme](#understanding-reasoning-levels) çabasını düşürebilirsiniz. Alternatif olarak, Gemini 3.7 Flash tam olarak desteklenmeye devam eder.

## Akıl yürütme düzeylerini anlama

Gemini 3.8 Flash, modelin düşünme düzeyini ayarlayarak gecikme ve zeka üzerinde esnek kontrol sağlar:

- **Düşük düşünme çabası**: Olay yanıtı işlem hatları, anlık sohbet, taslak yazma ve hızlı veri analizi gibi gecikmenin kritik olduğu görevlerde yanıt süresini kısaltır.
- **Orta (varsayılan):** Çoğu görev için en iyi kalite. Karmaşık kod ve yapay zeka aracılı kullanım alanları için önerilir. İlk geçişte daha yüksek doğruluk sağlar.
- **Yüksek düşünme çabası**: Modelin akıl yürütme ve araç düzenleme özelliklerini en üst düzeye çıkarır. Derinlemesine akıl yürütme, matematik ve zorlu çok adımlı görevler için idealdir.

Aşağıdaki örnekte, karmaşık bir kod analizi isteği için `thinking_level` değeri `medium` olarak ayarlanıyor:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    generation_config={
        "thinking_level": "medium"  # Balanced reasoning effort for complex tasks
    }
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  generation_config: {
    thinking_level: "medium"
  }
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("Hello world"))
    .build();
Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    "generation_config": {
      "thinking_level": "medium"
    }
  }'
```

## Antigravity aracısı güncellendi

Gemini Managed Agents'taki [Antigravity temsilcisi](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr), gelişmiş performansı ve akıl yürütme becerisi sayesinde artık varsayılan olarak Gemini 3.8 Flash ile oluşturuluyor.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=(
        "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
        "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
        "Check search indexing with Google Search for site:web.dev. "
        "Format the output as a side-by-side scorecard table with prioritized fixes."
    ),
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
  input: "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
  environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();
CreateModelInteraction req = CreateModelInteraction.builder()
    .model(Model.of("gemini-3.8-flash"))
    .input(InteractionsInput.of("Hello world"))
    .build();
Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(req)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google'\''s PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
    "environment": "remote"
}'
```

Temel Gemini modeli, `agent_config` kullanılarak [yapılandırılabilir](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr#model-selection).

## Taşıma kontrol listesi

```
  `/gemini-api-dev migrate my app to Gemini 3.8 Flash`
```

### gemini-3.8-flash'e geçiş yapma

- **Model Kimliğini Güncelle:** Hedef model dizesini `gemini-3.8-flash` olarak değiştirin.
- **Desteği sonlandırılan örnekleme parametrelerini kaldırma:**
  - Oluşturma yapılandırmalarından `temperature`, `top_p` ve `top_k` öğelerini kaldırın.
  - `thinking_budget` yerine dize numaralandırması `thinking_level` yazın. `minimal` simgesinin 3.8 Flash'ta desteklenmediğini unutmayın.
  - `candidate_count` simgesini kaldırın (Gemini 3 ve sonraki sürümlerde desteklenmez).
- **Hamle doğrulama kurallarını zorunlu kılma:**
  - Sunucu tarafında çok aşamalı etkileşim görüşmelerini standartlaştırın `previous_interaction_id`.
  - Önceden doldurulmuş model dönüşlerini kaldırın.
- **İşlev çağrısını denetleme:**
  - Çok formatlı öğeleri yanıt yükünün içine yerleştirin.
  - Satır içi talimatları `\n\n` kullanarak biçimlendirin.
  - Araç öncesi metinle ilgili `Malformed_Function_Call` hataları görüyorsanız [Araç öncesi metin koşulları için geçici çözümler](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr#workarounds-for-pre-tool-text-requirements) başlıklı makaleyi inceleyin.
  - Yalnızca generateContent API kullanılıyorsa: Tüm `FunctionResponse` nesnelerinin `call_id` ve `name` içerdiğinden emin olun.
- **Temel Gemini 3 şartları:** SDK güncellemeleri ve düşünce imzası koruması için [Gemini 3.5'e Geçiş Yapılacak İşler Listesi](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=tr#migration)'ne bakın.

## Fiyatlandırma

Gemini 3.8 Flash, Gemini 3.7 Flash ve Gemini 3.6 Flash için 31 Aralık 2026'ya kadar Google AI Studio ve Gemini Enterprise Agent Platform'da tanıtım fiyatlarından yararlanın. Standart fiyatlandırma 1 Ocak 2027'den itibaren geçerli olacak. Fiyatlandırma katmanlarının tamamı için [fiyatlandırma sayfasına](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#gemini-3.8-flash) bakın.

## Sonraki adımlar

- [Modellere Genel Bakış](https://ai.google.dev/gemini-api/docs/models?hl=tr) sayfasındaki API spesifikasyonlarını inceleyin.
- [Interactions API'sine Genel Bakış](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) bölümünde çoklu ajan düzenlemeyi keşfedin.
- [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=tr)'da istemleri test edin ve iyileştirin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-03 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-03 UTC."],[],[]]
