---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=tr
fetched_at: 2026-06-22T06:34:38.367566+00:00
title: "Google AI Studio'dan da\u011f\u0131tma \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Google AI Studio'dan dağıtma

Google AI Studio, tam yığın uygulamalarınızı doğrudan Oluşturma Modu'ndan dağıtmanıza olanak tanır. Bu sayede prototipten yönetilen ve ölçeklenebilir bir üretim ortamına hızlı bir şekilde geçebilirsiniz.

## Dağıtım seçenekleri

Uygulamanızı AI Studio'nun Oluşturma Modu'ndan dağıtmak için kullandığınız katmana bağlı olarak aşağıdaki şartları karşılamanız gerekir:

- [**Google Cloud Başlangıç Katmanı**](https://docs.cloud.google.com/docs/starter-tier?hl=tr):
  Google Cloud projesi veya faturalandırma hesabı oluşturmadan 2 tam yığın uygulaması yayınlamanıza olanak tanır.
- **Standart dağıtım**: AI Studio hesabınıza bağlı bir Google Cloud projesi ve bu projede faturalandırmanın etkinleştirilmesi gerekir.

## Başlangıç Seviyesi hakkında

Google Cloud Başlangıç Katmanı, tam bir Google Cloud ortamı veya faturalandırma hesabı oluşturmadan uygulamaları doğrudan Google AI Studio'dan Google Cloud'a dağıtmak için kolay bir yol sunar.

Her Google AI Studio dağıtımı, Cloud Run'da karşılık gelen bir hizmet oluşturur. Başlangıç Katmanı ile Google AI Studio'da dağıtılan hizmetler için aşağıdaki sınırlamalar geçerlidir:

- En fazla iki hizmet dağıtabilirsiniz.
- Hizmetleriniz [tek bir Cloud Run bölgesinde](https://docs.cloud.google.com/run/docs/locations?hl=tr) dağıtılmış olmalıdır.

## Başlangıç Seviyesi dağıtım adımları

Uygulamanızı Oluşturma modunda tasarladıktan sonra Başlangıç Katmanı ile dağıtın:

1. Sağ üst köşedeki **Yayınla** düğmesini tıklayın.
2. **Get Started**'ı (Başlayın) tıklayın.
3. **Uygulamayı Yayınla**'yı tıklayın.

Dağıtım tamamlandıktan sonra AI Studio, canlı uygulamanıza erişebileceğiniz bir Cloud Run URL'si sağlar.

## Standart dağıtım

Uygulamalarınız geliştikçe Başlangıç Katmanı'nın ötesinde özelliklere (ör. daha yüksek kotalar, daha fazla işlem kaynağı veya Başlangıç Katmanı'nda bulunmayan diğer Google Cloud ürünleri) ihtiyacınız olabilir. Bu özelliklerden yararlanmak için tamamen yönetilen Başlangıç Katmanı projenizi standart bir Google Cloud projesine dönüştürebilirsiniz.

Bu sayede, ilerlemenizi kaybetmeden sorunsuz bir şekilde ölçeklendirme yapabilirsiniz. [Cloud Faturalandırma Hesabı oluşturma](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=tr#create-new-billing-account), standart Google Cloud Hizmet Şartları'nı resmen kabul etme ve [standart Google Cloud projesine yükseltme](https://docs.cloud.google.com/docs/starter-tier?hl=tr#upgradee) adımlarını uygulayın.
Daha fazla bilgi için [Ücretli hesaplar için kurulum](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=tr#paid-setup) başlıklı makaleyi inceleyin.

Faturalandırma katmanları hakkında daha fazla bilgi edinmek için [Faturalandırma](https://ai.google.dev/gemini-api/docs/billing?hl=tr) başlıklı makaleyi inceleyin.

## Başvurunuzu silme

Uygulamanıza artık ihtiyacınız yoksa aşağıdaki talimatları uygulayarak Google AI Studio'da silebilirsiniz:

1. Google AI Studio'da [Uygulamalar sayfanıza](https://aistudio.google.com/app/apps?hl=tr) gidin.
2. Sol menüden **Uygulamalar**'ı seçin.
3. İşaretçiyi silmek istediğiniz uygulamanın üzerine getirin.
4. Uygulamayı silmek için satırın sağ tarafındaki çöp kutusu simgesini tıklayın.

## Sırada ne var?

- [Google Cloud Başlangıç Katmanı](https://docs.cloud.google.com/docs/starter-tier?hl=tr) hakkında daha fazla bilgi edinin.
- Gemini API'de [Faturalandırma](https://ai.google.dev/gemini-api/docs/billing?hl=tr) hakkında bilgi edinin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-16 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-16 UTC."],[],[]]
