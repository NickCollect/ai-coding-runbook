---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=tr
fetched_at: 2026-06-29T05:33:10.370895+00:00
title: "H\u0131zl\u0131 tasar\u0131m stratejileri \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Hızlı tasarım stratejileri

*İstem tasarımı*, dil modelinden doğru ve yüksek kaliteli yanıtlar alınmasını sağlayan istemler veya doğal dil istekleri oluşturma sürecidir.

Bu sayfada, Gemini yapay zeka modellerinden en iyi şekilde yararlanmak için istem tasarlamaya başlamanıza yardımcı olacak temel kavramlar, stratejiler ve en iyi uygulamalar tanıtılmaktadır.

## Konuya özel istem kılavuzları

Daha spesifik istem stratejileri mi arıyorsunuz? Aşağıdaki konularda diğer istem kılavuzlarımıza göz atın:

- [Medya dosyalarıyla istem oluşturma](https://ai.google.dev/gemini-api/docs/files?hl=tr#prompt-guide)
- [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=tr#imagen-prompt-guide) ve [Gemini Native Image Generation](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr#prompt-guide) ile görüntü üretme istemleri
- [Video üretimi için istem girme](https://ai.google.dev/gemini-api/docs/video?hl=tr#prompt-guide)

Bu kılavuzda paylaşılan birçok kavramı etkileşimli olarak sergilemek için tasarlanan [istem galerisinde](https://ai.google.dev/gemini-api/prompts?hl=tr) diğer örnek istemleri bulabilirsiniz.

## Net ve spesifik talimatlar

Model davranışını özelleştirmenin etkili ve verimli bir yolu, modele net ve spesifik talimatlar vermektir. Talimatlar soru, adım adım görevler şeklinde veya kullanıcının deneyimini ve düşünce yapısını haritalandırmak kadar karmaşık olabilir.

### Giriş

Giriş, istemde modelin yanıt vermesini istediğiniz zorunlu metindir. Girişler; modelin yanıtladığı bir soru (soru girişi), modelin gerçekleştirdiği bir görev (görev girişi), modelin üzerinde işlem yaptığı bir varlık (varlık girişi) veya modelin tamamladığı ya da devam ettirdiği kısmi giriş (tamamlama girişi) olabilir.

| **Giriş türü** | **İstem** | **Üretilen çıkış** |
| --- | --- | --- |
| Soru | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| Görev | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| Varlık | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### Kısmi giriş tamamlama

Üretken dil modelleri, gelişmiş bir otomatik tamamlama aracı gibi çalışır. Kısmi içerik sağladığınızda model, içeriğin geri kalanını veya içeriğin devamı olduğunu düşündüğü kısmı yanıt olarak verebilir. Bunu yaparken örnek veya bağlam eklerseniz model bu örnekleri ya da bağlamı dikkate alabilir.

Aşağıdaki örnekte, talimat ve öğe girişi içeren bir istem sağlanmaktadır:

|  |
| --- |
| **İstem:**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **Yanıt:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

Model, isteneni yapmasına rağmen talimatları doğal dilde yazmak bazen zor olabilir ve modelin yorumuna çok şey bırakır.
Örneğin, bir restoranın menüsünde birçok öğe olabilir. JSON yanıtının boyutunu küçültmek için sipariş edilmeyen öğeleri atlamak isteyebilirsiniz. Bu durumda, bir örnek ve yanıt öneki verebilir, modelin bunu tamamlamasına izin verebilirsiniz:

|  |
| --- |
| **İstem:**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **Yanıt:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

"Cheeseburger"ın siparişin bir parçası olmadığı için çıkıştan nasıl hariç tutulduğuna dikkat edin.

Basit JSON yanıt nesnelerinin biçimini istemleri kullanarak belirtebilseniz de yanıt için daha karmaşık bir JSON şeması belirtirken Gemini API'nin [yapılandırılmış çıkış](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr) özelliğini kullanmanızı öneririz.

### Sınırlamalar

İstemin okunması veya yanıt oluşturulmasıyla ilgili kısıtlamaları belirtin. Modele ne yapıp ne yapmaması gerektiğini söyleyebilirsiniz. Örneğin, istemde özetin ne kadar uzun olmasını istediğinize dair bir kısıtlama belirtebilirsiniz:

|  |
| --- |
| **İstem:**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **Yanıt:**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### Yanıt biçimi

Yanıtın biçimini belirten talimatlar verebilirsiniz. Örneğin, yanıtın tablo, madde işaretli liste, kısa tanıtım, anahtar kelimeler, cümle veya paragraf olarak biçimlendirilmesini isteyebilirsiniz. Aşağıdaki sistem talimatı, modele yanıtında daha sohbet tarzında olmasını söylüyor:

|  |
| --- |
| **Sistem talimatı**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **İstem**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **Yanıt:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### Tamamlama stratejisiyle yanıtları biçimlendirme

[Tamamlama stratejisi](#completion), yanıtın biçimlendirilmesine de yardımcı olabilir.
Aşağıdaki örnekte, modelden bir deneme taslağı oluşturması isteniyor:

|  |
| --- |
| **İstem:**    ``` Create an outline for an essay about hummingbirds. ```  **Yanıt:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

İstemde taslağın biçimi belirtilmediği için model sizin için bir biçim seçti. Modelin belirli bir biçimde taslak döndürmesini sağlamak için taslağın başlangıcını temsil eden metin ekleyebilir ve başlattığınız kalıba göre modeli tamamlayabilirsiniz.

|  |
| --- |
| **İstem:**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **Yanıt:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## Sıfır görevli ve çok görevli istemler

İstemde, modelin doğru yanıtın nasıl göründüğünü anlamasına yardımcı olacak örnekler ekleyebilirsiniz. Model, örneklerdeki kalıpları ve ilişkileri belirlemeye çalışır ve yanıt oluştururken bunları uygular. Birkaç örnek içeren istemlere *az görevli* istemler, örnek içermeyen istemlere ise *sıfır görevli* istemler denir. Az görevli istemler genellikle model yanıtlarının biçimlendirmesini, ifade biçimini, kapsamını veya genel kalıbını düzenlemek için kullanılır. Modelin odak noktasını daraltmasına ve daha doğru sonuçlar üretmesine yardımcı olmak için spesifik ve çeşitli örnekler kullanın.

İstemlerinize her zaman birkaç görevli örnek eklemenizi öneririz. Az görevli örnekler içermeyen istemlerin etkili olma olasılığı daha düşüktür. Hatta örnekleriniz, söz konusu görevi gösterme konusunda yeterince netse isteminizden talimatları kaldırabilirsiniz.

Aşağıdaki sıfır görevli istemde modelden en iyi açıklamayı seçmesi isteniyor.

|  |
| --- |
| **İstem:**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Yanıt:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

Kullanım alanınızda modelin kısa yanıtlar üretmesi gerekiyorsa isteme kısa yanıtları tercih eden örnekler ekleyebilirsiniz.

Aşağıdaki istemde, daha kısa açıklamalara öncelik verildiğini gösteren iki örnek yer alıyor. Yanıtta, örneklerin modeli daha önce yaptığı gibi daha uzun açıklama (`Explanation1`) yerine daha kısa açıklamayı (`Explanation2`) seçmeye yönlendirdiği görülüyor.

|  |
| --- |
| **İstem:**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Yanıt:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### İdeal örnek sayısı

Gemini gibi modeller, birkaç örnek kullanarak kalıpları tespit edebilir. Ancak en iyi sonuçları elde etmek için istemde sağlanan örneklerin sayısıyla denemeler yapmanız gerekebilir. Aynı zamanda, çok fazla örnek eklerseniz model, yanıtı örneklere [aşırı uydurmaya](https://developers.google.com/machine-learning/glossary?hl=tr#overfitting) başlayabilir.

### Tutarlı format

İstenmeyen biçimlerde yanıtlar almamak için birkaç görevli örneklerin yapısının ve biçimlendirmesinin aynı olduğundan emin olun. İstemlere birkaç görevli örnek eklemenin temel amaçlarından biri, modele yanıt biçimini göstermektir. Bu nedenle, özellikle XML etiketlerine, boşluklara, yeni satırlara ve örnek ayırıcılara dikkat ederek tüm örneklerde tutarlı bir biçim sağlamak önemlidir.

## Bağlam bilgisi ekleyin

Modelin gerekli tüm bilgilere sahip olduğunu varsaymak yerine, bir isteme talimatlar ve bilgiler ekleyerek modelin bir sorunu çözmesini sağlayabilirsiniz. Bu bağlamsal bilgiler, modelin istediğiniz işle ilgili kısıtlamaları ve ayrıntıları anlamasına yardımcı olur.

Aşağıdaki örnekte, modelden bir yönlendiriciyle ilgili sorun giderme talimatları vermesi isteniyor:

|  |
| --- |
| **İstem:**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **Yanıt:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

Yanıtta, yönlendiriciye veya LED gösterge ışıklarının durumuna özgü olmayan genel sorun giderme bilgileri yer alıyor.

Yanıtı belirli bir yönlendirici için özelleştirmek istiyorsanız isteme, yanıt verirken başvurması için yönlendiricinin sorun giderme kılavuzunu bağlam olarak ekleyebilirsiniz.

|  |
| --- |
| **İstem:**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **Yanıt:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## İstemleri bileşenlere ayırma

Karmaşık istemler gerektiren kullanım alanlarında, öğeleri daha basit bileşenlere ayırarak modelin bu karmaşıklığı yönetmesine yardımcı olabilirsiniz.

1. **Talimatları bölme:** Tek bir istemde çok sayıda talimat vermek yerine her talimat için ayrı bir istem oluşturun. Kullanıcının girişine göre hangi istemin işleneceğini seçebilirsiniz.
2. **İstemleri zincirleme:** Sıralı birden fazla adım içeren karmaşık görevler için her adımı istem olarak girin ve istemleri bir sırayla zincirleyin. Bu sıralı istem zincirinde, dizideki bir istemin çıkışı bir sonraki istemin girişi olur. Dizideki son istemin çıkışı, nihai çıkıştır.
3. **Yanıtları toplama:** Toplama, verilerin farklı bölümlerinde farklı paralel görevler gerçekleştirmek ve sonuçları toplayarak nihai çıktıyı oluşturmak istediğinizde yapılır. Örneğin, modele verilerin ilk bölümünde bir işlem, verilerin geri kalanında başka bir işlem yapmasını ve sonuçları toplamasını söyleyebilirsiniz.

## Model parametreleriyle denemeler yapma

Bir modele gönderdiğiniz her çağrı, modelin nasıl yanıt üreteceğini kontrol eden parametre değerleri içerir. Model, farklı parametre değerleri için farklı sonuçlar üretebilir. Görev için en iyi değerleri elde etmek üzere farklı parametre değerleriyle denemeler yapın. Farklı modeller için kullanılabilen parametreler farklı olabilir. En yaygın parametreler şunlardır:

1. **Maksimum çıkış jetonu sayısı:** Yanıtta oluşturulabilecek maksimum jeton sayısını belirtir. Bir jeton, yaklaşık dört karakterden oluşur. 100 jeton yaklaşık 60-80 kelimeye denk gelir.
2. **Sıcaklık:** Sıcaklık, jeton seçimindeki rastgelelik derecesini kontrol eder. Sıcaklık, yanıt üretimi sırasında örnekleme için kullanılır. Bu işlem, `topP` ve `topK` uygulandığında gerçekleşir. Düşük sıcaklıklar, daha kontrollü veya daha az açık uçlu yanıt gerektiren istemler için tercih edilir. Yüksek sıcaklıklar ise daha çeşitli veya yaratıcı sonuçlar sunabilir. Sıcaklık 0 olduğunda her zaman en yüksek olasılıklı yanıt seçilir.
3. **`topK`:** `topK` parametresi, modelin çıkış için jetonları nasıl seçeceğini değiştirir. `topK` değeri 1 olduğunda, seçilen jeton modelin sözlüğündeki tüm jetonlar arasında en olası olanıdır (açgözlü kod çözme olarak da adlandırılır). `topK` değeri 3 olduğunda ise bir sonraki jeton, sıcaklık kullanılarak en olası 3 jeton arasından seçilir. Her jeton seçme adımında, en yüksek olasılıklara sahip `topK` jeton örneklenir. Jetonlar daha sonra `topP`'ye göre daha da filtrelenir ve son jeton, sıcaklık örnekleme kullanılarak seçilir.
4. **`topP`:** `topP` parametresi, modelin çıkış için jetonları nasıl seçeceğini değiştirir. Jetonlar, olasılıklarının toplamı `topP` değerine eşit olana kadar en olasıdan en az olasıya doğru seçilir. Örneğin, A, B ve C jetonlarının olasılığı 0,3, 0,2 ve 0,1 ise ve `topP` değeri 0,5 ise model, sıcaklığı kullanarak sonraki jeton olarak A veya B'yi seçer ve C'yi aday olarak hariç tutar. Varsayılan `topP` değeri 0,95'tir.
5. **`stop_sequences`:** Modeli içerik oluşturmayı durdurmaya yönlendirmek için durdurma sırası ayarlayın. Durdurma dizisi herhangi bir karakter dizisi olabilir. Oluşturulan içerikte görünebilecek karakter dizilerini kullanmaktan kaçının.

## İstem tekrarlama stratejileri

İstemin tasarımı, istediğiniz yanıtı tutarlı bir şekilde almadan önce bazen birkaç yineleme gerektirebilir. Bu bölümde, istemlerinizi yinelerken deneyebileceğiniz bazı yöntemler hakkında bilgi verilmektedir:

1. **Farklı ifadeler kullanın:** İstemlerinizde farklı kelimeler veya ifadeler kullanmak, aynı anlama gelseler bile modelden genellikle farklı yanıtlar almanızı sağlar. İsteminizden beklediğiniz sonuçları alamıyorsanız isteminizi yeniden ifade etmeyi deneyin.

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **Benzer bir göreve geçin:** Modelin bir görevle ilgili talimatlarınızı uygulamasını sağlayamıyorsanız aynı sonucu veren benzer bir görevle ilgili talimatlar vermeyi deneyin.

   Bu istemde, modelden önceden tanımlanmış kategorileri kullanarak bir kitabı sınıflandırması isteniyor:

   |  |
   | --- |
   | **İstem:**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **Yanıt:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   Yanıt doğru ancak model, seçeneklerin sınırları içinde kalmadı. Ayrıca, modelin tam cümleyle yanıt vermek yerine yalnızca seçeneklerden birini kullanarak yanıt vermesini istiyorsunuz. Bu durumda, talimatları çoktan seçmeli soru olarak yeniden ifade edebilir ve modelden bir seçenek belirlemesini isteyebilirsiniz.

   |  |
   | --- |
   | **İstem:**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **Yanıt:**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **İstem içeriğinin sırasını değiştirme:** İstemdeki içeriğin sırası bazen yanıtı etkileyebilir. İçerik sırasını değiştirmeyi deneyin ve bunun yanıtı nasıl etkilediğini görün.

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

## Yedek yanıtlar

Yedek yanıt, istem veya yanıt bir güvenlik filtresini tetiklediğinde model tarafından döndürülen yanıttır. Yedek yanıta örnek olarak "Yalnızca bir dil modeli olduğum için bu konuda yardımcı olamıyorum." verilebilir.

Model, yedek yanıtla karşılık veriyorsa sıcaklığı artırmayı deneyin.

## Temellendirme ve kod yürütme

Gemini, aksi takdirde yanlış yanıtlar verebileceği senaryolarda halüsinasyonları önlemek için araçları kullanabilir.

[Google Arama ile Temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr), Gemini modelini gerçek zamanlı web içeriğine bağlar ve modelin belirsiz veya güncel bilgileri bilmesi gerektiğinde etkinleştirilmelidir.

Gemini'ın [kod yürütme aracı](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr), modelin Python kodu oluşturup çalıştırmasını sağlar ve modelin herhangi bir aritmetik, sayma veya hesaplama işlemi yapması gerektiğinde etkinleştirilmelidir.

## Gemini 3

[Gemini 3 modelleri](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-3), gelişmiş akıl yürütme ve talimatları uygulama için tasarlanmıştır.
Bu modeller, doğrudan, iyi yapılandırılmış ve görevi ve kısıtlamaları net bir şekilde tanımlayan istemlere en iyi yanıtı verir. Gemini 3 ile en iyi sonuçları almak için aşağıdaki uygulamalar önerilir:

### Temel istem ilkeleri

- **Net ve doğrudan olun:** Hedefinizi açık ve kısa bir şekilde belirtin. Gereksiz veya aşırı ikna edici dil kullanmaktan kaçının.
- **Tutarlı bir yapı kullanın:** İsteminizin farklı bölümlerini ayırmak için net sınırlayıcılar kullanın. XML tarzı etiketler (ör. `<context>`, `<task>`) veya Markdown başlıkları etkili olur. Tek bir istemde tutarlı bir şekilde kullanmak için bir biçim seçin.
- **Parametreleri tanımlayın:** Belirsiz terimleri veya parametreleri açıkça açıklayın.
- **Çıkış ayrıntı düzeyini kontrol etme:** Gemini 3 modelleri varsayılan olarak doğrudan ve verimli yanıtlar verir. Daha sohbet tarzında veya ayrıntılı bir yanıt istiyorsanız talimatlarınızda bunu açıkça belirtmeniz gerekir.
- **Çok formatlı girişleri tutarlı bir şekilde işleme:** Metin, resim, ses veya video kullanırken bunları eşit sınıf girişler olarak ele alın. Talimatlarınızda her bir yönteme gerektiği şekilde açıkça atıfta bulunduğunuzdan emin olun.
- **Önemli talimatlara öncelik verin:** Temel davranışsal kısıtlamaları, rol tanımlarını (persona) ve çıkış biçimi gereksinimlerini Sistem Talimatı'na veya kullanıcı isteminin en başına yerleştirin.
- **Uzun bağlamlar için yapı:** Büyük miktarda bağlam (ör. dokümanlar, kod) sağlarken önce tüm bağlamı sağlayın. Belirli talimatlarınızı veya sorularınızı istemin en *sonuna* yerleştirin.
- **Bağlamı sabitleme:** Büyük bir veri bloğundan sonra, bağlam ile sorgunuz arasında köprü kurmak için net bir geçiş ifadesi kullanın. Örneğin, "Yukarıdaki bilgilere göre..."

### Gemini 3 Flash stratejileri

- **Güncel gün doğruluğu:** Modelin, güncel günün 2026'da olduğuna dikkat etmesine yardımcı olmak için sistem talimatlarına aşağıdaki maddeyi ekleyin:

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **Son güncel bilgi tarihi doğruluğu:** Modeli son güncel bilgi tarihi konusunda bilgilendirmek için sistem talimatlarına aşağıdaki tümceyi ekleyin:

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **Temellendirme performansı:** Modelin yanıtları sağlanan bağlamda temellendirme becerisini artırmak için sistem talimatlarına aşağıdaki ifadeyi ekleyin (gerekli yerlerde düzenlemeler yaparak):

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

### Akıl yürütme ve planlamayı geliştirme

Gemini 2.5 ve 3 serisi modeller, akıl yürütme performansını artırmak için otomatik olarak dahili "düşünme" metni oluşturur. Bu nedenle, döndürülen yanıtta modelin ana hatlarını, planını veya ayrıntılı gerekçelendirme adımlarını belirtmek genellikle gerekli değildir. Yoğun muhakeme gerektiren sorunlarda, "Yanıt vermeden önce çok iyi düşün" gibi basit istekler, ek düşünme jetonları karşılığında performansı artırabilir.

Daha fazla ayrıntı için [Gemini düşünme süreci](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) dokümanlarını inceleyin.

### Yapılandırılmış istem örnekleri

Etiket veya Markdown kullanmak, modelin talimatlar, bağlam ve görevler arasında ayrım yapmasına yardımcı olur.

**XML örneği:**

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

**Markdown örneği:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### En iyi uygulamaları birleştiren örnek şablon

Bu şablon, Gemini 3 ile istem yazmayla ilgili temel ilkeleri içerir. Kullanım alanınıza göre her zaman yineleme ve değişiklik yapmayı unutmayın.

**Sistem Talimatı:**

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

**Kullanıcı İstemi:**

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

## Temsilci tabanlı iş akışları

Derin etkileşimli iş akışlarında, modelin görevleri nasıl gerekçelendireceğini, planlayacağını ve yürüteceğini kontrol etmek için genellikle belirli talimatlar gerekir. Gemini genel olarak güçlü bir performans sunsa da karmaşık ajanlar genellikle hesaplama maliyeti (gecikme ve jetonlar) ile görev doğruluğu arasındaki dengeyi yapılandırmanızı gerektirir.

Ajanlar için istem tasarlarken ajanda yönlendirebileceğiniz aşağıdaki davranış boyutlarını göz önünde bulundurun:

### Muhakeme ve strateji

Modelin işlem yapmadan önce nasıl düşüneceği ve planlayacağıyla ilgili yapılandırma.

- **Mantıksal ayrıştırma:** Modelin kısıtlamaları, ön koşulları ve işlem sırasını ne kadar ayrıntılı bir şekilde analiz etmesi gerektiğini tanımlar.
- **Sorun teşhisi**: Nedenler belirlenirken analiz derinliğini ve modelin abdüktif akıl yürütme kullanımını kontrol eder. Modelin en belirgin cevabı kabul edip etmeyeceğini veya karmaşık, daha az olası açıklamaları inceleyip incelemeyeceğini belirler.
- **Bilgi kapsamlılığı:** Mevcut her politikayı ve belgeyi analiz etmek ile verimliliğe ve hıza öncelik vermek arasındaki denge.

### Yürütme ve güvenilirlik

Ajanın bağımsız olarak çalışması ve engelleri aşmasıyla ilgili yapılandırma.

- **Uyarlanabilirlik:** Modelin yeni verilere nasıl tepki verdiği. Başlangıç planına sıkı sıkıya bağlı kalıp kalmayacağını veya gözlemler varsayımlarla çeliştiğinde hemen değişip değişmeyeceğini belirler.
- **Kalıcılık ve Kurtarma:** Modelin hataları kendi kendine düzeltme girişimi. Yüksek kalıcılık, başarı oranlarını artırır ancak daha yüksek jeton maliyetleri veya döngüler riski taşır.
- **Risk Değerlendirmesi:** Sonuçları değerlendirme mantığı. Düşük riskli keşif işlemleri (okuma) ile yüksek riskli durum değişiklikleri (yazma) arasında açıkça ayrım yapar.

### Etkileşim ve çıktı

Ajanın kullanıcıyla nasıl iletişim kuracağı ve sonuçları nasıl biçimlendireceğiyle ilgili yapılandırma.

- **Belirsizlik ve izin işleme:** Modelin ne zaman varsayımda bulunmasına izin verildiğini, ne zaman yürütmeyi duraklatıp kullanıcıdan açıklama veya izin istemesi gerektiğini tanımlar.
- **Ayrıntı düzeyi:** Araç çağrılarıyla birlikte oluşturulan metinlerin hacmini kontrol eder. Bu, modelin işlemlerini kullanıcıya açıklayıp açıklamayacağını veya yürütme sırasında sessiz kalıp kalmayacağını belirler.
- **Hassasiyet ve eksiksizlik:** Çıkışın gerekli doğruluğu. Modelin her uç durumu çözmesi ve tam rakamlar sağlaması gerekip gerekmediğini veya yaklaşık tahminlerin kabul edilip edilmeyeceğini belirtir.

### Sistem talimatı şablonu

Aşağıdaki sistem talimatı, modelin karmaşık bir kural kitabına uyması ve kullanıcıyla etkileşimde bulunması gereken, araştırmacılar tarafından değerlendirilmiş bir örnektir. Bu örnek, agentic karşılaştırma testlerinde performansı artırmak için kullanılmıştır. Bu istem, ajanı güçlü bir muhakeme ve planlama aracı olarak hareket etmeye teşvik eder, yukarıda listelenen boyutlarda belirli davranışları zorunlu kılar ve modelin herhangi bir işlem yapmadan önce proaktif olarak plan yapmasını gerektirir.

Bu şablonu, kullanım alanınızla ilgili kısıtlamalara uyacak şekilde uyarlayabilirsiniz.

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

## Sonraki adımlar

- İstem tasarımını daha iyi anladığınıza göre [Google AI Studio](http://aistudio.google.com?hl=tr)'yu kullanarak kendi istemlerinizi yazmayı deneyin.
- Çok formatlı istemler hakkında bilgi edinmek için [Medya dosyalarıyla istem oluşturma](https://ai.google.dev/gemini-api/docs/files?hl=tr#prompt-guide) başlıklı makaleyi inceleyin.
- Resimleri istem olarak kullanma hakkında bilgi edinmek için [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr#prompt-guide) ve [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=tr#imagen-prompt-guide) istem kılavuzlarına bakın.
- Video istemi hakkında bilgi edinmek için [Veo istem rehberini](https://ai.google.dev/gemini-api/docs/video?hl=tr#prompt-guide) inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-10 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-10 UTC."],[],[]]
