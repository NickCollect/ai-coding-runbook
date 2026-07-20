---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar
fetched_at: 2026-07-20T04:33:14.152415+00:00
title: "\u0648\u0627\u062c\u0647\u0629 \u0628\u0631\u0645\u062c\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642\u0627\u062a Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# واجهة برمجة التطبيقات Interactions API

توفّر Interactions API أفضل طريقة لتصميم التطبيقات باستخدام نماذج Gemini ووكلاء Gemini. اعتبارًا من يونيو 2026، أصبحت هذه الميزة متاحة بشكل عام ويُنصح باستخدامها في جميع المشاريع الجديدة. على الرغم من أنّ واجهة برمجة التطبيقات الأصلية
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ar) أصبحت قديمة،
إلا أنّها لا تزال متوافقة تمامًا.

## أسباب استخدام Interactions API

- **واجهة عالمية لجميع التطبيقات**: تم تصميمها لتكون الواجهة العادية لكل حالة استخدام، بما في ذلك إنشاء النصوص في محادثة واحدة، والفهم المتعدّد الوسائط، والمخرجات المنظَّمة، وتنظيم الأدوات، وسير العمل المستند إلى الوكلاء.
- **واجهة برمجة تطبيقات واحدة للنماذج والوكلاء**: نقطة نهاية ونمط موحّدان
  لاستدعاء نماذج Gemini العادية والوكلاء المتخصّصين مباشرةً (مثل
  Deep Research والوكلاء المخصّصين المُدارين).
- **إمكانات جديدة جاهزة للاستخدام**: ميزات مثل حالة المحادثة الاختيارية من جهة الخادم باستخدام `previous_interaction_id`، وخطوات التنفيذ القابلة للمراقبة لتصحيح الأخطاء وعرض واجهة المستخدم، و[التنفيذ في الخلفية](https://ai.google.dev/gemini-api/docs/background-execution?hl=ar) للمهام الطويلة الأمد باستخدام `background=true`.
- **تكلفة أقل مع معدّلات أعلى لنتيجة ذاكرة التخزين المؤقت**: عند استخدام المحادثات المترابطة، تتيح إدارة الحالة الاختيارية من جهة الخادم تخزينًا مؤقتًا أكثر فعالية للسياق على مستوى الأدوار، ما يقلّل من تكاليف الرموز المميزة.
- **مكان إطلاق الميزات الجديدة**: من الآن فصاعدًا، سيتم إطلاق جميع النماذج الجديدة والإمكانات والأدوات والميزات المستندة إلى الذكاء الاصطناعي التفاعلي على Interactions API.

تخزّن Interactions API الطلبات تلقائيًا حتى تتمكّن من الاستفادة من ميزات إدارة الحالة من جهة الخادم باستخدام `previous_interaction_id`. يمكنك تفعيل السلوك غير المرتبط بحالة معيّنة من خلال ضبط
`store=false`. راجِع قسم [الاحتفاظ بالبيانات](#data-storage-retention) لمعرفة التفاصيل.

## البدء

- **إعداد وكيل الترميز**: اربط وكيل الترميز **ببروتوكول MCP الخاص بـ &quot;مستندات Gemini&quot;** وثبِّت مهارة `gemini-interactions-api` لمنح مساعدك إذن الوصول المباشر إلى أحدث مستندات المطوّرين وأفضل الممارسات. لمعرفة الخطوات التفصيلية، يُرجى الاطّلاع على
  [دليل إعداد وكيل الترميز](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ar).
- **نقل البيانات من `generateContent`**: إذا كان لديك عملية دمج حالية، اتّبِع [دليل نقل البيانات](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ar) للانتقال إلى Interactions API.
- **البدء**: اتّبِع الخطوات الواردة في [دليل البدء في استخدام Interactions API](https://ai.google.dev/gemini-api/docs/get-started?hl=ar).

### أدلة الميزات

يمكنك استكشاف الإمكانات المحدّدة لواجهة Interactions API من خلال هذه الأدلة. يمكنك استخدام زر التبديل في هذه الصفحات للتبديل بين generateContent وInteractions API:

- [إنشاء النصوص](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar)
- [إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar)
- [فهم الصور](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ar)
- [فهم الصوت](https://ai.google.dev/gemini-api/docs/audio?hl=ar)
- [فهم الفيديوهات](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar)
- [معالجة المستندات](https://ai.google.dev/gemini-api/docs/document-processing?hl=ar)
- [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)
- [الناتج المنظَّم](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar)
- [Deep Research Agent](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar)
- [الاستدلال المرن](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ar)
- [استنتاج الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar)

## طريقة عمل Interactions API

تتمحور واجهة Interactions API حول مورد أساسي هو [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=ar#Resource:Interaction). يمثّل `Interaction` دورة كاملة في محادثة أو مهمة. يعمل هذا السجلّ كسجلّ جلسة، ويحتوي على السجلّ الكامل للتفاعل كسلسلة زمنية من **خطوات التنفيذ**. تشمل هذه الخطوات أفكار النموذج، وعمليات استدعاء الأدوات ونتائجها من جهة الخادم أو العميل (مثل `function_call` و`function_result`)، و`model_output` النهائي. يتضمّن المرجع المخزّن (الذي يتم استرجاعه من خلال `interactions.get`) أيضًا خطوات `user_input` للحصول على السياق الكامل، على الرغم من أنّ استجابة `interactions.create` تعرض فقط الخطوات التي أنشأها النموذج.

عند إجراء مكالمة إلى
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=ar#CreateInteraction)، فإنّك
تنشئ مورد `Interaction` جديدًا.

### إدارة الحالة من جهة الخادم

يمكنك استخدام `id` لتفاعل مكتمل في مكالمة لاحقة باستخدام المَعلمة `previous_interaction_id` لمواصلة المحادثة. يستخدم الخادم هذا المعرّف لاسترداد سجلّ المحادثات، ما يوفّر عليك عناء إعادة إرسال سجلّ المحادثات بأكمله.

تحتفظ المَعلمة `previous_interaction_id` بسجلّ المحادثات فقط (المدخلات والمخرجات) باستخدام `previous_interaction_id`. المَعلمات الأخرى **محدودة بنطاق التفاعل**
ولا تنطبق إلا على التفاعل المحدّد الذي يتم إنشاؤه حاليًا:

- `tools`
- `system_instruction`
- ‫`generation_config` (بما في ذلك `thinking_level` و`temperature` وما إلى ذلك)

وهذا يعني أنّه عليك إعادة تحديد هذه المَعلمات في كل تفاعل جديد إذا كنت تريد تطبيقها. إدارة الحالة من جهة الخادم هي إجراء اختياري، ويمكنك أيضًا التشغيل في وضع بلا حالة من خلال إرسال سجلّ المحادثة الكامل في كل طلب.

### تخزين البيانات والاحتفاظ بها

تخزِّن واجهة برمجة التطبيقات تلقائيًا جميع عناصر Interaction (`store=true`) بهدف تسهيل استخدام ميزات إدارة الحالة من جهة الخادم (باستخدام `previous_interaction_id`) و[التنفيذ في الخلفية](https://ai.google.dev/gemini-api/docs/background-execution?hl=ar) (باستخدام `background=true`) ولأغراض إمكانية تتبّع البيانات.

- **المستوى المدفوع**: يحتفظ النظام بالتفاعلات لمدة **55 يومًا**.
- **المستوى المجاني**: يحتفظ النظام بالتفاعلات لمدة **يوم واحد**.

إذا لم تكن تريد ذلك، يمكنك ضبط `store=false` في طلبك. يختلف عنصر التحكّم هذا عن إدارة الحالة، ويمكنك إيقاف مساحة التخزين لأي تفاعل. يُرجى العِلم أنّ `store=false` غير متوافق مع [التنفيذ في الخلفية](https://ai.google.dev/gemini-api/docs/background-execution?hl=ar) ويمنع استخدام `previous_interaction_id` في الأدوار اللاحقة.

بالنسبة إلى مشاريع &quot;المستوى المدفوع&quot;، يمكنك ضبط فترة الاحتفاظ بالبيانات في [AI Studio](https://aistudio.google.com/logs?hl=ar) لوضع علامة تلقائيًا على السجلات ليتم حذفها من مساحة تخزين المشروع بعد 7 أو 14 أو 28 أو 55 يومًا. قد يؤثّر تقليل مدة الاحتفاظ بالبيانات في استرجاع المحادثات السابقة.

يمكنك حذف التفاعلات المخزّنة في أي وقت باستخدام طريقة [`delete`](https://ai.google.dev/api/interactions-api?hl=ar#deleteInteraction) آليًا، والتي تتطلّب معرّف التفاعل. يمكنك أيضًا عرض سجلّات التفاعلات المخزّنة وإدارتها، بما في ذلك حذفها من مساحة تخزين المشروع، في [AI Studio](https://aistudio.google.com/logs?hl=ar).

وبعد انتهاء صلاحية فترة التخزين، سيتم حذف بياناتك تلقائيًا.

تتم معالجة عناصر التفاعل وفقًا [للبنود](https://ai.google.dev/gemini-api/terms?hl=ar).

### عرض التفاعلات في AI Studio

تخزّن واجهة برمجة التطبيقات طلبات Interactions API التي تم تنفيذها باستخدام `store=true` للمشاريع في "الفئة المدفوعة". يمكنك الاطّلاع عليها مباشرةً من
[صفحة "السجلات" في Google AI Studio](https://ai.google.dev/gemini-api/docs/www.aistudio.google.com/logs?hl=ar). اطّلِع على [دليل السجلات](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ar) لمزيد من المعلومات.

## أفضل الممارسات

- **معدل نتائج ذاكرة التخزين المؤقت**: يتم دعم التخزين المؤقت الضمني في الوضعَين الذي يتضمّن حالة والذي لا يتضمّن حالة (راجِع [البدء السريع](https://ai.google.dev/gemini-api/docs/get-started?hl=ar#4_multi-turn_conversations)). يتيح استخدام
  `previous_interaction_id` (مع الاحتفاظ بالحالة) لمواصلة المحادثات للنظام الاستفادة بسهولة أكبر من التخزين المؤقت الضمني لسجلّ المحادثات، ما يحسّن الأداء ويقلّل التكاليف.
- **مزج التفاعلات**: يمكنك مزج التفاعلات بين الوكيل والنموذج ومطابقتها ضمن محادثة واحدة. على سبيل المثال، يمكنك استخدام وكيل متخصص، مثل وكيل &quot;البحث المعمّق&quot;، لجمع البيانات الأولية، ثم استخدام نموذج Gemini عادي لتنفيذ مهام المتابعة، مثل التلخيص أو إعادة التنسيق، وربط هذه الخطوات باستخدام `previous_interaction_id`.

## النماذج والوكلاء المتوافقون

| اسم النموذج | النوع | رقم تعريف الطراز |
| --- | --- | --- |
| Gemini 3.5 Flash | الطراز | `gemini-3.5-flash` |
| معاينة Gemini 3.1 Pro | الطراز | `gemini-3.1-pro-preview` |
| Gemini 3.1 Flash-Lite | الطراز | `gemini-3.1-flash-lite` |
| معاينة Gemini 3 Flash | الطراز | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | الطراز | `gemini-2.5-pro` |
| Gemini 2.5 Flash | الطراز | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | الطراز | `gemini-2.5-flash-lite` |
| صورة Gemini 3 Pro | الطراز | `gemini-3-pro-image` |
| صورة Gemini 3.1 Flash | الطراز | `gemini-3.1-flash-image` |
| معاينة ميزة "تحويل النص إلى كلام" في Gemini 3.1 Flash | الطراز | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | الطراز | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | الطراز | `gemma-4-26b-a4b-it` |
| معاينة مقطع Lyria 3 | الطراز | `lyria-3-clip-preview` |
| معاينة Lyria 3 Pro | الطراز | `lyria-3-pro-preview` |
| معاينة Deep Research | الوكيل | `deep-research-preview-04-2026` |
| معاينة Deep Research | الوكيل | `deep-research-max-preview-04-2026` |
| معاينة Antigravity | الوكيل | `antigravity-preview-05-2026` |

## حزم SDK

يمكنك استخدام أحدث إصدار من حِزم تطوير البرامج (SDK) من Google GenAI للوصول إلى واجهة برمجة التطبيقات Interactions API.

- في Python، هذه هي حزمة `google-genai` من الإصدار `2.3.0` فصاعدًا.
- في JavaScript، هذه هي حزمة `@google/genai` من الإصدار `2.3.0` والإصدارات الأحدث.

يمكنك الاطّلاع على مزيد من المعلومات حول كيفية تثبيت حِزم SDK على صفحة [المكتبات](https://ai.google.dev/gemini-api/docs/libraries?hl=ar).

## القيود

- **بروتوكول سياق النموذج (MCP) عن بُعد**: لا يتوافق Gemini 3 مع بروتوكول سياق النموذج (MCP) عن بُعد، وسيتوفّر قريبًا.
- **توافق النماذج المتعددة الأدوار**: عند استخدام نماذج مختلفة في محادثة (سواء كانت تتضمّن حالة أو لا تتضمّن حالة)، يجب أن تتوافق النماذج اللاحقة مع أساليب الإخراج الخاصة بالنماذج السابقة كمدخلات. على سبيل المثال، إذا أنشأت صورة باستخدام `gemini-3.1-flash-image`، لا يمكنك مواصلة المحادثة مع نموذج لا يقبل إدخالات الصور (مثل نموذج نصي فقط أو نموذج لإنشاء الموسيقى مثل Lyria).

تتوافق الميزات التالية مع واجهة
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ar) API، ولكنها **غير متاحة بعد** في Interactions API:

- **[البيانات الوصفية للفيديو](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar)**: الحقل `video_metadata`، ويُستخدم لضبط فواصل الاقتطاع ومعدّلات اللقطات المخصّصة لفهم الفيديو.
- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar)**
- **[استدعاء الدوال تلقائيًا (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=ar#automatic_function_calling_python_only)**
- **[التخزين المؤقت الصريح](https://ai.google.dev/gemini-api/docs/caching?hl=ar)**: يُرجى العِلم أنّ التخزين المؤقت الضمني من جهة الخادم متاح في Interactions API
  من خلال `previous_interaction_id`.
- **[إعدادات الأمان](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ar)**: لا تتوافق إعدادات الأمان المخصّصة مع Interactions API.

## الملاحظات

تُعدّ ملاحظاتك مهمة جدًا لتطوير Interactions API.
يمكنك مشاركة أفكارك أو الإبلاغ عن أخطاء أو طلب ميزات في [منتدى مطوّري الذكاء الاصطناعي من Google](https://discuss.ai.google.dev/c/gemini-api/4?hl=ar).

## الخطوات التالية

- جرِّب [دفتر ملاحظات التشغيل السريع لواجهة Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=ar).
- [مزيد من المعلومات حول "وكيل Deep Research" في Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-16 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-16 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
