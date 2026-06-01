---
source_url: https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=tr
fetched_at: 2026-06-01T06:03:12.320757+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Öncelik çıkarımı

Gemini Priority API, daha düşük gecikme süresi ve en yüksek güvenilirlik gerektiren, işletme açısından kritik iş yükleri için tasarlanmış premium bir çıkarım katmanıdır. Bu katman, premium fiyat noktasında sunulur. Öncelikli katman trafiğine, standart API ve esnek katman trafiğine göre öncelik verilir.

Öncelikli çıkarım, Etkileşimler API uç noktalarında kullanılabilir.

## Öncelik özelliğini kullanma

Öncelikli katmanı kullanmak için isteğinizdeki `service_tier` alanını `priority` olarak ayarlayın. Alan atlanırsa varsayılan katman standarttır.

### Python

```
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="Triage this critical customer support ticket immediately.",
        service_tier='priority'
    )

    print(interaction.output_text)

except Exception as e:
    print(f"Error during API call: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const interaction = await ai.interactions.create({
          model: "gemini-3.5-flash",
          input: "Triage this critical customer support ticket immediately.",
          service_tier: "priority"
      });

      console.log(interaction.output_text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Öncelikli çıkarımın işleyiş şekli

Öncelikli çıkarım, istekleri yüksek önem dereceli bilgi işlem kuyruklarına yönlendirerek kullanıcıya yönelik uygulamalar için tahmin edilebilir ve hızlı performans sunar. Bu özelliğin temel mekanizması, dinamik sınırları aşan trafik için sunucu tarafında standart işleme sorunsuz bir şekilde geçiş yaparak isteği başarısız kılmak yerine uygulamanın kararlılığını sağlamaktır.

| Özellik | Öncelik | Standart | Yaratıcılığınızı | Toplu |
| --- | --- | --- | --- | --- |
| **Fiyatlandırma** | Standart'tan% 75-100 daha fazla | Tam fiyat | %50 indirim | %50 indirim |
| **Gecikme** | Saniye | Saniyelerden dakikalara | Dakikalar (1-15 dakika hedef) | En fazla 24 saat |
| **Güvenilirlik** | Yüksek (tüy dökmeyen) | Yüksek / Biraz yüksek | En iyi sonuç (Sheddable) | Yüksek (işleme hızı için) |
| **Arayüz** | Eşzamanlı | Eşzamanlı | Eşzamanlı | Eşzamansız |

### Temel avantajlar

- **Düşük gecikme**: Etkileşimli, kullanıcıya yönelik yapay zeka araçları için saniyelik yanıt süreleri sunacak şekilde tasarlanmıştır.
- **Yüksek güvenilirlik**: Trafik en yüksek öncelik seviyesinde ele alınır ve kesinlikle bırakılmaz.
- **Kontrollü azalma**: Dinamik sınırları aşan trafik artışları, başarısız olmak yerine işleme için otomatik olarak Standart katmanına düşürülür ve hizmet kesintileri önlenir.
- **Kolaylık**: Standart ve Flex katmanlarıyla aynı senkron `create` yöntemi kullanılır.

### Kullanım alanları

Öncelikli işleme, performans ve güvenilirliğin en önemli olduğu, işletme açısından kritik iş akışları için idealdir.

- **Etkileşimli yapay zeka uygulamaları**: Kullanıcıların premium ödeme yaptığı ve hızlı, tutarlı yanıtlar beklediği müşteri hizmetleri sohbet botları ve yardımcı pilotlar.
- **Anlık karar motorları**: Canlı bilet önceliklendirme veya sahtekarlık tespiti gibi yüksek güvenilirlik ve düşük gecikme süresi gerektiren sistemler.
- **Premium müşteri özellikleri**: Ücretli müşteriler için daha yüksek hizmet düzeyi hedefleri (SLO'lar) garanti etmesi gereken geliştiriciler.

### Hız sınırları

Öncelikli tüketim, [genel etkileşimli trafik hızı sınırlarına](https://aistudio.google.com/rate-limit?hl=tr) dahil edilse de kendi hız sınırlarına sahiptir. Öncelikli çıkarım için varsayılan sıklık sınırları **Model / Katman için standart sıklık sınırının 0,3 katıdır**.

### Kontrollü sürüm düşürme mantığı

Yoğunluk nedeniyle öncelik sınırları aşılırsa taşma istekleri, 503 veya 429 hatasıyla başarısız olmak yerine **otomatik olarak ve sorunsuz bir şekilde** standart işleme düşürülür. Düşürülmüş istekler, öncelikli premium oran üzerinden değil, standart oran üzerinden faturalandırılır.

### Müşterinin sorumluluğu

- **Yanıt izleme**: Geliştiriciler, isteklerin sık sık `x-gemini-service-tier`
  düşürülüp düşürülmediğini tespit etmek için API yanıtındaki `standard` başlığını izlemelidir.
- **Yeniden denemeler**: İstemciler, `DEADLINE_EXCEEDED` gibi standart hatalar için yeniden deneme mantığı/eksponansiyel geri yükleme uygulamalıdır.

## Fiyatlandırma

Öncelikli çıkarım, [standart API](https://ai.google.dev/gemini-api/docs/pricing?hl=tr)'den% 75-100 daha yüksek bir fiyata sunulur ve jeton başına faturalandırılır.

## Desteklenen modeller

Aşağıdaki modellerde öncelikli çıkarım desteklenir:

| Model | Öncelik çıkarımı |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=tr) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr) | ✔️ |
| [Gemini 3.1 Pro Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=tr) | ✔️ |
| [Gemini 3 Flash Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=tr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=tr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=tr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=tr) | ✔️ |

## Sırada ne var?

- Maliyet azaltımı için [esnek çıkarım](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=tr).
- [Jetonlar](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=tr): Jetonları anlayın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-28 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-28 UTC."],[],[]]
