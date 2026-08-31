---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr
fetched_at: 2026-08-31T06:36:25.941413+00:00
title: "Google Haritalar ile temellendirme \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Google Haritalar ile temellendirme

Google Haritalar ile Temellendirme, Gemini'ın üretken özelliklerini Google Haritalar'ın zengin, doğru ve güncel verileriyle birleştirir. Bu özellik, geliştiricilerin konuma duyarlı işlevleri uygulamalarına kolayca dahil etmelerini sağlar. Kullanıcı sorgusu Haritalar verileriyle ilgili bir bağlama sahip olduğunda Gemini modeli, kullanıcının belirttiği konum veya genel alanla alakalı, olgusal olarak doğru ve güncel yanıtlar sağlamak için Google Haritalar'dan yararlanır.

- **Doğru ve konuma duyarlı yanıtlar:** Coğrafi olarak belirli sorgular için Google Haritalar'ın kapsamlı ve güncel verilerinden yararlanın.
- **Gelişmiş kişiselleştirme:** Kullanıcı tarafından sağlanan konumlara göre önerileri ve bilgileri uyarlayın.

## Başlayın

Bu örnekte, kullanıcı sorgularına doğru ve konuma duyarlı yanıtlar sağlamak için Google Haritalar ile Temellendirme'yi uygulamanıza nasıl entegre edeceğiniz gösterilmektedir. İstemde, isteğe bağlı kullanıcı konumuyla birlikte yerel öneriler isteniyor. Bu sayede Gemini modeli, Google Haritalar verilerini kullanabiliyor.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
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
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Google Haritalar ile Temellendirme'nin işleyiş şekli

Google Haritalar ile Temellendirme, temellendirme kaynağı olarak Maps API'sini kullanarak Gemini API'yi Google Coğrafi Ekosistemi ile entegre eder. Kullanıcının sorgusu coğrafi bağlam içerdiğinde Gemini modeli, Google Haritalar ile Temellendirme aracını çağırabilir. Model daha sonra, sağlanan konumla alakalı Google Haritalar verilerine dayalı yanıtlar üretebilir.

Bu süreç genellikle şunları içerir:

1. **Kullanıcı sorgusu:** Bir kullanıcı, uygulamanıza coğrafi bağlam da içerebilecek bir sorgu gönderir (ör. "yakınımdaki kafeler", "San Francisco'daki müzeler").
2. **Araç çağırma:** Coğrafi amaçlı sorguyu tanıyan Gemini modeli, Google Haritalar ile Temellendirme aracını çağırır. Bu araç, isteğe bağlı olarak kullanıcının `latitude` ve `longitude` ile birlikte sağlanabilir. Bu araç, metin tabanlı bir arama aracıdır ve Haritalar'da arama yapmaya benzer şekilde çalışır. Yerel sorgular ("yakınımdaki") koordinatları kullanırken belirli veya yerel olmayan sorguların açık konumdan etkilenmesi olası değildir.
3. **Veri alma:** Google Haritalar ile Temellendirme hizmeti, Google Haritalar'da alakalı bilgiler (ör. yerler, yorumlar, fotoğraflar, adresler, çalışma saatleri) için sorgu gönderir.
4. **Temellendirilmiş üretim:** Haritalar'dan alınan veriler, Gemini modelinin yanıtını bilgilendirmek için kullanılır. Böylece olgusal doğruluk ve alaka düzeyi sağlanır.
5. **Yanıt ve ek açıklamalar:** Model, Google Haritalar kaynaklarına bağlantı veren satır içi ek açıklamalar içeren bir metin yanıtı döndürür. Bu sayede geliştiriciler alıntıları gösterebilir.

## Google Haritalar ile Temellendirme neden ve ne zaman kullanılmalı?

Google Haritalar ile temellendirme, doğru, güncel ve konuma özel bilgiler gerektiren uygulamalar için idealdir. Dünya genelinde 250 milyondan fazla yerin bulunduğu Google Haritalar'ın kapsamlı veritabanı tarafından desteklenen alakalı ve kişiselleştirilmiş içerikler sunarak kullanıcı deneyimini iyileştirir.

Uygulamanızın aşağıdaki durumlarda Google Haritalar ile Temellendirme'yi kullanması gerekir:

- Coğrafi konuma özgü sorulara eksiksiz ve doğru yanıtlar verin.
- Sohbete dayalı gezi planlayıcıları ve yerel rehberler oluşturun.
- Konuma ve kullanıcı tercihlerine (ör. restoranlar veya mağazalar) göre ilgi çekici yerler önerin.
- Sosyal medya, perakende veya yemek teslimatı hizmetleri için konuma duyarlı deneyimler oluşturun.

Google Haritalar ile temellendirme, yakınlık ve güncel gerçek verilerin kritik olduğu kullanım alanlarında (ör. "yakınımdaki en iyi kafeyi" bulma veya yol tarifi alma) mükemmel sonuçlar verir.

## Kullanım alanları

Google Haritalar ile temellendirme, konuma duyarlı çeşitli kullanım alanlarını destekler.

### Yere özgü soruları yanıtlama

Google kullanıcı yorumlarına ve diğer Haritalar verilerine dayalı yanıtlar almak için belirli bir yer hakkında ayrıntılı sorular sorun.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Konuma dayalı kişiselleştirme sağlama

Kullanıcının tercihlerine ve belirli bir coğrafi bölgeye göre uyarlanmış öneriler alın.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Seyahat planı oluşturma konusunda yardım

Yol tarifleri ve çeşitli konumlar hakkında bilgiler içeren çok günlük planlar oluşturun. Bu planlar, seyahat uygulamaları için idealdir.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## Hizmet kullanım şartları

Bu bölümde, Google Haritalar ile Temellendirme için hizmet kullanım şartları açıklanmaktadır.

### Kullanıcıyı Google Haritalar kaynaklarının kullanımı hakkında bilgilendirin.

Her Google Haritalar Temelli sonuçta, `model_output` adımının her yanıtı destekleyen içerik bloklarında kaynak açıklamaları gösterilir. Aşağıdaki meta veriler döndürülür:

- kaynak URL
- ad

Google Haritalar ile Temellendirme'den elde edilen sonuçları sunarken ilişkili Google Haritalar kaynaklarını belirtmeniz ve kullanıcılarınızı aşağıdakiler hakkında bilgilendirmeniz gerekir:

- Google Haritalar kaynakları, kaynakların desteklediği oluşturulmuş içeriği hemen takip etmelidir. Bu oluşturulan içeriğe Google Haritalar'da Temellendirilmiş Sonuç da denir.
- Google Haritalar kaynakları, tek bir kullanıcı etkileşimi içinde görüntülenebilmelidir.

### Google Haritalar bağlantılarıyla Google Haritalar kaynaklarını görüntüleme

Her kaynak açıklaması için aşağıdaki koşullara uygun bir bağlantı önizlemesi oluşturulmalıdır:

- Google Haritalar metin [atfetme yönergelerine](#maps-attribution-guidelines) uyarak her kaynağı Google Haritalar'a atfedin.
- Yanıtta belirtilen kaynak adını gösterir.
- Açıklamadaki `url` simgesini kullanarak kaynağa bağlantı verin.

### Google Haritalar metin atıfı yönergeleri

Metinde kaynakları Google Haritalar'a atfederken aşağıdaki yönergeleri uygulayın:

- Google Haritalar metnini hiçbir şekilde değiştirmeyin:
  - Google Haritalar'ın büyük/küçük harf kullanımını değiştirmeyin.
  - Google Haritalar'ı birden fazla satıra sarmayın.
  - Google Haritalar'ı başka bir dile yerelleştirmeyin.
  - HTML özelliğini translate="no" kullanarak tarayıcıların Google Haritalar'ı çevirmesini engelleyin.

Google Haritalar veri sağlayıcılarımız ve lisans şartları hakkında daha fazla bilgi için [Google Haritalar ve Google Earth yasal bildirimleri](https://www.google.com/help/legalnotices_maps/?hl=tr)'ne bakın.

## En iyi uygulamalar

- **Kullanıcı konumunu sağlama:** En alakalı ve kişiselleştirilmiş yanıtlar için kullanıcının konumu bilindiğinde `google_maps` aracı yapılandırmanıza her zaman `latitude` ve `longitude` parametrelerini ekleyin.
- **Son Kullanıcıları Bilgilendirin:** Özellikle araç etkinleştirildiğinde, Google Haritalar verilerinin sorgularını yanıtlamak için kullanıldığını son kullanıcılarınıza net bir şekilde bildirin.
- **Gerekmediğinde Kapatma:** Google Haritalar ile temellendirme özelliği varsayılan olarak kapalıdır. Performansı ve maliyeti optimize etmek için yalnızca bir sorgunun net bir coğrafi bağlamı olduğunda (`"tools": [{"type": "google_maps"}]`) etkinleştirin.

## Sınırlamalar

- Google Haritalar ile temellendirme özelliği şu anda yalnızca İngilizce istemleri ve yanıtları desteklemektedir.
- Bu araç bazı bölgelerde kullanılamayabilir.
- Sonuçlar, konum doğruluğuna ve kullanılabilir Haritalar verilerine göre değişiklik gösterebilir.
- **Coğrafi Kapsam:** Google Haritalar ile Temellendirme özelliği dünya genelinde kullanılabilir.
- **Varsayılan Durum:** Google Haritalar ile Temellendirme aracı varsayılan olarak devre dışıdır.
  API isteklerinizde bunu açıkça etkinleştirmeniz gerekir.

## Fiyatlandırma ve sıklık sınırları

Google Haritalar ile temellendirme fiyatı, model nesline göre değişir:

- **Gemini 3 modelleri:** Projeniz, modelin yürütmeye karar verdiği her **arama sorgusu** için faturalandırılır. Tek bir **arama istemi** (modele yönelik API isteğiniz), modelin gerekli bilgileri bulmak için birden fazla arama sorgusu yürütmesine neden olabilir. Bu sorguların her biri, aracın faturalandırılabilir kullanımı olarak kabul edilir.
- **Gemini 2.5 ve eski modeller:** Projeniz için **arama istemi** başına faturalandırma yapılır.
  Bir istek yalnızca istem, bu sonucu elde etmek için modelin dahili olarak kaç ayrı arama sorgusu gerçekleştirdiğine bakılmaksızın, en az bir Google Haritalar temelli sonuç döndürdüğünde faturalandırılır.

Ayrıntılı fiyatlandırma bilgileri için [Gemini API fiyatlandırma sayfasına](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) bakın.

## Desteklenen modeller

Aşağıdaki modeller, Google Haritalar ile Temellendirme özelliğini destekler:

| Model | Google Haritalar ile Temellendirme |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=tr) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=tr) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=tr) | ✔️ |
| [Gemini 3.1 Pro Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=tr) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr) | ✔️ |
| [Gemini 3 Flash Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=tr) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=tr) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=tr) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=tr) | ✔️ |

## Desteklenen araç kombinasyonları

Gemini 3 modelleri, yerleşik araçların (ör. Google Haritalar ile Temellendirme) özel araçlarla (işlev çağrısı) birlikte kullanılmasını destekler. [Araç kombinasyonları](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) sayfasından daha fazla bilgi edinin.

## Sırada ne var?

- Diğer [kullanılabilir araçlar](https://ai.google.dev/gemini-api/docs/tools?hl=tr) hakkında bilgi edinin.
- Sorumlu yapay zekaya dair en iyi uygulamalar ve Gemini API'nin güvenlik filtreleri hakkında daha fazla bilgi edinmek için [Güvenlik ayarları kılavuzuna](https://ai.google.dev/gemini-api/docs/safety-settings?hl=tr) bakın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
