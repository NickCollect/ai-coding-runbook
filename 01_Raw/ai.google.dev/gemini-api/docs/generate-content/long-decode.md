---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=sq
fetched_at: 2026-11-02T07:02:24.182593+00:00
title: "Dekodim i gjat\u00eb \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs/generate-content?hl=sq)

Dërgo komente

# Dekodim i gjatë

Dekodimi i gjatë lejon që Gemini 4 Argon të gjenerojë përtej kufirit të daljes së një kërkese të vetme për detyrat e arsyetimit të thellë, deri në dritaren e unifikuar të kontekstit me 1 milion kode (1 048 576 kode të ndara në hyrje, mendim dhe dalje).

Ndryshimi i vetëm i ID-së së modelit nuk e aktivizon dekodimin e gjatë. Pa konfigurim shtesë, dalja ndalon në 64K kode për telefonatat e transmetimit dhe 32K kode për telefonatat jo të transmetimit. Mënyra më e shpejtë për të aktivizuar dekodimin e gjatë është të përmirësosh Google GenAI SDK dhe të caktosh `max_output_tokens` më të madhe se 65 536. Ky udhëzues shpjegon se si funksionon dekodimi i gjatë, kur duhet ta përdorësh dhe si ta aktivizosh atë me `generateContent`.

## Për sa kohë funksionon deshifrimi

Një kërkesë e vetme transmetimi ose SDK gjeneron deri në 64 000 kode, dhe një kërkesë REST jo e transmetimit gjeneron deri në 32 000 kode. Kur një përgjigje ka nevojë për më shumë kode, modeli e gjeneron atë nëpër disa kërcime të kërkesave dhe përgjigjeve që secili vazhdon nga vendi ku ndaloi kërcimi i mëparshëm.

- **Kufiri i unifikuar i hyrjes dhe daljes së kodeve:** Hyrja, të menduarit, thirrjet e funksioneve dhe përgjigjja përfundimtare ndajnë një dritare me 1 milion kode. Rezultati mund të përdorë deri në 1 048 576 minus kodet e tua hyrëse.
- **Një kufi për çdo hap:** Një hap kthen deri në 65 536 output tokens. Kërkesat REST jo transmetuese kthejnë deri në 32,768.
- **Një sinjal vazhdimi:** Nëse modeli arrin kufirin dhe ka mbetur shenja, përgjigjja përfundon me `finish_reason: CONTINUATION` dhe një `continuation_token`.
- **Hapi tjetër:** Klienti dërgon përsëri të njëjtën kërkesë me kodin. Modeli vazhdon nga vendi ku ndaloi.
- **Një total për të gjitha kërcimet:** `max_output_tokens` cakton numrin total të kodeve të arsyetimit dhe të daljes për të gjitha kërcimet së bashku.
- **Një sinjal ndalimi:** Kur modeli përdor të gjithë `max_output_tokens`, përgjigjja përfundon me `finish_reason: MAX_TOKENS`.

Për problemet e vështira, një hop mund të shpenzojë të gjitha kodet e tij për të menduar në mënyrë të brendshme dhe të kthejë tekst bosh me një `continuation_token`. Kjo është normale dhe përgjigjja përfundimtare mbërrin në kërcimet e mëvonshme.

## Kufijtë e parazgjedhur të rezultateve

Pa dekodimin e gjatë, një kërkesë e vetme ndalon në këta kufij për kërkesë:

- **Kërkesat për transmetim dhe kërkesat jo për transmetim nëpërmjet Google GenAI SDK (`generate_content`):** Parazgjedhje në 64 000 token-ë të nxjerrjes.
- **Telefonatat e drejtpërdrejta REST pa transmetim (`generateContent`):** Parazgjedhje në 32 000 tokenë të rezultatit. Cilësimi i `max_output_tokens` më i madh se 32 768 në një telefonatë REST jo transmetuese pa një `continuation_token` kthen një gabim `400`.

| Si e quan modelin | Kufiri i daljes pa dekodim të gjatë | Dekodimi i gjatë në nisje | Çfarë të bësh |
| --- | --- | --- | --- |
| Google GenAI SDK, versioni më i fundit | 64 mijë | Po, SDK-ja vazhdon për ty | Cakto `max_output_tokens`. |
| Google GenAI SDK, version më i vjetër, jo transmetim | 64 mijë | Jo | Përmirëso SDK-në. |
| REST `streamGenerateContent` | 64 mijë | Po, me ciklin tënd | Shkruaj një cikël. Shiko [Opsionin 2](#option-2-loop). |
| REST `generateContent` | 32K | Po, me ciklin tënd | Shkruaj një lak. Shiko [Opsionin 2](#option-2-loop). |

## Kur të përdorësh dekodimin e gjatë

Shumica e kërkesave përfundojnë brenda kufirit të kërkesës së vetme (64 mijë kode për transmetimin dhe thirrjet e SDK-së ose 32 mijë kode për thirrjet REST jo të transmetimit). Përdor dekodimin e gjatë kur një përgjigje ka nevojë për më shumë tokenë të kombinuar të arsyetimit dhe të rezultateve sesa lejon një kërkesë e vetme. Rritja e `max_output_tokens` i jep modelit një kufi më të lartë për të arsyetuar për probleme të vështira, në vend që t'i bëjë përgjigjet standarde më të gjata.

| Ngarkesa e punës | Të përdoret dekodimi i gjatë? | Pse |
| --- | --- | --- |
| Matematikë e vështirë, shkencë, kërkime dhe prova formale | Po | Modeli mund të shpenzojë më shumë se 64 000 jetone për të eksploruar dhe kontrolluar arsyetimin e tij. |
| Detyrat më të vështira të kodimit dhe agjentike | Po | Disa detyra kërkojnë më shumë se 64 000 tokena arsyetimi dhe kodi në një përgjigje. Shumica e detyrave të kodimit dhe agjentike përfundojnë nën 64 KB. |
| Struktura vlerësimi që ndalojnë në kufirin e nxjerrjes | Po | Dekodimi i gjatë parandalon përgjigjet e ndërprera kur modeli shpenzon një kërkesë të plotë prej 64K ose 32K për të menduarit. |
| Biseda, pyetje-përgjigje, përmbledhje, klasifikim dhe nxjerrje | Jo | Këto detyra përfundojnë me më pak se 32 000 kode. |
| Kërkesat për një gjatësi fikse, si p.sh. "shkruaj një libër me 700 000 fjalë" | Jo | Modeli nuk ndjek objektivat e gjatësisë. |
| Agjentët që telefonojnë veglat në shumë kthesa të shkurtra | Jo | Çdo radhë është e shkurtër. Rezultatet e mëdha në çdo radhë e mbushin shpejt dritaren e unifikuar të hyrjes dhe daljes prej 1 milion tokenësh. |
| Kërkesat pranë kufirit të hyrjes prej 1 milion tokenësh | Jo | Dalja mund të përdorë vetëm 1 milion minus hyrjen tënde. |
| Kërkesat e ndjeshme ndaj vonesës | Jo | Dekodimi i gjatë mund të zgjasë për disa minuta. |

Caktimi i një vlere të lartë për `max_output_tokens` i jep modelit hapësirë për të menduar më gjatë për problemet e vështira, por modeli vendos ende se sa të shkruajë. Për të kontrolluar se sa përpjekje arsyetimi përdor modeli, cakto [`thinking_level`](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=sq).

## Aktivizo dekodimin e gjatë

Mund të ekzekutosh automatikisht dekodimin e gjatë me Google GenAI SDK (opsioni 1, i rekomanduar për shumicën e aplikacioneve) ose të shkruash ciklin tënd të vazhdimit (opsioni 2). Të dyja opsionet mbështesin dritaren kontekstuale të plotë me 1 milion tokenë.

|  | Opsioni 1: Google GenAI SDK (rekomandohet) | Opsioni 2: Cikli yt i transmetimit | Opsioni 2: Lak i yt jotransmetues |
| --- | --- | --- | --- |
| **Kush e fillon çdo hop** | SDK-ja. Ke caktuar `max_output_tokens`. | Kodi yt, në çdo pikë kontrolli ose pas një transmetimi të ndërprerë | Kodi yt, çdo 32 000 tokenë |
| **Tokenët për kërkesë** | 64 K për hop | 64K për transmetim, me një pikë kontrolli çdo 5K kode pas 32K | 32 000 për kërkesë |
| **Kufiri kohor për kërkesë** | 20 minuta | 20 minuta | 20 minuta |
| **Hapësira ruajtëse** | Nuk ka hapësirë ruajtëse në server | Nuk ka hapësirë ruajtëse në server | Nuk ka hapësirë ruajtëse në server |
| **Më të mirat për** | Shumica e aplikacioneve | Telefonuesit REST dhe pajisjet e personalizuara që transmetojnë | Struktura të thjeshta vlerësimi |

`continuation_token` i enkriptuar mbart gjendjen e modelit ndërmjet kërkesave, kështu që asgjë nuk ruhet në server.

### Opsioni 1: Përdor Google GenAI SDK (rekomandohet)

Në SDK-në më të fundit të IA-së gjeneruese të Google, `automatic_continuation` është e aktivizuar si parazgjedhje për telefonatat me transmetim dhe ato pa transmetim, kështu që nuk ka nevojë ta caktosh atë. Kur cakton `max_output_tokens` mbi kufirin për kërkesë, SDK-ja ekzekuton automatikisht kalimet e vazhdimit dhe kthen një përgjigje të kombinuar.

1. Përmirëso SDK-në.

   ### Python

   ```
   pip install -U "google-genai>=2.30.1"
   ```

   ### JavaScript

   ```
   npm install "@google/genai@>=2.29.1"
   ```
2. Cakto `max_output_tokens` më të madhe se 65 536.

   ### Python

   ```
   from google import genai
   from google.genai import types

   client = genai.Client()  # Reads GEMINI_API_KEY

   response = client.models.generate_content(
       model="gemini-4-argon",
       contents="Write a complete, rigorous proof of the prime number theorem.",
       config=types.GenerateContentConfig(
           max_output_tokens=262_144,  # Total thinking and output for all hops
           thinking_config=types.ThinkingConfig(thinking_level="high"),
           automatic_continuation=True,  # Default. Shown for clarity.
       ),
   )

   print(response.text)
   print("Finish reason:", response.candidates[0].finish_reason)
   print("Prompt size:", response.usage_metadata.initial_prompt_token_count)
   print("Billed tokens:", response.usage_metadata.total_token_count)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI, ThinkingLevel } from "@google/genai";

   const ai = new GoogleGenAI({}); // Reads GEMINI_API_KEY

   const response = await ai.models.generateContent({
     model: "gemini-4-argon",
     contents: "Write a complete, rigorous proof of the prime number theorem.",
     config: {
       maxOutputTokens: 262144, // Total thinking and output for all hops
       thinkingConfig: { thinkingLevel: ThinkingLevel.HIGH },
       automaticContinuation: true, // Default. Shown for clarity.
     },
   });

   console.log(response.text);
   console.log("Finish reason:", response.candidates?.[0]?.finishReason);
   console.log("Prompt size:", response.usageMetadata?.initialPromptTokenCount);
   console.log("Billed tokens:", response.usageMetadata?.totalTokenCount);
   ```

Ki parasysh këto pika:

- **Transmetimi:** `generate_content_stream` (Python) dhe `generateContentStream` (JavaScript) vazhdojnë gjithashtu për ty. Nëse një transmetim ndërpritet pas një pike kontrolli, SDK-ja vazhdon nga ajo pikë kontrolli.
- **Skadimet e kohës:** Skadimet e kohës dhe riprovat zbatohen për çdo kalim, jo për ekzekutimin e plotë.
- **Kontrolli manual:** Për ta ekzekutuar vetë luajtjen e përsëritur, cakto `automatic_continuation=False` (Python) ose `automaticContinuation: false` (JavaScript). Më pas ndiq opsionin 2.
- **Përdorimi:** Fushat e përdorimit shfaqin shumën e të gjitha kalimeve. Për të marrë madhësinë e kërkesës sate, lexo `initial_prompt_token_count`. Shiko [Numëro elementet](#count-tokens).

### Opsioni 2: Shkruaj ciklin tënd

Shkruaj ciklin tënd nëse telefonon REST drejtpërdrejt, përdor një gjuhë pa SDK-në më të fundit ose ke nevojë për kontroll të plotë. Mund t'u referohesh gjithashtu implementimeve tona të Google GenAI SDK në [Python](https://github.com/googleapis/python-genai/blob/v2.30.1/google/genai/models.py#L6111) dhe [JavaScript/TypeScript](https://github.com/googleapis/js-genai/blob/v2.29.1/src/models.ts#L88) si referencë.

Ndiq këto rregulla:

1. **Dërgo të njëjtën kërkesë në çdo hop.** Dërgo `contents`, `system_instruction`, `tools` dhe `generation_config` origjinale. Mbaje `max_output_tokens` njëlloj.
2. **Mos shto nxjerrje të pjesshme te `contents`.** `continuation_token` mbart gjendjen e modelit, duke përfshirë arsyetimin e tij.
3. **Dërgo vetëm kodin më të fundit.** Çdo kod përmban të gjithë progresin e mëparshëm.
4. **Vazhdo ndërkohë që `finish_reason` është `CONTINUATION`.** Ndalo për çdo arsye tjetër përfundimi.
5. **Bashko pjesët pas kërcimit të fundit.** Kombino pjesët nga të gjitha kalimet në një radhë të modelit për historikun e bisedës.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()  # Reads GEMINI_API_KEY
PROMPT = "Write a complete, rigorous proof of the prime number theorem."
parts = []
token = None

while True:
    response = client.models.generate_content(
        model="gemini-4-argon",
        contents=PROMPT,  # The original contents on every request
        config=types.GenerateContentConfig(
            max_output_tokens=262_144,  # The same total on every request
            thinking_config=types.ThinkingConfig(thinking_level="high"),
            automatic_continuation=False,  # You run the loop
            continuation_token=token,
        ),
    )
    candidate = response.candidates[0]
    if candidate.content and candidate.content.parts:
        parts.extend(candidate.content.parts)
    token = candidate.continuation_token
    if candidate.finish_reason != types.FinishReason.CONTINUATION or not token:
        break

print("".join(p.text for p in parts if p.text and not p.thought))
print("Finish reason:", candidate.finish_reason)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({}); // Reads GEMINI_API_KEY
const PROMPT = "Write a complete, rigorous proof of the prime number theorem.";
const parts = [];
let token = undefined;
let candidate = undefined;

while (true) {
  const response = await ai.models.generateContent({
    model: "gemini-4-argon",
    contents: PROMPT, // The original contents on every request
    config: {
      maxOutputTokens: 262144, // The same total on every request
      thinkingConfig: { thinkingLevel: ThinkingLevel.HIGH },
      automaticContinuation: false, // You run the loop
      continuationToken: token,
    },
  });
  candidate = response.candidates?.[0];
  if (candidate?.content?.parts) {
    parts.push(...candidate.content.parts);
  }
  token = candidate?.continuationToken;
  if (candidate?.finishReason !== "CONTINUATION" || !token) {
    break;
  }
}

console.log(parts.filter((p) => p.text && !p.thought).map((p) => p.text).join(""));
console.log("Finish reason:", candidate?.finishReason);
```

### QETËSI

```
# Hop 1: send the request with max_output_tokens.
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "Write a complete, rigorous proof of the prime number theorem."}]}],
    "generationConfig": {
      "maxOutputTokens": 262144,
      "thinkingConfig": {"thinkingLevel": "high"}
    }
  }'

# Hop 2: if finishReason is CONTINUATION, send the same request plus the token.
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "Write a complete, rigorous proof of the prime number theorem."}]}],
    "generationConfig": {
      "maxOutputTokens": 262144,
      "thinkingConfig": {"thinkingLevel": "high"}
    },
    "continuationToken": "TOKEN_FROM_HOP_1"
  }'
```

Një kërcim i shpenzuar tërësisht për të menduar kthen `text` bosh me `finishReason: "CONTINUATION"`. Trajtoje këtë si progres normal dhe kërko kërcimin vijues:

```
{
  "candidates": [{
    "content": {"role": "model", "parts": [{"text": ""}]},
    "finishReason": "CONTINUATION",
    "continuationToken": "CiQ4ZmQ3..."
  }],
  "usageMetadata": {
    "promptTokenCount": 142,
    "candidatesTokenCount": 0,
    "thoughtsTokenCount": 32768,
    "totalTokenCount": 32910
  }
}
```

**Ciklet e transmetimit** kanë nevojë për një rregull tjetër. Pas 32 768 kodeve të para, transmetimi dërgon një kod kontrolli çdo 5 000 kode. Mbaji pjesët e reja në një listë në pritje. Kur një pjesë ka një `continuation_token`, zhvendosi pjesët në pritje në daljen tënde të kryer dhe ruaj tokenin. Nëse transmetimi ndërpritet, hiqi pjesët në pritje dhe vazhdo nga tokeni i fundit. Nëse transmetimi ndërpritet para pikës së parë të kontrollit, dërgo përsëri kërkesën origjinale.

## Seti `max_output_tokens`

`max_output_tokens` cakton kufirin e kombinuar për të menduarit dhe daljen në të gjitha kërcimet. Ulja e tij nuk e bën modelin të mendojë në mënyrë më koncize, por në vend të kësaj e ndërpret përgjigjen më herët.

| Ngarkesa jote e punës | `max_output_tokens` e rekomanduar |
| --- | --- |
| Aplikacionet ekzistuese me një kufi më të ulët se 32 KB | Rrite në 32 768. |
| Detyrat e gjata të kodimit dhe agjentike | Fillo në 65 536. |
| Matematikë, shkencë, kërkime dhe vërtetime të vështira | Testo vlerat nga 262 144 deri në 1 048 576 minus kodet hyrëse. |

Për të përdorur më pak kode, ule `thinking_level`. Përdor `high` për detyrat më të vështira të arsyetimit. Përdor `medium` (parazgjedhja) për shumicën e punës së kodimit dhe agjentike. Përdor `low` për detyra më pak komplekse.

## Menaxho kërkesat afatgjata

Duke qenë se Gemini 4 Argon mendon më gjatë se modelet Gemini 3.x për problemet e vështira, duhet të rritësh kohët e pritjes të klientit në mënyrë që kërkesat e gjata të mos shkëputen herët.

- **Telefonatat jo transmetuese:** Serveri e mbyll lidhjen pas 10 minutash.
- **Telefonatat e transmetimit:** Serveri e mbyll transmetimin pas 20 minutash.
- **Kohët e pritjes për klientin:** Cakto kohën e pritjes për leximin e HTTP-së në 20 minuta. Një skadim kohe prej 3 ose 5 minutash e ndalon kërkesën herët.

Në Python, cakto kohën e pritjes për klientin në milisekonda:

```
client = genai.Client(http_options=types.HttpOptions(timeout=1_200_000))  # 20 minutes
```

Për punët që klienti yt i kërkon, Interactions API ekzekuton dekodimin e gjatë në server. Shiko [ekzekutimin në sfond](https://ai.google.dev/gemini-api/docs/background-execution?hl=sq).

## Vazhdo kur modeli të përdorë të gjitha xhetonet e nxjerra

Kur një përgjigje mbaron me `MAX_TOKENS`, ajo përfshin ende një `continuation_token`. Ke dy zgjedhje:

- **Vazhdo:** Dërgo të njëjtën kërkesë me kodin dhe një `max_output_tokens` më të lartë. Vlera duhet të jetë mbi numrin e tokenëve të përdorur deri tani. Në rast të kundërt, API-ja kthen një gabim 400.
- **Fillo përsëri:** Dërgo kërkesën origjinale me një `max_output_tokens` më të lartë dhe pa kod. Ti paguan për të dyja dërgesat.

## Numëro tokenët

Me vazhdimin automatik, `usage_metadata` raporton totalet në të gjitha kalimet. SDK-ja mbledh çdo fushë numërimi: `prompt_token_count`, `cached_content_token_count`, `candidates_token_count`, `thoughts_token_count` dhe `total_token_count`.

`prompt_token_count` mbledh token-at e hyrjes të çdo kërcimi. Çdo kërcim e dërgon kërkesën tënde plus gjithçka që është gjeneruar deri tani përsëri te modeli si hyrje, kështu që të njëjtët kode numërohen përsëri në çdo kërcim të mëvonshëm. Për shembull, me Google GenAI SDK, një kërkesë me 1 000 dërgime që prodhon 200 000 dërgime të të menduarit dhe të nxjerrjes kërkon katër hapa:

| Hop | Hyrja u dërgua te modeli | Tokenët e hyrjes |
| --- | --- | --- |
| 1 | Kërkesa | 1 000 |
| 2 | Kërko dhe hidh 1 | 66,536 |
| 3 | Kërkesa + hops 1 dhe 2 | 132,072 |
| 4 | Kërkesa + 1 deri në 3 kalime | 197 608 |
| **Totali** |  | **397 216** |

`prompt_token_count` raporton rreth 397 000 kode (me hyrjet e përsëritura të kërcimeve të zbritura automatikisht me 95% nga ruajtja e fshehtë e të dhënave) dhe `total_token_count` raporton rreth 597 000 kode, edhe pse madhësia aktuale e kontekstit është vetëm rreth 201 000 kode: kërkesa me 1000 kode plus 200 000 kode për të menduarit dhe daljen. Një cikël REST pa transmetim përdor 32 000 kapërcime, kështu që duhen shtatë kapërcime për të njëjtin rezultat dhe raporton 695 128 jeto hyrëse.

| Si e quan modelin | Çfarë shfaq `usage_metadata` | Për koston | Për madhësinë e kërkesës |
| --- | --- | --- | --- |
| Google GenAI SDK, vazhdimi automatik (parazgjedhja) | Totalet në të gjitha ndalesat | Lexo fushat e përdorimit siç janë. | Lexo `usage_metadata.initial_prompt_token_count` (Python) ose `usageMetadata.initialPromptTokenCount` (JavaScript). |
| SDK me `automatic_continuation=False` ose REST | Një kërcim për përgjigje | Shto çdo fushë nëpër kërcime. | Lexo `prompt_token_count` nga hopi i parë. |

`prompt_token_count` dhe `total_token_count` janë shuma e çdo kërcimi, jo madhësia e kontekstit tënd. Mos i përdor ato për të vendosur se kur duhet të përmbledhësh ose të shkurtosh historikun e bisedave (kompaktimi i kontekstit) ose për të zbatuar një kufi të kontekstit. Për të përllogaritur madhësinë e kontekstit, shto madhësinë e kërkesës sate nga tabela te `candidates_token_count` dhe `thoughts_token_count`.

Përditëso kuadrin e agjentit, veglën e vlerësimit ose ndërmjetësin para se të ekzekutosh deshifrimin e gjatë:

- **Agjentët dhe veglat e vlerësimit:** Nëse kodi yt e ngjesh kontekstin ose e ndalon ekzekutimin në një kufi të shenjave, përdor `initial_prompt_token_count` (ose `prompt_token_count` e hapit të parë në REST) në vend të `prompt_token_count` të mbledhur. Përgjigjet që përfundojnë në një hop raportojnë të njëjtën vlerë në të dyja fushat, kështu që testet e shkurtra nuk e shfaqin problemin.
- **Proksitë dhe portat që thërrasin REST:** Çdo përgjigje REST raporton vetëm kërcimin e vet. Shto çdo fushë nëpër transferta për koston dhe mbaj `promptTokenCount` e transfertës së parë si madhësinë e kërkesës. Në rast të kundërt, përdoruesit e tu shohin numra të ndryshëm nga ata që shohin përdoruesit e SDK-së për të njëjtën kërkesë.
- **Regjistrat dhe përgjigjet e serializuara:** SDK-ja llogarit `initial_prompt_token_count` në klient. Nuk është në përgjigjen REST ose në daljen JSON të SDK-së, si p.sh. `model_dump()`. Ruaje si një vlerë të veçantë nëse të nevojitet më vonë.

Nëse transmeton në luajtjen tënde të përsëritur, `usage_metadata` është kumulative brenda çdo transmetimi. Mbaj vetëm vlerën e fundit të çdo transmetimi, më pas shto vlerat nëpër hop-e.

## Kupto faturimin

Ti paguan për çdo kod në çdo hap, duke përfshirë hapat që përmbajnë vetëm të menduarit.

- **Zbritja e memories specifike:** Ruajtja specifike në memorie ul me 95% hyrjen e përsëritur në çdo hap. Hyrja e ruajtur në memorien specifike kushton 0,10 USD për 1 milion tokenë në vend të 2,00 USD gjatë periudhës prezantuese.
- **Skadimi i memorjes specifike:** Memorja specifike skadon pas 15 deri në 20 minuta pa përdorim. Një pauzë e gjatë mes kërcimeve tarifon përsëri tarifën e plotë të hyrjes.
- **Hopet e dështuara pa transmetim:** Ti paguan vetëm kur përfundon një përgjigje. Një kërkesë e dështuar ose e lëshuar kushton $0.
- **Transmetimet e ndërprera:** Një transmetim që ndërpritet para 32 000 kodeve kushton 0 dollarë. Pas kësaj, ti paguan deri te tokeni i pikës së fundit të kontrollit, sepse mund të vazhdosh nga ai.

## Zgjidhja e problemeve

| Simptoma | Shkaku dhe rregullimi |
| --- | --- |
| Dalja ndalon në 64K ose 32K me `CONTINUATION` | Modeli ka kode të mbetura, por asgjë nuk e vazhdoi kërkesën. Përmirëso SDK-në ose shto një lak. |
| Dalja ndalon në 64K ose 32K me `MAX_TOKENS` | `max_output_tokens` nuk është caktuar ose është shumë i ulët. Caktoje në më shumë se 65 536. |
| Tekst bosh me "`MAX_TOKENS`" | Modeli përdori të gjitha kodet në arsyetim. Ngri `max_output_tokens` ose ul `thinking_level`. |
| 400: "Kodi i vazhdimit ka përdorur tashmë kodet e daljes..." | `max_output_tokens` nuk është mbi numrin e përdorur të token-ëve deri tani. Ngrije. |
| Gabim për `thinking_level: "minimal"` ose për `thinking_budget` me `thinking_level` | Gemini 4 Argon nuk e mbështet `minimal`. Përdor `low`, `medium` ose `high`. Cakto `thinking_level` ose `thinking_budget`, jo të dyja. |
| Paralajmërim për: `thinking_budget`, `temperature`, `top_p` ose `top_k` | Gemini 4 Argon i shpërfill ose i hartëzon këto fusha. Përdor `thinking_level` dhe hiq parametrat e kampionimit. |
| Kërkesa përfundon pas 3 ose 5 minutash | Koha e pritjes e klientit është shumë e shkurtër. Caktoje në 20 minuta. |
| Ngjeshja e kontekstit fillon shumë herët | Struktura lexon hyrjen e mbledhur. Lexo `initial_prompt_token_count` më mirë. |

## Kufizimet

- **Pika fundore e përputhshmërisë me OpenAI:** Dekodimi i gjatë nuk ofrohet. Dalja ndalon në kufirin për kërkesë.
- **SDK-të më të vjetra:** Versionet nën minimumet në shënim nuk vazhdojnë automatikisht.
- **Gjatësia:** Modeli nuk ndjek objektivat për numrin e tokenëve ose numrin e fjalëve.

## Listë kontrolli

- Përmirëso SDK-në e Google GenAI në versionin minimal.
- Cakto `max_output_tokens` më të madhe se 65 536.
- Përdor `thinking_level` (`low`, `medium` ose `high`), jo `thinking_budget`.
- Cakto kohët e pritjes për leximin e HTTP-së në 20 minuta.
- Përdor `initial_prompt_token_count` për madhësinë dhe kompaktësimin e kontekstit.
- Ekzekuto një kërkesë si test para një vlerësimi të madh.

## Hapat e radhës

- [Çfarë ka të re në Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=sq)
- [Po mendoj](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=sq)
- [Numërimi i tokenëve](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=sq)

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-13 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-13 UTC."],[],[]]
