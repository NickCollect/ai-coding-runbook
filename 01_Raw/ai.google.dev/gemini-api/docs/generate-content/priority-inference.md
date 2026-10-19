---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=sq
fetched_at: 2026-10-19T05:42:12.044166+00:00
title: "Konkludimi me p\u00ebrpar\u00ebsi \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs/generate-content?hl=sq)

Dërgo komente

# Konkludimi me përparësi

Përshkrimi: Mëso se si të optimizosh vonesën me nivelin e përparësisë së përfundimit

Gemini Priority API është një nivel i parashikimit premium i krijuar për ngarkesat e punës që janë kritike për biznesin që kërkojnë vonesë më të ulët dhe besueshmëri më të lartë me një çmim premium. Trafiku i nivelit të përparësisë ka përparësi ndaj
trafikut të nivelit standard të API-së dhe Flex.

Konkludimi i përparësisë ofrohet për përdoruesit e [nivelit 2 dhe nivelit 3](https://ai.google.dev/gemini-api/docs/billing?hl=sq#about-billing) nëpër pikat fundore të API-së së "Gjenerimit të përmbajtjes" dhe API-së së "Ndërveprimeve".

## Si të përdorësh "Përparësinë"

Për të përdorur nivelin e përparësisë, cakto fushën `service_tier` në trupin e kërkesës në
`priority`. Niveli i parazgjedhur është standard nëse fusha hiqet.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3.8-flash",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### QETËSI

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## Si funksionon përfundimi për "Prioritetin"

Itineraret e përfundimeve me përparësi i drejtojnë kërkesat te radhët e llogaritjeve me nivel të lartë kritik, duke ofruar performancë të parashikueshme dhe të shpejtë për aplikacionet e përdoruesve. Mekanizmi i tij kryesor është një ulje e nivelit të shërbimit në anën e serverit në përpunimin standard për trafikun që tejkalon kufijtë dinamikë, duke siguruar stabilitetin e aplikacionit në vend që të dështojë kërkesa.

| Veçoria | Me përparësi | Standard | Tregim force | Paketë |
| --- | --- | --- | --- | --- |
| **Çmimet** | 75-100% më shumë se standarde | Çmimi i plotë | 50% zbritje | 50% zbritje |
| **Vonesa** | Sekonda | Sekonda në minuta | Minuta (objektivi 1-15 min.) | Deri në 24 orë |
| **Besueshmëria** | E lartë (jo e heqshme) | E lartë / mesatarisht e lartë | Me përpjekjen më të mirë (i heqshëm) | E lartë (për rendiment) |
| **Ndërfaqja** | Sinkron | Sinkron | Sinkron | Josinkron |

### Përfitimet kryesore

- **Vonesë e ulët**: Projektuar për kohë përgjigjeje në sekonda për vegla interaktive të IA-së për përdoruesit.
- **Besueshmëri e lartë**: Trafiku trajtohet me nivelin më të lartë të kriticitetit dhe është
  rreptësisht i pandërprerë.
- **Degradimi i butë**: Rritjet e trafikut që tejkalojnë kufijtë dinamikë ulen automatikisht në nivelin "Standard" për përpunim në vend që të dështojnë, duke parandaluar ndërprerjet e shërbimit.
- **Fërkimi i ulët**: Përdor të njëjtën metodë sinkrone `generateContent` si nivelet standarde dhe Flex.

### Rastet e përdorimit

Përpunimi me përparësi është ideal për flukset e punës që janë kritikë për biznesin ku performanca dhe besueshmëria janë parësore.

- **Aplikacionet ndërvepruese të IA-së**: Robotët bisedarë të shërbimit ndaj klientit dhe pilotët ndihmës ku përdoruesit paguajnë një tarifë premium dhe presin përgjigje të shpejta dhe të qëndrueshme.
- **Motorët e vendimeve në kohë reale**: Sistemet që kërkojnë rezultate shumë të besueshme me vonesë të ulët, si p.sh. triazhimi i biletave të drejtpërdrejta ose zbulimi i mashtrimeve.
- **Veçoritë premium për klientët**: Zhvilluesit që duhet të garantojnë objektiva më të lartë të nivelit të shërbimit (SLO) për klientët me pagesë.

### Kufijtë e normës

Konsumimi me përparësi ka kufijtë e vet të normës edhe pse konsumimi llogaritet për [kufijtë e normës së përgjithshme të trafikut interaktiv](https://aistudio.google.com/rate-limit?hl=sq). Kufijtë e parazgjedhur të normës
për përfundimin e "Përparësisë" janë **0,3 herë kufiri standard i normës për modelin / nivelin**

### Logjika e uljes normale të nivelit

Nëse kufijtë e "Prioritetit" tejkalohen për shkak të mbingarkesës, kërkesat e tepërta **zbresin automatikisht dhe pa probleme** në përpunim standard në vend që të dështojnë me një gabim 503 ose 429. Kërkesat e ulura në nivel tarifohen me tarifën standarde, jo me tarifën premium të përparësisë.

### Përgjegjësia e klientit

- **Monitorimi i përgjigjes**: Zhvilluesit duhet të monitorojnë `x-gemini-service-tier`
  titullin në përgjigjen e API-së për të zbuluar nëse kërkesat po ulen shpesh në nivelin `standard`.
- **Riprovat**: Klientët duhet të zbatojnë logjikën e riprovës/kohën e pritjes eksponenciale për gabimet standarde, si p.sh. `DEADLINE_EXCEEDED`.

## Çmimet

Përfundimi me përparësi ka një çmim 75-100% më të lartë se [API-ja standarde](https://ai.google.dev/gemini-api/docs/pricing?hl=sq) dhe faturohet për çdo kod.

## Modelet e mbështetura

Modelet e mëposhtme mbështesin përfundimin me përparësi:

| Modeli | Konkludimi me përparësi |
| --- | --- |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=sq) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=sq) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=sq) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=sq) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=sq) | ✔️ |
| [Versioni paraprak i Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=sq) | ✔️ |
| [Pamja paraprake e Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=sq) | ✔️ |
| [Pamja paraprake e imazheve të Gemini 3 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=sq) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=sq) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=sq) | ✔️ |
| [Imazhi i Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=sq) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=sq) | ✔️ |

## Çfarë ka më pas

Lexo rreth opsioneve të tjera të [përfundimit dhe optimizimit](https://ai.google.dev/gemini-api/docs/optimization?hl=sq) të Gemini:

- [Deduksioni Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=sq) për 50% ulje të kostos.
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=sq) për përpunim asinkron brenda 24 orëve.
- [Ruajtja në memorien specifike e kontekstit](https://ai.google.dev/gemini-api/docs/caching?hl=sq) për kosto të reduktuara të kodeve të hyrjes.

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-13 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-13 UTC."],[],[]]
