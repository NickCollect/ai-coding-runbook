---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=he
fetched_at: 2026-08-17T02:28:12.459200+00:00
title: "\u05d9\u05e6\u05d9\u05e8\u05ea \u05de\u05d5\u05d6\u05d9\u05e7\u05d4 \u05d1\u05d6\u05de\u05df \u05d0\u05de\u05ea \u05d1\u05d0\u05de\u05e6\u05e2\u05d5\u05ea Lyria RealTime \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# יצירת מוזיקה בזמן אמת באמצעות Lyria RealTime

‫Gemini API, באמצעות [Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=he), מספק גישה למודל מתקדם ליצירת מוזיקה בסטרימינג בזמן אמת. היא מאפשרת למפתחים ליצור אפליקציות שבהן המשתמשים יכולים ליצור מוזיקה אינסטרומנטלית באופן אינטראקטיבי, לכוון אותה באופן רציף ולבצע אותה.

התכונה 'יצירת מוזיקה בזמן אמת' ב-Lyria משתמשת בחיבור סטרימינג קבוע ודו-כיווני עם השהיה נמוכה באמצעות [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API).

כדי לראות מה אפשר ליצור באמצעות Lyria RealTime, אתם יכולים לנסות אותו ב-AI Studio באמצעות האפליקציות [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=he) או [MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=he).

## יצירה ושליטה במוזיקה

הפעולה של Lyria RealTime דומה לזו של [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=he), בכך שהיא משתמשת ב-WebSockets כדי לשמור על תקשורת בזמן אמת עם המודל.

בדוגמה הבאה אפשר לראות איך יוצרים מוזיקה:

### Python

בדוגמה הזו, הפונקציה `client.aio.live.music.connect()` מאתחלת את הסשן של Lyria RealTime, ואז הפונקציה `session.set_weighted_prompts()` שולחת הנחיה ראשונית עם הגדרה ראשונית באמצעות `session.set_music_generation_config`, הפונקציה `session.play()` מתחילה את יצירת המוזיקה והפונקציה `receive_audio()` מוגדרת לעיבוד של נתחי האודיו שהיא מקבלת.

```
  import asyncio
  from google import genai
  from google.genai import types

  client = genai.Client(http_options={'api_version': 'v1beta'})

  async def main():
      async def receive_audio(session):
        """Example background task to process incoming audio."""
        while True:
          async for message in session.receive():
            audio_data = message.server_content.audio_chunks[0].data
            # Process audio...
            await asyncio.sleep(10**-12)

      async with (
        client.aio.live.music.connect(model='models/lyria-realtime-exp') as session,
        asyncio.TaskGroup() as tg,
      ):
        # Set up task to receive server messages.
        tg.create_task(receive_audio(session))

        # Send initial prompts and config
        await session.set_weighted_prompts(
          prompts=[
            types.WeightedPrompt(text='minimal techno', weight=1.0),
          ]
        )
        await session.set_music_generation_config(
          config=types.LiveMusicGenerationConfig(bpm=90, temperature=1.0)
        )

        # Start streaming music
        await session.play()
  if __name__ == "__main__":
      asyncio.run(main())
```

### JavaScript

בדוגמה הזו, הסשן של Lyria RealTime מאותחל באמצעות `client.live.music.connect()`, ואז נשלחת הנחיה ראשונית עם `session.setWeightedPrompts()` יחד עם הגדרה ראשונית באמצעות `session.setMusicGenerationConfig`, מתחילה יצירת המוזיקה באמצעות `session.play()` ומוגדר קריאה חוזרת (callback) של `onMessage` לעיבוד של חלקי האודיו שמתקבלים.

```
import { GoogleGenAI } from "@google/genai";
import Speaker from "speaker";
import { Buffer } from "buffer";

const client = new GoogleGenAI({
  apiKey: GEMINI_API_KEY,
    apiVersion: "v1beta" ,
});

async function main() {
  const speaker = new Speaker({
    channels: 2,       // stereo
    bitDepth: 16,      // 16-bit PCM
    sampleRate: 44100, // 44.1 kHz
  });

  const session = await client.live.music.connect({
    model: "models/lyria-realtime-exp",
    callbacks: {
      onmessage: (message) => {
        if (message.serverContent?.audioChunks) {
          for (const chunk of message.serverContent.audioChunks) {
            const audioBuffer = Buffer.from(chunk.data, "base64");
            speaker.write(audioBuffer);
          }
        }
      },
      onerror: (error) => console.error("music session error:", error),
      onclose: () => console.log("Lyria RealTime stream closed."),
    },
  });

  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: "Minimal techno with deep bass, sparse percussion, and atmospheric synths", weight: 1.0 },
    ],
  });

  await session.setMusicGenerationConfig({
    musicGenerationConfig: {
      bpm: 90,
      temperature: 1.0,
      audioFormat: "pcm16",  // important so we know format
      sampleRateHz: 44100,
    },
  });

  await session.play();
}

main().catch(console.error);
```

אחר כך תוכלו להשתמש במקשים `session.play()`, ‏ `session.pause()`, ‏ `session.stop()` ו-`session.reset_context()` כדי להתחיל את הסשן, להשהות אותו, לעצור אותו או לאפס אותו.

## התאמה של המוזיקה בזמן אמת

אתם יכולים לכוון את יצירת המוזיקה בזמן אמת על ידי שליחת הנחיות ועדכון פרמטרים של יצירה בזמן אמת.

### הנחיית Lyria בזמן אמת

במהלך השידור הפעיל, אתם יכולים לשלוח הודעות חדשות עם `WeightedPrompt` בכל שלב כדי לשנות את המוזיקה שנוצרה. המודל יעבור בצורה חלקה על סמך הקלט החדש.

ההנחיות צריכות להיות בפורמט הנכון עם `text` (ההנחיה בפועל) ו-`weight`. המאפיין `weight` יכול לקבל כל ערך חוץ מ-`0`. `1.0`
בדרך כלל זו נקודת התחלה טובה.

### Python

```
  from google.genai import types

  await session.set_weighted_prompts(
    prompts=[
      {"text": "Piano", "weight": 2.0},
      types.WeightedPrompt(text="Meditation", weight=0.5),
      types.WeightedPrompt(text="Live Performance", weight=1.0),
    ]
  )
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    weightedPrompts: [
      { text: 'Harmonica', weight: 0.3 },
      { text: 'Afrobeat', weight: 0.7 }
    ],
  });
```

שימו לב: המעברים בין המודלים יכולים להיות קצת פתאומיים כשמשנים את ההנחיות באופן קיצוני, ולכן מומלץ להטמיע מעין מעבר הדרגתי בין המודלים על ידי שליחת ערכי משקל ביניים למודל.

### עדכון ההגדרות

אתם יכולים לשנות את הפרמטרים של יצירת המוזיקה בזמן אמת כדי להשפיע על המוזיקה שנוצרת. אי אפשר רק לעדכן פרמטר, צריך להגדיר את כל ההגדרה, אחרת השדות האחרים יאופסו לערכי ברירת המחדל שלהם.

עדכון של ה-BPM או של הסולם הוא שינוי משמעותי במודל, ולכן צריך גם להורות לו לאפס את ההקשר באמצעות `reset_context()` כדי להתחשב בהגדרה החדשה. השידור לא ייפסק, אבל המעבר יהיה חד. אין צורך לעשות זאת לגבי הפרמטרים האחרים.

### Python

```
  from google.genai import types

  await session.set_music_generation_config(
    config=types.LiveMusicGenerationConfig(
      bpm=128,
      scale=types.Scale.D_MAJOR_B_MINOR,
      music_generation_mode=types.MusicGenerationMode.QUALITY
    )
  )
  await session.reset_context();
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    musicGenerationConfig: { 
      bpm: 120,
      density: 0.75,
      musicGenerationMode: MusicGenerationMode.QUALITY
    },
  });
  await session.reset_context();
```

## מדריך לכתיבת הנחיות ל-Lyria RealTime

הנה רשימה חלקית של הנחיות שאפשר להשתמש בהן כדי לתת הנחיות ל-Lyria RealTime:

- אמצעי תשלום: `303 Acid Bass, 808 Hip Hop Beat, Accordion, Alto Saxophone,
  Bagpipes, Balalaika Ensemble, Banjo, Bass Clarinet, Bongos, Boomy Bass,
  Bouzouki, Buchla Synths, Cello, Charango, Clavichord, Conga Drums,
  Didgeridoo, Dirty Synths, Djembe, Drumline, Dulcimer, Fiddle, Flamenco
  Guitar, Funk Drums, Glockenspiel, Guitar, Hang Drum, Harmonica, Harp,
  Harpsichord, Hurdy-gurdy, Kalimba, Koto, Lyre, Mandolin, Maracas, Marimba,
  Mbira, Mellotron, Metallic Twang, Moog Oscillations, Ocarina, Persian Tar,
  Pipa, Precision Bass, Ragtime Piano, Rhodes Piano, Shamisen, Shredding
  Guitar, Sitar, Slide Guitar, Smooth Pianos, Spacey Synths, Steel Drum, Synth
  Pads, Tabla, TR-909 Drum Machine, Trumpet, Tuba, Vibraphone, Viola Ensemble,
  Warm Acoustic Guitar, Woodwinds, ...`
- ז'אנר מוזיקלי: `Acid Jazz, Afrobeat, Alternative Country, Baroque, Bengal Baul,
  Bhangra, Bluegrass, Blues Rock, Bossa Nova, Breakbeat, Celtic Folk, Chillout,
  Chiptune, Classic Rock, Contemporary R&B, Cumbia, Deep House, Disco Funk,
  Drum & Bass, Dubstep, EDM, Electro Swing, Funk Metal, G-funk, Garage Rock,
  Glitch Hop, Grime, Hyperpop, Indian Classical, Indie Electronic, Indie Folk,
  Indie Pop, Irish Folk, Jam Band, Jamaican Dub, Jazz Fusion, Latin Jazz, Lo-Fi
  Hip Hop, Marching Band, Merengue, New Jack Swing, Minimal Techno, Moombahton,
  Neo-Soul, Orchestral Score, Piano Ballad, Polka, Post-Punk, 60s Psychedelic
  Rock, Psytrance, R&B, Reggae, Reggaeton, Renaissance Music, Salsa, Shoegaze,
  Ska, Surf Rock, Synthpop, Techno, Trance, Trap Beat, Trip Hop, Vaporwave,
  Witch house, ...`
- אווירה/תיאור: `Acoustic Instruments, Ambient, Bright Tones, Chill,
  Crunchy Distortion, Danceable, Dreamy, Echo, Emotional, Ethereal Ambience,
  Experimental, Fat Beats, Funky, Glitchy Effects, Huge Drop, Live Performance,
  Lo-fi, Ominous Drone, Psychedelic, Rich Orchestration, Saturated Tones,
  Subdued Melody, Sustained Chords, Swirling Phasers, Tight Groove,
  Unsettling, Upbeat, Virtuoso, Weird Noises, ...`

אלה רק כמה דוגמאות, אבל Lyria RealTime יכול לעשות הרבה יותר. נסו להשתמש בהנחיות משלכם!

## שיטות מומלצות

- אפליקציות לקוח צריכות להטמיע מאגר אודיו חזק כדי להבטיח הפעלה חלקה. כך אפשר להביא בחשבון את התנודות ברשת ואת השינויים הקלים בזמן האחזור של יצירת התוכן.
- הנחיות יעילות:
  - השתמשו בתיאורים בחוכמה. השתמשו בשמות תואר שמתארים את האווירה, הז'אנר והכלים.
  - לבצע איטרציות ולשנות את הכיוון בהדרגה. במקום לשנות את ההנחיה לגמרי, כדאי לנסות להוסיף או לשנות רכיבים כדי שהמוזיקה תשתנה בצורה חלקה יותר.
  - אפשר לשחק עם המשקל ב-`WeightedPrompt` כדי להשפיע על מידת ההשפעה של הנחיה חדשה על היצירה המתמשכת.

## פרטים טכניים

בקטע הזה מוסבר איך משתמשים ב-Lyria RealTime ליצירת מוזיקה.

### מפרטים

- פורמט פלט: אודיו PCM גולמי של 16 ביט
- תדירות הדגימה: 48kHz
- ערוצים: 2 (סטריאו)

### פקדים

אפשר להשפיע על יצירת המוזיקה בזמן אמת על ידי שליחת הודעות שמכילות:

- ‫`WeightedPrompt`: מחרוזת טקסט שמתארת רעיון מוזיקלי, ז'אנר, כלי נגינה, מצב רוח או מאפיין. אפשר לספק כמה הנחיות כדי לשלב השפעות. [למעלה](#steer-music) מופיעים פרטים נוספים על הדרך הטובה ביותר להנחות את Lyria RealTime.
- ‫`MusicGenerationConfig`: הגדרה לתהליך יצירת המוזיקה, שמשפיעה על המאפיינים של פלט האודיו. הפרמטרים כוללים:
  - ‫`guidance`: (float) טווח: `[0.0, 6.0]`. ברירת מחדל: `4.0`.
    ההגדרה הזו קובעת עד כמה המודל יפעל לפי ההנחיות. הנחיה גבוהה יותר משפרת את ההתאמה להנחיה, אבל המעברים חדים יותר.
  - ‫`bpm`: (int) טווח: `[60, 200]`.
    מגדירים את מספר הפעימות לדקה שרוצים למוזיקה שנוצרה. צריך להפעיל או להשהות את המודל או לאפס את ההקשר שלו כדי שהוא יתחשב ב-BPM החדש.
  - ‫`density`: (float) טווח: `[0.0, 1.0]`.
    שליטה בצפיפות של תווים או צלילים מוזיקליים. ערכים נמוכים יוצרים מוזיקה דלילה יותר, וערכים גבוהים יוצרים מוזיקה עשירה יותר.
  - ‫`brightness`: (float) טווח: `[0.0, 1.0]`.
    שינוי איכות הטון. ערכים גבוהים יותר יוצרים אודיו עם צליל 'בהיר' יותר, ובדרך כלל מדגישים תדרים גבוהים יותר.
  - ‫`scale`: (טיפוסים בני מנייה (enum))
    הגדרת הסולם המוזיקלי (מפתח ומצב) ליצירה. משתמשים ב[ערכי ה-enum‏ `Scale`](#scale-enum) שסופקו על ידי ה-SDK. צריך להפסיק/להפעיל או לאפס את ההקשר של המודל כדי שהשינוי יחול.
  - ‫`mute_bass`: (bool) ברירת מחדל: `False`.
    קובעת אם המודל יפחית את הבאס בפלט.
  - ‫`mute_drums`: (bool) ברירת מחדל: `False`.
    קובעת אם המודל יפחית את התוצאות של תופי הפלט.
  - ‫`only_bass_and_drums`: (bool) ברירת מחדל: `False`.
    הנחיית המודל לנסות להפיק רק בס ותופים.
  - ‫`music_generation_mode`: (Enum)
    מציין למודל אם להתמקד ב`QUALITY` (ערך ברירת מחדל) או ב`DIVERSITY` של המוזיקה. אפשר גם להגדיר את הערך `VOCALIZATION` כדי לאפשר למודל ליצור קולות ככלי נגינה נוסף (להוסיף אותם כהנחיות חדשות).
- ‫`PlaybackControl`: פקודות לשליטה בהיבטים של ההפעלה, כמו הפעלה, השהיה, עצירה או איפוס ההקשר.

בפרמטרים `bpm`, ‏ `density`, ‏ `brightness` ו-`scale`, אם לא מציינים ערך, המודל יחליט מה הכי טוב לפי ההנחיות הראשוניות.

אפשר גם להתאים אישית פרמטרים קלאסיים יותר כמו `temperature` (0.0 עד 3.0, ברירת מחדל 1.1), `top_k` (1 עד 1,000, ברירת מחדל 40) ו-`seed` (0 עד 2,147,483,647, נבחר באופן אקראי כברירת מחדל) ב-`MusicGenerationConfig`.

#### שינוי קנה המידה של ערכי enum

אלה כל הערכים של קנה המידה שהמודל יכול לקבל:

| הערך של הטיפוס בן המנייה (enum) | קנה מידה / מפתח |
| --- | --- |
| `C_MAJOR_A_MINOR` | דו מז'ור / לה מינור |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | רה במול מז'ור / סי במול מינור |
| `D_MAJOR_B_MINOR` | D major / B minor |
| `E_FLAT_MAJOR_C_MINOR` | מי במול מז'ור / דו מינור |
| `E_MAJOR_D_FLAT_MINOR` | מי מז'ור / דו# מינור/רה במול מינור |
| `F_MAJOR_D_MINOR` | פה מז'ור / רה מינור |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | סול במול מז'ור / מי במול מינור |
| `G_MAJOR_E_MINOR` | סול מז'ור / מי מינור |
| `A_FLAT_MAJOR_F_MINOR` | לה במול מז'ור / פה מינור |
| `A_MAJOR_G_FLAT_MINOR` | לה מז'ור / פה דיאז/סול במול מינור |
| `B_FLAT_MAJOR_G_MINOR` | סי במול מז'ור / סול מינור |
| `B_MAJOR_A_FLAT_MINOR` | B major / G♯/A♭ minor |
| `SCALE_UNSPECIFIED` | ברירת מחדל / המודל מחליט |

המודל מסוגל להנחות את התווים שמושמעים, אבל הוא לא מבחין בין מפתחות יחסיים. לכן, כל enum תואם גם לטון המז'ורי וגם לטון המינורי היחסי. לדוגמה, `C_MAJOR_A_MINOR` יתאים לכל הקלידים הלבנים של פסנתר, ו-`F_MAJOR_D_MINOR` יהיה כל הקלידים הלבנים חוץ מסי במול.

### מגבלות

- מוזיקה אינסטרומנטלית בלבד: המודל יוצר מוזיקה אינסטרומנטלית בלבד.
- בטיחות: המסננים בודקים את ההנחיות כדי לוודא שהן בטוחות. המערכת תתעלם מהנחיות שמפעילות את המסננים, ובמקרה כזה הסבר ייכתב בשדה `filtered_prompt` של הפלט.
- הוספת סימן מים: תמיד מתווסף סימן מים לפלט האודיו לצורך זיהוי, בהתאם לעקרונות [ה-AI האחראי](https://ai.google/responsibility/principles/?hl=he) שלנו.

## המאמרים הבאים

- ליצור שירים מלאים וטראקים של שירה עם [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=he),
- במקום מוזיקה, אפשר ללמוד איך ליצור שיחה עם כמה דוברים באמצעות [מודלים של TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he),
- [איך יוצרים תמונות](https://ai.google.dev/gemini-api/docs/image-generation?hl=he) או [סרטונים](https://ai.google.dev/gemini-api/docs/video?hl=he)
- במקום ליצור מוזיקה או אודיו, אתם יכולים ללמוד איך Gemini יכול [להבין קובצי אודיו](https://ai.google.dev/gemini-api/docs/audio?hl=he).
- מנהלים שיחה בזמן אמת עם Gemini באמצעות [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=he).

ב[ספר המתכונים](https://github.com/google-gemini/cookbook) אפשר למצוא עוד דוגמאות קוד ומדריכים.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-28 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-28 (שעון UTC)."],[],[]]
