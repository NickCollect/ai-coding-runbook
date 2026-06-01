---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=tr
fetched_at: 2026-06-01T06:10:19.198859+00:00
title: "Google AI Studio h\u0131zl\u0131 ba\u015flang\u0131\u00e7 k\u0131lavuzu \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Google AI Studio hızlı başlangıç kılavuzu

[Google AI Studio](https://aistudio.google.com/?hl=tr), modelleri hızlı bir şekilde denemenize ve farklı istemlerle denemeler yapmanıza olanak tanır. Geliştirmeye hazır olduğunuzda [Gemini API](https://ai.google.dev/gemini-api/docs/quickstart?hl=tr)'yi kullanmak için "Kodu al"ı ve tercih ettiğiniz programlama dilini seçebilirsiniz.

## İstemler ve ayarlar

Google AI Studio, farklı kullanım alanları için tasarlanmış çeşitli istem arayüzleri sunar. Bu kılavuzda, sohbet deneyimleri oluşturmak için kullanılan **sohbet istemleri** ele alınmaktadır. Bu istem tekniği, çıktı oluşturmak için birden fazla giriş ve yanıt etkileşimine olanak tanır. [Aşağıdaki sohbet istemi örneğimizden](#chat_example) daha fazla bilgi edinebilirsiniz.
Diğer seçenekler arasında **Anlık yayın**, **Video oluşturma** ve daha fazlası yer alır.

AI Studio'da **Çalıştırma ayarları** paneli de bulunur. Bu panelde [model parametrelerinde](https://ai.google.dev/docs/prompting-strategies?hl=tr#model-parameters) ve [güvenlik ayarlarında](https://ai.google.dev/gemini-api/docs/safety-settings?hl=tr) düzenlemeler yapabilir, [yapılandırılmış çıkış](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr), [işlev çağrısı](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr), [kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) ve [temellendirme](https://ai.google.dev/gemini-api/docs/grounding?hl=tr) gibi araçları etkinleştirebilirsiniz.

## Chat istemi örneği: Özel bir sohbet uygulaması oluşturma

[Gemini](https://gemini.google.com/?hl=tr) gibi genel amaçlı bir chatbot kullandıysanız üretken yapay zeka modellerinin açık uçlu diyaloglar için ne kadar güçlü olabileceğini ilk elden deneyimlemişsinizdir. Bu genel amaçlı chatbot'lar faydalı olsa da genellikle belirli kullanım alanlarına göre uyarlanmaları gerekir.

Örneğin, yalnızca bir şirketin ürünüyle ilgili görüşmeleri destekleyen bir müşteri hizmetleri chatbot'u oluşturmak isteyebilirsiniz. Belirli bir üslup veya tarzda konuşan bir chatbot oluşturmak isteyebilirsiniz. Örneğin, çok sayıda şaka yapan, şair gibi kafiyeli konuşan veya yanıtlarında çok sayıda emoji kullanan bir bot.

Bu örnekte, Google AI Studio'yu kullanarak Jüpiter'in uydularından biri olan Europa'da yaşayan bir uzaylı gibi iletişim kuran samimi bir chatbot'u nasıl oluşturacağınız gösterilmektedir.

### 1. adım: Sohbet istemi oluşturun

Chatbot oluşturmak için, modeli istediğiniz yanıtları vermeye yönlendirmek üzere kullanıcı ile chatbot arasındaki etkileşim örneklerini sağlamanız gerekir.

Sohbet istemi oluşturmak için:

1. [Google AI Studio](https://aistudio.google.com/?hl=tr)'yu açın. **Playground**, yeni bir sohbet istemiyle varsayılan olarak açık olur.
2. Sağ üst köşedeki **Çalıştırma ayarları**'nı tune tıklayarak paneli genişletin ve [**Sistem Talimatları**](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr#system-instructions) giriş alanını bulun. Aşağıdakileri metin giriş alanına yapıştırın:

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

Sistem talimatlarını ekledikten sonra modelle sohbet ederek uygulamanızı test etmeye başlayın:

1. **Bir şeyler yazın...** etiketli metin giriş kutusuna, kullanıcının sorabileceği bir soru veya yapabileceği bir gözlem yazın. Örneğin:

   **Kullanıcı:**

   ```
   What's the weather like?
   ```
2. Chatbot'tan yanıt almak için **Çalıştır** düğmesini tıklayın. Bu yanıt, aşağıdakine benzer bir şey olabilir:

   **Model:**

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   (gemini-2.5-pro)

### 2. adım: Botunuza daha iyi sohbet etmeyi öğretin

Tek bir talimat vererek temel bir Europa uzaylı chatbot'u oluşturabildiniz. Ancak tek bir talimat, modelin yanıtlarında tutarlılık ve kalite sağlamak için yeterli olmayabilir. Daha ayrıntılı talimatlar olmadan modelin hava durumuyla ilgili bir soruya verdiği yanıt çok uzun olma eğilimindedir ve kendi başına hareket edebilir.

Sistem talimatlarına aşağıdakileri ekleyerek chatbot'unuzun üslubunu özelleştirin:

1. Yeni bir sohbet istemi başlatın veya aynı istemi kullanın. Sistem talimatları, sohbet oturumu başladıktan sonra değiştirilebilir.
2. **Sistem Talimatları** bölümünde, mevcut talimatları aşağıdaki talimatlarla değiştirin:

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. Sorunuzu yeniden girin (`What's the weather like?`) ve **Çalıştır** düğmesini tıklayın. Yeni bir sohbet başlatmadıysanız yanıtınız aşağıdaki gibi olabilir:

   **Model:**

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   (gemini-2.5-pro)

Bu yaklaşımı kullanarak chatbot'a daha fazla derinlik katabilirsiniz. Daha fazla soru sorun, yanıtları düzenleyin ve chatbot'unuzun kalitesini artırın. Talimatları eklemeye veya değiştirmeye devam edin ve chatbot'unuzun davranışını nasıl değiştirdiklerini test edin.

### 3. adım: Sonraki adımlar

Diğer istem türlerine benzer şekilde, isteminizin prototipini istediğiniz gibi oluşturduktan sonra kodlamaya başlamak için **Kodu al** düğmesini kullanabilir veya isteminizi kaydedip daha sonra üzerinde çalışabilir ve başkalarıyla paylaşabilirsiniz.

## Daha fazla bilgi

- Kod yazmaya hazırsanız [API hızlı başlangıç kılavuzlarına](https://ai.google.dev/gemini-api/docs/quickstart?hl=tr) bakın.
- Daha iyi istemler oluşturmayı öğrenmek için [İstem tasarımı kurallarına](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=tr) göz atın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-12 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-12 UTC."],[],[]]
