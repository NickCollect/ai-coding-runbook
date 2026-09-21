---
source_url: https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=th
fetched_at: 2026-09-21T05:47:37.677798+00:00
title: "\u0e04\u0e39\u0e48\u0e21\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e43\u0e0a\u0e49\u0e1e\u0e23\u0e2d\u0e21\u0e15\u0e4c\u0e02\u0e2d\u0e07 Lyria \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# คู่มือการใช้พรอมต์ของ Lyria

Gemini API มี 2 วิธีในการสร้างเพลงด้วย Lyria ดังนี้

- **Lyria 3.5 และ Lyria 3 Clip**: การสร้างแบบไม่สตรีมสำหรับคลิปความยาว 30 วินาทีหรือเพลงแบบเต็มพร้อมเนื้อเพลงและเสียงร้อง ดู[สร้างเพลงด้วย Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=th)
- **Lyria RealTime**: การสตรีมเพลงแบบเรียลไทม์และแบบอินเทอร์แอกทีฟ รวมถึงการควบคุมแบบเรียลไทม์ผ่าน WebSockets ดู[การสร้างเพลงแบบเรียลไทม์ด้วย Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=th)

ทั้ง 2 โมเดลตอบสนองต่อพรอมต์ข้อความอธิบาย คำศัพท์ทางดนตรี และคำสั่งโครงสร้าง คู่มือนี้ครอบคลุมวิธีเขียนพรอมต์ที่มีประสิทธิภาพสำหรับการสร้างแบบกลุ่มและการควบคุมแบบเรียลไทม์

## พื้นฐานของพรอมต์

พรอมต์ของคุณอาจเป็นวลีสั้นๆ ดังนี้

```
A folk song about cute cats avoiding puddles, female vocals, acoustic guitar, sound of rain
```

หรือคำอธิบายแบบละเอียดที่มีโครงสร้าง

```
A 1980s-style synth-pop track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. The song should have a retro-futuristic feel with modern production polish. Upbeat tempo around 120 BPM, clear verse-chorus structure, and a memorable instrumental hook. The lyrics describe getting ready for a party.
```

ทั้งพรอมต์แบบสั้นและแบบละเอียดให้ผลลัพธ์ที่ยอดเยี่ยม ใช้กลยุทธ์ต่อไปนี้เพื่อนำโมเดลไปสู่เสียงที่คุณต้องการ

## แนวเพลงและสไตล์

นำหน้าพรอมต์ด้วยประเภทหลัก คุณสามารถผสมผสานแนวเพลงเพื่อสร้างแนวเพลงลูกผสมที่ไม่เหมือนใครได้ดังนี้

- การผสมผสานระหว่างเมทัลและฮิปฮอป
- เดธเมทัลผสมกับเสียงร้องแบบโอเปร่า
- ดนตรีคลาสสิกสำหรับวงเครื่องดนตรีขนาดเล็กที่มีองค์ประกอบดรอนอิเล็กทรอนิกส์มืดหม่น
- เพลงอิเล็กทรอนิกส์แดนซ์ (EDM) สมัยใหม่ผสมกับเพลงป๊อปยุโรป

นอกจากนี้ คุณยังระบุยุคดนตรีหรือรูปแบบตามภูมิภาคได้ด้วย

- ฮิปฮอปบูมแบ็ปช่วงต้นทศวรรษ 1990
- เพลงป๊อปเยเย่ของฝรั่งเศสในยุค 1960
- โพสต์พังก์และนิวเวฟยุค 1980
- อาร์แอนด์บีกระแสหลักยุค 2000
- เทคโนมินิมอลของเบอร์ลินหรือไฮฟีของเบย์แอเรีย

### คีย์เวิร์ดประเภท

ใช้คำศัพท์แนวเพลงที่รู้จักเหล่านี้ในพรอมต์สำหรับ Lyria 3.5 และ Lyria RealTime

- **อิเล็กทรอนิกและแดนซ์**: `Acid House, Breakbeat, Chillout, Chiptune, Deep House, Drum & Bass, Dubstep, EDM, Electro Swing, Glitch Hop, Hyperpop, Minimal Techno, Moombahton, Psytrance, Synthpop, Techno, Trance, Trip Hop, Vaporwave`
- **ฮิปฮอปและอาร์แอนด์บี**: `808 Hip Hop, Boom-Bap, Contemporary R&B, G-funk, Grime, Lo-Fi Hip Hop, Neo-Soul, New Jack Swing, Trap Beat`
- **ร็อกและอัลเทอร์เนทีฟ**: `Alternative Country, Blues Rock, Classic Rock, Funk Metal, Garage Rock, Indie Folk, Indie Pop, Post-Punk, 60s Psychedelic Rock, Shoegaze, Surf Rock`
- **แจ๊ส โซล และฟังก์**: `Acid Jazz, Afrobeat, Bossa Nova, Disco Funk, Funk, Jazz Fusion, Latin Jazz`
- **เพลงพื้นบ้านและเพลงดั้งเดิม**: `Bengal Baul, Bhangra, Bluegrass, Celtic Folk, Cumbia, Indian Classical, Irish Folk, Merengue, Polka, Reggae, Reggaeton, Renaissance Music, Salsa`
- **คลาสสิกและอะคูสติก**: `Baroque, Orchestral Score, Piano Ballad`

## เครื่องดนตรีและพื้นผิว

Lyria จะเลือกเครื่องดนตรีที่เหมาะสมกับแนวเพลงที่ขอโดยอัตโนมัติ หากต้องการเครื่องดนตรีที่เฉพาะเจาะจงหรือการผสมผสานที่แปลกใหม่ ให้ประกาศอย่างชัดเจนดังนี้

```
A dance track with a driving beat, shimmering synthesizers, and a catchy, anthemic chorus. A saxophone solo enters during the bridge.
```

อธิบายลักษณะเสียงของเครื่องดนตรีและการทำงานร่วมกันเพื่อสร้างอารมณ์และพื้นผิว

- เสียงเบสไลน์ 303 ที่ดัดแปลงซึ่งตัดผ่านเสียงไฮแฮตที่คมชัดและแน่น
- เสียงสังเคราะห์แบบอนาล็อกที่อบอุ่นค่อยๆ ดังขึ้นใต้เสียงกีตาร์โปร่งที่แห้งและใกล้ชิด
- กำแพงเสียงที่สร้างขึ้นจากกีตาร์ฟัซหลายเลเยอร์ พร้อมเสียงร้องที่อยู่ไกลๆ ซึ่งเต็มไปด้วยรีเวิร์บ

### คีย์เวิร์ดของเครื่องมือ

- **คีย์บอร์ดและซินธิไซเซอร์**: `Buchla Synths, Clavichord, Dirty Synths, Harpsichord, Mellotron, Moog Oscillations, Ragtime Piano, Rhodes Piano, Smooth Pianos, Spacey Synths, Synth Pads`
- **เบสและกลอง**: `303 Acid Bass, 808 Hip Hop Beat, Boomy Bass, Conga Drums, Drumline, Funk Drums, Precision Bass, Tabla, TR-909 Drum Machine`
- **กีตาร์และสาย**: `Banjo, Balalaika, Bouzouki, Cello, Charango, Dulcimer, Fiddle, Flamenco Guitar, Guitar, Harp, Koto, Lyre, Mandolin, Pipa, Shamisen, Shredding Guitar, Sitar, Slide Guitar, Viola Ensemble, Warm Acoustic Guitar`
- **เครื่องลมและเครื่องทองเหลือง**: `Alto Saxophone, Bagpipes, Bass Clarinet, Didgeridoo, Harmonica, Ocarina, Trumpet, Tuba, Woodwinds`
- **เครื่องเพอร์คัชชัน**: `Bongos, Djembe, Glockenspiel, Hang Drum, Kalimba, Maracas, Marimba, Mbira, Steel Drum, Vibraphone`

## โครงสร้างและจังหวะเวลาของเพลง

สำหรับ Lyria 3.5 ให้กำหนดความคืบหน้าของเพลงโดยใช้แท็กหรือลูกศร

- `[Intro] -> [Verse 1] -> [Chorus] -> [Verse 2] -> [Chorus] -> [Bridge] -> [Outro]`
- เริ่มด้วยอินโทรเปียโนที่นุ่มนวล ค่อยๆ เพิ่มจังหวะให้เป็นท่อนเวิร์สที่กระฉับกระเฉง หยุดพักเพื่อช่วงเวลาแห่งความเงียบ แล้วระเบิดออกมาเป็นท่อนคอรัส

คุณสามารถกำหนดพลวัตและการเปลี่ยนผ่านด้านพลังงานได้ดังนี้

- สร้างความตึงเครียดผ่านท่อนก่อนฮุก จากนั้นก็เงียบก่อนที่จะเข้าท่อนฮุกที่ทรงพลัง
- ค่อยๆ เพิ่มความเข้มข้นของเพลงตลอดทั้งเพลง โดยเพิ่มเครื่องดนตรีทีละชิ้นในแต่ละท่อน
- หยุดกะทันหันหลังท่อนบริดจ์ ตามด้วยคอรัสแบบอะแคปเปลลา

นอกจากนี้ คุณยังแจ้งให้ใส่เครื่องหมายเวลาที่เฉพาะเจาะจงได้ด้วย

- สร้างช่วงดรอปของเพลงที่ 12 วินาที
- ตัวอย่างเสียงร้องจะเล่นซ้ำทุกๆ 4 บาร์
- ท่อนฮุกเริ่มที่ 22 วินาที

## เนื้อเพลงและเสียงร้อง

Lyria 3.5 จะสร้างแทร็กเสียงร้องพร้อมเนื้อเพลงโดยค่าเริ่มต้น คุณสามารถระบุเนื้อเพลงของคุณเอง ขอให้โมเดลสร้างเนื้อเพลง หรือขอแทร็กบรรเลงได้

### การใช้เนื้อเพลงของคุณเอง

ใส่เนื้อเพลงลงในพรอมต์โดยตรงใต้ส่วนหัว `Lyrics:` ติดแท็กแต่ละส่วนเพื่อเป็นแนวทางในการนำเสนอเสียงร้อง

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

ใช้เครื่องหมายวงเล็บสำหรับเสียงร้องประสาน เสียงก้อง หรือการด้นสด เช่น `(moving on)`

### การกำกับเนื้อเพลงที่สร้างขึ้น

เมื่อขอให้ Lyria 3.5 เขียนเนื้อเพลง ให้ระบุโครงเรื่อง อารมณ์ หรือวลีสำคัญ

```
The lyrics describe driving down the Pacific Coast Highway at sunset. The mood is nostalgic and reflective. Include an uplifting, anthemic chorus about second chances and starting over.
```

สำหรับแนวเพลงอิเล็กทรอนิกส์และแดนซ์ ให้ขอท่อนฮุกเสียงร้องสั้นๆ ที่ร้องซ้ำ

```
An upbeat dance-pop track with a repetitive, high-energy vocal hook: "Feel the rhythm all night long."
```

### การนำส่งเสียงร้องและโปรไฟล์นักร้อง

ระบุเพศ ช่วงเสียง และโทนเสียงเพื่อให้ได้ผลลัพธ์ที่แม่นยำ

- **โซปราโนหญิง**: เสียงใสราวคริสตัลที่มีความคล่องตัวและทรงพลัง โทนสว่างที่ให้พื้นผิวโปร่งและมีลม
- **อัลโตหญิง**: เสียงทุ้มที่อบอุ่นและแหบพร่า เสียงทุ้มต่ำที่เต็มไปด้วยจิตวิญญาณและก้องกังวาน
- **เสียงเทเนอร์ชาย**: สดใส ก้องกังวาน และมีพลัง เสียงที่สดใสพร้อมพลังเสียงสูงที่โดดเด่นในมิกซ์ที่ซับซ้อน
- **บาร์ริโทนชาย**: เสียงทุ้มต่ำนุ่มละมุนจากอกพร้อมการนำเสนอที่อบอุ่น นุ่มนวล และขับกล่อม
- **ร็อกเกอร์ผู้ผ่านร้อนผ่านหนาว**: เสียงแหบแห้งที่ชวนให้นึกถึงร็อกอัลเทอร์เนทีฟยุค 90 ความเข้มข้นทางอารมณ์ที่ดิบเถื่อนพร้อมโน้ตสูงที่ตึงเครียด

### เอฟเฟกต์เสียงร้องที่ไม่มีเนื้อร้อง

นอกจากนี้ คุณยังแจ้งให้สร้างบทสนทนาที่พูด เสียงร้อง และเอฟเฟกต์การแซมเปิลได้ด้วย

- เสียงประกาศจากวิทยุโบราณจะแนะนำเพลงก่อนที่จังหวะจะเริ่มขึ้น
- เสียงพูดกระซิบก่อนดรอป ตามด้วยซินธ์ที่มีพลังสูง
- ตัวอย่างเสียงร้องที่ตัดต่อและเปลี่ยนระดับเสียงซึ่งวนซ้ำเป็นองค์ประกอบจังหวะของเครื่องดนตรี

## พารามิเตอร์ทางดนตรี

ปรับแต่งพรอมต์ด้วยคุณสมบัติทางดนตรีมาตรฐาน

- **เทมโป (BPM)**: ตั้งค่าเทมโปโดยตรง (เช่น `120 BPM`, `slow tempo around 72 BPM`, `fast 160 BPM`)
- **คีย์และสเกล**: ระบุคีย์รูทและโทนเสียง (เช่น `in G major`, `in D minor`, `in C pentatonic`)
- **อารมณ์และบรรยากาศ**: ใช้คำคุณศัพท์ที่สื่อถึงอารมณ์
  `Ambient, Bright, Chill, Dark, Dreamy, Emotional, Ethereal, Euphoric, Funky, Groovy, Melancholic, Nostalgic, Ominous, Psychedelic, Relaxed, Soulful, Triumphant, Upbeat, Whimsical`

## การแจ้ง Lyria RealTime

Lyria RealTime ใช้**พรอมต์แบบถ่วงน้ำหนัก**แทนสตริงพรอมต์แบบโมโนลิธเดียว ซึ่งช่วยให้คุณผสมผสานอิทธิพลทางดนตรีหลายอย่างได้อย่างไดนามิกและควบคุมเพลงอย่างต่อเนื่องผ่านการเชื่อมต่อ WebSocket

### โครงสร้างพรอมต์แบบถ่วงน้ำหนัก

พรอมต์ที่มีการถ่วงน้ำหนักแต่ละรายการประกอบด้วยวลีข้อความอธิบายและน้ำหนักจุดลอยตัว

```
prompts = [
    types.WeightedPrompt(text="minimal techno", weight=1.0),
    types.WeightedPrompt(text="deep sub bass", weight=0.6),
    types.WeightedPrompt(text="shimmering hi-hats", weight=0.4),
]
```

### กลยุทธ์การปรับแบบเรียลไทม์

- **การผสมผสานแนวเพลง**: ผสมผสานสไตล์ที่แตกต่างกันโดยกำหนดน้ำหนักที่สมดุล ดังนี้
  - `ambient synth pads (weight: 0.8)` + `lo-fi hip-hop drums (weight: 0.6)`
  - `flamenco guitar (weight: 0.7)` + `deep house groove (weight: 0.5)`
- **การเปลี่ยนผ่านที่ลื่นไหล**: หากต้องการเปลี่ยนเพลงอย่างราบรื่น ให้ปรับน้ำหนักของพรอมต์เมื่อเวลาผ่านไปโดยทำดังนี้
  1. เริ่มต้นด้วย `chill jazz piano (weight: 1.0)`
  2. ค่อยๆ เพิ่ม `electronic breakbeat (weight: 0.3)`
  3. เพิ่ม `electronic breakbeat` เป็น `0.8` ขณะที่ลด `chill jazz piano` เป็น `0.3`
- **การวางเลเยอร์องค์ประกอบ**: แยกแท็กเครื่องดนตรีและแท็กอารมณ์ออกจากกันเพื่อให้ปรับแยกกันได้ โดยทำดังนี้
  - พรอมต์ 1: `bossa nova guitar (weight: 0.9)`
  - พรอมต์ 2: `warm acoustic bass (weight: 0.7)`
  - พรอมต์ 3: `subtle vinyl crackle (weight: 0.3)`

## ตัวอย่างพรอมต์

### ตัวอย่าง Lyria 3.5

- **Lo-Fi Study Beat**
  `none
  A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes piano chords, a relaxed boom-bap drum groove at 82 BPM, and a warm upright bassline. Instrumental only.`
- **เพลงป๊อป**
  `none
  An upbeat, feel-good indie-pop song in G major at 122 BPM. Bright acoustic guitar strumming, driving kick drum, handclaps, and warm female vocal harmonies. The lyrics describe an unforgettable summer road trip with friends.`
- **ไซเบอร์พังก์แบบภาพยนตร์**
  `none
  Dark, cinematic cyberpunk synthwave at 110 BPM in D minor. Heavy distorted bass, ominous arpeggiated analog synthesizers, distant metallic percussion, and an ethereal female vocalise swelling during the climax.`

### ชุดการบังคับเลี้ยวแบบเรียลไทม์ของ Lyria

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

## ขั้นตอนถัดไป

- [สร้างเพลงด้วย Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=th): สร้างเพลงเต็มและคลิปความยาว 30 วินาทีโดยใช้ Interactions API
- [การสร้างเพลงแบบเรียลไทม์ด้วย Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=th): สร้างแอปพลิเคชันการสตรีมเพลงแบบอินเทอร์แอกทีฟแบบเรียลไทม์ผ่าน WebSockets

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-18 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-18 UTC"],[],[]]
