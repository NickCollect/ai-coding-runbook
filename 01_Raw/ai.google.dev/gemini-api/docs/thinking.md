---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=tr
fetched_at: 2026-06-29T05:38:51.576336+00:00
title: "Gemini d\u00fc\u015f\u00fcncesi \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini düşüncesi

[Gemini 3 ve 2.5 serisi modeller](https://ai.google.dev/gemini-api/docs/models?hl=tr), akıl yürütme ve çok adımlı planlama yeteneklerini önemli ölçüde geliştiren bir "düşünme süreci" kullanır. Bu sayede kodlama, ileri matematik ve veri analizi gibi karmaşık görevlerde oldukça etkili olurlar.

Düşünme modeli kullandığınızda Gemini, yanıt vermeden önce dahili olarak akıl yürütür. Etkileşimler API'si, bu gerekçeyi `thought` adımları aracılığıyla gösterir. Bu adımlar, `steps` dizisindeki işlev çağrıları, kullanıcı girişleri veya model çıkışlarıyla birlikte kronolojik olarak görünür.

Her düşünce adımı iki alan içerir:

| Alan | Zorunlu | Açıklama |
| --- | --- | --- |
| `signature` | ✅ Evet | Modelin dahili muhakeme durumunun şifrelenmiş temsili. Model en az muhakeme yaptığında bile her zaman mevcuttur. |
| `summary` | ❌ Hayır | Gerekçeyi özetleyen bir dizi içerik (metin ve/veya resim). [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=tr) yapılandırmasına, modelin yeterli akıl yürütme yapıp yapmadığına veya içerik türüne (ör. görüntü latents'lerinde metin özetleri olmayabilir) bağlı olarak boş olabilir. |

## Düşünceyle etkileşimler

Bir düşünce modeliyle etkileşim başlatmak, diğer etkileşim isteklerine benzer. `model` alanında [düşünme desteği olan modellerden](#thinking-levels) birini belirtin:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## Düşünce özetleri

Düşünce özetleri, modelin dahili akıl yürütme süreci hakkında bilgi verir.
Varsayılan olarak yalnızca son çıktı döndürülür. `thinking_summaries` ile düşünce özetlerini etkinleştirebilirsiniz:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

Düşünce bloğu, aşağıdaki durumlarda **yalnızca özet içermeyen bir imza** içerebilir:

- Modelin özet oluşturmak için yeterince gerekçe sunmadığı basit istekler
- `thinking_summaries: "none"`, özetlerin açıkça devre dışı bırakıldığı yerler
- Resim gibi belirli düşünce içerik türlerinde metin özetleri olmayabilir.

Kodunuz, `summary` değerinin boş veya eksik olduğu düşünce bloklarını her zaman işlemelidir.

## Düşünerek yayın yapma

Oluşturma sırasında artımlı düşünce özetleri almak için akışı kullanın.
Düşünce blokları, iki farklı delta türüyle Server-Sent Events (SSE) kullanılarak yayınlanır:

| Delta türü | Şunu içerir: | Gönderildiğinde |
| --- | --- | --- |
| `thought_summary` | Metin veya resim özet içeriği | Artımlı özet içeren bir veya daha fazla delta |
| `thought_signature` | Kriptografik imza | `step.stop` tarihinden önceki son değişiklik |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

Akış yanıtı, sunucu tarafından gönderilen etkinlikleri (SSE) kullanır ve adımlar ile etkinliklerden oluşur. Örneğin:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.5-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Düşünceleri kontrol etme

Gemini modelleri, varsayılan olarak dinamik düşünme özelliğini kullanır ve isteğin karmaşıklığına göre akıl yürütme çabasını otomatik olarak ayarlar. Bu davranışı `thinking_level` parametresini kullanarak kontrol edebilirsiniz.

| Model | Varsayılan Düşünme | Desteklenen Seviyeler |
| --- | --- | --- |
| gemini-3.1-pro-preview | Açık (yüksek) | düşük, orta, yüksek |
| gemini-3-flash-preview | Açık (yüksek) | düşük, orta, yüksek |
| gemini-3-pro-preview | Açık (yüksek) | düşük, yüksek |
| gemini-3.5-flash | Açık (orta) | düşük, orta, yüksek |
| gemini-2.5-pro | Açık | düşük, orta, yüksek |
| gemini-2.5-flash | Açık | düşük, orta, yüksek |
| gemini-2.5-flash-lite | Kapalı | düşük, orta, yüksek |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Düşünce imzaları

Düşünce imzaları, modelin dahili muhakemesinin şifrelenmiş gösterimleridir. Çok aşamalı etkileşimlerde muhakeme sürekliliğini korumaları gerekir.

Etkileşimler API'si, `generateContent` API'ye kıyasla düşünce imzalarını işlemeyi çok daha kolay hale getirir.

### Durumlu mod (önerilir)

Durumlu modda Etkileşimler API'sini kullandığınızda (`store: true` ayarlanarak ve sonraki dönüşlerde `previous_interaction_id` iletilerek) sunucu, tüm düşünce blokları ve imzalar dahil olmak üzere görüşme durumunu otomatik olarak yönetir. Bu modda imzalarla ilgili herhangi bir işlem yapmanız gerekmez. Tamamen sunucu tarafında işlenirler.

### Durumsuz mod

Sohbet durumunu kendiniz yönetiyorsanız (durum bilgisiz mod) ve her istekte giriş ve çıkışların tam geçmişini iletiyorsanız:

- Tüm `thought` bloklarını modelden alındığı şekilde **MUTLAKA** yeniden göndermelisiniz.
- Modelin akıl yürütmeye devam etmesi için gereken imzaları içerdiğinden, geçmişteki düşünce bloklarını **KALDIRMAMALI** veya değiştirmemelisiniz.
- Bir oturumda modeller arasında geçiş yaparken önceki modelin düşünce bloklarını yine de yeniden göndermeniz gerekir. Uyumluluk, arka uç tarafından yönetilir.

## Fiyatlandırma

Düşünme etkinleştirildiğinde yanıt fiyatı, çıkış jetonlarının ve düşünme jetonlarının toplamıdır. Oluşturulan düşünme jetonlarının toplam sayısını `total_thought_tokens` alanından alabilirsiniz.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

Düşünme modelleri, nihai yanıtın kalitesini artırmak için tam düşünceler üretir ve ardından düşünce süreci hakkında bilgi vermek için [özetler](#summaries) oluşturur. Fiyatlandırma, API'den yalnızca özet çıkışı yapılmasına rağmen modelin oluşturması gereken tam düşünce jetonlarına göre belirlenir.

Jetonlar hakkında daha fazla bilgiyi [Jeton sayımı](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) kılavuzunda bulabilirsiniz.

## En iyi uygulamalar

Aşağıdaki yönergeleri uygulayarak düşünce modellerini verimli bir şekilde kullanın.

- **Gerekçeyi inceleme**: Hataları anlamak ve istemleri iyileştirmek için düşünce özetlerini analiz edin.
- **Düşünme bütçesini kontrol etme**: Jeton tasarrufu için uzun çıktılarda modelin daha az düşünmesini sağlayın.
- **Basit görevler**: Bilgi alma veya sınıflandırma için düşük düşünme düzeyini kullanın (ör. "DeepMind nerede kuruldu?").
- **Denetleme görevleri**: Kavramları karşılaştırmak veya yaratıcı akıl yürütme için varsayılan düşünceyi kullanın (ör. elektrikli ve hibrit arabaları karşılaştırın).
- **Karmaşık görevler**: Gelişmiş kodlama, matematik veya çok adımlı planlama (ör. AIME matematik problemlerini çözme) için maksimum düşünme özelliğini kullanın.

## Sırada ne var?

- [Metin üretme](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr): Temel metin yanıtları
- [İşlev çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr): Araçlara bağlanma
- [Gemini 3 rehberi](https://ai.google.dev/gemini-api/docs/gemini-3?hl=tr): Modele özgü özellikler

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-24 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-24 UTC."],[],[]]
