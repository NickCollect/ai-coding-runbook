---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=hi
fetched_at: 2026-05-05T20:07:57.657083+00:00
title: "\u092a\u094d\u0930\u0949\u092e\u094d\u092a\u094d\u091f \u0921\u093f\u091c\u093c\u093e\u0907\u0928 \u0938\u0947 \u091c\u0941\u0921\u093c\u0940 \u0930\u0923\u0928\u0940\u0924\u093f\u092f\u093e\u0902 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# प्रॉम्प्ट डिज़ाइन से जुड़ी रणनीतियां

*प्रॉम्प्ट डिज़ाइन*, प्रॉम्प्ट या आम भाषा में किए गए अनुरोध बनाने की प्रोसेस है. इससे लैंग्वेज मॉडल से सटीक और अच्छी क्वालिटी के जवाब मिलते हैं.

इस पेज पर, बुनियादी अवधारणाओं, रणनीतियों, और सबसे सही तरीकों के बारे में बताया गया है. इनकी मदद से, Gemini के एआई मॉडल से ज़्यादा से ज़्यादा फ़ायदा पाने के लिए, प्रॉम्प्ट डिज़ाइन किए जा सकते हैं.

## विषय के हिसाब से प्रॉम्प्ट गाइड

क्या आपको प्रॉम्प्ट बनाने की ज़्यादा खास रणनीतियां चाहिए? इन विषयों पर प्रॉम्प्ट लिखने से जुड़ी हमारी अन्य गाइड देखें:

- [मीडिया फ़ाइलों का इस्तेमाल करके प्रॉम्प्ट देना](https://ai.google.dev/gemini-api/docs/files?hl=hi#prompt-guide)
- [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=hi#imagen-prompt-guide) और [Gemini की इमेज जनरेट करने की सुविधा](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi#prompt-guide) की मदद से इमेज जनरेट करने के लिए प्रॉम्प्ट देना
- [वीडियो जनरेट करने के लिए प्रॉम्प्ट देना](https://ai.google.dev/gemini-api/docs/video?hl=hi#prompt-guide)

आपको [प्रॉम्प्ट गैलरी](https://ai.google.dev/gemini-api/prompts?hl=hi) में अन्य सैंपल प्रॉम्प्ट मिल सकते हैं. इनका मकसद, इस गाइड में शेयर किए गए कई कॉन्सेप्ट को इंटरैक्टिव तरीके से दिखाना है.

## साफ़ और सटीक निर्देश

मॉडल के व्यवहार को अपनी ज़रूरत के हिसाब से बनाने का सबसे अच्छा तरीका यह है कि उसे साफ़ तौर पर और खास निर्देश दिए जाएं. निर्देश, किसी सवाल के तौर पर दिए जा सकते हैं. इसके अलावा, सिलसिलेवार तरीके से टास्क पूरे करने के लिए भी निर्देश दिए जा सकते हैं. साथ ही, उपयोगकर्ता के अनुभव और सोच को मैप करने जैसे मुश्किल निर्देश भी दिए जा सकते हैं.

### इनपुट

इनपुट, प्रॉम्प्ट में मौजूद वह ज़रूरी टेक्स्ट होता है जिसके बारे में आपको मॉडल से जवाब चाहिए. इनपुट, मॉडल से पूछा गया कोई सवाल (सवाल वाला इनपुट), मॉडल को दिया गया कोई टास्क (टास्क वाला इनपुट), मॉडल को दी गई कोई इकाई (इकाई वाला इनपुट) या मॉडल को दिया गया कोई अधूरा इनपुट (पूरा करने वाला इनपुट) हो सकता है.

| **इनपुट का टाइप** | **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- | --- |
| सवाल | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| टास्क | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| इकाई | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### इनपुट को कुछ हद तक पूरा करने की सुविधा

जनरेटिव लैंग्वेज मॉडल, अपने-आप पूरे होने की सुविधा देने वाले बेहतर टूल की तरह काम करते हैं. अधूरा कॉन्टेंट देने पर, मॉडल बाकी कॉन्टेंट या उस कॉन्टेंट को आगे बढ़ाने वाले कॉन्टेंट को जवाब के तौर पर दे सकता है. ऐसा करते समय, अगर आपने कोई उदाहरण या कॉन्टेक्स्ट शामिल किया है, तो मॉडल उन उदाहरणों या कॉन्टेक्स्ट को ध्यान में रख सकता है.

यहां दिए गए उदाहरण में, निर्देश और इकाई के इनपुट के साथ प्रॉम्प्ट दिया गया है:

|  |
| --- |
| **प्रॉम्प्ट:**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **जवाब:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

मॉडल ने प्रॉम्प्ट के मुताबिक जवाब दिया है. हालांकि, सामान्य भाषा में निर्देश लिखना कभी-कभी मुश्किल हो सकता है. साथ ही, इससे मॉडल को अपने हिसाब से जवाब देने का मौका मिल जाता है.
उदाहरण के लिए, किसी रेस्टोरेंट के मेन्यू में कई आइटम हो सकते हैं. JSON रिस्पॉन्स का साइज़ कम करने के लिए, आपको शायद उन आइटम को हटाना पड़े जिनका ऑर्डर नहीं दिया गया था. इस मामले में, उदाहरण और जवाब का प्रीफ़िक्स दिया जा सकता है. इसके बाद, मॉडल को जवाब पूरा करने दिया जा सकता है:

|  |
| --- |
| **प्रॉम्प्ट:**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **जवाब:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

ध्यान दें कि "चीज़बर्गर" को आउटपुट से हटा दिया गया है, क्योंकि यह ऑर्डर का हिस्सा नहीं था.

प्रॉम्प्ट का इस्तेमाल करके, सामान्य JSON रिस्पॉन्स ऑब्जेक्ट का फ़ॉर्मैट तय किया जा सकता है. हालांकि, हमारा सुझाव है कि रिस्पॉन्स के लिए ज़्यादा जटिल JSON स्कीमा तय करते समय, Gemini API की [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi) सुविधा का इस्तेमाल करें.

### कंस्ट्रेंट

प्रॉम्प्ट को पढ़ने या जवाब जनरेट करने से जुड़ी कोई भी पाबंदी बताएं. मॉडल को यह बताया जा सकता है कि उसे क्या करना है और क्या नहीं. उदाहरण के लिए, प्रॉम्प्ट में यह बताया जा सकता है कि आपको जवाब कितना लंबा चाहिए:

|  |
| --- |
| **प्रॉम्प्ट:**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **जवाब:**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### जवाब का फ़ॉर्मैट

जवाब के फ़ॉर्मैट के बारे में निर्देश दिए जा सकते हैं. उदाहरण के लिए, जवाब को टेबल, बुलेट वाली सूची, एलिवेटर पिच, कीवर्ड, वाक्य या पैराग्राफ़ के तौर पर फ़ॉर्मैट करने के लिए कहा जा सकता है. सिस्टम के इस निर्देश से, मॉडल को बातचीत के अंदाज़ में जवाब देने के लिए कहा गया है:

|  |
| --- |
| **सिस्टम के लिए निर्देश**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **प्रॉम्प्ट**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **जवाब:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### जवाबों को पूरा करने की रणनीति के हिसाब से फ़ॉर्मैट करना

[जवाब पूरा करने की रणनीति](#completion) से भी जवाब को फ़ॉर्मैट करने में मदद मिल सकती है.
यहां दिए गए उदाहरण में, मॉडल को निबंध की आउटलाइन बनाने के लिए कहा गया है:

|  |
| --- |
| **प्रॉम्प्ट:**    ``` Create an outline for an essay about hummingbirds. ```  **जवाब:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

प्रॉम्प्ट में, आउटलाइन का फ़ॉर्मैट नहीं बताया गया था. इसलिए, मॉडल ने आपके लिए कोई फ़ॉर्मैट चुना है. मॉडल से किसी खास फ़ॉर्मैट में आउटलाइन पाने के लिए, आउटलाइन की शुरुआत में टेक्स्ट जोड़ा जा सकता है. इसके बाद, मॉडल को उस पैटर्न के आधार पर आउटलाइन को पूरा करने दें जिसे आपने शुरू किया था.

|  |
| --- |
| **प्रॉम्प्ट:**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **जवाब:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## ज़ीरो-शॉट प्रॉम्प्ट बनाम फ़्यू-शॉट प्रॉम्प्ट

प्रॉम्प्ट में ऐसे उदाहरण शामिल किए जा सकते हैं जिनसे मॉडल को यह पता चले कि सही जवाब कैसा होता है. यह मॉडल, उदाहरणों से पैटर्न और संबंधों की पहचान करने की कोशिश करता है. साथ ही, जवाब जनरेट करते समय उन्हें लागू करता है. जिन प्रॉम्प्ट में कुछ उदाहरण दिए जाते हैं उन्हें *उदाहरण के साथ डाले गए प्रॉम्प्ट* कहा जाता है. वहीं, जिन प्रॉम्प्ट में कोई उदाहरण नहीं दिया जाता उन्हें *बिना उदाहरण वाले प्रॉम्प्ट* कहा जाता है. फ़्यू-शॉट प्रॉम्प्ट का इस्तेमाल अक्सर, मॉडल के जवाबों के फ़ॉर्मैट, शब्दों, स्कोप या सामान्य पैटर्न को कंट्रोल करने के लिए किया जाता है. मॉडल को ज़्यादा सटीक नतीजे जनरेट करने में मदद करने के लिए, अलग-अलग और खास उदाहरणों का इस्तेमाल करें.

हमारा सुझाव है कि आप अपने प्रॉम्प्ट में हमेशा कुछ उदाहरण शामिल करें. कुछ उदाहरणों के बिना दिए गए प्रॉम्प्ट ज़्यादा असरदार नहीं होते. अगर आपके उदाहरणों में टास्क को साफ़ तौर पर दिखाया गया है, तो प्रॉम्प्ट से निर्देशों को हटाया जा सकता है.

नीचे दिए गए ज़ीरो-शॉट प्रॉम्प्ट में, मॉडल से सबसे सही जवाब चुनने के लिए कहा गया है.

|  |
| --- |
| **प्रॉम्प्ट:**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **जवाब:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

अगर आपको मॉडल से छोटे जवाब चाहिए, तो प्रॉम्प्ट में ऐसे उदाहरण शामिल करें जिनमें छोटे जवाबों को प्राथमिकता दी गई हो.

नीचे दिए गए प्रॉम्प्ट में दो उदाहरण दिए गए हैं. इनमें छोटे जवाबों को प्राथमिकता दी गई है. जवाब में, यह देखा जा सकता है कि उदाहरणों की मदद से मॉडल को, लंबे जवाब (`Explanation1`) के बजाय छोटा जवाब (`Explanation2`) चुनने के लिए गाइड किया गया है. ऐसा पहले नहीं किया गया था.

|  |
| --- |
| **प्रॉम्प्ट:**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **जवाब:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### उदाहरणों की सही संख्या

Gemini जैसे मॉडल, कुछ उदाहरणों का इस्तेमाल करके पैटर्न का पता लगा सकते हैं. हालाँकि, बेहतर नतीजे पाने के लिए, आपको प्रॉम्प्ट में दिए जाने वाले उदाहरणों की संख्या के साथ एक्सपेरिमेंट करना पड़ सकता है. हालांकि, अगर बहुत ज़्यादा उदाहरण शामिल किए जाते हैं, तो मॉडल, उदाहरणों के हिसाब से जवाब देने के लिए [ओवरफ़िट](https://developers.google.com/machine-learning/glossary?hl=hi#overfitting) हो सकता है.

### एक ही तरह का फ़ॉर्मैट इस्तेमाल करना

पक्का करें कि कुछ उदाहरणों का स्ट्रक्चर और फ़ॉर्मैटिंग एक जैसी हो, ताकि आपको ऐसे जवाब न मिलें जो आपके काम के न हों. प्रॉम्प्ट में कुछ उदाहरण जोड़ने का मुख्य मकसद, मॉडल को जवाब का फ़ॉर्मैट दिखाना है. इसलिए, यह ज़रूरी है कि सभी उदाहरणों में एक जैसा फ़ॉर्मैट हो. खास तौर पर, एक्सएमएल टैग, व्हाइट स्पेस, नई लाइनें, और उदाहरणों को अलग करने वाले वर्णों पर ध्यान देना ज़रूरी है.

## संदर्भ जोड़ें

प्रॉम्प्ट में निर्देश और जानकारी शामिल की जा सकती है. इससे मॉडल को किसी समस्या को हल करने में मदद मिलती है. यह न मान लें कि मॉडल के पास सभी ज़रूरी जानकारी है. इस कॉन्टेक्स्ट वाली जानकारी से, मॉडल को उन सीमाओं और जानकारी को समझने में मदद मिलती है जिनके आधार पर आपको उससे काम करवाना है.

यहां दिए गए उदाहरण में, मॉडल से राउटर से जुड़ी समस्या हल करने के बारे में निर्देश देने के लिए कहा गया है:

|  |
| --- |
| **प्रॉम्प्ट:**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **जवाब:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

जवाब में समस्या हल करने के बारे में सामान्य जानकारी दी गई है. इसमें न तो राउटर के बारे में खास जानकारी दी गई है और न ही एलईडी इंडिकेटर लाइट की स्थिति के बारे में बताया गया है.

किसी खास राउटर के लिए जवाब को पसंद के मुताबिक बनाने के लिए, प्रॉम्प्ट में राउटर की समस्या हल करने से जुड़ी गाइड जोड़ें. इससे, जवाब देते समय राउटर को गाइड से मदद मिलेगी.

|  |
| --- |
| **प्रॉम्प्ट:**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **जवाब:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## प्रॉम्प्ट को कॉम्पोनेंट में बांटना

जिन मामलों में मुश्किल प्रॉम्प्ट की ज़रूरत होती है उनमें मॉडल को इस जटिलता को मैनेज करने में मदद की जा सकती है. इसके लिए, जानकारी को आसान कॉम्पोनेंट में तोड़ें.

1. **निर्देशों को अलग-अलग हिस्सों में बांटें:** एक ही प्रॉम्प्ट में कई निर्देश देने के बजाय, हर निर्देश के लिए अलग-अलग प्रॉम्प्ट बनाएं. आपके पास यह चुनने का विकल्प होता है कि उपयोगकर्ता के इनपुट के आधार पर, किस प्रॉम्प्ट को प्रोसेस करना है.
2. **चेन प्रॉम्प्ट:** ऐसे जटिल टास्क के लिए जिनमें एक के बाद एक कई चरण शामिल होते हैं,
   हर चरण को एक प्रॉम्प्ट बनाएं और प्रॉम्प्ट को एक क्रम में एक साथ जोड़ें. प्रॉम्प्ट की इस सीक्वेंशियल चेन में, क्रम में मौजूद किसी प्रॉम्प्ट का आउटपुट, अगले प्रॉम्प्ट का इनपुट बन जाता है. सीक्वेंस में मौजूद आखिरी प्रॉम्प्ट का आउटपुट, फ़ाइनल आउटपुट होता है.
3. **जवाबों को एग्रीगेट करना:** एग्रीगेशन तब किया जाता है, जब आपको डेटा के अलग-अलग हिस्सों पर अलग-अलग समानांतर टास्क करने हों. साथ ही, फ़ाइनल आउटपुट जनरेट करने के लिए, नतीजों को एग्रीगेट करना हो. उदाहरण के लिए, मॉडल को यह निर्देश दिया जा सकता है कि वह डेटा के पहले हिस्से पर एक ऑपरेशन करे, बाकी डेटा पर दूसरा ऑपरेशन करे, और फिर नतीजों को इकट्ठा करे.

## मॉडल के पैरामीटर आज़माना

मॉडल को भेजे जाने वाले हर कॉल में, पैरामीटर की वैल्यू शामिल होती हैं. इनसे यह कंट्रोल किया जाता है कि मॉडल जवाब कैसे जनरेट करे. मॉडल, पैरामीटर की अलग-अलग वैल्यू के लिए अलग-अलग नतीजे जनरेट कर सकता है. टास्क के लिए सबसे सही वैल्यू पाने के लिए, पैरामीटर की अलग-अलग वैल्यू आज़माएं. अलग-अलग मॉडल के लिए उपलब्ध पैरामीटर अलग-अलग हो सकते हैं. सबसे ज़्यादा इस्तेमाल किए जाने वाले पैरामीटर ये हैं:

1. **ज़्यादा से ज़्यादा आउटपुट टोकन:** इससे यह तय किया जाता है कि जवाब में ज़्यादा से ज़्यादा कितने टोकन जनरेट किए जा सकते हैं. एक टोकन में करीब चार वर्ण होते हैं. 100
   टोकन का मतलब करीब 60 से 80 शब्द होता है.
2. **तापमान:** तापमान से यह तय होता है कि टोकन को कितनी बार रैंडम तरीके से चुना जाएगा. जवाब जनरेट करने के दौरान, तापमान का इस्तेमाल सैंपलिंग के लिए किया जाता है. ऐसा तब होता है, जब `topP` और `topK` लागू किए जाते हैं. कम तापमान उन प्रॉम्प्ट के लिए अच्छा होता है जिनके लिए ज़्यादा सटीक या कम ओपन-एंडेड जवाब की ज़रूरत होती है. वहीं, ज़्यादा तापमान से अलग-अलग तरह के या क्रिएटिव नतीजे मिल सकते हैं. टेंपरेचर 0 होने का मतलब है कि जवाब तय होता है. इसका मतलब है कि सबसे ज़्यादा संभावना वाले जवाब को हमेशा चुना जाता है.
3. **`topK`:** `topK` पैरामीटर से, मॉडल के आउटपुट के लिए टोकन चुनने के तरीके में बदलाव होता है. `topK` की वैल्यू 1 होने का मतलब है कि मॉडल के शब्दावली में मौजूद सभी टोकन में से, चुना गया टोकन सबसे ज़्यादा संभावित है. इसे ग्रीडी डिकोडिंग भी कहा जाता है. वहीं, `topK` की वैल्यू 3 होने का मतलब है कि तापमान का इस्तेमाल करके, अगले टोकन को तीन सबसे संभावित टोकन में से चुना गया है. टोकन चुनने के हर चरण में, सबसे ज़्यादा संभावना वाले `topK` टोकन का सैंपल लिया जाता है. इसके बाद, टोकन को `topP` के आधार पर फ़िल्टर किया जाता है. आखिर में, तापमान के आधार पर सैंपलिंग करके टोकन चुना जाता है.
4. **`topP`:** `topP` पैरामीटर से, मॉडल के आउटपुट के लिए टोकन चुनने के तरीके में बदलाव होता है. टोकन, सबसे ज़्यादा से लेकर सबसे कम संभावना वाले क्रम में तब तक चुने जाते हैं, जब तक उनकी संभावनाओं का योग `topP` वैल्यू के बराबर न हो जाए. उदाहरण के लिए, अगर टोकन A, B, और C की संभावना 0.3, 0.2, और 0.1 है और `topP` की वैल्यू 0.5 है, तो मॉडल, तापमान का इस्तेमाल करके अगले टोकन के तौर पर A या B में से किसी एक को चुनेगा. साथ ही, C को उम्मीदवार के तौर पर शामिल नहीं करेगा. डिफ़ॉल्ट `topP` वैल्यू 0.95 है.
5. **`stop_sequences`:** मॉडल को कॉन्टेंट जनरेट करने से रोकने के लिए, स्टॉप सीक्वेंस सेट करें. स्टॉप सीक्वेंस, वर्णों का कोई भी सीक्वेंस हो सकता है. ऐसे वर्णों के क्रम का इस्तेमाल करने से बचें जो जनरेट किए गए कॉन्टेंट में दिख सकते हैं.

## प्रॉम्प्ट को बेहतर बनाने की रणनीतियां

कभी-कभी, आपको मनमुताबिक जवाब पाने के लिए, प्रॉम्प्ट डिज़ाइन को कुछ बार दोहराना पड़ सकता है. इस सेक्शन में, प्रॉम्प्ट को बेहतर बनाने के लिए कुछ सुझाव दिए गए हैं:

1. **अलग-अलग शब्दों का इस्तेमाल करें:** अपने प्रॉम्प्ट में अलग-अलग शब्दों या वाक्यांशों का इस्तेमाल करने से, मॉडल से अक्सर अलग-अलग जवाब मिलते हैं. भले ही, उन सभी का मतलब एक ही हो. अगर आपको अपने प्रॉम्प्ट के हिसाब से नतीजे नहीं मिल रहे हैं, तो उसे फिर से लिखें.

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **मिलते-जुलते टास्क पर स्विच करें:** अगर मॉडल किसी टास्क के लिए दिए गए आपके निर्देशों का पालन नहीं कर रहा है, तो उसे मिलते-जुलते किसी ऐसे टास्क के लिए निर्देश दें जिससे आपको वही नतीजा मिले.

   इस प्रॉम्प्ट से मॉडल को, पहले से तय की गई कैटगरी का इस्तेमाल करके किसी किताब को कैटगरी में बांटने के लिए कहा गया है:

   |  |
   | --- |
   | **प्रॉम्प्ट:**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **जवाब:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   जवाब सही है, लेकिन मॉडल ने विकल्पों की सीमा का पालन नहीं किया. आपको मॉडल से यह भी कहना है कि वह पूरे वाक्य में जवाब देने के बजाय, सिर्फ़ एक विकल्प के साथ जवाब दे. इस मामले में, निर्देशों को कई विकल्पों वाले सवाल के तौर पर फिर से लिखा जा सकता है. इसके बाद, मॉडल से कोई विकल्प चुनने के लिए कहा जा सकता है.

   |  |
   | --- |
   | **प्रॉम्प्ट:**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **जवाब:**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **प्रॉम्प्ट के कॉन्टेंट का क्रम बदलना:** कभी-कभी, प्रॉम्प्ट में कॉन्टेंट के क्रम से जवाब पर असर पड़ सकता है. कॉन्टेंट का क्रम बदलकर देखें और देखें कि इससे जवाब पर क्या असर पड़ता है.

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

## फ़ॉलबैक जवाब

फ़ॉलबैक जवाब, मॉडल से मिला ऐसा जवाब होता है जब प्रॉम्प्ट या जवाब, सुरक्षा फ़िल्टर को ट्रिगर करता है. फ़ॉलबैक जवाब का एक उदाहरण यह है: "मैं इसमें आपकी मदद नहीं कर सकता, क्योंकि मैं सिर्फ़ एक लैंग्वेज मॉडल हूँ."

अगर मॉडल फ़ॉलबैक जवाब देता है, तो तापमान बढ़ाएं.

## तथ्यों के साथ जवाब देना और कोड चलाना

Gemini, ऐसे मामलों में टूल का इस्तेमाल कर सकता है जहां वह गलत जवाब दे सकता है. इससे उसे भ्रमित करने वाली जानकारी से बचने में मदद मिलती है.

[Google Search से जानकारी पाने की सुविधा](https://ai.google.dev/gemini-api/docs/google-search?hl=hi), Gemini मॉडल को रीयल-टाइम वेब कॉन्टेंट से कनेक्ट करती है. इसे तब चालू किया जाना चाहिए, जब मॉडल को किसी विषय के बारे में कम जानकारी हो या उसे हाल ही के तथ्यों के बारे में जानना हो.

Gemini की [कोड एक्ज़ीक्यूशन टूल](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi) की मदद से, मॉडल Python कोड जनरेट और रन कर सकता है. इस टूल को तब चालू किया जाना चाहिए, जब मॉडल को किसी भी तरह की अंकगणित, गिनती या हिसाब-किताब करना हो.

## Gemini 3

[Gemini 3 मॉडल](https://ai.google.dev/gemini-api/docs/models?hl=hi#gemini-3) को, तर्क के साथ जवाब देने और निर्देशों का पालन करने के लिए डिज़ाइन किया गया है.
ये मॉडल, सीधे तौर पर पूछे गए सवालों के जवाब सबसे अच्छे तरीके से देते हैं. साथ ही, ये ऐसे सवालों के जवाब भी अच्छे से देते हैं जिनमें टास्क और किसी भी तरह की पाबंदियों के बारे में साफ़ तौर पर बताया गया हो. Gemini 3 से सबसे अच्छे नतीजे पाने के लिए, इन तरीकों का इस्तेमाल करें:

### प्रॉम्प्ट लिखने से जुड़े मुख्य सिद्धांत

- **सटीक और सीधे तौर पर जानकारी दें:** अपने लक्ष्य के बारे में साफ़ तौर पर और कम शब्दों में बताएं. ज़रूरत से ज़्यादा या बहुत ज़्यादा लुभावनी भाषा का इस्तेमाल न करें.
- **एक जैसा स्ट्रक्चर इस्तेमाल करें:** अपने प्रॉम्प्ट के अलग-अलग हिस्सों को अलग करने के लिए, साफ़ तौर पर सीमाएं तय करने वाले शब्दों का इस्तेमाल करें. एक्सएमएल स्टाइल वाले टैग (जैसे, `<context>`, `<task>`) या मार्कडाउन हेडिंग का इस्तेमाल करना फ़ायदेमंद होता है. कोई एक फ़ॉर्मैट चुनें और एक ही प्रॉम्प्ट में उसका लगातार इस्तेमाल करें.
- **पैरामीटर तय करना:** अस्पष्ट शब्दों या पैरामीटर के बारे में साफ़ तौर पर बताएं.
- **जवाब में शब्दों की संख्या को कंट्रोल करना:** डिफ़ॉल्ट रूप से, Gemini 3 मॉडल सीधे और असरदार जवाब देते हैं. अगर आपको बातचीत के लहजे में या ज़्यादा जानकारी वाला जवाब चाहिए, तो आपको निर्देशों में साफ़ तौर पर इसका अनुरोध करना होगा.
- **टेक्स्ट, इमेज, ऑडियो या वीडियो जैसे मल्टीमॉडल इनपुट को एक साथ प्रोसेस करना:** टेक्स्ट, इमेज, ऑडियो या वीडियो का इस्तेमाल करते समय, उन्हें एक जैसे इनपुट के तौर पर प्रोसेस करना. पक्का करें कि आपके निर्देशों में, ज़रूरत के हिसाब से हर मोडेलिटी का साफ़ तौर पर रेफ़रंस दिया गया हो.
- **ज़रूरी निर्देशों को प्राथमिकता दें:** व्यवहार से जुड़ी ज़रूरी पाबंदियों, भूमिका की परिभाषाओं (पर्सोना), और आउटपुट फ़ॉर्मैट की ज़रूरी शर्तों को सिस्टम के निर्देश में या उपयोगकर्ता के प्रॉम्प्ट की शुरुआत में रखें.
- **ज़्यादा जानकारी वाले कॉन्टेक्स्ट के लिए स्ट्रक्चर:** ज़्यादा जानकारी (जैसे, दस्तावेज़, कोड) देते समय, सबसे पहले पूरी जानकारी दें. अपने खास निर्देशों या सवालों को प्रॉम्प्ट के *आखिर* में रखें.
- **एंकर कॉन्टेक्स्ट:** डेटा के बड़े ब्लॉक के बाद, कॉन्टेक्स्ट और अपनी क्वेरी के बीच अंतर को कम करने के लिए, ट्रांज़िशन फ़्रेज़ का इस्तेमाल करें. जैसे, "ऊपर दी गई जानकारी के आधार पर..."

### Gemini 3 Flash की रणनीतियां

- **आज की तारीख के हिसाब से सही जवाब देने की क्षमता:** सिस्टम को निर्देश देते समय, यह क्लॉज़ जोड़ें. इससे मॉडल को यह ध्यान रखने में मदद मिलेगी कि आज की तारीख 2026 की है:

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **जानकारी के अपडेट होने की तारीख के बारे में सटीक जानकारी:** सिस्टम को दिए जाने वाले निर्देशों में यह क्लॉज़ जोड़ें, ताकि मॉडल को जानकारी के अपडेट होने की तारीख के बारे में पता चल सके:

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **जवाब में भरोसेमंद स्रोतों से मिली जानकारी शामिल करने की क्षमता:** सिस्टम के निर्देशों में यह क्लॉज़ जोड़ें. इसमें ज़रूरत के हिसाब से बदलाव करें, ताकि मॉडल, दिए गए कॉन्टेक्स्ट के आधार पर जवाब दे सके:

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

### तर्क करने और प्लान बनाने की क्षमता को बेहतर बनाना

Gemini 2.5 और 3 सीरीज़ के मॉडल, तर्क करने की परफ़ॉर्मेंस को बेहतर बनाने के लिए, अपने-आप इंटरनल "थिंकिंग" टेक्स्ट जनरेट करते हैं. इसलिए, आम तौर पर यह ज़रूरी नहीं है कि मॉडल, जवाब में ही आउटलाइन, प्लान या तर्क के चरणों की जानकारी दे. जिन समस्याओं के लिए ज़्यादा तर्क की ज़रूरत होती है उनके लिए, "जवाब देने से पहले बहुत सोच-विचार करो" जैसे सामान्य अनुरोधों से परफ़ॉर्मेंस को बेहतर बनाया जा सकता है. हालांकि, इसके लिए ज़्यादा थिंकिंग टोकन खर्च करने पड़ सकते हैं.

ज़्यादा जानकारी के लिए, [Gemini के सोचने के तरीके](https://ai.google.dev/gemini-api/docs/thinking?hl=hi) से जुड़ा दस्तावेज़ देखें.

### स्ट्रक्चर्ड प्रॉम्प्ट के उदाहरण

टैग या Markdown का इस्तेमाल करने से, मॉडल को निर्देशों, कॉन्टेक्स्ट, और टास्क के बीच अंतर करने में मदद मिलती है.

**एक्सएमएल का उदाहरण:**

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

**मार्कडाउन का उदाहरण:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### सबसे सही तरीकों को मिलाकर बनाए गए टेंप्लेट का उदाहरण

इस टेंप्लेट में, Gemini 3 के साथ प्रॉम्प्ट करने के मुख्य सिद्धांतों के बारे में बताया गया है. हमेशा
अपनी ज़रूरत के हिसाब से प्रॉम्प्ट में बदलाव करें.

**सिस्टम के लिए निर्देश:**

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

**उपयोगकर्ता का प्रॉम्प्ट:**

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

## एजेंट की तरह काम करने वाले वर्कफ़्लो

एजेंट के तौर पर काम करने वाले डीप वर्कफ़्लो के लिए, अक्सर खास निर्देशों की ज़रूरत होती है. इनसे यह कंट्रोल किया जा सकता है कि मॉडल कैसे तर्क देता है, प्लान बनाता है, और टास्क पूरे करता है. Gemini, सामान्य तौर पर अच्छा परफ़ॉर्म करता है. हालांकि, जटिल एजेंट के लिए, आपको कंप्यूटेशनल लागत (लेटेंसी और टोकन) और टास्क की सटीकता के बीच ट्रेड-ऑफ़ कॉन्फ़िगर करना होता है.

एजेंट के लिए प्रॉम्प्ट डिज़ाइन करते समय, व्यवहार के इन डाइमेंशन को ध्यान में रखें. इनकी मदद से, एजेंट के व्यवहार को कंट्रोल किया जा सकता है:

### रीज़निंग और रणनीति

यह कॉन्फ़िगरेशन, कार्रवाई करने से पहले मॉडल के सोचने और प्लान बनाने के तरीके के बारे में बताता है.

- **लॉजिकल डीकंपोज़िशन:** इससे यह तय होता है कि मॉडल को, शर्तों, ज़रूरी शर्तों, और कार्रवाइयों के क्रम का कितना बारीकी से विश्लेषण करना चाहिए.
- **समस्या का पता लगाना**: यह विकल्प, समस्याओं की वजहों का पता लगाने के लिए विश्लेषण की गहराई को कंट्रोल करता है. साथ ही, यह मॉडल के अनुमान लगाने के तरीके को भी कंट्रोल करता है. इससे यह तय होता है कि मॉडल को सबसे सही जवाब स्वीकार करना चाहिए या मुश्किल और कम संभावित जवाबों को एक्सप्लोर करना चाहिए.
- **जानकारी की पूरी उपलब्धता:** उपलब्ध हर नीति और दस्तावेज़ का विश्लेषण करने के बीच, दक्षता और तेज़ी को प्राथमिकता देने का फ़ायदा.

### एक्ज़ीक्यूशन और विश्वसनीयता

इस कॉन्फ़िगरेशन से यह तय होता है कि एजेंट, अपने-आप कैसे काम करेगा और समस्याओं को कैसे हल करेगा.

- **अनुकूलन क्षमता:** मॉडल नए डेटा पर कैसे काम करता है. इससे यह तय होता है कि इसे अपने शुरुआती प्लान पर बने रहना चाहिए या जब अनुमानों से अलग नतीजे मिलते हैं, तो तुरंत बदलाव करना चाहिए.
- **गड़बड़ियों को ठीक करने की क्षमता:** मॉडल, गड़बड़ियों को खुद ठीक करने की कितनी कोशिश करता है. टोकन को लंबे समय तक सेव रखने से, सफलता की दर बढ़ जाती है. हालांकि, इससे टोकन की लागत बढ़ सकती है या लूप बन सकते हैं.
- **जोखिम का आकलन:** नतीजों का आकलन करने का लॉजिक. यह कम जोखिम वाले एक्सप्लोरेटरी ऐक्शन (पढ़ना) और ज़्यादा जोखिम वाले स्टेट चेंज (लिखना) के बीच अंतर करता है.

### इंटरैक्शन और आउटपुट

इस कॉन्फ़िगरेशन से यह तय होता है कि एजेंट, उपयोगकर्ता से कैसे कम्यूनिकेट करेगा और नतीजों को कैसे फ़ॉर्मैट करेगा.

- **अस्पष्टता और अनुमति मैनेज करना:** इससे यह तय होता है कि मॉडल को कब अनुमान लगाने की अनुमति है और कब उसे उपयोगकर्ता से अनुमति या जानकारी मांगने के लिए, कार्रवाई को रोकना होगा.
- **ज़्यादा जानकारी देना:** इससे टूल कॉल के साथ जनरेट किए गए टेक्स्ट की आवाज़ को कंट्रोल किया जाता है. इससे यह तय होता है कि मॉडल, उपयोगकर्ता को अपनी कार्रवाइयों के बारे में बताएगा या कार्रवाई करते समय चुप रहेगा.
- **सटीकता और पूरी जानकारी:** आउटपुट में ज़रूरी जानकारी का सटीक होना. इससे यह तय होता है कि मॉडल को हर मुश्किल समस्या को हल करना है और सटीक आंकड़े देने हैं या अनुमानित आंकड़े स्वीकार किए जा सकते हैं.

### सिस्टम के निर्देशों का टेंप्लेट

यहां दिए गए सिस्टम के निर्देश का उदाहरण, शोधकर्ताओं ने एआई एजेंट के लिए तय किए गए बेंचमार्क पर परफ़ॉर्मेंस को बेहतर बनाने के लिए तैयार किया है. इसमें मॉडल को नियमों की जटिल किताब का पालन करना होता है और उपयोगकर्ता के साथ इंटरैक्ट करना होता है. इससे एजेंट को बेहतर तरीके से सोचने और प्लान बनाने में मदद मिलती है. साथ ही, ऊपर बताए गए डाइमेंशन के हिसाब से खास व्यवहार लागू करने में मदद मिलती है. इसके अलावा, मॉडल को कोई भी कार्रवाई करने से पहले, प्लान बनाने की ज़रूरत होती है.

इस टेंप्लेट को, अपने इस्तेमाल के उदाहरण की खास शर्तों के हिसाब से बदला जा सकता है.

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

## अगले चरण

- अब आपको प्रॉम्प्ट डिज़ाइन के बारे में ज़्यादा जानकारी मिल गई है. इसलिए, [Google AI Studio](http://aistudio.google.com?hl=hi) का इस्तेमाल करके, अपने प्रॉम्प्ट लिखें.
- मल्टीमॉडल प्रॉम्प्टिंग के बारे में जानने के लिए, [मीडिया फ़ाइलों के साथ प्रॉम्प्ट करना](https://ai.google.dev/gemini-api/docs/files?hl=hi#prompt-guide) लेख पढ़ें.
- इमेज प्रॉम्प्ट के बारे में जानने के लिए, [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi#prompt-guide) और [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=hi#imagen-prompt-guide) के प्रॉम्प्ट से जुड़े दिशा-निर्देश देखें.
- वीडियो प्रॉम्प्टिंग के बारे में जानने के लिए, [Veo की प्रॉम्प्ट गाइड](https://ai.google.dev/gemini-api/docs/video?hl=hi#prompt-guide) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-04-29 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-04-29 (UTC) को अपडेट किया गया."],[],[]]
