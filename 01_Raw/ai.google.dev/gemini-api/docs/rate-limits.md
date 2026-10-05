---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=tr
fetched_at: 2026-10-05T06:46:30.469829+00:00
title: "H\u0131z s\u0131n\u0131rlar\u0131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Hız sınırları

Sıklık sınırları, belirli bir zaman aralığında Gemini API'ye gönderebileceğiniz istek sayısını düzenler. Bu sınırlar, adil kullanımı sürdürmeye, kötüye kullanıma karşı korumaya ve tüm kullanıcılar için sistem performansını korumaya yardımcı olur.

[AI Studio'da etkin hız sınırlarınızı görüntüleme](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=tr)

## Hız sınırlarının işleyiş şekli

Hız sınırları genellikle üç boyutta ölçülür:

- Dakikada istek sayısı (**RPM**)
- Dakikada jeton sayısı (giriş) (**TPM**)
- Günlük istek sayısı (**RPD**)

Kullanımınız her sınıra göre değerlendirilir ve herhangi bir sınırı aşmanız durumunda sıklık sınırı hatası tetiklenir. Örneğin, RPM sınırınız 20 ise TPM veya diğer sınırlarınızı aşmamış olsanız bile bir dakika içinde 21 istekte bulunmanız hataya neden olur.

Hız sınırları API anahtarı başına değil, proje başına uygulanır. Günlük istek sayısı (**RPD**) kotaları, Pasifik saatine göre gece yarısında sıfırlanır.

Sınırlar, kullanılan modele göre değişir ve bazı sınırlar yalnızca belirli modeller için geçerlidir. Örneğin, dakikadaki görüntü sayısı (IPM) yalnızca görüntü oluşturabilen modeller (Nano Banana) için hesaplanır ancak kavramsal olarak TPM'ye benzer. Diğer modellerde günlük jeton sınırı (TPD) olabilir.

Hız sınırları, deneysel ve önizleme modellerinde daha kısıtlıdır.

### Harcamaya dayalı sıklık sınırları

Gemini API, dakika başına istek (RPM) ve dakika başına jeton (TPM) sınırlarına ek olarak, beklenmedik ücretlere karşı koruma sağlamak için harcamaya dayalı hız sınırlarını zorunlu kılar. Bu sınırların hesabınız için geçerli olup olmadığı, faturalandırma geçmişinize ve [kullanım katmanınıza](#usage-tiers) bağlıdır.

Aşağıdaki tabloda, her [kullanım katmanı](#usage-tiers) için harcamaya dayalı sıklık sınırları gösterilmektedir. Bu sınırlar, 10 dakikalık bir süre içinde değerlendirilir. Bu sınırların hesabınız için geçerli olup olmadığı, faturalandırma geçmişinize ve hesap durumunuza bağlıdır.

| Kullanım katmanı | Harcama hızı sınırı (10 dakikada bir) |
| --- | --- |
| **Ücretsiz** | Yok |
| **1. Katman** | 10 Hong Kong doları |
| **2. Katman** | 200 ABD doları |
| **3. Katman** | 200 ABD doları |

Harcamaya dayalı bir hız sınırına ulaşırsanız API, `429 RESOURCE_EXHAUSTED` hatası döndürür. Bu sorunu çözmek için:

- Kısa bir süre sonra **bekleyip tekrar deneyin**.
- **Pahalı isteklerin oranını azaltın**. Örneğin, daha küçük bağlam pencereleri veya daha kısa çıkışlar kullanın.
- Normal kullanım sırasında bu sınıra sürekli olarak ulaşıyorsanız [hız sınırı artışı isteğinde bulunun](#request-rate-limit-increase).

## Kullanım katmanları

Hız sınırları, projenin kullanım katmanına bağlıdır. API kullanımınız ve harcamanız arttıkça, daha yüksek hız sınırlarına sahip bir katmana otomatik olarak yükseltilirsiniz.

2. ve 3. katmanların şartları, projenize bağlı faturalandırma hesabı için Google Cloud hizmetlerine (Gemini API dahil ancak bununla sınırlı olmamak üzere) yapılan toplam kümülatif harcamaya dayanır.

| Kullanım katmanı | Eleme | [Faturalandırma katmanı sınırı](https://ai.google.dev/gemini-api/docs/billing?hl=tr#tier-spend-caps) |
| --- | --- | --- |
| **Ücretsiz** | [Etkin proje](https://ai.google.dev/gemini-api/docs/api-key?hl=tr#google-cloud-projects) veya ücretsiz deneme | Yok |
| **1. Katman** | [Etkin bir faturalandırma hesabı oluşturma ve bağlama](https://ai.google.dev/gemini-api/docs/billing?hl=tr#setup-billing) | 250 ABD Doları |
| **2. Katman** | 100 ABD doları + ilk başarılı ödemeden itibaren 3 gün | 2.000 ABD doları |
| **3. Katman** | 1.000 ABD doları + ilk başarılı ödemeden itibaren 30 gün | 20.000 ABD doları - 100.000 ABD doları ve üzeri |

Belirtilen uygunluk ölçütlerini karşılamak genellikle onay için yeterli olsa da nadir durumlarda inceleme süreci sırasında belirlenen diğer faktörlere bağlı olarak yükseltme isteği reddedilebilir.

Bu sistem, Gemini API platformunun tüm kullanıcılar için güvenliğini ve bütünlüğünü korumaya yardımcı olur.

## Gemini API hız sınırları

Hız sınırları, kullanım katmanınız gibi çeşitli faktörlere bağlıdır ve Google AI Studio'da görüntülenebilir. Zaman içinde katmanınız ve hesap durumunuz değiştikçe hız sınırlarınız otomatik olarak güncellenir.

[AI Studio'da etkin sıklık sınırlarınızı görüntüleme](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=tr)

Belirtilen hız sınırları garanti edilmez ve gerçek kapasite farklılık gösterebilir.

## Öncelik çıkarımı sıklık sınırları

[Öncelikli](https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr) tüketim, tüketim genel etkileşimli trafik hızı sınırlarına dahil edilse de kendi hız sınırlarına sahiptir. **Varsayılan sıklık sınırları: Her model ve katman için [standart sıklık sınırının](https://aistudio.google.com/rate-limit?hl=tr) 0,3 katı**

## Batch API hız sınırları

[Toplu API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr) istekleri, toplu olmayan API çağrılarından ayrı olarak kendi hız sınırlamalarına tabidir.

- **Eşzamanlı toplu istek sayısı:** 100
- **Giriş dosyasının boyut sınırı:** 2 GB
- **Dosya depolama alanı sınırı:** 20 GB
- **Model başına sıraya alınan jetonlar:** **Toplu iş için sıraya alınan jetonlar** tablosunda, belirli bir model için tüm etkin toplu işlerinizde toplu işleme için sıraya alınabilecek maksimum jeton sayısı listelenir.

### Katman 1

| Model | Toplu olarak sıraya alınan jetonlar |
| --- | --- |
| Metin çıkışı modelleri | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro Önizlemesi | 5.000.000 |
| Gemini 3.5 Flash-Lite | 10.000.000 |
| Gemini 3.1 Flash Lite | 10.000.000 |
| Gemini 3.1 Flash Lite Önizlemesi | 10.000.000 |
| Gemini 3.6 Flash | 3.000.000 |
| Gemini 3.5 Flash | 3.000.000 |
| Gemini 2.5 Pro | 5.000.000 |
| Gemini 2.5 Pro TTS | 25.000 |
| Gemini 2.5 Flash | 3.000.000 |
| Gemini 2.5 Flash Önizlemesi | 3.000.000 |
| Gemini 2.5 Flash Image Önizlemesi | 3.000.000 |
| Gemini 2.5 Flash TTS | 100.000 |
| Gemini 2.5 Flash Lite | 10.000.000 |
| Gemini 2.5 Flash Lite Önizlemesi | 10.000.000 |
| Gemini 2.0 Flash | 10.000.000 |
| Gemini 2.0 Flash Görüntüsü | 3.000.000 |
| Gemini 2.0 Flash Lite | 10.000.000 |
| Çok formatlı üretken modeller | | | | |
| Gemini 3.1 Flash Image Preview 🍌 | 1.000.000 |
| Gemini 3.1 Flash Lite Image 🍌 | 2.000.000 |
| Gemini 3 Pro ile görüntü önizlemesi 🍌 | 2.000.000 |
| Yerleştirme modelleri | | | | |
| Gemini Yerleştirme | 500.000 |

### Katman 2

| Model | Toplu olarak sıraya alınan jetonlar |
| --- | --- |
| Metin çıkışı modelleri | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro Önizlemesi | 500.000.000 |
| Gemini 3.5 Flash-Lite | 500.000.000 |
| Gemini 3.1 Flash Lite | 500.000.000 |
| Gemini 3.1 Flash Lite Önizlemesi | 500.000.000 |
| Gemini 3.6 Flash | 400.000.000 |
| Gemini 3.5 Flash | 400.000.000 |
| Gemini 2.5 Pro | 500.000.000 |
| Gemini 2.5 Pro TTS | 100.000 |
| Gemini 2.5 Flash | 400.000.000 |
| Gemini 2.5 Flash Önizlemesi | 400.000.000 |
| Gemini 2.5 Flash Image Önizlemesi | 400.000.000 |
| Gemini 2.5 Flash TTS | 100.000 |
| Gemini 2.5 Flash Lite | 500.000.000 |
| Gemini 2.5 Flash Lite Önizlemesi | 500.000.000 |
| Gemini 2.0 Flash | 1.000.000.000 |
| Gemini 2.0 Flash Görüntüsü | 400.000.000 |
| Gemini 2.0 Flash Lite | 1.000.000.000 |
| Çok formatlı üretken modeller | | | | |
| Gemini 3.1 Flash Image Preview 🍌 | 250.000.000 |
| Gemini 3.1 Flash Lite Image 🍌 | 270.000.000 |
| Gemini 3 Pro ile görüntü önizlemesi 🍌 | 270.000.000 |
| Yerleştirme modelleri | | | | |
| Gemini Yerleştirme | 5.000.000 |

### 3. Katman

| Model | Toplu olarak sıraya alınan jetonlar |
| --- | --- |
| Metin çıkışı modelleri | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro Önizlemesi | 1.000.000.000 |
| Gemini 3.5 Flash-Lite | 1.000.000.000 |
| Gemini 3.1 Flash Lite | 1.000.000.000 |
| Gemini 3.1 Flash Lite Önizlemesi | 1.000.000.000 |
| Gemini 3.6 Flash | 1.000.000.000 |
| Gemini 3.5 Flash | 1.000.000.000 |
| Gemini 2.5 Pro | 1.000.000.000 |
| Gemini 2.5 Pro TTS | 1.000.000 |
| Gemini 2.5 Flash | 1.000.000.000 |
| Gemini 2.5 Flash Önizlemesi | 1.000.000.000 |
| Gemini 2.5 Flash Image Önizlemesi | 1.000.000.000 |
| Gemini 2.5 Flash TTS | 4.000.000 |
| Gemini 2.5 Flash Lite | 1.000.000.000 |
| Gemini 2.5 Flash Lite Önizlemesi | 1.000.000.000 |
| Gemini 2.0 Flash | 5.000.000.000 |
| Gemini 2.0 Flash Görüntüsü | 1.000.000.000 |
| Gemini 2.0 Flash Lite | 5.000.000.000 |
| Çok formatlı üretken modeller | | | | |
| Gemini 3.1 Flash Image Preview 🍌 | 750.000.000 |
| Gemini 3.1 Flash Lite Image 🍌 | 1.000.000.000 |
| Gemini 3 Pro ile görüntü önizlemesi 🍌 | 1.000.000.000 |
| Yerleştirme modelleri | | | | |
| Gemini Yerleştirme | 10.000.000 |

## Bir sonraki katmana yükseltme

Ücretsiz katmandan ücretli bir katmana geçmek için önce [AI Studio'da faturalandırmayı ayarlamanız](https://ai.google.dev/gemini-api/docs/billing?hl=tr) gerekir.

Projeniz [belirtilen ölçütleri](#usage-tiers) karşıladığında otomatik olarak bir sonraki katmana yükseltilir. Ücretsiz katmandan 1. katmana yükseltme genellikle anında, sonraki katman yükseltmeleri ise 10 dakika içinde geçerlilik kazanır. Katmanlarınızı kontrol etmek için AI Studio'da [Projeler sayfasına](https://aistudio.google.com/projects?hl=tr) gidin.

## Oran sınırı artışı isteme

Her model varyasyonunun ilişkili bir sıklık sınırı (dakikadaki istek sayısı, RPM) vardır.
Bu hız sınırlarıyla ilgili ayrıntılar için [AI Studio Hız Sınırı](https://aistudio.google.com/rate-limit?hl=tr) sayfasına bakın.

[Ücretli katman için istek oranı sınırı artışı isteğinde bulunma](https://forms.gle/ETzX94k8jf7iSotH9)

Hız sınırınızı artıracağımız konusunda garanti vermiyoruz ancak isteğinizi incelemek için elimizden geleni yapacağız.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-12 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-12 UTC."],[],[]]
