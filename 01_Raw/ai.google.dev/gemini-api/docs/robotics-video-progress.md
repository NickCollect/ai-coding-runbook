---
source_url: https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ar
fetched_at: 2026-08-10T03:14:41.253757+00:00
title: "\u0641\u0647\u0645 \u0627\u0644\u0641\u064a\u062f\u064a\u0648 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# فهم الفيديو

يمكن لروبوت Gemini Robotics ER 2 تتبُّع تقدّم المهمة من خلال خلاصات الفيديو المستمرة باستخدام ميزتَين:

- العثور على اللحظات: يحدّد الطابع الزمني الدقيق الذي يقع فيه حدث رئيسي.
- تصنيف مستوى التقدّم: يتم تصنيف كل فيديو ضمن إحدى فئات مستوى الإكمال الخمس (من 0 إلى 20%، ومن 20 إلى 40%، ومن 40 إلى 60%، ومن 60 إلى 80%، ومن 80 إلى 100%).

## العثور على اللحظات المميزة

تحدّد ميزة "العثور على اللحظات" إطار الفيديو الدقيق الذي يقع فيه حدث مهم، مثل امتلاء كوب أو عقد ربطة. تستخدم الروبوتات هذه البيانات للتحقّق من نجاح العملية، وترتيب الخطوات، وتفعيل التصحيحات.

يطلب مثال الطلب التالي من النموذج تحديد لحظة إكمال مهمة معيّنة في فيديو:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

تعرض الصورة التالية لقطات نموذجية من فيديو يهدف إلى العثور على لحظة معيّنة، حيث يحدّد النموذج الطابع الزمني لإكمال المهمة:

![مثال على إطارات فيديو تعرض نتيجة العثور على اللحظة مع تراكب طابع زمني](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=ar)

## تصنيف مستوى التقدم

يصنّف الفيديو ضمن إحدى فئات الاكتمال الخمس التالية:
من 0 إلى %20 أو من %20 إلى %40 أو من %40 إلى %60 أو من %60 إلى %80 أو من %80 إلى %100. يمنح ذلك الروبوتات إدراكًا للوضع في الوقت الفعلي، ما يتيح لها تعديل الإجراءات أو إعادة محاولة الخطوات التي تعذّر تنفيذها بدون إعادة تشغيل سير العمل بأكمله.

يطلب الطلب النموذجي التالي من النموذج تصنيف مستوى التقدّم الحالي من فيديو:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

تعرض الصورة التالية أمثلة على لقطات من فيديو لتصنيف مستوى التقدّم، مع تحديد فئة مستوى التقدّم من خلال النموذج:

![أمثلة على لقطات فيديو تعرض ناتج تصنيف مستوى التقدّم مع تصنيف بين قوسين](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=ar)

## أمثلة

للاطّلاع على أمثلة كاملة قابلة للتنفيذ تتضمّن تتبُّع المهام المتعدّدة الخطوات، يُرجى الرجوع إلى [كتاب وصفات الروبوتات](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## الخطوات التالية

- [Live API للروبوتات](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ar): بث ثنائي الاتجاه في الوقت الفعلي
- [تنظيم المهام](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=ar): مهام طويلة الأمد تتضمّن التفكير المكاني
- [نظرة عامة على Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=ar): مقارنة النماذج والإمكانات

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
