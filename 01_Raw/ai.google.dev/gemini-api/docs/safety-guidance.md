---
source_url: https://ai.google.dev/gemini-api/docs/safety-guidance?hl=tr
fetched_at: 2026-08-24T02:37:21.930055+00:00
title: "G\u00fcvenlik ve do\u011frulukla ilgili rehber \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Güvenlik ve doğrulukla ilgili rehber

Üretken yapay zeka modelleri güçlü araçlar olsa da sınırlamaları vardır. Çok yönlülükleri ve uygulanabilirlikleri bazen yanlış, taraflı veya rahatsız edici gibi beklenmedik sonuçlara yol açabilir. Bu tür çıkışlardan kaynaklanan zarar riskini sınırlamak için sonradan işleme ve titiz bir manuel değerlendirme gereklidir.

Gemini API tarafından sağlanan modeller, çok çeşitli üretken yapay zeka ve doğal dil işleme (NLP) uygulamalarında kullanılabilir. Bu işlevler yalnızca Gemini API veya Google AI Studio web uygulaması üzerinden kullanılabilir. Gemini API'yi kullanımınız [Üretken Yapay Zeka Yasaklanan Kullanım Politikası](https://policies.google.com/terms/generative-ai/use-policy?hl=tr) ve [Gemini API Hizmet Şartları](https://ai.google.dev/terms?hl=tr)'na tabidir.

Büyük dil modellerini (LLM'ler) bu kadar kullanışlı kılan özelliklerden biri, birçok farklı dil görevini ele alabilen yaratıcı araçlar olmalarıdır. Maalesef bu durum, büyük dil modellerinin rahatsız edici, duyarsız veya olgusal olarak yanlış metinler de dahil olmak üzere beklemediğiniz çıktılar üretebileceği anlamına da geliyor.
Ayrıca, bu modellerin inanılmaz çok yönlülüğü, tam olarak ne tür istenmeyen sonuçlar üretebileceklerini tahmin etmeyi de zorlaştırır. Gemini API, [Google'ın yapay zeka ilkeleri](https://ai.google/principles/?hl=tr) göz önünde bulundurularak tasarlanmış olsa da bu modelleri sorumlu bir şekilde uygulamak geliştiricilerin sorumluluğundadır. Gemini API, geliştiricilerin güvenli ve sorumlu uygulamalar oluşturmasına yardımcı olmak için yerleşik içerik filtreleme özelliğinin yanı sıra 4 zarar boyutunda ayarlanabilir güvenlik ayarlarına sahiptir. Daha fazla bilgi edinmek için [güvenlik ayarları](https://ai.google.dev/gemini-api/docs/safety-settings?hl=tr) kılavuzuna bakın. Ayrıca, doğruluk oranını artırmak için Google Arama ile Temellendirme özelliği de sunar. Ancak bu özellik, kullanım alanları daha yaratıcı olan ve bilgi edinmeye yönelik olmayan geliştiriciler için devre dışı bırakılabilir.

Bu belgenin amacı, LLM'leri kullanırken ortaya çıkabilecek bazı güvenlik riskleri hakkında sizi bilgilendirmek ve yeni güvenlik tasarımı ve geliştirme önerileri sunmaktır. (Yasa ve yönetmeliklerin de kısıtlamalar getirebileceğini ancak bu tür hususların bu kılavuzun kapsamı dışında olduğunu unutmayın.)

Büyük dil modelleriyle uygulama geliştirirken aşağıdaki adımların uygulanması önerilir:

- Uygulamanızın güvenlik risklerini anlama
- Güvenlik risklerini azaltmak için düzenlemeler yapmayı düşünün.
- Kullanım alanınıza uygun güvenlik testi yapma
- Kullanıcılardan geri bildirim isteme ve kullanımı izleme

Uygulamanız için uygun performansa ulaşana kadar ayarlama ve test aşamaları tekrarlanmalıdır.

![Model uygulama döngüsü](https://ai.google.dev/static/gemini-api/docs/images/safety_diagram.png?hl=tr)

## Uygulamanızın güvenlik risklerini anlama

Bu bağlamda güvenlik, bir LLM'nin kullanıcılarına zarar vermekten kaçınma yeteneği olarak tanımlanır. Örneğin, toksik dil veya kalıplaşmış düşünceleri teşvik eden içerik oluşturmaktan kaçınma. Gemini API aracılığıyla kullanılabilen modeller, [Google'ın Yapay Zeka İlkeleri](https://ai.google/principles/?hl=tr) dikkate alınarak tasarlanmıştır ve bu modelleri kullanımınız [Üretken Yapay Zeka Yasaklanan Kullanım Politikası](https://policies.google.com/terms/generative-ai/use-policy?hl=tr)'na tabidir. API, toksik dil ve nefret söylemi gibi bazı yaygın dil modeli sorunlarını ele almaya yardımcı olmak ve kapsayıcılık ile kalıplaşmış düşüncelerin önlenmesi için yerleşik güvenlik filtreleri sağlar. Ancak her uygulama, kullanıcıları için farklı bir risk grubu oluşturabilir. Bu nedenle, uygulama sahibi olarak kullanıcılarınızı ve uygulamanızın neden olabileceği olası zararları bilmekten ve uygulamanızın LLM'leri güvenli ve sorumlu bir şekilde kullanmasını sağlamaktan siz sorumlusunuz.

Bu değerlendirme kapsamında, zararın meydana gelme olasılığını göz önünde bulundurmalı, ciddiyetini ve azaltma adımlarını belirlemelisiniz. Örneğin, gerçek olaylara dayalı denemeler oluşturan bir uygulamanın, eğlence amaçlı kurgusal hikayeler oluşturan bir uygulamaya kıyasla yanlış bilgilendirmeyi önleme konusunda daha dikkatli olması gerekir. Potansiyel güvenlik risklerini keşfetmeye başlamanın iyi bir yolu, son kullanıcılarınızı ve uygulamanızın sonuçlarından etkilenebilecek diğer kişileri araştırmaktır. Bu, uygulama alanınızdaki en yeni çalışmaları araştırma, kullanıcıların benzer uygulamaları nasıl kullandığını gözlemleme veya kullanıcı çalışması, anket yapma ya da potansiyel kullanıcılarla gayri resmi görüşmeler yapma gibi birçok şekilde olabilir.

### Gelişmiş ipuçları

- Uygulamanız ve kullanım amacı hakkında hedef kitlenizdeki çeşitli potansiyel kullanıcılarla konuşarak olası riskler hakkında daha geniş bir bakış açısı elde edin ve çeşitlilik ölçütlerini gerektiği gibi ayarlayın.
- ABD hükümetinin Ulusal Standartlar ve Teknoloji Enstitüsü (NIST) tarafından yayınlanan [Yapay Zeka Risk Yönetimi Çerçevesi](https://www.nist.gov/itl/ai-risk-management-framework), yapay zeka risk yönetimi için daha ayrıntılı rehberlik ve ek öğrenme kaynakları sunar.
- DeepMind'ın [dil modellerinden kaynaklanan etik ve sosyal zarar riskleri](https://arxiv.org/abs/2112.04359) hakkındaki yayını, dil modeli uygulamalarının zarar verebileceği yolları ayrıntılı olarak açıklar.

## Güvenlik ve doğruluk risklerini azaltmak için ayarlamalar yapma

Riskleri anladığınıza göre, bunları nasıl azaltacağınıza karar verebilirsiniz. Hangi risklere öncelik verileceğini ve bunları önlemeye çalışmak için ne kadar çaba göstermeniz gerektiğini belirlemek, bir yazılım projesindeki hataları öncelik sırasına koymaya benzer şekilde kritik bir karardır. Öncelikleri belirledikten sonra en uygun azaltma türlerini düşünmeye başlayabilirsiniz. Genellikle basit değişiklikler fark yaratabilir ve riskleri azaltabilir.

Örneğin, bir uygulama tasarlarken şunları göz önünde bulundurun:

- Uygulama bağlamınızda kabul edilebilir olanı daha iyi yansıtmak için **model çıkışını ayarlama**. İnce ayar, modelin çıkışını daha tahmin edilebilir ve tutarlı hale getirebilir. Bu nedenle, belirli risklerin azaltılmasına yardımcı olabilir.
- **Daha güvenli çıkışlar sağlayan bir giriş yöntemi sunma.** Büyük dil modeline verdiğiniz girişin tam olarak ne olduğu, çıktının kalitesinde fark yaratabilir.
  Kullanım alanınızda en güvenli şekilde çalışan istemleri bulmak için denemeler yapmak, kullanıcı deneyimini kolaylaştıracak bir UX sunmanızı sağlayacağından çabalarınıza değecektir. Örneğin, kullanıcıların yalnızca bir giriş istemi açılır listesinden seçim yapmasını kısıtlayabilir veya uygulama bağlamınızda güvenli bir şekilde çalıştığını tespit ettiğiniz açıklayıcı ifadeler içeren pop-up öneriler sunabilirsiniz.
- **Güvenli olmayan girişleri engelleme ve çıkışı kullanıcıya gösterilmeden önce filtreleme** Basit durumlarda, istemlerde veya yanıtlarda güvenli olmayan kelimeleri ya da ifadeleri belirleyip engellemek veya bu tür içeriklerin uzman incelemeciler tarafından manuel olarak değiştirilmesini ya da engellenmesini zorunlu kılmak için engelleme listeleri kullanılabilir.
- **Her istemi olası zararlar veya saldırgan sinyallerle etiketlemek için eğitilmiş sınıflandırıcılar kullanma.** Ardından, tespit edilen zararın türüne bağlı olarak isteğin nasıl işleneceği konusunda farklı stratejiler uygulanabilir. Örneğin, giriş açıkça saldırgan veya kötüye kullanıma yönelikse engellenebilir ve bunun yerine önceden hazırlanmış bir yanıt verilebilir. **İleri düzey ipucu:** Sinyaller, çıkışın zararlı olduğunu belirlerse uygulama aşağıdaki seçenekleri kullanabilir:

  - Hata mesajı veya önceden hazırlanmış çıkış sunma
  - Aynı istem bazen farklı çıkışlar ürettiğinden, alternatif bir güvenli çıkış oluşturulması ihtimaline karşı istemi tekrar deneyin.
- **Kasıtlı kötüye kullanıma karşı koruma önlemleri alma** (ör. her kullanıcıya benzersiz bir kimlik atama ve belirli bir dönemde gönderilebilecek kullanıcı sorgularının hacmine sınır koyma). Diğer bir önlem de olası istem enjeksiyonuna karşı koruma sağlamaya çalışmaktır. SQL enjeksiyonu gibi istem enjeksiyonu da kötü amaçlı kullanıcıların, modelin çıkışını manipüle eden bir giriş istemi tasarlamasına olanak tanır. Örneğin, modele önceki örnekleri yok saymasını söyleyen bir giriş istemi gönderilebilir. Kasıtlı hatalı kullanım hakkında ayrıntılı bilgi için [Üretken Yapay Zeka Yasaklanan Kullanım Politikası](https://policies.google.com/terms/generative-ai/use-policy?hl=tr)'nı inceleyin.
- **İşlevselliği, doğası gereği daha düşük riskli bir şeye göre ayarlama.**
  Kapsamı daha dar olan (ör. metin parçalarından anahtar kelimeler çıkarma) veya daha fazla insan gözetimi olan (ör. bir insan tarafından incelenecek kısa içerikler oluşturma) görevler genellikle daha düşük risk taşır. Örneğin, sıfırdan e-posta yanıtı yazmak için bir uygulama oluşturmak yerine, uygulamayı bir taslağı genişletmek veya alternatif ifadeler önermekle sınırlayabilirsiniz.
- **Zararlı içerik güvenlik ayarlarını, zararlı olabilecek yanıtları görme olasılığınızı azaltacak şekilde ayarlama** Gemini API, prototip oluşturma aşamasında ayarlayabileceğiniz güvenlik ayarları sunar. Bu ayarlar, uygulamanızın daha kısıtlayıcı veya daha az kısıtlayıcı bir güvenlik yapılandırması gerektirip gerektirmediğini belirlemenize yardımcı olur. Belirli içerik türlerini kısıtlamak veya bunlara izin vermek için bu ayarları beş filtre kategorisinde ayarlayabilirsiniz. Gemini API aracılığıyla kullanılabilen ayarlanabilir güvenlik ayarları hakkında bilgi edinmek için [güvenlik ayarları kılavuzuna](https://ai.google.dev/gemini-api/docs/safety-settings?hl=tr) bakın.
- **Google Arama ile Temellendirme'yi etkinleştirerek olası gerçeklik hatalarını veya halüsinasyonları azaltın**. Birçok yapay zeka modelinin deneysel olduğunu ve gerçeklik hataları içeren bilgiler sunabileceğini, halüsinasyonlar üretebileceğini veya başka sorunlu çıktılar oluşturabileceğini unutmayın. Google Arama ile Temellendirme özelliği, Gemini modelini gerçek zamanlı web içeriğine bağlar ve tüm dillerde kullanılabilir. Bu sayede Gemini, daha doğru yanıtlar verebilir ve modelin bilgi kesme tarihinin ötesinde doğrulanabilir kaynaklar alıntılayabilir.

## Kullanım alanınıza uygun güvenlik testi yapın

Test, sağlam ve güvenli uygulamalar oluşturmanın önemli bir parçasıdır ancak testin kapsamı, boyutu ve stratejileri değişiklik gösterir. Örneğin, sadece eğlence amaçlı bir haiku oluşturucunun, hukuk firmaları tarafından yasal belgeleri özetlemek ve sözleşme taslakları hazırlamak için kullanılmak üzere tasarlanmış bir uygulamaya kıyasla daha az ciddi riskler oluşturması muhtemeldir. Ancak haiku oluşturucu daha geniş bir kullanıcı kitlesi tarafından kullanılabileceğinden, saldırı amaçlı girişimlerin veya istenmeden girilen zararlı girişlerin olasılığı daha yüksek olabilir. Uygulama bağlamı da önemlidir. Örneğin, herhangi bir işlem yapılmadan önce çıkışları uzmanlar tarafından incelenen bir uygulamanın, aynı denetim mekanizmasına sahip olmayan aynı uygulamanın zararlı çıkışlar üretme olasılığı daha düşük kabul edilebilir.

Nispeten düşük riskli uygulamalar için bile yayınlamaya hazır olduğunuzdan emin olmadan önce birkaç kez değişiklik yapıp test etmeniz yaygın bir durumdur. Yapay zeka uygulamaları için özellikle iki tür test yararlıdır:

- **Güvenlik karşılaştırması**, uygulamanızın nasıl kullanılabileceği bağlamında güvenli olmayabileceği yolları yansıtan güvenlik metrikleri tasarlamayı ve ardından değerlendirme veri kümelerini kullanarak uygulamanızın bu metriklerde ne kadar iyi performans gösterdiğini test etmeyi içerir. Test etmeden önce güvenlik metriklerinin kabul edilebilir minimum düzeylerini düşünmek iyi bir uygulamadır. Böylece 1) test sonuçlarını bu beklentilere göre değerlendirebilir ve 2) en çok önem verdiğiniz metrikleri değerlendiren testlere göre değerlendirme veri kümesini toplayabilirsiniz.

  **Gelişmiş ipuçları:**

  - Uygulamanızın bağlamına tam olarak uyması için kendi test veri kümelerinizi insan değerlendiricilerle oluşturmanız gerekeceğinden, "hazır" yaklaşımlara aşırı güvenmekten kaçının.
  - Birden fazla metriğiniz varsa bir değişiklik bir metrikte iyileşmeye yol açarken diğerinde kötüleşmeye neden olursa nasıl bir denge kuracağınıza karar vermeniz gerekir. Diğer performans mühendisliği çalışmalarında olduğu gibi, ortalama performans yerine değerlendirme kümenizdeki en kötü performans durumuna odaklanmak isteyebilirsiniz.
- **Çekişmeli test**, uygulamanızı proaktif bir şekilde bozmaya çalışmayı içerir. Buradaki amaç, zayıf noktaları belirleyerek uygun şekilde düzeltici adımlar atmanızı sağlamaktır. Saldırgan test, uygulamanız konusunda uzman olan değerlendiricilerden önemli ölçüde zaman/çaba gerektirebilir. Ancak ne kadar çok test yaparsanız sorunları, özellikle de nadiren veya yalnızca uygulamanın tekrar tekrar çalıştırılmasından sonra ortaya çıkan sorunları tespit etme olasılığınız o kadar artar.

  - Çekişmeli test, kötü niyetli veya istemeden zararlı girişler sağlandığında nasıl davrandığını öğrenmek amacıyla bir makine öğrenimi modelini sistematik olarak değerlendirme yöntemidir:
    - Girişin açıkça güvenli olmayan veya zararlı bir çıkış üretecek şekilde tasarlanması durumunda giriş kötü amaçlı olabilir. Örneğin, bir metin üretme modelinden belirli bir din hakkında nefret dolu bir söylem oluşturmasını istemek.
    - Girişin kendisi zararsız olsa da zararlı çıkış ürettiğinde giriş, istemeden zararlı olur. Örneğin, bir metin oluşturma modelinden belirli bir etnik kökenden olan bir kişiyi tanımlamasını istemek ve ırkçı bir çıkış almak.
  - Bir saldırı testini standart değerlendirmeden ayıran şey, test için kullanılan verilerin bileşimidir. Saldırgan testler için modelden sorunlu çıkış elde etme olasılığı en yüksek olan test verilerini seçin. Bu, nadir veya sıra dışı örnekler ve güvenlik politikalarıyla alakalı uç durumlar da dahil olmak üzere, olası tüm zarar türleri açısından modelin davranışını incelemek anlamına gelir. Ayrıca, cümlelerin yapısı, anlamı ve uzunluğu gibi farklı boyutlarında çeşitlilik de içermelidir. Test veri kümesi oluştururken nelere dikkat etmeniz gerektiğiyle ilgili daha fazla bilgi için [Google'ın adaletle ilgili sorumlu yapay zeka uygulamaları](https://ai.google/responsibilities/responsible-ai-practices/?category=fairness&hl=tr) başlıklı makaleyi inceleyebilirsiniz.
    **Gelişmiş ipuçları:**
  - Uygulamanızı kırmaya çalışmak için geleneksel olarak "kırmızı takımlara" insanları dahil etme yöntemi yerine [otomatik testleri](https://www.deepmind.com/blog/red-teaming-language-models-with-language-models?hl=tr) kullanın. Otomatik testlerde "kırmızı takım", test edilen modelden zararlı çıkışlar elde eden giriş metinlerini bulan başka bir dil modelidir.

## Sorunları izleme

Ne kadar çok test edip azaltırsanız azaltın, mükemmelliği asla garanti edemezsiniz. Bu nedenle, ortaya çıkan sorunları nasıl tespit edeceğinizi ve nasıl ele alacağınızı önceden planlayın. Kullanıcıların geri bildirimlerini paylaşmaları için izlenen bir kanal oluşturmak (ör.beğeni/beğenmeme puanı) ve çeşitli kullanıcılardan proaktif olarak geri bildirim almak için bir kullanıcı çalışması yürütmek, yaygın yaklaşımlar arasındadır. Bu yaklaşım, özellikle kullanım kalıpları beklentilerden farklıysa değerlidir.

### Gelişmiş ipuçları

- Kullanıcılar yapay zeka ürünlerine geri bildirim verdiğinde, yapay zeka performansını ve kullanıcı deneyimini zaman içinde büyük ölçüde iyileştirebilir. Örneğin, istem ayarlama için daha iyi örnekler seçmenize yardımcı olabilir. [Google'ın İnsan ve Yapay Zeka Rehberi](https://pair.withgoogle.com/guidebook/chapters)'ndeki [Geri Bildirim ve Kontrol bölümünde](https://pair.withgoogle.com/chapter/feedback-controls/), geri bildirim mekanizmaları tasarlarken dikkate alınması gereken önemli noktalar vurgulanmaktadır.

## Sonraki adımlar

- Gemini API'si aracılığıyla kullanılabilen ayarlanabilir güvenlik ayarları hakkında bilgi edinmek için [güvenlik ayarları](https://ai.google.dev/gemini-api/docs/safety-settings?hl=tr) kılavuzuna bakın.
- İlk istemlerinizi yazmaya başlamak için [istem yazmaya giriş](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=tr) bölümüne bakın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-05 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-05 UTC."],[],[]]
