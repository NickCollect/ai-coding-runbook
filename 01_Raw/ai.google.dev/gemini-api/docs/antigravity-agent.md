---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr
fetched_at: 2026-08-24T02:26:11.804507+00:00
title: "Antigravity ajan\u0131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Antigravity ajanı

Antigravity ajanı, Gemini API'de genel amaçlı bir yönetilen ajandır. Tek bir API çağrısı, Google tarafından barındırılan kendi güvenli Linux sanal alanınızda akıl yürüten, kod yürüten, dosyaları yöneten ve web'de gezinmenizi sağlayan bir aracı sunar.

Gemini 3.7 Flash tarafından desteklenir ve Antigravity IDE ile aynı koşum takımını kullanır. Temel Gemini modelini `agent_config` kullanarak yapılandırabilirsiniz. [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) ve [Google AI Studio](https://aistudio.google.com?hl=tr) üzerinden kullanılabilir.

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

## Özellikler

Her çağrı, bir Linux sanal alanı sağlayabilir ve araç kullanma döngüsü başlatabilir. Ajan; plan yapar, harekete geçer, sonuçları gözlemler ve görev tamamlanana kadar tekrarlar.

- **Kod yürütme:** Bash, Python ve Node.js komutlarını çalıştırın. Paketleri yükleyin, testleri çalıştırın ve uygulamalar oluşturun.
- **Dosya yönetimi:** Sandbox'taki dosyaları okuma, yazma, düzenleme, arama ve listeleme. Dosyalar, etkileşimler arasında korunur.
- **Web erişimi:** Veriler için Google Arama ve URL getirme.
- **Bağlam sıkıştırma:** Bağlamı kaybetmeden veya parça sınırlarına ulaşmadan uzun süren, çok aşamalı etkileşim oturumlarını desteklemek için otomatik bağlam sıkıştırma (~135.000 parçada tetiklenir).

Çok aşamalı etkileşim kullanımı ve yayın için [Hızlı Başlangıç](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr) bölümüne bakın.

## Desteklenen araçlar

Varsayılan olarak, ajan `code_execution`, `google_search` ve `url_context` uygulamalarına erişebilir. `environment` parametresini belirttiğinizde dosya sistemi araçları otomatik olarak etkinleştirilir. Ayrıca, aracıyı kendi API'lerinize ve araçlarınıza bağlamak için **özel işlevler** de tanımlayabilirsiniz. Varsayılan grubu özelleştirirken veya kısıtlarken ya da özel işlevler eklerken yalnızca `tools` parametresini belirtmeniz gerekir.

| Araç | Tür değeri | Açıklama |
| --- | --- | --- |
| Kod Yürütme | `code_execution` | stdout/stderr yakalama ile kabuk komutlarını (bash, Python, Node) çalıştırın. |
| Google Arama | `google_search` | Herkese açık web'de arama yapın. |
| URL Bağlamı | `url_context` | Web sayfalarını getirme ve okuma |
| Dosya sistemi | *(`environment` üzerinden etkinleştirilir)* | Sandbox'ta dosyaları okuma, yazma, düzenleme, arama ve listeleme Sistemi `environment` olarak ayarladığınızda bu araçlar otomatik olarak etkinleştirilir. |
| Özel İşlevler | `function` | Ajanın yürütülmesini isteyebileceği özel işlevler tanımlayın. [İşlev çağırma](#function-calling) başlıklı makaleyi inceleyin. |
| Uzak MCP sunucusu | `mcp_server` | Harici Model Bağlam Protokolü (MCP) sunucularını araç olarak kaydedin. [MCP sunucuları](#mcp-servers) başlıklı makaleyi inceleyin. |

Senkron [kancalar](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=tr) kullanarak `code_execution` ve `filesystem` araç yürütmesini doğrudan uzak korumalı alanda yakalayabilir ve doğrulayabilirsiniz.

Aracıyı belirli araçlarla sınırlamak için yalnızca ihtiyacınız olanları iletin:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
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
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## Çok formatlı giriş

Antigravity aracısı, çok formatlı girişleri destekler. Şu anda yalnızca `text` ve `image` girişleri desteklenmektedir. Resimler, satır içi Base64 kodlu dizeler (`data`) olarak sağlanmalıdır.

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### REST

```
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## İşlev çağırma

İşlev çağırma, aracının çağırabileceği özel araçlar tanımlayarak Antigravity aracısını harici API'lere ve veritabanlarına bağlamanıza olanak tanır. Genel kavramlar için [Gemini API ile işlev çağrısı](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=tr) başlıklı makaleyi inceleyin.

Aşağıdaki örnekte 2 dönüşlü bir etkileşim gösterilmektedir. Ajan önce özel bir `get_weather` işlev çağrısı ister, istemci bunu yürütür ve sonucu ikinci turda döndürür.

### Python

```
from google import genai

client = genai.Client()

# 1. Define the custom function
get_weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and country, e.g. San Francisco, USA",
            }
        },
        "required": ["location"],
    },
}

# 2. Call the agent with the custom tool (Turn 1)
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[
        {"type": "code_execution"},  # Enable default code execution
        get_weather_tool,            # Add custom function
    ],
)

# Check if the agent requested a function call
if interaction.status == "requires_action":
    # Find function calls that do not have a matching function result.
    # Filesystem tools (like write_file) are also represented as function calls
    # but are executed automatically by the environment.
    executed_calls = {step.call_id for step in interaction.steps if step.type == "function_result"}
    pending_calls = [step for step in interaction.steps if step.type == "function_call" and step.id not in executed_calls]

    if pending_calls:
        fc_step = pending_calls[0]
        print(f"Function to call: {fc_step.name} (ID: {fc_step.id})")
        print(f"Arguments: {fc_step.arguments}")

        # 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
        function_result = {
            "temperature": 23,
            "unit": "celsius"
        }

        final_interaction = client.interactions.create(
            agent="antigravity-preview-05-2026",
            previous_interaction_id=interaction.id,  # Reference the interaction ID
            environment=interaction.environment_id,
            input=[
                {
                    "type": "function_result",
                    "name": fc_step.name,
                    "call_id": fc_step.id,
                    "result": function_result,
                }
            ],
        )

        print(final_interaction.output_text)
        # Output: The current weather in Tokyo, Japan is 23°C (Celsius).
    else:
        print("No pending function calls.")
else:
    print(f"Interaction completed with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// 1. Define the custom function
const get_weather_tool = {
  type: "function",
  name: "get_weather",
  description: "Gets the current weather for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city and country, e.g. San Francisco, USA",
      },
    },
    required: ["location"],
  },
};

// 2. Call the agent with the custom tool (Turn 1)
const interaction = await client.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "What is the weather in Tokyo?",
  environment: "remote",
  tools: [
    { type: "code_execution" },
    get_weather_tool,
  ],
}, { timeout: 300000 });

if (interaction.status === "requires_action") {
  // Find function calls that do not have a matching function result.
  // Filesystem tools (like write_file) are also represented as function calls
  // but are executed automatically by the environment.
  const executedCalls = new Set(
    interaction.steps
      .filter(s => s.type === "function_result")
      .map(s => s.call_id)
  );
  const pendingCalls = interaction.steps.filter(
    s => s.type === "function_call" && !executedCalls.has(s.id)
  );

  if (pendingCalls.length > 0) {
    const fcStep = pendingCalls[0];
    console.log(`Function to call: ${fcStep.name} (ID: ${fcStep.id})`);

    // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
    const functionResult = {
      temperature: 23,
      unit: "celsius"
    };

    const finalInteraction = await client.interactions.create({
      agent: "antigravity-preview-05-2026",
      previous_interaction_id: interaction.id, // Reference the interaction ID
      environment: interaction.environment_id,
      input: [
        {
          type: "function_result",
          name: fcStep.name,
          call_id: fcStep.id,
          result: functionResult,
        }
      ],
    }, { timeout: 300000 });

    console.log(finalInteraction.output_text);
  } else {
    console.log("No pending function calls.");
  }
} else {
  console.log(`Interaction completed with status: ${interaction.status}`);
}
```

### REST

```
# 1. Turn 1: Request function call
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [
          {"type": "code_execution"},
          {
              "type": "function",
              "name": "get_weather",
              "description": "Gets the current weather for a given location.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {"type": "string"}
                  },
                  "required": ["location"]
              }
          }
      ]
  }')

# Extract interaction ID, environment ID, and call ID (requires jq)
INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')
ENVIRONMENT_ID=$(echo $RESPONSE | jq -r '.environment_id')
CALL_ID=$(echo $RESPONSE | jq -r '.steps[] | select(.type=="function_call") | .id')

# 2. Turn 2: Send function result back using variables
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"input\": [
          {
              \"type\": \"function_result\",
              \"name\": \"get_weather\",
              \"call_id\": \"$CALL_ID\",
              \"result\": {
                  \"temperature\": 23,
                  \"unit\": \"celsius\"
              }
          }
      ]
  }"
```

## MCP sunucuları

Uzak Model Bağlam Protokolü (MCP) sunucularını kaydederek Antigravity ajanı harici araçlara bağlayabilirsiniz. Aracı, akışa uygun HTTP üzerinden uzak MCP sunucularını destekler.

Bir MCP sunucusu kaydederken `tools` dizisinde aşağıdaki alanları belirtmeniz gerekir:

| Alan | Tür | Zorunlu | Açıklama |
| --- | --- | --- | --- |
| `type` | dize | Evet | `"mcp_server"` olmalıdır. |
| `name` | dize | Evet | Sunucunun benzersiz tanımlayıcısı. Kesinlikle küçük harf ve alfanümerik olmalıdır (`^[a-z0-9_-]+$` ile eşleşmelidir). |
| `url` | dize | Evet | Uzak MCP sunucusunun uç nokta URL'si. |
| `headers` | nesne | Hayır | İsteklerle gönderilen özel üstbilgiler (ör. kimlik doğrulama). |
| `allowed_tools` | dizi | Hayır | Çalıştırılmasına izin verilen araç adlarının listesi. Atlanırsa tüm araçlara izin verilir. |

### Python

```
from google import genai

client = genai.Client()

# Register a remote HTTP MCP server
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "weather", # Must be lowercase
        "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "What is the weather in Tokyo?",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "weather", // Must be lowercase
        url: "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
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
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [{
          "type": "mcp_server",
          "name": "weather",
          "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
      }]
  }'
```

## Model seçimi

`antigravity-preview-05-2026` için varsayılan model **Gemini 3.7 Flash**'tır (`gemini-3.7-flash`). `agent_config` öğesini atlarsanız temsilci varsayılan olarak `gemini-3.7-flash` modelini kullanır.

Hızı, maliyeti veya muhakeme yeteneğini optimize etmek için `agent_config` kullanarak temel Gemini modelini yapılandırabilirsiniz.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Summarize the key differences between functional and object-oriented programming.",
    environment="remote",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.5-flash-lite",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Summarize the key differences between functional and object-oriented programming.",
    environment: "remote",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.5-flash-lite",
    },
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
      "input": "Summarize the key differences between functional and object-oriented programming.",
      "environment": "remote",
      "agent_config": {
          "type": "antigravity",
          "model": "gemini-3.5-flash-lite"
      }
  }'
```

`agent_config.model` için desteklenen değerler şunlardır:

| Model | `agent_config.model` cinsinden değer | Açıklama |
| --- | --- | --- |
| **Gemini 3.7 Flash** (varsayılan) | `gemini-3.7-flash` | Akıl yürütme, kodlama ve araç kullanımı için varsayılan dengeli model. |
| **Gemini 3.6 Flash** | `gemini-3.6-flash` | Genel temsilci tabanlı iş akışları için önceki nesil Flash modeli. |
| **Gemini 3.5 Flash** | `gemini-3.5-flash` | Genel iş akışları için hafif model. |
| **Gemini 3.5 Flash-Lite** | `gemini-3.5-flash-lite` | Düşük gecikme ve maliyete duyarlı görevler için optimize edilmiş hafif model. |

`agents.create` ile yönetilen bir aracı oluştururken `base_agent` ve `agent_config` parametrelerini ileterek modeli tam olarak aynı şekilde yapılandırırsınız. `agents.create` ile oluşturulan yönetilen bir aracı için etkileşim sırasında modeli geçersiz kılamayacağınızı unutmayın. Model, aracı oluşturulurken ayarlananlara göre kilitlenir. Bu sayede, araç çağırma davranışının tahmin edilebilir olması, tutarlı hata ayıklama ve güvenlik sınırlarına uyulması sağlanır.

## Aracıyı özelleştirme

Antigravity aracısını talimatlarını, araçlarını ve ortamını özelleştirerek genişletebilirsiniz. Aracı, özelleştirme için dosya sistemiyle uyumlu bir yaklaşımı destekler: Talimatlar ve beceriler için `AGENTS.md` gibi dosyaları doğrudan korumalı alana `.agents/skills/` altında bağlayabilir veya yapılandırmayı etkileşim sırasında satır içi olarak iletebilirsiniz. Yapılandırmanızı satır içi olarak yineleyebilir ve hazır olduğunuzda yönetilen ajan olarak kaydedebilirsiniz.

Özel ajanları oluşturma hakkında ayrıntılı bilgi için [Yönetilen Ajanlar Oluşturma](https://ai.google.dev/gemini-api/docs/custom-agents?hl=tr) başlıklı makaleyi inceleyin.

## Arka planda yürütme

Çok adımlı akıl yürütme, kod yürütme veya dosya işlemleri içeren aracı görevlerinin tamamlanması birkaç dakika sürebilir. Etkileşimi eşzamansız olarak çalıştırmak için `background=True` öğesini kullanın. API, durum `completed` veya `failed` olana kadar yokladığınız bir etkileşim kimliğiyle hemen yanıt verir.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Start the interaction in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run a complex analysis on the repository.",
    environment="remote",
    background=True,
)

print(f"Interaction started in background: {interaction.id}")

# 2. Poll for completion
while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run a complex analysis on the repository.",
    environment: "remote",
    background: true,
});

console.log(`Interaction started in background: ${interaction.id}`);

let result = interaction;
while (result.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    result = await client.interactions.get(interaction.id);
}

if (result.status === "completed") {
    console.log(result.output_text);
} else {
    console.log(`Finished with status: ${result.status}`);
}
```

### REST

```
# 1. Start the interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Run a complex analysis on the repository.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll for results (repeat until status is "completed")
curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

Arka planda yürütme için varsayılan olarak `store=True` gerekir. Arka planda yürütme sırasında gerçek zamanlı ilerleme güncellemeleri için [Arka planda etkileşimleri yayınlama](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=tr#streaming-background) başlıklı makaleyi inceleyin.

`cancel` yöntemini kullanarak devam eden bir arka plan etkileşimini iptal edebilirsiniz.

### Python

```
client.interactions.cancel(id="INTERACTION_ID")
```

### JavaScript

```
await client.interactions.cancel("INTERACTION_ID");
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID:cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

**Arka planda yürütme ile çok aşamalı etkileşim**

Arka plandaki bir etkileşim durum bilgisi olan araçları (ör. bir sandbox'ta kod yürütme) içerdiğinde, aynı ortamda devam etmek için tamamlanan etkileşimdeki `environment_id` simgesini kullanın. Bu sayede, temsilci tüm dosyalar ve durum korunarak kaldığı yerden devam eder.

### Python

```
import time
from google import genai

client = genai.Client()

# First turn: run a task in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Clone https://github.com/google/generative-ai-python and run its tests.",
    environment="remote",
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Second turn: continue in the same environment
followup = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Fix any failing tests and re-run them.",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    background=True,
)

while followup.status == "in_progress":
    time.sleep(5)
    followup = client.interactions.get(id=followup.id)

print(followup.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First turn: run a task in the background
let interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Clone https://github.com/google/generative-ai-python and run its tests.",
    environment: "remote",
    background: true,
});

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

// Second turn: continue in the same environment
let followup = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Fix any failing tests and re-run them.",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    background: true,
});

while (followup.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    followup = await client.interactions.get(followup.id);
}

console.log(followup.output_text);
```

### REST

```
# 1. Start first interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Clone https://github.com/google/generative-ai-python and run its tests.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll until completed (repeat until status is "completed")
RESULT=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY")

ENVIRONMENT_ID=$(echo $RESULT | jq -r '.environment_id')

# 3. Continue in the same environment
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"input\": \"Fix any failing tests and re-run them.\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"background\": true
  }"
```

## Ortam

Her çağrı, bir Linux sanal alanı oluşturur veya yeniden kullanır. `environment` parametresi üç biçimde olabilir:

| Form | Açıklama |
| --- | --- |
| `"remote"` | Varsayılan ayarlarla yeni bir sanal alan sağlayın. |
| `"env_abc123"` | Tüm dosyaları ve durumu koruyarak mevcut bir ortamı kimliğe göre yeniden kullanın. |
| `{...}` | Özel kaynaklar ve ağ kurallarıyla tam `EnvironmentConfig` |

Kaynaklar (Git, GCS, satır içi), ağ, yaşam döngüsü ve kaynak sınırları hakkında ayrıntılı bilgi için [Ortamlar](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr) başlıklı makaleyi inceleyin.

## Tetikleyiciler

Tetikleyiciler, bir aracı cron zamanlamasına göre otomatik olarak çalışacak şekilde planlamanıza olanak tanır. Tetikleyici, bir temsilciyi, ortamı, istemi ve planı manuel müdahale olmadan tetiklenen kalıcı bir kaynağa bağlar. Her yürütme aynı ortamı yeniden kullandığından, bir çalıştırmada oluşturulan dosyalar kalıcı olur ve bir sonraki çalıştırmada görünür.

### Tetikleyici oluştur

Cron planı, saat dilimi ve etkileşim yapılandırmasını belirterek tetikleyici oluşturun. Tetikleyici, `active` durumunda başlar ve eşleşen bir sonraki cron zamanında tetiklenir. Sonraki çağrılarda tetikleyiciyi yönetmek için döndürülen `id` değerini kaydedin.

### Python

```
from google import genai

client = genai.Client()

trigger = client.triggers.create(
    schedule="0 9 * * *",
    time_zone="America/Argentina/Buenos_Aires",
    display_name="issue-solver",
    interaction={
        "agent": "antigravity-preview-05-2026",
        "input": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        "environment": {
            "type": "remote",
            "network": {
                "allowlist": [
                    {
                        "domain": "api.github.com",
                        "transform": {
                            "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                        },
                    },
                    {"domain": "github.com"},
                ]
            },
        },
    },
)

print(f"Trigger created: {trigger.id}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const trigger = await client.triggers.create({
    schedule: "0 9 * * *",
    time_zone: "America/Argentina/Buenos_Aires",
    display_name: "issue-solver",
    interaction: {
        agent: "antigravity-preview-05-2026",
        input: [{
            type: "text",
            text: "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        }],
        environment: {
            type: "remote",
            network: {
                allowlist: [
                    {
                        domain: "api.github.com",
                        transform: {
                            "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                        },
                    },
                    { domain: "github.com" },
                ],
            },
        },
    },
});

console.log(`Trigger created: ${trigger.id}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "schedule": "0 9 * * *",
      "time_zone": "America/Argentina/Buenos_Aires",
      "display_name": "issue-solver",
      "interaction": {
          "agent": "antigravity-preview-05-2026",
          "input": [{"type": "text", "text": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled accepted, skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."}],
          "environment": {
              "type": "remote",
              "network": {
                  "allowlist": [
                      {
                          "domain": "api.github.com",
                          "transform": {
                              "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                          }
                      },
                      {"domain": "github.com"}
                  ]
              }
          }
      }
  }'
```

`CreateTrigger` isteği aşağıdaki alanları kabul eder:

| Alan | Tür | Zorunlu | Açıklama |
| --- | --- | --- | --- |
| `schedule` | dize | Evet | Cron ifadesi (ör. saatlik için `0 * * * *`, hafta içi sabahları için `0 9 * * 1-5`). |
| `time_zone` | dize | Evet | IANA saat dilimi (ör. `UTC`, `America/Argentina/Buenos_Aires`). |
| `display_name` | dize | Hayır | Tetikleyicinin, kullanıcılar tarafından okunabilir adı. |
| `max_consecutive_failures` | tam sayı | Hayır | Tetikleyicinin otomatik olarak duraklatılmadan önceki maksimum hata sayısı. Varsayılan: 5. |
| `execution_timeout_seconds` | tam sayı | Hayır | Yürütme başına zaman aşımı süresi (saniye). Varsayılan: 600. |
| `interaction` | nesne | Evet | Ajanı, girişi, araçları ve ortamı tanımlayan bir `CreateInteractionRequest`. |

Yanıtta aşağıdaki önemli alanlar bulunur:

| Alan | Tür | Açıklama |
| --- | --- | --- |
| `id` | dize | Tetikleyicinin benzersiz tanımlayıcısı. Bunu sonraki tüm işlemlerde kullanın. |
| `status` | dize | Mevcut durum: `active`, `paused` veya `disabled`. |
| `next_run_time` | dize | Sonraki planlanmış yürütmenin ISO 8601 zaman damgası. |
| `consecutive_failure_count` | tam sayı | Son başarılı yürütmeden bu yana art arda başarısız olan yürütme sayısı. |

### Tetikleyicileri listeleme

Projenizle ilişkili tüm tetikleyicileri alın.

### Python

```
triggers = client.triggers.list()
for trigger in triggers.triggers:
    print(f"{trigger.id}: {trigger.display_name} ({trigger.status})")
```

### JavaScript

```
const triggers = await client.triggers.list();
for (const trigger of triggers.triggers) {
    console.log(`${trigger.id}: ${trigger.display_name} (${trigger.status})`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Tetikleyici edinme

Tek bir tetikleyicinin tam yapılandırmasını ve mevcut durumunu getirin.

### Python

```
trigger = client.triggers.get(id="TRIGGER_ID")
print(f"Schedule: {trigger.schedule}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
const trigger = await client.triggers.get("TRIGGER_ID");
console.log(`Schedule: ${trigger.schedule}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Duraklatma ve devam ettirme

Programlanmış yürütmeleri durdurmak için tetikleyiciyi duraklatabilir, zamanlamayı yeniden etkinleştirmek için ise devam ettirebilirsiniz. Duraklatma, manuel yürütmeleri etkilemez.

### Python

```
# Pause
client.triggers.update(id="TRIGGER_ID", status="paused")

# Resume
client.triggers.update(id="TRIGGER_ID", status="active")
```

### JavaScript

```
// Pause
await client.triggers.update("TRIGGER_ID", { status: "paused" });

// Resume
await client.triggers.update("TRIGGER_ID", { status: "active" });
```

### REST

```
# Pause
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "paused"}'

# Resume
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "active"}'
```

### Tetikleyici silme

Bir tetikleyiciyi kalıcı olarak kaldırma Geçmiş yürütme geçmişi silinmez.

### Python

```
client.triggers.delete(id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.delete("TRIGGER_ID");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Tetikleyiciyi hemen çalıştırma

Bir sonraki planlanmış zamanı beklemeden isteğe bağlı olarak tetikleyiciyi etkinleştirin. Bu özellik, tetikleyici duraklatılmış olsa bile çalışır.

### Python

```
client.triggers.run(trigger_id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.run("TRIGGER_ID");
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Yürütmeleri listeleme

Bir tetikleyicinin yürütme geçmişini görüntüleme Her yürütme işleminde `status`, zaman damgaları, tam etkileşim çıkışını getirmek için kullanabileceğiniz bir `interaction_id` ve tüm çalıştırmaların aynı korumalı alanı paylaştığını onaylayan bir `environment_id` bulunur.

### Python

```
executions = client.triggers.list_executions(trigger_id="TRIGGER_ID")
for ex in executions.trigger_executions:
    print(f"{ex.id}: {ex.status} ({ex.start_time} - {ex.end_time})")

# Fetch the full interaction for an execution
interaction = client.interactions.get(id=ex.interaction_id)
print(interaction.output_text)
```

### JavaScript

```
const executions = await client.triggers.listExecutions("TRIGGER_ID");
for (const ex of executions.trigger_executions) {
    console.log(`${ex.id}: ${ex.status} (${ex.start_time} - ${ex.end_time})`);
}

// Fetch the full interaction for an execution
const interaction = await client.interactions.get(ex.interaction_id);
console.log(interaction.output_text);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Kullanılabilirlik ve fiyatlandırma

Antigravity aracısı, Google AI Studio'daki [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) ve hem ücretsiz katman hem de ücretli katman projeleri için Gemini API aracılığıyla önizleme sürümünde kullanılabilir.

Fiyatlandırma, temel Gemini model jetonlarına ve aracının kullandığı araçlara dayalı [kullandıkça öde modeline](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#pricing-for-agents) göre belirlenir. Tek bir çıkış üreten standart bir sohbet isteğinin aksine, Antigravity etkileşimi, bir aracı iş akışıdır. Tek bir istek, muhakeme, araç yürütme, kod çalıştırma ve dosya yönetimi gibi işlemleri içeren bağımsız bir döngüyü tetikler. Ücretsiz katman projelerinde ücretsiz bir hız sınırı ve kullanım kotası bulunur.

Antigravity etkileşimleri, çok turlu bağımsız döngüler çalıştırır ve önemli sayıda jeton tüketebilir. Jeton kullanımını sınırlamak için isteğinizde [bütçe kontrolleri](#budget-controls) ayarlayın. Ayrıca [SSE akışıyla](https://ai.google.dev/gemini-api/docs/streaming?hl=tr) ilerlemeyi anlık olarak izleyebilir veya çalışan istekleri iptal edebilirsiniz.

### Bütçe kontrolleri

[Model seçimine](#model-selection) ek olarak, bir etkileşimin kullanabileceği toplam jeton sayısını (giriş + çıkış + düşünme) sınırlamak için `max_total_tokens` değerini `agent_config` içinde (`"type": "antigravity"` ile) ayarlayın.
Önbelleğe alınan jetonlar bu sınıra dahil edilmez. Ajan sınıra ulaştığında etkileşim durdurulur ve `status: "incomplete"` ile geri döner. Bu sınır, en iyi çaba ilkesine göre belirlenir: Ajanın adımlar arasında bütçeyi kontrol etme zamanına bağlı olarak gerçek kullanım bu sınırı biraz aşabilir.

`agent_config`, `agent` ve `input` ile birlikte etkileşim isteğinde bütçeyi ayarlayın.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    },
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": "/workspace/data.csv",
                "content": "id,name,value\n1,alpha,100\n2,beta,200\n",
            }
        ],
    }
)
print(f"Status: {interaction.status}")  # "incomplete" if budget was hit
print(f"Tokens used: {interaction.usage.total_tokens}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config: {
        type: "antigravity",
        max_total_tokens: 50000
    },
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: "/workspace/data.csv",
                content: "id,name,value\n1,alpha,100\n2,beta,200\n",
            },
        ],
    },
});
console.log(`Status: ${interaction.status}`);
console.log(`Tokens used: ${interaction.usage.total_tokens}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    },
    "environment": {
      "type": "remote",
      "sources": [
        {
          "type": "inline",
          "target": "/workspace/data.csv",
          "content": "id,name,value\n1,alpha,100\n2,beta,200\n"
        }
      ]
    }
  }'
```

#### Tamamlanmamış bir etkileşimi devam ettirme

Bir etkileşim `status: "incomplete"` döndürdüğünde temsilcinin çalışması ve bağlamı korunur. Kaldığı yerden devam etmek için orijinal etkileşime `id` ve `environment_id` referans veren yeni bir etkileşim gönderin. Yeni etkileşimin kendi `max_total_tokens` bütçesi olur.

### Python

```
# Continue from where the agent stopped
continuation = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="continue",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    }
)
print(f"Status: {continuation.status}")
```

### JavaScript

```
const continuation = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "continue",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    agent_config: {
        type: "antigravity",
        max_total_tokens: 50000
    }
});
console.log(`Status: ${continuation.status}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "continue",
    "previous_interaction_id": "INTERACTION_ID",
    "environment": "ENVIRONMENT_ID",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    }
  }'
```

### Tahmini maliyetler

Maliyetler, görevin karmaşıklığına göre değişir. Ajan, kaç araç çağrısı, kod yürütme ve dosya işlemi gerektiğini bağımsız olarak belirler. Aşağıdaki tahminler çalıştırmalara dayanmaktadır.

| Görev kategorisi | Giriş jetonu sayısı | Çıkış jetonu sayısı | Normal maliyet |
| --- | --- | --- | --- |
| **Araştırma ve bilgi sentezi** | 100.000-500.000 | 10.000-40.000 | 0,30-1,00 ABD doları |
| **Doküman ve içerik oluşturma** | 100.000-500.000 | 15.000-50.000 | 0,30-1,30 ABD doları |
| **Süreç ve sistem tasarımı** | 100.000-400.000 | 10.000-30.000 | 0,25-0,80 ABD doları |
| **Veri işleme ve analiz** | 300.000-3.000.000 | 30 bin - 150 bin | 0,70-3,25 ABD doları |

Giriş jetonlarının% 50-70'i genellikle önbelleğe alınır. Çok sayıda araç çağrısı içeren karmaşık aracı iş akışları, tek bir etkileşimde 3-5 milyon jeton biriktirebilir ve maliyeti yaklaşık 5 ABD dolarına kadar çıkabilir.

Önizleme döneminde **ortam bilgi işlem** (CPU, bellek, korumalı alan yürütme) için **ücret alınmaz**.

## Sınırlamalar

- **Önizleme durumu:** Antigravity ajanı ve Interactions API'si. Özellikler ve şemalar değişebilir.
- **Desteklenmeyen oluşturma yapılandırması:** Şu parametreler desteklenmez ve 400 hatası döndürür: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Yapılandırılmış çıkış:** Antigravity aracısı, yapılandırılmış çıkışları desteklemez.
- **Kullanılamayan araçlar:** `file_search`, `computer_use` ve `google_maps` henüz desteklenmemektedir.
- **Uzak MCP sınırlamaları:** Server-Sent Events (SSE) aktarımı desteklenmez (Streamable HTTP kullanın). Ayrıca, sunucu `name` kesinlikle küçük harf ve alfasayısal olmalıdır (büyük harf kullanılması genel bir `400 Bad Request` hatasını tetikler).
- **Dosya sistemi aracı:** Şu anda dosya sistemi aracı yok. Bu, `environment`'nın bir parçasıdır.
- **Mağaza şartı:** `background=True` kullanılarak yapılan aracı yürütme işlemi için `store=True` gerekir.
- **Yalnızca durum bilgisi olan işlev çağrısı:** İşlev çağrısı yalnızca durum bilgisi olan modda desteklenir. Sırayı devam ettirmek için `previous_interaction_id` kullanmanız gerekir. Geçmişi manuel olarak yeniden oluşturma (durum bilgisiz mod) desteklenmiyor.
- **Desteklenmeyen çok formatlı türler.** Ses, video ve doküman girişleri şu anda desteklenmemektedir. Yalnızca metin ve resimlere izin verilir.

## Sırada ne var?

- [Hızlı başlangıç](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr): Çok aşamalı etkileşimler ve akış.
- [Özel Ajanlar Oluşturma](https://ai.google.dev/gemini-api/docs/custom-agents?hl=tr): Özel talimatlar, beceriler ve ajanları kaydetme.
- [Ortamlar](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr): korumalı alan yapılandırması, kaynaklar, ağ iletişimi.
- [Kancalar](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=tr): Korumalı alan içinde güvenlik kapılarını ve yan etki doğrulamasını zorunlu kılın.
- [Deep Research aracısı](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr): Uzun araştırma görevleri.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr): Temel API.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-08-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-08-19 UTC."],[],[]]
