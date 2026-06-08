---
source_url: https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=he
fetched_at: 2026-06-08T05:31:01.873345+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# יצירת המרת טקסט לדיבור (TTS)

‫Gemini API יכול להפוך קלט טקסט לאודיו עם דובר אחד או כמה דוברים באמצעות יכולות ההמרה של Gemini מטקסט לדיבור (TTS).
הפקת המרת טקסט לדיבור (TTS) היא *[ניתנת לשליטה](#controllable)*, כלומר אפשר להשתמש בשפה טבעית כדי לבנות אינטראקציות ולהנחות את *הסגנון*, *המבטא*, *הקצב* ו*הטון* של האודיו.

יכולת ה-TTS שונה מיצירת דיבור שמתבצעת באמצעות [Live API](https://ai.google.dev/gemini-api/docs/live?hl=he), שנועד לאודיו אינטראקטיבי לא מובנה ולתשומות ולתפוקות מולטימודאליות. ‫Live API מצטיין בהקשרים דינמיים של שיחות, אבל TTS דרך Gemini API מותאם לתרחישים שבהם נדרשת הקראה מדויקת של טקסט עם שליטה מדויקת בסגנון ובצליל, כמו יצירת פודקאסטים או ספרי אודיו.

במדריך הזה מוסבר איך ליצור אודיו עם דובר אחד או עם כמה דוברים מטקסט.

## לפני שמתחילים

חשוב לוודא שמשתמשים בגרסה של מודל Gemini 2.5 עם יכולות של Gemini להמרת טקסט לדיבור (TTS), כמו שמופיע בקטע [מודלים נתמכים](https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=he#supported-models). כדי לקבל תוצאות אופטימליות, כדאי לבחור את המודל שהכי מתאים לתרחיש השימוש הספציפי שלכם.

יכול להיות שיהיה לכם שימושי [לבחון את מודלי ה-TTS של Gemini 2.5 ב-AI Studio]

## המרת טקסט לדיבור (TTS) עם דובר יחיד

כדי להמיר טקסט לאודיו עם קריין יחיד, צריך להגדיר את אופן התגובה כ'אודיו' ולהעביר אובייקט `speech_config` עם שם של קול.
תצטרכו לבחור שם לקול מתוך [הקולות המוכנים מראש לפלט](#voices).

בדוגמה הזו, פלט האודיו מהמודל נשמר בקובץ wave:

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_modalities=["audio"],
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: "Say cheerfully: Have a wonderful day!",
      response_modalities: ['audio'],
      generation_config: {
         speech_config: [
            { voice: 'Kore' }
         ]
      },
    });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');

   await saveWaveFile('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_modalities": ["audio"],
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

אפשר לאחזר נתוני אודיו שנוצרו באמצעות המאפיין `interaction.output_audio`, שמחזיר את בלוק האודיו האחרון שנוצר. פרטים על מאפייני נוחות מופיעים במאמר [סקירה כללית על אינטראקציות](https://ai.google.dev/gemini-api/docs/interactions?hl=he#convenience-properties).

## המרת טקסט לדיבור (TTS) עם כמה דוברים

כדי להשתמש באודיו עם כמה רמקולים, צריך אובייקט `multi_speaker_voice_config` עם כל רמקול (עד 2) שמוגדר כ-`speaker_voice_config`.
צריך להגדיר כל `speaker` עם אותם שמות שמשמשים ב[הנחיה](#controllable):

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

 interaction = client.interactions.create(
     model="gemini-3.1-flash-tts-preview",
     input=prompt,
     response_modalities=["audio"],
     generation_config={
         "speech_config": [
             {"speaker": "Joe", "voice": "Kore"},
             {"speaker": "Jane", "voice": "Puck"}
         ]
     }
 )

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const client = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: prompt,
      response_modalities: ['audio'],
      generation_config: {
         speech_config: [
            { speaker: 'Joe', voice: 'Kore' },
            { speaker: 'Jane', voice: 'Puck' }
         ]
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');

   await saveWaveFile('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
  "model": "gemini-3.1-flash-tts-preview",
  "input": "TTS the following conversation between Joe and Jane: Joe: Hows it going today Jane? Jane: Not too bad, how about you?",
  "response_modalities": ["audio"],
  "generation_config": {
    "speech_config": [
      { "speaker": "Joe", "voice": "Kore" },
      { "speaker": "Jane", "voice": "Puck" }
    ]
  }
}'
```

## שליטה בסגנון הדיבור באמצעות הנחיות

אתם יכולים לשלוט בסגנון, בטון, במבטא ובקצב באמצעות הנחיות בשפה טבעית, גם בהמרת טקסט לדיבור עם דובר אחד וגם עם כמה דוברים.
לדוגמה, בהנחיה עם דובר אחד, אפשר לומר:

```
Say in an spooky whisper:
"By the pricking of my thumbs...
Something wicked this way comes"
```

בהנחיה עם כמה דוברים, צריך לספק למודל את השם של כל דובר ואת התמליל המתאים. אפשר גם לספק הנחיות לכל דובר בנפרד:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... what's on the agenda today?
Speaker2: You're never going to guess!
```

כדי להדגיש את הסגנון או הרגש שרוצים להעביר, אפשר להשתמש ב[אפשרות קולית](#voices) שמתאימה להם. בהנחיה הקודמת, לדוגמה, יכול להיות שההגייה של *אנסלדוס* תדגיש את המילים 'עייף' ו'משועמם', בעוד שהטון העליז של  יכול להשלים את המילים 'נרגש' ו'שמח'.

## יצירת הנחיה להמרה לאודיו

מודלים של TTS מוציאים רק אודיו, אבל אפשר להשתמש ב[מודלים אחרים](https://ai.google.dev/gemini-api/docs/models?hl=he) כדי ליצור תמליל, ואז להעביר את התמליל הזה למודל ה-TTS כדי שיקרא אותו בקול.

### Python

```
from google import genai

client = genai.Client()

transcript_interaction = client.interactions.create(
   model="gemini-3.5-flash",
   input="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam."""
)
transcript = transcript_interaction.output_text

tts_interaction = client.interactions.create(
   model="gemini-3.1-flash-tts-preview",
   input=transcript,
   response_modalities=["audio"],
   generation_config={
      "speech_config": [
         {"speaker": "Dr. Anya", "voice": "Kore"},
         {"speaker": "Liam", "voice": "Puck"}
      ]
   }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {

const transcriptInteraction = await client.interactions.create({
   model: "gemini-3.5-flash",
   input: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const ttsInteraction = await client.interactions.create({
   model: "gemini-3.1-flash-tts-preview",
   input: transcriptInteraction.output_text,
   response_modalities: ['audio'],
   generation_config: {
      speech_config: [
         { speaker: "Dr. Anya", voice: "Kore" },
         { speaker: "Liam", voice: "Puck" }
      ]
   }
  });
}

await main();
```

## אפשרויות קול

מודלים של TTS תומכים ב-30 אפשרויות הקול הבאות בשדה `voice_name`:

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** -- *Upbeat* | ‫**Charon** – *Informative* |
| **Kore** -- *Firm* | ‫**Fenrir** -- *Excitable* | **Leda** -- *Youthful* |
| ‫**Orus** -- *Firm* | ‫**Aoede** – *Breezy* | ‫**Callirrhoe** – *נינוח* |
| **Autonoe** -- *Bright* | **Enceladus** -- *Breathy* | ‫**Iapetus** -- *Clear* |
| **Umbriel** -- *Easy-going* | **Algieba** -- *Smooth* | **Despina** -- *Smooth* |
| ‫**Erinome** -- *Clear* | ‫**Algenib** – *מחוספס* | **Rasalgethi** -- *Informative* |
| ‫**Laomedeia** -- *Upbeat* | ‫**Achernar** -- *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | ‫**Gacrux** – *למבוגרים* | ‫**Pulcherrima** -- *Forward* |
| ‫**Achird** – *ידידותי* | ‫**Zubenelgenubi** – *שגרתי* | ‫**Vindemiatrix** -- *Gentle* |
| **Sadachbia** -- *Lively* | **Sadaltager** -- *Knowledgeable* | ‫**Sulafat** -- *Warm* |

אפשר לשמוע את כל האפשרויות של הקולות ב

## שפות נתמכות

מודלים של TTS מזהים את שפת הקלט באופן אוטומטי. השפות הנתמכות הן:

| שפה | קוד BCP-47 | שפה | קוד BCP-47 |
| --- | --- | --- | --- |
| ערבית | ar | פיליפינית | fil |
| בנגלית | bn | פינית | fi |
| הולנדית | nl | גליציאנית | gl |
| אנגלית | en | גאורגית | ka |
| צרפתית | fr | יוונית | el |
| גרמנית | de | גוג'ראטי | gu |
| הינדי | hi | קריאולית האיטית | ht |
| אינדונזית | id [מזהה] | עברית | הוא |
| איטלקית | it | הונגרית | hu |
| יפנית | ja | איסלנדית | is |
| קוריאנית | ko | ג'אווה | jv |
| מראטהית | mr | קנאדה | kn |
| פולנית | pl | קונקאני | kok |
| פורטוגזית | pt | לאו | lo |
| רומנית | ro | מוזיקה לטינית | לה |
| רוסית | ru | לטבית | lv |
| ספרדית | es | ליטאית | lt |
| טמילית | ta | לוקסמבורגית | lb |
| טלוגו | te | מקדונית | mk |
| תאית | th | מאיטילית | mai |
| טורקית | tr | מלגשית | מ"ג |
| אוקראינית | uk | מלאית | ms |
| וייטנאמית | vi | מליאלאם | ml |
| אפריקאנס | af | מונגולית | mn |
| אלבנית | sq | נפאלית | ne |
| אמהרית | am | נורווגית, ספרותית | nb |
| ארמנית | hy | נורווגית, נינורסק | nn |
| אזרית | az | אודיה | או |
| בסקית | eu | פשטו | ps |
| בלארוסית | be | פרסית | fa |
| בולגרית | bg | פנג'אבי | pa |
| בורמזית | my | סרבית | sr |
| קטלאנית | ca | סינדהית | SD |
| סבואנו | ceb | סינהאלה | si |
| סינית, מנדרינית | cmn | סלובקית | sk |
| קרואטית | שעה | סלובנית | sl |
| צ'כית | cs | סווהילי | sw |
| דנית | da | שוודית | sv |
| אסטונית | et | אורדו | ur |

## מודלים נתמכים

| מודל | דובר יחיד | מערכת רמקולים |
| --- | --- | --- |
| [תצוגה מקדימה של Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=he) | ✔️ | ✔️ |
| [Gemini 2.5 Flash Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=he) | ✔️ | ✔️ |
| [תצוגה מקדימה של Gemini ‎2.5 Pro TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=he) | ✔️ | ✔️ |

## מדריך לכתיבת הנחיות

מודל **Gemini Native Audio Generation Text-to-Speech (TTS)** שונה ממודלים רגילים של TTS בכך שהוא מבוסס על מודל שפה גדול שיודע ***לא רק מה לומר, אלא גם איך לומר את זה***.

אפשר לחשוב על הנחיה מתקדמת כהוראת מערכת שהמודל צריך לפעול לפיה. זו דרך לספק למודל יותר הקשר ולשלוט בביצועים שלו.

כדי להשתמש ביכולת הזו, המשתמשים יכולים לדמיין שהם במאים שמגדירים סצנה לקריין וירטואלי. כדי ליצור הנחיה, מומלץ להשתמש ברכיבים הבאים: **פרופיל אודיו** שמגדיר את הזהות והארכיטיפ העיקריים של הדמות, **תיאור סצנה** שמגדיר את הסביבה הפיזית ואת האווירה הרגשית, ו**הערות הבמאי** שמציעות הנחיות מדויקות יותר לגבי סגנון, מבטא ושליטה בקצב.

הוראות מפורטות כמו מבטא אזורי מדויק, מאפיינים פרא-לשוניים ספציפיים (למשל, נשימה) או קצב דיבור, מאפשרות למשתמשים לנצל את המודעות להקשר של המודל כדי ליצור ביצועים אודיו דינמיים, טבעיים ומלאי הבעה. כדי להשיג ביצועים אופטימליים, מומלץ שההנחיות ל**תסריט** ולהנחיות הבימוי יהיו תואמות, *כך שההנחיה 'מי אומר את זה'* תתאים להנחיות *'מה נאמר'* ו*'איך זה נאמר'*.

מטרת המדריך הזה היא לספק הנחיות בסיסיות ולעורר רעיונות לפיתוח חוויות אודיו באמצעות יצירת אודיו ב-Gemini TTS. אנחנו סקרנים לראות מה תיצרו!

### תגי אודיו

תגים הם משנים מוטבעים כמו `[whispers]` או `[laughs]` שמאפשרים לכם שליטה פרטנית בהצגת המודעות. אתם יכולים להשתמש בהם כדי לשנות את הטון, הקצב והאווירה הרגשית של שורה או קטע בתמליל. אפשר גם להשתמש בהם כדי להוסיף קריאות ביניים וכמה צלילים לא מילוליים אחרים לביצוע, כמו `[cough]`, `[sighs]` או `[gasp]`.

אין רשימה מלאה של תגים שעובדים ושלא עובדים, ולכן מומלץ להתנסות עם רגשות והבעות שונים כדי לראות איך הפלט משתנה.

אם התמליל לא באנגלית, כדי לקבל את התוצאות הכי טובות מומלץ להשתמש בתגי אודיו באנגלית.

**יצירתיות עם תגי אודיו**

כדי להראות את סוגי הווריאציות שאפשר לקבל באמצעות תגי אודיו, הנה כמה דוגמאות שבהן נאמר אותו הדבר, אבל אופן ההצגה משתנה בהתאם לתגים שבהם נעשה שימוש.

כדי לשנות את ההדגשה של הדיבור, אפשר להוסיף תגים בתחילת השורה כדי שהדובר ישמע נרגש, משועמם או מסויג:

- `[excitedly]` שלום, אני מודל חדש של המרת טקסט לדיבור, ואני יכול להגיד דברים בהרבה דרכים שונות. איך אוכל לעזור לך?
- `[bored]` היי, אני מודל חדש של המרת טקסט לדיבור…
- `[reluctantly]` היי, אני מודל חדש של המרת טקסט לדיבור…

אפשר גם להשתמש בתגים כדי לשנות את קצב ההצגה, או כדי לשלב בין התג pace לבין התג emphasis:

- `[very fast]` היי, אני מודל חדש של המרת טקסט לדיבור…
- `[very slow]` היי, אני מודל חדש של המרת טקסט לדיבור…
- `[sarcastically, one painfully slow word at a time]` היי, אני מודל חדש של המרת טקסט לדיבור…

יש לכם גם שליטה מדויקת על חלקים ספציפיים, כך שאתם יכולים ללחוש חלק אחד ולצעוק חלק אחר.

- `[whispers]` שלום, אני מודל חדש של המרת טקסט לדיבור, `[shouting]` ואני יכול להגיד דברים בדרכים שונות. `[whispers]` איך אוכל לעזור לך?

אתם יכולים גם להתנסות בכל רעיון יצירתי שתרצו:

- `[like a cartoon dog]` היי, אני מודל חדש של המרת טקסט לדיבור…
- `[like dracula]` היי, אני מודל חדש של המרת טקסט לדיבור…

תגים נפוצים:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

תגים מאפשרים שליטה מהירה בהעברה של התמליל. כדי לקבל שליטה רבה עוד יותר, אפשר לשלב אותם עם הנחיה להגדרת הקשר כדי להגדיר את הטון והאווירה הכלליים של הביצוע.

### מבנה ההנחיות

הנחיה טובה כוללת את הרכיבים הבאים, שמשולבים יחד כדי ליצור ביצועים מצוינים:

- **פרופיל אודיו** – הגדרה של דמות לקול, כולל זהות, ארכיטיפ ומאפיינים אחרים כמו גיל, רקע וכו'.
- **סצנה** – מגדירה את הבמה. מתאר את הסביבה הפיזית ואת האווירה.
- **הערות הבמאי** – הנחיות לגבי הביצועים שבהן אפשר לפרט אילו הוראות חשובות לכישרון הווירטואלי. דוגמאות: סגנון, נשימה, קצב, הבעה ומבטא.
- **הקשר לדוגמה** – מספק למודל נקודת התחלה הקשרית, כך שהשחקן הווירטואלי ייכנס לסצנה שהגדרתם באופן טבעי.
- ‫**Transcript** (תמליל) – הטקסט שהמודל יקריא. כדי לקבל את הביצועים הטובים ביותר, חשוב לזכור שהנושא של התמליל וסגנון הכתיבה צריכים להיות קשורים להוראות שאתם נותנים.
- **תגי אודיו** – משנים שאפשר להוסיף לתמליל כדי לשנות את אופן ההקראה של חלק מסוים בטקסט, כמו `[whispers]` או `[shouting]`.

דוגמה להנחיה מלאה:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

### DIRECTOR'S NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
* Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions - no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
Yes, massive vibes in the studio! You are locked in and it is absolutely
popping off in London right now. If you're stuck on the tube, or just sat
there pretending to work... stop it. Seriously, I see you. Turn this up!
We've got the project roadmap landing in three, two... let's go!
```

### שיטות מפורטות ליצירת הנחיות

כדאי לפרק כל רכיב בהנחיה באופן הבא:

#### פרופיל אודיו

תאר בקצרה את הפרסונה של הדמות.

- **שם**. כשנותנים לדמות שם, המודל מקבל יותר פרטים על הדמות ומשפר את הביצועים. כדאי להתייחס לדמות בשם כשמגדירים את הסצנה וההקשר.
- **תפקיד**. הזהות והארכיטיפ העיקריים של הדמות שמופיעה בסצנה. לדוגמה, שדרן רדיו, מגיש פודקאסט, כתב חדשות וכו'.

דוגמאות:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### סצינה

מגדירים את ההקשר של הסצנה, כולל המיקום, האווירה ופרטים סביבתיים שיוצרים את הטון והאווירה. תאר מה קורה מסביב לדמות ואיך זה משפיע עליה. הסצנה מספקת את ההקשר הסביבתי לכל האינטראקציה ומנחה את ביצועי המשחק בצורה עדינה ואורגנית.

דוגמאות:

```
## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
```

```
## THE SCENE: Homegrown Studio
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
```

#### הערות הבמאי

הקטע החשוב הזה כולל הנחיות ספציפיות לשיפור הביצועים. אפשר לדלג על כל הרכיבים האחרים, אבל מומלץ לכלול את הרכיב הזה.

חשוב להגדיר רק את מה שחשוב לביצועים, ולהיזהר שלא להגדיר יותר מדי. יותר מדי כללים מחמירים יגבילו את היצירתיות של המודלים, ועשויים להוביל לביצועים גרועים יותר. חשוב ליצור איזון בין תיאור התפקיד והסצנה לבין כללי הביצוע הספציפיים.

ההנחיות הנפוצות ביותר הן **סגנון, קצב ומבטא**, אבל המודל לא מוגבל להנחיות האלה ולא נדרש להן. אתם יכולים לכלול הוראות מותאמות אישית כדי לציין פרטים נוספים שחשובים לביצועים, ולפרט כמה שצריך.

לדוגמה:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**סגנון:**

הגדרת הטון והסגנון של הדיבור שנוצר. כדאי לכלול הנחיות כמו קצבי, אנרגטי, רגוע, משועמם וכו' כדי להנחות את הביצוע. הקפידו על תיאוריות וספקו כמה שיותר פרטים: *"התלהבות מדבקת. המאזין צריך להרגיש שהוא חלק מאירוע קהילתי עצום ומרגש".* עדיף על *"אנרגטי ונלהב".*

אפשר גם לנסות מונחים פופולריים בתעשיית הקריינות, כמו "חיוך קולי". אפשר להוסיף כמה מאפייני סגנון שרוצים.

דוגמאות:

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

יותר עומק

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

רמה למתקדמים מאוד

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**מבטא:**

תאר את המבטא שנבחר. ככל שהתיאור יהיה מפורט יותר, התוצאות יהיו טובות יותר. לדוגמה, עדיף להשתמש בביטוי *מבטא בריטי כמו שמדברים בקרוידון, אנגליה* במקום *מבטא בריטי*.

דוגמאות:

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a from Brixton, London
...
```

**קצב:**

הקצב הכללי והשינויים בקצב לאורך היצירה.

דוגמאות:

פשוט

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

עומק רב יותר

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

רמה למתקדמים מאוד

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

**רוצים לנסות?**

אתם יכולים לנסות בעצמכם את הדוגמאות האלה ב[אפליקציית TTS](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=he) ולתת ל-Gemini להושיב אתכם על כיסא הבמאי. כדי ליצור ביצועים קוליים מעולים, כדאי לזכור את הטיפים הבאים:

- חשוב לזכור שההנחיה כולה צריכה להיות עקבית – התסריט והבימוי משלימים זה את זה כדי ליצור ביצוע מוצלח.
- לא צריך לתאר כל דבר, לפעמים כדאי לתת למודל מקום למלא את הפערים כדי שהתוצאה תהיה טבעית. (Just like a talented actor)
- אם אתם מרגישים תקועים, אתם יכולים לבקש מ-Gemini עזרה בכתיבת התסריט או בביצוע.

## מגבלות

- מודלים של TTS יכולים לקבל רק קלט טקסט ולהפיק פלט אודיו.
- לסשן TTS יש מגבלת [חלון הקשר](https://ai.google.dev/gemini-api/docs/long-context?hl=he) של 32 אלף טוקנים.
- בקטע [שפות](https://ai.google.dev/gemini-api/docs/interactions/speech-generation?hl=he#languages) מפורטות השפות הנתמכות.
- ה-TTS לא תומך בסטרימינג.

ההגבלות הבאות חלות באופן ספציפי כשמשתמשים במודל טרום ההשקה של Gemini 3.1 Flash
TTS ליצירת דיבור:

- **חוסר עקביות בקול בהשוואה להוראות בהנחיה:** יכול להיות שהפלט של המודל לא תמיד יתאים בדיוק לרמקול שנבחר, ולכן האודיו לא יישמע כמו שציפיתם. כדי למנוע חוסר התאמה בטונים (למשל, קול גברי עוצמתי שמנסה לדבר כמו ילדה צעירה), חשוב לוודא שהטון וההקשר של ההנחיה תואמים באופן טבעי לפרופיל של הדובר שנבחר.
- **איכות של פלט ארוך יותר:** איכות הדיבור והעקביות עשויות להתחיל להידרדר בפלט שנוצר ואורכו יותר מכמה דקות. מומלץ לפצל את התמלילים לחלקים קטנים יותר.
- **החזרת אסימוני טקסט מדי פעם:** המודל מחזיר מדי פעם אסימוני טקסט במקום אסימוני אודיו, ולכן השרת לא מצליח לבצע את הבקשה ומחזיר שגיאת `500`. השגיאה הזו מתרחשת באופן אקראי באחוז קטן מאוד של הבקשות, ולכן כדאי להטמיע באפליקציה לוגיקה אוטומטית לניסיון חוזר כדי לטפל בה.
- **דחיות שגויות של מסווג ההנחיות:** יכול להיות שהנחיות לא ברורות לא יפעילו את מסווג סינתזת הדיבור, וכתוצאה מכך הבקשה תידחה (`PROHIBITED_CONTENT`) או שהמודל יקרא בקול רם את הוראות הסגנון ואת הערות הבמאי. כדי לוודא שההנחיות תקינות, מוסיפים פתיח ברור שמנחה את המודל לסנתז דיבור, ומציינים באופן מפורש איפה מתחיל התמליל הממשי של הדיבור.

## המאמרים הבאים

- [ממשק Gemini Live API](https://ai.google.dev/gemini-api/docs/live?hl=he) מציע אפשרויות אינטראקטיביות ליצירת אודיו שאפשר לשלב עם אמצעים אחרים.
- כדי לקבל מידע על עבודה עם *קלט* אודיו, אפשר לעיין במדריך [הבנת אודיו](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-05-28 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-05-28 (שעון UTC)."],[],[]]
