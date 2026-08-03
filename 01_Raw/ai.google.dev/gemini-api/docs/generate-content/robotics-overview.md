---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-overview?hl=ar
fetched_at: 2026-08-03T04:30:19.754105+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# Gemini Robotics ER

نماذج Gemini Robotics ER (الاستدلال المجسّد) هي نماذج للرؤية واللغة (VLM) تتيح للروبوتات إدراك العالم المادي والتفاعل معه. وهي تفسّر البيانات المرئية، وتجري عمليات استدلال مكانية وزمانية، وتخطّط لمهام متعدّدة الخطوات، وتنسّق بين الروبوتات والأدوات.

## النماذج

‫Gemini Robotics ER 2 هو أحدث طراز في Gemini Robotics.
وهو نموذج محدّث للاستدلال يتيح للروبوتات فهم البيئات المحيطة بها بدقة. وهي متخصّصة في إمكانات الاستدلال المجسّد، مثل التنسيق بين برامج الروبوت (مثل استخدام المساعدين الافتراضيين المرئيين) وفهم فيديوهات الروبوت، بما في ذلك فهم التقدم المحرز ورصد النجاح وقراءة الأدوات والإشارة والاستدلال المكاني.

يقدّم نموذج Gemini Robotics ER 2 نقطتَي نهاية للنموذج:

- ‫**`gemini-robotics-er-2-preview`**: نموذج ER 2 العادي يستند إلى Gemini 3.5 Flash مع تحسينات على الاستدلال المكاني، والعثور على لحظات في الفيديو، وتصنيف تقدّم الفيديو، وتنسيق عمل الروبوتات المتعددة، واستخدام الأدوات المتعددة الخطوات.
- **`gemini-robotics-er-2-streaming-preview`**: تم تحسينها للبث المباشر في الوقت الفعلي من خلال [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ar). استخدِم هذا النموذج
  لبرامج الروبوت التي تتطلّب زمن استجابة منخفضًا وتعالج بيانات الصوت والفيديو
  المتواصلة.

إذا كنت تستخدم Gemini Robotics ER 1.6، يمكنك الترقية إلى Gemini Robotics ER 2 من خلال استبدال
`model="gemini-robotics-er-1.6-preview"` بـ
`model="gemini-robotics-er-2-preview"` أو
`model="gemini-robotics-er-2-streaming-preview"` في طلبات البيانات من واجهة برمجة التطبيقات. يُرجى العِلم أنّه سيتم إيقاف نموذج Gemini Robotics ER 1.6 في [نهاية أغسطس](https://ai.google.dev/gemini-api/docs/deprecations?hl=ar#robotics-models).

[تجربة الإصدار الثاني من Gemini Robotics في Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=ar)

## إمكانات الروبوتات

يتيح Gemini Robotics ER مجموعة من إمكانات الاستدلال المجسَّد.
اختَر إحدى الإمكانيات لمعرفة المزيد من المعلومات:

| إمكانية | الوصف | الدليل |
| --- | --- | --- |
| الاستدلال المكاني | توجيه الكاميرا إلى الأجسام وتتبُّعها في الفيديو ورصدها باستخدام مربّعات حدودية وتخطيط مساراتها | [الاستدلال المكاني](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=ar) |
| الرؤية المستنِدة إلى الذكاء الاصطناعي الوكيل | استخدِم ميزة "تنفيذ الرموز البرمجية" لتحسين الإمكانات الأخرى من خلال الاستفادة من أدوات معالجة الصور. | [الرؤية المستندة إلى الذكاء الاصطناعي الوكيل](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=ar) |
| تنظيم المهام | يمكنك الجمع بين الاستدلال المكاني وواجهات برمجة التطبيقات المخصّصة للروبوتات لإكمال مهام طويلة الأمد. | [تنظيم المهام](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=ar) |
| البث (نقطة نهاية البث في Gemini Robotics ER 2 فقط) | البث الثنائي الاتجاه لوكلاء الروبوت في الوقت الفعلي مع إمكانية استدعاء الدوال بوقت استجابة منخفض | [البث للروبوتات](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ar) |
| تقدّم الفيديو (في الإصدار الثاني من Gemini Robotics فقط) | العثور على اللحظات وتصنيف مستوى التقدّم من خلاصات الفيديو المتواصل. | [فهم الفيديوهات](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=ar) |

## الخطوات الأولى

يعثر المثال التالي على عناصر في صورة ويعرض إحداثياتها الثنائية الأبعاد العادية وتصنيفاتها. يمكنك تمرير هذا الناتج مباشرةً إلى واجهة برمجة تطبيقات خاصة بالروبوتات أو إلى نموذج VLA لإنشاء إجراءات الروبوت.

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_uri(
            file_uri=uploaded_file.uri,
            mime_type=uploaded_file.mime_type
        ),
        PROMPT
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    ),
)

print(response.text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-2-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "'"${IMAGE_BASE64}"'"
            }
          },
          {
            "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
          }
        ]
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "high"
      }
    }
  }'
```

سيكون الناتج مصفوفة JSON تحتوي على عناصر، كل منها يتضمّن `point`
(إحداثيات `[y, x]` عادية) و`label` يحدّد العنصر.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

في ما يلي مثال على كيفية عرض هذه النقاط:

![مثال يعرض نقاط العناصر في صورة](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=ar)

## آلية العمل

تتلقّى Gemini Robotics ER الصور أو الفيديوهات أو الملفات الصوتية من خلال طلبات مكتوبة باللغة الطبيعية. تحدّد هذه الخدمة العناصر، وتستنتج سياق المشهد والعلاقات المكانية، وتعرض نتائج منظَّمة، مثل الإحداثيات أو مربّعات الإحاطة.

تتّسم Gemini Robotics ER أيضًا بالقدرة على تنفيذ المهام بشكل مستقل، إذ تقسم المهام المعقّدة إلى مهام فرعية وتنفّذها من خلال استدعاء وظائف الروبوت أو تشغيل الرمز البرمجي الذي تم إنشاؤه. على سبيل المثال، تتحوّل الجملة "ضَع التفاحة في الوعاء" إلى سلسلة من الخطوات التي تتضمّن تحديد الموقع والإمساك والتوضيع.

يمكنك الاطّلاع على [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=ar#how-it-works) للحصول على تفاصيل حول طريقة تنفيذ Gemini لطلبات استخدام الأدوات.

## الأمان

على الرغم من أنّ Gemini Robotics ER مصمَّم مع مراعاة السلامة، تقع على عاتقك مسؤولية الحفاظ على بيئة آمنة حول الروبوت. قد ترتكب نماذج الذكاء الاصطناعي التوليدي أخطاءً، وقد تتسبّب الروبوتات المادية في إلحاق الضرر. لمزيد من المعلومات، يُرجى الانتقال إلى [صفحة أمان الروبوتات في Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=ar).

## أفضل الممارسات

1. استخدِم اللغة الطبيعية. قدِّم وصفًا للروبوت بشأن ما تريد منه تنفيذه، تمامًا كما تفعل مع شخص آخر. إذا لم تنجح عبارة بحث، جرِّب استخدام مرادف شائع.
2. تحسين الإدخال المرئي اقطع أو كبِّر العناصر الصغيرة أو غير الواضحة قبل إرسال الصورة. يمكن أن تؤثر الإضاءة والتباين المنخفض في الألوان في عملية الرصد.
3. قسِّم المهام المعقّدة إلى خطوات. أرسِل كل خطوة كطلب منفصل للحفاظ على تركيز النموذج وتحسين الدقة.
4. إرسال طلبات بحث متعددة والحصول على متوسط النتائج للمهام التي تتطلّب دقة عالية يقلّل نهج التوافق هذا التباين في النتائج المكانية.

## القيود

يجب مراعاة القيود التالية عند التطوير باستخدام Gemini Robotics ER:

- **القيود المفروضة على مفتاح واجهة برمجة التطبيقات:** لا تقبل Gemini API الطلبات الواردة من مفاتيح واجهة برمجة التطبيقات غير الخاضعة لقيود، وتعرض الخطأ `403 Forbidden`. يمكنك حماية مفتاح واجهة برمجة التطبيقات من خلال إضافة قيود في [AI Studio](https://aistudio.google.com/api-keys?hl=ar).
  لمزيد من التفاصيل، يمكنك الاطّلاع على [تأمين مفاتيح واجهة برمجة التطبيقات غير المحظورة](https://ai.google.dev/gemini-api/docs/api-key?hl=ar#secure-unrestricted-keys).
- **وقت الاستجابة مقابل الأداء:** يمكن أن تؤدي الطلبات المعقّدة أو المدخلات العالية الدقة أو مستويات التفكير العالية إلى زيادة أوقات المعالجة. بالنسبة إلى مستوى التفكير
  استخدِم "متوسط" لتحقيق توازن جيد بين وقت الاستجابة والأداء.
- **الهلوسات:** مثل جميع النماذج اللغوية الكبيرة، يمكن أن "تهلوس" نماذج Gemini Robotics ER في بعض الأحيان أو تقدّم معلومات غير صحيحة، خاصةً في ما يتعلّق بالطلبات الغامضة أو المدخلات غير المتوقّعة.
- **الاعتماد على جودة الطلب:** تعتمد جودة النتائج على وضوح الطلب الذي يتم إدخاله. استخدِم طلبات محدّدة ومنظَّمة بشكل جيد.
- **التكلفة الحسابية:** يؤدي تشغيل النموذج، خاصةً مع إدخال فيديوهات أو `thinking_budget` مرتفع، إلى استهلاك موارد حسابية وتكبّد تكاليف.
  يمكنك الاطّلاع على صفحة [التفكير](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ar) لمزيد من التفاصيل.
- **أنواع الإدخال:** اطّلِع على المواضيع التالية لمعرفة تفاصيل حول القيود المفروضة على كل وضع.
  - [مدخلات الصور](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=ar#technical-details-image)
  - [إدخالات الفيديو](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ar#supported-formats)
  - [إدخال الصوت](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=ar#supported-formats)

## إشعار الخصوصية

أنت تقرّ بأنّ النماذج المشار إليها في هذا المستند ("نماذج الروبوتات") تستخدم بيانات الفيديو والصوت لتشغيل الأجهزة وتحريكها وفقًا لتعليماتك. وبالتالي، يمكنك تشغيل &quot;نماذج الروبوتات&quot; بطريقة تؤدي إلى جمع بيانات من أشخاص يمكن التعرّف عليهم، مثل بيانات الصوت والصور والتشابه (&quot;البيانات الشخصية&quot;). إذا اخترت تشغيل "نماذج الروبوتات" بطريقة تجمع "البيانات الشخصية"، أنت توافق على عدم السماح لأي أشخاص يمكن التعرّف عليهم بالتفاعل مع "نماذج الروبوتات" أو التواجد في المنطقة المحيطة بها، إلا بعد إبلاغ هؤلاء الأشخاص بشكل كافٍ وموافقتهم على إمكانية تقديم بياناتهم الشخصية إلى Google واستخدامها من قِبلها على النحو الموضّح في "بنود الخدمة الإضافية لخدمة Gemini API" المتوفّرة على الرابط [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=ar) (المشار إليها باسم "البنود")، بما في ذلك وفقًا للقسم بعنوان "طريقة استخدام Google لبياناتك". ستضمن أنّ هذا الإشعار يسمح بجمع البيانات الشخصية واستخدامها على النحو الموضّح في &quot;البنود&quot;، وستبذل جهودًا معقولة تجاريًا للحدّ من جمع البيانات الشخصية وتوزيعها باستخدام تقنيات مثل تمويه الوجوه وتشغيل &quot;نماذج الروبوتات&quot; في مناطق لا تحتوي على أشخاص يمكن التعرّف عليهم إلى الحدّ الذي يمكن تنفيذه عمليًا.

## الأسعار

للحصول على معلومات تفصيلية حول الأسعار والمناطق المتاحة، يُرجى الرجوع إلى صفحة [الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).

## نقاط نهاية النماذج

### ‫Gemini Robotics ER 2 Preview

| الموقع | الوصف |
| --- | --- |
| رمز النموذج id\_card | `gemini-robotics-er-2-preview` |
| saveأنواع البيانات المتوافقة | **المدخلات**  النصوص والصور والفيديوهات والمحتوى الصوتي  **الناتج**  نص |
| token\_autoحدود الرموز المميزة[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ar) | **الحدّ الأقصى لعدد الرموز المميزة التي يمكن إدخالها**  131,072  **الحدّ الأقصى لعدد الرموز المميزة الناتجة**  65,536 |
| handymanالإمكانات | **[إنشاء الصوت](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar)**  غير متاح  **[التخزين المؤقت](https://ai.google.dev/gemini-api/docs/caching?hl=ar)**  متاح  **[تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar)**  متاح  **[استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar)**  متاح  **[البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar)**  متاح  **[استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)**  متاح  **[استخدام "خرائط Google" كمصدر](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar)**  متاح  **[إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar)**  غير متاح  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ar)**  غير متاح  **[تحديد المصادر في "بحث Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar)**  متاح  **[المُخرجات المنظَّمة](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar)**  متاح  **[التفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar)**  متاح  **[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar)**  متاح |
| speedخيارات الاستهلاك | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar)**  متاح  **[الاستدلال المرن](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ar)**  غير متاح  **[استنتاج الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar)**  غير متاح |
| 123الإصدارات | يمكنك الاطّلاع على [أنماط إصدارات النماذج](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#model-versions) لمزيد من التفاصيل.  - معاينة: `gemini-robotics-er-2-preview` |
| calendar\_monthآخر تعديل | يوليو 2026 |
| id\_cardبطاقة النموذج | [بطاقة النموذج](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=ar) |

### Gemini Robotics ER 2 Streaming Preview

| الموقع | الوصف |
| --- | --- |
| رمز النموذج id\_card | `gemini-robotics-er-2-streaming-preview` |
| saveأنواع البيانات المتوافقة | **المدخلات**  النصوص والصور والفيديوهات والمحتوى الصوتي  **الناتج**  نص |
| token\_autoحدود الرموز المميزة[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ar) | **الحدّ الأقصى لعدد الرموز المميزة التي يمكن إدخالها**  131,072  **الحدّ الأقصى لعدد الرموز المميزة الناتجة**  65,536 |
| handymanالإمكانات | **[إنشاء الصوت](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar)**  غير متاح  **[التخزين المؤقت](https://ai.google.dev/gemini-api/docs/caching?hl=ar)**  غير متاح  **[تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar)**  غير متاح  **[استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar)**  غير متاح  **[البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar)**  غير متاح  **[استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)**  متاح  **[استخدام "خرائط Google" كمصدر](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar)**  غير متاح  **[إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar)**  غير متاح  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ar)**  متاح  **[تحديد المصادر في "بحث Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar)**  متاح  **[المُخرجات المنظَّمة](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar)**  غير متاح  **[التفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar)**  متاح  **[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar)**  غير متاح |
| speedخيارات الاستهلاك | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar)**  غير متاح  **[الاستدلال المرن](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ar)**  غير متاح  **[استنتاج الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar)**  غير متاح |
| 123الإصدارات | يمكنك الاطّلاع على [أنماط إصدارات النماذج](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#model-versions) لمزيد من التفاصيل.  - معاينة: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthآخر تعديل | يوليو 2026 |
| id\_cardبطاقة النموذج | [بطاقة النموذج](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=ar) |

### معاينة Gemini Robotics ER 1.6

| الموقع | الوصف |
| --- | --- |
| رمز النموذج id\_card | `gemini-robotics-er-1.6-preview` |
| saveأنواع البيانات المتوافقة | **المدخلات**  النصوص والصور والفيديوهات والمحتوى الصوتي  **الناتج**  نص |
| token\_autoحدود الرموز المميزة[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ar) | **الحدّ الأقصى لعدد الرموز المميزة التي يمكن إدخالها**  131,072  **الحدّ الأقصى لعدد الرموز المميزة الناتجة**  65,536 |
| handymanالإمكانات | **[إنشاء الصوت](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar)**  غير متاح  **[التخزين المؤقت](https://ai.google.dev/gemini-api/docs/caching?hl=ar)**  متاح  **[تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar)**  متاح  **[استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar)**  متاح  **[البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar)**  متاح  **[استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)**  متاح  **[استخدام "خرائط Google" كمصدر](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar)**  متاح  **[إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar)**  غير متاح  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ar)**  غير متاح  **[تحديد المصادر في "بحث Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar)**  متاح  **[المُخرجات المنظَّمة](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar)**  متاح  **[التفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar)**  متاح  **[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar)**  متاح |
| speedخيارات الاستهلاك | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar)**  متاح  **[الاستدلال المرن](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ar)**  غير متاح  **[استنتاج الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar)**  غير متاح |
| 123الإصدارات | يمكنك الاطّلاع على [أنماط إصدارات النماذج](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar#model-versions) لمزيد من التفاصيل.  - معاينة: `gemini-robotics-er-1.6-preview` |
| calendar\_monthآخر تعديل | ديسمبر 2025 |
| cognition\_2تاريخ آخر تحديث للبيانات | يناير 2025 |

## الخطوات التالية

- [الاستدلال المكاني](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=ar): يشمل الإشارة والتتبُّع ومربّعات الإحاطة والمسارات.
- [إمكانات بالذكاء الاصطناعي الوكيل](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=ar): تطبيق الرموز البرمجية، وقياس حالة التطبيق، وإضافة تعليقات توضيحية على الصور.
- [تنظيم المهام](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=ar): مهام طويلة الأمد باستخدام واجهات برمجة تطبيقات مخصّصة للروبوتات
- [الروبوتات التي تتضمّن بثًا مباشرًا](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ar): بث مباشر ثنائي الاتجاه في الوقت الفعلي (Gemini Robotics ER 2 فقط)
- [فهم الفيديو](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=ar): العثور على اللحظات وتصنيف مستوى التقدّم (الإصدار الثاني من Gemini Robotics فقط)
- [أمان الروبوتات في Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=ar): أبحاث الأمان التي تستند إليها مجموعة النماذج

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
