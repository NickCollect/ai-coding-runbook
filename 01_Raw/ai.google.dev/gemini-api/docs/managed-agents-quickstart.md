---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=hi
fetched_at: 2026-07-20T04:36:23.510889+00:00
title: "\u092e\u0948\u0928\u0947\u091c \u0915\u093f\u090f \u0917\u090f \u090f\u091c\u0947\u0902\u091f\u094b\u0902 \u0915\u0947 \u0932\u093f\u090f \u0915\u094d\u0935\u093f\u0915\u0938\u094d\u091f\u093e\u0930\u094d\u091f \u0917\u093e\u0907\u0921 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# मैनेज किए गए एजेंटों के लिए क्विकस्टार्ट गाइड

इस गाइड में, [Antigravity एजेंट](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=hi) का इस्तेमाल करके, Gemini API पर मैनेज किए गए एजेंट बनाने और उनका इस्तेमाल करने का तरीका बताया गया है. आपको एजेंट से पहला कॉल करने, कई बार बातचीत जारी रखने, जवाब स्ट्रीम करने, सैंडबॉक्स से फ़ाइलें डाउनलोड करने, और Antigravity के मैनेज किए गए एजेंट के साथ काम करने का मौका मिलेगा.

## एजेंट के साथ पहली बार इंटरैक्ट करना

[Interactions API](https://ai.google.dev/gemini-api/docs?hl=hi) को एक बार कॉल करने पर, Linux सैंडबॉक्स उपलब्ध कराया जाता है, एजेंट लूप चलाया जाता है, और नतीजा दिखाया जाता है. आपको तीन पैरामीटर तय करने होंगे:

- `agent` को `"antigravity-preview-05-2026",` के तौर पर पास करें. यह पहले से तय और सामान्य मकसद के लिए मैनेज किए जाने वाले एजेंट का मौजूदा वर्शन है.
- `environment="remote"` को तय करें, ताकि नया सैंडबॉक्स एनवायरमेंट उपलब्ध कराया जा सके.
- एक इनपुट बनाएं और उसमें बताएं कि आपको एजेंट से क्या काम करवाना है.

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

जवाब में, एक `Interaction` ऑब्जेक्ट मिलता है. `interaction.id` और `interaction.environment_id` को सेव करें, ताकि उसी सैंडबॉक्स में बातचीत जारी रखी जा सके. एजेंट के आखिरी जवाब को ऐक्सेस करने के लिए, `interaction.output_text` का इस्तेमाल करें. `interaction.steps` में, एजेंट की ओर से किए गए हर चरण की जानकारी दी गई होती है. जैसे, तर्क, टूल कॉल, कोड एक्ज़ीक्यूट करना.

## बातचीत जारी रखना (कई बार)

यह एपीआई, दो इंडिपेंडेंट स्टेट डाइमेंशन ट्रैक करता है:

- **बातचीत का कॉन्टेक्स्ट:** चैट का इतिहास, तर्क का पता लगाना, टूल का इस्तेमाल करना, और `previous_interaction_id` का इस्तेमाल करना.
- [**एनवायरमेंट की स्थिति:**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=hi) फ़ाइलें, इंस्टॉल किए गए पैकेज, और सैंडबॉक्स की स्थिति. इसके लिए, `environment` का इस्तेमाल किया जाता है.

इन दोनों को इनकी जगह पर पास करें, ताकि प्रोसेस को फिर से शुरू किया जा सके:

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

पहले टर्न (`fibonacci.txt`) की फ़ाइलें, दूसरे टर्न में भी मौजूद रहती हैं. एजेंट के पास बातचीत का कॉन्टेक्स्ट भी बना रहता है.

इनको अलग-अलग तरीके से इस्तेमाल किया जा सकता है:

- **बातचीत मिटाएं, फ़ाइलें सेव रखें:** `previous_interaction_id` को शामिल न करें. सिर्फ़ `environment` का इस्तेमाल करके एनवायरमेंट आईडी पास करें, ताकि उसी वर्कस्पेस में नई बातचीत शुरू की जा सके.
- **बातचीत जारी रखें, नया वर्कस्पेस:** `previous_interaction_id` पास करें और नए सैंडबॉक्स के लिए `environment="remote"` सेट करें.

### कॉन्टेक्स्ट को अपने-आप छोटा करने की सुविधा

लंबे समय तक चलने वाली, कई बार की बातचीत में, तर्क देने के चरणों, टूल कॉल, और बड़ी फ़ाइल के कॉन्टेंट का रॉ डेटा तेज़ी से बढ़ सकता है. इससे कॉन्टेक्स्ट के लिए उपलब्ध जगह काफ़ी कम हो जाती है. टोकन की सीमा से जुड़ी गड़बड़ियों को रोकने और एजेंट का फ़ोकस बनाए रखने (कॉन्टेक्स्ट रोट को रोकने) के लिए, Managed Agents API में करीब 1,35,000 टोकन पर कॉन्टेक्स्ट कंपैक्शन का एक नेटिव चरण होता है. यह अपने-आप होता है.

## जवाब को स्ट्रीम करना

लंबे समय तक चलने वाले टास्क के लिए, जवाब को स्ट्रीम किया जा सकता है. इससे एजेंट को रीयल टाइम में काम करते हुए देखा जा सकता है:

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

स्ट्रीमिंग से, चरण के अंतर का एक इटरेबल मिलता है. यह इंक्रीमेंटल टेक्स्ट, तर्क के टोकन, और टूल कॉल के अपडेट होते हैं. [स्ट्रीमिंग गाइड](https://ai.google.dev/gemini-api/docs/streaming?hl=hi) में, जवाबों को स्ट्रीम करने के तरीके के बारे में ज़्यादा जानें.

## एनवायरमेंट से फ़ाइलें डाउनलोड करना

जब एजेंट, सैंडबॉक्स में फ़ाइलें बनाता है. इन्हें सीधे एचटीटीपी अनुरोध (अभी तक कोई एसडीके तरीका नहीं है) के साथ Files API का इस्तेमाल करके डाउनलोड करें:

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

## मैनेज किए जा रहे एजेंट को सेव करना

पिछले चरणों में, हमने डिफ़ॉल्ट Antigravity एजेंट का इस्तेमाल किया था और उसे इनलाइन तरीके से पसंद के मुताबिक बनाया था. कॉन्फ़िगरेशन (निर्देश, स्किल, और एनवायरमेंट) को दोहराने के बाद, इसे मैनेज किए जा सकने वाले एजेंट के तौर पर सेव किया जा सकता है. इससे कॉन्फ़िगरेशन को दोहराए बिना, आईडी के ज़रिए इसे चालू किया जा सकता है.

किसी एजेंट को सेव करते समय, आपको `base_environment` तय करना होता है. इसके लिए, सोर्स से डेटा लिया जा सकता है या किसी मौजूदा एनवायरमेंट को फ़ोर्क किया जा सकता है. एजेंट, हर नए इंटरैक्शन के लिए इस एनवायरमेंट का इस्तेमाल करेगा.

**सोर्स से:** सोर्स को इनलाइन या GitHub या Cloud Storage जैसे अन्य सोर्स से तय करें.

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

## मैनेज किए जा रहे एजेंट को शुरू करना

मैनेज किए जा रहे एजेंट को सेव करने के बाद, उसे आईडी के ज़रिए शुरू किया जा सकता है. हर इनवोकेशन, बेस एनवायरमेंट को फ़ोर्क करता है. इसलिए, हर रन क्लीन तरीके से शुरू होता है:

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

## आगे क्या करना है

- [ऐंटीग्रैविटी एजेंट](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=hi): सुविधाएं, इस्तेमाल किए जा सकने वाले टूल, मल्टीमॉडल इनपुट, कीमत, और सीमाएं.
- [मैनेज किए गए एजेंट बनाना](https://ai.google.dev/gemini-api/docs/custom-agents?hl=hi): अपने निर्देशों, कौशल, और डेटा के साथ Antigravity को बेहतर बनाएं.
- [एनवायरमेंट](https://ai.google.dev/gemini-api/docs/agent-environment?hl=hi): सोर्स, नेटवर्किंग, लाइफ़साइकल, संसाधन की सीमाएं.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi): यह मॉडल और एजेंट के लिए बुनियादी एपीआई है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-22 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-22 (UTC) को अपडेट किया गया."],[],[]]
