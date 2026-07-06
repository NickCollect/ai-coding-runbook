---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=tr
fetched_at: 2026-07-06T05:21:58.536965+00:00
title: "AI Studio Playground'daki temsilciler \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# AI Studio Playground'daki temsilciler

Google AI Studio Playground, API çağrıları oluşturup yazmak zorunda kalmadan yönetilen temsilcilerin nasıl oluşturulacağını öğrenmek ve prototip oluşturmak için görsel bir arayüz sağlar.

Başlamak için Google AI Studio'nun gezinme panelinde **Playground** sekmesine gidin ve açma/kapatma düğmesini **Agents** olarak değiştirin.

## Önceden oluşturulmuş şablonlar

**Ajanlar** sekmesinde, araç ve ortam yapılandırmalarını ayarlayarak temel Antigravity Ajanı'nı önceden yapılandıran bir dizi şablon bulunur. Tüm şablonlar açık kaynaklıdır ve [google-gemini/gemini-managed-agents-templates](https://github.com/google-gemini/gemini-managed-agents-templates/) deposunda yayınlanır. Bu şablonları inceleyerek kendi yönetilen aracınızı nasıl oluşturacağınızı ve yapılandıracağınızı öğrenebilirsiniz.

Örneğin, Yapay Zeka Radyosu şablonunu seçtiğinizde izin verilen tüm araçlar etkinleştirilir ve radyo programı üretimi için özel bir `AGENTS.md` dosyası ve becerileri bağlanır. Bu ayarları, **Kaynaklar** düğmesini tıklayarak Playground kullanıcı arayüzündeki **Ortam** bölümünde görüntüleyebilirsiniz.

## Araç yapılandırması

Playground'daki Agent ayarları bölümünde aşağıdaki yerleşik araçlara erişimi açıp kapatabilirsiniz:

- **Google Arama:** Gerçek zamanlı bilgi temellendirmesi için açık web'e erişin.
- **URL Bağlamı:** Belirli web sayfası URL'lerinin metin içeriğini getirip ayrıştırın.
- **Kod Yürütme:** Bash ve Python komutlarını doğrudan izole edilmiş korumalı alan ortamında çalıştırın.
- **Dosya Sistemi Araçları:** Çalışma alanındaki dosyaları okuma, yazma, listeleme ve silme.

## Ortam Yapılandırması

Yönetilen aracılar, güvenli ve kısa ömürlü bir Linux korumalı alanında (ortam) çalışır. Bu ortam, aracılara çalışmak için ihtiyaç duydukları çalışma alanını ve araçları sağlar. Daha fazla bilgi için [yönetilen aracı ortamı](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr) kılavuzuna bakın.

### Ajan davranışını kontrol etme

Ajanın davranışı, karakteri ve yetenekleri büyük ölçüde ortamındaki dosyalar tarafından belirlenir. Aracı, yapılandırmaları özel bir `.agents` klasörden otomatik olarak algılayıp yükler:

- **`AGENTS.md`**: Sistem talimatlarını ve karakterini tanımlamak için aracının bağlamına önceden yüklenir.
- **`SKILL.md`**: Belirli özellikleri ve iş akışlarını tanımlamak için ilgili beceri klasörlerinin (ör. `.agents/skills/my-skill/SKILL.md`) altında yer alır.

### Ortamın temel hazırlığını yapma

Bir oturum başlatmadan önce dosyaları ortama bağlayarak aracının kullanacağı ortamı yapılandırabilirsiniz. Kaynakları bağlayarak yeni bir ortam oluşturabilir veya önceki bir ortamı geri yükleyebilirsiniz:

- **Yeni bir ortam oluşturmak için** Ortam ayarları panelinde **Kaynak ekle**'yi tıklayın ve aşağıdaki kaynak türlerinden birini seçin:

| Kaynak türü | Açıklama | Bağlantı yolu |
| --- | --- | --- |
| **Satır İçi Dosyalar** | Yapılandırma dosyalarını, sahte veri kümelerini veya yardımcı program komut dosyalarını (100 KB'a kadar) doğrudan Playground kullanıcı arayüzüne yazın ya da yapıştırın. | Kullanıcı tanımlı hedef yolu (ör. `/workspace/scripts/parser.py`). |
| **Google Cloud Storage** | Herkese açık veya özel bir Cloud Storage paketi bağlayın.  Özel paketler için standart bir OAuth 2.0 Bearer jetonu gerekir. Daha fazla bilgi için [Özel kaynaklar](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr#private-sources) başlıklı makaleyi inceleyin. | Bir GCS paketi yolunu (ör. `gs://your-bucket-name/data/`) bir çalışma alanı diziniyle (ör. `/workspace/data/`) eşler. |
| **GitHub depoları** | Herkese açık veya özel kod tabanlarını klonlayın.  Özel depolar için GitHub kişisel erişim jetonunuzla (PAT) temel kimlik doğrulama gerekir. Daha fazla bilgi için [Özel kaynaklar](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr#private-sources) başlıklı makaleyi inceleyin. | Doğrudan `/workspace/` içine kopyalanır (genellikle `/workspace/<repo-name>` saniyeden kısa sürer). |

- **Önceki bir ortamı geri yüklemek için**, tam durumunu klonlamak ve çatallamak üzere [mevcut bir ortam kimliğini yeniden kullanabilirsiniz](#reusing-an-existing-environment-id).

### Mevcut bir ortam kimliğini yeniden kullanma

Bir test ortamı oluşturmak için zaman harcadıysanız sıfırdan başlamanız gerekmez. Mevcut bir ortamı kullanmak için:

1. AI Studio'da Ortamlar paneline gidin ve **Tür**'ü **Mevcut** olarak değiştirin.
2. **Ortam kimliğini** girin (ör.`env_abc123`).

Daha fazla bilgi için [Ortam yapılandırma](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr#configure-an-environment) başlıklı makaleyi inceleyin. Ayrıca, mevcut oturumun ortam kimliğini kullanıcı arayüzündeki Ortam sekmesinden de alabilirsiniz.

Temsilciye ilk mesajınızı gönderdiğinizde ortam yapılandırması, söz konusu oturum için sabitlenir. Etkileşim etkin olarak çalışırken yeni kaynaklar bağlayamaz veya ağ izin verilenler listesini değiştiremezsiniz.

## Ortamı indirme

Bir ortam oluşturulduktan sonra, ortam dosyalarını tarball olarak almak için AI Studio Playground'un Ortam ayarlarındaki **İndir** düğmesini kullanarak ortam anlık görüntüsünü istediğiniz zaman indirebilirsiniz.

## Güvenlik ve Maliyet Yönetimi

### Jeton tüketimini yönetme

Tek bir çıktı üreten standart bir sohbet isteğinin aksine, Antigravity Agent bağımsız bir iş akışı yürütür. Planlama yapar, kodu çalıştırır, sonuçları gözlemler ve tekrarlar. Bu, tek bir istemin sınırsız jeton tüketimine yol açabileceği anlamına gelir.

Maliyetleri yönetmek için **istemlerinizde net sonlandırma ölçütleri sağlayın ve görevleri, aracı için dar bir kapsamda tutun**. İyi bir örnek olarak şu istem verilebilir:
*Çekme isteğini incele ve Markdown özetini oluşturduktan sonra dur.
Düzeltmeyi kendiniz yazmaya çalışmayın*.

**Durdur** düğmesini kullanarak aracı istediğiniz zaman durdurabilirsiniz.

### Ek Maliyetler

Varsayılan olarak, Playground'daki tüm aracı şablonları Gemini API hizmetine erişebilir ve istekleri karşılamak için ortamdan API çağrıları yapabilir. Bunlar, jeton tüketimine yansıtılmayacak ek maliyetlere neden olabilir.

Benzer şekilde, başka harici hizmetler eklerseniz aracı, bu hizmetleri sizin adınıza çağırarak ek maliyetlere neden olabilir.

### Ağ izin verilenler listesi

Varsayılan olarak, AI Studio'da aracınızın korumalı alan ortamından gelen tüm giden ağ istekleri, güvenliği sağlamak için sıkı bir şekilde kontrol edilir ve kısıtlanır. Aracınıza harici API'lere, web hizmetlerine veya paket yöneticilerine ulaşma izni vermek için bunları açıkça belirtmeniz gerekir:

1. AI Studio'da Ortamlar paneline gidin.
2. **Ağ**'ın yanındaki **kurallar** düğmesini seçin.
3. **Ağ yapılandırması** panelinde **İzin verilenler listesine ekle**'yi tıklayın ve ilgili ayrıntıları girin:
   - **Alan adı kısıtlaması:** Yalnızca listeye eklenen belirli alan adlarına veya joker karakter kalıplarına aracının sanal makinesi tarafından erişilebilir. Örneğin, `api.github.com` gibi tam alan adları veya `*.googleapis.com` gibi geniş kalıplar girebilirsiniz.
   - **HTTP Üstbilgisi ve Jeton Ekleme:** Belirli bir alan için gerekli kimlik bilgilerini (ör. API jetonu) güvenli bir şekilde eklemek üzere **HTTP üstbilgisi ekle** seçeneğini kullanın. Bu kimlik bilgileri, çıkış proxy'si üzerinden güvenli bir şekilde iletilir ve hiçbir zaman aracı özel korumalı alanında doğrudan ham metin olarak gösterilmez.

İzin verilenler listenize alan eklerken her zaman dikkatli olun. Aracıya kimliği doğrulanmış hizmetlere erişim izni vermek, aracının sizin adınıza hareket edebileceği anlamına gelir. Bu durum, dikkatli bir şekilde izlenmediği takdirde istenmeyen işlemlere yol açabilir.

### Kimlik bilgileriyle ilgili en iyi uygulamalar

İş akışınızda aracının harici hizmetlerle kimliğini doğrulaması gerekiyorsa bu kimlik bilgilerini sağlama ve kapsamını belirleme sorumluluğu size aittir. Riski azaltmak için aşağıdaki yönergeleri uygulayın:

- **En az ayrıcalık ilkesine uygun kimlik bilgileri kullanın:** Yalnızca aracınızın ihtiyaç duyduğu izinlere sahip hizmet hesapları veya API anahtarları oluşturun. Geniş veya yönetici erişimi olan kimlik bilgilerini iletmekten kaçının.
- **Kısa ömürlü jetonları tercih edin:** Mümkün olduğunda uzun ömürlü API anahtarları yerine, geçerlilik süresi sınırlı kimlik bilgileri veya süresi dolan jetonlar kullanın.
- **Tam erişim varsay:** Ajan, kendisine verdiğiniz görevi tamamlamak için erişebildiği tüm kimlik bilgilerini kullanabilir. Yalnızca tam kapsamlı erişim izni vermeye hazır olduğunuz kimlik bilgilerini sağlayın.
- **Kimlik bilgilerini düzenli olarak değiştirin:** Aracıyla paylaşılan kimlik bilgilerine, diğer tüm programatik kimlik bilgilerine davrandığınız gibi davranın ve bunları düzenli olarak değiştirin.

### Harici araçları ve API'leri bağlama

Ajanın özelliklerini genişletmek için harici araçları ve API'leri (ör. Model Context Protocol / MCP sunucuları) bağlayabilirsiniz. Bu işlemi yaparken:

- Yalnızca güvendiğiniz kaynaklardan gelen araçları bağlayın. Kötü amaçlı veya kötü yazılmış bir araç, verileri açığa çıkarabilir ya da istenmeyen işlemler gerçekleştirebilir.
- Araçları, kullanım alanınız için gereken minimum izinlerle yapılandırın. Bir araç salt okuma modunu destekliyorsa yazma işlemi kesinlikle gerekli olmadığı sürece bu modu tercih edin.
- Bir aracı üretim veri kaynağına bağlamadan önce, aracının beklendiği gibi kullandığını doğrulamak için örnek veya sentetik verilerle test edin.

### İnsan gözetimi

Ajanlar, çok adımlı iş akışlarını yüksek düzeyde bağımsızlıkla akıl yürüterek, planlayarak ve uygulayarak gerçekleştirebilir. Bu özellik güçlü olsa da özellikle verileri değiştiren veya harici sistemlerle etkileşimde bulunan görevler için uygun gözetim uygulamanız gerekir.

Oluşturulan kod, veri dönüşümleri veya yapılandırma değişiklikleri gibi kritik çıkışları dağıtmadan önce her zaman doğrulayın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-20 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-20 UTC."],[],[]]
