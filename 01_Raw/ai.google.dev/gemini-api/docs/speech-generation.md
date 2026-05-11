---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar
fetched_at: 2026-05-11T04:59:56.155194+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إنشاء محتوى باستخدام تكنولوجيا تحويل النص إلى كلام (TTS)

يمكن لواجهة Gemini API تحويل النص إلى صوت أحادي أو متعدّد المتحدثين باستخدام إمكانات إنشاء تحويل النص إلى كلام (TTS) في Gemini.
إنّ عملية إنشاء الصوت باستخدام ميزة "تحويل النص إلى كلام" *[قابلة للتحكّم](#controllable)*،
ما يعني أنّه يمكنك استخدام اللغة الطبيعية لتنظيم التفاعلات وتحديد *الأسلوب* و*اللهجة* و*السرعة* و*النبرة* الخاصة بالصوت.

[تجربة الميزة في Google AI Studio](https://aistudio.google.com/apps/bundled/voice-library?showPreview=truew&hl=ar)

تختلف إمكانية تحويل النص إلى كلام عن إمكانية إنشاء الكلام المقدَّمة من خلال
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar)، وهي مصمَّمة لتوفير تجربة تفاعلية
للمحتوى الصوتي غير المنظَّم، وللمدخلات والمخرجات المتعددة الوسائط. في حين تتفوّق Live API في سياقات المحادثات الديناميكية، تم تصميم ميزة تحويل النص إلى كلام من خلال Gemini API لتناسب السيناريوهات التي تتطلّب تلاوة نصية دقيقة مع إمكانية التحكّم بدقة في الأسلوب والصوت، مثل إنشاء البودكاست أو الكتب المسموعة.

يوضّح لك هذا الدليل كيفية إنشاء محتوى صوتي يتضمّن متحدثًا واحدًا أو عدة متحدثين من نص.

## قبل البدء

تأكَّد من استخدام أحد أنواع نماذج Gemini التي تتضمّن ميزة تحويل النص إلى كلام (TTS) من Gemini، كما هو موضّح في قسم [النماذج المتوافقة](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar#supported-models). للحصول على أفضل النتائج، عليك تحديد النموذج الأنسب لحالة الاستخدام المحدّدة.

ننصحك [بتجربة نماذج تحويل النص إلى كلام من Gemini في AI Studio](https://aistudio.google.com/generate-speech?hl=ar) قبل البدء في إنشاء التطبيق.

## تحويل النص إلى كلام بصوت شخص واحد

لتحويل النص إلى صوت أحادي المتحدث، اضبط وضع الاستجابة على "صوت"،
وأرسِل عنصر `SpeechConfig` مع ضبط `VoiceConfig`.
عليك اختيار اسم صوت من [الأصوات الجاهزة](#voices).

يحفظ هذا المثال الصوت الناتج من النموذج في ملف موجي:

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

## تحويل النص إلى كلام لعدة متحدثين

بالنسبة إلى الصوت المتعدّد المصادر، ستحتاج إلى كائن `MultiSpeakerVoiceConfig` يتضمّن كل مكبّر صوت (بحد أقصى 2) تم ضبطه على أنّه `SpeakerVoiceConfig`.
عليك تحديد كل `speaker` باستخدام الأسماء نفسها المستخدَمة في
[الطلب](#controllable):

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

## التحكّم في أسلوب الكلام باستخدام الطلبات

يمكنك التحكّم في الأسلوب والنبرة واللهجة والسرعة باستخدام طلبات مكتوبة بلغة طبيعية
أو [علامات صوتية](#transcript-tags) لكل من ميزة تحويل النص إلى كلام (TTS) بصوت متحدث واحد أو عدة متحدثين.
على سبيل المثال، في طلب يتضمّن متحدثًا واحدًا، يمكنك قول:

```
Say in an spooky voice:
"By the pricking of my thumbs... [short pause]
[whisper] Something wicked this way comes"
```

في طلب يتضمّن عدة متحدثين، قدِّم إلى النموذج اسم كل متحدث والنص المقابل. يمكنك أيضًا تقديم إرشادات لكل متحدث على حدة:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... [yawn] what's on the agenda today?
Speaker2: You're never going to guess!
```

جرِّب استخدام [خيار صوتي](#voices) يتوافق مع الأسلوب أو المشاعر التي تريد التعبير عنها، وذلك للتأكيد عليها بشكل أكبر. في الطلب السابق، على سبيل المثال، قد يؤكّد صوت *إنسيلادوس* المتهدّج على حالتَي "التعب" و"الملل"، بينما قد تتناسب نبرة *بوك* المبهجة مع حالتَي "الحماس" و"السعادة".

## جارٍ إنشاء طلب لتحويل النص إلى صوت

تنتج نماذج تحويل النص إلى كلام محتوًى صوتيًا فقط، ولكن يمكنك استخدام [نماذج أخرى](https://ai.google.dev/gemini-api/docs/models?hl=ar) لإنشاء نص أولاً، ثم تمرير هذا النص إلى نموذج تحويل النص إلى كلام لقراءته بصوت مرتفع.

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

## خيارات الصوت

تتيح نماذج "تحويل النص إلى كلام" 30 خيارًا صوتيًا في الحقل `voice_name`:

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *ساطع* | **Puck** -- *مفعم بالحيوية* | **Charon** -- *مفيدة* |
| **كوريا** -- *شركة* | **Fenrir** -- *متحمّس* | **Leda** -- *Youthful* |
| **Orus** -- *شركة* | **Aoede** -- *Breezy* | **Callirrhoe** -- *مريح* |
| **Autonoe** -- *Bright* | ‫**Enceladus** -- *Breathy* | **Iapetus** -- *Clear* |
| **Umbriel**: *شخصية سهلة* | **الجبهة** -- *ناعم* | **Despina** -- *Smooth* |
| **Erinome** -- *محو* | **Algenib** -- *Gravelly* | **Rasalgethi** -- *مفيدة* |
| ‫**Laomedeia** -- *مرح* | **Achernar** -- *Soft* | **Alnilam** -- *الشركة* |
| **Schedar** -- *Even* | **Gacrux** -- *محتوى للبالغين* | **Pulcherrima** -- *واثق* |
| **Achird** -- *ودود* | **Zubenelgenubi** -- *غير رسمي* | **Vindemiatrix** -- *لطيف* |
| **Sadachbia** -- *مفعم بالحيوية* | **Sadaltager** -- *مُلمّ* | **سولفات** -- *دافئ* |

يمكنك الاستماع إلى جميع خيارات الأصوات في [AI Studio](https://aistudio.google.com/generate-speech?hl=ar).

## اللغات المتاحة

ترصد نماذج تحويل النص إلى كلام لغة الإدخال تلقائيًا. تتوفّر اللغات التالية:

| اللغة | رمز BCP-47 | اللغة | رمز BCP-47 |
| --- | --- | --- | --- |
| العربية | ar | الفلبينية | fil |
| البنغالية | bn | الفنلندية | fi |
| الهولندية | nl | الغليشيانية | gl |
| الإنجليزية | en | الجورجية | ka |
| الفرنسية | fr | اليونانية | el |
| الألمانية | de | الغوجاراتية | gu |
| الهندية | hi | الكريولية الهايتية | ht |
| الإندونيسية | id | العبرية | هو |
| الإيطالية | it | الهنغارية | hu |
| اليابانية | ja | الأيسلندية | هو |
| الكورية | ko | الجافانية | jv |
| المراثية | mr | الكانادا | kn |
| البولندية | pl | الكونكانية | kok |
| البرتغالية | pt | لاو | lo |
| الرومانية | ro | اللاتينية | la |
| الروسية | ru | اللاتفية | lv |
| الإسبانية | es | الليتوانية | lt |
| التاميلية | ta | اللوكسمبورغية | لبنان |
| التيلوغوية | te | المقدونية | mk |
| التايلاندية | th | المايثيلي | mai |
| التركية | tr | الملغاشية | مليغرام |
| الأوكرانية | uk | الماليزية | مللي ثانية |
| الفيتنامية | vi | المالايالامية | ml |
| الأفريقانية | af | المنغولية | mn |
| الألبانية | sq | النيبالية | ne |
| الأمهرية | am | النرويجية، بوكمال | nb |
| الأرمينية | hy | النرويجية، نينورسك | nn |
| الأذربيجانية | az | الأورية | أو |
| الباسك | eu | البشتو | ps |
| البيلاروسية | be | الفارسية | fa |
| البلغارية | bg | البنجابية | pa |
| البورمية | my | الصربية | sr |
| الكتالانية | ca | السندية | دقة عادية |
| السيبيوانية | ceb | السنهالية | si |
| الصينية، المندرينية | cmn | السلوفاكية | sk |
| الكرواتية | ساعة | السلوفينية | sl |
| التشيكية | cs | السواحيلية | sw |
| الدانمركية | da | السويدية | sv |
| الإستونية | et | الأوردية | ur |

## النماذج المتوافقة

| الطراز | متحدّث واحد | ميزة "المتحدثون المتعدّدون" |
| --- | --- | --- |
| [معاينة ميزة تحويل النص إلى كلام في Gemini 3.1 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=ar) | ✔️ | ✔️ |
| [Gemini 2.5 Flash Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=ar) | ✔️ | ✔️ |
| [إصدار تجريبي من ميزة "تحويل النص إلى كلام" في Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=ar) | ✔️ | ✔️ |

## دليل كتابة الطلبات

يختلف نموذج **الإنشاء الصوتي المدمج لتحويل النص إلى كلام (TTS) من Gemini** عن نماذج تحويل النص إلى كلام التقليدية من خلال استخدام نموذج لغوي كبير يعرف ***ليس فقط ما يجب قوله، بل أيضًا كيفية قوله***.

سيفسّر النموذج تلقائيًا نصًا مكتوبًا ويحدّد الطريقة التي يجب أن يتم بها عرض كلماتك. تكون النصوص البسيطة بدون أي طلبات إضافية طبيعية. لكنّ ميزة &quot;تحويل النص إلى كلام&quot; في Gemini تتضمّن أيضًا أدوات يمكنك استخدامها للتحكّم بها.

يهدف هذا الدليل إلى تقديم توجيهات أساسية وإثارة أفكار عند تطوير تجارب صوتية. سنبدأ باستخدام **العلامات** للتحكّم السريع المضمّن، ثم نستكشف **بُنى الطلبات** المتقدّمة لتوجيه الأداء بشكل كامل.

### علامات صوتية

العلامات هي معدِّلات مضمّنة، مثل `[whispers]` أو `[laughs]`، تمنحك تحكّمًا دقيقًا في العرض. يمكنك استخدامها لتغيير نبرة الصوت وسرعته
والإحساس العاطفي في سطر أو قسم من النص. يمكنك أيضًا استخدامها
لإضافة عبارات اعتراضية وبعض الأصوات غير اللفظية الأخرى إلى الأداء، مثل
`[cough]` أو `[sighs]` أو `[gasp]`.

لا تتوفّر قائمة شاملة بالعلامات التي تعمل وتلك التي لا تعمل، وننصحك بتجربة مشاعر وتعبيرات مختلفة لمعرفة كيف يتغيّر الناتج.

إذا لم تكن النسخة مكتوبة باللغة الإنجليزية، ننصحك باستخدام علامات صوتية باللغة الإنجليزية للحصول على أفضل النتائج.

**استخدام علامات صوتية مبتكرة**

لعرض نوع التغيّر الذي يمكن الحصول عليه باستخدام علامات الصوت، إليك مجموعة من الأمثلة التي تعبّر عن المعنى نفسه، ولكن يختلف العرض استنادًا إلى العلامات المستخدَمة.

يمكنك تغيير طريقة إلقاء الكلام من خلال إضافة علامات في بداية السطر لجعل المتحدث يبدو متحمسًا أو متضايقًا أو مترددًا:

- `[excitedly]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام، ويمكنني التحدّث بطرق مختلفة. كيف يمكنني مساعدتك اليوم؟
- `[bored]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام…
- `[reluctantly]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام…

يمكن أيضًا استخدام العلامات لتغيير سرعة التسليم أو لدمج السرعة مع التأكيد:

- `[very fast]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام…
- `[very slow]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام…
- `[sarcastically, one painfully slow word at a time]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام…

يمكنك أيضًا التحكّم بدقة في مقاطع معيّنة، ما يعني أنّه يمكنك تسجيل جزء من الفيديو بصوت منخفض وتسجيل جزء آخر بصوت مرتفع.

- `[whispers]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام، `[shouting]` ويمكنني التحدّث بطرق مختلفة. `[whispers]` كيف يمكنني مساعدتك اليوم؟

يمكنك أيضًا تجربة أي فكرة إبداعية تريدها:

- `[like a cartoon dog]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام…
- `[like dracula]` مرحبًا، أنا نموذج جديد لتحويل النص إلى كلام…

تشمل العلامات الشائعة الاستخدام ما يلي:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

تتيح لك العلامات التحكّم بسرعة وسهولة في عملية تسليم نص الفيديو. ولمزيد من التحكّم، يمكنك دمجها مع طلب سياق لتحديد النبرة العامة
والأجواء التي ستسود الأغنية.

### الطلبات المتقدّمة

يمكنك اعتبار الطلب المتقدّم بمثابة تعليمات نظامية يقدّمها المستخدم للنموذج لكي يتّبعها. وهي طريقة لتزويد النموذج بمزيد من السياق والتحكّم في الأداء.

يتضمّن نص الطلب الفعّال بشكل مثالي العناصر التالية التي تتكامل معًا
لتحقيق أداء رائع:

- **الملف الصوتي**: يحدّد شخصية الصوت، ويحدد هوية الشخصية ونمطها وأي خصائص أخرى، مثل العمر والخلفية وما إلى ذلك.
- **المشهد**: يضبط المشهد. يصف هذا الحقل البيئة المادية والأجواء.
- **ملاحظات المخرج**: إرشادات الأداء التي يمكنك من خلالها تحديد التعليمات المهمة التي يجب أن يضعها الممثل الافتراضي في اعتباره. وتشمل الأمثلة
  الأسلوب والتنفس والسرعة والتعبير واللهجة.
- **مثال على السياق**: يمنح النموذج نقطة بداية سياقية، ما يتيح للممثل الافتراضي الدخول إلى المشهد الذي أعددته بشكل طبيعي.
- **نص**: النص الذي سينطقه النموذج. للحصول على أفضل أداء، تذكَّر أنّ موضوع النص وأسلوب الكتابة يجب أن يكونا مرتبطَين بالتعليمات التي تقدّمها.
- **علامات الصوت**: هي معدِّلات يمكنك إضافتها إلى نص لتغيير طريقة عرض جزء من النص، مثل `[whispers]` أو `[shouting]`.

مثال على الطلب الكامل:

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

### استراتيجيات مفصّلة لتقديم الطلبات

دعونا نحلّل كل عنصر من عناصر الطلب.

#### ملف تعريف الصوت

صف بإيجاز سمات الشخصية.

- **الاسم:** يساعد إعطاء اسم للشخصية في ترسيخ النموذج وتقديم أداء متماسك. لذا، يُرجى الإشارة إلى الشخصية بالاسم عند تحديد المشهد والسياق.
- **الدور:** تمثّل هذه السمة الهوية الأساسية والنموذج الأصلي للشخصية التي تظهر في المشهد، مثل منسّق موسيقى في الراديو أو مقدّم بودكاست أو مراسل إخباري وما إلى ذلك.

أمثلة:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### منظر

حدِّد سياق المشهد، بما في ذلك الموقع الجغرافي والمزاج والتفاصيل البيئية التي تحدّد النبرة والأجواء. صِف ما يحدث حول الشخصية وتأثيره عليها. يوفّر المشهد السياق البيئي للتفاعل بأكمله، ويوجه الأداء التمثيلي بطريقة طبيعية دقيقة.

أمثلة:

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

#### ملاحظات المخرجين

يتضمّن هذا القسم المهم إرشادات محدّدة بشأن الأداء. يمكنك تخطّي جميع العناصر الأخرى، ولكن ننصحك بتضمين هذا العنصر.

حدِّد فقط ما هو مهم للأداء، مع الحرص على عدم المبالغة في التحديد. سيؤدي وضع عدد كبير جدًا من القواعد الصارمة إلى الحدّ من إبداع النماذج وقد يؤدي إلى تراجع الأداء. وازِن بين وصف الدور والمشهد وقواعد الأداء المحدّدة.

إنّ التوجيهات الأكثر شيوعًا هي **الأسلوب والوتيرة واللهجة**، ولكن النموذج لا يقتصر على هذه التوجيهات ولا يتطلّبها. يمكنك تضمين تعليمات مخصّصة لتغطية أي تفاصيل إضافية مهمة لأدائك، ويمكنك تقديم التفاصيل بقدر ما يلزم.

على سبيل المثال:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**النمط:**

يضبط هذا الحقل نبرة الكلام الذي يتم إنشاؤه وأسلوبه. يمكنك تضمين كلمات مثل "مبهج" أو "نشيط" أو "مسترخٍ" أو "ملل" وما إلى ذلك لتوجيه الأداء. يجب أن تكون الأوصاف وافية
وتتضمّن أكبر قدر ممكن من التفاصيل الضرورية: *"حماس معدٍ. إنّ عبارة "يجب أن يشعر المستمع بأنّه يشارك في فعالية ضخمة ومثيرة"* أفضل من مجرد القول *"نشيط وحماسي".*

يمكنك حتى تجربة عبارات شائعة في مجال التعليق الصوتي، مثل "ابتسامة صوتية". يمكنك إضافة أي عدد تريده من خصائص الأنماط.

أمثلة:

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

مزيد من العمق

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

متقدّم

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**اللهجة:**

قدِّم وصفًا للّكنة المطلوبة. كلّما كانت التفاصيل أكثر، كانت النتائج أفضل. على سبيل المثال، استخدِم "*لهجة إنجليزية بريطانية كما تُسمع في كرويدون، إنجلترا*" بدلاً من "*لهجة بريطانية*".

أمثلة:

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

**معدّل تسجيل مرات الظهور:**

الوتيرة الإجمالية وتفاوت الوتيرة في جميع أنحاء المقطوعة

أمثلة:

بسيط

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

مزيد من التفاصيل

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

متقدّم

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

#### النص والعلامات الصوتية

النص هو الكلمات المحدّدة التي سينطق بها النموذج. علامة الصوت هي كلمة
بين قوسين مربّعين تشير إلى طريقة لفظ كلمة أو عبارة، أو إلى تغيير
في النبرة، أو إلى عبارة اعتراضية.

```
### TRANSCRIPT

I know right, [sarcastically] I couldn't believe it. [whispers] She should have totally left
at that point.

[cough] Well, [sighs] I guess it doesn't matter now.
```

**تجربة الميزة**

يمكنك تجربة بعض هذه الأمثلة بنفسك على
[AI Studio](https://aistudio.google.com/generate-speech?hl=ar)، واستخدام
[تطبيق تحويل النص إلى كلام](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=ar)،
والاستفادة من
ميزات Gemini لتجربة الإخراج. إليك بعض النصائح التي يجب وضعها في الاعتبار لتقديم أداء صوتي رائع:

- تذكَّر أن تحافظ على تماسك الطلب بأكمله، فالنص والاتجاه يسيران جنبًا إلى جنب في تقديم أداء رائع.
- لا تشعر بأنّك مضطر إلى وصف كل شيء، ففي بعض الأحيان، يساعد منح النموذج مساحة لملء الفراغات في الحفاظ على طبيعية النص. (تمامًا مثل الممثل الموهوب)
- إذا واجهت صعوبة في كتابة نص أو أداء أغنية، يمكن أن يساعدك Gemini في ذلك.

## القيود

- يمكن لنماذج تحويل النص إلى كلام تلقّي إدخالات نصية فقط وإنشاء مخرجات صوتية.
- تبلغ قدرة [الاستيعاب](https://ai.google.dev/gemini-api/docs/long-context?hl=ar) لجلسة تحويل النص إلى كلام 32 ألف رمز مميّز.
- راجِع قسم [اللغات](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar#languages) لمعرفة اللغات المتاحة.
- لا تتيح ميزة "تحويل النص إلى كلام" البث.

تنطبق القيود التالية تحديدًا عند استخدام نموذج Gemini 3.1 Flash
TTS Preview لإنشاء الكلام:

- **عدم تطابق الصوت مع تعليمات الطلب:** قد لا يتطابق الناتج الذي تقدّمه النماذج دائمًا مع الصوت الذي تم اختياره، ما يؤدي إلى اختلاف الصوت عن المتوقع. لتجنُّب عدم تطابق النبرات (مثل صوت رجل عميق يحاول التحدّث مثل فتاة صغيرة)، تأكَّد من أنّ النبرة والسياق المكتوبَين في الطلب يتوافقان بشكل طبيعي مع الملف الشخصي للمتحدث المحدّد.
- **جودة النتائج الأطول:** قد تبدأ جودة الكلام واتساقه في التدهور مع النتائج التي تزيد مدتها عن بضع دقائق. ننصحك بتقسيم النصوص إلى أجزاء أصغر.
- **عرض رموز نصية بشكل متقطّع:** يعرض النموذج أحيانًا رموزًا نصية بدلاً من رموز صوتية، ما يؤدي إلى تعذُّر تنفيذ الطلب على الخادم وظهور الخطأ `500`. بما أنّ هذا يحدث بشكل عشوائي في نسبة صغيرة جدًا من الطلبات، عليك تنفيذ منطق إعادة المحاولة المبرمَج في تطبيقك للتعامل مع هذه الحالات.
- **الرفض الخاطئ لمصنّف الطلبات:** قد لا تؤدي الطلبات الغامضة إلى تشغيل مصنّف تركيب الكلام، ما يؤدي إلى رفض الطلب (`PROHIBITED_CONTENT`) أو جعل النموذج يقرأ تعليمات الأسلوب وملاحظات المخرج بصوت عالٍ. تحقّق من صحة الطلبات من خلال إضافة مقدمة واضحة
  تطلب من النموذج تركيب الكلام، مع تحديد موضع بدء
  النص المكتوب المنطوق بشكل صريح.

## الخطوات التالية

- جرِّب [كتاب وصفات إنشاء الصوت](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb?hl=ar).
- توفّر [واجهة برمجة التطبيقات Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar) من Gemini خيارات تفاعلية لإنشاء الصوت يمكنك دمجها مع وسائط أخرى.
- للتعرّف على كيفية التعامل مع *مدخلات* الصوت، يُرجى الانتقال إلى دليل [فهم الصوت](https://ai.google.dev/gemini-api/docs/audio?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-07 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-07 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
