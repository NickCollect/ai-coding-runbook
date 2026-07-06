---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr
fetched_at: 2026-07-06T05:19:38.533194+00:00
title: "Y\u00f6netilen Ajanlar H\u0131zl\u0131 Ba\u015flang\u0131\u00e7 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Yönetilen Ajanlar Hızlı Başlangıç

Bu kılavuzda, [Antigravity agent](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=tr)'ı kullanarak Gemini API'de Yönetilen Ajanlar oluşturma ve kullanma adımları açıklanmaktadır. İlk temsilci görüşmenizi yapacak, çok turlu bir sohbete devam edecek, yanıtı yayınlayacak, korumalı alandan dosya indirecek ve Antigravity tarafından yönetilen temsilciyle çalışacaksınız.

## İlk temsilci etkileşiminizi çalıştırma

[Interactions API](https://ai.google.dev/gemini-api/docs?hl=tr)'ye yapılan tek bir çağrı, Linux özel korumalı alanını sağlar, aracı döngüsünü çalıştırır ve sonucu döndürür. Üç parametre tanımlarsınız:

- Önceden tanımlanmış ve genel amaçlı yönetilen aracımızın mevcut sürümü olan `agent` değerini `"antigravity-preview-05-2026",` olarak iletin.
- Yeni bir temiz sanal alan ortamı sağlamak için `environment="remote"` tanımlayın.
- Temsilcinin ne yapmasını istediğinizi tanımlayan bir giriş oluşturun.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output: {interaction.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment: "remote",
});

console.log(`Interaction ID: ${interaction.id}`);
console.log(`Environment ID: ${interaction.environment_id}`);

console.log(`Output: ${interaction.output_text}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."}],
    "environment": {"type": "remote"}
}'
```

Yanıt, `Interaction` nesnesi döndürür. Aynı korumalı alanda sohbete devam etmek için `interaction.id` ve `interaction.environment_id` değerlerini saklayın. Temsilcinin son yanıtına erişmek için `interaction.output_text` simgesini kullanın. `interaction.steps`, aracının gerçekleştirdiği her adımı (gerekçe, araç çağrıları, kod yürütme) listeler.

## Görüşmeye devam etme (çok adımlı)

API, iki bağımsız durum boyutunu izler:

- **Sohbet bağlamı:** Sohbet geçmişi, akıl yürütme izi, araç kullanımı, `previous_interaction_id` kullanımı.
- [**Ortam durumu:**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr) `environment` kullanılarak dosyalar, yüklü paketler ve korumalı alan durumu.

Devam etmek için her ikisini de ilgili yere yerleştirin:

### Python

```
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
)

print(interaction_2.output_text)
```

### JavaScript

```
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    input: "Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
}, { timeout: 300_000 });

console.log(interaction2.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "previous_interaction_id": "interaction_id_from_step_1",
    "environment": "environment_id_from_step_1",
    "input": [{"type": "text", "text": "Now plot the Fibonacci sequence as a line chart and save it as chart.png."}]
}'
```

1. turdaki dosyalar (`fibonacci.txt`) 2. turda kalır. Temsilci, sohbet bağlamını da korur.

Bunları bağımsız olarak karıştırıp eşleştirebilirsiniz:

- **Net görüşme, dosyaları saklama:** `previous_interaction_id` simgesini atlayın, aynı çalışma alanında yeni bir görüşme için yalnızca `environment` kullanarak ortam kimliğini iletin.
- **Sohbeti sürdürme, yeni çalışma alanı:** Geçiş `previous_interaction_id`, yeni bir sandbox için `environment="remote"` ayarlayın.

### Otomatik bağlam sıkıştırma

Uzun süren, çok turlu sohbetlerde, muhakeme adımlarının, araç çağrılarının ve büyük dosya içeriklerinin ham geçmişi hızla büyüyebilir ve önemli miktarda bağlam alanı tüketebilir. Yönetilen Aracılar API'si, jeton sınırı hatalarını önlemek ve aracının odak noktasını korumak (bağlam bozulmasını önlemek) için yaklaşık 135.000 jetonluk yerel bir bağlam sıkıştırma adımına sahiptir. Bu, otomatik olarak gerçekleşir.

## Yanıtı akış şeklinde gösterme

Uzun süren görevlerde, temsilcinin çalışmasını anlık olarak görmek için yanıtı yayınlayabilirsiniz:

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)

for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment: "remote",
    stream: true,
});

for await (const event of stream) {
    console.log(event);
}
```

### REST

```
curl -N -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    "environment": "remote",
    "stream": true
}'
```

Yayın, adım farklılıklarının yinelenebilir bir değerini döndürür. Bu değerler, artımlı metin, akıl yürütme jetonları ve araç çağrısı güncellemeleridir. Yanıtları yayınlama hakkında daha fazla bilgiyi [Yayınlama kılavuzu](https://ai.google.dev/gemini-api/docs/streaming?hl=tr)'nda bulabilirsiniz.

## Ortamdan dosya indirme

Aracı, sanal ortamda dosya oluşturduğunda Doğrudan HTTP isteğiyle (henüz SDK yöntemi yok) Files API'yi kullanarak indirin:

### Python

```
import os
import requests
import tarfile

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot.tar", "wb") as f:
    f.write(response.content)

with tarfile.open("snapshot.tar") as tar:
    tar.extractall(path="extracted_snapshot")
```

### JavaScript

```
import fs from "fs";
import { execSync } from "child_process";

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot.tar", buffer);

if (!fs.existsSync("extracted_snapshot")) {
    fs.mkdirSync("extracted_snapshot");
}
execSync("tar -xf snapshot.tar -C extracted_snapshot");

console.log(fs.readdirSync("extracted_snapshot"));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-o snapshot.tar

tar -xf snapshot.tar -C extracted_snapshot
```

## Yönetilen bir aracıyı kaydetme

Önceki adımlarda varsayılan Antigravity aracısını kullandık ve satır içi olarak özelleştirdik. Yapılandırmanızı (talimatlar, beceriler ve ortam) yineledikten sonra yönetilen bir aracı olarak kaydedebilirsiniz. Bu sayede, yapılandırmayı tekrarlamadan kimliğe göre çağırabilirsiniz.

Bir aracı kaydettiğinizde `base_environment` tanımlarsınız (kaynaklardan veya mevcut bir ortamı çatallayarak). Temsilci, her yeni etkileşim için bu ortamı kullanır.

**Kaynaklardan:** Kaynakları satır içi olarak veya GitHub ya da Cloud Storage gibi diğer kaynaklardan tanımlayın.

### Python

```
agent = client.agents.create(
    id="fibonacci-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports.",
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ],
    },
)

print(f"Saved agent: {agent.id}")
```

### JavaScript

```
const agent = await client.agents.create({
    id: "fibonacci-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always include a chart and a summary table in your reports.",
            },
            {
                type: "repository",
                source: "https://github.com/your-org/skills",
                target: ".agents/skills"
            }
        ],
    },
});

console.log(`Saved agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "fibonacci-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "system_instruction": "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports."
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ]
    }
}'
```

## Yönetilen aracıyı çağırma

Kaydettiğiniz yönetilen temsilcileri kimlikleriyle çağırabilirsiniz. Her çağırma işlemi temel ortamı çatalladığından her çalıştırma temiz bir şekilde başlar:

### Python

```
result = client.interactions.create(
    agent="fibonacci-analyst",
    input="Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "fibonacci-analyst",
    input: "Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment: "remote",
}, {
    timeout: 300_000,
});

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "fibonacci-analyst",
    "environment": "remote",
    "input": "Generate the first 50 prime numbers, plot their distribution, and save a PDF report."
}'
```

## Sırada ne var?

- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr): Yetenekler, desteklenen araçlar, çok formatlı giriş, fiyatlandırma ve sınırlamalar.
- [Yönetilen Ajanlar Oluşturma](https://ai.google.dev/gemini-api/docs/custom-agents?hl=tr): Antigravity'yi kendi talimatlarınız, becerileriniz ve verilerinizle genişletin.
- [Ortamlar](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr): kaynaklar, ağ, yaşam döngüsü, kaynak sınırları.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr): Modeller ve aracılar için temel API.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-22 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-22 UTC."],[],[]]
