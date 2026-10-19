---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=sq
fetched_at: 2026-10-19T05:40:12.734533+00:00
title: "Gemini Developer API kundrejt platform\u00ebs Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs?hl=sq)

Dërgo komente

# Gemini Developer API kundrejt platformës Gemini

Kur zhvillon zgjidhje gjeneruese të IA-së me Gemini, Google ofron dy produkte API: [Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=sq) dhe [Gemini platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=sq).

Gemini Developer API ofron shtegun më të shpejtë për të ndërtuar, prodhuar dhe shkallëzuar aplikacionet e mundësuara nga Gemini. Shumica e zhvilluesve duhet të përdorin Gemini Developer API, përveçse nëse ka nevojë për kontrolle specifike të ndërmarrjes.

Platforma Gemini ofron një ekosistem gjithëpërfshirës veçorish dhe shërbimesh të gatshme për ndërmarrjen për ndërtimin dhe vendosjen e aplikacioneve të IA-së gjeneruese të mbështetura nga Google Cloud.

Ne e kemi thjeshtuar së fundi migrimin midis këtyre shërbimeve. Gemini
Developer API dhe Gemini platform API janë të dyja të qasshme tani
nëpërmjet [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=sq) të unifikuar dhe
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=sq).

## Krahasimi i kodeve: API-ja e ndërveprimeve (rekomandohet)

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=sq) është mënyra e rekomanduar për të ndërtuar me modelet dhe agjentët e Gemini. Shembujt e mëposhtëm
krahasojnë gjenerimin e tekstit midis Gemini Developer API dhe platformës Gemini.

### Python

Mund të qasesh si te Gemini Developer API, ashtu edhe te shërbimet e platformës Gemini nëpërmjet bibliotekës `google-genai` (`>= 2.3.0`). Shiko faqen e
[bibliotekave](https://ai.google.dev/gemini-api/docs/libraries?hl=sq) për udhëzime se si të instalosh
`google-genai`.

### Gemini Developer API

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words",
)
print(interaction.output_text)
```

### Gemini platform API

```
from google import genai

client = genai.Client(
    enterprise=True, project="your-project-id", location="global"
)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words",
)
print(interaction.output_text)
```

### JavaScript dhe TypeScript

Mund të qasesh si te Gemini Developer API, ashtu edhe te shërbimet e platformës Gemini nëpërmjet bibliotekës `@google/genai` (`>= 2.3.0`). Shiko faqen e
[bibliotekave](https://ai.google.dev/gemini-api/docs/libraries?hl=sq) për udhëzime se si të instalosh
`@google/genai`.

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

### Gemini platform API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  enterprise: true,
  project: "your_project",
  location: "global",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

## Krahasimi i kodeve: API-ja generateContent

Ndërkohë që API-ja e "Ndërveprimeve" rekomandohet për projektet e reja, API-ja e
`generateContent` vazhdon të mbështetet.

### Python

Mund të qasesh si te Gemini Developer API, ashtu edhe te shërbimet e platformës Gemini nëpërmjet bibliotekës `google-genai`. Shiko faqen e
[bibliotekave](https://ai.google.dev/gemini-api/docs/libraries?hl=sq) për udhëzime se si të instalosh
`google-genai`.

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.8-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript dhe TypeScript

Mund të qasesh si te Gemini Developer API, ashtu edhe te shërbimet e platformës Gemini nëpërmjet bibliotekës `@google/genai`. Shiko faqen e [bibliotekave](https://ai.google.dev/gemini-api/docs/libraries?hl=sq) për udhëzime se si të instalosh `@google/genai`.

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

Mund të qasesh si te Gemini Developer API, ashtu edhe te shërbimet e platformës Gemini nëpërmjet bibliotekës `google.golang.org/genai`. Shiko faqen e [bibliotekave](https://ai.google.dev/gemini-api/docs/libraries?hl=sq) për udhëzime se si të instalosh `google.golang.org/genai`.

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google Cloud project
const project = "your-project"

// A Google Cloud location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Raste të tjera përdorimi dhe platforma

Referoju udhëzuesve specifikë për rastet e përdorimit në [Dokumentacionin e Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=sq)
dhe [dokumentacionin e platformës Gemini](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=sq)
për platforma dhe raste të tjera përdorimi.

## Konsideratat për migrimin

Kur migron:

- Do të duhet të përdorësh llogaritë e shërbimit të Google Cloud për t'u identifikuar. Shiko
  [dokumentacionin e platformës Gemini](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=sq)
  për më shumë informacione.
- Mund të përdorësh projektin tënd ekzistues të Google Cloud
  (të njëjtin që ke përdorur për të gjeneruar çelësin e API-së) ose mund të
  [krijosh një projekt të ri të Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=sq).
- Rajonet e mbështetura mund të ndryshojnë midis Gemini Developer API dhe Gemini platform API. Gjatë "Versionit paraprak",
  [Interactions API në platformën Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions/?hl=sq)
  mbështet vetëm pikën përfundimtare `global` (`location="global"`). Shih listën e
  [rajoneve të mbështetura për IA-në gjeneruese në Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=sq).
- Çdo model që ke krijuar në Google AI Studio duhet të ritrajnohet në platformën Gemini.

Nëse nuk ke më nevojë të përdorësh çelësin e Gemini API për Gemini Developer API, atëherë ndiq praktikat më të mira të sigurisë dhe fshije atë.

Për të fshirë një çelës API:

1. Hap faqen e
   [Kredencialeve të Google Cloud API](https://console.cloud.google.com/apis/credentials?hl=sq).
2. Gjej çelësin API që dëshiron të fshish dhe kliko ikonën **Veprimet**.
3. Zgjidh **Fshi çelësin API**.
4. Në modalen **Fshi kredencialet**, zgjidh **Fshi**.

   Fshirja e një çelësi API kërkon disa minuta që të përhapet. Pasi të përfundojë
   përhapja, çdo trafik që përdor çelësin e fshirë të API-së do të refuzohet.

## Hapat e radhës

- Eksploro udhëzuesin e zhvilluesit të
  [Interactions API në platformën Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions/?hl=sq).
- Shiko
  [Përmbledhjen e IA-së gjeneruese në platformën Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=sq)
  për të mësuar më shumë rreth zgjidhjeve të IA-së gjeneruese në platformën Gemini.

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-08 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-08 UTC."],[],[]]
