---
source_url: https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=hi
fetched_at: 2026-10-05T06:38:19.183565+00:00
title: "Lyria \u092a\u094d\u0930\u0949\u092e\u094d\u092a\u094d\u091f \u0915\u0947 \u0932\u093f\u090f \u0917\u093e\u0907\u0921 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Lyria प्रॉम्प्ट के लिए गाइड

Gemini API की मदद से, Lyria में संगीत जनरेट करने के दो तरीके हैं:

- **Lyria 3.5 और Lyria 3 Clip**: स्ट्रीमिंग के बिना, 30 सेकंड की क्लिप या पूरे गाने जनरेट किए जा सकते हैं. इनमें बोल और संगीत भी शामिल होता है. [Lyria 3.5 की मदद से संगीत जनरेट करना](https://ai.google.dev/gemini-api/docs/music-generation?hl=hi) लेख पढ़ें.
- **Lyria RealTime**: यह WebSockets पर रीयल-टाइम में इंटरैक्टिव म्यूज़िक स्ट्रीमिंग और लाइव स्टीयरिंग की सुविधा देता है. [Lyria RealTime की मदद से रीयल-टाइम में संगीत जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=hi) लेख पढ़ें.

दोनों मॉडल, टेक्स्ट के ब्यौरे वाले प्रॉम्प्ट, संगीत की शब्दावली, और स्ट्रक्चर से जुड़े निर्देशों का जवाब देते हैं. इस गाइड में, बैच जनरेशन और रीयल-टाइम स्टीयरिंग, दोनों के लिए असरदार प्रॉम्प्ट लिखने का तरीका बताया गया है.

## प्रॉम्प्ट से जुड़ी बुनियादी बातें

आपके प्रॉम्प्ट में कोई छोटा वाक्यांश शामिल हो सकता है:

```
A folk song about cute cats avoiding puddles, female vocals, acoustic guitar, sound of rain
```

या स्ट्रक्चर्ड और पूरी जानकारी वाला ब्यौरा:

```
A 1980s-style synth-pop track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. The song should have a retro-futuristic feel with modern production polish. Upbeat tempo around 120 BPM, clear verse-chorus structure, and a memorable instrumental hook. The lyrics describe getting ready for a party.
```

छोटे और ज़्यादा जानकारी वाले, दोनों तरह के प्रॉम्प्ट से अच्छे नतीजे मिलते हैं. मॉडल को अपनी पसंद के हिसाब से आवाज़ देने के लिए, यहां दी गई रणनीतियों का इस्तेमाल करें.

## शैली और स्टाइल

अपने प्रॉम्प्ट की शुरुआत मुख्य शैली से करें. यूनिक हाइब्रिड बनाने के लिए, शैलियों को आपस में मिलाया जा सकता है:

- मेटल और हिप-हॉप का फ़्यूज़न
- ऑपरा स्टाइल में आवाज़ के साथ डेथ मेटल
- डार्क इलेक्ट्रॉनिक ड्रोन वाले एलिमेंट के साथ क्लासिकल चैंबर म्यूज़िक
- यूरोपॉप के साथ मॉडर्न इलेक्ट्रॉनिक डांस म्यूज़िक (ईडीएम)

संगीत का दौर या क्षेत्रीय वैरिएंट भी तय किया जा सकता है:

- 1990 के दशक की शुरुआत का बूम-बैप हिप-हॉप
- 1960 के दशक का फ़्रेंच ये-ये पॉप
- 1980 के दशक का पोस्ट-पंक और न्यू वेव
- 2000 के दशक का मुख्यधारा वाला आर ऐंड बी
- बर्लिन का मिनिमल टेक्नो या बे एरिया का हाइफ़ी

### शैली के हिसाब से कीवर्ड

Lyria 3.5 और Lyria RealTime के लिए, अपने प्रॉम्प्ट में शैली के इन शब्दों का इस्तेमाल करें:

- **इलेक्ट्रॉनिक और डांस**: `Acid House, Breakbeat, Chillout, Chiptune, Deep House, Drum & Bass, Dubstep, EDM, Electro Swing, Glitch Hop, Hyperpop, Minimal Techno, Moombahton, Psytrance, Synthpop, Techno, Trance, Trip Hop, Vaporwave`
- **हिप-हॉप और आर ऐंड बी**: `808 Hip Hop, Boom-Bap, Contemporary R&B, G-funk, Grime, Lo-Fi Hip Hop, Neo-Soul, New Jack Swing, Trap Beat`
- **रॉक और ऑल्टरनेटिव**: `Alternative Country, Blues Rock, Classic Rock, Funk Metal, Garage Rock, Indie Folk, Indie Pop, Post-Punk, 60s Psychedelic Rock, Shoegaze, Surf Rock`
- **जैज़, सोल, और फ़ंक**: `Acid Jazz, Afrobeat, Bossa Nova, Disco Funk, Funk, Jazz Fusion, Latin Jazz`
- **लोक और पारंपरिक संगीत**: `Bengal Baul, Bhangra, Bluegrass, Celtic Folk, Cumbia, Indian Classical, Irish Folk, Merengue, Polka, Reggae, Reggaeton, Renaissance Music, Salsa`
- **क्लासिकल और ऐकोस्टिक**: `Baroque, Orchestral Score, Piano Ballad`

## वाद्य यंत्र और बनावट

Lyria, अनुरोध किए गए ज़ॉनर के लिए सही इंस्ट्रुमेंटेशन अपने-आप चुन लेता है. अगर आपको कुछ खास इंस्ट्रुमेंट या असामान्य कॉम्बिनेशन चाहिए, तो उनके बारे में साफ़ तौर पर बताएं:

```
A dance track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. A saxophone solo enters during the bridge.
```

बताएं कि मूड और टेक्सचर सेट करने के लिए, इंस्ट्रुमेंट कैसे बजते हैं और आपस में कैसे इंटरैक्ट करते हैं:

- क्रिसप और टाइट हाई-हैट के साथ, 303 बासलाइन को तोड़-मरोड़कर बनाया गया
- सूखे और सुकून भरे अकूस्टिक गिटार के नीचे, ऐनलॉग सिंथेसाइज़र की सुकून भरी धुन
- फ़ज़ गिटार की कई लेयर से बनी आवाज़, जिसमें दूर से गूंजती हुई आवाज़ सुनाई दे रही हो

### इंस्ट्रुमेंट कीवर्ड

- **कीबोर्ड और सिंथेसाइज़र**: `Buchla Synths, Clavichord, Dirty Synths, Harpsichord, Mellotron, Moog Oscillations, Ragtime Piano, Rhodes Piano, Smooth Pianos, Spacey Synths, Synth Pads`
- **बास और ड्रम**: `303 Acid Bass, 808 Hip Hop Beat, Boomy Bass, Conga Drums, Drumline, Funk Drums, Precision Bass, Tabla, TR-909 Drum Machine`
- **गिटार और स्ट्रिंग**: `Banjo, Balalaika, Bouzouki, Cello, Charango, Dulcimer, Fiddle, Flamenco Guitar, Guitar, Harp, Koto, Lyre, Mandolin, Pipa, Shamisen, Shredding Guitar, Sitar, Slide Guitar, Viola Ensemble, Warm Acoustic Guitar`
- **विंड और ब्रास**: `Alto Saxophone, Bagpipes, Bass Clarinet, Didgeridoo, Harmonica, Ocarina, Trumpet, Tuba, Woodwinds`
- **परकशन**: `Bongos, Djembe, Glockenspiel, Hang Drum, Kalimba, Maracas, Marimba, Mbira, Steel Drum, Vibraphone`

## गाने का स्ट्रक्चर और टाइमिंग

Lyria 3.5 के लिए, टैग या ऐरो का इस्तेमाल करके गाने की प्रोग्रेशन तय करें:

- `[Intro] -> [Verse 1] -> [Chorus] -> [Verse 2] -> [Chorus] -> [Bridge] -> [Outro]`
- शांत पियानो की धुन से शुरू करें, फिर एक जोशीली कविता बनाएं, कुछ देर के लिए रुकें, और फिर कोरस में जोश भर दें.

आपके पास एनर्जी के डाइनैमिक और ट्रांज़िशन को सीधे तौर पर कंट्रोल करने का विकल्प होता है:

- प्री-कोरस के ज़रिए गाने में तनाव बढ़ाएं. इसके बाद, धमाकेदार कोरस से पहले गाने को शांत कर दें
- पूरे गाने में धीरे-धीरे आवाज़ बढ़ती है. हर सेक्शन में एक इंस्ट्रुमेंट जोड़ा जाता है
- ब्रिज के बाद अचानक रुक जाना और फिर अ कपेला कोरस

इसके अलावा, किसी खास समय के मार्कर के बारे में भी पूछा जा सकता है:

- 12 सेकंड पर बीट ड्रॉप करें
- गाने के बोल का सैंपल हर चार बार दोहराया जाता है
- कोरस 22 सेकंड पर शुरू होता है

## गाने के बोल और गाने से जुड़ा कॉपीराइट

Lyria 3.5, डिफ़ॉल्ट रूप से बोल वाले वोकल ट्रैक जनरेट करता है. आपके पास अपने बोल देने, मॉडल से बोल जनरेट करने के लिए कहने या इंस्ट्रुमेंटल ट्रैक का अनुरोध करने का विकल्प होता है.

### खुद के लिखे गए बोल इस्तेमाल करना

`Lyrics:` हेडर के नीचे दिए गए प्रॉम्प्ट में, सीधे तौर पर अपने बोल शामिल करें. बोलकर जानकारी देने के लिए, हर सेक्शन को टैग करें:

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

बैकग्राउंड में गाए जाने वाले गाने, गूंजने वाली आवाज़ या बिना तैयारी के बोले गए शब्दों के लिए, ब्रैकेट का इस्तेमाल करें. जैसे, `(moving on)`.

### जनरेट किए गए बोल के लिए निर्देश देना

Lyria 3.5 को गीत के बोल लिखने के लिए कहते समय, कहानी, भावना या मुख्य वाक्यांशों के बारे में बताएँ:

```
The lyrics describe driving down the Pacific Coast Highway at sunset. The mood is nostalgic and reflective. Include an uplifting, anthemic chorus about second chances and starting over.
```

इलेक्ट्रॉनिक और डांस शैलियों के लिए, दोहराए जाने वाले छोटे वोकल हुक का अनुरोध करें:

```
An upbeat dance-pop track with a repetitive, high-energy vocal hook: "Feel the rhythm all night long."
```

### गायक की आवाज़ और उनकी प्रोफ़ाइलें

सटीक नतीजे पाने के लिए, गायक का जेंडर, वोकल रेंज, और टिंबर बताएँ:

- **सोप्रानो**: साफ़, क्रिस्टलीय टिंबर के साथ तेज़ और ऊंची डिलीवरी. ब्राइट टोन, जो हवादार और सांस लेने जैसी बनावट वाली आवाज़ें निकाल सकती है.
- **फ़्रीक्वेंसी रेंज में महिला की आवाज़**: यह आवाज़, गहरी, गर्म, और भारी होती है. स्मोकी टिंबर के साथ, दिल को छू लेने वाली और गूंजती हुई चेस्ट वॉइस.
- **पुरुष टेनर**: तेज़, तीखी, और ऊर्जा से भरपूर आवाज़. ऊंची बेल्टिंग पावर वाली युवा आवाज़, जो घने मिक्स को काटती है.
- **पुरुष की बैरिटोन आवाज़**: गहरी, मखमली, और सुकून देने वाली आवाज़.
- **Weathered Rocker**: यह आवाज़, 1990 के दशक के ऑल्टरनेटिव रॉक की याद दिलाती है. ऊंचे सुरों के साथ, भावनाओं को ज़ाहिर करने वाली आवाज़.

### बिना लिरिक्स वाले वोकल इफ़ेक्ट

इसके अलावा, बोले गए डायलॉग, वोकल चॉप, और सैंपलिंग इफ़ेक्ट के लिए भी प्रॉम्प्ट दिया जा सकता है:

- रेडियो पर ब्रॉडकास्ट होने वाली आवाज़ में, बीट शुरू होने से पहले गाने के बारे में बताया जाता है
- ड्रॉप से ठीक पहले, एक आवाज़ फुसफुसाती है. इसके बाद, हाई-एनर्जी वाले सिंथेसाइज़र बजते हैं
- काटे गए, पिच-शिफ़्ट किए गए वोकल सैंपल, जो इंस्ट्रुमेंटल रिदम एलिमेंट के तौर पर लूप हो रहे हैं

## म्यूज़िकल पैरामीटर

संगीत की स्टैंडर्ड प्रॉपर्टी का इस्तेमाल करके, अपने प्रॉम्प्ट को बेहतर बनाएं:

- **टेंपो (बीपीएम)**: सीधे तौर पर टेंपो सेट करें (जैसे, `120 BPM`, `slow tempo around 72 BPM`, `fast 160 BPM`).
- **की और स्केल**: रूट की और टोनैलिटी (जैसे, `in G major`, `in D minor`, `in C pentatonic`) के बारे में बताएं.
- **मूड और माहौल**: भावनाओं को ज़ाहिर करने वाले विशेषणों का इस्तेमाल करें:
  `Ambient, Bright, Chill, Dark, Dreamy, Emotional, Ethereal, Euphoric, Funky, Groovy, Melancholic, Nostalgic, Ominous, Psychedelic, Relaxed, Soulful, Triumphant, Upbeat, Whimsical`

## Lyria RealTime को प्रॉम्प्ट करना

Lyria RealTime, एक ही प्रॉम्प्ट स्ट्रिंग के बजाय **वेटेड प्रॉम्प्ट** का इस्तेमाल करता है. इससे आपको एक साथ कई म्यूज़िकल स्टाइल को डाइनैमिक तरीके से मिक्स करने और WebSocket कनेक्शन पर लगातार म्यूज़िक चलाने की सुविधा मिलती है.

### वज़न के हिसाब से प्रॉम्प्ट स्ट्रक्चर

वज़न के हिसाब से हर प्रॉम्प्ट में, जानकारी देने वाला टेक्स्ट फ़्रेज़ और फ़्लोटिंग-पॉइंट वेट होता है:

```
prompts = [
    types.WeightedPrompt(text="minimal techno", weight=1.0),
    types.WeightedPrompt(text="deep sub bass", weight=0.6),
    types.WeightedPrompt(text="shimmering hi-hats", weight=0.4),
]
```

### रीयल-टाइम में स्टीयरिंग की रणनीतियां

- **अलग-अलग शैलियों को ब्लेंड करना**: अलग-अलग शैलियों को ब्लेंड करने के लिए, उन्हें बराबर वेट असाइन करें:
  - `ambient synth pads (weight: 0.8)` + `lo-fi hip-hop drums (weight: 0.6)`
  - `flamenco guitar (weight: 0.7)` + `deep house groove (weight: 0.5)`
- **डाइनैमिक ट्रांज़िशन**: संगीत को आसानी से ट्रांज़िशन करने के लिए, समय के साथ प्रॉम्प्ट के वेट में बदलाव करें:
  1. `chill jazz piano (weight: 1.0)` से शुरू करें.
  2. धीरे-धीरे `electronic breakbeat (weight: 0.3)` जोड़ें.
  3. `chill jazz piano` को `0.3` पर सेट करते हुए, `electronic breakbeat` को `0.8` पर बढ़ाएं.
- **लेयरिंग एलिमेंट**: इंस्ट्रुमेंट टैग और मूड टैग को अलग-अलग रखें, ताकि आप उनमें अलग-अलग बदलाव कर सकें:
  - प्रॉम्प्ट 1: `bossa nova guitar (weight: 0.9)`
  - प्रॉम्प्ट 2: `warm acoustic bass (weight: 0.7)`
  - प्रॉम्प्ट 3: `subtle vinyl crackle (weight: 0.3)`

## प्रॉम्प्ट के उदाहरण

### Lyria 3.5 के उदाहरण

- **Lo-Fi Study Beat**:
  `none
  A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes piano chords, a relaxed boom-bap drum groove at 82 BPM, and a warm upright bassline. Instrumental only.`
- **पॉप ऐंथम**:
  `none
  An upbeat, feel-good indie-pop song in G major at 122 BPM. Bright acoustic guitar strumming, driving kick drum, handclaps, and warm female vocal harmonies. The lyrics describe an unforgettable summer road trip with friends.`
- **सिनमैटिक साइबरपंक**:
  `none
  Dark, cinematic cyberpunk synthwave at 110 BPM in D minor. Heavy distorted bass, ominous arpeggiated analog synthesizers, distant metallic percussion, and an ethereal female vocalise swelling during the climax.`

### Lyria RealTime स्टीयरिंग सेट है

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

## आगे क्या करना है

- [Lyria 3.5 की मदद से संगीत जनरेट करना](https://ai.google.dev/gemini-api/docs/music-generation?hl=hi): Interactions API का इस्तेमाल करके, पूरे गाने और 30 सेकंड की क्लिप जनरेट करें.
- [Lyria RealTime की मदद से रीयल-टाइम में संगीत जनरेट करना](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=hi): WebSockets पर रीयल-टाइम में इंटरैक्टिव म्यूज़िक स्ट्रीमिंग ऐप्लिकेशन बनाएं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-18 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-18 (UTC) को अपडेट किया गया."],[],[]]
