---
source_url: https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=ar
fetched_at: 2026-06-15T06:20:07.279475+00:00
title: "\u0648\u0627\u062c\u0647\u0629 \u0628\u0631\u0645\u062c\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642\u0627\u062a Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# واجهة برمجة التطبيقات Interactions API

‫**Interactions API** هي المعيار الجديد المقترَح للإنشاء باستخدام Gemini. وهي محسّنة لسير العمل بالذكاء الاصطناعي الوكيل وإدارة الحالة من جهة الخادم والمحادثات المعقّدة المتعددة الوسائط والمحادثات المترابطة. تظلّ [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ar) API الأصلية متوافقة تمامًا.

## أهمية استخدام Interactions API

- **إدارة سجلّ المحادثات من جهة الخادم**: تبسيط التدفقات متعددة المحادثات المترابطة من خلال `previous_interaction_id` يُفعِّل الخادم الحالة تلقائيًا (`store=true`)، ولكن يمكنك اختيار السلوك بدون حالة من خلال ضبط `store=false`.
- **خطوات التنفيذ القابلة للمراقبة**: تسهّل الخطوات المكتوبة تصحيح الأخطاء في التدفقات المعقّدة وعرض واجهة المستخدم للأحداث الوسيطة (مثل الأفكار أو مربّعات البحث).
- **مصمّمة لسير العمل بالذكاء الاصطناعي الوكيل**: توفّر دعمًا أصليًا لاستخدام الأدوات المتعددة الخطوات والتنسيق وتدفقات الاستدلال المعقّدة من خلال خطوات التنفيذ المكتوبة.
- **المهام الطويلة والمهام في الخلفية**: تتيح نقل العمليات التي تستغرق وقتًا طويلاً
  إلى العمليات في الخلفية باستخدام `background=true`. يتوفّر ذلك لكلّ من النماذج (مثل
  [Deep Think](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=ar)) والوكلاء (مثل
  [Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=ar)).
- **الوصول إلى النماذج والإمكانات الجديدة**: من الآن فصاعدًا، سيتم إطلاق النماذج الجديدة التي تتجاوز عائلة النماذج الأساسية، بالإضافة إلى الإمكانات والأدوات الجديدة بالذكاء الاصطناعي الوكيل، حصريًا على Interactions API.

**استخدِم Interactions API** إذا كنت تبدأ مشروعًا جديدًا أو تنشئ تطبيقات بالذكاء الاصطناعي الوكيل أو تحتاج إلى إدارة المحادثات من جهة الخادم. **استخدِم [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ar)** إذا كان لديك عملية دمج حالية تلبي احتياجاتك أو إذا كنت بحاجة إلى ميزة [غير متاحة بعد](#limitations) في Interactions API، مثل Batch API أو التخزين المؤقت الصريح.

## البدء

- **إعداد وكيل الترميز**: يمكنك الاتصال بـ **Gemini Docs MCP** وتثبيت
  مهارة `gemini-interactions-api` لمنح مساعدك إمكانية الوصول المباشر إلى
  أحدث مستندات المطوّرين وأفضل الممارسات.
  [إعداد وكيل الترميز ←](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ar)
- **نقل البيانات من `generateContent`**: إذا كان لديك عملية دمج حالية،
  اتّبِع [دليل نقل البيانات](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ar) للانتقال إلى Interactions API.
- **تجربة التشغيل السريع**: ابدأ باستخدام مثال بسيط من
  [Interactions API quickstart](https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=ar).

### أدلة الميزات

يمكنك استكشاف الإمكانات المحدّدة لـ Interactions API من خلال هذه الأدلة. يمكنك استخدام الزرّ في هذه الصفحات للتبديل بين generateContent وInteractions API:

- [إنشاء النصوص](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ar)
- [إنشاء الصور](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=ar)
- [فهم الصور](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=ar)
- [فهم المحتوى الصوتي](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=ar)
- [فهم الفيديوهات](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=ar)
- [معالجة المستندات](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=ar)
- [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar)
- [ناتج منظَّم](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=ar)
- [وكيل Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=ar)
- [الاستدلال المرن](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=ar)
- [الاستدلال حسب الأولوية](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=ar)
- [بث](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=ar)

## طريقة عمل Interactions API

تتمحور Interactions API حول مورد أساسي: الـ [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=ar#Resource:Interaction). يمثّل `Interaction` دورًا كاملاً في محادثة أو مهمة. ويعمل كسجلّ جلسة، يحتوي على سجلّ التفاعل بالكامل كسلسلة زمنية من **خطوات التنفيذ**. تتضمّن هذه الخطوات أفكار النموذج واستدعاءات الأدوات ونتائجها من جهة الخادم أو من جهة العميل (مثل `function_call` و`function_result`) و`model_output` النهائي. يتضمّن المورد المخزَّن (الذي يتم استرداده من خلال `interactions.get`) أيضًا خطوات `user_input` للحصول على السياق الكامل، على الرغم من أنّ استجابة `interactions.create` لا تعرض سوى الخطوات التي أنشأها النموذج.

عند إجراء طلب إلى
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=ar#CreateInteraction)، أنت
تنشئ موردًا جديدًا `Interaction`.

### الوصول إلى النتائج باستخدام خصائص حزمة تطوير البرامج (SDK) المريحة

على الرغم من أنّ Interactions API تعرض جدولاً زمنيًا منظَّمًا لخطوات التنفيذ (مثل الأفكار وطلبات البحث واستدعاءات الدوال)، ليس عليك الانتقال يدويًا بين الخطوات للحصول على استجابة النموذج النهائية.

توفر حِزم تطوير البرامج (SDK) للذكاء الاصطناعي التوليدي من Google خصائص مريحة مباشرةً
في عنصر `Interaction` الذي يتم عرضه للوصول إلى النتائج لمختلف
الوسائط:

| خاصية حزمة تطوير البرامج (SDK) المريحة | نوع القيمة التي يتم عرضها | الوصف |
| --- | --- | --- |
| **`interaction.output_text`** | سلسلة | تعرض آخر فقرات نصية في استجابة النموذج. إذا تم تقسيم الاستجابة على عدّة فقرات `TextContent` متتالية، يتم دمجها تلقائيًا. لا تتضمّن الفقرات النصية السابقة التي تفصلها محتوى غير نصي (مثل الأفكار أو الصور أو المحتوى الصوتي أو استدعاءات الأدوات). بالنسبة إلى الاستجابات المعقّدة أو المتداخلة المتعددة الوسائط، عليك تكرار `steps` يدويًا بدلاً من ذلك. |
| **`interaction.output_image`** | ImageContent أو `None` | تعرض آخر فقرة صور أنشأها النموذج في الطلب الحالي. |
| **`interaction.output_audio`** | AudioContent أو `None` | تعرض آخر فقرة صوت أنشأها النموذج في الطلب الحالي. |

بالنسبة إلى حالات الاستخدام المتقدّمة، مثل عرض عمليات التفكير الوسيطة أو فحص استدعاءات الأدوات خطوة بخطوة أو تصحيح الأخطاء، يمكنك مع ذلك فحص الجدول الزمني `interaction.steps` الأولي والانتقال بين الخطوات يدويًا.

### إدارة الحالة من جهة الخادم

يمكنك استخدام `id` لتفاعل مكتمل في طلب لاحق باستخدام
`previous_interaction_id` لمواصلة المحادثة. يستخدم الخادم هذا المعرّف لاسترداد سجلّ المحادثات، ما يوفّر عليك إعادة إرسال سجلّ المحادثات بالكامل.

تحتفظ المَعلمة `previous_interaction_id` بسجلّ المحادثات فقط (المدخلات والمخرجات) باستخدام `previous_interaction_id`. أما المَعلمات الأخرى، فهي **ضمن نطاق التفاعل** ولا تنطبق إلا على التفاعل المحدّد الذي تنشئه حاليًا:

- `tools`
- `system_instruction`
- `generation_config` (بما في ذلك `thinking_level` و`temperature` وما إلى ذلك)

هذا يعني أنّه عليك إعادة تحديد هذه المَعلمات في كل تفاعل جديد إذا كنت تريد تطبيقها. تكون إدارة الحالة من جهة الخادم اختيارية، ويمكنك أيضًا العمل في وضع بدون حالة من خلال إرسال سجلّ المحادثات الكامل في كل طلب.

### التنفيذ في الخلفية

بالنسبة إلى المهام الطويلة، يمكنك تشغيل التفاعلات في الخلفية من خلال ضبط `background=true` في طلبك. يتوفّر ذلك لكلّ من:

- [**النماذج**: مفيدة للمهام التي تستغرق وقتًا أطول للمعالجة، مثل المهام التي تستخدم التفكير.](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=ar)
- **الوكلاء**: مطلوبة لسير عمل الوكلاء الطويل، مثل
  [Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=ar).

عند التشغيل في الخلفية:

- عليك ضبط `store=true` (الإعداد التلقائي) لأنّ النظام يحتاج إلى تخزين مورد التفاعل حتى تتمكّن من استرداده لاحقًا.
- يعرض الطلب الأولي إلى `interactions.create` على الفور حالة `in_progress`.
- يمكنك استرداد حالة التفاعل ونتائجه من خلال استدعاء
  `interactions.get` باستخدام معرّف التفاعل، أو من خلال ضبط
  [روابط الويب](https://ai.google.dev/gemini-api/docs/interactions/webhooks?hl=ar) لتلقّي الإشعارات
  عند اكتمال التفاعل.
- يمكنك أيضًا
  [بث](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=ar#streaming-background) التفاعل لتلقّي آخر الأخبار عن التقدّم.

### تخزين البيانات والاحتفاظ بها

تخزّن واجهة برمجة التطبيقات تلقائيًا جميع عناصر التفاعل (`store=true`) لتسهيل استخدام ميزات إدارة الحالة من جهة الخادم (باستخدام `previous_interaction_id`) والتنفيذ في الخلفية (باستخدام `background=true`) ولأغراض إمكانية تتبّع البيانات.

- **الخطة المدفوعة**: يحتفظ النظام بالتفاعلات لمدة **55 يومًا**.
- **الخطة المجانية**: يحتفظ النظام بالتفاعلات لمدة **يوم واحد**.

إذا لم تكن تريد ذلك، يمكنك ضبط `store=false` في طلبك. يختلف عنصر التحكّم هذا عن إدارة الحالة، ويمكنك إيقاف التخزين لأي تفاعل. ومع ذلك، يُرجى العِلم أنّ `store=false` غير متوافق مع `background=true` ويمنع استخدام `previous_interaction_id` للأدوار اللاحقة.

يمكنك حذف التفاعلات المخزَّنة في أي وقت باستخدام طريقة الحذف المتوفّرة في
[مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api/interactions-api?hl=ar). لا يمكنك حذف التفاعلات إلا إذا كنت تعرف معرّف التفاعل.

وبعد انتهاء فترة التخزين، سيتم حذف بياناتك تلقائيًا.

يعالج النظام عناصر التفاعل وفقًا للأحكام .

## أفضل الممارسات

- **معدّل نتائج ذاكرة التخزين المؤقت**: يتيح استخدام `previous_interaction_id` لمواصلة المحادثات للنظام استخدام التخزين المؤقت الضمني لـ سجلّ المحادثات بسهولة أكبر، ما يحسّن الأداء ويقلّل التكاليف.
- **دمج التفاعلات**: يمكنك دمج تفاعلات الوكيل و
  النموذج ومطابقتها ضمن محادثة. على سبيل المثال، يمكنك استخدام وكيل متخصّص، مثل وكيل Deep Research، لجمع البيانات الأولية، ثم استخدام نموذج Gemini عادي للمهام اللاحقة، مثل التلخيص أو إعادة التنسيق، وربط هذه الخطوات باستخدام `previous_interaction_id`.

## النماذج والوكلاء المتوافقون

| اسم النموذج | النوع | رقم تعريف الطراز |
| --- | --- | --- |
| Gemini 3.5 Flash | الطراز | `gemini-3.5-flash` |
| Gemini 3.1 Flash-Lite | الطراز | `gemini-3.1-flash-lite` |
| Gemini 3.1 Pro Preview | الطراز | `gemini-3.1-pro-preview` |
| Gemini 3 Flash Preview | الطراز | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | الطراز | `gemini-2.5-pro` |
| Gemini 2.5 Flash | الطراز | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | الطراز | `gemini-2.5-flash-lite` |
| Lyria 3 Clip Preview | الطراز | `lyria-3-clip-preview` |
| Lyria 3 Pro Preview | الطراز | `lyria-3-pro-preview` |
| Deep Research Preview | الوكيل | `deep-research-pro-preview-12-2025` |
| Deep Research Preview | الوكيل | `deep-research-preview-04-2026` |
| Deep Research Preview | الوكيل | `deep-research-max-preview-04-2026` |

## حزم SDK

يمكنك استخدام أحدث إصدار من حِزم تطوير البرامج (SDK) للذكاء الاصطناعي التوليدي من Google للوصول إلى Interactions API.

- في Python، هذه هي حزمة `google-genai` من الإصدار `1.55.0` والإصدارات الأحدث.
- في JavaScript، هذه هي حزمة `@google/genai` من الإصدار `1.33.0` والإصدارات الأحدث.

يمكنك الاطّلاع على مزيد من المعلومات حول كيفية تثبيت حِزم تطوير البرامج (SDK) في صفحة
[المكتبات](https://ai.google.dev/gemini-api/docs/libraries?hl=ar).

## القيود

- **الحالة التجريبية**: تتوفّر Interactions API في إصدار تجريبي. قد تتغيّر الميزات والمخططات.
- **Remote MCP**: لا يتيح Gemini 3 استخدام Remote MCP، ولكن سيتم توفيره قريبًا.

تتيح
[`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ar) API الميزات التالية، ولكنها **غير متاحة بعد** في Interactions API:

- **[بيانات الفيديو الوصفية](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=ar)**: الحقل `video_metadata`، الذي يُستخدم لضبط فواصل الاقتصاص
  ومعدّلات الإطارات المخصّصة لفهم الفيديوهات
- **[‫\*\*Batch API\*\*](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar)**
- **[استدعاء الدوال تلقائيًا (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=ar#automatic_function_calling_python_only)**
- **[التخزين المؤقت الصريح](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=ar)**: يُرجى العِلم أنّ التخزين المؤقت الضمني من جهة الخادم متاح في Interactions API
  عبر `previous_interaction_id`.

## تغييرات قد تؤدي إلى أعطال

تتوفّر Interactions API حاليًا في مرحلة تجريبية مبكرة. نعمل بنشاط على تطوير وتحسين إمكانات واجهة برمجة التطبيقات ومخططات الموارد وواجهات حزمة تطوير البرامج (SDK) استنادًا إلى الاستخدام الفعلي وملاحظات المطوّرين. نتيجةً لذلك، **قد تحدث تغييرات قد تؤدي إلى أعطال**.

التغييرات الحالية التي قد تؤدي إلى أعطال:

- **مخطط الخطوات**: تحلّ مجموعة خطوات جديدة محلّ مجموعة النتائج، ما يوفّر جدولاً زمنيًا منظَّمًا لكل دور من أدوار التفاعل.

للتعرّف على أحدث تغيير قد يؤدي إلى عطل وكيفية نقل البيانات، يُرجى الاطّلاع على [دليل نقل البيانات بسبب التغييرات التي قد تؤدي إلى أعطال (مايو 2026)](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=ar).

قد تتضمّن التحديثات المحتمَلة الأخرى تغييرات في مخططات الإدخال والإخراج وتوقيعات طرق حزمة تطوير البرامج (SDK) وبُنى العناصر وسلوكيات ميزات محدّدة.

بالنسبة إلى أحمال العمل في مرحلة الإنتاج، عليك مواصلة استخدام
[`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ar) API العادية. تظلّ هذه الواجهة هي المسار المقترَح للعمليات الثابتة، وسنواصل تطويرها وصيانتها بنشاط.

## الملاحظات

ملاحظاتك ضرورية لتطوير Interactions API.
يمكنك مشاركة أفكارك أو الإبلاغ عن الأخطاء أو طلب ميزات في
[منتدى Google AI Developer Community](https://discuss.ai.google.dev/c/gemini-api/4?hl=ar).

## الخطوات التالية

- تجربة دفتر ملاحظات [Interactions API quickstart](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=ar)
- التعرّف على [التفاعلات المتدفقة](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=ar) لمعالجة الاستجابات في الوقت الفعلي
- مزيد من المعلومات حول [وكيل Deep Research في Gemini](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-08 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-08 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
