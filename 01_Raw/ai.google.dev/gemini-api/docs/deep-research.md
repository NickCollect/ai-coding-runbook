---
source_url: https://ai.google.dev/gemini-api/docs/deep-research?hl=tr
fetched_at: 2026-07-20T04:44:56.696696+00:00
title: "Gemini Deep Research Temsilcisi \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini Deep Research Temsilcisi

Gemini Deep Research Temsilcisi, çok adımlı araştırma görevlerini bağımsız olarak planlar, yürütür ve sentezler. Gemini destekli bu araç, karmaşık bilgi ortamlarında gezinerek ayrıntılı ve alıntılı raporlar oluşturur. Yeni özellikler sayesinde, yapay zeka ajanıyla birlikte plan yapabilir, MCP sunucularını kullanarak harici araçlara bağlanabilir, görselleştirmeler (ör. grafikler) ekleyebilir ve belgeleri doğrudan giriş olarak sağlayabilirsiniz.

Araştırma görevleri, tekrara dayalı arama ve okuma işlemlerini içerir ve tamamlanması birkaç dakika sürebilir. Aracıyı eşzamansız olarak çalıştırmak ve sonuçları yoklamak ya da güncellemeleri yayınlamak için [arka planda yürütmeyi](https://ai.google.dev/gemini-api/docs/background-execution?hl=tr) (`background=true` olarak ayarlayın) kullanmanız gerekir. Daha fazla bilgi için [Uzun süren görevleri işleme](#long-running-tasks) başlıklı makaleyi inceleyin.

Aşağıdaki örnekte, arka planda araştırma görevi başlatma ve sonuçları yoklama işlemi gösterilmektedir.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Desteklenen sürümler

Deep Research aracısı iki sürümde sunulur:

- **Deep Research** (`deep-research-preview-04-2026`): Hız ve verimlilik için tasarlanmıştır. İstemci kullanıcı arayüzüne geri aktarılmak için idealdir.
- **Deep Research Max** (`deep-research-max-preview-04-2026`): Otomatik bağlam toplama ve sentezleme için maksimum kapsamlılık.

## Ortak planlama

Ortak planlama, araştırmayı yürütmeden önce araştırma planını inceleyip iyileştirmenize olanak tanıyarak temsilci çalışmaya başlamadan önce araştırma yönünü kontrol etmenizi sağlar. Etkinleştirildiğinde, ajan hemen yürütmek yerine önerilen bir araştırma planı döndürür. Ardından, çok turlu etkileşimler aracılığıyla planı inceleyebilir, değiştirebilir veya onaylayabilirsiniz.

### 1. adım: Plan isteğinde bulunun

İlk etkileşimde `collaborative_planning=True` değerini ayarlayın. Ajan, tam rapor yerine araştırma planı döndürüyor.

### Python

```
from google import genai

client = genai.Client()

# First interaction: request a research plan
plan_interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Do some research on Google TPUs.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    background=True,
)

# Wait for and retrieve the plan
while (result := client.interactions.get(id=plan_interaction.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const planInteraction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Do some research on Google TPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    background: true
});

let result;
while ((result = await client.interactions.get(planInteraction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Do some research on Google TPUs.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "background": true
}'
```

### 2. adım: Planı iyileştirin (isteğe bağlı)

Sohbete devam etmek ve planı yinelemek için `previous_interaction_id` aboneliğini kullanın. Planlama modunda kalmak için `collaborative_planning=True` tuşunu basılı tutun.

### Python

```
# Second interaction: refine the plan
refined_plan = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    previous_interaction_id=plan_interaction.id,
    background=True,
)

while (result := client.interactions.get(id=refined_plan.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const refinedPlan = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Focus more on the differences between Google TPUs and competitor hardware, and less on the history.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    previous_interaction_id: planInteraction.id,
    background: true
});

let result;
while ((result = await client.interactions.get(refinedPlan.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

### 3. adım: Onaylayın ve yürütün

Planı onaylamak ve araştırmayı başlatmak için `collaborative_planning=False` değerini ayarlayın (veya bu değeri atlayın).

### Python

```
# Third interaction: approve the plan and kick off research
final_report = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Plan looks good!",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": False,
    },
    previous_interaction_id=refined_plan.id,
    background=True,
)

while (result := client.interactions.get(id=final_report.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const finalReport = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Plan looks good!',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: false
    },
    previous_interaction_id: refinedPlan.id,
    background: true
});

let result;
while ((result = await client.interactions.get(finalReport.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Plan looks good!",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": false
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

## Görselleştirme

`visualization`, `"auto"` olarak ayarlandığında ajan, araştırma bulgularını desteklemek için grafikler ve diğer görsel öğeler oluşturabilir.
Oluşturulan resimler, yanıt adımlarına dahil edilir ve `image` deltalara dönüştürülerek yayınlanır. En iyi sonuçları elde etmek için sorgunuzda görselleri açıkça isteyin. Örneğin, "Zaman içindeki trendleri gösteren grafikler ekle" veya "Pazar payını karşılaştıran grafikler oluştur" gibi ifadeler kullanın. `visualization` değerini `"auto"` olarak ayarlamak özelliği etkinleştirir ancak ajan, yalnızca istemde istenirse görsel oluşturur.

### Python

```
import base64
import time

from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Analyze global semiconductor market trends. Include graphics showing market share changes.",
    agent_config={
        "type": "deep-research",
        "visualization": "auto",
    },
    background=True,
)

print(f"Research started: {interaction.id}")

while (result := client.interactions.get(id=interaction.id)).status != "completed":
    time.sleep(5)

for step in result.steps:
    if step.type == "model_output":
        for content_item in step.content:
            if content_item.type == "text":
                print(content_item.text)
            elif content_item.type == "image" and content_item.data:
                image_bytes = base64.b64decode(content_item.data)
                print(f"Received image: {len(image_bytes)} bytes")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Analyze global semiconductor market trends. Include graphics showing market share changes.',
    agent_config: {
        type: 'deep-research',
        visualization: 'auto'
    },
    background: true
});

console.log(`Research started: ${interaction.id}`);

let result;
while ((result = await client.interactions.get(interaction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}

for (const step of result.steps) {
    if (step.type === 'model_output') {
        for (const contentItem of step.content) {
            if (contentItem.type === 'text') {
                console.log(contentItem.text);
            } else if (contentItem.type === 'image' && contentItem.data) {
                console.log(`[Image Output: ${contentItem.data.substring(0, 20)}...]`);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Analyze global semiconductor market trends. Include graphics showing market share changes.",
    "agent_config": {
        "type": "deep-research",
        "visualization": "auto"
    },
    "background": true
}'
```

## Desteklenen araçlar

Deep Research, birden fazla yerleşik ve harici aracı destekler. Varsayılan olarak (`tools` parametresi sağlanmadığında) aracı, Google Arama, URL Bağlamı ve Kod Yürütme'ye erişebilir. Ajanın yeteneklerini kısıtlamak veya genişletmek için araçları açıkça belirtebilirsiniz.

| Araç | Tür değeri | Açıklama |
| --- | --- | --- |
| Google Arama | `google_search` | Herkese açık web'de arama yapın. Varsayılan olarak etkindir. |
| URL Bağlamı | `url_context` | Web sayfası içeriğini okuma ve özetleme Varsayılan olarak etkindir. |
| Kod Yürütme | `code_execution` | Hesaplamalar ve veri analizi yapmak için kodu yürütün. Varsayılan olarak etkindir. |
| MCP Sunucusu | `mcp_server` | Harici araç erişimi için uzaktaki MCP sunucularına bağlanın. |
| Dosya Arama | `file_search` | Yüklediğiniz doküman derlemlerinde arama yapın. |

### Google Arama

Google Arama'yı tek araç olarak açıkça etkinleştirin:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "google_search"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'What are the latest developments in quantum computing?',
    tools: [{ type: 'google_search' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "What are the latest developments in quantum computing?",
    "tools": [{"type": "google_search"}],
    "background": true
}'
```

### URL Bağlamı

Ajana belirli web sayfalarını okuma ve özetleme yetkisi verin:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Summarize the content of https://www.wikipedia.org/.",
    tools=[{"type": "url_context"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Summarize the content of https://www.wikipedia.org/.',
    tools: [{ type: 'url_context' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Summarize the content of https://www.wikipedia.org/.",
    "tools": [{"type": "url_context"}],
    "background": true
}'
```

### Kod Yürütme

Ajanın hesaplamalar ve veri analizi için kod yürütmesine izin verin:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Calculate the 50th Fibonacci number.",
    "agent": "deep-research-preview-04-2026",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### MCP sunucuları

Ajanın harici araçlara ve hizmetlere erişmesini sağlamak için uzak MCP sunucularına bağlanın.

Araç yapılandırmasında sunucuyu `name` ve `url` olarak belirtin. Ayrıca, kimlik doğrulama kimlik bilgilerini iletebilir ve aracının hangi araçları çağırabileceğini kısıtlayabilirsiniz.

| Alan | Tür | Zorunlu | Açıklama |
| --- | --- | --- | --- |
| `type` | `string` | Evet | `"mcp_server"` olmalıdır. |
| `name` | `string` | Hayır | MCP sunucusunun görünen adı. |
| `url` | `string` | Hayır | MCP sunucusu uç noktasının tam URL'si. |
| `headers` | `object` | Hayır | Sunucuya yapılan her istekle birlikte HTTP başlıkları olarak gönderilen anahtar/değer çiftleri (örneğin, kimlik doğrulama jetonları). |
| `allowed_tools` | `array` | Hayır | Ajanın sunucudan hangi araçları çağırabileceğini kısıtlayın. |

#### Temel kullanım

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ],
    "background": true
}'
```

### Dosya Arama

[Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr) aracını kullanarak aracıya kendi verilerinize erişim izni verin.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Compare our 2025 fiscal year report against current public web news.",
    agent="deep-research-preview-04-2026",
    background=True,
    tools=[
        {
            "type": "file_search",
            "file_search_store_names": ['fileSearchStores/my-store-name']
        }
    ]
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Compare our 2025 fiscal year report against current public web news.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    tools: [
        { type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] },
    ]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Compare our 2025 fiscal year report against current public web news.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "tools": [
        {"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]},
    ]
}'
```

## Yönlendirilebilirlik ve biçimlendirme

İsteminizde belirli biçimlendirme talimatları vererek aracının çıktısını yönlendirebilirsiniz. Bu sayede raporları belirli bölümler ve alt bölümler halinde yapılandırabilir, veri tabloları ekleyebilir veya farklı kitlelere yönelik üslubu ayarlayabilirsiniz (ör. "teknik", "yönetici", "gündelik").

İstenen çıkış biçimini giriş metninizde açıkça tanımlayın.

### Python

```
prompt = """
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
"""

interaction = client.interactions.create(
    input=prompt,
    agent="deep-research-preview-04-2026",
    background=True
)
```

### JavaScript

```
const prompt = `
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
`;

const interaction = await client.interactions.create({
    input: prompt,
    agent: 'deep-research-preview-04-2026',
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of EV batteries.\n\nFormat the output as a technical report with the following structure: \n1. Executive Summary\n2. Key Players (Must include a data table comparing capacity and chemistry)\n3. Supply Chain Risks",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'
```

## Çok formatlı girişler

Derin Araştırma, resimler ve dokümanlar (PDF'ler) dahil olmak üzere çok formatlı girişleri destekler. Böylece, aracının görsel içerikleri analiz etmesine ve sağlanan girişlerle bağlamsallaştırılmış web tabanlı araştırmalar yapmasına olanak tanır.

### Python

```
import time
from google import genai

client = genai.Client()

prompt = """Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground."""

interaction = client.interactions.create(
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"
        }
    ],
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const prompt = `Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground.`;

const interaction = await client.interactions.create({
    input: [
        { type: 'text', text: prompt },
        {
            type: 'image',
            mime_type: "image/jpeg",
            uri: 'https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg'
        }
    ],
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task with image input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": [
        {"type": "text", "text": "Analyze the interspecies dynamics and behavioral risks present in the provided image of the African watering hole. Specifically, investigate the symbiotic relationship between the avian species and the pachyderms shown, and conduct a risk assessment for the reticulated giraffes based on their drinking posture relative to the specific predator visible in the foreground."},
        {"type": "image", "mime_type": "image/jpeg", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Belge anlama

Doküman yorumlama, dokümanların doğrudan çok formatlı giriş olarak iletilmesine olanak tanır.
Aracı, sağlanan belgeleri analiz eder ve içeriklerine dayalı araştırma yapar.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "https://arxiv.org/pdf/1706.03762",
            "mime_type": "application/pdf",
        },
    ],
    background=True,
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'https://arxiv.org/pdf/1706.03762',
            mime_type: 'application/pdf'
        }
    ],
    background: true
});
```

### REST

```
# 1. Start the research task with document input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {"type": "document", "uri": "https://arxiv.org/pdf/1706.03762", "mime_type": "application/pdf"}
    ],
    "background": true
}'
```

## Uzun süreli görevleri işleme

Deep Research; planlama, arama, okuma ve yazma gibi çok adımlı bir süreçtir. Bu döngü genellikle senkron API çağrılarının standart zaman aşımı sınırlarını aşar.

Temsilcilerin `background=True` kullanması gerekir. API, hemen kısmi bir `Interaction` nesnesi döndürür. Anket için etkileşim almak üzere `id` özelliğini kullanabilirsiniz. Etkileşim durumu `in_progress`'dan `completed` veya `failed`'ye geçiş yapar. Arka plan görevlerini yönetmeyle ilgili kapsamlı bir kılavuz için [Arka planda yürütme](https://ai.google.dev/gemini-api/docs/background-execution?hl=tr) başlıklı makaleyi inceleyin.

### Canlı Yayın

Deep Research, düşünce özetleri, metin çıktısı ve oluşturulan resimler dahil olmak üzere araştırma ilerlemesiyle ilgili anlık güncellemeler almak için akışı destekler.
`stream=True` ve `background=True` öğelerini ayarlamanız gerekir.

Ara muhakeme adımlarını (düşünceler) ve ilerleme durumu güncellemelerini almak için `agent_config` bölümünde `thinking_summaries` ayarını `"auto"` olarak belirleyerek **düşünce özetlerini** etkinleştirmeniz gerekir. Bu olmadan yayın yalnızca nihai sonuçları sağlayabilir.

#### Akış etkinliği türleri

| Etkinlik türü | Delta türü | Açıklama |
| --- | --- | --- |
| `step.delta` | `thought` | Aracının akıl yürütme sürecindeki ara adım. |
| `step.delta` | `text` | Nihai metin çıktısının bir parçası. |
| `step.delta` | `image` | Üretilmiş bir resim (base64 kodlu). |

Aşağıdaki örnekte bir araştırma görevi başlatılıyor ve otomatik yeniden bağlantı ile yayın işleniyor. Bağlantı kesilirse (örneğin, 600 saniyelik zaman aşımından sonra) kaldığı yerden devam edebilmesi için `interaction_id` ve `last_event_id` değerlerini izler.

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for event in stream:
        if event.event_type == "interaction.created":
            interaction_id = event.interaction.id
        if event.event_id:
            last_event_id = event.event_id
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
            elif event.delta.type == "thought":
                print(f"Thought: {event.delta.text}", flush=True)
        elif event.event_type in ("interaction.completed", "interaction.error"):
            is_complete = True

stream = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
    stream=True,
    agent_config={"type": "deep-research", "thinking_summaries": "auto"},
)
process_stream(stream)

# Reconnect if the connection drops
while not is_complete and interaction_id:
    status = client.interactions.get(interaction_id)
    if status.status != "in_progress":
        break
    stream = client.interactions.get(
        id=interaction_id, stream=True, last_event_id=last_event_id,
    )
    process_stream(stream)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interactionId;
let lastEventId;
let isComplete = false;

async function processStream(stream) {
    for await (const event of stream) {
        if (event.type === 'interaction.created') {
            interactionId = event.interaction.id;
        }
        if (event.event_id) lastEventId = event.event_id;
        if (event.type === 'step.delta') {
            if (event.delta.type === 'text') {
                process.stdout.write(event.delta.text);
            } else if (event.delta.type === 'thought') {
                console.log(`Thought: ${event.delta.text}`);
            }
        } else if (['interaction.completed', 'interaction.error'].includes(event.type)) {
            isComplete = true;
        }
    }
}

const stream = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    stream: true,
    agent_config: { type: 'deep-research', thinking_summaries: 'auto' },
});
await processStream(stream);

// Reconnect if the connection drops
while (!isComplete && interactionId) {
    const status = await client.interactions.get(interactionId);
    if (status.status !== 'in_progress') break;
    const resumeStream = await client.interactions.get(interactionId, {
        stream: true, last_event_id: lastEventId,
    });
    await processStream(resumeStream);
}
```

### REST

```
# 1. Start the stream (save the INTERACTION_ID from the interaction.start event
#    and the last "event_id" you receive)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "stream": true,
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
}'

# 2. If the connection drops, reconnect with your saved IDs
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID?stream=true&last_event_id=LAST_EVENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Ek sorular ve etkileşimler

Temsilci nihai raporu döndürdükten sonra `previous_interaction_id` kullanarak görüşmeye devam edebilirsiniz. Bu sayede, görevin tamamını yeniden başlatmadan araştırmanın belirli bölümleriyle ilgili açıklama, özet veya ayrıntı isteyebilirsiniz.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Can you elaborate on the second point in the report?",
    model="gemini-3.1-pro-preview",
    previous_interaction_id="COMPLETED_INTERACTION_ID"
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-3.1-pro-preview',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Can you elaborate on the second point in the report?",
    "model": "gemini-3.1-pro-preview",
    "previous_interaction_id": "COMPLETED_INTERACTION_ID"
}'
```

## Gemini Deep Research Ajanı'nı ne zaman kullanmalısınız?

Deep Research yalnızca bir model değil, **ajandır**. Düşük gecikmeli sohbet yerine "analist-in-a-box" yaklaşımı gerektiren iş yükleri için en uygun seçenektir.

| Özellik | Standart Gemini Modelleri | Gemini Deep Research Ajanı |
| --- | --- | --- |
| **Gecikme** | Saniye | Dakika (Eşzamansız/Arka Plan) |
| **İşlem** | Oluştur -> Çıkış | Plan -> Search -> Read -> Iterate -> Output |
| **Çıkış** | Etkileşimli metin, kod, kısa özetler | Ayrıntılı raporlar, uzun analizler, karşılaştırmalı tablolar |
| **İdeal kullanım alanları** | Chatbot'lar, ayıklama, yaratıcı yazarlık | Pazar analizi, durum tespiti, literatür taramaları, rekabet ortamı |

## Aracı yapılandırması

Deep Research, davranışı kontrol etmek için `agent_config` parametresini kullanır.
Aşağıdaki alanları içeren bir sözlük olarak iletin:

| Alan | Tür | Varsayılan | Açıklama |
| --- | --- | --- | --- |
| `type` | `string` | Zorunlu | `"deep-research"` olmalıdır. |
| `thinking_summaries` | `string` | `"none"` | Yayın sırasında ara muhakeme adımlarını almak için `"auto"` olarak ayarlayın. Devre dışı bırakmak için `"none"` olarak ayarlayın. |
| `visualization` | `string` | `"auto"` | Ajan tarafından oluşturulan grafik ve resimleri etkinleştirmek için `"auto"` olarak ayarlayın. Devre dışı bırakmak için `"off"` olarak ayarlayın. |
| `collaborative_planning` | `boolean` | `false` | Araştırma başlamadan önce çok turlu plan incelemesini etkinleştirmek için `true` olarak ayarlayın. |

### Python

```
agent_config = {
    "type": "deep-research",
    "thinking_summaries": "auto",
    "visualization": "auto",
    "collaborative_planning": False,
}

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the competitive landscape of cloud GPUs.",
    agent_config=agent_config,
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Research the competitive landscape of cloud GPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        visualization: 'auto',
        collaborative_planning: false,
    },
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of cloud GPUs.",
    "agent": "deep-research-preview-04-2026",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "visualization": "auto",
        "collaborative_planning": false
    },
    "background": true
}'
```

## Kullanılabilirlik ve fiyatlandırma

Google AI Studio'daki Interactions API ve Gemini API'yi kullanarak Gemini Deep Research Agent'a erişebilirsiniz.

Fiyatlandırma, temel Gemini modellerine ve aracının kullandığı belirli araçlara dayalı [kullandıkça öde modeline](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#pricing-for-agents) göre belirlenir. Bir isteğin tek bir çıkışa yol açtığı standart sohbet isteklerinin aksine, Deep Research görevi, bir aracı iş akışıdır. Tek bir istek, planlama, arama, okuma ve akıl yürütme işlemlerinden oluşan bağımsız bir döngüyü tetikler.

### Tahmini maliyetler

Maliyetler, gereken araştırma derinliğine göre değişir. Ajan, isteminize yanıt vermek için ne kadar okuma ve arama yapılması gerektiğini bağımsız olarak belirler.

- **Deep Research** (`deep-research-preview-04-2026`): Orta düzeyde analiz gerektiren tipik bir sorgu için ajan yaklaşık 80 arama sorgusu, yaklaşık 250 bin giriş jetonu (yaklaşık% 50-70 önbelleğe alınmış) ve yaklaşık 60 bin çıkış jetonu kullanabilir.
  - **Tahmini toplam:** Görev başına ~1,00 TL - 3,00 TL
- **Deep Research Max** (`deep-research-max-preview-04-2026`): Derinlemesine rekabet ortamı analizi veya kapsamlı durum tespiti için ajan, ~160 arama sorgusu, ~900 bin giriş jetonu (~% 50-70 önbelleğe alınmış) ve ~80 bin çıkış jetonu kullanabilir.
  - **Tahmini toplam:** Görev başına ~3,00 TL - 7,00 TL

## Güvenlikle ilgili olarak göz önünde bulundurulması gerekenler

Bir aracıya web'e ve özel dosyalarınıza erişim izni vermek için güvenlik risklerini dikkatlice değerlendirmeniz gerekir.

- **Dosyaları kullanarak istem ekleme:** Aracı, sağladığınız dosyaların içeriğini okur. Yüklenen dokümanların (PDF'ler, metin dosyaları) güvenilir kaynaklardan geldiğinden emin olun. Kötü amaçlı bir dosya, aracının çıkışını manipüle etmek için tasarlanmış gizli metinler içerebilir.
- **Web içeriği riskleri:** Aracı, herkese açık web'de arama yapar. Güçlü güvenlik filtreleri uyguladığımız halde, aracının kötü amaçlı web sayfalarıyla karşılaşma ve bunları işleme riski vardır. Kaynakları doğrulamak için yanıtta `citations` bilgilerini incelemenizi öneririz.
- **Veri sızdırma:** Agent'ın web'e göz atmasına da izin veriyorsanız hassas dahili verileri özetlemesini isterken dikkatli olun.

## En iyi uygulamalar

- **Bilinmeyenler için istem:** Eksik verilerin nasıl işleneceği konusunda temsilciye talimat verin.
  Örneğin, isteminize *"2025'e ait belirli rakamlar mevcut değilse tahmin etmek yerine bunların tahmin olduğunu veya kullanılamadığını açıkça belirt"* ifadesini ekleyin.
- **Bağlam sağlama:** Giriş isteminde doğrudan arka plan bilgileri veya kısıtlamalar sağlayarak aracının araştırmasına temel oluşturun.
- **Ortak planlamayı kullanın:** Karmaşık sorgular için, yürütmeden önce araştırma planını incelemek ve iyileştirmek üzere ortak planlamayı etkinleştirin.
- **Çok formatlı girişler:** Deep Research Agent, çok formatlı girişleri destekler.
  Maliyetleri artırdığı ve bağlam penceresinin taşmasına neden olabileceği için dikkatli kullanın.

## Sınırlamalar

- **Özel araçlar:** Şu anda özel işlev çağrısı araçları sağlayamıyorsunuz ancak Derin Araştırma aracısıyla uzak MCP (Model Context Protocol) sunucularını kullanabilirsiniz.
- **Yapılandırılmış çıkış:** Derin Araştırma Aracısı şu anda yapılandırılmış çıkışları desteklememektedir.
- **Maksimum araştırma süresi:** Deep Research aracısının maksimum araştırma süresi 60 dakikadır. Çoğu görev 20 dakika içinde tamamlanır.
- **Mağaza koşulu:** `background=True` kullanılarak yapılan aracı yürütme işlemi için `store=True` gerekir.
- **Google Arama:** [Google Arama](https://ai.google.dev/gemini-api/docs/google-search?hl=tr) varsayılan olarak etkindir ve temellendirilmiş sonuçlar için [belirli kısıtlamalar](https://ai.google.dev/gemini-api/terms?hl=tr#use-restrictions2) geçerlidir.

## Sırada ne var?

- [Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) hakkında daha fazla bilgi edinin.
- [Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr) aracını kullanarak kendi verilerinizi nasıl kullanacağınızı öğrenin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-14 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-14 UTC."],[],[]]
