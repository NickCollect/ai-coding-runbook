---
source_url: https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=ar
fetched_at: 2026-10-19T05:55:08.795737+00:00
title: "\u062f\u0644\u064a\u0644 \u0643\u062a\u0627\u0628\u0629 \u0627\u0644\u0637\u0644\u0628\u0627\u062a \u0641\u064a Lyria \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon متاح الآن. [جرِّب هذه الميزة](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# دليل كتابة الطلبات في Lyria

يوفّر Gemini API طريقتَين لإنشاء الموسيقى باستخدام Lyria:

- ‫**Lyria 3.5 وLyria 3 Clip**: إنشاء مقاطع مدتها 30 ثانية أو أغاني كاملة الطول تتضمّن كلمات وغناء بدون بث مباشر اطّلِع على [إنشاء الموسيقى باستخدام Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=ar).
- **Lyria RealTime**: بث الموسيقى التفاعلي في الوقت الفعلي والتحكّم المباشر عبر WebSockets [مزيد من المعلومات حول إنشاء الموسيقى في الوقت الفعلي باستخدام Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ar)

يستجيب كلا النموذجين لطلبات نصية وصفية ومصطلحات موسيقية وتوجيهات هيكلية. يغطّي هذا الدليل كيفية كتابة طلبات فعّالة لكلّ من إنشاء الصور المجمّعة والتوجيه في الوقت الفعلي.

## أساسيات الطلبات

يمكن أن يكون طلبك عبارة قصيرة:

```
A folk song about cute cats avoiding puddles, female vocals, acoustic guitar, sound of rain
```

أو وصف مفصّل ومنظَّم:

```
A 1980s-style synth-pop track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. The song should have a retro-futuristic feel with modern production polish. Upbeat tempo around 120 BPM, clear verse-chorus structure, and a memorable instrumental hook. The lyrics describe getting ready for a party.
```

تؤدي الطلبات الموجزة والمفصّلة إلى نتائج قوية. استخدِم الاستراتيجيات التالية لتوجيه النموذج نحو الصوت الذي تريده بالضبط.

## النوع والأسلوب

ابدأ طلبك بالنوع الأساسي. يمكنك الجمع بين الأنواع لإنشاء سلالات هجينة فريدة:

- مزيج من موسيقى الميتال والهيب هوب
- موسيقى "ديث ميتال" مع غناء أوبرا
- موسيقى حجرة كلاسيكية مع عناصر إلكترونية داكنة
- موسيقى رقص إلكترونية حديثة (EDM) ممزوجة بموسيقى البوب الأوروبية

يمكنك أيضًا تحديد حقبة موسيقية أو نوع إقليمي:

- موسيقى الهيب هوب "بوم-باب" في أوائل التسعينيات
- موسيقى "ييه ييه" الفرنسية من الستينيات
- موسيقى "بوست بانك" و"الموجة الجديدة" في الثمانينيات
- أبرز أغاني الآر أند بي في الألفية الجديدة
- موسيقى التكنو البسيطة في برلين أو موسيقى الهيفي في منطقة خليج سان فرانسيسكو

### الكلمات الرئيسية الخاصة بالنوع

استخدِم عبارات الأنواع الموسيقية المعروفة هذه في طلباتك إلى Lyria 3.5 وLyria RealTime:

- **موسيقى إلكترونية للرقص**: `Acid House, Breakbeat, Chillout, Chiptune, Deep House, Drum & Bass, Dubstep, EDM, Electro Swing, Glitch Hop, Hyperpop, Minimal Techno, Moombahton, Psytrance, Synthpop, Techno, Trance, Trip Hop, Vaporwave`
- **موسيقى "هيب هوب" و"آر آند بي"**: `808 Hip Hop, Boom-Bap, Contemporary R&B, G-funk, Grime, Lo-Fi Hip Hop, Neo-Soul, New Jack Swing, Trap Beat`
- **موسيقى الروك والموسيقى البديلة**: `Alternative Country, Blues Rock, Classic Rock, Funk Metal, Garage Rock, Indie Folk, Indie Pop, Post-Punk, 60s Psychedelic Rock, Shoegaze, Surf Rock`
- **موسيقى الجاز والسول والفانك**: `Acid Jazz, Afrobeat, Bossa Nova, Disco Funk, Funk, Jazz Fusion, Latin Jazz`
- **موسيقى فلكلورية وتقليدية**: `Bengal Baul, Bhangra, Bluegrass, Celtic Folk, Cumbia, Indian Classical, Irish Folk, Merengue, Polka, Reggae, Reggaeton, Renaissance Music, Salsa`
- **موسيقى كلاسيكية وهادئة**: `Baroque, Orchestral Score, Piano Ballad`

## الآلات الموسيقية والأنسجة

يختار نموذج Lyria الآلات الموسيقية المناسبة للنوع الموسيقي المطلوب تلقائيًا. إذا كنت تريد آلات موسيقية معيّنة أو مجموعات غير عادية، عليك الإفصاح عنها بوضوح:

```
A dance track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. A saxophone solo enters during the bridge.
```

يُرجى وصف طريقة تفاعل الآلات الموسيقية مع بعضها البعض لتحديد الأجواء والملمس:

- موسيقى باص مشوّهة من آلة 303 تخترق صوت الصنجات العالي الواضح
- أصوات سنثسيزر دافئة تتصاعد تحت عزف غيتار أكوستيك بلمسة دافئة وقريبة
- جدار صوتي مصنوع من طبقات متعددة من غيتار مشوّش، مع أصوات غنائية بعيدة ومغمورة بالصدى

### الكلمات الرئيسية للأدوات

- **الآلات الموسيقية ذات المفاتيح ولوحات المفاتيح**: `Buchla Synths, Clavichord, Dirty Synths, Harpsichord, Mellotron, Moog Oscillations, Ragtime Piano, Rhodes Piano, Smooth Pianos, Spacey Synths, Synth Pads`
- **Bass & Drums**: `303 Acid Bass, 808 Hip Hop Beat, Boomy Bass, Conga Drums, Drumline, Funk Drums, Precision Bass, Tabla, TR-909 Drum Machine`
- **غيتارات وآلات وترية**: `Banjo, Balalaika, Bouzouki, Cello, Charango, Dulcimer, Fiddle, Flamenco Guitar, Guitar, Harp, Koto, Lyre, Mandolin, Pipa, Shamisen, Shredding Guitar, Sitar, Slide Guitar, Viola Ensemble, Warm Acoustic Guitar`
- **آلات النفخ**: `Alto Saxophone, Bagpipes, Bass Clarinet, Didgeridoo, Harmonica, Ocarina, Trumpet, Tuba, Woodwinds`
- **آلات النفخ**: `Bongos, Djembe, Glockenspiel, Hang Drum, Kalimba, Maracas, Marimba, Mbira, Steel Drum, Vibraphone`

## بنية الأغنية وتوقيتها

بالنسبة إلى Lyria 3.5، حدِّد تقدّم الأغنية باستخدام علامات أو أسهم:

- `[Intro] -> [Verse 1] -> [Chorus] -> [Verse 2] -> [Chorus] -> [Bridge] -> [Outro]`
- ابدأ بمقدمة هادئة على البيانو، ثم انتقِل إلى مقطع حيوي، وتوقّف للحظة صمت، ثم انتقِل إلى اللازمة.

يمكنك توجيه ديناميكيات الطاقة وانتقالاتها من خلال:

- بناء التشويق من خلال المقطع التمهيدي قبل الجوقة، ثم الانتقال إلى الصمت قبل جوقة حماسية
- تصاعد تدريجي في مستوى الصوت خلال الأغنية، مع إضافة آلة موسيقية واحدة لكل مقطع
- تتضمّن أغنية "أنا مش بتاعت الكلام ده" مقطعًا موسيقيًا قصيرًا بعد الجسر الموسيقي، يليه مقطع كورال بدون موسيقى

يمكنك أيضًا طلب علامات توقيت محدّدة:

- الوصول إلى ذروة الأغنية عند الثانية 12
- تتكرر عينة الصوت كل 4 مقاييس
- تبدأ اللازمة الموسيقية عند الثانية 22

## كلمات الأغنية والغناء

تنشئ Lyria 3.5 مقاطع صوتية تتضمّن غناءً وكلمات تلقائيًا. يمكنك تقديم كلمات الأغنية الخاصة بك أو الطلب من النموذج إنشاءها أو طلب مقطع موسيقي فقط.

### استخدام كلمات الأغنية الخاصة بك

أدرِج كلمات الأغنية مباشرةً في الطلب أسفل العنوان `Lyrics:`. ضع علامة لكل قسم لتوجيه الأداء الصوتي:

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

استخدِم الأقواس لوصف الغناء المساند أو الصدى أو الارتجال، مثل `(moving on)`.

### توجيه عملية إنشاء كلمات الأغاني

عندما تطلب من Lyria 3.5 كتابة كلمات أغنية، حدِّد القصة أو المشاعر أو العبارات الرئيسية:

```
The lyrics describe driving down the Pacific Coast Highway at sunset. The mood is nostalgic and reflective. Include an uplifting, anthemic chorus about second chances and starting over.
```

بالنسبة إلى أنواع الموسيقى الإلكترونية والرقص، اطلب جملًا موسيقية قصيرة متكررة:

```
An upbeat dance-pop track with a repetitive, high-energy vocal hook: "Feel the rhythm all night long."
```

### الأداء الصوتي وملفات المغنّين الشخصية

تحديد الجنس والمجال الصوتي والنبرة للحصول على أداء دقيق:

- **السوبرانو النسائي**: صوت واضح ونقي مع أداء رشيق وعالٍ. نغمة مشرقة قادرة على إنتاج ملمس خفيف وناعم.
- **صوت الألتو الأنثوي**: صوت غني ودافئ وأجش في النطاق المنخفض نبرة صوتية دخانية مع صوت جهوري رنان.
- **صوت التينور الرجالي**: صوت حاد ونشيط ومشرق نبرة شبابية مع قوة عالية في الغناء الحماسي تخترق التشكيلات الكثيفة.
- **صوت ذكوري عميق**: صوت عميق وناعم كالمخمل يخرج من الصدر بنبرة دافئة وهادئة.
- **Weathered Rocker**: صوت أجش وخشن يذكّر بموسيقى الروك البديلة في التسعينيات. أداء عاطفي قوي مع نغمات عليا متوترة

### تأثيرات صوتية غير غنائية

يمكنك أيضًا طلب حوار منطوق وأغاني مقطّعة وتأثيرات أخذ العيّنات:

- يقدّم صوت برنامج إذاعي قديم الأغنية قبل أن تبدأ الإيقاعات
- همسات صوتية قبل الجزء الحماسي، تليها أصوات تركيبية حماسية
- عينات صوتية مقطّعة ومعدّلة النبرة يتم تكرارها كعنصر إيقاعي موسيقي

## المَعلمات الموسيقية

حسِّن طلبك باستخدام الخصائص الموسيقية العادية:

- **الإيقاع (نبضة في الدقيقة)**: اضبط الإيقاع مباشرةً (مثل `120 BPM` أو `slow tempo around 72 BPM` أو `fast 160 BPM`).
- **المفتاح الموسيقي والمقياس**: حدِّد المفتاح الموسيقي الأساسي والأسلوب الموسيقي (مثل `in G major` أو `in D minor` أو `in C pentatonic`).
- **الحالة المزاجية والأجواء**: استخدِم صفات عاطفية وصفية:
  `Ambient, Bright, Chill, Dark, Dreamy, Emotional, Ethereal, Euphoric, Funky, Groovy, Melancholic, Nostalgic, Ominous, Psychedelic, Relaxed, Soulful, Triumphant, Upbeat, Whimsical`

## إدخال طلبات إلى Lyria RealTime

تستخدم Lyria RealTime **طلبات مرجّحة** بدلاً من سلسلة طلب واحدة متكاملة. يتيح لك ذلك مزج عدة تأثيرات موسيقية بشكل ديناميكي وتوجيه الموسيقى باستمرار عبر اتصال WebSocket.

### بنية الطلب المرجّحة

يتألف كل طلب مرجّح من عبارة نصية وصفية ووزن نقطة عائمة:

```
prompts = [
    types.WeightedPrompt(text="minimal techno", weight=1.0),
    types.WeightedPrompt(text="deep sub bass", weight=0.6),
    types.WeightedPrompt(text="shimmering hi-hats", weight=0.4),
]
```

### استراتيجيات التوجيه في الوقت الفعلي

- **دمج الأنواع**: يمكنك دمج أنماط مختلفة من خلال تخصيص أوزان متوازنة:
  - `ambient synth pads (weight: 0.8)` + `lo-fi hip-hop drums (weight: 0.6)`
  - `flamenco guitar (weight: 0.7)` + `deep house groove (weight: 0.5)`
- **تأثيرات انتقالية ديناميكية**: لضمان انتقال الموسيقى بسلاسة، اضبط أوزان الطلبات بمرور الوقت:
  1. ابدأ بنسبة شحن ‎`chill jazz piano (weight: 1.0)`.
  2. أضِف `electronic breakbeat (weight: 0.3)` تدريجيًا.
  3. زيادة `electronic breakbeat` إلى `0.8` مع خفض `chill jazz piano` إلى `0.3`
- **الطبقات**: يجب إبقاء علامات الآلات الموسيقية وعلامات الحالة المزاجية منفصلة حتى تتمكّن من تعديلها بشكل مستقل:
  - الطلب 1: `bossa nova guitar (weight: 0.9)`
  - الطلب 2: `warm acoustic bass (weight: 0.7)`
  - الطلب 3: `subtle vinyl crackle (weight: 0.3)`

## أمثلة على الطلبات

### أمثلة على Lyria 3.5

- **Lo-Fi Study Beat**:
  `none
  A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes piano chords, a relaxed boom-bap drum groove at 82 BPM, and a warm upright bassline. Instrumental only.`
- **أغنية بوب**:
  `none
  An upbeat, feel-good indie-pop song in G major at 122 BPM. Bright acoustic guitar strumming, driving kick drum, handclaps, and warm female vocal harmonies. The lyrics describe an unforgettable summer road trip with friends.`
- **Cinematic Cyberpunk**:
  `none
  Dark, cinematic cyberpunk synthwave at 110 BPM in D minor. Heavy distorted bass, ominous arpeggiated analog synthesizers, distant metallic percussion, and an ethereal female vocalise swelling during the climax.`

### Lyria RealTime steering set

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

## الخطوات التالية

- [إنشاء الموسيقى باستخدام Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=ar): يمكنك إنشاء أغانٍ كاملة ومقاطع مدتها 30 ثانية باستخدام Interactions API.
- [إنشاء الموسيقى في الوقت الفعلي باستخدام Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ar): يمكنك إنشاء تطبيقات تفاعلية لبث الموسيقى في الوقت الفعلي عبر WebSockets.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-18 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-18 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
