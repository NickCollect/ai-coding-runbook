---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ar
fetched_at: 2026-07-06T05:16:28.895420+00:00
title: "\u0627\u0633\u062a\u0631\u0627\u062a\u064a\u062c\u064a\u0627\u062a \u0627\u0644\u062a\u0635\u0645\u064a\u0645 \u0627\u0644\u0641\u0648\u0631\u064a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# استراتيجيات التصميم الفوري

*تصميم الطلبات* هو عملية إنشاء طلبات أو طلبات بلغة طبيعية تؤدي إلى إنتاج ردود دقيقة وعالية الجودة من نموذج لغوي.

تقدّم هذه الصفحة المفاهيم الأساسية والاستراتيجيات وأفضل الممارسات لمساعدتك في البدء بتصميم الطلبات للاستفادة إلى أقصى حدّ من نماذج الذكاء الاصطناعي من Gemini.

## أدلة كتابة الطلبات المتعلقة بموضوع معيّن

هل تبحث عن استراتيجيات أكثر تحديدًا لإنشاء الطلبات؟ يمكنك الاطّلاع على أدلة كتابة الطلبات الأخرى
على:

- [تقديم الطلبات باستخدام ملفات الوسائط](https://ai.google.dev/gemini-api/docs/files?hl=ar#prompt-guide)
- تقديم طلبات لإنشاء الصور باستخدام [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=ar#imagen-prompt-guide) و[ميزة إنشاء الصور الأصلية في Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar#prompt-guide)
- [تقديم طلب لإنشاء فيديو](https://ai.google.dev/gemini-api/docs/video?hl=ar#prompt-guide)

يمكنك العثور على نماذج أخرى من الطلبات في [معرض الطلبات](https://ai.google.dev/gemini-api/prompts?hl=ar)
المخصّص لعرض العديد من المفاهيم الواردة في هذا الدليل بشكل تفاعلي.

## تعليمات واضحة ومحدّدة

تتمثّل إحدى الطرق الفعّالة والمجدية لتخصيص سلوك النموذج في تزويده بتعليمات واضحة ومحدّدة، ويمكن أن تكون التعليمات على شكل سؤال أو مهام مفصّلة أو معقّدة مثل تحديد تجربة المستخدم وطريقة تفكيره.

### الإدخال

الإدخال هو النص المطلوب في الطلب الذي تريد أن يقدّم النموذج ردًا عليه. يمكن أن تكون المدخلات سؤالاً يجيب عنه النموذج (مدخلات السؤال)، أو مهمة ينفّذها النموذج (مدخلات المهمة)، أو كيانًا يعمل عليه النموذج (مدخلات الكيان)، أو مدخلات جزئية يكملها النموذج أو يتابعها (مدخلات الإكمال).

| **نوع الإدخال** | **الطلب** | **المخرجات المولَّدة** |
| --- | --- | --- |
| السؤال | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| المهمة | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| الكيان | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### إكمال الإدخال جزئيًا

تعمل نماذج اللغة التوليدية مثل أداة متقدّمة للإكمال التلقائي. فعندما تقدّم محتوًى جزئيًا، يمكن للنموذج تقديم بقية المحتوى أو ما يعتقد أنّه استمرار لهذا المحتوى كردّ. وعندما يفعل ذلك، إذا تضمّن المحتوى أي أمثلة أو سياق، يمكن للنموذج أخذ هذه الأمثلة أو السياق في الاعتبار.

يقدّم المثال التالي طلبًا يتضمّن تعليمات ومدخلات كيان:

|  |
| --- |
| **الطلب:**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **الردّ:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

مع أنّ النموذج نفّذ ما طُلب منه، إلا أنّ كتابة التعليمات باللغة الطبيعية قد تكون صعبة في بعض الأحيان، كما أنّها تترك الكثير من الخيارات لتفسير النموذج.
على سبيل المثال، قد تحتوي قائمة طعام أحد المطاعم على العديد من الأطباق. لتقليل حجم ردّ JSON، من المحتمل أنّك تريد حذف العناصر التي لم يتم طلبها. في هذه الحالة، يمكنك تقديم مثال وبادئة ردّ والسماح للنموذج بإكمالها:

|  |
| --- |
| **الطلب:**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **الردّ:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

لاحظ كيف تم استبعاد "تشيز برجر" من الناتج لأنّه لم يكن جزءًا من الطلب.

على الرغم من أنّه يمكنك تحديد تنسيق كائنات ردود JSON البسيطة باستخدام الطلبات، ننصحك باستخدام ميزة [الإخراج المنظَّم](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar) في Gemini API عند تحديد مخطط JSON أكثر تعقيدًا للرد.

### القيود

حدِّد أي قيود على قراءة الطلب أو إنشاء ردّ، فيمكنك أن تطلب من النموذج تنفيذ إجراءات معيّنة أو عدم تنفيذها. على سبيل المثال، يمكنك تحديد قيد في الطلب بشأن المدة التي تريد أن يستغرقها التلخيص:

|  |
| --- |
| **الطلب:**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **الردّ:**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### تنسيق الردّ

يمكنك تقديم تعليمات تحدّد تنسيق الردّ، مثلاً، يمكنك طلب أن يكون الردّ منسّقًا كجدول أو قائمة نقطية أو عرض موجز أو كلمات رئيسية أو جملة أو فقرة. توجّه تعليمات النظام التالية النموذج لتقديم ردّ أكثر حوارية:

|  |
| --- |
| **تعليمات النظام**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **الطلب**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **الردّ:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### تنسيق الردود باستخدام استراتيجية الإكمال

يمكن أن تساعد [استراتيجية الإكمال](#completion) أيضًا في تنسيق الردّ.
يطلب المثال التالي من النموذج إنشاء مخطط لمقال:

|  |
| --- |
| **الطلب:**    ``` Create an outline for an essay about hummingbirds. ```  **الردّ:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

لم يحدّد الطلب شكل المخطط التفصيلي، فاختار النموذج شكلاً مناسبًا لك. للحصول على مخطط تفصيلي بالشكل الذي تريده، يمكنك إضافة نص يمثّل بداية المخطط التفصيلي والسماح للنموذج بإكماله استنادًا إلى النمط الذي بدأته.

|  |
| --- |
| **الطلب:**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **الردّ:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## الطلبات بلا أمثلة مقابل الطلبات ببضعة أمثلة

يمكنك تضمين أمثلة في الطلب توضّح للنموذج الشكل الصحيح للردّ. يحاول النموذج تحديد الأنماط والعلاقات من الأمثلة وتطبيقها عند إنشاء ردّ. تُعرف الطلبات التي تحتوي على بعض الأمثلة باسم طلبات *التعلم من أمثلة قليلة*، بينما تُعرف الطلبات التي لا تقدّم أي أمثلة باسم طلبات *التعلم بدون أمثلة*. غالبًا ما تُستخدَم طلبات التعلم من أمثلة قليلة لتنظيم التنسيق أو الصياغة أو النطاق أو الأنماط العامة لردود النموذج. استخدِم أمثلة محدّدة ومتنوعة لمساعدة النموذج في تضييق نطاق تركيزه وإنشاء نتائج أكثر دقة.

ننصحك دائمًا بتضمين أمثلة قليلة في طلباتك، لأنّ الطلبات التي لا تتضمّن أمثلة قليلة من المرجّح أن تكون أقل فعالية. في الواقع، يمكنك إزالة التعليمات من طلبك إذا كانت الأمثلة واضحة بما يكفي في عرض المهمة المطلوبة.

يطلب طلب zero-shot التالي من النموذج اختيار أفضل شرح.

|  |
| --- |
| **الطلب:**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **الردّ:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

إذا كانت حالة الاستخدام تتطلّب أن يقدّم النموذج ردودًا موجزة، يمكنك تضمين أمثلة في الطلب تعطي الأولوية للردود الموجزة.

يقدّم الطلب التالي مثالَين يوضّحان تفضيل التفسيرات الأقصر. في الردّ، يمكنك ملاحظة أنّ الأمثلة ساعدت النموذج في اختيار التفسير الأقصر (`Explanation2`) بدلاً من التفسير الأطول (`Explanation1`) كما فعل سابقًا.

|  |
| --- |
| **الطلب:**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **الردّ:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### العدد الأمثل للأمثلة

يمكن للنماذج، مثل Gemini، غالبًا رصد الأنماط باستخدام بعض الأمثلة، ولكن قد تحتاج إلى تجربة عدد الأمثلة التي يجب تقديمها في الطلب للحصول على أفضل النتائج. في الوقت نفسه، إذا تضمّن الطلب عددًا كبيرًا جدًا من الأمثلة، قد يبدأ النموذج في [المبالغة في مطابقة](https://developers.google.com/machine-learning/glossary?hl=ar#overfitting) الردّ مع الأمثلة.

### اعتماد تنسيق موحَّد

احرص على أن يكون تنسيق الأمثلة القليلة متشابهًا لتجنُّب الردود بتنسيقات غير مرغوب فيها. أحد الأهداف الأساسية لإضافة أمثلة قليلة في الطلبات هو عرض تنسيق الردّ على النموذج، لذا من الضروري التأكّد من اتّساق التنسيق في جميع الأمثلة، مع الانتباه بشكل خاص إلى علامات XML والمسافات البيضاء وأسطر جديدة وعوامل تقسيم الأمثلة.

## إضافة سياق

يمكنك تضمين تعليمات ومعلومات في طلب يحتاج النموذج إلى
حلّ مشكلة، بدلاً من افتراض أنّ النموذج يتضمّن كل المعلومات
المطلوبة. تساعد هذه المعلومات السياقية النموذج في فهم القيود والتفاصيل المتعلقة بما تطلبه منه.

يطلب المثال التالي من النموذج تقديم إرشادات لتحديد المشاكل في جهاز توجيه وحلّها:

|  |
| --- |
| **الطلب:**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **الردّ:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

يبدو أنّ الرد يتضمّن معلومات عامة لتحديد المشاكل وحلّها، وهي غير مرتبطة بجهاز التوجيه أو حالة أضواء مؤشر LED.

لتخصيص الردّ لجهاز التوجيه المحدّد، يمكنك إضافة دليل تحديد المشاكل وحلّها الخاص بجهاز التوجيه إلى الطلب كمرجع يمكن للنموذج الرجوع إليه عند تقديم الردّ.

|  |
| --- |
| **الطلب:**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **الردّ:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## تقسيم الطلبات إلى مكوّنات

بالنسبة إلى حالات الاستخدام التي تتطلّب طلبات معقّدة، يمكنك مساعدة النموذج في التعامل مع هذا التعقيد من خلال تقسيم الطلبات إلى مكوّنات أبسط.

1. **تقسيم التعليمات:** بدلاً من تضمين العديد من التعليمات في طلب واحد، أنشئ طلبًا واحدًا لكل تعليمات. يمكنك اختيار الطلب الذي تريد معالجته استنادًا إلى إدخال المستخدم.
2. **تسلسل الطلبات:** بالنسبة إلى المهام المعقّدة التي تتضمّن خطوات متعدّدة متسلسلة،
   اجعل كل خطوة طلبًا، واربط الطلبات معًا في تسلسل،
   بحيث يصبح الناتج من أحد الطلبات في التسلسل هو
   مدخل الطلب التالي، ويكون الناتج من الطلب الأخير في التسلسل
   هو الناتج النهائي.
3. **تجميع الردود:** يحدث التجميع عندما تريد تنفيذ مهام متوازية مختلفة على أجزاء مختلفة من البيانات وتجميع النتائج لإنتاج الناتج النهائي. على سبيل المثال، يمكنك أن تطلب من النموذج تنفيذ عملية واحدة على الجزء الأول من البيانات، وتنفيذ عملية أخرى على بقية البيانات، ثم تجميع النتائج.

## تجربة مَعلمات النموذج

يتضمّن كل طلب ترسله إلى أحد النماذج قيم مَعلمات تتحكّم في طريقة إنشاء النموذج للردّ، ويمكن أن ينشئ النموذج نتائج مختلفة لقيم المَعلمات المختلفة. جرِّب قيم مَعلمات مختلفة للحصول على أفضل القيم للمهمة، مع العلم بأنّ المَعلمات المتاحة للنماذج المختلفة قد تختلف، وفي ما يلي المَعلمات الأكثر شيوعًا:

1. **الحدّ الأقصى لعدد الرموز المميزة للناتج:** يحدّد الحدّ الأقصى لعدد الرموز المميزة التي يمكن إنشاؤها في الرد. الرمز المميز هو أربعة أحرف تقريبًا. تتجاوب 100
   رمز مميز مع 60 إلى 80 كلمة تقريبًا.
2. **درجة العشوائية:** تتحكّم درجة العشوائية في مستوى العشوائية في اختيار الرموز المميزة. يتم استخدام درجة العشوائية لأخذ العيّنات أثناء إنشاء رد،
   ويحدث ذلك عند تطبيق `topP` و`topK`. تكون درجات العشوائية المنخفضة مناسبة للطلبات التي تتطلّب ردودًا أكثر حتمية أو أقل انفتاحًا، بينما يمكن أن تؤدي درجات العشوائية المرتفعة إلى نتائج أكثر تنوعًا أو إبداعًا. درجة الحرارة 0 هي درجة حتمية، ما يعني أنّه يتم دائمًا اختيار الردّ ذي الاحتمالية الأعلى.
3. **`topK`:** تغيّر المَعلمة `topK` طريقة اختيار النموذج للرموز المميزة في الناتج. تشير القيمة 1 للمَعلمة `topK` إلى أنّ الرمز المميز المحدّد هو الأكثر احتمالاً بين جميع الرموز المميزة في مفردات النموذج (يُعرف أيضًا باسم فك الترميز الجشع)، بينما تشير القيمة 3 للمَعلمة `topK` إلى أنّه يتم اختيار الرمز المميز التالي من بين 3 رموز مميزة هي الأكثر احتمالاً باستخدام درجة الحرارة. في كل خطوة من خطوات اختيار الرمز المميز، يتم أخذ عيّنات من الرموز المميزة `topK` التي تتضمّن أعلى الاحتمالات. بعد ذلك، يتم فلترة الرموز المميزة بشكل أكبر استنادًا إلى `topP` مع اختيار الرمز المميز النهائي باستخدام أخذ العيّنات من درجة الحرارة.
4. **`topP`:** تغيّر المَعلمة `topP` طريقة اختيار النموذج للرموز المميزة في الناتج. ويتم اختيار الرموز المميزة من الأكثر احتمالاً إلى الأقل احتمالاً إلى أن يساوي مجموع احتمالاتها قيمة `topP`. على سبيل المثال، إذا كان احتمال الرموز المميزة A وB وC هو 0.3 و0.2 و0.1 وكانت قيمة `topP` هي 0.5، سيختار النموذج إما A أو B كرمز مميز تالٍ باستخدام درجة العشوائية ويستبعد C كمرشح. قيمة `topP` التلقائية هي 0.95.
5. **`stop_sequences`:** يمكنك ضبط تسلسل إيقاف لتوجيه النموذج إلى التوقف عن إنشاء المحتوى. يمكن أن يكون تسلسل الإيقاف أي تسلسل من الأحرف، ولكن ننصحك بتجنُّب استخدام تسلسل من الأحرف قد يظهر في المحتوى الذي يتم إنشاؤه.

## استراتيجيات كتابة الطلبات المتلاحقة

قد يتطلّب تصميم الطلبات أحيانًا إجراء بعض التكرارات قبل أن تحصل باستمرار على الردّ الذي تبحث عنه. يقدّم هذا القسم إرشادات حول بعض الإجراءات التي يمكنك تجربتها عند تكرار طلباتك:

1. **استخدام صياغة مختلفة:** غالبًا ما يؤدي استخدام كلمات أو صياغة مختلفة في الطلبات إلى حصولك على ردود مختلفة من النموذج، حتى لو كانت جميعها تعني الشيء نفسه. إذا لم تحصل على النتائج المتوقّعة من طلبك، جرِّب إعادة صياغته.

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **التبديل إلى مهمة مشابهة:** إذا لم يتمكّن النموذج من اتّباع تعليماتك بشأن مهمة معيّنة، حاوِل تقديم تعليمات بشأن مهمة مشابهة تؤدي إلى النتيجة نفسها.

   يطلب هذا الطلب من النموذج تصنيف كتاب باستخدام فئات محدّدة مسبقًا:

   |  |
   | --- |
   | **الطلب:**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **الردّ:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   الردّ صحيح، ولكن النموذج لم يلتزم بحدود الخيارات. تريد أيضًا أن يردّ النموذج بأحد الخيارات فقط بدلاً من جملة كاملة. في هذه الحالة، يمكنك إعادة صياغة التعليمات كسؤال خيارات متعدّدة وطلب أن يختار النموذج أحد الخيارات.

   |  |
   | --- |
   | **الطلب:**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **الردّ:**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **تغيير ترتيب المحتوى في الطلب:** يمكن أن يؤثر ترتيب المحتوى في الطلب أحيانًا في الردّ. حاوِل تغيير ترتيب المحتوى ومعرفة تأثير ذلك في الردّ.

     ```
     Version 1:
     [examples]
     [context]
     [input]

     Version 2:
     [input]
     [examples]
     [context]

     Version 3:
     [examples]
     [input]
     [context]
     ```

## الردود الاحتياطية

الردّ الاحتياطي هو ردّ يقدّمه النموذج عندما يؤدي الطلب أو الردّ إلى تفعيل فلتر الأمان. ومن الأمثلة على الردود الاحتياطية: "لا يمكنني المساعدة في ذلك، فأنا مجرد نموذج لغوي".

إذا ردّ النموذج بردّ احتياطي، جرِّب زيادة درجة العشوائية.

## الاستناد إلى الحقائق وتنفيذ الرموز البرمجية

يستطيع Gemini استخدام أدوات لتجنُّب الهلوسة في السيناريوهات التي قد يؤدي فيها إلى تقديم ردود غير صحيحة.

تتيح ميزة [تحديد المصدر من خلال بحث Google](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) ربط نموذج Gemini بمحتوى الويب في الوقت الفعلي، ويجب تفعيلها عندما يحتاج النموذج إلى معرفة حقائق غير واضحة أو حديثة.

تتيح [أداة تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) في Gemini للنموذج إنشاء رموز Python البرمجية وتشغيلها، ويجب تفعيلها عندما يحتاج النموذج إلى إجراء أي نوع من العمليات الحسابية أو العد أو العمليات الحسابية.

## Gemini 3

تم تصميم [نماذج Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-3) لإجراء تحليلات متقدّمة واتّباع التعليمات.
وتقدّم أفضل ردّ في الطلبات المباشرة والمنظَّمة جيدًا والتي تحدّد بوضوح المهمة وأي قيود. يُنصح باتّباع الممارسات التالية للحصول على أفضل النتائج باستخدام Gemini 3:

### المبادئ الأساسية لإنشاء الطلبات

- **كن دقيقًا ومباشرًا:** حدِّد هدفك بوضوح واختصار، وتجنَّب استخدام لغة غير ضرورية أو مفرطة في الإقناع.
- **استخدام بنية متّسقة:** استخدِم فواصل واضحة للفصل بين الأجزاء المختلفة من الطلب. تُعدّ علامات XML (مثل `<context>` و`<task>`) أو عناوين Markdown فعّالة. اختَر تنسيقًا واحدًا واستخدِمه بشكل متّسق في طلب واحد.
- **تحديد المَعلمات:** اشرح بوضوح أي مصطلحات أو مَعلمات غامضة.
- **التحكّم في مستوى تفصيل الناتج:** تقدّم نماذج Gemini 3 إجابات مباشرة وفعّالة بشكل تلقائي. إذا كنت بحاجة إلى ردّ أكثر تفصيلاً أو بأسلوب محادثة، عليك أن تطلب ذلك صراحةً في تعليماتك.
- **التعامل مع المدخلات المتعددة الوسائط بشكل متسق:** عند استخدام النصوص أو الصور أو المحتوى الصوتي أو الفيديو، يجب التعامل معها كمدخلات من الفئة نفسها، والتأكّد من أنّ التعليمات تشير بوضوح إلى كل وسيط حسب الحاجة.
- **إعطاء الأولوية للتعليمات المهمة:** ضَع القيود السلوكية الأساسية وتعريفات الأدوار (الشخصية) ومتطلبات تنسيق الإخراج في &quot;تعليمات النظام&quot; أو في بداية طلب المستخدم.
- **بنية النصوص الطويلة:** عند تقديم كميات كبيرة من النصوص (مثل المستندات أو الرموز البرمجية)، يجب تقديم كل النصوص أولاً، ثم وضع التعليمات أو الأسئلة المحدّدة في *نهاية* الطلب.
- **سياق الفقرة التمهيدية:** بعد عرض مجموعة كبيرة من البيانات، استخدِم عبارة انتقال واضحة لربط السياق بطلب البحث، مثل "استنادًا إلى المعلومات الواردة أعلاه...".

### استراتيجيات Gemini 3 Flash

- **دقة اليوم الحالي:** أضِف العبارة التالية إلى تعليمات النظام لمساعدة النموذج في الانتباه إلى أنّ اليوم الحالي هو في عام 2026:

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **دقة تاريخ انتهاء قاعدة المعرفة:** أضِف العبارة التالية إلى تعليمات النظام لكي يكون النموذج على دراية بتاريخ انتهاء قاعدة المعرفة:

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **أداء الاستناد إلى مصادر خارجية:** أضِف العبارة التالية إلى تعليمات النظام (مع إجراء التعديلات اللازمة) لتحسين قدرة النموذج على الاستناد إلى السياق المقدَّم في الردود:

  ```
  You are a strictly grounded assistant limited to the information provided in
  the User Context. In your answers, rely **only** on the facts that are
  directly mentioned in that context. You must **not** access or utilize your
  own knowledge or common sense to answer. Do not assume or infer from the
  provided facts; simply report them exactly as they appear. Your answer must
  be factual and fully truthful to the provided text, leaving absolutely no
  room for speculation or interpretation. Treat the provided context as the
  absolute limit of truth; any facts or details that are not directly
  mentioned in the context must be considered **completely untruthful** and
  **completely unsupported**. If the exact answer is not explicitly written in
  the context, you must state that the information is not available.
  ```

### تحسين قدرات الاستدلال والتخطيط

تنشئ نماذج Gemini 2.5 و3 تلقائيًا نصًا داخليًا "للتفكير" من أجل تحسين أداء الاستدلال، وبالتالي، ليس من الضروري عادةً أن يقدّم النموذج مخططًا أو خطة أو تفاصيل لخطوات الاستدلال في الرد الذي يتم إرجاعه. بالنسبة إلى المشاكل التي تتطلب استدلالاً مكثفًا، يمكن أن تؤدي الطلبات البسيطة، مثل "التفكير مليًا قبل الإجابة"، إلى تحسين الأداء، ولكن على حساب رموز التفكير الإضافية.

يمكنك الاطّلاع على مستندات [طريقة عمل Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=ar) لمزيد من التفاصيل.

### أمثلة على الطلبات المنظَّمة

يساعد استخدام العلامات أو Markdown النموذج في التمييز بين التعليمات والسياق والمهام.

**مثال على تنسيق XML:**

```
<role>
You are a helpful assistant.
</role>

<constraints>
1. Be objective.
2. Cite sources.
</constraints>

<context>
[Insert User Input Here - The model knows this is data, not instructions]
</context>

<task>
[Insert the specific user request here]
</task>
```

**مثال على Markdown:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### مثال على نموذج يجمع بين أفضل الممارسات

يقدّم هذا النموذج المبادئ الأساسية لكتابة الطلبات باستخدام Gemini 3. احرص دائمًا على تكرار الخطوات وتعديلها لتناسب حالة الاستخدام المحدّدة.

**تعليمات النظام:**

```
<role>
You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
You are precise, analytical, and persistent.
</role>

<instructions>
1. **Plan**: Analyze the task and create a step-by-step plan.
2. **Execute**: Carry out the plan.
3. **Validate**: Review your output against the user's task.
4. **Format**: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Specify Low/Medium/High]
- Tone: [Specify Formal/Casual/Technical]
</constraints>

<output_format>
Structure your response as follows:
1. **Executive Summary**: [Short overview]
2. **Detailed Response**: [The main content]
</output_format>
```

**طلب المستخدم:**

```
<context>
[Insert relevant documents, code snippets, or background info here]
</context>

<task>
[Insert specific user request here]
</task>

<final_instruction>
Remember to think step-by-step before answering.
</final_instruction>
```

## عمليات سير العمل المستندة إلى الوكلاء

بالنسبة إلى مهام سير العمل المعقّدة التي تتضمّن وكلاء، غالبًا ما تكون هناك حاجة إلى تعليمات محدّدة للتحكّم في طريقة استدلال النموذج وتخطيطه وتنفيذه للمهام. وعلى الرغم من أنّ Gemini يقدّم أداءً عامًا قويًا، غالبًا ما تتطلّب الوكلاء المعقّدة منك ضبط المفاضلة بين التكلفة الحسابية (وقت الاستجابة والرموز المميزة) ودقة المهام.

عند تصميم الطلبات الموجّهة إلى الوكلاء، يجب مراعاة جوانب السلوك التالية التي يمكنك توجيهها في الوكيل:

### الاستدلال والاستراتيجية

إعدادات طريقة تفكير النموذج وتخطيطه قبل اتخاذ أي إجراء

- **التجزئة المنطقية:** تحدّد مدى دقة تحليل النموذج للقيود والمتطلبات الأساسية وترتيب العمليات.
- **تشخيص المشكلة**: يتحكّم في عمق التحليل عند تحديد الأسباب وفي استخدام النموذج للاستدلال الاستنتاجي. تحدّد ما إذا كان النموذج سيقبل الإجابة الأكثر وضوحًا أو سيبحث عن تفسيرات معقّدة وأقل احتمالاً.
- **شمولية المعلومات:** المفاضلة بين تحليل كل السياسات والمستندات المتاحة وبين إعطاء الأولوية للكفاءة والسرعة

### التنفيذ والموثوقية

إعدادات طريقة عمل الوكيل بشكل مستقل والتعامل مع العوائق

- **القدرة على التكيّف:** طريقة تفاعل النموذج مع البيانات الجديدة تحدّد هذه السمة ما إذا كان يجب الالتزام بدقة بالخطة الأولية أو تغييرها على الفور عندما تتعارض الملاحظات مع الافتراضات.
- **المثابرة والاسترداد:** هي مدى محاولة النموذج تصحيح الأخطاء ذاتيًا. تزيد المثابرة العالية من معدلات النجاح ولكنها تنطوي على مخاطر ارتفاع تكاليف الرموز المميزة أو التكرار.
- **تقييم المخاطر:** منطق تقييم العواقب يميز بوضوح بين الإجراءات الاستكشافية المنخفضة المخاطر (عمليات القراءة) وتغييرات الحالة العالية المخاطر (عمليات الكتابة).

### التفاعل والإخراج

إعدادات طريقة تواصل الوكيل مع المستخدم وتنسيق النتائج

- **الغموض والتعامل مع الأذونات:** يحدّد هذا الإعداد الحالات التي يُسمح فيها للنموذج بوضع افتراضات والحالات التي يجب فيها إيقاف التنفيذ مؤقتًا لطلب توضيح أو إذن من المستخدم.
- **مستوى التفصيل:** يتحكّم في حجم النص الذي يتم إنشاؤه إلى جانب طلبات الأدوات. يحدّد هذا الخيار ما إذا كان النموذج يوضّح للمستخدم الإجراءات التي يتّخذها أو يبقى صامتًا أثناء التنفيذ.
- **الدقة والشمولية:** تشير إلى الدقة المطلوبة للناتج، وتحدّد ما إذا كان على النموذج حلّ كل الحالات الحدّية وتقديم أرقام دقيقة أو ما إذا كانت التقديرات التقريبية مقبولة.

### نموذج تعليمات النظام

تعليمات النظام التالية هي مثال قيّمه الباحثون لتحسين الأداء في مقاييس الأداء المستندة إلى الوكلاء، حيث يجب أن يلتزم النموذج بمجموعة معقّدة من القواعد ويتفاعل مع المستخدم. تشجّع هذه التعليمات الوكيل على التفكير والتخطيط بشكل فعّال، وتفرض سلوكيات محدّدة على مستوى الأبعاد المذكورة أعلاه، وتتطلّب من النموذج التخطيط بشكل استباقي قبل اتخاذ أي إجراء.

يمكنك تعديل هذا النموذج ليتناسب مع القيود المحدّدة لحالة الاستخدام.

```
You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses.

Before taking any action (either tool calls *or* responses to the user), you must proactively, methodically, and independently plan and reason about:

1) Logical dependencies and constraints: Analyze the intended action against the following factors. Resolve conflicts in order of importance:
    1.1) Policy-based rules, mandatory prerequisites, and constraints.
    1.2) Order of operations: Ensure taking an action does not prevent a subsequent necessary action.
        1.2.1) The user may request actions in a random order, but you may need to reorder operations to maximize successful completion of the task.
    1.3) Other prerequisites (information and/or actions needed).
    1.4) Explicit user constraints or preferences.

2) Risk assessment: What are the consequences of taking the action? Will the new state cause any future issues?
    2.1) For exploratory tasks (like searches), missing *optional* parameters is a LOW risk. **Prefer calling the tool with the available information over asking the user, unless** your `Rule 1` (Logical Dependencies) reasoning determines that optional information is required for a later step in your plan.

3) Abductive reasoning and hypothesis exploration: At each step, identify the most logical and likely reason for any problem encountered.
    3.1) Look beyond immediate or obvious causes. The most likely reason may not be the simplest and may require deeper inference.
    3.2) Hypotheses may require additional research. Each hypothesis may take multiple steps to test.
    3.3) Prioritize hypotheses based on likelihood, but do not discard less likely ones prematurely. A low-probability event may still be the root cause.

4) Outcome evaluation and adaptability: Does the previous observation require any changes to your plan?
    4.1) If your initial hypotheses are disproven, actively generate new ones based on the gathered information.

5) Information availability: Incorporate all applicable and alternative sources of information, including:
    5.1) Using available tools and their capabilities
    5.2) All policies, rules, checklists, and constraints
    5.3) Previous observations and conversation history
    5.4) Information only available by asking the user

6) Precision and Grounding: Ensure your reasoning is extremely precise and relevant to each exact ongoing situation.
    6.1) Verify your claims by quoting the exact applicable information (including policies) when referring to them. 

7) Completeness: Ensure that all requirements, constraints, options, and preferences are exhaustively incorporated into your plan.
    7.1) Resolve conflicts using the order of importance in #1.
    7.2) Avoid premature conclusions: There may be multiple relevant options for a given situation.
        7.2.1) To check for whether an option is relevant, reason about all information sources from #5.
        7.2.2) You may need to consult the user to even know whether something is applicable. Do not assume it is not applicable without checking.
    7.3) Review applicable sources of information from #5 to confirm which are relevant to the current state.

8) Persistence and patience: Do not give up unless all the reasoning above is exhausted.
    8.1) Don't be dissuaded by time taken or user frustration.
    8.2) This persistence must be intelligent: On *transient* errors (e.g. please try again), you *must* retry **unless an explicit retry limit (e.g., max x tries) has been reached**. If such a limit is hit, you *must* stop. On *other* errors, you must change your strategy or arguments, not repeat the same failed call.

9) Inhibit your response: only take an action after all the above reasoning is completed. Once you've taken an action, you cannot take it back.
```

## الخطوات التالية

- بعد أن أصبح لديك فهم أعمق لتصميم الطلبات، جرِّب كتابة طلباتك الخاصة باستخدام [Google AI Studio](http://aistudio.google.com?hl=ar).
- لمزيد من المعلومات حول إنشاء الطلبات المتعددة الوسائط، اطّلِع على [توجيه الطلبات باستخدام ملفات الوسائط](https://ai.google.dev/gemini-api/docs/files?hl=ar#prompt-guide).
- لمعرفة المزيد عن توجيه الطلبات باستخدام الصور، يمكنك الاطّلاع على أدلة الطلبات الخاصة بـ [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar#prompt-guide) و[Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=ar#imagen-prompt-guide).
- لمعرفة المزيد عن طلبات الفيديو، اطّلِع على [دليل كتابة طلبات Veo](https://ai.google.dev/gemini-api/docs/video?hl=ar#prompt-guide).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-10 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-10 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
