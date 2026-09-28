---
source_url: https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=tr
fetched_at: 2026-09-28T06:30:57.670998+00:00
title: "Lyria istem rehberi \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Lyria istem rehberi

Gemini API, Lyria ile müzik üretmek için iki yöntem sunar:

- **Lyria 3.5 ve Lyria 3 Clip**: Şarkı sözleri ve vokaller içeren 30 saniyelik klipler veya tam uzunluktaki şarkılar için akışsız üretim. [Lyria 3.5 ile müzik üretme](https://ai.google.dev/gemini-api/docs/music-generation?hl=tr) başlıklı makaleyi inceleyin.
- **Lyria RealTime**: WebSocket'ler üzerinden anlık, etkileşimli müzik yayını ve canlı yönlendirme. [Lyria RealTime ile gerçek zamanlı müzik üretme](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=tr) başlıklı makaleyi inceleyin.

Her iki model de açıklayıcı metin istemlerine, müzik terminolojisine ve yapısal talimatlara yanıt verir. Bu kılavuzda, hem toplu oluşturma hem de anlık yönlendirme için etkili istemlerin nasıl yazılacağı açıklanmaktadır.

## İstemlerle ilgili temel bilgiler

İsteminiz kısa bir ifade olabilir:

```
A folk song about cute cats avoiding puddles, female vocals, acoustic guitar, sound of rain
```

Veya yapılandırılmış, ayrıntılı bir açıklama:

```
A 1980s-style synth-pop track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. The song should have a retro-futuristic feel with modern production polish. Upbeat tempo around 120 BPM, clear verse-chorus structure, and a memorable instrumental hook. The lyrics describe getting ready for a party.
```

Hem kısa hem de ayrıntılı istemler iyi sonuçlar verir. Modeli istediğiniz sese yönlendirmek için aşağıdaki stratejileri kullanın.

## Tür ve stil

İsteminize birincil türle başlayın. Benzersiz karışımlar oluşturmak için türleri birleştirebilirsiniz:

- Metal ve hip-hop'ın birleşimi
- Opera vokalleriyle birleşen death metal
- Karanlık elektronik drone öğeleri içeren klasik oda müziği
- Europop ile karıştırılmış modern elektronik dans müziği (EDM)

Ayrıca bir müzik dönemi veya bölgesel varyant da belirtebilirsiniz:

- 1990'ların başlarındaki boom-bap hip-hop
- 1960'ların Fransız yé-yé pop müziği
- 1980'lerin post-punk ve new wave müzikleri
- 2000'lerin popüler R&B müzikleri
- Berlin minimal tekno veya Bay Area hyphy

### Tür anahtar kelimeleri

Lyria 3.5 ve Lyria RealTime istemlerinizde şu tür terimlerini kullanın:

- **Elektronik ve Dans**: `Acid House, Breakbeat, Chillout, Chiptune, Deep House, Drum & Bass, Dubstep, EDM, Electro Swing, Glitch Hop, Hyperpop, Minimal Techno, Moombahton, Psytrance, Synthpop, Techno, Trance, Trip Hop, Vaporwave`
- **Hip-Hop ve R&B**: `808 Hip Hop, Boom-Bap, Contemporary R&B, G-funk, Grime, Lo-Fi Hip Hop, Neo-Soul, New Jack Swing, Trap Beat`
- **Rock ve Alternatif**: `Alternative Country, Blues Rock, Classic Rock, Funk Metal, Garage Rock, Indie Folk, Indie Pop, Post-Punk, 60s Psychedelic Rock, Shoegaze, Surf Rock`
- **Caz, Soul ve Funk**: `Acid Jazz, Afrobeat, Bossa Nova, Disco Funk, Funk, Jazz Fusion, Latin Jazz`
- **Folk ve Geleneksel**: `Bengal Baul, Bhangra, Bluegrass, Celtic Folk, Cumbia, Indian Classical, Irish Folk, Merengue, Polka, Reggae, Reggaeton, Renaissance Music, Salsa`
- **Klasik ve Akustik**: `Baroque, Orchestral Score, Piano Ballad`

## Enstrümanlar ve dokular

Lyria, istenen tür için uygun enstrümanı otomatik olarak seçer. Belirli enstrümanlar veya alışılmadık kombinasyonlar istiyorsanız bunları açıkça belirtin:

```
A dance track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. A saxophone solo enters during the bridge.
```

Enstrümanların ruh halini ve dokuyu belirlemek için nasıl ses çıkardığını ve etkileşime girdiğini açıklayın:

- Net ve sıkı hi-hat'lerin arasından geçen bozuk bir 303 bas hattı
- Sıcak, analog synth pad'ler, kuru, samimi bir akustik gitarın altında yükseliyor.
- Uzaktan gelen, yankı efektli vokallerle birlikte, birden fazla kat fuzz gitarla oluşturulmuş bir ses duvarı

### Enstrüman anahtar kelimeleri

- **Klavyeler ve Synthesizer'lar**: `Buchla Synths, Clavichord, Dirty Synths, Harpsichord, Mellotron, Moog Oscillations, Ragtime Piano, Rhodes Piano, Smooth Pianos, Spacey Synths, Synth Pads`
- **Bas ve Davul**: `303 Acid Bass, 808 Hip Hop Beat, Boomy Bass, Conga Drums, Drumline, Funk Drums, Precision Bass, Tabla, TR-909 Drum Machine`
- **Gitarlar ve Teller**: `Banjo, Balalaika, Bouzouki, Cello, Charango, Dulcimer, Fiddle, Flamenco Guitar, Guitar, Harp, Koto, Lyre, Mandolin, Pipa, Shamisen, Shredding Guitar, Sitar, Slide Guitar, Viola Ensemble, Warm Acoustic Guitar`
- **Üflemeli ve Bakır**: `Alto Saxophone, Bagpipes, Bass Clarinet, Didgeridoo, Harmonica, Ocarina, Trumpet, Tuba, Woodwinds`
- **Vurmalı çalgılar**: `Bongos, Djembe, Glockenspiel, Hang Drum, Kalimba, Maracas, Marimba, Mbira, Steel Drum, Vibraphone`

## Şarkı yapısı ve zamanlama

Lyria 3.5'te şarkı ilerlemesini etiketleri veya okları kullanarak tanımlayın:

- `[Intro] -> [Verse 1] -> [Chorus] -> [Verse 2] -> [Chorus] -> [Bridge] -> [Outro]`
- Sakin bir piyano girişiyle başlayın, enerjik bir verse ile devam edin, bir anlık sessizlik için duraklayın ve ardından nakaratla patlayın.

Enerji dinamiklerini ve geçişlerini yönlendirebilirsiniz:

- Nakarat öncesi bölümle gerilimi artırın, ardından patlayıcı bir nakarattan önce sessizliğe geçin.
- Şarkı boyunca kademeli olarak artan, her bölüme bir enstrüman eklenen crescendo
- Köprüden sonra aniden durulur ve a cappella koro başlar.

Ayrıca belirli zamanlama işaretleri de isteyebilirsiniz:

- 12. saniyede ritmin düşeceği bir bölüm oluşturun.
- Vokal örneği her 4 ölçüde bir tekrarlanır
- Koro 22. saniyede başlıyor

## Şarkı sözleri ve vokaller

Lyria 3.5, varsayılan olarak şarkı sözleri içeren vokal parçaları üretir. Kendi şarkı sözlerinizi sağlayabilir, modelden şarkı sözü oluşturmasını isteyebilir veya enstrümantal parça isteğinde bulunabilirsiniz.

### Kendi şarkı sözlerinizi kullanma

Şarkı sözlerinizi doğrudan `Lyrics:` başlığının altındaki isteme ekleyin. Vokal sunumunu yönlendirmek için her bölümü etiketleyin:

```
Lyrics:

[Intro]
Ooooh, yeah

[Verse 1]
Early morning rain on the window pane
City lights wash away the pain
Walking down this empty street again

[Chorus]
We keep moving on (moving on)
Until the morning light
Everything will be alright
```

Geri vokaller, ekolar veya doğaçlamalar için parantez kullanın (ör. `(moving on)`).

### Oluşturulan şarkı sözlerini yönlendirme

Lyria 3.5'ten şarkı sözü yazmasını isterken anlatıyı, duyguyu veya anahtar ifadeleri özetleyin:

```
The lyrics describe driving down the Pacific Coast Highway at sunset. The mood is nostalgic and reflective. Include an uplifting, anthemic chorus about second chances and starting over.
```

Elektronik ve dans türleri için kısa ve tekrarlayan vokal bölümleri isteyin:

```
An upbeat dance-pop track with a repetitive, high-energy vocal hook: "Feel the rhythm all night long."
```

### Vokal sunumu ve şarkıcı profilleri

Cinsiyeti, vokal aralığını ve tınıyı belirterek daha iyi sonuçlar elde edin:

- **Kadın Soprano**: Çevik ve yükselen bir performansla net, kristal tını. Hafif ve nefesli dokular oluşturabilen parlak ton.
- **Kadın Alto**: Zengin, sıcak ve kısık alt aralık. Duygusal ve rezonanslı bir göğüs sesiyle dumanlı bir tını.
- **Erkek Tenor**: Parlak, keskin ve enerjik. Yoğun mikslerde öne çıkan, yüksek belting gücüne sahip genç bir tını.
- **Erkek Bariton**: Derin, kadife gibi pürüzsüz, sıcak, rahatlatıcı ve yumuşak bir ses.
- **Weathered Rocker**: 1990'ların alternatif rock müziğini anımsatan, pürüzlü ve sert tını. Gergin üst notalarla birlikte ham duygusal yoğunluk.

### Söz içermeyen vokal efektleri

Ayrıca, konuşma diyalogları, vokal kesintileri ve örnekleme efektleri için de istemde bulunabilirsiniz:

- Bir radyo yayını sesi, ritim başlamadan önce şarkıyı tanıtıyor.
- Drop'tan hemen önce fısıldayan bir ses ve ardından yüksek enerjili synth sesleri
- Enstrümantal ritim öğesi olarak döngüye alınan, kesilmiş ve perdesi değiştirilmiş vokal örnekleri

## Müzikal parametreler

İsteminizi standart müzik özellikleriyle iyileştirin:

- **Tempo (BPM)**: Tempoyu doğrudan ayarlayın (ör. `120 BPM`, `slow tempo around 72 BPM`, `fast 160 BPM`).
- **Ton ve Ölçek**: Anahtarı ve tonu belirtin (ör. `in G major`, `in D minor`, `in C pentatonic`).
- **Ruh Hali ve Atmosfer**: Duygusal sıfatlar kullanın:
  `Ambient, Bright, Chill, Dark, Dreamy, Emotional, Ethereal, Euphoric, Funky, Groovy, Melancholic, Nostalgic, Ominous, Psychedelic, Relaxed, Soulful, Triumphant, Upbeat, Whimsical`

## Lyria RealTime'ı isteme

Lyria RealTime, tek bir monolitik istem dizesi yerine **ağırlıklı istemler** kullanır. Bu sayede, birden fazla müzik etkisini dinamik olarak harmanlayabilir ve WebSocket bağlantısı üzerinden müziği sürekli olarak yönlendirebilirsiniz.

### Ağırlıklı istem yapısı

Her ağırlıklı istem, açıklayıcı bir metin ifadesi ve kayan noktalı bir ağırlıktan oluşur:

```
prompts = [
    types.WeightedPrompt(text="minimal techno", weight=1.0),
    types.WeightedPrompt(text="deep sub bass", weight=0.6),
    types.WeightedPrompt(text="shimmering hi-hats", weight=0.4),
]
```

### Gerçek zamanlı yönlendirme stratejileri

- **Türleri karıştırma**: Dengeli ağırlıklar atayarak farklı stilleri karıştırın:
  - `ambient synth pads (weight: 0.8)` + `lo-fi hip-hop drums (weight: 0.6)`
  - `flamenco guitar (weight: 0.7)` + `deep house groove (weight: 0.5)`
- **Dinamik geçişler**: Müzik geçişini sorunsuz hale getirmek için zaman içinde istem ağırlıklarını ayarlayın:
  1. `chill jazz piano (weight: 1.0)` ile başlayın.
  2. `electronic breakbeat (weight: 0.3)` değerini kademeli olarak ekleyin.
  3. `electronic breakbeat` değerini `0.8` olarak artırırken `chill jazz piano` değerini `0.3` olarak düşürün.
- **Öğeleri katmanlama**: Enstrüman etiketlerini ve ruh hali etiketlerini ayrı tutarak bunları bağımsız olarak ayarlayabilirsiniz:
  - 1. istem: `bossa nova guitar (weight: 0.9)`
  - İstem 2: `warm acoustic bass (weight: 0.7)`
  - 3. İstem: `subtle vinyl crackle (weight: 0.3)`

## Örnek istemler

### Lyria 3.5 örnekleri

- **Lo-Fi Study Beat**:
  `none
  A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes piano chords, a relaxed boom-bap drum groove at 82 BPM, and a warm upright bassline. Instrumental only.`
- **Pop Anthem**:
  `none
  An upbeat, feel-good indie-pop song in G major at 122 BPM. Bright acoustic guitar strumming, driving kick drum, handclaps, and warm female vocal harmonies. The lyrics describe an unforgettable summer road trip with friends.`
- **Sinematik Cyberpunk**:
  `none
  Dark, cinematic cyberpunk synthwave at 110 BPM in D minor. Heavy distorted bass, ominous arpeggiated analog synthesizers, distant metallic percussion, and an ethereal female vocalise swelling during the climax.`

### Lyria RealTime yönlendirme seti

```
# Initial high-energy groove
await session.set_weighted_prompts(
    prompts=[
        types.WeightedPrompt(text="techno groove", weight=1.0),
        types.WeightedPrompt(text="acid 303 bass", weight=0.8),
    ]
)

# Transition to a melodic breakdown
await session.set_weighted_prompts(
    prompts=[
        types.WeightedPrompt(text="ambient synth pads", weight=1.0),
        types.WeightedPrompt(text="subtle reverberant piano", weight=0.7),
        types.WeightedPrompt(text="techno groove", weight=0.2),
    ]
)
```

## Sırada ne var?

- [Lyria 3.5 ile müzik üretme](https://ai.google.dev/gemini-api/docs/music-generation?hl=tr): Interactions API'yi kullanarak tam şarkılar ve 30 saniyelik klipler oluşturun.
- [Lyria RealTime ile anlık müzik üretme](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=tr): WebSockets üzerinden anlık ve etkileşimli müzik akışı uygulamaları oluşturun.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-18 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-18 UTC."],[],[]]
