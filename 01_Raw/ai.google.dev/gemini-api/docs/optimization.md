---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=tr
fetched_at: 2026-06-01T05:59:32.132628+00:00
title: "Gemini API optimizasyonu ve \u00e7\u0131kar\u0131m\u0131 \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini API optimizasyonu ve çıkarımı

Gemini API, belirli iş yükü ihtiyaçlarınıza göre hız, maliyet ve güvenilirlik arasında denge kurmanıza yardımcı olacak çeşitli optimizasyon mekanizmaları sunar.
İster gerçek zamanlı sohbet botları oluşturuyor ister yoğun çevrimdışı veri işleme işlem hatları çalıştırıyor olun, doğru paradigmayı seçmek maliyetleri önemli ölçüde azaltabilir veya performansı artırabilir.

| Özellik | Standart | Yaratıcılığınızı | Öncelik | Toplu | Önbelleğe alma |
| --- | --- | --- | --- | --- | --- |
| **Fiyatlandırma** | Tam Fiyat | %50 indirim | Standarttan% 75 ila% 100 daha fazla | %50 indirim | %90 indirim + Kullanıma göre hesaplanan jeton depolama alanı |
| **Gecikme** | Saniyelerden dakikalara | Dakikalar (1-15 dakika hedef) | Saniye | En fazla 24 saat | Daha hızlı ilk jeton süresi |
| **Güvenilirlik** | Yüksek / Biraz yüksek | En iyi sonuç (Sheddable) | Yüksek (tüy dökmeyen) | Yüksek (işleme hızı için) | Yok |
| **Arayüz** | Senkronize | Senkronize | Senkronize | Eşzamansız | Kaydedilmiş durum |
| **En iyi kullanım alanı** | Genel uygulama iş akışları | Acil olmayan sıralı zincirler | Üretim, kullanıcıya yönelik uygulamalar | Büyük veri kümeleri, çevrimdışı değerlendirmeler | Aynı dosya üzerinde yinelenen sorgular |

## Çıkarım hizmeti katmanları (Eşzamanlı)

Standart oluşturma çağrılarınızda `service_tier` parametresini ileterek güvenilirlik için optimize edilmiş ve maliyet için optimize edilmiş senkron trafik arasında geçiş yapabilirsiniz.

### Standart çıkarım (varsayılan)

Standart katman, sıralı içerik oluşturma için varsayılan seçenektir.
Ek primler veya yoğun kuyruklar olmadan normal yanıt süreleri sağlar.

- **Güvenilirlik:** Standart önem düzeyi
- **Fiyat:** Standart fiyatlandırma.
- **En uygun kullanım alanı:** En etkileşimli günlük uygulamalar.

### Öncelikli çıkarım (Gecikme için optimize edilmiş)

[Öncelikli](https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr) işleme, isteklerinizi yüksek önem dereceli bilgi işlem kuyruklarına yönlendirir.
Bu trafik kesinlikle öncelikli değildir (diğer katmanlar tarafından asla önceliklendirilmez) ve en yüksek güvenilirliği sunar. Dinamik öncelik sınırlarını aşarsanız sistem, isteği hatayla başarısız kılmak yerine sorunsuz bir şekilde standart işleme düşürür.

- **Güvenilirlik:** En yüksek önem düzeyi
- **Fiyat:** Standart ücretlerin% 75 ila% 100 üzerinde.
- **En uygun kullanım alanları:** Müşteri sohbet botları, gerçek zamanlı sahtekarlık tespiti ve işletme açısından kritik öneme sahip yardımcılar.

### Esnek çıkarım (maliyet açısından optimize edilmiş)

[Esnek çıkarım](https://ai.google.dev/gemini-api/docs/flex-inference?hl=tr), fırsatçı ve yoğun olmayan zamanlardaki işlem kapasitesini kullanarak standart ücretlere kıyasla% 50 indirim sunar. İstekler eşzamanlı olarak işlenir. Bu nedenle, toplu nesneleri yönetmek için kodu yeniden yazmanız gerekmez.
Bu trafik "kaldırılabilir" bir trafik olduğundan, sistemde standart trafik artışları yaşanırsa istekler öncelikli olarak işlenebilir.

- **Güvenilirlik:** Garanti edilmeyen, azaltılabilir önem düzeyi
- **Fiyat:** Standart fiyatlandırmanın% 50'si (jeton başına faturalandırılır).
- **En uygun olduğu durumlar:** N+1 çağrısının N çağrısının çıkışına, arka plandaki CRM güncellemelerine ve çevrimdışı değerlendirmelere bağlı olduğu çok adımlı aracı iş akışları.

## Batch API (Toplu, eşzamansız)

[Toplu İşlem API'si](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr), büyük hacimli istekleri standart maliyetin% 50'si karşılığında eşzamansız olarak işlemek için tasarlanmıştır. İstekleri satır içi sözlükler olarak veya JSONL giriş dosyası (en fazla 2 GB) kullanarak gönderebilirsiniz. İstekleri, 24 saatlik hedef yanıt süresiyle arka plan işleme hızına sahip kuyrukları kullanarak işler.

- **Güvenilirlik:** 24 saatlik otomatik yeniden deneme ve kuyruk sistemiyle birlikte, dökülebilir
- **Fiyat:** Standart fiyatın% 50'si.
- **En uygun olduğu durumlar:** Büyük veri kümelerini önceden işleme, düzenli regresyon test paketleri çalıştırma ve yüksek hacimli resim veya yerleştirme oluşturma.

## Bağlamı önbelleğe alma (giriş tasarrufu)

[Bağlamı önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr), önemli bir ilk bağlama kısa isteklerle tekrar tekrar başvurulduğunda kullanılır.

- **Örtülü önbelleğe alma:** Gemini 2.5 ve daha yeni modellerde otomatik olarak etkinleştirilir.
  İsteğiniz, yaygın istem ön eklerine dayalı olarak mevcut önbelleklerle eşleşirse sistem maliyet tasarruflarını aktarır.
- **Açık Önbelleğe Alma:** Belirli bir geçerlilik süresine (TTL) sahip bir önbellek nesnesini manuel olarak oluşturabilirsiniz. Oluşturulduktan sonra, aynı gövde yükünün tekrar tekrar iletilmesini önlemek için sonraki isteklerde önbelleğe alınmış jetonlara başvurursunuz.
- **Fiyat:** Önbellek jetonu sayısı ve depolama süresine (TTL) göre faturalandırılır.
- **En İyi Kullanım Alanları:** Kapsamlı sistem talimatları içeren chatbot'lar, uzun video dosyalarının tekrarlanan analizi veya büyük doküman kümelerine yönelik sorgular.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-04-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-04-29 UTC."],[],[]]
