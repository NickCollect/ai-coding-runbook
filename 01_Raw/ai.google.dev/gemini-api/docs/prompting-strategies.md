---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ar
fetched_at: 2026-10-26T05:58:37.874848+00:00
title: "\u0627\u0633\u062a\u0631\u0627\u062a\u064a\u062c\u064a\u0627\u062a \u0627\u0644\u062a\u0635\u0645\u064a\u0645 \u0627\u0644\u0641\u0648\u0631\u064a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon متاح الآن. [جرِّب هذه الميزة](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# استراتيجيات التصميم الفوري

*تصميم الطلبات* هو عملية إنشاء طلبات أو طلبات باللغة الطبيعية
تؤدي إلى إنتاج ردود دقيقة وعالية الجودة من نموذج لغوي.

تقدّم هذه الصفحة المفاهيم الأساسية والاستراتيجيات وأفضل الممارسات لمساعدتك في البدء بتصميم الطلبات للاستفادة إلى أقصى حدّ من نماذج الذكاء الاصطناعي من Gemini.

## أدلة كتابة الطلبات حسب الموضوع

هل تبحث عن استراتيجيات أكثر تحديدًا لإنشاء الطلبات؟ اطّلِع على أدلة كتابة الطلبات الأخرى
على:

- [استخدام ملفات الوسائط في الطلبات](https://ai.google.dev/gemini-api/docs/files?hl=ar#prompt-guide)
- [طلبات إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar#prompt-guide)
- [إدخال الطلبات لإنشاء الفيديوهات](https://ai.google.dev/gemini-api/docs/video?hl=ar#prompt-guide)

يمكنك العثور على نماذج طلبات أخرى في [معرض الطلبات](https://ai.google.dev/gemini-api/prompts?hl=ar)
الذي يهدف إلى عرض العديد من المفاهيم التي تمت مشاركتها في هذا الدليل بشكل تفاعلي.

## تعليمات واضحة ومحدّدة

تتمثّل إحدى الطرق الفعّالة والمناسبة لتخصيص سلوك النموذج في تزويده بتعليمات واضحة ومحدّدة. يمكن أن تكون التعليمات في شكل سؤال أو مهام خطوة بخطوة أو معقدة مثل تخطيط تجربة المستخدم وعقليته.

### الإدخال

الإدخال هو النص المطلوب في الطلب الذي تريد أن يقدّم النموذج ردًا عليه. يمكن أن تكون المدخلات سؤالاً يجيب عنه النموذج (إدخال سؤال)، أو مهمة يؤديها النموذج (إدخال مهمة)، أو كيانًا يعمل عليه النموذج (إدخال كيان)، أو إدخالاً جزئيًا يكمله النموذج أو يواصله (إدخال الإكمال).

| **نوع الطلبات** | **الطلب** | **الردّ الذي أنشأه الذكاء الاصطناعي** |
| --- | --- | --- |
| السؤال | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| المهمة | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| الكيان | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### الإكمال الجزئي للإدخال

تعمل النماذج اللغوية التوليدية كأداة إكمال تلقائي متقدّمة. عند تقديم محتوى جزئي، يمكن للنموذج تقديم بقية المحتوى أو ما يعتقد أنّه استمرار لهذا المحتوى كاستجابة. عند القيام بذلك، إذا قمت بتضمين أي أمثلة أو سياق، يمكن للنموذج أن يأخذ هذه الأمثلة أو السياق في الاعتبار.

يقدّم المثال التالي طلبًا يتضمّن تعليمات وإدخال كيان:

|  |
| --- |
| **الطلب:**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **الردّ:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

مع أنّ النموذج نفّذ ما طُلب منه، إلا أنّ كتابة التعليمات بلغة طبيعية قد يكون أمرًا صعبًا في بعض الأحيان، كما أنّه يترك الكثير من الخيارات لتفسير النموذج.
على سبيل المثال، قد تحتوي قائمة المطعم على العديد من الأصناف. لتقليل حجم استجابة JSON، قد ترغب في حذف العناصر التي لم يتم طلبها. في
هذه الحالة، يمكنك تقديم مثال وبادئة ردّ والسماح للنموذج
بإكمالها:

|  |
| --- |
| **الطلب:**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **الردّ:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

لاحظ كيف تم استبعاد "تشيز برغر" من الناتج لأنّه لم يكن جزءًا من الطلب.

على الرغم من أنّه يمكنك تحديد تنسيق عناصر الرد البسيطة بتنسيق JSON باستخدام الطلبات، ننصحك باستخدام ميزة [الإخراج المنظَّم](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar) في Gemini API عند تحديد مخطط JSON أكثر تعقيدًا للرد.

### القيود

حدِّد أي قيود على قراءة الطلب أو إنشاء ردّ. يمكنك
إخبار النموذج بما يجب فعله وما لا يجب فعله. على سبيل المثال، يمكنك تحديد قيد
في الطلب بشأن المدة التي تريد أن يستغرقها الملخّص:

|  |
| --- |
| **الطلب:**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **الردّ:**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### تنسيق الردّ

يمكنك تقديم تعليمات تحدّد تنسيق الرد. على سبيل المثال، يمكنك طلب تنسيق الردّ كجدول أو قائمة نقطية أو عرض تقديمي ترويجي سريع أو كلمات رئيسية أو جملة أو فقرة. تطلب تعليمات النظام التالية من النموذج أن يكون أكثر حوارية في ردوده:

|  |
| --- |
| **تعليمات النظام**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **الطلب**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **الردّ:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### تنسيق الردود باستخدام استراتيجية الإكمال

يمكن أن تساعد [استراتيجية الإكمال](#completion) أيضًا في تنسيق الردّ.
يطلب المثال التالي من النموذج إنشاء مخطط تفصيلي لمقالة:

|  |
| --- |
| **الطلب:**    ``` Create an outline for an essay about hummingbirds. ```  **الردّ:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

لم يحدّد الطلب تنسيق المخطط، فاختار النموذج تنسيقًا لك. للحصول على مخطط تفصيلي بتنسيق محدّد من النموذج، يمكنك إضافة نص يمثّل بداية المخطط التفصيلي والسماح للنموذج بإكماله استنادًا إلى النمط الذي بدأته.

|  |
| --- |
| **الطلب:**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **الردّ:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## الطلبات بلا أمثلة مقابل الطلبات ببضعة أمثلة

يمكنك تضمين أمثلة في الطلب توضّح للنموذج الشكل الذي تبدو عليه الإجابة الصحيحة. يحاول النموذج تحديد الأنماط والعلاقات من الأمثلة وتطبيقها عند إنشاء رد. تُعرف الطلبات التي تتضمّن بضعة أمثلة باسم طلبات *التلقين ببضعة أمثلة*، بينما تُعرف الطلبات التي لا تتضمّن أي أمثلة باسم طلبات *التلقين بلا أمثلة*. غالبًا ما تُستخدم الطلبات ببضعة أمثلة لتنظيم التنسيق أو الصياغة أو تحديد النطاق أو الأنماط العامة لردود النموذج. استخدِم أمثلة محدّدة ومتنوّعة لمساعدة النموذج في تضييق نطاق تركيزه
وإنشاء نتائج أكثر دقة.

ننصحك دائمًا بتضمين أمثلة التلقين ببضعة أمثلة في طلباتك. من المرجّح أن تكون الطلبات التي لا تتضمّن التلقين ببضعة أمثلة أقل فعالية. في الواقع، يمكنك إزالة التعليمات من طلبك إذا كانت الأمثلة واضحة بما يكفي لإظهار المهمة المطلوبة.

يطلب الطلب التالي بدون أمثلة من النموذج اختيار أفضل تفسير.

|  |
| --- |
| **الطلب:**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **الردّ:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

إذا كانت حالة الاستخدام تتطلّب أن ينتج النموذج ردودًا موجزة، يمكنك تضمين أمثلة في الطلب تعطي الأولوية للردود الموجزة.

يقدّم الطلب التالي مثالَين يوضّحان تفضيل التفسيرات الأقصر. في الردّ، يمكنك ملاحظة أنّ الأمثلة وجّهت النموذج لاختيار التفسير الأقصر (`Explanation2`) بدلاً من التفسير الأطول (`Explanation1`) كما فعل سابقًا.

|  |
| --- |
| **الطلب:**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **الردّ:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### العدد الأمثل للأمثلة

يمكن لنماذج مثل Gemini غالبًا التعرّف على الأنماط باستخدام بعض الأمثلة، ولكن قد تحتاج إلى تجربة عدد الأمثلة التي يجب تقديمها في الطلب للحصول على أفضل النتائج. في الوقت نفسه، إذا أضفت الكثير من الأمثلة،
قد يبدأ النموذج في [الإفراط في ملاءمة](https://developers.google.com/machine-learning/glossary?hl=ar#overfitting)
الردّ مع الأمثلة.

### اعتماد تنسيق موحَّد

تأكَّد من أنّ بنية وتنسيق التلقين ببضعة أمثلة متطابقة لتجنُّب الحصول على ردود بتنسيقات غير مرغوب فيها. من الأهداف الأساسية لإضافة التلقين ببضعة أمثلة في الطلبات هو توضيح تنسيق الرد للنموذج. لذلك،
من الضروري ضمان اتساق التنسيق في جميع الأمثلة، مع إيلاء اهتمام خاص لعلامات XML والمسافات البيضاء والأسطر الجديدة وفواصل الأمثلة.

## إضافة سياق

يمكنك تضمين تعليمات ومعلومات في طلب يحتاج النموذج إلى
حلّ مشكلة، بدلاً من افتراض أنّ النموذج يتضمّن كل المعلومات
المطلوبة. تساعد هذه المعلومات السياقية النموذج في فهم القيود
وتفاصيل ما تطلب منه القيام به.

يطلب المثال التالي من النموذج تقديم إرشادات لتحديد المشاكل في جهاز التوجيه وحلّها:

|  |
| --- |
| **الطلب:**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **الردّ:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

يبدو الردّ كمعلومات عامة حول تحديد المشاكل وحلّها، ولا يتعلّق
بجهاز التوجيه أو حالة مؤشرات LED الضوئية.

لتخصيص الردّ لجهاز التوجيه المحدّد، يمكنك إضافة دليل تحديد المشاكل وحلّها الخاص بجهاز التوجيه إلى الطلب كمرجع يمكن للنموذج الاستناد إليه عند تقديم الردّ.

|  |
| --- |
| **الطلب:**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **الردّ:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## تقسيم الطلبات إلى مكوّنات

بالنسبة إلى حالات الاستخدام التي تتطلّب طلبات معقّدة، يمكنك مساعدة النموذج في التعامل مع هذا التعقيد من خلال تقسيم الطلبات إلى مكوّنات أبسط.

1. **تقسيم التعليمات:** بدلاً من تضمين العديد من التعليمات في طلب واحد، يمكنك إنشاء طلب واحد لكل تعليمة. يمكنك اختيار الطلب الذي تريد معالجته
   بناءً على إدخال المستخدم.
2. **الطلبات المتسلسلة:** بالنسبة إلى المهام المعقّدة التي تتضمّن خطوات متسلسلة متعددة،
   يمكنك جعل كل خطوة طلبًا وربط الطلبات معًا في تسلسل. في هذه السلسلة المتتابعة من الطلبات، يصبح الناتج من أحد الطلبات في التسلسل هو المدخل للطلب التالي. ويكون الناتج من الطلب الأخير في التسلسل
   هو الناتج النهائي.
3. **تجميع الردود:** يحدث التجميع عندما تريد تنفيذ مهام متوازية مختلفة على أجزاء مختلفة من البيانات وتجميع النتائج لإنتاج الناتج النهائي. على سبيل المثال، يمكنك أن تطلب من النموذج تنفيذ عملية واحدة على الجزء الأول من البيانات، وتنفيذ عملية أخرى على بقية البيانات، ثم تجميع النتائج.

## تجربة مَعلمات النموذج

يتضمّن كل طلب ترسله إلى أحد النماذج قيم مَعلمات تتحكّم في طريقة إنشاء النموذج للردّ. يمكن أن ينشئ النموذج نتائج مختلفة لقيم المَعلمات المختلفة. جرِّب قيم مَعلمات مختلفة للحصول على
أفضل القيم للمهمة. قد تختلف المَعلمات المتاحة
للطُرز المختلفة. في ما يلي المَعلمات الأكثر شيوعًا:

1. **الحدّ الأقصى لعدد الرموز المميزة للناتج:** يحدّد الحدّ الأقصى لعدد الرموز المميزة التي يمكن إنشاؤها في الردّ. يتألف الرمز المميّز من أربعة أحرف تقريبًا. يتوافق 100 رمز مميز مع 60 إلى 80 كلمة تقريبًا.
2. **درجة العشوائية:** تتحكّم درجة العشوائية في مستوى العشوائية في اختيار الرموز المميزة. يتم استخدام درجة الحرارة لأخذ العينات أثناء إنشاء الردود،
   ويحدث ذلك عند تطبيق `topP` و`topK`. تكون درجات العشوائية المنخفضة مناسبة للطلبات التي تتطلّب ردودًا أكثر حتمية أو أقل انفتاحًا، بينما يمكن أن تؤدي درجات العشوائية المرتفعة إلى نتائج أكثر تنوعًا أو إبداعًا. درجة الحرارة 0 هي درجة حتمية، ما يعني أنّه يتم دائمًا اختيار الردّ ذي الاحتمالية الأعلى.
3. **`topK`:** تغيّر المَعلمة `topK` طريقة اختيار النموذج للرموز المميّزة في
   النتائج. يشير `topK` البالغ 1 إلى أنّ الرمز المميّز المحدّد هو الأكثر احتمالاً بين جميع الرموز المميّزة في مفردات النموذج (يُعرف أيضًا باسم فك الترميز الجشع)، بينما يشير `topK` البالغ 3 إلى أنّه يتم اختيار الرمز المميّز التالي من بين 3 رموز مميّزة الأكثر احتمالاً باستخدام درجة الحرارة. في كل خطوة من خطوات اختيار الرموز المميّزة، يتم اختيار الرموز المميّزة التي يبلغ عددها `topK` والتي لها أعلى احتمالات. بعد ذلك، تتم فلترة الرموز المميّزة بشكل أكبر استنادًا إلى `topP`، ويتم اختيار الرمز المميّز النهائي باستخدام عيّنات درجة الحرارة.
4. ‫**`topP`:** تغيّر المَعلمة `topP` طريقة اختيار النموذج للرموز المميزة في
   الناتج. يتم اختيار الرموز المميّزة من الأكثر احتمالاً إلى الأقل احتمالاً حتى يساوي مجموع
   احتمالاتها قيمة `topP`. على سبيل المثال، إذا كانت الرموز المميزة A وB وC تتضمّن احتمالية 0.3 و0.2 و0.1 وكانت قيمة `topP` هي 0.5، سيختار النموذج الرمز المميز A أو B كرمز مميز تالٍ باستخدام درجة الحرارة ويستبعد C كمرشح. القيمة التلقائية `topP` هي 0.95.
5. **`stop_sequences`:** يمكنك ضبط تسلسل إيقاف لإعلام النموذج بالتوقف عن إنشاء المحتوى. يمكن أن يكون تسلسل الإيقاف أي تسلسل من الأحرف. حاوِل تجنُّب استخدام سلسلة من الأحرف التي قد تظهر في المحتوى الذي يتم إنشاؤه.

## استراتيجيات كتابة الطلبات المتلاحقة

قد يتطلّب تصميم الطلبات أحيانًا بضع محاولات قبل
الحصول على الردّ المطلوب بشكل متّسق. يقدّم هذا القسم إرشادات حول بعض الإجراءات التي يمكنك تجربتها عند تكرار طلباتك:

1. **استخدام صياغة مختلفة:** غالبًا ما يؤدي استخدام كلمات أو صياغة مختلفة في طلباتك إلى الحصول على ردود مختلفة من النموذج، على الرغم من أنّها تعني جميعًا الشيء نفسه. إذا لم تحصل على النتائج المتوقّعة من طلبك، حاوِل إعادة صياغته.

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **التبديل إلى مهمة مشابهة:** إذا لم تتمكّن من جعل النموذج يتّبع تعليماتك لمهمة معيّنة، حاوِل إعطاءه تعليمات لمهمة مشابهة تحقّق النتيجة نفسها.

   يطلب هذا الطلب من النموذج تصنيف كتاب باستخدام فئات محدّدة مسبقًا:

   |  |
   | --- |
   | **الطلب:**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **الردّ:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   الردّ صحيح، ولكن النموذج لم يلتزم بالخيارات المتاحة. تريد أيضًا أن يستجيب النموذج بأحد الخيارات بدلاً من جملة كاملة. في هذه الحالة، يمكنك إعادة صياغة التعليمات كسؤال خيارات متعدّدة والطلب من النموذج تحديد خيار.

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
   - **تغيير ترتيب محتوى الطلب:** يمكن أن يؤثر ترتيب المحتوى في الطلب أحيانًا في الردّ. جرِّب تغيير ترتيب المحتوى ولاحظ
     كيف يؤثر ذلك في الردّ.

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

الردّ الاحتياطي هو ردّ يقدّمه النموذج عندما يؤدي الطلب أو الردّ إلى تفعيل فلتر أمان. مثال على الردّ الاحتياطي: "لا يمكنني المساعدة في ذلك، فأنا مجرد نموذج لغوي".

إذا قدّم النموذج ردًا احتياطيًا، جرِّب زيادة درجة العشوائية.

## التحقّق من المصادر وتنفيذ الرموز البرمجية

يستطيع Gemini استخدام الأدوات لتجنُّب الهلوسة في السيناريوهات التي قد ينتج عنها ردود غير صحيحة.

تتيح ميزة [تحديد المصدر من خلال &quot;بحث Google&quot;](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) ربط نموذج Gemini بمحتوى الويب في الوقت الفعلي، ويجب تفعيلها عندما يحتاج النموذج إلى معرفة حقائق غامضة أو حديثة.

تتيح [أداة تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) في Gemini للنموذج إنشاء رموز Python البرمجية وتنفيذها، ويجب تفعيلها عندما يحتاج النموذج إلى إجراء أي نوع من العمليات الحسابية أو العدّ أو الحساب.

## Gemini 3

[نماذج Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-3) مصمَّمة للاستدلال المتقدّم
واتّباع التعليمات.
وتقدّم أفضل ردّ على الطلبات المباشرة والمنظّمة بشكل جيد والتي تحدّد المهمة وأي قيود بوضوح. يُنصح باتّباع الممارسات التالية للحصول على أفضل النتائج باستخدام Gemini 3:

### المبادئ الأساسية لإنشاء الطلبات

- **الدقة والوضوح:** حدِّد هدفك بوضوح وإيجاز. تجنَّب
  اللغة غير الضرورية أو المقنعة بشكل مفرط.
- **استخدام بنية متّسقة:** استخدِم فواصل واضحة لفصل الأجزاء المختلفة من طلبك. يمكنك استخدام علامات بتنسيق XML (مثل `<context>` و`<task>`) أو عناوين بتنسيق Markdown. اختَر تنسيقًا واحدًا واستخدِمه باستمرار
  ضمن طلب واحد.
- **تحديد المَعلمات:** اشرح بوضوح أي مصطلحات أو مَعلمات غامضة.
- **التحكّم في إسهاب المخرجات:** تقدّم نماذج Gemini 3 تلقائيًا إجابات مباشرة وفعّالة. إذا كنت بحاجة إلى ردّ أكثر تفصيلاً أو بأسلوب حواري،
  عليك طلب ذلك صراحةً في تعليماتك.
- **التعامل مع المدخلات المتعددة الوسائط بشكل متسق:** عند استخدام النصوص أو الصور أو المحتوى الصوتي أو الفيديو، يجب التعامل معها كمدخلات من الفئة نفسها. تأكَّد من أنّ تعليماتك تشير بوضوح
  إلى كل طريقة حسب الحاجة.
- **إعطاء الأولوية للتعليمات المهمة:** ضَع القيود السلوكية الأساسية وتعريفات الأدوار (الشخصية) ومتطلبات تنسيق الإخراج في &quot;تعليمات النظام&quot; أو في بداية طلب المستخدم.
- **تنظيم السياقات الطويلة:** عند تقديم كميات كبيرة من السياق (مثل المستندات أو الرموز البرمجية)، يجب تقديم السياق بالكامل أولاً. أضِف تعليماتك أو أسئلتك المحدّدة في *نهاية* الطلب.
- **سياق عبارة الربط:** بعد عرض مجموعة كبيرة من البيانات، استخدِم عبارة انتقال واضحة لربط السياق بطلب البحث، مثل "استنادًا إلى المعلومات الواردة أعلاه...".

### استراتيجيات Gemini 3 Flash

- **دقة اليوم الحالي:** أضِف العبارة التالية إلى تعليمات النظام لمساعدة النموذج في الانتباه إلى أنّ اليوم الحالي هو في عام 2026:

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **دقة تاريخ آخر تحديث للبيانات:** أضِف العبارة التالية إلى تعليمات النظام لإعلام النموذج بتاريخ آخر تحديث للبيانات:

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **أداء التأسيس:** أضِف العبارة التالية إلى تعليمات النظام (مع إجراء تعديلات عند الاقتضاء) لتحسين قدرة النموذج على تأسيس الردود في السياق المقدَّم:

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

تنشئ نماذج Gemini 2.5 و3 تلقائيًا نصًا داخليًا "تحليليًا" لتحسين أداء الاستدلال. وبالتالي، ليس من الضروري عادةً أن يتضمّن الردّ الذي يتم إرجاعه
مخطط النموذج أو خطته أو تفاصيل خطوات الاستدلال. بالنسبة إلى المشاكل التي تتطلّب استدلالاً مكثّفًا، يمكن أن تؤدي الطلبات البسيطة مثل "فكِّر
بجدية قبل الإجابة" إلى تحسين الأداء، ولكن على حساب
رموز مميّزة إضافية للتفكير.

لمزيد من التفاصيل، يُرجى الاطّلاع على مستندات [طريقة عمل Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=ar).

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

يتضمّن هذا النموذج المبادئ الأساسية لكتابة الطلبات في Gemini 3. احرص دائمًا على تكرار الخطوات وتعديلها لتناسب حالة الاستخدام المحدّدة.

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

## سير العمل المستند إلى الوكلاء

بالنسبة إلى سير العمل المستند إلى الوكلاء، غالبًا ما تكون هناك حاجة إلى تعليمات محدّدة للتحكّم في كيفية استدلال النموذج وتخطيطه وتنفيذه للمهام. على الرغم من أنّ Gemini يقدّم أداءً عامًا قويًا، غالبًا ما يتطلّب منك الوكلاء المعقّدون ضبط المفاضلة بين تكلفة الحوسبة (وقت الاستجابة والرموز المميّزة) ودقة المهام.

عند تصميم الطلبات الموجّهة إلى الوكلاء، ضَع في اعتبارك جوانب السلوك التالية التي يمكنك توجيهها في الوكيل:

### الاستدلال والاستراتيجية

إعدادات تحدّد طريقة تفكير النموذج وتخطيطه قبل اتخاذ الإجراءات

- **التحليل المنطقي:** يحدّد مدى دقة النموذج في تحليل القيود والمتطلبات الأساسية وترتيب العمليات.
- **تشخيص المشاكل**: يتحكّم في مدى عمق التحليل عند تحديد الأسباب واستخدام النموذج للاستدلال الاستقرائي. تحدّد هذه السمة ما إذا كان النموذج سيقبل الإجابة الأكثر وضوحًا أو سيستكشف تفسيرات معقّدة وأقل احتمالاً.
- **شمولية المعلومات:** الموازنة بين تحليل كل سياسة ومستند متاحَين مقابل إعطاء الأولوية للكفاءة والسرعة.

### التنفيذ والموثوقية

إعدادات طريقة عمل الوكيل بشكل مستقل وكيفية تعامله مع العقبات

- **القدرة على التكيّف:** طريقة تفاعل النموذج مع البيانات الجديدة يحدّد ما إذا كان يجب الالتزام الصارم بالخطة الأولية أو تغييرها فورًا عندما تتعارض الملاحظات مع الافتراضات.
- **الثبات والاسترداد:** يشير إلى مدى محاولة النموذج تصحيح الأخطاء ذاتيًا. تزيد المثابرة العالية من معدلات النجاح، ولكنّها قد تؤدي إلى ارتفاع تكاليف الرموز المميّزة أو حدوث تكرار حلقي.
- **تقييم المخاطر:** منطق تقييم العواقب يفرّق بشكل واضح بين الإجراءات الاستكشافية المنخفضة المخاطر (عمليات القراءة) وتغييرات الحالة العالية المخاطر (عمليات الكتابة).

### التفاعل والإخراج

إعدادات طريقة تواصل الوكيل مع المستخدم وتنسيق النتائج

- **التعامل مع الغموض والأذونات:** يحدّد هذا الإعداد الحالات التي يُسمح فيها للنموذج بوضع افتراضات مقابل الحالات التي يجب فيها إيقاف التنفيذ مؤقتًا لطلب توضيح أو إذن من المستخدم.
- **الإسهاب:** يتحكّم في حجم النص الذي يتم إنشاؤه مع طلبات الأدوات. يحدّد هذا الإعداد ما إذا كان النموذج يشرح إجراءاته للمستخدم أو يظل صامتًا أثناء التنفيذ.
- **الدقة والاكتمال:** مستوى الدقة المطلوب في الناتج. تحدّد هذه السمة ما إذا كان على النموذج حلّ كل الحالات الحدّية وتقديم أرقام دقيقة أو ما إذا كانت التقديرات التقريبية مقبولة.

### نموذج تعليمات النظام

تعليمات النظام التالية هي مثال تم تقييمه من قِبل الباحثين لتحسين الأداء في مقاييس الأداء المستندة إلى الوكلاء، حيث يجب أن يلتزم النموذج بقواعد معقّدة ويتفاعل مع المستخدم. يشجّع هذا النظام الوكيل على التفكير والتخطيط بشكل فعّال، ويفرض سلوكيات محدّدة على مستوى الأبعاد المذكورة أعلاه، ويطلب من النموذج التخطيط بشكل استباقي قبل اتخاذ أي إجراء.

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

- بعد أن أصبحت لديك معرفة أعمق بتصميم الطلبات، جرِّب كتابة طلباتك الخاصة باستخدام [Google AI Studio](http://aistudio.google.com?hl=ar).
- لمزيد من المعلومات حول توجيه الطلبات المتعدّدة الوسائط، اطّلِع على المقالة
  [توجيه الطلبات باستخدام ملفات الوسائط](https://ai.google.dev/gemini-api/docs/files?hl=ar#prompt-guide).
- لمعرفة المزيد عن كتابة الطلبات لإنشاء الصور، اطّلِع على دليل الطلبات في [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar#prompt-guide).
- لمعرفة المزيد عن طلبات الفيديو، اطّلِع على [دليل طلبات Veo](https://ai.google.dev/gemini-api/docs/video?hl=ar#prompt-guide).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-10-13 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-10-13 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
