---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=tr
fetched_at: 2026-09-07T05:41:01.800436+00:00
title: "Google AI Studio ile ilgili sorunlar\u0131 giderme \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Google AI Studio ile ilgili sorunları giderme

Bu sayfada, Google AI Studio'da sorun yaşarsanız sorun giderme ile ilgili öneriler verilmektedir.

## 403 Erişim Kısıtlandı hatalarını anlama

403 Erişim Kısıtlandı hatası görürseniz Google AI Studio'yu [Hizmet Şartları](https://ai.google.dev/terms?hl=tr)'na uymayan bir şekilde kullanıyorsunuz demektir. Bunun yaygın bir nedeni, [desteklenen bir bölgede](https://ai.google.dev/available_regions?hl=tr) bulunmamanızdır.

## Google AI Studio'da "İçerik Yok" yanıtlarını çözme

İçerik herhangi bir nedenle engellenirse Google AI Studio'da warning **No Content** (İçerik Yok) mesajı gösterilir. Daha fazla ayrıntı görmek için fare imlecini **İçerik Yok**'un üzerine getirin ve warning **Güvenlik**'i tıklayın.

Yanıt, [güvenlik ayarları](https://ai.google.dev/docs/safety_setting?hl=tr) nedeniyle engellendiyse ve kullanım alanınızla ilgili [güvenlik risklerini](https://ai.google.dev/docs/safety_guidance?hl=tr) göz önünde bulundurduysanız döndürülen yanıtı etkilemek için [güvenlik ayarlarını](https://ai.google.dev/docs/safety_setting?hl=tr#safety_settings_in_makersuite) değiştirebilirsiniz.

Yanıt, güvenlik ayarları nedeniyle değil de başka bir nedenle engellendiyse sorgu veya yanıt [Hizmet Şartları](https://ai.google.dev/terms?hl=tr)'nı ihlal ediyor ya da başka bir şekilde desteklenmiyor olabilir.

## Jeton kullanımını ve sınırlarını kontrol etme

Bir istem açıkken ekranın alt kısmındaki **Metin Önizleme** düğmesinde, isteminizin içeriği için kullanılan mevcut jetonlar ve kullanılan modelin maksimum jeton sayısı gösterilir.

## AI Studio için Google Cloud IAM izinleri

Google Cloud projesi üyelerinin Google AI Studio'da işlem yapabilmek için belirli Identity and Access Management (IAM) izinlerine sahip olması gerekir. Bu kimlikler hakkında daha fazla bilgi için [IAM asıl üyelerine genel bakış](https://cloud.google.com/iam/docs/principals?hl=tr) başlıklı makaleyi inceleyin.

İlişkili Google Cloud projesinde **Düzenleyici** veya **Sahip** rollerine sahip kullanıcılar, kontrol panellerini görüntüleme ve Gemini API anahtarlarını yönetme konusunda tam izinlere sahiptir. **Görüntüleyici** rolüne sahip kullanıcılar kontrol panellerini ve API anahtarlarını görüntüleyebilir ancak bunları oluşturamaz, güncelleyemez veya silemez.

Daha ayrıntılı kontrol için her bir AI Studio özelliği için gereken belirli izinleri aşağıdaki tablodan inceleyin. Bu izinleri verme talimatları için Google Cloud dokümanlarındaki [Kaynaklara erişim verme, erişimi değiştirme ve iptal etme](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=tr) başlıklı makaleyi inceleyin.

| AI Studio özelliği | Gerekli IAM izinleri | Diğer şartlar |
| --- | --- | --- |
| **Proje arama** (projeleri içe aktarma) | `resourcemanager.projects.get` |  |
| **Projeyi yeniden adlandırma** | `resourcemanager.projects.update` |  |
| **Görüntüleme kotası katmanı** | Yok |  |
| **API anahtarı oluşturma** | **Projede arama** iznine sahip olmanız ve:  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **API anahtarlarını listeleme** | **Projede arama** iznine sahip olmanız ve:  `apikeys.keys.list` `serviceusage.services.get` | Google Cloud projesinde [Generative Language API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=tr) etkinleştirilmiş olmalıdır. |
| **API anahtarlarını yeniden adlandırma** | `apikeys.keys.update` |  |
| **API anahtarlarını silme** | `apikeys.keys.delete` |  |
| **Kullanım kontrol paneli** | **Projede arama** iznine sahip olmanız ve:  `monitoring.timeSeries.list` |  |
| **Hız sınırı kontrol paneli** | **Kullanım kontrol paneli** izinlerine sahip olma ve:  `cloudquotas.quotas.get` |  |
| **Harcama (Faturalandırma sınırı)** | `billing.resourceCosts.get` (harcamayı görüntülemek için) `billing.resourcebudgets.read` (sınırı görüntülemek için) `billing.resourcebudgets.write` (sınır belirlemek için) |  |
| **Faturalandırma kontrol paneli** | `billing.accounts.get` |  |

### Diğer erişim kontrolleri

AI Studio, Google Cloud IAM izinlerine ek olarak güvenlik ve uygunluk kontrolleri de gerçekleştirir. Aşağıdaki şartları karşılamıyorsanız AI Studio arayüzünde veya API yanıtlarında `PERMISSION_DENIED` ya da erişim kısıtlaması hatasıyla karşılaşabilirsiniz:

- **Güvenlik kontrolleri:** İsteğiniz otomatik güvenlik kontrollerinden geçmelidir.
- **Hizmet Şartları:** Google Hizmet Şartları'nı ve Üretken Yapay Zeka Ek Hizmet Şartları'nı kabul etmeniz gerekir.
- **Desteklenen bölge:** [Desteklenen bir bölgede](https://ai.google.dev/gemini-api/docs/available-regions?hl=tr) bulunmanız gerekir.
- **Güven ve Güvenlik:** Google Cloud projesi kötüye kullanım nedeniyle işaretlenmemiş olmalıdır.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-29 UTC."],[],[]]
