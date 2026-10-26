---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=sq
fetched_at: 2026-10-26T05:54:05.675902+00:00
title: "Konkludimi me p\u00ebrpar\u00ebsi \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs?hl=sq)

Dërgo komente

# Konkludimi me përparësi

Description: Learn how to optimize latency with the Priority inference tier in the Interactions API

Gemini Priority API është një nivel i parashikimit premium i krijuar për ngarkesat e punës që janë kritike për biznesin që kërkojnë vonesë më të ulët dhe besueshmëri më të lartë me një çmim premium. Trafiku i nivelit të përparësisë ka përparësi mbi
trafikun e nivelit standard të API-së dhe nivelit Flex.

Konkluzioni me përparësi ofrohet në pikat fundore të Interactions API.

## Si të përdorësh "Përparësinë"

Për të përdorur nivelin "Me përparësi", cakto fushën `service_tier` në kërkesën tënde në `priority`. Niveli i parazgjedhur është standard nëse fusha hiqet.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
        model: "gemini-3.8-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Perform a priority inference task."))
        .serviceTier(ServiceTier.PRIORITY)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("Perform a priority inference task."),
            ServiceTier: interactions.ServiceTierPriority.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### QETËSI

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Si funksionon nxjerrja e përfundimeve për "Përparësinë"

Itineraret e përfundimeve me përparësi i drejtojnë kërkesat te radhët e llogaritjeve me nivel të lartë kritik, duke ofruar performancë të parashikueshme dhe të shpejtë për aplikacionet e përdoruesve. Mekanizmi i tij kryesor është një ulje e nivelit në anën e serverit në përpunim standard për trafikun që tejkalon kufijtë dinamikë, duke siguruar qëndrueshmërinë e aplikacionit në vend që të dështojë kërkesa.

| Veçoria | Me përparësi | Standard | Tregim force | Paketë |
| --- | --- | --- | --- | --- |
| **Çmimet** | 75-100% më shumë se Standard | Çmimi i plotë | 50% zbritje | 50% zbritje |
| **Vonesa** | Sekonda | Sekonda në minuta | Minuta (objektivi 1–15 min.) | Deri në 24 orë |
| **Besueshmëria** | E lartë (jo e lëshueshme) | E lartë / mesatarisht e lartë | Me përpjekjen më të mirë (i heqshëm) | E lartë (për rendimentin) |
| **Ndërfaqja** | Sinkron | Sinkron | Sinkron | Josinkron |

### Përfitimet kryesore

- **Vonesë e ulët**: Projektuar për kohë përgjigjeje në sekonda për vegla interaktive të IA-së për përdoruesit.
- **Besueshmëri e lartë**: Trafiku trajtohet me nivelin më të lartë të rëndësisë dhe është rreptësisht i pashmangshëm.
- **Degradimi i butë**: Rritjet e trafikut që tejkalojnë kufijtë dinamikë ulen automatikisht në nivelin "Standard" për përpunim në vend që të dështojnë, duke parandaluar ndërprerjet e shërbimit.
- **Fërkim i ulët**: Përdor të njëjtën metodë sinkrone `create` si niveli standard dhe ai Flex.

### Rastet e përdorimit

Përpunimi me përparësi është ideal për flukset e punës kritike për biznesin ku performanca
dhe besueshmëria janë parësore.

- **Aplikacionet ndërvepruese të IA-së**: Robotët e bisedës dhe bashkëpilotët e shërbimit të klientit ku përdoruesit paguajnë një premium dhe presin përgjigje të shpejta dhe të qëndrueshme.
- **Motorët e vendimmarrjes në kohë reale**: Sistemet që kërkojnë rezultate shumë të besueshme me vonesë të ulët, si p.sh. triazhi i biletave drejtpërdrejt ose zbulimi i mashtrimeve.
- **Veçoritë e klientëve premium**: Zhvilluesit që duhet të garantojnë objektiva më të lartë të nivelit të shërbimit (SLO) për klientët që paguajnë.

### Kufijtë e kursit të këmbimit

Konsumimi me përparësi ka kufijtë e vet të normës edhe pse konsumimi llogaritet për [kufijtë e normës së përgjithshme të trafikut interaktiv](https://aistudio.google.com/rate-limit?hl=sq). Kufijtë e parazgjedhur të normës
për përfundimin e "Përparësisë" janë **0,3 herë kufiri standard i normës për modelin / nivelin**

### Logjika e uljes së nivelit me hapa të ngadaltë

Nëse kufijtë e "Përparësisë" tejkalohen për shkak të mbingarkesës, kërkesat e tepërta
**ulen automatikisht dhe me mirësjellje** në përpunimin "Standard" në vend që të
dështojnë me një gabim 503 ose 429. Kërkesat e ulura në nivel tarifohen me tarifën standarde, jo me tarifën premium të "Përparësisë".

### Përgjegjësia e klientit

- **Monitorimi i përgjigjes**: Zhvilluesit duhet të monitorojnë kokën `x-gemini-service-tier`
  në përgjigjen e API-së për të zbuluar nëse kërkesat po ulen shpesh në
  `standard`.
- **Riprovat**: Klientët duhet të zbatojnë logjikën e riprovës/kohën e pritjes eksponenciale për gabimet standarde, si p.sh. `DEADLINE_EXCEEDED`.

## Çmimet

Konkluzioni me përparësi ka një çmim 75-100% më të lartë se [API-ja standarde](https://ai.google.dev/gemini-api/docs/pricing?hl=sq) dhe faturohet për çdo dërgim.

## Modelet e mbështetura

Modelet e mëposhtme mbështesin nxjerrjen e përfundimeve me përparësi:

| Modeli | Konkludimi me përparësi |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=sq) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=sq) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=sq) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=sq) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=sq) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=sq) | ✔️ |
| [Pamja paraprake e Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=sq) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=sq) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=sq) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=sq) | ✔️ |

## Çfarë ka më pas

- [Deduksioni Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=sq) për reduktimin e kostos.
- [Tokenët](https://ai.google.dev/gemini-api/docs/tokens?hl=sq): Kupto tokenët.

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-13 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-13 UTC."],[],[]]
