---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=sq
fetched_at: 2026-11-02T07:11:42.489408+00:00
title: "Nd\u00ebrto aplikacione n\u00eb Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs?hl=sq)

Dërgo komente

# Ndërto aplikacione në Google AI Studio

Kjo faqe përshkruan se si të përdorësh Google AI Studio për të ndërtuar me shpejtësi (ose për të programuar me "vibe code") dhe për të prezantuar aplikacione që testojnë aftësitë më të fundit të Gemini, si p.sh. [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=sq) dhe [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=sq). Google AI Studio mbështet ndërtimin e **aplikacioneve të uebit** me ekzekutime të stivës së plotë dhe **aplikacioneve të integruara për Android** me Kotlin dhe Jetpack Compose - të gjitha nëpërmjet kërkesave me gjuhë natyrale.

## Fillo

Fillo programimin "vibe coding" në [modalitetin "Ndërto"](https://aistudio.google.com/apps?hl=sq) të Google AI Studio. Mund të fillosh të ndërtosh në disa mënyra:

- **Fillo me një kërkesë**: Në modalitetin "Ndërto", përdor kutinë e hyrjes për të futur një përshkrim të asaj që dëshiron të ndërtosh. Zgjidh "Çipat e IA-së" për të shtuar veçori specifike si p.sh. gjenerimi i imazheve ose të dhënat e Google Maps në kërkesën tënde. Mund të thuash edhe atë që dëshiron duke përdorur butonin e ligjërimit në tekst.
- **Butoni "Ndihem me fat"**: Nëse ke nevojë për një shkëndijë krijuese, përdor butonin "Ndihem me fat" dhe Gemini do të gjenerojë një kërkesë me një ide projekti për të të ndihmuar të fillosh.
- **Remikso një projekt nga galeria**: Hap një projekt nga [Galeria e aplikacioneve](https://aistudio.google.com/apps?source=showcase&hl=sq) dhe zgjidh **Kopjo aplikacionin**.
- **Importo një projekt nga GitHub**: Në modalitetin "Ndërto", zgjidh
  **Importo nga GitHub** nga menyja **Shto skedarë** (ikona +) në kutinë e hyrjes së kërkesës për të importuar kodin tënd ekzistues.

Pasi të ekzekutosh kërkesën, do të shikosh që gjenerohen kodi dhe skedarët e nevojshëm,
me një pamje paraprake të drejtpërdrejtë të aplikacionit tënd që shfaqet në anën e djathtë.

## Çfarë është krijuar?

Kur ekzekuton kërkesën tënde, AI Studio krijon një aplikacion të plotë. Mund të zgjedhësh të ndërtosh një **aplikacion uebi** ose një **aplikacion origjinal për Android** duke përdorur zgjedhësin e platformës.

Për **aplikacionet e uebit** (parazgjedhje), AI Studio krijon një mjedis me stivë të plotë që përfshin:

- **Në anën e klientit**: Një ndërfaqe uebi (React është parazgjedhja).
- **Në anën e serverit**: Një kohë ekzekutimi Node.js që lejon telefonata të sigurta API,
  lidhjet e bazës së të dhënave dhe përdorimin e paketës npm.

Për **aplikacionet për Android**, AI Studio gjeneron një projekt me Kotlin dhe Jetpack Compose
që mund ta shikosh paraprakisht në një imitues të bazuar në shfletues, ta instalosh në një pajisje fizike
dhe ta publikosh në "Dyqanin e Play" për testim. [Mëso më shumë rreth krijimit të aplikacioneve për Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=sq).

Mund ta shikosh kodin që gjenerohet duke zgjedhur skedën **Kodi** në panelin e shikimit paraprak në anën e djathtë. **Agjenti i Antigravity** menaxhon në mënyrë inteligjente
disa skedarë nëpër paketën tënde, duke u siguruar që ndryshimet të përhapen
si duhet.

### Agjenti i Antigravity

**Agjenti i Antigravity** është funksionaliteti kryesor i IA-së brenda [Google
Antigravity](https://antigravity.google?hl=sq) dhe tani komponentët kryesorë të
infrastrukturës së agjentit po mundësojnë përvojën e modalitetit Build në Google AI Studio. Ai shkon
përtej gjenerimit të thjeshtë të kodeve duke mbajtur kontekstin e të gjithë projektit tënd,
duke menaxhuar disa skedarë dhe duke kuptuar udhëzime komplekse për të ndërtuar aplikacione
të fuqishme me stivë të plotë.

Aftësitë kryesore përfshijnë:

- **Ndërgjegjësimi për kontekstin**: Mban kontekstin e kërkesave të mëparshme dhe gjendjeve të skedarëve.
- **Menaxhimi i disa skedarëve**: Menaxhon varësitë në disa skedarë.
- **Ekzekutimi i verifikuar**: Verifikon përditësimet e kodit për të reduktuar halucinacionet.

## Aftësi të stivës së plotë

Google AI Studio shkyç fuqinë e ekosistemit modern të uebit, duke të të lejuar të ndërtosh më shumë se thjesht prototipa në anën e klientit.

- **Koha e ekzekutimit në anën e serverit dhe npm**: Përdor bibliotekën e madhe të paketave npm. Agjenti do të identifikojë dhe instalojë automatikisht paketat sipas nevojës për aplikacionin tënd (p.sh. biblioteka specifike për vizualizimin e të dhënave ose klientët e API-së). Mund
  të kërkosh gjithashtu paketa specifike nëse dëshiron.
- **Menaxhimi i sekreteve**: Ruaj në mënyrë të sigurt çelësat API dhe sekretet në menynë **Cilësimet**. Këto janë të qasshme në kodin në anën e serverit, duke i mbajtur ato të sigurta nga ekspozimi në anën e klientit.
- **Me shumë lojtarë**: Ndërto përvoja bashkëpunuese në kohë reale drejtpërdrejt brenda AI Studio. Koha e ekzekutimit në anën e serverit menaxhon gjendjen dhe lidhjet
  e kërkuara që përdoruesit të ndërveprojnë së bashku.
- **Firebase Firestore and Authentication**: Siguro dhe konfiguro automatikisht Firebase, duke përfshirë bazën e të dhënave të Firestore (ruajtja e vazhdueshme e të dhënave) dhe Firebase Authentication (rrjedhat e identifikimit, veçanërisht "Identifikohu me Google"). Agjenti administron të gjithë procesin e konfigurimit dhe madje shkruan kodin në aplikacionin tënd për këto shërbime.
- **Integrimet e Google Workspace**: Lidh aplikacionin tënd me API-të e Google Workspace si Gmail, "Fletët", "Dokumentet", "Disku", "Kalendari" etj. AI Studio i administron
  të gjitha konfigurimet e OAuth automatikisht.

[Mëso më shumë rreth zhvillimit të aplikacioneve me stivë të plotë](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=sq)

### Aplikacionet për Android

Mund të ndërtosh gjithashtu aplikacione specifike për Android duke përdorur Kotlin dhe Jetpack Compose.
Shiko paraprakisht aplikacionin tënd në një imitues të Android bazuar në shfletues, instaloje atë në një pajisje fizike duke përdorur ADB-në në shfletues dhe publikoje në "Dyqanin e Play" për testim të brendshëm.

AI Studio integrohet gjithashtu me
[Firebase](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=sq)
për aplikacionet për Android për të ofruar automatikisht **Firebase AI Logic** dhe **Firebase
App Check** (për thirrje të sigurta të Gemini API nga ana e klientit pa ekspozuar çelësat e papërpunuar të API-së), si dhe **Cloud Firestore** dhe **Firebase Authentication**.

[Mëso më shumë rreth ndërtimit të aplikacioneve për Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=sq)

## Vazhdo të ndërtosh

Pasi Google AI Studio të gjenerojë kodin fillestar për aplikacionin tënd, mund të vazhdosh ta rafinosh atë:

### Ndërto në Google AI Studio

- **Përsërit me Gemini**: Përdor panelin e bisedës në **modalitetin "Ndërto"** për t'i kërkuar Gemini
  të bëjë modifikime, të shtojë veçori të reja ose të ndryshojë stilin.
- **Modifiko kodin drejtpërdrejt**: Hap **skedën "Kodi"** në panelin e pamjes paraprake për të bërë modifikime në çast.

### Zhvillo në nivel të jashtëm

Për flukse pune më të përparuara, mund ta sinkronizosh ose ta eksportosh kodin për të punuar në mjedisin tënd të preferuar:

- **Sinkronizo me GitHub**: Lidhe aplikacionin tënd me një depo të GitHub për të aktivizuar sinkronizimin dypalësh. Mund t'i dërgosh ndryshimet e kërkuara në AI Studio drejtpërdrejt në depon tënde me mesazhe të gjeneruara nga IA-ja ose të marrësh ndryshimet e bëra në nivel lokal në IDE ose nga anëtarët e ekipit përsëri në AI Studio. Menaxho statusin e sinkronizimit në çdo kohë në skedën **GitHub** te "Cilësimet".
- **Shkarko dhe zhvillo në nivel lokal**: Eksporto kodin e gjeneruar si një **skedar ZIP** dhe importoje atë në modifikuesin tënd të kodit.

## Veçoritë kryesore

Google AI Studio përfshin disa veçori për ta bërë procesin e ndërtimit intuitiv dhe vizual:

- **Krijo dhe përsërit në aplikacionet me stivë të plotë**: Krijo aplikacione me stivë të plotë me vetëm një kërkesë dhe përsërit nëpërmjet bisedës ose **modalitetit të shënimeve**. Modaliteti i shënimeve
  të lejon të theksosh çdo pjesë të ndërfaqes së përdoruesit të aplikacionit tënd dhe të përshkruash ndryshimin që dëshiron.
- **Ndaj dhe prezanto aplikacionin tënd**: Mund t'i ndash krijimet e tua me të tjerët për të bashkëpunuar ose për të prezantuar punën tënde. Kur ndan, thirrjet për API llogariten në kufijtë e tu të përdorimit. Nëse përdor modele me pagesë, mund të zbatohen kosto. Më pas, kur aplikacioni yt të jetë gati, shpërndaje në Cloud Run.
- **Galeria e aplikacioneve**: "Galeria e aplikacioneve" ofron një bibliotekë vizuale me ide për projekte.
  Mund të shfletosh se çfarë është e mundur me Gemini, të shikosh paraprakisht aplikacionet në çast,
  si dhe t'i remiksosh ato për t'i bërë të tuat.

## Shpërndaj ose arkivo aplikacionin tënd

Pasi aplikacioni yt të jetë gati, mund ta përdorësh atë:

- **Cloud Run**: Shpërndaje aplikacionin tënd si një shërbim të shkallëzueshëm.
  Mund të zbatohen çmime për [Google Cloud Run](https://cloud.google.com/run?hl=sq) bazuar në përdorimin. Për të mësuar më shumë rreth përdorimit, shiko
  [Përdorimi nga Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=sq).
- **GitHub**: Sinkronizo projektin tënd me një depo të re ose ekzistuese të GitHub
  për të menaxhuar kodin burimor ose për të bashkëpunuar me shokët e ekipit.

## Kufizimet

Ky seksion liston kufizimet aktuale të modalitetit të ndërtimit në Google AI Studio.

### Menaxhimi i çelësit API

Kur krijon një aplikacion të ri uebi që përdor Gemini API, AI Studio konfiguron automatikisht çelësin tënd të Gemini API si një sekret në mjedisin në anën e serverit të aplikacionit.
Mund ta shikosh dhe ta menaxhosh këtë çelës në panelin **Sekretet**.

- **Konfigurimi automatik**: `GEMINI_API_KEY` yt është konfiguruar për ty - nuk kërkohet asnjë konfigurim manual për të filluar ndërtimin.
- **Vetëm në anën e serverit**: Çelësat API injektohen në kohën e ekzekutimit në anën e serverit dhe nuk përfshihen asnjëherë në kodin në anën e klientit.
- **Aplikacionet ekzistuese**: Për aplikacionet e ndërtuara para datës 14 maj 2026, agjenti do të përmirësojë automatikisht integrimin e API-së së Gemini në qasjen e rekomanduar në anën e serverit herën tjetër që do të modifikosh veçoritë e Gemini të aplikacionit.

#### Aplikacionet për Android

Kur ndërton aplikacione për Android, AI Studio përdor
[Firebase AI Logic dhe Firebase App
Check](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=sq#firebase-integration) në vend të një çelësi
API të papërpunuar, kështu që kredencialet nuk integrohen asnjëherë në APK-në tënde.

### Vendosja jashtë Google AI Studio

- **Cloud Run**: Kur e dislokon në Cloud Run nga AI Studio, çelësi yt i API-së përfshihet në mënyrë të sigurt në mjedisin në anën e serverit. Aplikacioni i prezantuar do të përdorë
  çelësin tënd API për të gjitha thirrjet e Gemini API të përdoruesve.
- **Shkarkimi i ZIP**: Nëse e shkarkon aplikacionin tënd si skedar ZIP për ta ekzekutuar atë diku tjetër, do të duhet të konfigurosh ndryshoren e mjedisit `GEMINI_API_KEY` në mjedisin tënd të strehimit. Duke qenë se thirrjet e API-së së Gemini të aplikacionit tënd bëhen nga kodi në anën e serverit, çelësi nuk u ekspozohet përdoruesve fundorë.

### Gabim gjatë ndarjes së aplikacioneve

Nëse ndan aplikacionin tënd dhe përdoruesi yt fundor ndesh një gabim **403 Qasja e kufizuar** kur përdor URL-në e ndarë, kjo mund të jetë për shkak të një prej arsyeve të mëposhtme:

- **Shtesat e shfletuesit**: Shtesat e privatësisë si Privacy Badger mund të jenë duke bllokuar aplikacionin. Çaktivizo shtesën për të shmangur gabimin.
- **Probleme me ndërtimin**: Mund të ketë probleme me kodin aktual. Kërkoji agjentit të "rregullojë çdo problem me ndërtimin me kodin aktual" dhe më pas ndaje përsëri URL-në.

## Pyetjet e shpeshta

### Çfarë është "Ndërto në AI Studio"?

AI Studio Build është një platformë e projektuar për të të çuar nga një kërkesë e thjeshtë në një aplikacion të gatshëm për prodhim, të mundësuar nga IA-ja, duke përdorur Gemini. Përshkruaj se çfarë dëshiron të ndërtosh me një kërkesë dhe Gemini do të gjenerojë një aplikacion për ty. Mund
të eksplorosh gjithashtu galerinë tonë për të parë se çfarë është e mundur me Gemini API,
si dhe të remiksosh aplikacionet për t'i bërë të tuat.

### Si e administron Build çelësin tim të Gemini API?

Kur krijon një aplikacion uebi që përdor Gemini API, AI Studio konfiguron automatikisht çelësin tënd të Gemini API si një sekret në anën e serverit. Telefonatat e API-së së Gemini të aplikacionit tënd bëhen nga kodi në anën e serverit duke përdorur këtë çelës, kështu që ai nuk ekspozohet asnjëherë në shfletues. Mund ta shikosh çelësin tënd të API-së në panelin **Sekretet** te "Cilësimet". Për aplikacionet për Android, AI Studio përdor [Firebase AI Logic dhe Firebase App
Check](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=sq#firebase-integration) për të bërë telefonata të sigurta nga ana e klientit pa integruar një çelës API në binarin e aplikacionit.

### A ekspozohet çelësi im API kur ndaj aplikacione?

Jo. Çelësi yt i API-së ruhet si një sekret në anën e serverit dhe nuk përfshihet asnjëherë në kodin në anën e klientit. Kur ndan aplikacionin tënd, përdoruesit e tjerë mund ta përdorin atë, por ata nuk mund ta shikojnë çelësin tënd API.

Kur ndan aplikacionet e tua me të tjerët, thirrjet e API-së llogariten në kufijtë e përdorimit.
Nëse përdor modele me pagesë, mund të zbatohen kosto. AI Studio do të të njoftojë gjatë konfigurimit dhe para se të ndash nëse aplikacioni yt mund të ketë kosto.

### Kush mund t'i shikojë aplikacionet e mia?

Si parazgjedhje, aplikacioni yt është privat. Mund ta ndash aplikacionin tënd me përdorues të tjerë për t'i lënë ta përdorin atë. Përdoruesit me të cilët e ndan aplikacionin tënd mund ta shikojnë kodin e tij dhe ta degëzojnë atë për qëllimet e tyre. Nëse e ndan aplikacionin tënd me leje për modifikim, përdoruesit e tjerë mund ta modifikojnë kodin e aplikacionit tënd.

### A mund t'i ekzekutoj aplikacionet jashtë AI Studio?

Po. Mund ta prezantosh aplikacionin tënd në [Cloud Run](https://cloud.google.com/run?hl=sq) nga AI Studio, gjë që i jep aplikacionit tënd një URL publike me çelësin tënd të API-së të konfiguruar në mënyrë të sigurt në mjedisin në anën e serverit. Gjithashtu, mund ta shkarkosh aplikacionin tënd si një skedar ZIP dhe
ta strehosh diku tjetër — do të të duhet të caktosh ndryshoren e mjedisit `GEMINI_API_KEY`
në mjedisin tënd të strehimit. Duke qenë se thirrjet e Gemini API bëhen nga kodi në anën e serverit, çelësi yt mbetet i sigurt.

Për të mësuar më shumë rreth opsioneve të nxjerrjes, shiko [Nxjerrja nga Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=sq).

### A mund të zhvilloj aplikacione në nivel lokal me veglat e mia dhe më pas t'i ndaj ato këtu?

Po. Mund ta lidhësh aplikacionin tënd të AI Studio me një depo të GitHub për të zhvilluar
në nivel lokal duke përdorur modifikuesin e preferuar të kodit ose veglat CLI, për të dërguar ndryshimet e tua te
GitHub dhe më pas për t'i tërhequr ato përditësime drejtpërdrejt përsëri në AI Studio duke përdorur
skedën **GitHub** te "Cilësimet".

### Si mund të përdor një bazë të dhënash ose një hapësirë tjetër ruajtëse me aplikacionet e mia?

Aplikacionet e AI Studio janë aplikacione standarde që ekzekutohen në një kontejner të Cloud Run. Mund të përdorësh çdo zgjidhje për hapësirën ruajtëse që mund ta lidhësh nëpërmjet një rrjeti, për sa kohë që nuk ka një mur mbrojtës që parandalon qasjen nga një diapazon dinamik i adresave IP.

Ne po punojmë për të shtuar mbështetje të drejtpërdrejtë për hapësirën ruajtëse në të ardhmen, të cilën do të mund ta konfigurosh drejtpërdrejt brenda AI Studio.

### Si mund të qasem te mikrofoni, uebkamera dhe API-të e tjera të Navigator?

Për t'u siguruar që shikuesit janë në dijeni për përdorimin e uebkamerës ose pajisjeve të tjera nga një aplikacion, ne kërkojmë një konfirmim shtesë para se aplikacioni të mund të qaset në këto [API të Navigator](https://developer.mozilla.org/en-US/docs/Web/API/Navigator).
Krijuesit e aplikacioneve mund t'i shtojnë këto kërkesa për leje në skedarin `metadata.json` të aplikacionit të tyre. Për shembull:

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

Vlerat e mbështetura për `requestFramePermissions` janë një nëngrup i
[veçorive standarde të kontrolluara nga politika](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md).

### Si mund ta përdor GitHub me aplikacionet e mia?

AI Studio mbështet sinkronizimin dypalësh me GitHub:

- **Importo një depo**: Në modalitetin "Ndërto", zgjidh **Importo nga GitHub**
  nga menyja **Shto skedarë** (ikona +) në kutinë e hyrjes së kërkesës për të importuar
  kodin ekzistues.
- **Lidh një depo**: Te "Cilësimet", hap skedën **GitHub** për të krijuar një depo të re të GitHub nga aplikacioni yt ose lidhe me një depo ekzistuese.
- **Sinkronizimi dypalësh**: Transfero ndryshimet e kërkuara në AI Studio drejtpërdrejt në depon tënde me mesazhe të gjeneruara nga IA-ja ose tërhiq ndryshimet e bëra nga jashtë (si p.sh. modifikimet lokale të IDE-së ose kërkesat për tërheqje të anëtarëve të ekipit) përsëri në AI Studio.
- **Zgjidh konfliktet e bashkimit**: Nëse ndryshimet bien në konflikt gjatë sinkronizimit me GitHub, AI Studio ofron një dialog **Zgjidh konfliktet** me një shikues të diferencave krah për krah, duke të të lejuar të rishikosh diferencat dhe të zgjedhësh nëse do të mbash versionin e AI Studio apo të GitHub për çdo skedar në konflikt.

### A mund t'u jap përdoruesve të tjerë qasje për modifikim në aplikacionin tim?

AI Studio nuk mbështet modifikimin e drejtpërdrejtë bashkëpunues në kohë reale.
Megjithatë, mund të bashkëpunosh me shokët e ekipit duke e lidhur aplikacionin tënd me një depo të ndarë të GitHub. Anëtarët e ekipit mund të shtyjnë ndryshimet ose të hapin kërkesat për tërheqje në GitHub,
dhe ti mund t'i tërheqësh ato përditësime në AI Studio.

### Pse është raportuar aplikacioni im për shkelje të politikës?

Ne kemi sisteme që shqyrtojnë automatikisht aplikacionet për t'u siguruar që ato janë në përputhje me politikat tona. Nëse zbulojmë se një aplikacion shkel politikat tona, aplikacioni do të hiqet nga AI Studio. Shkeljet e politikës mund të përfshijnë, por nuk kufizohen në sa më poshtë:

- Aplikacionet që përmbajnë softuerë keqdashës, mashtrime ose imitime
- Aplikacionet që shfaqin ose shpërndajnë përmbajtje që shkel politikën për imazhet e abuzimit seksual të fëmijëve
- Aplikacione që shfaqin ose shpërndajnë përmbajtje që shkel politikën për ngacmimin
- Aplikacione që shfaqin ose shpërndajnë përmbajtje që shkel politikën për gjuhën e urrejtjes
- Aplikacione që shfaqin ose shpërndajnë përmbajtje që shkel politikën për trafikimin e qenieve njerëzore
- Aplikacionet që shfaqin ose shpërndajnë përmbajtje që shkel politikën për përmbajtjet e papërshtatshme seksuale
- Aplikacionet që shfaqin ose shpërndajnë përmbajtje që shkel politikën për dhunën dhe gjakderdhjen
- Aplikacionet që shfaqin ose shpërndajnë përmbajtje që shkel politikën për përmbajtjet e dëmshme ose të rrezikshme

Nëse aplikacioni yt është raportuar për një shkelje të politikës dhe beson se është një gabim, mund të dërgosh një apelim. Shkeljet e përsëritura të politikave tona mund të rezultojnë në mbylljen e qasjes sate në AI Studio.

### Cilat janë përgjegjësitë e mia si zhvillues i aplikacionit?

Si rikujtesë, si zotërues i aplikacionit tënd, ti je përgjegjës për sjelljen e tij dhe të gjitha të dhënat që ai administron. Kjo përfshin:

- **Përputhshmëria ligjore dhe të drejtat e palëve të treta:** Sigurimi që aplikacioni yt është në përputhje me të gjitha ligjet dhe rregulloret e zbatueshme dhe nuk shkel të drejtat e të tjerëve, duke përfshirë të drejtat e pronësisë intelektuale dhe të privatësisë.
- **Monitorimi i përmbajtjes:** Përputhja me kushtet shtesë mund të zbatohet për shërbimet e tjera të përdorura nga aplikacioni yt. Për shembull, ["Kushtet e shërbimit" të Google Cloud](https://cloud.google.com/terms?hl=sq), të zbatueshme për Firestore, kërkojnë që klientët që strehojnë përmbajtje të palëve të treta të publikojnë politika që përcaktojnë se cilat përmbajtje janë të ndaluara (p.sh. përmbajtjet e paligjshme) dhe të monitorojnë për praninë e këtyre përmbajtjeve të paligjshme.
- **Zbatimi i sigurt:** Zbatimi i masave mbrojtëse dhe veglave të nevojshme të moderimit për të parandaluar keqpërdorimin e aplikacionit tënd.

Ki parasysh [kufizimet e përdorimit](https://ai.google.dev/gemini-api/terms?hl=sq#use-restrictions)
në "Kushtet e shërbimit".

### Cilat kushte zbatohen për aplikacionet në galerinë e aplikacioneve në AI Studio?

[Kushtet shtesë të shërbimit të Gemini API](https://ai.google.dev/gemini-api/terms?hl=sq)
zbatohen për përdorimin e aplikacioneve të paraqitura në galerinë e aplikacioneve në AI Studio, përveçse nëse
përcaktohet ndryshe.

## Çfarë ka më pas

- [Developing Full-Stack Apps](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=sq) (ueb)
- [Ndërto aplikacione për Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=sq)
- Shiko shembujt te [Galeria e aplikacioneve](https://aistudio.google.com/apps?source=showcase&hl=sq).

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-26 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-26 UTC."],[],[]]
