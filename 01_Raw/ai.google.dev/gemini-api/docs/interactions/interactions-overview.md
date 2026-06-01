---
source_url: https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=ar
fetched_at: 2026-06-01T06:04:58.854274+00:00
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

**Interactions API** هو المعيار الجديد الذي يُنصح به عند إنشاء تطبيقات باستخدام Gemini. تم تحسينه ليتوافق مع مهام سير العمل المستندة إلى وكلاء وإدارة الحالة من جهة الخادم والمحادثات المعقّدة المتعددة الوسائط والمتعددة الأدوار. ستظلّ واجهة برمجة التطبيقات الأصلية [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ar) متوافقة تمامًا.

## لماذا يجب استخدام Interactions API؟

- **إدارة السجلّ من جهة الخادم**: تبسيط مسارات المحادثات المتعددة الأدوار من خلال `previous_interaction_id` يسمح الخادم بالحالة تلقائيًا (`store=true`)، ولكن يمكنك اختيار السلوك غير المرتبط بحالة من خلال ضبط `store=false`.
- **خطوات التنفيذ القابلة للمراقبة**: تسهّل الخطوات المكتوبة تصحيح الأخطاء في التدفقات المعقّدة وعرض واجهة المستخدم للأحداث الوسيطة (مثل الأفكار أو أدوات البحث).
- **مصمَّم لسير العمل المستند إلى الذكاء الاصطناعي الوكيل**: يتوافق بشكلٍ كامل مع استخدام الأدوات المتعددة الخطوات والتنسيق وسير العمل المعقّد من خلال خطوات التنفيذ المكتوبة.
- **المهام الطويلة والمهام التي يتم تنفيذها في الخلفية**: تتيح نقل العمليات التي تستغرق وقتًا طويلاً، مثل [Deep Think](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=ar) و[Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=ar)، إلى العمليات التي يتم تنفيذها في الخلفية باستخدام `background=true`.
- **الوصول إلى النماذج والإمكانات الجديدة**: من الآن فصاعدًا، سيتم إطلاق النماذج الجديدة التي تتجاوز عائلة النماذج الأساسية، بالإضافة إلى الإمكانات والأدوات الجديدة بالذكاء الاصطناعي الوكيل، حصريًا على Interactions API.

**استخدِم Interactions API** إذا كنت تبدأ مشروعًا جديدًا أو تنشئ تطبيقات مستندة إلى وكيل أو تحتاج إلى إدارة المحادثات من جهة الخادم. **استخدِم [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ar)** إذا كان لديك عملية دمج حالية تناسب احتياجاتك، أو إذا كنت بحاجة إلى ميزة [غير متاحة بعد](#limitations) في Interactions API، مثل Batch API أو التخزين المؤقت الصريح.

## البدء

- **إعداد وكيل الترميز**: اربط وكيلك **ببروتوكول MCP في "مستندات Gemini"** وثبِّت مهارة `gemini-interactions-api` لمنح مساعدك إذن الوصول المباشر إلى أحدث مستندات المطوّرين وأفضل الممارسات.
  [إعداد وكيل الترميز →](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ar)
- **نقل البيانات من `generateContent`**: إذا كان لديك عملية دمج حالية، اتّبِع [دليل نقل البيانات](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ar) للانتقال إلى Interactions API.
- **تجربة التشغيل السريع**: ابدأ باستخدام مثال بسيط يعمل في [دليل التشغيل السريع لواجهة Interactions API](https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=ar).

### أدلة الميزات

يمكنك استكشاف الإمكانات المحدّدة لواجهة برمجة التطبيقات Interactions API من خلال هذه الأدلة. يمكنك استخدام زر التبديل في هذه الصفحات للتبديل بين generateContent وInteractions API:

- [إنشاء النصوص](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ar)
- [إنشاء الصور](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=ar)
- [فهم الصور](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=ar)
- [فهم الصوت](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=ar)
- [فهم الفيديو](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=ar)
- [معالجة المستندات](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=ar)
- [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar)
- [الناتج المنظَّم](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=ar)
- [وكيل Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=ar)
- [الاستدلال المرن](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=ar)
- [استنتاج الأولوية](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=ar)
- [بث](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=ar)

## طريقة عمل Interactions API

تتمحور واجهة Interactions API حول مورد أساسي هو [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=ar#Resource:Interaction). يمثّل `Interaction` دورة كاملة في محادثة أو مهمة. يعمل هذا السجلّ كسجلّ جلسة، ويحتوي على السجلّ الكامل للتفاعل كسلسلة زمنية من **خطوات التنفيذ**. تشمل هذه الخطوات أفكار النموذج، وعمليات استدعاء الأدوات ونتائجها من جهة الخادم أو العميل (مثل `function_call` و`function_result`)، و`model_output` النهائي. يتضمّن المرجع المخزّن (الذي يتم استرجاعه من خلال `interactions.get`) أيضًا خطوات `user_input` للحصول على السياق الكامل، على الرغم من أنّ استجابة `interactions.create` تعرض فقط الخطوات التي أنشأها النموذج.

عند إجراء طلب إلى
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=ar#CreateInteraction)، فإنّك
تنشئ مورد `Interaction` جديدًا.

### الوصول إلى النتائج باستخدام خصائص سهلة الاستخدام في حزمة SDK

على الرغم من أنّ Interactions API تعرض مخططًا زمنيًا منظَّمًا لخطوات التنفيذ (مثل الأفكار وطلبات البحث واستدعاء الدوال)، ليس عليك الانتقال يدويًا بين الخطوات للحصول على الرد النهائي من النموذج.

توفّر حِزم تطوير البرامج (SDK) من Google للذكاء الاصطناعي التوليدي خصائص ملائمة مباشرةً في عنصر `Interaction` الذي يتم عرضه للوصول إلى النواتج الخاصة بالوسائط المختلفة:

| السمة المريحة لحزمة تطوير البرامج (SDK) | نوع القيمة التي يتم عرضها | الوصف |
| --- | --- | --- |
| **`interaction.output_text`** | سلسلة | تعرض هذه السمة آخر كتل نصية في ردّ النموذج. إذا تم تقسيم الرد على عدة كتل `TextContent` متتالية، سيتم ربطها تلقائيًا. لا يتضمّن هذا القسم كتل نصية سابقة مفصولة بمحتوى غير نصي (مثل الأفكار أو الصور أو المحتوى الصوتي أو طلبات استخدام الأدوات). بالنسبة إلى الردود المعقّدة أو المتداخلة المتعدّدة الوسائط، عليك تكرار `steps` يدويًا بدلاً من ذلك. |
| **`interaction.output_image`** | ‫ImageContent أو `None` | تعرض هذه السمة آخر كتلة صور أنشأها النموذج في الطلب الحالي. |
| **`interaction.output_audio`** | AudioContent أو `None` | تعرض هذه السمة آخر مقطع صوتي أنشأه النموذج في الطلب الحالي. |

بالنسبة إلى حالات الاستخدام المتقدّمة، مثل عرض عمليات التفكير الوسيطة أو فحص عمليات استدعاء الأدوات خطوة بخطوة أو تصحيح الأخطاء، يمكنك مواصلة فحص مخطط `interaction.steps` الزمني الأولي وتصفّحه يدويًا.

### إدارة الحالة من جهة الخادم

يمكنك استخدام `id` لتفاعل مكتمل في مكالمة لاحقة باستخدام المَعلمة `previous_interaction_id` لمواصلة المحادثة. يستخدم الخادم هذا المعرّف لاسترداد سجلّ المحادثات، ما يوفّر عليك عناء إعادة إرسال سجلّ المحادثات بأكمله.

تحتفظ المَعلمة `previous_interaction_id` بسجلّ المحادثات فقط (المدخلات والمخرجات) باستخدام `previous_interaction_id`. المَعلمات الأخرى **محدودة بنطاق التفاعل**
ولا تنطبق إلا على التفاعل المحدّد الذي يتم إنشاؤه حاليًا:

- `tools`
- `system_instruction`
- ‫`generation_config` (بما في ذلك `thinking_level` و`temperature` وما إلى ذلك)

وهذا يعني أنّه عليك إعادة تحديد هذه المَعلمات في كل تفاعل جديد إذا كنت تريد تطبيقها. إدارة الحالة من جهة الخادم هي إجراء اختياري، ويمكنك أيضًا التشغيل في وضع بلا حالة من خلال إرسال سجلّ المحادثة الكامل في كل طلب.

### تخزين البيانات والاحتفاظ بها

تخزّن واجهة برمجة التطبيقات تلقائيًا جميع عناصر Interaction (`store=true`) بهدف تسهيل استخدام ميزات إدارة الحالة من جهة الخادم (باستخدام `previous_interaction_id`) والتنفيذ في الخلفية (باستخدام `background=true`) ولأغراض إمكانية تتبّع البيانات.

- **المستوى المدفوع**: يحتفظ النظام بالتفاعلات لمدة **55 يومًا**.
- **المستوى المجاني**: يحتفظ النظام بالتفاعلات لمدة **يوم واحد**.

إذا كنت لا تريد ذلك، يمكنك ضبط `store=false` في طلبك. يتم فصل عنصر التحكّم هذا عن إدارة الحالة، ويمكنك إيقاف مساحة التخزين لأي تفاعل. يُرجى العِلم أنّ `store=false` لا يتوافق مع `background=true` ويمنع استخدام `previous_interaction_id` في الأدوار اللاحقة.

يمكنك حذف التفاعلات المخزّنة في أي وقت باستخدام طريقة الحذف المتوفّرة في [مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api/interactions-api?hl=ar). لا يمكنك حذف التفاعلات إلا إذا كنت تعرف رقم تعريف التفاعل.

وبعد انتهاء صلاحية فترة التخزين، سيتم حذف بياناتك تلقائيًا.

يعالج النظام عناصر التفاعل وفقًا [للبنود](https://ai.google.dev/gemini-api/terms?hl=ar).

## أفضل الممارسات

- **نسبة نتيجة ذاكرة التخزين المؤقت**: يتيح استخدام `previous_interaction_id` لمواصلة المحادثات للنظام الاستفادة بسهولة أكبر من التخزين المؤقت الضمني لسجلّ المحادثات، ما يحسّن الأداء ويقلّل التكاليف.
- **مزج التفاعلات**: يمكنك مزج التفاعلات بين الوكيل والنموذج ومطابقتها ضمن محادثة واحدة. على سبيل المثال، يمكنك استخدام وكيل متخصص، مثل وكيل &quot;البحث المعمّق&quot;، لجمع البيانات الأولية، ثم استخدام نموذج Gemini عادي لتنفيذ مهام المتابعة، مثل التلخيص أو إعادة التنسيق، وربط هذه الخطوات باستخدام `previous_interaction_id`.

## الطُرز والوكلاء المتوافقون

| اسم النموذج | النوع | رقم تعريف الطراز |
| --- | --- | --- |
| Gemini 3.5 Flash | الطراز | `gemini-3.5-flash` |
| Gemini 3.1 Flash-Lite | الطراز | `gemini-3.1-flash-lite` |
| معاينة Gemini 3.1 Pro | الطراز | `gemini-3.1-pro-preview` |
| معاينة Gemini 3 Flash | الطراز | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | الطراز | `gemini-2.5-pro` |
| Gemini 2.5 Flash | الطراز | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | الطراز | `gemini-2.5-flash-lite` |
| معاينة مقطع Lyria 3 | الطراز | `lyria-3-clip-preview` |
| معاينة Lyria 3 Pro | الطراز | `lyria-3-pro-preview` |
| معاينة Deep Research | الوكيل | `deep-research-pro-preview-12-2025` |
| معاينة Deep Research | الوكيل | `deep-research-preview-04-2026` |
| معاينة Deep Research | الوكيل | `deep-research-max-preview-04-2026` |

## حزم SDK

يمكنك استخدام أحدث إصدار من حِزم تطوير البرامج (SDK) من Google GenAI للوصول إلى واجهة برمجة التطبيقات Interactions API.

- في Python، هذه هي حزمة `google-genai` من الإصدار `1.55.0` فصاعدًا.
- في JavaScript، هذه هي حزمة `@google/genai` من الإصدار `1.33.0` والإصدارات الأحدث.

يمكنك الاطّلاع على مزيد من المعلومات حول كيفية تثبيت حِزم SDK في صفحة [المكتبات](https://ai.google.dev/gemini-api/docs/libraries?hl=ar).

## القيود

- **حالة الإصدار التجريبي**: تتوفّر Interactions API في إصدار تجريبي/معاينة. قد تتغيّر الميزات والمخططات.
- **MCP عن بُعد**: لا يتوافق Gemini 3 مع MCP عن بُعد، ولكن ستتوفّر هذه الميزة قريبًا.

تتوافق الميزات التالية مع واجهة برمجة التطبيقات
[`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ar)، ولكنها **غير متاحة بعد** في واجهة Interactions API:

- **[البيانات الوصفية للفيديو](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=ar)**: الحقل `video_metadata`، ويُستخدم لضبط فواصل التقطيع ومعدّلات اللقطات المخصّصة لفهم الفيديو.
- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar)**
- **[استدعاء الدوال تلقائيًا (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=ar#automatic_function_calling_python_only)**
- **[التخزين المؤقت الصريح](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=ar)**: يُرجى العِلم أنّ التخزين المؤقت الضمني من جهة الخادم متاح في Interactions API
  من خلال `previous_interaction_id`.

## التغييرات التي قد تؤدي إلى أعطال

تتوفّر واجهة برمجة التطبيقات Interactions API حاليًا في مرحلة تجريبية مبكرة. نعمل حاليًا على تطوير وتحسين إمكانات واجهة برمجة التطبيقات ومخططات الموارد وواجهات حزمة تطوير البرامج (SDK) استنادًا إلى الاستخدام الفعلي وملاحظات المطوّرين. نتيجةً لذلك، **قد تحدث تغييرات غير متوافقة مع الإصدارات السابقة**.

التغييرات الحالية التي قد تؤدي إلى عطل:

- **مخطط الخطوات**: تحلّ مصفوفة خطوات جديدة محلّ مصفوفة النتائج، ما يوفّر مخططًا زمنيًا منظَّمًا لكلّ دورة تفاعل.

للاطّلاع على آخر تغيير قد يؤدي إلى أعطال ومعرفة كيفية نقل البيانات، يُرجى الرجوع إلى [دليل نقل البيانات المتعلقة بالتغييرات التي قد تؤدي إلى أعطال (مايو 2026)](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=ar).

قد تشمل التحديثات المحتملة الأخرى تغييرات في مخططات الإدخال والإخراج، وتوقيعات طرق حزمة تطوير البرامج (SDK) وبُنى العناصر، وسلوكيات ميزات معيّنة.

بالنسبة إلى أحمال العمل في مرحلة الإنتاج، عليك مواصلة استخدام واجهة برمجة التطبيقات القياسية
[`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=ar). ويظل هذا المسار هو المسار المقترَح لعمليات النشر الثابتة، وسنواصل تطويره وصيانته بشكل نشط.

## الملاحظات

تُعدّ ملاحظاتك مهمة جدًا لتطوير Interactions API.
يمكنك مشاركة أفكارك أو الإبلاغ عن أخطاء أو طلب ميزات في [منتدى مطوّري الذكاء الاصطناعي من Google](https://discuss.ai.google.dev/c/gemini-api/4?hl=ar).

## الخطوات التالية

- جرِّب [دفتر ملاحظات التشغيل السريع لواجهة Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=ar).
- [مزيد من المعلومات حول التفاعلات أثناء البث](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=ar) للتعامل مع الردود في الوقت الفعلي
- [مزيد من المعلومات حول "وكيل Deep Research" في Gemini](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
