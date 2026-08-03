---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=tr
fetched_at: 2026-08-03T04:37:03.449422+00:00
title: "Gemini MCP ve Skills ile kodlama asistan\u0131n\u0131z\u0131 ayarlama \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini MCP ve Skills ile kodlama asistanınızı ayarlama

Yapay zeka kodlama asistanları güçlüdür ancak sınırlamaları vardır. Eğitim verileri belirli bir tarihte sona erer, yeni API özellikleri ve değişiklikleri eksiktir. Gemini'a özel belgelere erişim olmadığında, aracıların optimize edilmiş yaklaşımlar yerine genel kalıplar önermesi mümkündür.

Kodlama asistanınızın, gelişen Gemini API ve önerilen kullanımıyla güncel kalması için **Gemini Docs MCP**'yi ayarlamanızı ve ortamınızı **Gemini API Becerileri** ile geliştirmenizi öneririz. Bu araçlar bağımsız olarak kullanılabilir ancak eksiksiz kapsam sağlamak için birlikte çalışacak şekilde tasarlanmıştır.

## Gemini Dokümanları MCP'sini bağlama

Gemini, `https://gemini-api-docs-mcp.dev` adresinde herkese açık bir Model Context Protocol (MCP) sunucusu barındırır. Kodlama temsilcinizi bu sunucuya bağladığınızda tüm sorguların en yeni API'lere, kod güncellemelerine ve optimum yapılandırma örneklerine erişebilmesi sağlanır.

Sunucuyu yüklemek için aracınızın terminalinde veya proje kök dizininde aşağıdaki komutu çalıştırın:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

Bu sunucu, aracınızın resmi Gemini doküman dosyalarından gerçek zamanlı API tanımlarını ve entegrasyon kalıplarını almak için kullanabileceği bir `search_documentation` işlevi ekler.

## API geliştirme becerileri ekleme

Beceriler, doğrudan asistanınızın bağlamında **yerleşik kurallar ve en iyi uygulamalar** (ör. doğru SDK ve mevcut model sürümlerini zorunlu kılma) sağlar. Bu beceri, Gemini Dokümanları MCP hizmetiyle birlikte çalışır: Her ikisi de yüklüyse beceri, dokümanlar için MCP hizmetini kullanır. Ancak MCP yüklü olmasa bile yedek olarak `llms.txt` kaynağından `ai.google.dev` verilerini getirir.

Bu becerileri yüklemek için aşağıdaki desteklenen araçlardan birini kullanabilirsiniz. Her ikisi için de yükleme talimatları her beceri modülünün altında verilmiştir:

- **[skills.sh](https://skills.sh)**: Önerilir. Taşınabilir temsilci davranışları için açık standart.
- **[Context7](https://context7.com)**: Context7 ekosistemini kullanan kullanıcılar tarafından desteklenir.

### gemini-api-dev

Genel amaçlı Gemini geliştirme için temel beceri. Bu beceri, aşağıdaki konularla ilgili dokümanlar ve en iyi uygulamalar sunar:

- Mevcut modellere (ör. Gemini 3.1 Pro/Flash) istem yönlendirme ve desteği sonlandırılan modellerden kaçınma
- Çok formatlı istem, işlev çağrısı, yapılandırılmış çıkışlar ve yaygın entegrasyon kalıpları

#### Install with skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### Context7 ile yükleme

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

Gemini Live API ile anlık sohbet yapabilen yapay zeka uygulamaları oluşturma becerisi. Bu beceri, aşağıdaki konularla ilgili dokümanlar ve en iyi uygulamalar sunar:

- Düşük gecikmeli yayın için WebSocket bağlantıları
- Ses, video ve metin akışı
- Ses etkinliği algılama ve araya girme desteği

#### Install with skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### Context7 ile yükleme

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### gemini-interactions-api

[Etkileşimler API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) ile uygulama geliştirme becerisi. Etkileşimler API'si, Gemini modelleri ve aracılarıyla uygulama geliştirmenin en basit ve en iyi yoludur. Bu beceri şunları kapsar:

- Metin oluşturma, çok adımlı sohbet ve yayın
- İşlev çağırma, yapılandırılmış çıkış ve görüntü üretme
- Arka planda yürütme ve Deep Research temsilcileri
- Sunucu tarafı sohbet durumu yönetimi
- Python ve TypeScript SDK kalıpları

#### Install with skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### Context7 ile yükleme

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## Yüklemeyi doğrula

Yükleme işleminden sonra kodlama asistanınızın Gemini Docs MCP sunucusuna bağlanabildiğini ve yüklediğiniz becerileri kullanabildiğini onaylayın.

### 1. Temsilci davranışını doğrulama

Doğrulamanın en güvenilir yolu, aracınıza Gemini API hakkında teknik bir soru sormaktır.

**İstem:** "Gemini API ile bağlam önbelleğini nasıl kullanırım?"

Başarılı bir kurulum:

- **Doğru kod sağlama**: En yeni uç noktalardaki `cacheContent` veya `cachedContents.create` gibi belirli Gemini yöntemlerine referans verin.
- **MCP aracını kullanma**: **Gemini Dokümanları MCP sunucusuna** bağlı olduğunu veya veri getirmek için `search_documentation` aracını kullandığını gösterin.
- **Yüklenen becerileri çağırma**: "Beceriyi kullanıyor: gemini-api-dev" (ikincil bir sarmalayıcıya güveniyorsanız) göstergesini gösterin.

### 2. Manifestoları ve araçları doğrulama

Aracı genel bir yanıt verirse Docs MCP'nin veya becerinin belleğe yüklendiğini doğrulamak için ortamınızla ilgili Discovery veya Status komutlarını kullanın.

| Ortam | MCP Doğrulaması | Yetenek Doğrulaması |
| --- | --- | --- |
| **Claude Code** | Etkin sunucuları ve `search_documentation` araçlarını görüntülemek için terminale `/mcp` yazın. | Etkin olan tüm manifestleri listelemek için terminale `/skills` yazın. |
| **İmleç** | **Ayarlar > Özellikler > MCP**'ye gidin. Sunucunun "Bağlı" olduğundan emin olun. | **Ayarlar > Kurallar**'ı açın. Beceri, "Temsilci Karar Verir" bölümünde görünüyor mu? |
| **Antigravity** | MCP durumunu öğrenmek için **Özelleştirmeler > Bağlantılar** kenar çubuğunu kontrol edin. | `/skills list` yazın veya **Özelleştirmeler > Kurallar** kenar çubuğunu kontrol edin. |
| **Gemini CLI** | `gemini mcp list` komutunu çalıştırın veya `/mcp list` kullanın. | `gemini skills list` komutunu çalıştırın veya oturumda `/skills` eğik çizgi komutunu kullanın. |
| **Copilot** | Etkin veri bağlayıcılarını listelemek için `@gemini /mcp` yazın. | Etkin uzantıları görüntülemek için `@gemini /skills` (veya `/skills`) yazın. |

## Sorun giderme

Ajanınız yalnızca genel bilgiler veriyorsa veya Gemini'a özgü yöntemleri tanımıyorsa aşağıdakileri kontrol edin:

### Ajan, beceriyi keşfetmedi

Çoğu temsilci, becerileri yalnızca başlangıçta dizine ekler.

**Düzeltme:** IDE'nizi (Cursor/VS Code) tamamen yeniden başlatın veya terminal tabanlı aracınızdan (Claude Code) çıkıp yeniden açın.

### Küresel ve yerel çatışmalar

`--global` işaretini kullanarak yükleme yaptıysanız aracınız, projeye özel kurallar lehine bu işareti yoksayıyor olabilir.

**Düzeltme:** Beceriyi global işaret olmadan doğrudan proje kökünüze yüklemeyi deneyin:

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## Kaynaklar

- [GitHub'daki Gemini API becerileri](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr)
- [Başlayın](https://ai.google.dev/gemini-api/docs/get-started?hl=tr)
- [Kitaplıklar](https://ai.google.dev/gemini-api/docs/libraries?hl=tr)

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-08 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-08 UTC."],[],[]]
