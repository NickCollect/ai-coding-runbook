---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=he
fetched_at: 2026-05-05T20:44:36.185340+00:00
title: "\u05d9\u05e6\u05d9\u05e8\u05ea \u05d4\u05de\u05e8\u05ea \u05d8\u05e7\u05e1\u05d8 \u05dc\u05d3\u05d9\u05d1\u05d5\u05e8 (TTS) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# יצירת המרת טקסט לדיבור (TTS)

‫Gemini API יכול להפוך קלט טקסט לאודיו עם דובר אחד או כמה דוברים באמצעות יכולות ההמרה של Gemini מטקסט לדיבור (TTS).
הפקת המרת טקסט לדיבור (TTS) היא *[ניתנת לשליטה](#controllable)*, כלומר אפשר להשתמש בשפה טבעית כדי לבנות אינטראקציות ולהנחות את *הסגנון*, *המבטא*, *הקצב* ו*הטון* של האודיו.

[לניסיון ב-Google AI Studio](https://aistudio.google.com/apps/bundled/voice-library?showPreview=truew&hl=he)

יכולת ה-TTS שונה מיצירת דיבור שמתבצעת באמצעות [Live API](https://ai.google.dev/gemini-api/docs/live?hl=he), שנועד לאודיו אינטראקטיבי ולא מובנה, ולקלט ולפלט מולטי-מודאליים. ‫Live API מצטיין בהקשרים דינמיים של שיחות, אבל TTS דרך Gemini API מותאם לתרחישים שבהם נדרשת הקראה מדויקת של טקסט עם שליטה מדויקת בסגנון ובצליל, כמו יצירת פודקאסטים או ספרי אודיו.

במדריך הזה מוסבר איך ליצור אודיו עם דובר אחד או עם כמה דוברים מטקסט.

## לפני שמתחילים

חשוב לוודא שאתם משתמשים בגרסה של מודל Gemini עם יכולות של המרת טקסט לדיבור (TTS) ב-Gemini, כמו שמופיע בקטע [מודלים נתמכים](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he#supported-models). כדי לקבל תוצאות אופטימליות, כדאי לבחור את המודל שהכי מתאים לתרחיש השימוש הספציפי שלכם.

מומלץ [לבדוק את מודלי ה-TTS של Gemini ב-AI Studio](https://aistudio.google.com/generate-speech?hl=he) לפני שמתחילים לפתח.

## המרת טקסט לדיבור (TTS) עם דובר יחיד

כדי להמיר טקסט לאודיו עם דובר אחד, מגדירים את אופן התגובה ל'אודיו' ומעבירים אובייקט `SpeechConfig` עם ההגדרה `VoiceConfig`.
תצטרכו לבחור שם קול מתוך [הקולות המובנים של הפלט](#voices).

בדוגמה הזו, האודיו שנוצר על ידי המודל נשמר בקובץ wave:

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents="Say cheerfully: Have a wonderful day!",
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
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
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: 'Say cheerfully: Have a wonderful day!' }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               voiceConfig: {
                  prebuiltVoiceConfig: { voiceName: 'Kore' },
               },
            },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "parts":[{
            "text": "Say cheerfully: Have a wonderful day!"
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }
        },
        "model": "gemini-3.1-flash-tts-preview",
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode >out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## המרת טקסט לדיבור (TTS) עם כמה דוברים

כדי להשתמש באודיו עם כמה רמקולים, צריך אובייקט `MultiSpeakerVoiceConfig` עם כל רמקול (עד 2) שמוגדר כ-`SpeakerVoiceConfig`.
צריך להגדיר כל `speaker` עם אותם שמות שמשמשים ב[הנחיה](#controllable):

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
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

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=prompt,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Joe',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Jane',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
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
   const ai = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: prompt }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               multiSpeakerVoiceConfig: {
                  speakerVoiceConfigs: [
                        {
                           speaker: 'Joe',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Kore' }
                           }
                        },
                        {
                           speaker: 'Jane',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Puck' }
                           }
                        }
                  ]
               }
            }
      }
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
  "contents": [{
    "parts":[{
      "text": "TTS the following conversation between Joe and Jane:
                Joe: Hows it going today Jane?
                Jane: Not too bad, how about you?"
    }]
  }],
  "generationConfig": {
    "responseModalities": ["AUDIO"],
    "speechConfig": {
      "multiSpeakerVoiceConfig": {
        "speakerVoiceConfigs": [{
            "speaker": "Joe",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }, {
            "speaker": "Jane",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Puck"
              }
            }
          }]
      }
    }
  },
  "model": "gemini-3.1-flash-tts-preview",
}' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
    base64 --decode > out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## שליטה בסגנון הדיבור באמצעות הנחיות

אתם יכולים לשלוט בסגנון, בטון, במבטא ובקצב באמצעות הנחיות בשפה טבעית או [תגי אודיו](#transcript-tags), גם בהמרת טקסט לדיבור עם דובר אחד וגם עם כמה דוברים.
לדוגמה, בהנחיה עם דובר אחד, אפשר לומר:

```
Say in an spooky voice:
"By the pricking of my thumbs... [short pause]
[whisper] Something wicked this way comes"
```

בהנחיה עם כמה דוברים, צריך לספק למודל את השם של כל דובר ואת התמליל המתאים. אפשר גם לספק הנחיות לכל דובר בנפרד:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... [yawn] what's on the agenda today?
Speaker2: You're never going to guess!
```

כדי להדגיש את הסגנון או הרגש שרוצים להעביר, אפשר לנסות להשתמש ב[אפשרות קולית](#voices) שמתאימה להם. בהנחיה הקודמת, לדוגמה, יכול להיות שההגייה של *אנסלדוס* תדגיש את המילים 'עייף' ו'משועמם', בעוד שהטון העליז של  יכול להשלים את המילים 'נרגש' ו'שמח'.

## יצירת הנחיה להמרה לאודיו

מודלים של TTS מוציאים רק אודיו, אבל אפשר להשתמש ב[מודלים אחרים](https://ai.google.dev/gemini-api/docs/models?hl=he) כדי ליצור תמליל, ואז להעביר את התמליל הזה למודל ה-TTS כדי שיקרא אותו בקול.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

transcript = client.models.generate_content(
   model="gemini-3-flash-preview",
   contents="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam.""").text

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=transcript,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Dr. Anya',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Liam',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

# ...Code to handle audio output
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {

const transcript = await ai.models.generateContent({
   model: "gemini-3-flash-preview",
   contents: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const response = await ai.models.generateContent({
   model: "gemini-3.1-flash-tts-preview",
   contents: transcript,
   config: {
      responseModalities: ['AUDIO'],
      speechConfig: {
         multiSpeakerVoiceConfig: {
            speakerVoiceConfigs: [
                   {
                     speaker: "Dr. Anya",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Kore"},
                     }
                  },
                  {
                     speaker: "Liam",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Puck"},
                    }
                  }
                ]
              }
            }
      }
  });
}
// ..JavaScript code for exporting .wav file for output audio

await main();
```

## אפשרויות קול

מודלים של TTS תומכים ב-30 אפשרויות הקול הבאות בשדה `voice_name`:

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** -- *Upbeat* | ‫**Charon** – *Informative* |
| **Kore** -- *Firm* | ‫**Fenrir** -- *Excitable* | ‫**Leda** – *צעיר* |
| ‫**Orus** -- *Firm* | ‫**Aoede** – *Breezy* | ‫**Callirrhoe** – *נינוח* |
| **Autonoe** -- *Bright* | **Enceladus** -- *Breathy* | ‫**Iapetus** – *Clear* |
| **Umbriel** -- *Easy-going* | **Algieba** -- *Smooth* | ‫**Despina** – *Smooth* |
| ‫**Erinome** -- *Clear* | ‫**Algenib** -- *Gravelly* | **Rasalgethi** -- *Informative* |
| ‫**Laomedeia** -- *Upbeat* | ‫**Achernar** -- *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | ‫**Gacrux** -- *Mature* | ‫**Pulcherrima** -- *Forward* |
| ‫**Achird** – *ידידותי* | ‫**Zubenelgenubi** – *שגרתי* | ‫**Vindemiatrix** -- *Gentle* |
| **Sadachbia** -- *Lively* | **Sadaltager** -- *Knowledgeable* | ‫**Sulafat** -- *חמה* |

אפשר לשמוע את כל האפשרויות של הקול ב-[AI Studio](https://aistudio.google.com/generate-speech?hl=he).

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

| דגם | דובר יחיד | מערכת רמקולים |
| --- | --- | --- |
| [תצוגה מקדימה של Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=he) | ✔️ | ✔️ |
| [Gemini 2.5 Flash Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=he) | ✔️ | ✔️ |
| [תצוגה מקדימה של Gemini ‎2.5 Pro TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=he) | ✔️ | ✔️ |

## מדריך לכתיבת הנחיות

מודל **Gemini Native Audio Generation Text-to-Speech (TTS)** שונה ממודלים מסורתיים של TTS בכך שהוא מבוסס על מודל שפה גדול שיודע ***לא רק מה לומר, אלא גם איך לומר את זה***.

המודל יפרש באופן טבעי תמליל ויקבע איך להעביר את המילים שלכם. תמלילים פשוטים בלי הנחיות נוספות נשמעים טבעיים. אבל Gemini TTS כולל גם כלים שבעזרתם אפשר לשלוט בו.

מטרת המדריך הזה היא לספק הנחיות בסיסיות ולעורר רעיונות לפיתוח חוויות אודיו. נתחיל עם **תגים** לשליטה מהירה בתוך השורה, ואז נסביר על **מבני הנחיות** מתקדמים לשיפור הביצועים.

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

התגים מאפשרים לשלוט בקלות ובמהירות בהצגת התמליל. כדי לקבל שליטה רבה יותר, אפשר לשלב אותם עם הנחיה להגדרת הקשר כדי להגדיר את הטון והאווירה הכלליים של הביצוע.

### הנחיות מתקדמות

אפשר לחשוב על הנחיה מתקדמת כהוראת מערכת שהמודל צריך לפעול לפיה. זו דרך לספק למודל יותר הקשר ולשלוט בביצועים שלו.

הנחיה טובה כוללת את הרכיבים הבאים, שמשולבים יחד כדי ליצור ביצועים מצוינים:

- **פרופיל אודיו** – הגדרה של דמות לקול, כולל זהות, ארכיטיפ ומאפיינים אחרים כמו גיל, רקע וכו'.
- **סצנה** – מגדירה את הבמה. מתאר את הסביבה הפיזית ואת האווירה.
- **הערות הבמאי** – הנחיות לשיפור הביצועים שבהן אפשר לפרט אילו הוראות חשובות לכישרון הווירטואלי. דוגמאות: סגנון, נשימה, קצב, הבעה ומבטא.
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
with A "bouncing" cadence. High-speed delivery with fluid transitions — no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
[excitedly] Yes, massive vibes in the studio! You are locked in and it is
absolutely popping off in London right now. If you're stuck on the tube, or
just sat there pretending to work... stop it. Seriously, I see you.
[shouting] Turn this up! We've got the project roadmap landing in three,
two... let's go!
```

### שיטות מפורטות ליצירת הנחיות

בואו נפרט כל רכיב בהנחיה.

#### פרופיל אודיו

תאר בקצרה את הפרסונה של הדמות.

- **שם**. כשנותנים לדמות שם, המודל מקבל יותר פרטים על הדמות ומשפר את הביצועים. כדאי להתייחס לדמות בשם כשמגדירים את הסצנה וההקשר.
- **תפקיד**. הזהות והארכיטיפ העיקריים של הדמות שמופיעה בסצנה. לדוגמה: שדרן רדיו, מגיש פודקאסט, כתב חדשות וכו'.

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

חשוב להגדיר רק את מה שחשוב לביצועים, ולהיזהר שלא להגדיר יותר מדי. יותר מדי כללים מחמירים יגבילו את היצירתיות של המודלים, ועלולים להוביל לביצועים גרועים יותר. חשוב לאזן בין תיאור התפקיד והסצנה לבין כללי הביצוע הספציפיים.

ההנחיות הנפוצות ביותר הן **סגנון, קצב ומבטא**, אבל המודל לא מוגבל להנחיות האלה ולא דורש אותן. אתם יכולים לכלול הוראות מותאמות אישית כדי לציין פרטים נוספים שחשובים לביצועים שלכם, ולפרט כמה שצריך.

לדוגמה:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**סגנון:**

הגדרת הטון והסגנון של הדיבור שנוצר. כדאי לכלול הנחיות כמו קצבי, אנרגטי, רגוע, משועמם וכו' כדי להנחות את הביצוע. הקפידו על תיאוריות וספקו כמה שיותר פרטים: *"התלהבות מדבקת. ההנחיה "המאזין צריך להרגיש שהוא חלק מאירוע קהילתי גדול ומרגש"* עדיפה על *"אנרגטי ונלהב"*.

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

מתארים את המבטא הרצוי. ככל שהתיאור יהיה מפורט יותר, התוצאות יהיו טובות יותר. לדוגמה, אפשר להשתמש בביטוי *מבטא בריטי כמו שמדברים בקרוידון, אנגליה* במקום *מבטא בריטי*.

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
Accent: Jaz is a DJ from Brixton, London
...
```

**קצב ניצול:**

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

#### תמליל ותגי אודיו

התמליל הוא המילים המדויקות שהמודל יגיד. תג אודיו הוא מילה בסוגריים מרובעים שמציינת איך צריך להגיד משהו, שינוי בטון או קריאת ביניים.

```
### TRANSCRIPT

I know right, [sarcastically] I couldn't believe it. [whispers] She should have totally left
at that point.

[cough] Well, [sighs] I guess it doesn't matter now.
```

**רוצים לנסות?**

אתם יכולים לנסות בעצמכם כמה מהדוגמאות האלה ב-[AI Studio](https://aistudio.google.com/generate-speech?hl=he), להתנסות ב[אפליקציית ה-TTS](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=he) שלנו ולתת ל-Gemini להפוך אתכם לבמאים. כדי ליצור ביצועים קוליים מעולים, כדאי לזכור את הטיפים הבאים:

- חשוב לזכור שההנחיה כולה צריכה להיות עקבית – התסריט והבימוי משלימים זה את זה כדי ליצור ביצוע מוצלח.
- לא צריך לתאר כל דבר, לפעמים כדאי לתת למודל מקום למלא את הפערים כדי שהתוצאה תהיה טבעית. (Just like a talented actor)
- אם אתם מרגישים תקועים, אתם יכולים לבקש מ-Gemini עזרה בכתיבת התסריט או בביצוע.

## מגבלות

- מודלים של TTS יכולים לקבל רק קלט טקסט ולהפיק פלט אודיו.
- לסשן TTS יש מגבלת [חלון הקשר](https://ai.google.dev/gemini-api/docs/long-context?hl=he) של 32 אלף טוקנים.
- בקטע [שפות](https://ai.google.dev/gemini-api/docs/speech-generation?hl=he#languages) מפורטות השפות הנתמכות.
- ה-TTS לא תומך בסטרימינג.

ההגבלות הבאות חלות באופן ספציפי כשמשתמשים במודל Gemini 3.1 Flash
TTS Preview ליצירת דיבור:

- **חוסר עקביות בקול בהשוואה להוראות בהנחיה:** יכול להיות שהפלט של המודל לא תמיד יתאים בדיוק לרמקול שנבחר, ולכן האודיו יישמע שונה מהצפוי. כדי למנוע חוסר התאמה בטונים (למשל, קול גברי עוצמתי שמנסה לדבר כמו ילדה צעירה), חשוב לוודא שהטון וההקשר של ההנחיה תואמים באופן טבעי לפרופיל של הדובר שנבחר.
- **איכות של פלטים ארוכים יותר:** איכות הדיבור והעקביות עשויות להתחיל לדעוך בפלטים שנוצרו ואורכם יותר מכמה דקות. מומלץ לפצל את התמלילים לחלקים קטנים יותר.
- **המודל מחזיר מדי פעם טוקנים של טקסט:** המודל מחזיר מדי פעם טוקנים של טקסט במקום טוקנים של אודיו, ולכן השרת לא מצליח לבצע את הבקשה ומחזיר את השגיאה `500`. השגיאה הזו מתרחשת באופן אקראי באחוז קטן מאוד מהבקשות, ולכן כדאי להטמיע באפליקציה לוגיקה אוטומטית לניסיון חוזר כדי לטפל בה.
- **דחיות שגויות של מסווג ההנחיות:** יכול להיות שהנחיות לא ברורות לא יפעילו את מסווג סינתזת הדיבור, וכתוצאה מכך הבקשה תידחה (`PROHIBITED_CONTENT`) או שהמודל יקרא בקול רם את הוראות הסגנון ואת הערות הבמאי. כדי לוודא שההנחיות תקינות, מוסיפים פתיח ברור שמורה למודל לסנתז דיבור, ומציינים במפורש איפה מתחיל התמליל הממשי של הדיבור.

## המאמרים הבאים

- אפשר לנסות את [המדריך ליצירת אודיו](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb?hl=he).
- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=he) של Gemini מציע אפשרויות אינטראקטיביות ליצירת אודיו שאפשר לשלב עם מצבים אחרים.
- כדי לקבל מידע על עבודה עם *קלט* אודיו, אפשר לעיין במדריך [הבנת אודיו](https://ai.google.dev/gemini-api/docs/audio?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-04-29 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-04-29 (שעון UTC)."],[],[]]
