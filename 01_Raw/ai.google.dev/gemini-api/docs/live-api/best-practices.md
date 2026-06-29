---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=ar
fetched_at: 2026-06-29T05:33:07.914598+00:00
title: "\u0623\u0641\u0636\u0644 \u0627\u0644\u0645\u0645\u0627\u0631\u0633\u0627\u062a \u0627\u0644\u0645\u062a\u0639\u0644\u0651\u0642\u0629 \u0628\u0648\u0627\u062c\u0647\u0629 Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# أفضل الممارسات المتعلّقة بواجهة Live API

يتناول هذا الدليل أفضل الممارسات التي يمكنك اتّباعها لتحسين استخدامك لواجهة برمجة التطبيقات Live API.
للحصول على نظرة عامة ورمز نموذجي لحالات الاستخدام الشائعة، يُرجى الاطّلاع على صفحة [البدء في استخدام Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar).

## تصميم تعليمات واضحة للنظام

للحصول على أفضل أداء من Live API، ننصحك بوضع مجموعة محدّدة بوضوح من تعليمات النظام (SI) التي تحدّد شخصية الوكيل وقواعد المحادثة والضوابط، بهذا الترتيب.

للحصول على أفضل النتائج، افصل كل وكيل في تعليمات نظام مميزة.

1. **تحديد شخصية الوكيل:** قدِّم تفاصيل حول اسم الوكيل ودوره وأي خصائص مفضّلة. إذا أردت تحديد اللهجة، احرص أيضًا على تحديد لغة الإخراج المفضّلة (مثل اللهجة البريطانية للمتحدث باللغة الإنجليزية).
2. **تحديد قواعد المحادثة:** ضَع هذه القواعد بالترتيب الذي تتوقّع أن يتّبعه النموذج. ميِّز بين العناصر التي تظهر مرة واحدة في المحادثة والحلقات الحوارية. على سبيل المثال:

   - **العنصر الذي يظهر مرة واحدة:** اجمع تفاصيل العميل مرة واحدة (مثل الاسم والموقع الجغرافي ورقم بطاقة برنامج الولاء).
   - **الحلقة الحوارية:** يمكن للمستخدم مناقشة الاقتراحات والأسعار وعمليات الإرجاع والتسليم، وقد يرغب في الانتقال من موضوع إلى آخر. أخبِر النموذج أنّه لا بأس من المشاركة في هذه الحلقة الحوارية طالما أراد المستخدم ذلك.
3. **تحديد طلبات الأدوات ضِمن سير العمل في جمل منفصلة:** على سبيل المثال، إذا كانت خطوة جمع تفاصيل العميل مرة واحدة تتطلّب استدعاء دالة `get_user_info`، يمكنك قول: *خطوتك الأولى هي جمع معلومات المستخدم. اطلب أولاً من المستخدم تقديم اسمه وموقعه الجغرافي ورقم بطاقة برنامج الولاء. بعد ذلك،
   استدعِ `get_user_info` باستخدام هذه التفاصيل.*
4. ***إضافة أي ضوابط ضرورية:** قدِّم أي ضوابط عامة للمحادثة
   لا تريد أن يتّبعها النموذج. يمكنك تقديم أمثلة محدّدة على ما تريد أن يفعله النموذج إذا حدث *x*.* إذا كنت لا تزال لا تحصل على المستوى المفضّل من الدقة، استخدِم الكلمة *بشكل لا لبس فيه* لتوجيه النموذج إلى أن يكون دقيقًا.

## تحديد الأدوات بدقة

عند استخدام الأدوات مع Live API، كن محدّدًا في تعريفات الأدوات.
احرص على إخبار Gemini بالشروط التي يجب بموجبها استدعاء طلب الأداة. لمزيد من التفاصيل، يُرجى الاطّلاع على [تعريفات الأدوات](#tool-definitions-example) في
قسم المثال.

## صياغة طلبات فعّالة

- **استخدام طلبات واضحة:** قدِّم أمثلة على ما يجب وما لا يجب أن تفعله النماذج في الطلبات، وحاول حصر الطلبات في طلب واحد لكل شخصية أو دور في كل مرة. بدلاً من الطلبات الطويلة المتعدّدة الصفحات، ننصحك باستخدام تسلسل الطلبات بدلاً من ذلك. يحقّق النموذج أفضل أداء في المهام التي تتضمّن استدعاءات دالة واحدة.
- **تقديم أوامر ومعلومات البدء:** تتوقّع Live API بيانات أدخلها المستخدم قبل الردّ. لجعل Live API تبدأ المحادثة، ضَمِّن طلبًا يطلب منها تحية المستخدم أو بدء المحادثة. ضَمِّن معلومات عن المستخدم لجعل Live API تخصّص هذه التحية.

## تحديد اللغة

للحصول على أفضل أداء على `gemini-live-2.5-flash` المتسلسلة في Live API، تأكَّد من أنّ `language_code` في واجهة برمجة التطبيقات تطابق اللغة التي يتحدث بها المستخدم.

إذا كنت تتوقّع أن يردّ النموذج بلغة غير الإنجليزية، ضَمِّن ما يلي كجزء من تعليمات النظام:

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## البث

عند تنفيذ الصوت في الوقت الفعلي، اتّبِع أفضل الممارسات التالية:

- **حجم الجزء ووقت الاستجابة**: أرسِل الصوت في أجزاء تتراوح مدتها بين 20 ملي ثانية و40 ملي ثانية.
- **التعامل مع الانقطاع**: عندما يتحدث المستخدم أثناء ردّ النموذج،
  يرسل الخادم رسالة `server_content` تتضمّن `"interrupted": true`. عليك التخلّص فورًا من المخزن المؤقت للصوت من جهة العميل لمنع الوكيل من مواصلة التحدث أثناء حديث المستخدم.

## إدارة السياق

استخدِم `ContextWindowCompressionConfig` للجلسات الطويلة، لأنّ الرموز المميّزة الصوتية الأصلية تتراكم بسرعة (حوالي 25 رمزًا مميزًا لكل ثانية من الصوت).

## التخزين المؤقت من جهة العميل

لا تخزِّن الصوت المُدخَل مؤقتًا بشكل كبير (مثل ثانية واحدة) قبل الإرسال. أرسِل أجزاء صغيرة (من 20 ملي ثانية إلى 100 ملي ثانية) لتقليل وقت الاستجابة.

## إعادة أخذ العيّنات

تأكَّد من أنّ تطبيق العميل يعيد أخذ عيّنات من إدخال الميكروفون (غالبًا 44.1 كيلوهرتز أو 48 كيلوهرتز) إلى 16 كيلوهرتز قبل الإرسال.

## إدارة الجلسة

اتّبِع هذه الإرشادات للتعامل مع مراحل نشاط الجلسة وضمان تجربة مستخدم موثوقة:

- **تفعيل ضغط قدرة استيعاب السياق:** تتراكم الرموز المميّزة الصوتية بمعدّل 25 رمزًا مميزًا في الثانية تقريبًا. بدون الضغط، تقتصر الجلسات الصوتية فقط على 15 دقيقة والجلسات الصوتية والمرئية على دقيقتَين. فعِّل
  [ضغط قدرة استيعاب السياق](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ar#context-window-compression)
  لتمديد الجلسات إلى مدة غير محدودة.
- **تنفيذ استئناف الجلسة:** قد يعيد الخادم بشكل دوري ضبط اتصال WebSocket. استخدِم
  [ميزة استئناف الجلسة](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ar#session-resumption)
  لإعادة الاتصال بسلاسة بدون فقدان السياق. احتفِظ بأحدث رمز مميز للاستئناف من رسائل `SessionResumptionUpdate` ومرِّره كمقبض عند إعادة الاتصال. تكون الرموز المميّزة للاستئناف صالحة لمدة ساعتين بعد انتهاء الجلسة الأخيرة.
- **التعامل مع رسائل GoAway:** يرسل الخادم رسالة
  [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ar#goaway-message) قبل إنهاء الاتصال. استمِع إلى هذه الرسالة واستخدِم الحقل `timeLeft` لإنهاء المحادثة بسلاسة أو إعادة الاتصال قبل إغلاق الاتصال.
- **التعامل مع إشارات `generationComplete`:** استخدِم الرسالة
  [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ar#generation-complete-message)
  لمعرفة متى ينتهي النموذج من إنشاء ردّ، حتى يتمكّن تطبيقك
  من تعديل واجهة المستخدم أو المتابعة إلى الإجراء التالي.

لمعرفة تفاصيل التنفيذ، يُرجى الاطّلاع على
[إدارة الجلسة](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ar).

## أمثلة

يجمع هذا المثال بين أفضل الممارسات و
[الإرشادات لتصميم تعليمات النظام](#system-instruction-guidelines) من أجل
توجيه أداء النموذج كمدرب مهني.

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

يحدّد ملف JSON هذا الدوال ذات الصلة التي يتم استدعاؤها في مثال المدرب المهني.
للحصول على أفضل النتائج عند تحديد الدوال، ضَمِّن أسماءها وأوصافها ومَعلماتها وشروط استدعائها.

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

## التسعير والفوترة

تتم فوترة Gemini Live API بشكل صارم حسب استخدام الرموز المميّزة. بما أنّ Live API تحافظ على جلسة WebSocket مستمرة، تتّبع الفوترة نموذجًا مركّبًا استنادًا إلى قدرة الاستيعاب النشطة.

### قدرة استيعاب سياق الجلسة (التكاليف المركّبة)

تفرض عليك واجهة برمجة التطبيقات رسومًا لكل دورة على جميع الرموز المميّزة المعروضة في نافذة سياق الجلسة. يُعرَّف "الدور" على أنّه بيانات أدخلها المستخدم والردّ المقابل من النموذج.

- **التراكم:** تتضمّن نافذة السياق الرموز المميّزة الجديدة من الدور الحالي بالإضافة إلى جميع الرموز المميّزة المتراكمة من الأدوار السابقة.
- **إعادة الفوترة:** تتم إعادة معالجة الرموز المميّزة السابقة ويتم تدوين سجلات استخدامها في كل دورة جديدة، بما يصل إلى قدرة استيعاب التي تم ضبطها. كلما طالت الجلسة، زادت التكلفة لكل دورة لأنّه تتم إعادة معالجة سجلّ المحادثات.

### الرموز المميّزة الصوتية والنصوص المحوَّلة من مقاطع صوتية

تتسم Live API بأنّها متعدّدة الوسائط بشكل أساسي. تحتفظ بسجلّ المحادثات كرموز مميّزة صوتية أولية للحفاظ على الفروق الدقيقة في الصوت والنبرة.

- **الفوترة الصوتية:** تفرض عليك واجهة برمجة التطبيقات رسومًا على الرموز المميّزة الصوتية الأصلية المتراكمة بالمعدّل العادي لإدخال الصوت في كل دورة.
- **الرسوم الإضافية للنص المحوَّل من مقطع صوتي:** عند تفعيل ميزة تحويل الصوت إلى نص (`inputAudioTranscription` أو `outputAudioTranscription`)، تفرض واجهة برمجة التطبيقات رسومًا على جميع الرموز المميّزة النصية التي تم إنشاؤها للنص المحوَّل من مقطع صوتي بالمعدّل العادي لإخراج الرموز المميّزة النصية بالإضافة إلى التكاليف العادية للرموز المميّزة الصوتية.

### إدارة التكاليف باستخدام حدود السياق

لمنع النمو غير المحدود للتكلفة في الجلسات الطويلة، اضبط حجم قدرة الاستيعاب باستخدام `contextWindowCompression`.

من خلال ضبط مشغّل الضغط (مثل 25,000 رمز مميز) ونافذة منزلقة (مثل 8,000 رمز مميز)، تزيل واجهة برمجة التطبيقات تلقائيًا الرموز المميّزة الأقدم بمجرد الوصول إلى الحدّ الأقصى. بعد ذلك، لا تفرض واجهة برمجة التطبيقات رسومًا على الأدوار اللاحقة إلا على السجلّ المحتفظ به بالإضافة إلى أي رموز مميّزة جديدة.

### وضع الصوت فقط الاستباقي

عند تفعيل "وضع الصوت الاستباقي"، يتم تحصيل رسوم من الرموز المميّزة المُدخَلة طوال فترة استماع Live API، بينما لا يتم تحصيل رسوم من الرموز المميّزة الناتجة إلا عندما تردّ واجهة برمجة التطبيقات.

- **ملاحظة بشأن Gemini 3.1:** لا يتوفّر "وضع الصوت الاستباقي" في `gemini-3.1-flash-live-preview`. بالنسبة إلى هذا النموذج، لا يتم تحصيل رسوم منك مقابل الصوت إلا عند البث النشط للإدخال.

للحصول على معلومات مفصّلة عن الأسعار، يُرجى الاطّلاع على صفحة أسعار [Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-01 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-01 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
