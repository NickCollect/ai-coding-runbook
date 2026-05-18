---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=tr
fetched_at: 2026-05-18T05:11:33.026780+00:00
title: "Veri Kayd\u0131 ve Payla\u015f\u0131m\u0131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Veri Kaydı ve Paylaşımı

Bu sayfada, faturalandırmanın etkinleştirildiği projeler için desteklenen Gemini API çağrılarından elde edilen ve geliştiricilere ait API verileri olan [Gemini API günlüklerinin](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=tr) depolanması ve yönetilmesi açıklanmaktadır. Günlükler, kullanıcının isteğinden modelin yanıtına kadar olan tüm süreci kapsar.

## 1. Paylaşılabilecek veriler

Proje sahibi olarak, kendi kullanımınız için veya modellerimizi sürekli olarak geliştirmemize yardımcı olmak üzere Google ile geri bildirim ve paylaşım amacıyla Gemini API çağrılarının günlüğe kaydedilmesini etkinleştirebilirsiniz.

Günlük kaydı etkinleştirildiğinde, ürün iyileştirmeleri ve model eğitimi için aşağıdaki verileri göndermeyi seçerek çeşitli alanlardaki ve kullanım alanlarındaki geliştiriciler için değerli olmaya devam eden yapay zeka sistemleri oluşturmamıza yardımcı olabilirsiniz:

- **Veri kümeleri:** Google AI Studio'nun günlükler ve veri kümeleri arayüzünü kullanarak desteklenen Gemini API çağrılarından ilgilendiğiniz günlükleri (istekler, yanıtlar, meta veriler vb.) seçin. Veri kümelerine dahil edilerek katkıda bulunulan bu günlükler, veri kümesi oluşturma sırasında devre dışı bırakılabilir.
- **Geri bildirim:** Günlükleri incelerken geri bildirimde bulunabilirsiniz. Geri bildirimler arasında olumlu/olumsuz puanlar ve yazdığınız yorumlar yer alır.

Google ile bir veri kümesi paylaştığınızda, istekler ve yanıtlar dahil olmak üzere bu veri kümesindeki günlükleriniz, "[Ücretsiz Hizmetler](https://ai.google.dev/gemini-api/terms?hl=tr#data-use-unpaid)" ile ilgili [Şartlarımız](https://developers.google.com/terms?hl=tr) uyarınca işlenir. Bu, veri kümesinin, modellerimizi iyileştirme ve eğitme de dahil olmak üzere Google ürünlerini, hizmetlerini ve makine öğrenimi teknolojilerini geliştirmek ve iyileştirmek için kullanılabileceği anlamına gelir. **Kişisel, hassas veya gizli bilgiler eklemeyin.**

## 2. Verilerinizi nasıl kullanırız?

Günlüklerin süresi varsayılan olarak 55 gün sonra dolar. Bu sürenin sonunda kullanılamaz hale gelirler. Aşağı akış kullanım alanları için bu dönemin ötesinde ilgi veya değer günlüklerini saklamak ve model iyileştirmelerine isteğe bağlı olarak katkıda bulunmak üzere veri kümeleri oluşturulabilir. Veri kümelerinde depolanan günlüklerin son kullanma tarihi yoktur ancak her projenin varsayılan depolama sınırı 1.000 günlüktür.

Varsayılan olarak, günlük kaydı yalnızca faturalandırmanın etkinleştirildiği projelerde kullanılabildiğinden günlüklerdeki istemler ve yanıtlar, veri kullanımına ilişkin [Şartlarımız](https://developers.google.com/terms?hl=tr) uyarınca ürün iyileştirme veya geliştirme için kullanılmaz.

Günlüklerinizin veri kümelerini Google ile paylaşmayı seçerseniz bu veri kümeleri, yapay zeka sistemlerinin ve uygulamalarının kullanıldığı alanların ve bağlamların çeşitliliğini daha iyi anlamak için gerçek dünya gösterim verileri olarak kullanılır. Bu veriler, model kalitesini artırmak ve gelecekteki modellerin ve hizmetlerin eğitim ve değerlendirme süreçlerine bilgi sağlamak için kullanılabilir. Bu veriler, [Ücretsiz Hizmetler](https://ai.google.dev/gemini-api/terms?hl=tr#data-use-unpaid) için veri kullanım şartlarımıza uygun olarak işlenir.
Bu nedenle, inceleme uzmanları paylaştığınız API girişlerini ve çıkışlarını okuyabilir, işleyebilir ve bunlara açıklama ekleyebilir. Veriler model geliştirmede kullanılmadan önce Google, bu süreç kapsamında kullanıcı gizliliğini korumak için gerekli önlemleri alır. Örneğin, inceleme uzmanları görmeden veya açıklama eklemeden önce bu verilerin Google Hesabınız, API anahtarınız ve Cloud projenizle bağlantısını kaldırırız.

## 3. Veri izinleri

API verilerine katkıda bulunmayı etkinleştirerek Google'ın verileri bu belgede açıklandığı şekilde işlemesi ve kullanması için gerekli izinlere sahip olduğunuzu onaylarsınız. **Lütfen ücretli hizmet aracılığıyla elde edilen hassas, gizli veya özel bilgileri içeren günlükler göndermeyin**.
API Şartları'ndaki "[İçerik Gönderimi](https://developers.google.com/terms?hl=tr#b_submission_of_content)" bölümü uyarınca Google'a verdiğiniz lisans, Hizmetler'e gönderdiğiniz tüm içerikler (ör.ilişkili sistem talimatları da dahil olmak üzere istemler, önbelleğe alınmış içerikler ve resim, video ya da belge gibi dosyalar) ve oluşturulan tüm yanıtlar için de geçerlidir. Bu geçerlilik, kullanımımız için geçerli yasa kapsamında gerekli olduğu ölçüde geçerlidir.

## 4. Veri paylaşımı ve geri bildirim

Verilerinizi örnek olarak paylaşmayı kabul ederek yapay zeka araştırmalarının, Gemini API'nin ve Google AI Studio'nun sınırlarını genişletmemize yardımcı olabilirsiniz. Bu sayede, modellerimizi çeşitli bağlamlarda sürekli olarak iyileştirebilir ve farklı alanlardaki ve kullanım alanlarındaki geliştiriciler için değerli olmaya devam edecek yapay zeka sistemleri oluşturabiliriz.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-04-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-04-29 UTC."],[],[]]
