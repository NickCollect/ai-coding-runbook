---
source_url: https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=tr
fetched_at: 2026-06-08T05:30:39.732148+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Interactions API

**Interactions API**, Gemini ile geliştirme yaparken kullanılması önerilen yeni standarttır. Bu model; ajan tabanlı iş akışları, sunucu tarafı durum yönetimi ve karmaşık çok formatlı, çok adımlı sohbetler için optimize edilmiştir. Orijinal [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=tr) API'si tam olarak desteklenmeye devam etmektedir.

## Neden Etkileşimler API'sini kullanmalısınız?

- **Sunucu tarafı geçmiş yönetimi**: `previous_interaction_id` aracılığıyla basitleştirilmiş çok turlu akışlar. Sunucu, durumu varsayılan olarak etkinleştirir (`store=true`), ancak `store=false`'yi ayarlayarak durumsuz davranışı etkinleştirebilirsiniz.
- **Gözlemlenebilir yürütme adımları**: Yazılan adımlar, karmaşık akışlarda hata ayıklamayı ve ara etkinlikler (ör. düşünceler veya arama widget'ları) için kullanıcı arayüzü oluşturmayı kolaylaştırır.
- **Temsilci tabanlı iş akışları için tasarlandı**: Yazılı yürütme adımları aracılığıyla çok adımlı araç kullanımı, düzenleme ve karmaşık akıl yürütme akışları için yerel destek.
- **Uzun süren ve arka plan görevleri**: `background=true` kullanarak [Deep Think](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=tr) ve [Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=tr) gibi zaman alan işlemlerin arka plan süreçlerine aktarılmasını destekler.
- **Yeni modellere ve özelliklere erişim**: Gelecekte, temel ana hat ailesinin ötesindeki yeni modellerin yanı sıra yeni aracı özellikleri ve araçları yalnızca Interactions API'de kullanıma sunulacak.

Yeni bir projeye başlıyorsanız, yapay zeka tabanlı uygulamalar geliştiriyorsanız veya sunucu tarafında görüşme yönetimine ihtiyacınız varsa **Etkileşimler API'sini kullanın**. İhtiyaçlarınızı karşılayan mevcut bir entegrasyonunuz varsa veya Etkileşimler API'sinde [henüz kullanılamayan](#limitations) bir özelliğe (ör. Batch API veya açık önbelleğe alma) ihtiyacınız varsa **[`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=tr)** kullanın.

## Başlayın

- **Kodlama aracınızı ayarlayın**: **Gemini Docs MCP**'ye bağlanın ve `gemini-interactions-api` becerisini yükleyerek asistanınıza en yeni geliştirici belgelerine ve en iyi uygulamalara doğrudan erişim izni verin.
  [Kodlama aracınızı ayarlayın →](https://ai.google.dev/gemini-api/docs/coding-agents?hl=tr)
- **`generateContent`**'den geçiş yapma: Mevcut bir entegrasyonunuz varsa Etkileşimler API'sine geçiş yapmak için [Taşıma Kılavuzu](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=tr)'nu inceleyin.
- **Hızlı başlangıç kılavuzunu deneyin**: [Etkileşimler API'si hızlı başlangıç kılavuzundaki](https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=tr) minimum çalışma örneğiyle başlayın.

### Özellik rehberleri

Bu kılavuzlar aracılığıyla Etkileşimler API'sinin belirli özelliklerini keşfedin. generateContent ve Interactions API arasında geçiş yapmak için bu sayfalardaki açma/kapatma düğmesini kullanabilirsiniz:

- [Metin oluşturma](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=tr)
- [Görüntü üretme](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=tr)
- [Görüntü anlama](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=tr)
- [Ses yorumlama](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=tr)
- [Video anlama](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=tr) (Video understanding)
- [Belge işleme](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=tr)
- [İşlev çağırma](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=tr)
- [Yapılandırılmış çıkış](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=tr)
- [Deep Research Agent](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=tr)
- [Esnek çıkarım](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=tr)
- [Öncelik çıkarımı](https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=tr)
- [yayınlayarak](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=tr)

## Etkileşimler API'sinin işleyiş şekli

Etkileşimler API'si, temel bir kaynak olan [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=tr#Resource:Interaction) etrafında şekillenir. `Interaction`, bir görüşme veya görevdeki tam bir dönüşü temsil eder. Bir etkileşimin tüm geçmişini **yürütme adımlarının** kronolojik sırası olarak içeren bir oturum kaydı görevi görür. Bu adımlar arasında model düşünceleri, sunucu tarafında veya istemci tarafında araç çağrıları ve sonuçları (ör. `function_call` ve `function_result`) ve nihai `model_output` yer alır. Depolanan kaynak (`interactions.get` aracılığıyla alınır) tam bağlam için `user_input` adımlarını da içerir. Ancak `interactions.create` yanıtı yalnızca model tarafından oluşturulan adımları döndürür.

[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=tr#CreateInteraction) adresine çağrı yaptığınızda yeni bir `Interaction` kaynağı oluşturursunuz.

### SDK kolaylık özellikleriyle çıkışlara erişme

Etkileşimler API'si, yürütme adımlarının (ör. düşünceler, arama sorguları ve işlev çağrıları) yapılandırılmış bir zaman çizelgesini döndürse de nihai model yanıtını almak için adımları manuel olarak izlemeniz gerekmez.

Google GenAI SDK'ları, farklı yöntemlerdeki çıkışlara erişmek için doğrudan döndürülen `Interaction` nesnesinde kolaylık özellikleri sağlar:

| SDK kolaylık özelliği | Dönüş Türü | Açıklama |
| --- | --- | --- |
| **`interaction.output_text`** | Dize | Modelin yanıtındaki son metin bloklarını döndürür. Yanıt, birden fazla ardışık `TextContent` blokuna bölünmüşse bunlar otomatik olarak birleştirilir. Metin dışı içeriklerle (ör. düşünceler, resimler, ses veya araç çağrıları) ayrılmış önceki metin bloklarını içermez. Karmaşık veya iç içe geçmiş çok formatlı yanıtlarda bunun yerine `steps` üzerinde manuel olarak yineleme yapmanız gerekir. |
| **`interaction.output_image`** | ImageContent veya `None` | Modelin mevcut istekte oluşturduğu son resim bloğunu döndürür. |
| **`interaction.output_audio`** | AudioContent veya `None` | Geçerli istekte model tarafından oluşturulan son ses bloğunu döndürür. |

Ara düşünme süreçlerini oluşturma, adım adım araç çağrılarını inceleme veya hata ayıklama gibi gelişmiş kullanım alanlarında, ham `interaction.steps` zaman çizelgesini manuel olarak inceleyip gezinebilirsiniz.

### Sunucu tarafı durum yönetimi

Sohbete devam etmek için `previous_interaction_id` parametresini kullanarak sonraki bir çağrıda tamamlanmış bir etkileşimin `id` değerini kullanabilirsiniz. Sunucu, sohbet geçmişini almak için bu kimliği kullanır. Böylece, tüm sohbet geçmişini yeniden göndermeniz gerekmez.

`previous_interaction_id` parametresi yalnızca `previous_interaction_id` kullanılarak yapılan görüşme geçmişini (girişler ve çıkışlar) korur. Diğer parametreler **etkileşim kapsamlıdır**
ve yalnızca şu anda oluşturduğunuz etkileşim için geçerlidir:

- `tools`
- `system_instruction`
- `generation_config` (`thinking_level`, `temperature` vb. dahil)

Bu, geçerli olmasını istiyorsanız bu parametreleri her yeni etkileşimde yeniden belirtmeniz gerektiği anlamına gelir. Bu sunucu tarafı durum yönetimi isteğe bağlıdır. Her isteğe tam görüşme geçmişini göndererek durum bilgisiz modda da çalışabilirsiniz.

### Veri depolama ve saklama

API, varsayılan olarak sunucu tarafı durum yönetimi özelliklerinin (`previous_interaction_id` ile), arka planda yürütmenin (`background=true` kullanılarak) ve gözlemlenebilirlik amaçlarının kullanımını basitleştirmek için tüm Interaction nesnelerini (`store=true`) saklar.

- **Ücretli katman**: Sistem, etkileşimleri **55 gün** boyunca saklar.
- **Ücretsiz katman**: Sistem, etkileşimleri **1 gün** boyunca saklar.

Bunu istemiyorsanız isteğinizde `store=false` ayarlayabilirsiniz. Bu kontrol, durum yönetiminden ayrıdır. Herhangi bir etkileşim için depolamayı devre dışı bırakabilirsiniz. Ancak `store=false` ile `background=true`'nin uyumsuz olduğunu ve sonraki dönüşlerde `previous_interaction_id`'nin kullanılmasını engellediğini unutmayın.

[API Referansı](https://ai.google.dev/api/interactions-api?hl=tr)'nda bulunan silme yöntemini kullanarak depolanan etkileşimleri istediğiniz zaman silebilirsiniz. Yalnızca etkileşim kimliğini biliyorsanız etkileşimleri silebilirsiniz.

Saklama süresi sona erdikten sonra verileriniz otomatik olarak silinir.

Sistem, Etkileşim nesnelerini [şartlara](https://ai.google.dev/gemini-api/terms?hl=tr) göre işler.

## En iyi uygulamalar

- **Önbellek isabet oranı**: Sohbetlere devam etmek için `previous_interaction_id` kullanıldığında sistem, sohbet geçmişi için örtülü önbelleğe almayı daha kolay kullanabilir. Bu da performansı artırır ve maliyetleri düşürür.
- **Etkileşimleri karıştırma**: Bir görüşmede Aracı ve Model etkileşimlerini karıştırıp eşleştirebilirsiniz. Örneğin, ilk veri toplama işlemi için Deep Research aracısı gibi özel bir aracı kullanabilir, ardından özetleme veya yeniden biçimlendirme gibi takip görevleri için standart bir Gemini modeli kullanabilirsiniz. Bu adımları `previous_interaction_id` ile bağlayabilirsiniz.

## Desteklenen modeller ve aracıları

| Model Adı | Tür | Model Kimliği |
| --- | --- | --- |
| Gemini 3.5 Flash | Model | `gemini-3.5-flash` |
| Gemini 3.1 Flash-Lite | Model | `gemini-3.1-flash-lite` |
| Gemini 3.1 Pro Önizlemesi | Model | `gemini-3.1-pro-preview` |
| Gemini 3 Flash Önizlemesi | Model | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Model | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Model | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | Model | `gemini-2.5-flash-lite` |
| Lyria 3 Clip Preview | Model | `lyria-3-clip-preview` |
| Lyria 3 Pro Önizlemesi | Model | `lyria-3-pro-preview` |
| Deep Research Önizlemesi | Temsilci | `deep-research-pro-preview-12-2025` |
| Deep Research Önizlemesi | Temsilci | `deep-research-preview-04-2026` |
| Deep Research Önizlemesi | Temsilci | `deep-research-max-preview-04-2026` |

## SDK'lar

Etkileşimler API'sine erişmek için Google GenAI SDK'larının en son sürümünü kullanabilirsiniz.

- Python'da bu, `1.55.0` sürümünden itibaren `google-genai` paketidir.
- JavaScript'te bu, `1.33.0` sürümünden itibaren `@google/genai` paketidir.

SDK'ları nasıl yükleyeceğiniz hakkında daha fazla bilgiyi [Kitaplıklar](https://ai.google.dev/gemini-api/docs/libraries?hl=tr) sayfasında bulabilirsiniz.

## Sınırlamalar

- **Beta durumu**: Etkileşimler API'si beta/önizleme sürümündedir. Özellikler ve şemalar değişebilir.
- **Uzak MCP**: Gemini 3, uzak MCP'yi desteklemez. Bu özellik yakında kullanıma sunulacaktır.

Aşağıdaki özellikler [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=tr) API tarafından desteklenir ancak Interactions API'de **henüz kullanılamaz**:

- **[Video meta verileri](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=tr)**: Video anlayışı için klip aralıklarını ve özel kare hızlarını ayarlamak üzere kullanılan `video_metadata` alanı.
- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr)**
- **[Otomatik işlev çağırma (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=tr#automatic_function_calling_python_only)**
- **[Açık önbelleğe alma](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=tr)**: Sunucu tarafında örtülü önbelleğe almanın, `previous_interaction_id` aracılığıyla Etkileşimler API'sinde kullanılabildiğini unutmayın.

## Zarar veren değişiklikler

Etkileşimler API'si şu anda erken beta aşamasındadır. API özelliklerini, kaynak şemalarını ve SDK arayüzlerini gerçek hayattaki kullanıma ve geliştirici geri bildirimlerine göre aktif olarak geliştirip iyileştiriyoruz. Bu nedenle, **uyumluluğu bozan değişiklikler olabilir**.

Mevcut zarar veren değişiklikler:

- **Adımlar şeması**: Çıkışlar dizisinin yerini alan yeni bir adımlar dizisi, her etkileşim dönüşünün yapılandırılmış zaman çizelgesini sağlar.

En son zarar veren değişiklik hakkında bilgi edinmek ve nasıl taşıma yapacağınızı öğrenmek için [Zarar veren değişikliklerle ilgili taşıma rehberine (Mayıs 2026)](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=tr) göz atın.

Diğer olası güncellemeler arasında giriş ve çıkış şemaları, SDK yöntemi imzaları ve nesne yapıları ile belirli özellik davranışlarındaki değişiklikler yer alabilir.

Üretim iş yükleri için standart [`generateContent`](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=tr) API'yi kullanmaya devam etmeniz gerekir. Bu API, kararlı dağıtımlar için önerilen yol olmaya devam edecek ve aktif olarak geliştirilip bakımı yapılacaktır.

## Geri bildirim

Geri bildirimleriniz, Etkileşimler API'sinin geliştirilmesi açısından büyük önem taşır.
Düşüncelerinizi paylaşmak, hataları bildirmek veya özellik isteğinde bulunmak için [Google Yapay Zeka Geliştirici Topluluğu Forumu](https://discuss.ai.google.dev/c/gemini-api/4?hl=tr)'nu kullanabilirsiniz.

## Sırada ne var?

- [Etkileşimler API'si hızlı başlangıç not defterini](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=tr) deneyin.
- Gerçek zamanlı yanıt işleme için [Yayın etkileşimleri](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=tr) hakkında bilgi edinin.
- [Gemini Deep Research Agent](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=tr) hakkında daha fazla bilgi edinin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-04 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-04 UTC."],[],[]]
