---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=tr
fetched_at: 2026-10-26T05:42:56.295265+00:00
title: "Sorun giderme k\u0131lavuzu \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hemen oynayabilirsiniz. [Deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=tr).

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Sorun giderme kılavuzu

Gemini API'yi çağırırken ortaya çıkan yaygın sorunları teşhis edip çözmek için bu kılavuzdan yararlanabilirsiniz. Gemini API arka uç hizmetinden veya istemci SDK'larından kaynaklanan sorunlarla karşılaşabilirsiniz. İstemci SDK'larımız aşağıdaki depolarda açık kaynaklı olarak sunulur:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

API anahtarıyla ilgili sorunlarla karşılaşırsanız API anahtarınızı [API anahtarı kurulum kılavuzuna](https://ai.google.dev/gemini-api/docs/api-key?hl=tr) göre doğru şekilde ayarladığınızdan emin olun.

## Hata kodları

HTTP durum kodları, oluşturma engelleme kodları ve içerik hata kodları dahil olmak üzere tüm hata kodlarının tam listesi için [API hataları](https://ai.google.dev/gemini-api/docs/api-errors?hl=tr) sayfasını inceleyin.

## Yeniden deneme stratejisi

İsteğinizi yeniden denemeniz gerektiğini belirten bir hata (ör. `429 RESOURCE_EXHAUSTED` veya `503 UNAVAILABLE`) alırsanız eksponansiyel geri yükleme stratejisi uygulamanızı öneririz. Bu, ilk yeniden denemeden önce kısa bir süre beklediğiniz ve ardından sonraki yeniden denemeler arasındaki bekleme süresini kademeli olarak artırdığınız anlamına gelir.

Gemini API'nin resmi istemci SDK'ları (ör. [Python SDK](https://github.com/googleapis/python-genai)), zaman aşımı, ağ sorunları ve sıklık sınırlamaları (`429` ve `5xx` durum kodları) gibi geçici hataları işlemek için varsayılan olarak eksponansiyel geri yükleme ile otomatik yeniden deneme mantığı içerir. Örneğin, Python SDK'sı geçici hataları yaklaşık 1 saniyelik bir başlangıç gecikmesi ve maksimum 60 saniyelik bir gecikmeyle otomatik olarak dört kez yeniden dener.

Doğrudan REST API istekleri gönderiyorsanız veya yeniden deneme mantığınızı özelleştiriyorsanız başarılı bir istek olasılığını artırmak ve hizmetin aşırı yüklenmesini önlemek için aşağıdaki en iyi uygulamaları izleyin:

- **Eksponansiyel geri yükleme kullanın:** İlk yeniden denemeden önce kısa bir süre (ör. 1 saniye) bekleyin, ardından gecikmeyi üstel olarak artırın (ör. 2 sn, 4 sn, 8 sn).
- **Dalgalanma ekleme:** Tüm istemcilerin tam olarak aynı anda yeniden denemesini önlemek için gecikmeye rastgele "dalgalanma" ekleyin.
- **Belirli hatalarda yeniden deneyin:** Yalnızca geçici hatalarda (`429`, `408` veya `5xx` gibi) yeniden deneyin. Geçersiz API anahtarları, tükenmiş ön ödeme kredileri veya hatalı söz dizimi gibi sorunları gösteren istemci hatalarında (`400`, `402` veya `403` gibi) yeniden denemeyin.
- **Maksimum yeniden deneme sayısını ayarlayın:** Sonsuz döngüleri önlemek için maksimum yeniden deneme sayısı belirleyin.

## Model parametresi hataları için API çağrılarınızı kontrol etme

Model parametrelerinizin aşağıdaki değerler arasında olduğunu doğrulayın:

|  |  |
| --- | --- |
| **Model parametresi** | **Değerler (aralık)** |
| Aday sayısı | 1-8 (tam sayı) |
| Sıcaklık | 0,0-1,0 |
| Maksimum çıkış jetonu sayısı | Kullandığınız model için maksimum parça sayısını belirlemek üzere [modeller sayfasını](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr) kullanın. |
| TopP | 0,0-1,0 |

Parametre değerlerini kontrol etmenin yanı sıra doğru [API sürümünü](https://ai.google.dev/gemini-api/docs/api-versions?hl=tr) (ör. `/v1` veya `/v1beta`) ve ihtiyacınız olan özellikleri destekleyen modeli kullandığınızdan emin olun. Örneğin, bir özellik Beta sürümündeyse yalnızca `/v1beta` API sürümünde kullanılabilir.

## Doğru modele sahip olup olmadığınızı kontrol etme

[Modeller sayfamızda](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr) listelenen desteklenen modellerden birini kullandığınızı doğrulayın.

## Düşünebilen modellerde daha yüksek gecikme veya jeton kullanımı

Gemini 3.x modellerinde düşünme özelliği varsayılan olarak etkin olduğundan gecikme veya jeton kullanımı genellikle daha yüksektir. Desteği sonlandırılan Gemini 2.5 modelleri de varsayılan düşünme özelliğini kullanır.

Düşünen modeller, kaliteyi artırmak için dahili akıl yürütme jetonları üretir. Bu akıl yürütme süreci, hem yanıt gecikmesini hem de toplam jeton tüketimini artırır.

Daha düşük gecikme süresine öncelik veriyorsanız veya maliyetleri en aza indirmeniz gerekiyorsa düşünme seviyesini düşürebilir ya da düşünme özelliğini kapatabilirsiniz.

Yapılandırma ayrıntıları ve kod örnekleri için [düşünme kılavuzuna](https://ai.google.dev/gemini-api/docs/thinking?hl=tr#thinking-levels) bakın.

## Güvenlik sorunları

API çağrınızdaki bir güvenlik ayarı nedeniyle bir istemin engellendiğini görürseniz istemi, API çağrısında ayarladığınız filtrelere göre inceleyin.

`BlockedReason.OTHER` simgesini görüyorsanız sorgu veya yanıt, [hizmet şartlarını](https://ai.google.dev/terms?hl=tr) ihlal ediyor ya da başka bir nedenle desteklenmiyor olabilir.

## Okuma sorunu

Modelin RECITATION nedeniyle çıkış oluşturmayı durdurduğunu görürseniz bu, model çıktısının belirli verilere benzeyebileceği anlamına gelir. Bu sorunu düzeltmek için istemi / bağlamı mümkün olduğunca benzersiz hale getirmeye çalışın ve daha yüksek bir sıcaklık kullanın.

## Tekrarlanan jeton sorunu

Tekrarlanan çıkış jetonları görüyorsanız bunları azaltmak veya ortadan kaldırmak için aşağıdaki önerileri deneyin.

| Açıklama | Neden | Önerilen geçici çözüm |
| --- | --- | --- |
| Markdown tablolarında tekrarlanan kısa çizgiler | Bu durum, model görsel olarak hizalanmış bir Markdown tablosu oluşturmaya çalışırken tablonun içeriği uzun olduğunda ortaya çıkabilir. Ancak Markdown'da hizalama, doğru oluşturma için gerekli değildir. | Modele Markdown tabloları oluşturmayla ilgili belirli yönergeler vermek için isteminize talimatlar ekleyin. Bu kurallara uyan örnekler verin. Sıcaklığı ayarlamayı da deneyebilirsiniz. Kod veya Markdown tabloları gibi çok yapılandırılmış çıktılar oluşturmak için yüksek sıcaklığın (>= 0,8) daha iyi sonuç verdiği görülmüştür.  Aşağıda, bu sorunu önlemek için isteminize ekleyebileceğiniz örnek bir kural grubu verilmiştir:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Markdown tablolarında tekrarlanan jetonlar | Tekrarlanan tirelere benzer şekilde bu durum, model tablonun içeriğini görsel olarak hizalamaya çalıştığında ortaya çıkar. Markdown'da hizalama, doğru oluşturma için gerekli değildir. | - Sistem isteminize aşağıdaki gibi talimatlar eklemeyi deneyin:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Sıcaklığı ayarlamayı deneyin. Daha yüksek sıcaklıklar (>= 0,8) genellikle çıkıştaki tekrarları veya kopyaları ortadan kaldırmaya yardımcı olur. |
| Yapılandırılmış çıkışta tekrarlanan yeni satırlar (`\n`) | Model girişi, `\u` veya `\t` gibi Unicode ya da kaçış dizileri içerdiğinde yinelenen yeni satırlar oluşabilir. | - İsteminizde yasaklanmış çıkış dizileri olup olmadığını kontrol edin ve bunları UTF-8 karakterleriyle değiştirin. Örneğin, JSON örneklerinizdeki `\u` kaçış dizisi, modelin bunu çıktısında da kullanmasına neden olabilir. - Modele izin verilen çıkışlar hakkında talimat verin. Şuna benzer bir sistem talimatı ekleyin:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Yapılandırılmış çıkış kullanılırken tekrarlanan metin | Model çıkışındaki alanların sırası, tanımlanan yapılandırılmış şemadan farklı olduğunda metin tekrarlanabilir. | - İsteminizde alanların sırasını belirtmeyin. - Tüm çıkış alanlarını zorunlu hale getirin. |
| Tekrarlanan araç çağrıları | Bu durum, model önceki düşüncelerin bağlamını kaybederse ve/veya zorunlu olduğu kullanılamayan bir uç noktayı çağırırsa ortaya çıkabilir. | Modele, düşünme sürecinde durumu korumasını söyleyin. Sistem talimatlarınızın sonuna şunu ekleyin:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Yapılandırılmış çıkışın parçası olmayan tekrarlanan metinler | Bu durum, model çözemediği bir istekte takılı kaldığında ortaya çıkabilir. | - Düşünme özelliği etkinse talimatlarda bir sorunun nasıl ele alınacağına dair açık emirler vermekten kaçının. Yalnızca nihai çıktıyı isteyin. - Daha yüksek bir sıcaklık (>= 0,8) deneyin. - "Kısa ve öz ol", "Kendini tekrar etme" veya "Cevabı bir kez ver" gibi talimatlar ekleyin. |

## Proje kısıtlanmış veya kullanılamıyor

API istekleriniz `403 PERMISSION_DENIED` ("Projenizin erişimi reddedildi") hatası döndürüyorsa veya projenizin durumu [Google AI Studio](https://aistudio.google.com/?hl=tr)'da **Kısıtlı**, **Ücretsiz katman kullanılamıyor**, **Ödeme gerekli** ya da **Kullanılamıyor** olarak görünüyorsa projeniz için aşağıdaki bölümlerden hangisinin geçerli olduğunu kontrol edin:

### Gemini API ücretsiz katmanının kullanılamaması

Tüm Google Cloud projeleri veya hesapları Gemini API ücretsiz katmanına uygun değildir. Projenizin ücretsiz katmanı kullanması kısıtlanmışsa:

- **Aynı projede yeni bir API anahtarı oluşturmak hatayı çözmez.**
  Google, uygunluğu Google Cloud projesi düzeyinde değerlendirir.
- **Gemini API'yi bu projede kullanmak için etkin bir [Cloud Faturalandırma Hesabı](https://aistudio.google.com/billing?hl=tr) bağlayarak ücretli katmana geçmeniz gerekir**.
- Not: Bir projeyi ücretli katmana yükseltmek, ücretsiz katman kotasının kilidini açmaz.
  Google, ücretli katman kullanımını [Gemini API fiyatlandırmasına](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) göre faturalandırır veya uygun Google Cloud kredilerinden düşer.

### Cloud Faturalandırma Hesabı ödemesi gerekiyor

Projeniz bir Cloud Faturalandırma Hesabı'na bağlıysa ve **Ödeme gerekiyor** ifadesini gösteriyorsa (veya ödenmemiş bakiye nedeniyle `403 PERMISSION_DENIED` hatası veriyorsa):

- Ödenmemiş bakiyeyi kapatmak veya ödeme yönteminizi güncellemek için [AI Studio Faturalandırma sayfasını](https://aistudio.google.com/billing?hl=tr) ya da [Google Cloud Billing Konsolu](https://console.cloud.google.com/billing?hl=tr)'nu ziyaret edin.
- Faturalandırma hesabınız tekrar iyi duruma geldiğinde projeniz API erişimini otomatik olarak yeniden kazanır.

### Sızdırılan veya engellenen API anahtarları

`403 PERMISSION_DENIED` hata durumu, API anahtarınızın sızdırıldığını veya engellendiğini belirtiyorsa:

- Yeni bir API anahtarı oluşturmak ve uygulama kimlik bilgilerinizi güncellemek için [AI Studio API Anahtarları sayfasına](https://aistudio.google.com/apikeys?hl=tr) gidin.
- API anahtarlarını hiçbir zaman doğrudan istemci tarafı koduna veya herkese açık depolara yerleştirmeyin.

### Proje veya faturalandırma hesabı politikası nedeniyle askıya alınma

Google, bir politika ihlali nedeniyle Google Cloud projenizi veya Cloud Faturalandırma Hesabınızı askıya alırsa ilişkili e-posta adresini kontrol edin. Askıya alma bildirimlerini incelemek için [Google Cloud Console](https://console.cloud.google.com/?hl=tr)'u ziyaret edin ve [Proje Askıya Alma Kuralları](https://cloud.google.com/resource-manager/docs/project-suspension-guidelines?hl=tr)'nı uygulayın.

## Engellenen veya çalışmayan API anahtarları

Bu bölümde, Gemini API anahtarınızın engellenip engellenmediğini nasıl kontrol edeceğiniz ve bu durumda ne yapmanız gerektiği açıklanmaktadır.

### Anahtarların neden engellendiğini anlama

Bazı API anahtarlarının herkese açık olarak ifşa edilmiş olabileceği bir güvenlik açığı tespit ettik. Verilerinizi korumak ve yetkisiz erişimi önlemek için, sızdırıldığı bilinen bu anahtarların Gemini API'ye erişimini proaktif olarak engelledik.

### Anahtarlarınızın etkilenip etkilenmediğini doğrulama

Anahtarınızın sızdırıldığı biliniyorsa bu anahtarı artık Gemini API ile kullanamazsınız. API anahtarlarınızdan herhangi birinin Gemini API'yi çağırmasının engellenip engellenmediğini görmek ve yeni anahtarlar oluşturmak için [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=tr)'yu kullanabilirsiniz. Bu anahtarları kullanmaya çalışırken aşağıdaki hatayı da görebilirsiniz:

```
Your API key was reported as leaked. Please use another API key.
```

### Engellenen API anahtarları için işlem

[Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=tr)'yu kullanarak Gemini API entegrasyonlarınız için yeni API anahtarları oluşturmanız gerekir. Yeni anahtarlarınızın güvende tutulması ve herkese açık olarak gösterilmemesi için API anahtarı yönetimi uygulamalarınızı gözden geçirmenizi önemle tavsiye ederiz.

### Güvenlik açığı nedeniyle beklenmedik ücretler

[Faturalandırma destek kaydı gönderme](https://console.cloud.google.com/support/chat?hl=tr)
Faturalandırma ekibimiz bu konu üzerinde çalışıyor. Gelişmeleri en kısa sürede paylaşacağız.

### Sızdırılan anahtarlar için Google'ın güvenlik önlemleri

**API anahtarlarım sızdırılırsa Google, hesabımı bütçe aşımına ve kötüye kullanıma karşı korumaya nasıl yardımcı olacak?**

- [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=tr)'yu kullanarak yeni bir anahtar istediğinizde API anahtarları vermeye başlıyoruz. Bu anahtarlar varsayılan olarak yalnızca Google AI Studio ile sınırlı olacak ve diğer hizmetlerden anahtar kabul etmeyecek.
  Bu sayede, anahtarların istenmeyen şekilde çapraz kullanımı önlenir.
- Sızdırılan ve Gemini API ile kullanılan API anahtarlarını varsayılan olarak engelleyerek maliyetlerin ve uygulama verilerinizin kötüye kullanılmasını önlemeye yardımcı oluyoruz.
- API anahtarlarınızın durumunu [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key?hl=tr)'da bulabilirsiniz. API anahtarlarınızın sızdırıldığını tespit ettiğimizde hemen harekete geçebilmeniz için proaktif olarak iletişim kurmaya çalışacağız.

## Model çıktısını iyileştirme

Daha yüksek kaliteli model çıkışları için daha yapılandırılmış istemler yazmayı deneyin. [İstem mühendisliği kılavuzu](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=tr) sayfasında, başlamanıza yardımcı olacak bazı temel kavramlar, stratejiler ve en iyi uygulamalar tanıtılmaktadır.

## Jeton sınırlarını anlama

Jetonların nasıl sayılacağını ve sınırlarını daha iyi anlamak için [Jeton kılavuzumuzu](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) okuyun.

## Bilinen sorunlar

- API yalnızca belirli dilleri destekler. Desteklenmeyen dillerde istem gönderildiğinde beklenmedik veya engellenen yanıtlar alınabilir. Güncellemeler için [kullanılabilir dilleri](https://ai.google.dev/gemini-api/docs/models?hl=tr#supported-languages) inceleyin.

## Hata bildir

Sorularınız varsa [Google AI geliştirici forumunda](https://discuss.ai.google.dev?hl=tr) tartışmaya katılın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-23 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-23 UTC."],[],[]]
