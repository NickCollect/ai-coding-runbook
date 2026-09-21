---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ar
fetched_at: 2026-09-21T05:53:02.467820+00:00
title: "\u0625\u0646\u0634\u0627\u0621 \u0627\u0644\u0645\u0648\u0633\u064a\u0642\u0649 \u0641\u064a \u0627\u0644\u0648\u0642\u062a \u0627\u0644\u0641\u0639\u0644\u064a \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Lyria RealTime \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إنشاء الموسيقى في الوقت الفعلي باستخدام Lyria RealTime

تتيح Gemini API، باستخدام
[Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=ar)،
الوصول إلى نموذج متطوّر لإنشاء الموسيقى
بتقنية البث المباشر وفي الوقت الفعلي. تتيح هذه الواجهة للمطوّرين إنشاء تطبيقات يمكن للمستخدمين من خلالها إنشاء موسيقى آلية بشكل تفاعلي وتوجيهها باستمرار وتشغيلها.

تستخدم ميزة "إنشاء الموسيقى في الوقت الفعلي" من Lyria اتصالاً دائمًا وثنائي الاتجاه للبث مع تأخير منخفض باستخدام [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API).

لتجربة إمكانات Lyria RealTime، يمكنك استخدامها في AI Studio من خلال تطبيقَي [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=ar) أو [MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=ar).

## إنشاء الموسيقى والتحكّم فيها

تعمل Lyria RealTime بشكل مشابه [لواجهة برمجة التطبيقات Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ar)،
إذ تستخدم Websockets للحفاظ على التواصل في الوقت الفعلي مع النموذج.

يوضّح الرمز التالي كيفية إنشاء موسيقى:

### Python

يهدف هذا المثال إلى تهيئة جلسة Lyria RealTime باستخدام `client.aio.live.music.connect()`، ثم إرسال طلب أولي باستخدام `session.set_weighted_prompts()` مع عملية إعداد أولية باستخدام `session.set_music_generation_config`، وبدء إنشاء الموسيقى باستخدام `session.play()`، وإعداد `receive_audio()` لمعالجة أجزاء الصوت التي يتلقّاها.

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

يهدف هذا المثال إلى تهيئة جلسة Lyria RealTime باستخدام `client.live.music.connect()`، ثم إرسال طلب أولي باستخدام `session.setWeightedPrompts()` مع إعدادات أولية باستخدام `session.setMusicGenerationConfig`، وبدء إنشاء الموسيقى باستخدام `session.play()`، وإعداد معاودة الاتصال `onMessage` لمعالجة أجزاء الصوت التي يتم تلقّيها.

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

يمكنك بعد ذلك استخدام `session.play()` أو `session.pause()` أو `session.stop()` أو `session.reset_context()` لبدء الجلسة أو إيقافها مؤقتًا أو إيقافها أو إعادة ضبطها.

## توجيه الموسيقى في الوقت الفعلي

يمكنك توجيه عملية إنشاء الموسيقى في الوقت الفعلي من خلال إرسال الطلبات وتعديل معلمات الإنشاء في الوقت الفعلي.

### ‫Prompt Lyria RealTime

أثناء البث المباشر، يمكنك إرسال رسائل `WeightedPrompt` جديدة في أي وقت لتغيير الموسيقى التي تم إنشاؤها. سينتقل النموذج بسلاسة استنادًا إلى الإدخال الجديد.

يجب أن تتّبع الطلبات التنسيق الصحيح مع `text` (الطلب الفعلي) و`weight`. يمكن أن تأخذ `weight` أي قيمة باستثناء `0`. `1.0`
هي عادةً نقطة بداية جيدة.

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
  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: 'Harmonica', weight: 0.3 },
      { text: 'Afrobeat', weight: 0.7 }
    ],
  });
```

يُرجى العِلم أنّ عمليات الانتقال بين النماذج يمكن أن تكون مفاجئة بعض الشيء عند تغيير الطلبات بشكل كبير، لذا يُنصح بتنفيذ نوع من التلاشي التدريجي من خلال إرسال قيم أوزان وسيطة إلى النموذج.

### تعديل الإعداد

يمكنك توجيه عملية إنشاء الموسيقى من خلال تعديل مَعلمات إنشاء الموسيقى في الوقت الفعلي. لا يمكنك تعديل مَعلمة واحدة فقط، بل عليك ضبط الإعدادات بأكملها، وإلا ستتم إعادة ضبط الحقول الأخرى على قيمها التلقائية.

بما أنّ تعديل عدد النبضات في الدقيقة أو المقياس الموسيقي هو تغيير جذري للنموذج، عليك أيضًا إخباره بإعادة ضبط السياق باستخدام `reset_context()` ليأخذ الإعداد الجديد في الاعتبار. لن يؤدي ذلك إلى إيقاف البث، ولكن سيكون الانتقال صعبًا. ليس عليك إجراء ذلك للمعلمات الأخرى.

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

## إدخال طلبات إلى Lyria RealTime

تستخدم Lyria RealTime طلبات مرجّحة لدمج الأنواع الموسيقية والآلات الموسيقية والحالات المزاجية بشكل ديناميكي. للاطّلاع على استراتيجيات توجيه الطلبات ومفردات علامات الكلمات الرئيسية وأمثلة كاملة على الطلبات، يُرجى الرجوع إلى [دليل كتابة طلبات Lyria](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=ar#realtime-prompting).

## أفضل الممارسات

- يجب أن تنفّذ تطبيقات العميل عملية تخزين مؤقت قوية للصوت لضمان تشغيل سلس. يساعد ذلك في احتساب تفاوتات الشبكة والاختلافات الطفيفة في وقت استجابة الإنشاء.
- كتابة طلبات فعّالة:
  - استخدم عبارات وصفية. استخدِم صفات تصف الحالة المزاجية والنوع والآلات الموسيقية.
  - كرِّر العملية ووجِّهها تدريجيًا. بدلاً من تغيير الطلب بالكامل، جرِّب إضافة عناصر أو تعديلها لتغيير الموسيقى بسلاسة أكبر.
  - جرِّب استخدام ميزة "الوزن" في `WeightedPrompt` للتأثير في مدى تأثير طلب جديد في عملية الإنشاء الجارية.

## التفاصيل الفنية

يوضّح هذا القسم تفاصيل كيفية استخدام ميزة إنشاء الموسيقى في الوقت الفعلي من Lyria.

### المواصفات

- تنسيق الإخراج: ملف صوتي PCM خام 16 بت
- معدّل البيانات في الملف الصوتي: 48 كيلوهرتز
- القنوات: 2 (استيريو)

### عناصر التحكّم

يمكن التأثير في إنشاء الموسيقى في الوقت الفعلي من خلال إرسال رسائل تحتوي على:

- `WeightedPrompt`: سلسلة نصية تصف فكرة موسيقية أو نوعًا موسيقيًا أو آلة موسيقية أو حالة مزاجية أو سمة. يمكن تقديم طلبات متعدّدة لدمج التأثيرات. راجِع [ما ورد أعلاه](#steer-music) لمزيد من التفاصيل حول أفضل طريقة لتقديم الطلبات إلى Lyria RealTime.
- `MusicGenerationConfig`: إعدادات عملية إنشاء الموسيقى،
  ما يؤثر في خصائص الصوت الناتج. تشمل المَعلمات ما يلي:
  - ‫`guidance`: (عدد عشري) النطاق: `[0.0, 6.0]` القيمة التلقائية: `4.0`
    يتحكّم هذا الإعداد في مدى التزام النموذج بالطلبات. تؤدي الإرشادات الأعلى إلى تحسين الالتزام بالطلب، ولكنها تجعل الانتقالات أكثر حدة.
  - ‫`bpm`: (عدد صحيح) النطاق: `[60, 200]`
    تضبط هذه السمة عدد النبضات في الدقيقة الذي تريده للموسيقى التي يتم إنشاؤها. يجب إيقاف/تشغيل أو إعادة ضبط السياق للنموذج الذي يأخذ في الاعتبار عدد النبضات الجديد في الدقيقة.
  - ‫`density`: (عدد عشري) النطاق: `[0.0, 1.0]`
    تتحكّم هذه السمة في كثافة النوتات الموسيقية أو الأصوات. تؤدي القيم المنخفضة إلى إنتاج موسيقى أقل كثافة، بينما تؤدي القيم المرتفعة إلى إنتاج موسيقى "أكثر كثافة".
  - ‫`brightness`: (عدد عشري) النطاق: `[0.0, 1.0]`
    يضبط جودة النغمات. تنتج القيم الأعلى صوتًا "أكثر سطوعًا"، مع التركيز بشكل عام على الترددات الأعلى.
  - ‫`scale`: (تعداد)
    يضبط المقياس الموسيقي (المفتاح والوضع) للإنشاء. استخدِم
    [قيم التعداد `Scale`](#scale-enum) التي توفّرها حزمة SDK. عليك إيقاف/تشغيل أو إعادة ضبط السياق الخاص بالنموذج ليأخذ في الاعتبار المقياس الجديد.
  - ‫`mute_bass`: (bool) القيمة التلقائية: `False`
    تتحكّم هذه السمة في ما إذا كان النموذج يقلّل من مستوى صوت الجهير في النواتج.
  - ‫`mute_drums`: (bool) القيمة التلقائية: `False`
    تتحكّم هذه السمة في ما إذا كان النموذج سيقلّل من إيقاع الطبول في النتائج.
  - ‫`only_bass_and_drums`: (bool) القيمة التلقائية: `False`
    توجيه النموذج لمحاولة إخراج صوت الباس والطبول فقط
  - ‫`music_generation_mode`: (تعداد)
    تُعلم هذه السمة النموذج ما إذا كان يجب التركيز على `QUALITY` (القيمة التلقائية) أو `DIVERSITY` من المحتوى الموسيقي. يمكن أيضًا ضبطها على `VOCALIZATION` للسماح للنموذج بإنشاء أصوات كآلة موسيقية أخرى (إضافتها كطلبات جديدة).
- ‫`PlaybackControl`: أوامر للتحكّم في جوانب التشغيل، مثل التشغيل أو الإيقاف المؤقت أو الإيقاف أو إعادة ضبط السياق

بالنسبة إلى `bpm` و`density` و`brightness` و`scale`، إذا لم يتم تقديم أي قيمة، سيقرّر النموذج الخيار الأفضل وفقًا لطلباتك الأولية.

يمكن أيضًا تخصيص المزيد من المَعلمات الكلاسيكية، مثل `temperature` (من 0.0 إلى 3.0، القيمة التلقائية 1.1) و`top_k` (من 1 إلى 1000، القيمة التلقائية 40) و`seed` (من 0 إلى 2,147,483,647، يتم اختيارها عشوائيًا بشكل تلقائي) في `MusicGenerationConfig`.

#### قيم التعداد في المقياس

في ما يلي جميع قيم المقياس التي يمكن أن يقبلها النموذج:

| قيمة التعداد | المقياس / المفتاح |
| --- | --- |
| `C_MAJOR_A_MINOR` | دو الكبير / لا الصغير |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | D♭ major / B♭ minor |
| `D_MAJOR_B_MINOR` | D major / B minor |
| `E_FLAT_MAJOR_C_MINOR` | E♭ major / C minor |
| `E_MAJOR_D_FLAT_MINOR` | مفتاح E الرئيسي / C♯/D♭ ثانوي |
| `F_MAJOR_D_MINOR` | فا الكبير / ري الصغير |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | G♭ major / E♭ minor |
| `G_MAJOR_E_MINOR` | صول كبير / مي صغير |
| `A_FLAT_MAJOR_F_MINOR` | A♭ كبير / F صغير |
| `A_MAJOR_G_FLAT_MINOR` | لا كبير / فا♯/صول♭ صغير |
| `B_FLAT_MAJOR_G_MINOR` | B♭ major / G minor |
| `B_MAJOR_A_FLAT_MINOR` | B major / G♯/A♭ minor |
| `SCALE_UNSPECIFIED` | الخيار التلقائي / يقرّر النموذج |

يمكن للنموذج توجيه النغمات التي يتم تشغيلها، ولكنّه لا يميّز بين المفاتيح النسبية. وبالتالي، يتوافق كل نوع تعداد مع الإصدار الرئيسي والإصدار الثانوي النسبيين. على سبيل المثال، يشير `C_MAJOR_A_MINOR` إلى جميع المفاتيح البيضاء في البيانو، بينما يشير `F_MAJOR_D_MINOR` إلى جميع المفاتيح البيضاء باستثناء المفتاح B flat.

### القيود

- موسيقى فقط: ينشئ النموذج موسيقى فقط.
- الأمان: يتم فحص الطلبات باستخدام فلاتر الأمان. سيتم تجاهل الطلبات التي تؤدي إلى تفعيل الفلاتر، وفي هذه الحالة، سيتم كتابة توضيح في الحقل `filtered_prompt` في الناتج.
- وضع العلامات المائية: يتم دائمًا وضع علامات مائية على المقاطع الصوتية الناتجة لتحديدها وفقًا لمبادئ [الذكاء الاصطناعي المسؤول](https://ai.google/responsibility/principles/?hl=ar).

## الخطوات التالية

- إنشاء أغاني كاملة ومقاطع صوتية باستخدام [Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=ar)
- بدلاً من الموسيقى، تعرَّف على كيفية إنشاء محادثة بين عدة متحدثين باستخدام [نماذج تحويل النص إلى كلام](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar).
- تعرَّف على كيفية إنشاء [صور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar) أو [فيديوهات](https://ai.google.dev/gemini-api/docs/video?hl=ar).
- بدلاً من إنشاء موسيقى أو محتوى صوتي، تعرَّف على كيفية
  [فهم Gemini للملفات الصوتية](https://ai.google.dev/gemini-api/docs/audio?hl=ar).
- إجراء محادثة في الوقت الفعلي مع Gemini باستخدام
  [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ar)

يمكنك استكشاف [كتاب الطبخ](https://github.com/google-gemini/cookbook) للحصول على المزيد من الأمثلة والبرامج التعليمية حول الرموز البرمجية.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-18 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-18 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
