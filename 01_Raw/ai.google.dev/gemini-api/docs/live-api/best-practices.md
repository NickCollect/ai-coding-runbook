---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=ar
fetched_at: 2026-05-05T19:50:03.127039+00:00
title: "Live API best practices \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# Live API best practices

يتناول هذا الدليل أفضل الممارسات التي يمكنك اتّباعها لتحسين استخدامك لواجهة Live API.
يمكنك الاطّلاع على صفحة [البدء باستخدام Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar) للحصول على نظرة عامة ورمز نموذجي لحالات الاستخدام الشائعة.

## تصميم تعليمات نظام واضحة

للحصول على أفضل أداء من Live API، ننصحك بتحديد مجموعة واضحة من تعليمات النظام (SI) التي تحدّد شخصية الوكيل وقواعد المحادثة وضوابط الأمان، بهذا الترتيب.

للحصول على أفضل النتائج، قسِّم كل وكيل إلى نظام فرعي مميّز.

1. **تحديد شخصية الوكيل:** قدِّم تفاصيل حول اسم الوكيل ودوره وأي خصائص مفضّلة. إذا أردت تحديد اللهجة، احرص على تحديد لغة الإخراج المفضّلة أيضًا (مثل اللهجة البريطانية لشخص يتحدث الإنجليزية).
2. **تحديد قواعد المحادثة:** ضَع هذه القواعد بالترتيب الذي تتوقّع أن يتبعه النموذج. حدِّد الفرق بين العناصر التي تظهر لمرة واحدة في المحادثة وحلقات المحادثة. على سبيل المثال:

   - **العنصر لمرة واحدة:** جمع تفاصيل العميل مرة واحدة (مثل الاسم أو الموقع الجغرافي أو رقم بطاقة الولاء)
   - **حلقة المحادثة:** يمكن للمستخدم مناقشة الاقتراحات والأسعار وعمليات الإرجاع والتسليم، وقد يرغب في الانتقال من موضوع إلى آخر. أخبِر النموذج بأنّه لا بأس من المشاركة في هذه الحلقة الحوارية طالما أراد المستخدم ذلك.
3. **تحديد استدعاءات الأدوات ضمن تدفق في جمل منفصلة:** على سبيل المثال، إذا كانت خطوة واحدة لمرة واحدة لجمع تفاصيل العميل تتطلّب استدعاء دالة `get_user_info`، يمكنك القول: *خطوتك الأولى هي جمع معلومات المستخدم. في البداية،
   اطلب من المستخدم تقديم اسمه وموقعه الجغرافي ورقم بطاقة الولاء. بعد ذلك، استدعِ الدالة `get_user_info` باستخدام هذه التفاصيل.*
4. **إضافة أي ضوابط ضرورية:** قدِّم أي ضوابط عامة للمحادثات لا تريد أن يلتزم بها النموذج. يمكنك تقديم أمثلة محددة، مثل إذا حدث *س*، عليك أن تطلب من النموذج تنفيذ *ص*. إذا لم تحصل على مستوى الدقة المطلوب، استخدِم الكلمة *بشكل لا لبس فيه* لتوجيه النموذج إلى أن يكون دقيقًا.

## تحديد الأدوات بدقة

عند استخدام أدوات مع Live API، يجب أن تكون دقيقًا في تعريفات الأدوات.
احرص على إخبار Gemini بالشروط التي يجب استيفاؤها لتنفيذ استدعاء أداة. لمزيد من التفاصيل، راجِع [تعريفات الأدوات](#tool-definitions-example) في قسم الأمثلة.

## صياغة طلبات فعّالة

- **استخدام طلبات واضحة:** قدِّم أمثلة على ما يجب وما لا يجب أن تفعله النماذج في الطلبات، وحاوِل أن تقتصر الطلبات على طلب واحد لكل شخصية أو دور في كل مرة. بدلاً من الطلبات الطويلة التي تتضمّن صفحات متعددة، ننصحك باستخدام تسلسل الطلبات. يعمل النموذج على أفضل نحو في المهام التي تتضمّن استدعاءات دالة واحدة.
- **تقديم أوامر ومعلومات بدء:** تتوقّع واجهة برمجة التطبيقات Live API أن يقدّم المستخدم بيانات أدخلها المستخدم قبل أن تستجيب. لجعل Live API يبدأ المحادثة، أدرِج طلبًا يطلب منه الترحيب بالمستخدم أو بدء المحادثة. تضمين معلومات عن المستخدم لتخصيص التحية في Live API

## تحديد اللغة

لتحقيق الأداء الأمثل على واجهة برمجة التطبيقات المتسلسلة `gemini-live-2.5-flash`،
تأكَّد من أنّ `language_code` لواجهة برمجة التطبيقات يتطابق مع اللغة التي يتحدث بها المستخدم.

إذا كان المطلوب من النموذج الرد بلغة غير الإنجليزية،
يُرجى تضمين ما يلي كجزء من تعليمات النظام:

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## البث

عند تنفيذ ميزة "الصوت في الوقت الفعلي"، اتّبِع أفضل الممارسات التالية:

- **حجم الأجزاء ووقت الاستجابة**: أرسِل الصوت في أجزاء تتراوح مدتها بين 20 و40 ملي ثانية.
- **التعامل مع المقاطعات**: عندما يتحدث المستخدم أثناء ردّ النموذج، يرسل الخادم رسالة `server_content` تتضمّن `"interrupted": true`. عليك التخلص من مخزن الصوت المؤقت من جهة العميل على الفور لمنع الوكيل من مواصلة التحدث أثناء حديث المستخدم.

## إدارة السياق

استخدِم `ContextWindowCompressionConfig` للجلسات الطويلة، لأنّ الرموز المميزة الأصلية للصوت تتراكم بسرعة (حوالي 25 رمزًا مميزًا لكل ثانية من الصوت).

## التخزين المؤقت من جهة العميل

لا تخزِّن الصوت المُدخَل مؤقتًا بشكل كبير (مثل ثانية واحدة) قبل إرساله. إرسال أجزاء صغيرة (من 20 إلى 100 ملي ثانية) لتقليل وقت الاستجابة

## إعادة أخذ العيّنات

تأكَّد من أنّ تطبيق العميل يعيد أخذ عيّنات من إدخال الميكروفون (غالبًا 44.1 كيلو هرتز أو 48 كيلو هرتز) إلى 16 كيلو هرتز قبل الإرسال.

## إدارة الجلسة

اتّبِع الإرشادات التالية للتعامل مع دورة حياة الجلسة وضمان تقديم تجربة موثوقة للمستخدم:

- **تفعيل ميزة ضغط قدرة الاستيعاب:** تتراكم الرموز المميزة الصوتية بمعدل 25 رمزًا مميزًا في الثانية تقريبًا. بدون ضغط، تقتصر الجلسات الصوتية فقط على 15 دقيقة وجلسات الصوت والفيديو على دقيقتَين. فعِّل
  [ضغط قدرة الاستيعاب](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ar#context-window-compression)
  لتمديد الجلسات إلى مدة غير محدودة.
- **تنفيذ استئناف الجلسة:** قد يعيد الخادم ضبط اتصال WebSocket بشكل دوري. استخدِم ميزة
  [استئناف الجلسة](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ar#session-resumption)
  لإعادة الاتصال بسلاسة بدون فقدان السياق. الاحتفاظ بآخر رمز مميز لاستئناف المحادثة من `SessionResumptionUpdate` رسالة وتمريره كمؤشر عند إعادة الاتصال تكون رموز الإيقاف المؤقت صالحة لمدة ساعتين بعد انتهاء آخر جلسة.
- **التعامل مع رسائل GoAway:** يرسل الخادم رسالة [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ar#goaway-message) قبل إنهاء الاتصال. استمع إلى هذه الرسالة واستخدِم الحقل
  `timeLeft` لإنهاء الاتصال أو إعادة الاتصال بشكل سليم قبل إغلاق الاتصال.
- **التعامل مع إشارات generationComplete:** استخدِم رسالة
  [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ar#generation-complete-message)
  لمعرفة الوقت الذي ينتهي فيه النموذج من إنشاء ردّ، كي يتمكّن تطبيقك من تعديل واجهة المستخدم أو المتابعة إلى الإجراء التالي.

للحصول على تفاصيل التنفيذ، راجِع [إدارة الجلسات](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ar).

## أمثلة

يجمع هذا المثال بين أفضل الممارسات و[إرشادات تصميم تعليمات النظام](#system-instruction-guidelines) لتوجيه أداء النموذج بصفته مستشارًا مهنيًا.

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### تعريفات الأدوات

يحدد ملف JSON هذا الدوال ذات الصلة التي تم استدعاؤها في مثال "المستشار المهني".
للحصول على أفضل النتائج عند تحديد الدوال، يجب تضمين أسمائها وأوصافها ومَعلماتها وشروط استدعائها.

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
