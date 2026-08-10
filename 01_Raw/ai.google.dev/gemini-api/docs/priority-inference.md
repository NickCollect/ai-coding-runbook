---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr
fetched_at: 2026-08-10T03:16:35.084715+00:00
title: "\u00d6ncelik \u00e7\u0131kar\u0131m\u0131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Öncelik çıkarımı

Açıklama: Etkileşimler API'sindeki öncelikli çıkarım katmanıyla gecikmeyi nasıl optimize edeceğinizi öğrenin.

Gemini Priority API, daha düşük gecikme süresi ve en yüksek güvenilirlik gerektiren, işletme açısından kritik iş yükleri için tasarlanmış premium bir çıkarım katmanıdır. Bu katman, premium fiyat noktasında sunulur. Öncelikli katman trafiğine, standart API ve esnek katman trafiğine göre öncelik verilir.

Öncelikli çıkarım, Interactions API uç noktalarında kullanılabilir.

## Öncelik özelliğini kullanma

Öncelikli katmanı kullanmak için isteğinizdeki `service_tier` alanını `priority` olarak ayarlayın. Alan atlanırsa varsayılan katman standarttır.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Triage this critical customer support ticket immediately.",
    service_tier='priority'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
    const interaction = await ai.interactions.create({
        model: "gemini-3.6-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Öncelikli çıkarımın işleyiş şekli

Öncelikli çıkarım, istekleri yüksek önem dereceli bilgi işlem kuyruklarına yönlendirerek kullanıcıya yönelik uygulamalar için tahmin edilebilir ve hızlı performans sunar. Birincil mekanizması, dinamik sınırları aşan trafik için sunucu tarafında standart işleme sorunsuz bir şekilde geçiş yaparak isteği başarısız kılmak yerine uygulama kararlılığını sağlamaktır.

| Özellik | Öncelik | Standart | Yaratıcılığınızı | Toplu |
| --- | --- | --- | --- | --- |
| **Fiyatlandırma** | Standart plandan% 75-100 daha fazla | Tam fiyat | %50 indirim | %50 indirim |
| **Gecikme** | Saniye | Saniyeden dakikaya | Dakikalar (1-15 dakika hedef) | En fazla 24 saat |
| **Güvenilirlik** | Yüksek (tüy dökmeyen) | Yüksek / Biraz yüksek | En iyi sonuç (Sheddable) | Yüksek (işleme hızı için) |
| **Arayüz** | Eşzamanlı | Eşzamanlı | Eşzamanlı | Eşzamansız |

### Temel avantajlar

- **Düşük gecikme**: Etkileşimli, kullanıcıya yönelik yapay zeka araçları için saniyelik yanıt süreleri sunacak şekilde tasarlanmıştır.
- **Yüksek güvenilirlik**: Trafik en yüksek öncelik seviyesinde ele alınır ve kesinlikle bırakılmaz.
- **Kontrollü azalma**: Dinamik sınırları aşan trafik artışları, başarısız olmak yerine işleme için otomatik olarak Standart katmanına düşürülür ve hizmet kesintileri önlenir.
- **Kolay**: Standart ve Flex katmanlarıyla aynı senkron `create` yöntemi kullanılır.

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

Öncelikli çıkarım, [standart API](https://ai.google.dev/gemini-api/docs/pricing?hl=tr)'den% 75-100 daha yüksek bir fiyata sahiptir ve jeton başına faturalandırılır.

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
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=tr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=tr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=tr) | ✔️ |

## Sırada ne var?

- Maliyet azaltımı için [esnek çıkarım](https://ai.google.dev/gemini-api/docs/flex-inference?hl=tr).
- [Jetonlar](https://ai.google.dev/gemini-api/docs/tokens?hl=tr): Jetonları anlayın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
