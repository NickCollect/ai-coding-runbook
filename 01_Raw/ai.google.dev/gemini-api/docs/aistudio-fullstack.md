---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=tr
fetched_at: 2026-09-14T05:37:27.922607+00:00
title: "Google AI Studio'da tam y\u0131\u011f\u0131n uygulamalar geli\u015ftirme \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Google AI Studio'da tam yığın uygulamalar geliştirme

Google AI Studio artık tam yığın geliştirmeyi destekliyor. Bu sayede, istemci tarafı prototiplerin ötesine geçen uygulamalar oluşturabilirsiniz. Sunucu tarafı çalışma zamanı ile sırları yönetebilir, harici API'lere bağlanabilir ve gerçek zamanlı çok oyunculu deneyimler oluşturabilirsiniz.

## Sunucu tarafı çalışma zamanı

Google AI Studio uygulamaları artık sunucu tarafı bileşeni (Node.js) içerebilir.
Böylece aşağıdakileri yapabilirsiniz:

- **Sunucu tarafı mantığını yürütme**: İstemciye gösterilmemesi gereken kodu çalıştırın.
- **npm paketlerine erişme**: [Antigravity Agent](https://antigravity.google/docs/agent?hl=tr), geniş npm ekosistemindeki paketleri yükleyip kullanabilir.
- **Gizli anahtarları işleme**: API anahtarlarını ve kimlik bilgilerini güvenli bir şekilde kullanın.

### npm paketlerini kullanma

`npm install`'ı manuel olarak çalıştırmanız gerekmez. Temsilciden paket gerektiren işlevler eklemesini istemeniz yeterlidir. Temsilci, yükleme ve içe aktarma işlemlerini gerçekleştirir.

**Örnek**: > "Harici API'den veri getirmek için `axios` kullan."

## Gizli anahtarları güvenli bir şekilde yönetme

Sunucu tarafı kodu ve gizli anahtar yönetimi sayesinde artık dünyayla etkileşime geçen uygulamalar oluşturabilirsiniz.

### Gemini API anahtarı

Gemini API'yi kullanan yeni bir uygulama oluşturduğunuzda AI Studio, `GEMINI_API_KEY` değerinizi otomatik olarak sunucu tarafı gizli anahtarı olarak yapılandırır. Manuel kurulum gerekmez. Bu anahtarı Ayarlar'daki **Gizli Diziler** panelinde görüntüleyebilirsiniz. Uygulamanızın Gemini API çağrıları, bu anahtar kullanılarak sunucu tarafı kodundan yapılır. Bu nedenle, tarayıcıda hiçbir zaman gösterilmez.

### Üçüncü taraf API anahtarları

Diğer hizmetler için API anahtarlarını manuel olarak ekleyebilirsiniz:

- **Üçüncü taraf API'leri**: Stripe, SendGrid gibi hizmetlere veya özel REST API'lerine bağlanın.
- **Veritabanları**: Oturumun ötesinde verileri kalıcı hale getirmek için harici veritabanlarına (ör. Supabase, Firebase veya MongoDB Atlas aracılığıyla) bağlanın.

Gerçek dünya uygulamaları oluştururken genellikle API anahtarları gerektiren üçüncü taraf hizmetlerine (ör. Twilio, Slack veya veritabanları) bağlanmanız gerekir. Aşağıdaki adımları uygulayarak anahtarları manuel olarak ekleyebilirsiniz:

1. **Gizli dizi ekleme**: Google AI Studio'da **Ayarlar** menüsüne gidip Gizli Diziler bölümünü bulun.
2. **Anahtarınızı saklama**: API anahtarlarınızı veya gizli jetonlarınızı buraya ekleyin.
3. **Kodda erişim**: Aracı, bu sırları güvenli bir şekilde (genellikle ortam değişkenleri aracılığıyla) erişen sunucu tarafı kodu yazabilir ve bunların hiçbir zaman istemci tarafı tarayıcıya gösterilmemesini sağlayabilir.

Gerekli olduğunda, yeni bir sır gerektiğinde veya projenin ortam değişkenlerinde yeni bir anahtar algılandığında, aracı sohbet penceresinde anahtar eklemenizi isteyen bir kart da gösterir.

### Veritabanı ve kimlik doğrulama için Firebase entegrasyonu

Google AI Studio, [Firebase entegrasyonu](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=tr) aracılığıyla uygulamanıza veritabanı veya kimlik doğrulama eklemeyi kolaylaştırır.
Antigravity Agent, aşağıdaki hizmetleri sizin için otomatik olarak sağlayıp ayarlayabilir:

- **Firestore veritabanı**: İstemci ve sunucu tarafı geliştirme için verileri depolamak ve senkronize etmek üzere kullanılan esnek ve ölçeklenebilir bir NoSQL bulut veritabanı.
- **Firebase Authentication**: Kullanıcılarınızın "Google ile oturum açma" akışlarını kullanarak uygulamanızda güvenli bir şekilde oturum açmasına izin verin.

Aracıdan "uygulamama veritabanı ekle" veya "Google ile Giriş'i ayarla" demeniz yeterlidir. Aracı, gerekli yapılandırmayı ve kod oluşturma işlemlerini sizin için yapar.

Firebase'i ücretsiz olarak kullanmaya başlayabilir ve daha fazla kota veya ücretli özellikler kullanmaya hazır olduğunuzda ücretli bir hesapla ölçeklendirebilirsiniz.

## Google Workspace API'leri

Google AI Studio, Google Workspace API'lerine bağlanan uygulamalar oluşturmanıza olanak tanır. Böylece kullanıcılarınız, e-postalar, elektronik tablolar, dokümanlar, takvim etkinlikleri ve daha fazlası gibi gerçek verileriyle doğrudan uygulamanızda çalışabilir. Artık Google Cloud projesi oluşturmanız, OAuth'u yapılandırmanız veya API'nizi manuel olarak yönetmeniz gerekmez.

### İşleyiş şekli

Workspace entegrasyonunu iki şekilde ekleyebilirsiniz:

- **Sohbet panelinde açıklayın**: Alt kısımdaki sohbet panelinde, temsilciye ne istediğinizi söylemeniz yeterlidir. Örneğin, *"Makbuzları Google E-Tablolar'a kaydeden bir gider izleyici oluştur"* veya *"Okunmamış Gmail mesajlarımı özetleyen bir kontrol paneli oluştur."*
- **Entegrasyonlar panelinden seçme**: Oluşturma modunun sağ kenar çubuğunda **Entegrasyonlar** panelini açın ve bağlamak istediğiniz Workspace uygulamasını etkinleştirin.

Bir Workspace uygulaması eklediğinizde AI Studio otomatik olarak:

1. Uygulamanız için gerekli Google API'sini bağlar.
2. API'yi çağırmak için sunucu tarafı kodu oluşturur.
3. Uygulamanızın son kullanıcılarının kendi verilerine erişimi yetkilendirebilmesi için güvenli bir "Google ile oturum açma" akışı ekler.

### Desteklenen uygulamalar

Aşağıdaki Google Workspace uygulamaları kullanılabilir:

| Uygulama | Neler oluşturabilirsiniz? |
| --- | --- |
| Google Takvim | Etkinlikleri ve takvimleri okuma, oluşturma ve yönetme |
| Google Chat | İleti dizilerini ve grup alanlarını okuma ve bunlarla etkileşime geçme |
| Google Dokümanlar | Doküman oluşturma, okuma, güncelleme ve biçimlendirme |
| Google Drive | Dosya ve klasörleri düzenleme, arama ve yönetme |
| Google Formlar | Anket oluşturma, soruları güncelleme ve yanıtları alma |
| Gmail | E-posta içeriğini okuma, gönderme ve yönetme |
| Google Keep | Notları, listeleri ve ekleri yönetme |
| Google Meet | Görüntülü görüşme planlama ve yönetme |
| Kişiler | Kişileri senkronize etme ve yönetme |
| Google E-Tablolar | E-tablo verilerini okuma, yazma ve biçimlendirme |
| Google Slaytlar | Sunu oluşturma ve değiştirme |
| Google Görevler | Görev oluşturma, yönetme ve düzenleme |

### Kimlik doğrulama ve izinler

Oluşturucu olarak OAuth istemcilerini yapılandırmanız, kimlik bilgilerini yönetmeniz veya Google Cloud projesi oluşturmanız gerekmez. AI Studio tüm bu işlemleri sizin için yapar.

Workspace API'lerinin entegre edildiği uygulamalar, son kullanıcıların kimliğini doğrulamak için "Google ile oturum açma" özelliğini kullanır. Kullanıcılar uygulamanızı açtığında oturum açmaları ve uygulamanızın ihtiyaç duyduğu belirli izinleri (örneğin, takvimlerine salt okunur erişim veya bir e-tabloyu düzenleme olanağı) vermeleri istenir. Uygulamanız yalnızca uygulamayı kullanan kişinin verilerine erişir. Her kullanıcı, kendi hesabına erişim yetkisi verir.

### Örnek istemler

Workspace entegrasyonlarını kullanmaya başlamak için birkaç öneri:

- *"Google Takvim'imi okuyup her toplantı için Gmail'de hazırlık e-postaları oluşturan bir uygulama geliştir."*
- *"Google Dokümanı alıp Google Slaytlar'da 5 slaytlık bir özet sunu oluşturan bir araç geliştir."*
- *"Makbuz yüklediğim, Gemini'ın ayrıntıları çıkardığı ve Google E-Tablomda yeni bir satırın kaydedildiği bir gider izleyici oluştur."*

### OAuth'u ayarlama

Sır yönetimiyle ilgili temel kullanım alanlarından biri, diğer web sitelerine veya uygulamalara bağlanmak için OAuth'u ayarlamaktır. İsteminizde, OAuth kimlik doğrulaması gerektiren bir üçüncü taraf uygulamasına bağlanmayla ilgili talimatlar varsa aracı, bu uygulama için OAuth'u ayarlama talimatlarını sağlar. Bu talimatlar, OAuth uygulamanızı yapılandırmak için gerekli geri çağırma URL'lerini içerir.
Geri çağırma URL'lerini Ayarlar panelindeki **Entegrasyonlar** bölümünde de bulabilirsiniz.

## Çok oyunculu deneyimler oluşturma

Tam yığın çalışma zamanı, gerçek zamanlı ortak çalışma özelliklerini etkinleştirir.

- **Gerçek zamanlı durum**: Aracının "canlı sohbet", "ortak beyaz tahta" veya "çok oyunculu oyun" gibi özellikler oluşturmasını isteyebilirsiniz.
- **Senkronize oturumlar**: Sunucu durumu yönetir ve birden fazla kullanıcının aynı uygulama örneğiyle gerçek zamanlı olarak etkileşim kurmasına olanak tanır.

**Örnek istem**: > "Bunu, oyuncuların birbirlerinin imleçlerini görebileceği çok oyunculu bir oyun haline getir."

### Çok oyunculu uygulamaları test etme ipuçları

Uygulamanızı dağıtmadan önce çok oyunculu modu iki şekilde test edebilirsiniz.

1. Uygulamanızı Google AI Studio'nun Build (Oluştur) modunda birden fazla sekmede açın. Uygulamanız, Build modunda geliştirilirken bir geliştirme container'ında bulunur. Uygulamayı birden fazla sekmede açarak uygulamanızı kullanan birden fazla oyuncuyu simüle edebilirsiniz.
2. Sağ üstteki **Paylaş** menüsünü kullanarak uygulamayı başkalarıyla paylaşın.
   Ardından, uygulamayı paylaştığınız oyuncularla kullanmak için **Paylaş** menüsünün **Entegrasyonlar** sekmesindeki **Paylaşılan URL**'yi kullanın.

## En iyi uygulamalar

- **Gemini API çağrıları**: `GEMINI_API_KEY`, otomatik olarak sunucu tarafı gizli anahtarı olarak yapılandırılır. Bu anahtarı kullanarak sunucu tarafı kodunuzdan Gemini API çağrıları yapın. Bu bilgiyi **Sırlar** panelinde görüntüleyebilirsiniz.
- **Gizli anahtar güvenliği**: Hassas anahtarlar için her zaman Secret Manager'ı kullanın.
  Bunları dosyalarınızda asla sabit kodlamayın.
- **İlgi alanlarının ayrılması**: Kullanıcı arayüzü mantığınızı istemci tarafı çerçevesinde (React/Angular), iş mantığınızı/veri işlemeyi ise sunucu tarafında tutun.
- **Hata işleme**: Uygulamanın kilitlenmesini önlemek için sunucu tarafı kodunuzun harici API çağrılarından kaynaklanan hataları etkili bir şekilde işlemesini sağlayın.

## Sırada ne var?

- [Google AI Studio'da uygulama geliştirme](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=tr)
- [Google AI Studio'dan dağıtma](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=tr)
- [App Gallery](https://aistudio.google.com/apps?source=showcase&hl=tr)

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-08-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-08-19 UTC."],[],[]]
