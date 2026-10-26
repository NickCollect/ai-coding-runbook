---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=sq
fetched_at: 2026-10-26T05:47:01.055008+00:00
title: "P\u00ebrdorimi i veglave me Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs?hl=sq)

Dërgo komente

# Përdorimi i veglave me Gemini API

Veglat i zgjerojnë aftësitë e modeleve të Gemini, duke bërë të mundur që ato të ndërmarrin veprime në botë, të qasen në informacione në kohë reale dhe të kryejnë detyra komplekse llogaritëse. Modelet mund të përdorin veglat si në ndërveprimet standarde kërkesë-përgjigje, ashtu edhe në seancat e transmetimit në kohë reale duke përdorur [Live API](https://ai.google.dev/gemini-api/docs/live-tools?hl=sq).

Veglat janë aftësi specifike (si p.sh. "Kërko në Google" ose "Ekzekutimi i kodit") që një model mund t'i përdorë për t'iu përgjigjur pyetjeve. Gemini API ofron një paketë veglash të integruara plotësisht të menaxhuara ose mund të përcaktosh vegla të personalizuara duke përdorur [Thirrjen e funksionit](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq).

Për të ndërtuar sisteme me shumë hapa dhe të orientuara drejt objektivave, shiko [Përmbledhjen e agjentëve](https://ai.google.dev/gemini-api/docs/agents?hl=sq).

## Veglat e integruara që ofrohen

| Vegla | Përshkrimi | Rastet e përdorimit |
| --- | --- | --- |
| ["Kërko në Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=sq) | Bazo përgjigjet në ngjarjet aktuale dhe faktet nga uebi për të reduktuar halucinacionet. | Përgjigjja e pyetjeve për ngjarjet e fundit, verifikimi i fakteve me burime të ndryshme. |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=sq) | Krijo asistentë që e dinë vendndodhjen që mund të gjejnë vende, të marrin udhëzime dhe të ofrojnë kontekst të pasur lokal. | Planifikimi i itinerareve të udhëtimeve me shumë ndalesa, gjetja e bizneseve lokale bazuar në kriteret e përdoruesit. |
| [Ekzekutimi i kodit](https://ai.google.dev/gemini-api/docs/code-execution?hl=sq) | Lejo që modeli të shkruajë dhe të ekzekutojë kodin në Python për të zgjidhur probleme matematikore ose për të përpunuar të dhënat me saktësi. | Zgjidhja e ekuacioneve komplekse matematikore, përpunimi dhe analizimi i të dhënave të tekstit me saktësi. |
| [Konteksti i URL-së](https://ai.google.dev/gemini-api/docs/url-context?hl=sq) | Drejtoje modelin që të lexojë dhe të analizojë përmbajtje nga faqe uebi ose dokumente specifike. | Përgjigjja e pyetjeve bazuar në URL ose dokumente specifike, nxjerrja e informacioneve nëpër faqe të ndryshme uebi. |
| [Përdorimi i kompjuterit (versioni paraprak)](https://ai.google.dev/gemini-api/docs/computer-use?hl=sq) | Aktivizo Gemini për të shikuar një ekran dhe për të gjeneruar veprime për të ndërvepruar me ndërfaqet e përdoruesit të shfletuesit të uebit (ekzekutimi në anën e klientit). | Automatizimi i flukseve të përsëritura të punës bazuar në ueb, duke testuar ndërfaqet e përdoruesve të aplikacioneve të uebit. |
| [Kërkimi i skedarëve](https://ai.google.dev/gemini-api/docs/file-search?hl=sq) | Indekso dhe kërko dokumentet e tua për të aktivizuar Retrieval Augmented Generation (RAG). | Kërkimi në manualet teknike, përgjigjja e pyetjeve për të dhënat e pronësisë. |

Shiko [faqen e "Çmimeve"](https://ai.google.dev/gemini-api/docs/pricing?hl=sq#pricing_for_tools) për detaje
për kostot në lidhje me veglat specifike.

## Si funksionon ekzekutimi i veglave

Veglat e lejojnë modelin të kërkojë veprime gjatë një bisede. Rrjedha ndryshon në varësi të faktit nëse vegla është e integruar (menaxhuar nga Google) ose e personalizuar (menaxhuar nga ti).

### Rrjedha e veglës së integruar

Për veglat e integruara (Google Search, Google Maps, URL Context, File Search,
Code Execution), i gjithë procesi ndodh brenda një thirrjeje të API-së:

1. **Ti** dërgon një kërkesë: "Cila është rrënja katrore e çmimit më të fundit të aksioneve të GOOG?"
2. **Gemini** vendos që ka nevojë për vegla dhe i ekzekuton ato në serverët e Google
   (p.sh. kërkon për çmimin e aksioneve dhe më pas ekzekuton kodin në Python për të llogaritur rrënjën katrore).
3. **Gemini** dërgon mbrapsht përgjigjen përfundimtare të bazuar në rezultatet e veglës.

### Fluksi i veglës së personalizuar (thirrja e funksionit)

Për veglat e personalizuara dhe "Përdorimin e kompjuterit", aplikacioni yt administron ekzekutimin:

1. **Ti** dërgon një kërkesë bashkë me deklaratat e funksioneve (veglave).
2. **Gemini** mund të dërgojë mbrapsht JSON të strukturuar për të thirrur një funksion specifik
   (për shembull, `{"name": "get_order_status", "args": {"order_id": "123"}}`),
   gjithmonë me një `id` unike.
3. **Ti** ekzekuton funksionin në aplikacionin ose mjedisin tënd.
4. **Ti** dërgon rezultatet e funksionit, me të njëjtin `id` si thirrja e funksionit, mbrapsht te Gemini.
5. **Gemini** i përdor rezultatet për të gjeneruar një përgjigje përfundimtare ose një thirrje tjetër vegle.

Mëso më shumë tek [Udhëzuesi për thirrjen e funksionit](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq).

### Kombinimi i fluksit të veglave të integruara dhe të personalizuara

Për kërkesat që kombinojnë veglat e integruara dhe veglat e personalizuara (thirrjet e funksioneve), modeli përdor [qarkullimin e kontekstit të veglës](https://ai.google.dev/gemini-api/docs/tool-combination?hl=sq) për të koordinuar ekzekutimin në mjedise të ndryshme:

1. **Ti** dërgon një kërkesë dhe deklaron veglat e integruara dhe funksionet e personalizuara që dëshiron të aktivizosh, duke caktuar një flamur për të aktivizuar mbështetjen për kombinimin.
2. **Gemini** ekzekuton veglat e integruara dhe i jep përparësi përdoruesit nëse gjenerohen thirrje të funksionit në anën e klientit (se cila ekzekutohet e para varet nga kërkesa dhe nga ajo që vendos modeli). Ai dërgon përsëri një përgjigje me:
   - Konfirmimi i thirrjes së mjetit
   - Rezultatet e përgjigjes së veglës (kjo mund të vijë pas JSON nëse modeli ka gjeneruar dy thirrje paralele të funksionit)
   - JSON i strukturuar për të thirrur funksionin tënd
   - Nënshkrimet e enkriptuara të mendimit për të ruajtur kontekstin
3. **Ti** ekzekuton funksionin në aplikacionin ose mjedisin tënd.
4. **Ti** kthen të gjitha pjesët e përgjigjes së Gemini, si dhe rezultatet e thirrjes së funksionit tënd.
5. **Gemini** gjeneron përgjigjen përfundimtare duke përdorur të gjithë kontekstin e kombinuar.

Lexo [Udhëzuesin për kombinimin e veglave](https://ai.google.dev/gemini-api/docs/tool-combination?hl=sq) për të mësuar
se si të aktivizosh mbështetjen për kombinimin e veglave të integruara dhe të personalizuara dhe shembuj të
qarkullimit të kontekstit.

## Rezultatet e strukturuara kundrejt thirrjes së funksionit

Gemini ofron dy metoda për gjenerimin e rezultateve të strukturuara. Përdor [Thirrjen
e funksionit](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq) kur modeli duhet të kryejë një
hap të ndërmjetëm duke u lidhur me veglat ose sistemet e tua të të dhënave. Përdor
[Daljet e strukturuara](https://ai.google.dev/gemini-api/docs/structured-output?hl=sq) kur ke rreptësisht nevojë që përgjigjja përfundimtare e modelit të respektojë një skemë specifike, si p.sh. për paraqitjen e një ndërfaqeje të personalizuar përdoruesi.

## Rezultate të strukturuara me vegla

Mund të kombinosh [Rezultatet e strukturuara](https://ai.google.dev/gemini-api/docs/structured-output?hl=sq) me veglat e integruara për t'u siguruar që përgjigjet e modelit të bazuara në të dhëna ose llogaritje të jashtme të ndjekin ende një skemë strikte.

Shiko [Rezultatet e strukturuara me veglat](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe&hl=sq#tools)
për shembuj kodesh.

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-15 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-15 UTC."],[],[]]
