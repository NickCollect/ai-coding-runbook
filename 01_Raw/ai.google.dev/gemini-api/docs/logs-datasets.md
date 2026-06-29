---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=tr
fetched_at: 2026-06-29T05:34:10.880218+00:00
title: "G\u00fcnl\u00fckler ve veri k\u00fcmeleri \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Günlükler ve veri kümeleri

Bu kılavuzda, mevcut Gemini API uygulamalarınızda günlük kaydını etkinleştirmeye başlamak için ihtiyacınız olan her şey yer almaktadır. Bu kılavuzda, model davranışını ve kullanıcıların uygulamalarınızla nasıl etkileşim kurabileceğini daha iyi anlamak için Google AI Studio kontrol panelinde mevcut veya yeni bir uygulamadan gelen günlükleri nasıl görüntüleyeceğinizi öğreneceksiniz. Günlük kaydını kullanarak *kullanım geri bildirimlerini isteğe bağlı olarak Google ile paylaşabilir
ve geliştiricilerin kullanım alanlarında Gemini'ı iyileştirmeye yardımcı olabilirsiniz*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=tr)

[OpenAI uyumluluğu](https://ai.google.dev/gemini-api/docs/openai?hl=tr) uç noktaları üzerinden yapılanlar da dahil olmak üzere tüm `GenerateContent` ve `StreamGenerateContent` API çağrıları desteklenir.

## 1. Google AI Studio'da günlük kaydını etkinleştirme

Başlamadan önce, faturalandırmanın etkinleştirildiği ve sahibi olduğunuz bir projenin bulunduğundan emin olun.

1. Google [AI Studio](https://aistudio.google.com/logs?hl=tr)'da günlükler sayfasını açın.
2. Açılır listeden projenizi seçin ve tüm istekler için varsayılan olarak günlüğe kaydetmeyi etkinleştirmek üzere etkinleştirme düğmesine basın.

![](https://ai.google.dev/static/gemini-api/docs/images/logs-state.png?hl=tr)

Tüm projeler veya belirli projeler için günlük kaydını etkinleştirebilir ya da devre dışı bırakabilir ve bu tercihleri Google AI Studio üzerinden istediğiniz zaman değiştirebilirsiniz.

## 2. AI Studio'da günlükleri görüntüleme

1. [AI Studio](https://aistudio.google.com/logs?hl=tr)'ya gidin.
2. Günlüğü etkinleştirdiğiniz projeyi seçin.
3. Günlüklerinizin tabloda ters kronolojik sırada göründüğünü görmeniz gerekir.

![](https://storage.googleapis.com/generativeai-downloads/images/nano-banana-logs.gif)

İstek ve yanıt çiftinin tam sayfa görüntülemesi için bir girişi tıklayın. İstemin tamamını, Gemini'dan gelen yanıtın tamamını ve önceki aşamadaki bağlamı inceleyebilirsiniz. Her projenin varsayılan depolama sınırının 1.000 günlük olduğunu ve veri kümelerine kaydedilmeyen günlüklerin süresinin 55 gün sonra dolacağını unutmayın. Projeniz depolama alanı sınırına ulaşırsa günlükleri silmeniz istenir.

## 3. Veri kümelerini düzenleme ve paylaşma

- Filtreleme ölçütü olarak kullanılacak bir özellik seçmek için günlükler tablosunda üst kısımdaki filtre çubuğunu bulun.
- Filtrelenmiş günlük görünümünüzde, tüm günlükleri veya birkaç günlüğü seçmek için onay kutularını kullanın.
- Listenin en üstünde görünen "Veri kümesi oluştur" düğmesini tıklayın.
- Yeni veri kümenize açıklayıcı bir ad ve isteğe bağlı bir açıklama girin.
- Yeni oluşturduğunuz veri kümesini, seçilmiş günlükler kümesiyle birlikte görürsünüz.
- Daha ayrıntılı analiz için veri kümenizi CSV, JSONL dosyaları olarak veya Google E-Tablolar'a aktarın.

![](https://storage.googleapis.com/generativeai-downloads/images/sales-dataset.gif)

Veri kümeleri, çeşitli kullanım alanlarında faydalı olabilir.

- **Hazır soru setleri oluşturun:** Yapay zekanızın gelişmesini istediğiniz alanlara yönelik iyileştirmeler yapın.
- **Örnek kümeleri düzenleme:** Örneğin, başka bir modelden yanıt oluşturmak için gerçek kullanımdan alınan bir örnek veya dağıtımdan önce rutin kontroller için uç durumların bir koleksiyonu.
- **Değerlendirme kümeleri:** Diğer modeller veya sistem talimatı yinelemeleri arasında karşılaştırma yapmak için önemli özelliklerdeki gerçek kullanımı temsil eden kümeler.

Veri kümelerinizi gösterim örnekleri olarak paylaşmayı seçerek yapay zeka araştırmaları, Gemini API ve Google AI Studio'da ilerlemeye yardımcı olabilirsiniz. Bu sayede modellerimizi çeşitli bağlamlarda iyileştirebilir ve birçok alanda ve uygulamada geliştiriciler için faydalı olmaya devam eden yapay zeka sistemleri oluşturabiliriz.

## Sonraki adımlar ve test edilecek öğeler

Günlüğü etkinleştirdiğinize göre deneyebileceğiniz birkaç şey:

- **Oturum geçmişiyle prototip oluşturma:** Kod uygulamaları oluşturmak için [AI Studio Build](https://aistudio.google.com/apps?hl=tr)'dan yararlanın ve kullanıcı günlüklerinin geçmişini etkinleştirmek için API anahtarınızı ekleyin.
- **Gemini Batch API ile günlükleri yeniden çalıştırma:** [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb) aracılığıyla günlükleri yeniden çalıştırarak yanıt örnekleme ve modellerin ya da uygulama mantığının değerlendirilmesi için veri kümelerini kullanın.

## Uyumluluk

Günlüğe kaydetme özelliği şu anda aşağıdakiler için desteklenmemektedir:

- Imagen ve Veo modelleri
- Gemini yerleştirme modeli
- Video, GIF veya PDF içeren girişler

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-01 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-01 UTC."],[],[]]
