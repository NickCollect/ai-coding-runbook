---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/url-context?hl=sq
fetched_at: 2026-10-19T05:56:10.999461+00:00
title: "Konteksti i URL-s\u00eb \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs/generate-content?hl=sq)

Dërgo komente

# Konteksti i URL-së

Vegla e kontekstit të URL-së të lejon që t'u japësh kontekst shtesë modeleve në formën e URL-ve. Duke përfshirë URL-të në kërkesën tënde, modeli do të ketë qasje te përmbajtjet nga ato faqe (për aq kohë sa nuk është një lloj URL-je i listuar në [seksionin e kufizimeve](#limitations)) për të informuar dhe përmirësuar përgjigjen e tij.

Vegla e kontekstit me URL është e dobishme për detyra si më poshtë:

- **Nxirr të dhënat**: Merr informacione specifike si çmimet, emrat ose gjetjet kryesore nga disa URL.
- **Krahaso dokumentet**: Analizo disa raporte, artikuj ose skedarë PDF për të identifikuar ndryshimet dhe për të monitoruar tendencat.
- **Sintetizo dhe krijo përmbajtje**: Kombino informacionet nga disa URL burimesh për të gjeneruar përmbledhje, postime në blog ose raporte të sakta.
- **Analizo kodin dhe dokumentet**: Drejtohu te një depo e GitHub ose dokumentacion teknik për të shpjeguar kodin, për të gjeneruar udhëzime konfigurimi ose për t'iu përgjigjur pyetjeve.

Shembulli i mëposhtëm tregon se si të krahasosh dy receta nga uebsajte të ndryshme.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3.8-flash"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### QETËSI

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## Si funksionon

Vegla "Konteksti me URL" përdor një proces rikuperimi me dy hapa për të balancuar shpejtësinë, koston dhe qasjen në të dhënat më të fundit. Kur jep një URL, vegla
përpiqet fillimisht të marrë përmbajtjen nga një memorje specifike e indeksit të brendshëm. Kjo vepron si një
kesh i optimizuar në nivel të lartë. Nëse një URL nuk ofrohet në indeks (për shembull, nëse është një faqe shumë e re), vegla kthehet automatikisht për të bërë një marrje drejtpërdrejt.
Kjo qaset drejtpërdrejt në URL për të marrë përmbajtjen e saj në kohë reale.

## Kombinimi me vegla të tjera

Mund ta kombinosh veglën e kontekstit të URL-së me vegla të tjera për të krijuar flukse pune më të fuqishme.

[Modelet Gemini 3](#supported-models) mbështesin kombinimin e veglave të integruara (si p.sh. "Konteksti me URL") me veglat e personalizuara (thirrja e funksionit). Mëso më shumë në faqen e
[kombinimeve të veglave](https://ai.google.dev/gemini-api/docs/tool-combination?hl=sq).

### Argumentimi me kërkimin

Kur aktivizohen konteksti i URL-së dhe [Bazimi me "Kërko në Google"](https://ai.google.dev/gemini-api/docs/grounding?hl=sq), modeli mund të përdorë aftësitë e tij të kërkimit për të gjetur informacione përkatëse online dhe më pas të përdorë veglën e kontekstit të URL-së për të marrë një kuptim më të thelluar të faqeve që gjen. Kjo qasje është e fuqishme për kërkesat që kërkojnë kërkim të gjerë dhe analizë të thellë të faqeve specifike.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3.8-flash"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## Kuptimi i përgjigjes

Kur modeli përdor veglën e kontekstit të URL-së, përgjigjja përfshin një objekt të
`url_context_metadata`. Ky objekt liston URL-të nga të cilat modeli ka marrë përmbajtje dhe statusin e çdo përpjekjeje për marrje, gjë që është e dobishme për verifikimin dhe korrigjimin.

Më poshtë është një shembull i asaj pjese të përgjigjes
(pjesë të përgjigjes janë lënë jashtë për koncizitet):

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

Për detaje të plota për këtë objekt , shiko
[referencën e API-së të `UrlContextMetadata`](https://ai.google.dev/api/generate-content?hl=sq#UrlContextMetadata).

### Kontrollet e sigurisë

Sistemi kryen një kontroll të moderimit të përmbajtjes në URL për të konfirmuar që ato i plotësojnë standardet e sigurisë. Nëse URL-ja që ke dhënë dështon në këtë kontroll, do të marrësh një `url_retrieval_status` nga `URL_RETRIEVAL_STATUS_UNSAFE`.

### Numri i kodeve

Përmbajtja e marrë nga URL-të që specifikon në kërkesën tënde numërohet
si pjesë e kodeve hyrëse. Mund ta shikosh numrin e tokenëve për kërkesën tënde dhe përdorimin e veglave tek objekti [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=sq#UsageMetadata) i rezultatit të modelit. Më poshtë është një shembull i daljes:

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

Çmimi për kod varet nga modeli i përdorur. Shiko faqen e
[çmimeve](https://ai.google.dev/gemini-api/docs/pricing?hl=sq) për detaje.

## Modelet e mbështetura

| Modeli | Konteksti i URL-së |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=sq) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=sq) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=sq) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=sq) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=sq) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=sq) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=sq) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=sq) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=sq) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=sq) | ✔️ |

## Praktikat më të mira

- **Jep URL specifike**: Për rezultatet më të mira, jep URL të drejtpërdrejta për te përmbajtjet që dëshiron që të analizohen nga modeli. Modeli do të marrë vetëm përmbajtje nga URL-të që ti jep, jo përmbajtje nga lidhjet e mbivendosura.
- **Kontrollo për qasshmërinë**: Verifiko që URL-të që jep nuk të çojnë në faqe që kërkojnë një identifikim ose që janë pas një muri pagese.
- **Përdor URL-në e plotë**: Jep URL-në e plotë, duke përfshirë protokollin
  (p.sh. https://www.google.com në vend të thjesht google.com).

## Kufizimet

- Kufiri i kërkesave: Vegla mund të përpunojë deri në 20 URL për kërkesë.
- Madhësia e përmbajtjes së URL-së: Madhësia maksimale për përmbajtjen e marrë nga një URL e vetme është 34 MB.
- Qasshmëria publike: URL-të duhet të jenë të qasshme në mënyrë publike në ueb.
  Adresat e pritësit lokal (p.sh. localhost, 127.0.0.1), rrjetet private dhe shërbimet e tunelimit (p.sh. ngrok, pinggy) nuk mbështeten.

### Llojet e përmbajtjeve të mbështetura dhe të pambështetura

Vegla mund të nxjerrë përmbajtje nga URL-të me llojet e mëposhtme të përmbajtjeve:

- Tekst (text/html, application/json, text/plain, text/xml, text/css,
  text/javascript , text/csv, text/rtf)
- Imazh (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

Llojet e mëposhtme të përmbajtjes **nuk** mbështeten:

- Përmbajtja me mur pagese
- Videot në YouTube (Shiko
  [kuptimin e videos](https://ai.google.dev/gemini-api/docs/video-understanding?hl=sq#youtube) për të mësuar
  se si të përpunosh URL-të e YouTube)
- Skedarët e Google Workspace si "Dokumentet e Google" ose fletëllogaritëset
- Skedarët video dhe audio

## Çfarë ka më pas

- Eksploro [udhëzuesin për kontekstin me URL](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=sq#url-context)
  për më shumë shembuj.

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-13 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-13 UTC."],[],[]]
