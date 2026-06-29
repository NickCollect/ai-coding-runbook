---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=tr
fetched_at: 2026-06-29T05:28:34.040303+00:00
title: "Sorun giderme k\u0131lavuzu \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Sorun giderme kılavuzu

Gemini API'yi çağırırken ortaya çıkan yaygın sorunları teşhis edip çözmenize yardımcı olması için bu kılavuzu kullanın. Gemini API arka uç hizmeti veya istemci SDK'ları ile ilgili sorunlarla karşılaşabilirsiniz. İstemci SDK'larımız aşağıdaki depolarda açık kaynaklıdır:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

API anahtarıyla ilgili sorunlarla karşılaşırsanız [API anahtarı kurulum kılavuzuna](https://ai.google.dev/gemini-api/docs/api-key?hl=tr) göre API anahtarınızı doğru şekilde ayarladığınızı doğrulayın.

## Gemini API arka uç hizmeti hata kodları

Aşağıdaki tabloda, karşılaşabileceğiniz yaygın arka uç hata kodları, nedenlerinin açıklamaları ve sorun giderme adımları listelenmiştir:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **HTTP Kodu** | **Durum** | **Açıklama** | **Örnek** | **Çözüm** |
| 400 | INVALID\_ARGUMENT | İstek metni yanlış biçimlendirilmiş. | İsteğinizde yazım hatası var veya zorunlu bir alan eksik. | İstek biçimi, örnekler ve desteklenen sürümler için [API referansına](https://ai.google.dev/api?hl=tr) bakın. Daha yeni bir API sürümündeki özellikleri daha eski bir uç nokta ile kullanmak hatalara neden olabilir. |
| 400 | FAILED\_PRECONDITION | Gemini API ücretsiz katmanı ülkenizde kullanılamıyor. Lütfen Google AI Studio'da projenizde faturalandırmayı etkinleştirin. | Ücretsiz katmanın desteklenmediği bir bölgede istekte bulunuyorsunuz ve Google AI Studio'da projenizde faturalandırmayı etkinleştirmediniz. | Gemini API'yi kullanmak için [Google AI Studio](https://aistudio.google.com/apikey?hl=tr)'yu kullanarak ücretli bir plan oluşturmanız gerekir. |
| 403 | PERMISSION\_DENIED | API anahtarınız gerekli izinlere sahip değil. | Yanlış API anahtarını kullanıyorsunuz veya [uygun kimlik doğrulama](https://ai.google.dev/gemini-api/docs/model-tuning?hl=tr) işleminden geçmeden ayarlanmış bir modeli kullanmaya çalışıyorsunuz. | API anahtarınızın ayarlandığından ve doğru erişime sahip olduğundan emin olun. Ayrıca, ince ayarlı modelleri kullanmak için uygun kimlik doğrulama sürecinden geçtiğinizden emin olun. |
| 404 | NOT\_FOUND | İstenen kaynak bulunamadı. | İsteğinizde referans verilen bir resim, ses veya video dosyası bulunamadı. | İsteğinizdeki tüm [parametrelerin API sürümünüz için geçerli olup olmadığını](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=tr#check-api) kontrol edin. |
| 429 | RESOURCE\_EXHAUSTED | API'nin hız sınırlarından birini (RPM, TPM, RPD, harcama vb.) aştınız. | Çok fazla istek gönderiyor, çok fazla jeton kullanıyor veya hesabınızın fatura geçmişi ve katmanı için harcamaya dayalı sınırları aşıyor olabilirsiniz. | Modelin [hız sınırları](https://ai.google.dev/gemini-api/docs/rate-limits?hl=tr) dahilinde olduğunuzu doğrulayın. Bekleyin ve kısa bir süre sonra tekrar deneyin. İsteklerinizin sıklığını veya boyutunu azaltın. Gerekirse [hız sınırı artışı isteyin](https://ai.google.dev/gemini-api/docs/rate-limits?hl=tr#request-rate-limit-increase). |
| 499 | İPTAL EDİLDİ | İşlem, genellikle arayan tarafından iptal edildi. | İstemci, API yanıt vermeyi tamamlamadan önce bağlantıyı kapattı. | İstemcinizin veya ağ altyapınızın bağlantıyı erken kapatıp kapatmadığını kontrol edin (ör. istemci tarafında zaman aşımı nedeniyle). |
| 500 | ŞİRKET İÇİ | Google'dan kaynaklanan beklenmeyen bir hata oluştu. | Giriş bağlamınız çok uzun. | Devam eden olaylar için [Gemini API durum sayfasını](https://aistudio.google.com/status?hl=tr) kontrol edin. Giriş bağlamınızı azaltın veya geçici olarak başka bir modele (ör. Gemini 2.5 Pro'dan Gemini 2.5 Flash'e) geçip sorunun çözülüp çözülmediğini kontrol edin. Dilerseniz biraz bekleyip isteğinizi yeniden deneyebilirsiniz. Yeniden denedikten sonra sorun devam ederse lütfen Google AI Studio'daki **Geri bildirim gönder** düğmesini kullanarak sorunu bildirin. |
| 503 | UNAVAILABLE | Hizmet geçici olarak aşırı yüklü veya kapalı olabilir. | Hizmetin kapasitesi geçici olarak dolmuş olabilir. | Devam eden olaylar için [Gemini API durum sayfasını](https://aistudio.google.com/status?hl=tr) kontrol edin. Geçici olarak başka bir modele (ör. Gemini 2.5 Pro'dan Gemini 2.5 Flash'e) geçip çalışıp çalışmadığını kontrol edin. Dilerseniz biraz bekleyip isteğinizi yeniden deneyebilirsiniz. Yeniden denedikten sonra sorun devam ederse lütfen Google AI Studio'daki **Geri bildirim gönder** düğmesini kullanarak sorunu bildirin. |
| 504 | DEADLINE\_EXCEEDED | Hizmet, işleme işlemini son tarihe kadar tamamlayamıyor. | İsteminiz (veya bağlamınız), zamanında işlenemeyecek kadar büyük. | Bu hatayı önlemek için istemci isteğinizde daha büyük bir "zaman aşımı" ayarlayın. |

## API çağrılarınızda model parametresi hataları olup olmadığını kontrol edin

Model parametrelerinizin aşağıdaki değerler içinde olduğunu doğrulayın:

|  |  |
| --- | --- |
| **Model parametresi** | **Değerler (aralık)** |
| Aday sayısı | 1-8 (tam sayı) |
| Sıcaklık | 0,0-1,0 |
| Maksimum çıkış jetonu sayısı | Kullandığınız modelin maksimum jeton sayısını belirlemek için [modeller sayfasını](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr) kullanın. |
| TopP | 0,0-1,0 |

Parametre değerlerini kontrol etmenin yanı sıra doğru [API sürümünü](https://ai.google.dev/gemini-api/docs/api-versions?hl=tr) (ör. `/v1` veya `/v1beta`) ve ihtiyacınız olan özellikleri destekleyen modeli kullandığınızdan emin olun. Örneğin, bir özellik beta sürümündeyse yalnızca `/v1beta` API sürümünde kullanılabilir.

## Doğru modele sahip olup olmadığınızı kontrol etme

[Modeller sayfamızda](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr) listelenen desteklenen bir modeli kullandığınızı doğrulayın.

## 2.5 modellerinde daha yüksek gecikme veya jeton kullanımı

2.5 Flash ve Pro modellerinde daha yüksek gecikme süresi veya jeton kullanımı gözlemliyorsanız bunun nedeni, kaliteyi artırmak için **düşünme özelliğinin varsayılan olarak etkinleştirilmiş** olması olabilir. Hıza öncelik veriyorsanız veya maliyetleri en aza indirmeniz gerekiyorsa düşünme sürecini ayarlayabilir ya da devre dışı bırakabilirsiniz.

Yol gösterici bilgiler ve örnek kod için [düşünme sayfasına](https://ai.google.dev/gemini-api/docs/thinking?hl=tr#set-budget) bakın.

## Güvenlik sorunları

API çağrınızdaki bir güvenlik ayarı nedeniyle istemin engellendiğini görürseniz istemi, API çağrısında ayarladığınız filtrelere göre inceleyin.

`BlockedReason.OTHER` simgesini görüyorsanız sorgu veya yanıt, [Hizmet Şartları](https://ai.google.dev/terms?hl=tr)'nı ihlal ediyor ya da başka bir şekilde desteklenmiyor olabilir.

## Okuma sorunu

Modelin, RECITATION (Tekrar) nedeniyle çıkış oluşturmayı durdurduğunu görüyorsanız bu, model çıkışının belirli verilere benzeyebileceği anlamına gelir. Bu sorunu düzeltmek için istemi / bağlamı mümkün olduğunca benzersiz hale getirmeyi ve daha yüksek bir sıcaklık kullanmayı deneyin.

## Tekrarlanan jeton sorunu

Çıkış jetonlarının tekrarlandığını görüyorsanız bunları azaltmak veya tamamen ortadan kaldırmak için aşağıdaki önerileri deneyin.

| Açıklama | Neden | Önerilen geçici çözüm |
| --- | --- | --- |
| Markdown tablolarında tekrarlanan tireler | Model, görsel olarak hizalanmış bir Markdown tablosu oluşturmaya çalıştığı için tablonun içeriği uzun olduğunda bu durum ortaya çıkabilir. Ancak Markdown'da doğru oluşturma için hizalama gerekli değildir. | İsteminizde, modele Markdown tabloları oluşturmayla ilgili belirli yönergeler verecek talimatlar ekleyin. Bu yönergelere uygun örnekler verin. Sıcaklığı ayarlamayı da deneyebilirsiniz. Kod oluşturma veya Markdown tabloları gibi çok yapılandırılmış çıkışlar için yüksek sıcaklık değerlerinin daha iyi sonuç verdiği görülmüştür (>= 0,8).  Bu sorunu önlemek için isteminize ekleyebileceğiniz yönergelerle ilgili örnekleri aşağıda bulabilirsiniz:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Markdown tablolarında tekrarlanan jetonlar | Tekrarlanan tirelere benzer şekilde, bu durum model tablo içeriklerini görsel olarak hizalamaya çalıştığında ortaya çıkar. Doğru oluşturma için Markdown'da hizalama gerekmez. | - Sistem isteminize aşağıdakiler gibi talimatlar eklemeyi deneyin:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Sıcaklığı ayarlamayı deneyin. Daha yüksek sıcaklıklar (>= 0,8), çıkıştaki tekrarları veya kopyaları ortadan kaldırmaya yardımcı olur. |
| Yapılandırılmış çıkışta tekrar eden yeni satırlar (`\n`) | Model girişi, `\u` veya `\t` gibi Unicode ya da kaçış dizileri içerdiğinde tekrarlanan yeni satırlara yol açabilir. | - İsteminizde yasaklanmış kaçış dizilerini UTF-8 karakterleriyle değiştirin. Örneğin, JSON örneklerinizdeki `\u`   kaçış dizisi, modelin çıkışında da bunları kullanmasına neden olabilir. - Modele izin verilen kaçış karakterleri hakkında talimat verin. Aşağıdaki gibi bir sistem talimatı ekleyin:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Yapılandırılmış çıktı kullanılarak metnin tekrar edilmesi | Model çıkışında alanların sırası, tanımlanan yapılandırılmış şemadan farklı olduğunda metin tekrarı oluşabilir. | - İsteminizde alanların sırasını belirtmeyin. - Tüm çıkış alanlarını zorunlu hale getirin. |
| Tekrarlanan araç çağrısı | Bu durum, modelin önceki düşüncelerin bağlamını kaybetmesi ve/veya kullanılamayan bir uç noktayı çağırmaya zorlanması durumunda ortaya çıkabilir. | Modele, düşünce sürecinde durumu koruması talimatını verin. Bunu sistem talimatlarınızın sonuna ekleyin:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Yapılandırılmış çıktının parçası olmayan tekrarlayan metin | Bu durum, modelin çözemediği bir istekte takılıp kalması halinde ortaya çıkabilir. | - Düşünme özelliği etkinse talimatlarda bir sorunu nasıl düşüneceğinizle ilgili açıkça emir vermeyin. Yalnızca son çıktıyı isteyin. - Daha yüksek bir sıcaklık (ör. >= 0,8) deneyin. - "Kısa ve öz ol", "Kendini tekrar etme" veya "Cevabı bir kez ver" gibi talimatlar ekleyin. |

## Engellenmiş veya çalışmayan API anahtarları

Bu bölümde, Gemini API anahtarınızın engellenip engellenmediğini nasıl kontrol edeceğiniz ve bu durumda ne yapmanız gerektiği açıklanmaktadır.

### Anahtarların neden engellendiğini anlama

Bazı API anahtarlarının herkese açık olarak kullanılabildiği bir güvenlik açığı tespit ettik. Verilerinizi korumak ve yetkisiz erişimi önlemek için, sızdırıldığı bilinen bu anahtarların Gemini API'ye erişimini proaktif olarak engelledik.

### Anahtarlarınızın etkilenip etkilenmediğini onaylayın

Anahtarınızın sızdırıldığı biliniyorsa bu anahtarı artık Gemini API ile kullanamazsınız. API anahtarlarınızdan herhangi birinin Gemini API'yi çağırmasının engellenip engellenmediğini görmek ve yeni anahtarlar oluşturmak için [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=tr)'yu kullanabilirsiniz. Bu anahtarları kullanmaya çalışırken aşağıdaki hatayı da görebilirsiniz:

```
Your API key was reported as leaked. Please use another API key.
```

### Engellenen API anahtarları için işlem

[Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=tr)'yu kullanarak Gemini API entegrasyonlarınız için yeni API anahtarları oluşturmanız gerekir. Yeni anahtarlarınızın güvenli bir şekilde saklandığından ve herkese açık olmadığından emin olmak için API anahtarı yönetim uygulamalarınızı gözden geçirmenizi önemle tavsiye ederiz.

### Güvenlik açığı nedeniyle beklenmedik ücretler

[Faturalandırma konusunda destek kaydı gönderin](https://console.cloud.google.com/support/chat?hl=tr).
Fatura ekibimiz bu konu üzerinde çalışıyor. Güncellemeleri en kısa sürede sizinle paylaşacağız.

### Google'ın sızdırılan anahtarlara yönelik güvenlik önlemleri

**API anahtarlarım sızdırılırsa Google, hesabımın maliyet aşımı ve kötüye kullanımdan korunmasına nasıl yardımcı olacak?**

- [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=tr)'yu kullanarak yeni bir anahtar istediğinizde API anahtarları vermeye başlıyoruz. Bu anahtarlar varsayılan olarak yalnızca Google AI Studio ile sınırlı olacak ve diğer hizmetlerden gelen anahtarlar kabul edilmeyecek.
  Bu, yanlışlıkla anahtar kullanımını önlemeye yardımcı olur.
- Sızdırılan ve Gemini API ile kullanılan API anahtarlarını varsayılan olarak engelliyoruz. Böylece maliyetin ve uygulama verilerinizin kötüye kullanılmasını önlemeye yardımcı oluyoruz.
- API anahtarlarınızın durumunu [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=tr)'da bulabilirsiniz. API anahtarlarınızın sızdırıldığını tespit ettiğimizde ise hemen harekete geçmeniz için proaktif olarak sizinle iletişime geçeriz.

## Model çıktısını iyileştirme

Daha kaliteli model çıkışları için daha yapılandırılmış istemler yazmayı deneyin. [İstem mühendisliği rehberi](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=tr) sayfasında, başlamanıza yardımcı olacak bazı temel kavramlar, stratejiler ve en iyi uygulamalar tanıtılmaktadır.

## Jeton sınırlarını anlama

Jetonların nasıl sayılacağını ve sınırlarını daha iyi anlamak için [Jeton kılavuzumuzu](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) inceleyin.

## Bilinen sorunlar

- API yalnızca belirli dilleri destekler. Desteklenmeyen dillerde istem göndermek beklenmedik veya hatta engellenen yanıtlar üretebilir. Güncellemeler için [kullanılabilir dilleri](https://ai.google.dev/gemini-api/docs/models?hl=tr#supported-languages) inceleyin.

## Hata bildir

Sorularınız varsa [Google Yapay Zeka geliştirici forumunda](https://discuss.ai.google.dev?hl=tr) tartışmaya katılın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-23 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-23 UTC."],[],[]]
