---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=tr
fetched_at: 2026-09-14T05:37:12.993183+00:00
title: "\u00d6ncelik \u00e7\u0131kar\u0131m\u0131 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/generate-content?hl=tr)

Geri bildirim gönderin

# Öncelik çıkarımı

Açıklama: Priority çıkarım katmanıyla gecikmeyi nasıl optimize edeceğinizi öğrenin

Gemini Priority API, daha düşük gecikme süresi ve en yüksek güvenilirlik gerektiren, işletme açısından kritik iş yükleri için tasarlanmış premium bir çıkarım katmanıdır. Bu katman, premium fiyat noktasında sunulur. Öncelikli katman trafiğine, standart API ve esnek katman trafiğine göre öncelik verilir.

Öncelikli çıkarım, GenerateContent API ve Interactions API uç noktalarında [2. ve 3. katman](https://ai.google.dev/gemini-api/docs/billing?hl=tr#about-billing) kullanıcıları tarafından kullanılabilir.

## Öncelik özelliğini kullanma

Öncelik katmanını kullanmak için istek gövdesindeki `service_tier` alanını `priority` olarak ayarlayın. Alan atlanırsa varsayılan katman standarttır.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3.6-flash",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
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
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## Öncelikli çıkarımın işleyiş şekli

Öncelikli çıkarım, istekleri yüksek önem dereceli bilgi işlem kuyruklarına yönlendirerek kullanıcıya yönelik uygulamalar için tahmin edilebilir ve hızlı performans sunar. Birincil mekanizması, dinamik sınırları aşan trafik için sunucu tarafında standart işleme sorunsuz bir şekilde geçiş yaparak isteği başarısız kılmak yerine uygulama kararlılığını sağlamaktır.

| Özellik | Öncelik | Standart | Yaratıcılığınızı | Toplu |
| --- | --- | --- | --- | --- |
| **Fiyatlandırma** | Standart'tan% 75-100 daha fazla | Tam fiyat | %50 indirim | %50 indirim |
| **Gecikme** | Saniye | Saniyeden dakikaya | Dakika (1-15 dakika hedef) | En fazla 24 saat |
| **Güvenilirlik** | Yüksek (tüy dökmeyen) | Yüksek / Biraz yüksek | En iyi sonuç (Sheddable) | Yüksek (işleme hızı için) |
| **Arayüz** | Eşzamanlı | Eşzamanlı | Eşzamanlı | Eşzamansız |

### Temel avantajlar

- **Düşük gecikme**: Etkileşimli, kullanıcıya yönelik yapay zeka araçları için saniyelik yanıt süreleri sunmak üzere tasarlanmıştır.
- **Yüksek güvenilirlik**: Trafik en yüksek öncelik seviyesinde ele alınır ve kesinlikle bırakılmaz.
- **Kontrollü azalma**: Dinamik sınırları aşan trafik artışları, başarısız olmak yerine işleme için otomatik olarak Standart katmanına düşürülür ve hizmet kesintileri önlenir.
- **Kolay**: Standart ve Flex katmanlarıyla aynı senkron `generateContent` yöntemi kullanılır.

### Kullanım alanları

Öncelikli işleme, performans ve güvenilirliğin en önemli olduğu, işletme açısından kritik iş akışları için idealdir.

- **Etkileşimli yapay zeka uygulamaları**: Kullanıcıların premium ödeme yaptığı ve hızlı, tutarlı yanıtlar beklediği müşteri hizmetleri chatbot'ları ve yardımcı pilotlar.
- **Anlık karar motorları**: Canlı bilet önceliklendirme veya sahtekarlık tespiti gibi yüksek güvenilirlik ve düşük gecikme süresi gerektiren sistemler.
- **Premium müşteri özellikleri**: Ücretli müşteriler için daha yüksek hizmet düzeyi hedefleri (SLO'lar) garanti etmesi gereken geliştiriciler.

### Hız sınırları

Öncelikli tüketim, [genel etkileşimli trafik hızı sınırlarına](https://aistudio.google.com/rate-limit?hl=tr) dahil edilse de kendi hız sınırlarına sahiptir. Öncelikli çıkarım için varsayılan sıklık sınırları **Model / Katman için standart sıklık sınırının 0,3 katıdır**.

### Kontrollü sürüm düşürme mantığı

Yoğunluk nedeniyle öncelik sınırları aşılırsa taşma istekleri, 503 veya 429 hatasıyla başarısız olmak yerine **otomatik olarak ve sorunsuz bir şekilde** standart işleme düşürülür. Düşürülmüş istekler, öncelikli premium oran üzerinden değil, standart oran üzerinden faturalandırılır.

### Müşterinin sorumluluğu

- **Yanıt izleme**: Geliştiriciler, isteklerin sık sık `x-gemini-service-tier`
  sürümüne düşürülüp düşürülmediğini tespit etmek için API yanıtındaki `standard` başlığını izlemelidir.
- **Yeniden denemeler**: İstemciler, `DEADLINE_EXCEEDED` gibi standart hatalar için yeniden deneme mantığı/eksponansiyel geri yükleme uygulamalıdır.

## Fiyatlandırma

Öncelikli çıkarım, [standart API](https://ai.google.dev/gemini-api/docs/pricing?hl=tr)'den% 75-100 daha yüksek bir fiyatla sunulur ve jeton başına faturalandırılır.

## Desteklenen modeller

Aşağıdaki modellerde öncelikli çıkarım desteklenir:

| Model | Öncelik çıkarımı |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=tr) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=tr) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=tr) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr) | ✔️ |
| [Gemini 3.1 Pro Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=tr) | ✔️ |
| [Gemini 3 Flash Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=tr) | ✔️ |
| [Gemini 3 Pro ile Görüntü Önizleme](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=tr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=tr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=tr) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=tr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=tr) | ✔️ |

## Sırada ne var?

Gemini'ın diğer [çıkarım ve optimizasyon](https://ai.google.dev/gemini-api/docs/optimization?hl=tr) seçenekleri hakkında bilgi edinin:

- %50 maliyet tasarrufu için [Flex çıkarımı](https://ai.google.dev/gemini-api/docs/flex-inference?hl=tr).
- 24 saat içinde eşzamansız işleme için [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr).
- Giriş jetonu maliyetlerini azaltmak için [bağlam önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr).

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-12 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-12 UTC."],[],[]]
