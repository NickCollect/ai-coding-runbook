---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=tr
fetched_at: 2026-09-21T05:48:35.027188+00:00
title: "Gemini API'de video \u00fcretme \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini API'de video üretme

Gemini API, video oluşturmak için iki model sunar: [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=tr) ve [Veo](https://ai.google.dev/gemini-api/docs/veo?hl=tr).
Her biri farklı iş akışları için tasarlanmıştır.

Video üretimi için varsayılan modeliniz olarak Gemini Omni Flash'i kullanın. Üstün video tutarlılığı, çoklu giriş akıl yürütme (aynı anda metin, resim, ses ve video girişlerini destekler), karakter tutarlılığı, olgusal doğruluk ve çok turlu sohbete dayalı düzenleme (ör. öğe değiştirme veya perspektif değişiklikleri) sunar. Sahne genişletme, son kare kontrolü veya eski işlem hatlarıyla entegrasyon gibi belirli özellikler için Veo 3.1'in kullanılması gerekir.

## Gemini Omni Flash

Gemini Omni Flash, video üretimi ve sohbet tarzında video düzenleme için hızlı, çok formatlı bir modeldir. Metin istemlerini ve resimleri hızlı bir şekilde kısa videolara dönüştürme konusunda başarılıdır. Ayrıca, Etkileşimler API'sini kullanarak sonuçları birden fazla dönüşte iyileştirmenize olanak tanır.

[Gemini Omni Flash'ı kullanmaya başlayın →](https://ai.google.dev/gemini-api/docs/omni?hl=tr)

## Veo 3.1

Veo 3.1, tümleşik ses içeren videolar üretmek için kullanılan bir modeldir. `generateContent` API aracılığıyla video uzantısı, kareye özel üretim ve resme dayalı yönlendirme gibi özellikleri destekler.

[Veo 3.1'i kullanmaya başlama →](https://ai.google.dev/gemini-api/docs/veo?hl=tr)

## Video anlama

Yeni video oluşturmak yerine mevcut video içeriklerini alıp analiz etmeniz gerekiyorsa [Video anlama kılavuzu](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr)'na bakın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-30 UTC."],[],[]]
