---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=tr
fetched_at: 2026-06-15T06:23:53.048569+00:00
title: "Arac\u0131lara Genel Bak\u0131\u015f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Aracılara Genel Bakış

Gemini API'deki yönetilen temsilciler, yapılandırılabilir bir temsilci koşumu sağlar. Tek bir API çağrısı, aracının akıl yürüttüğü, kod yürüttüğü, dosyaları yönettiği ve web'de bağımsız olarak gezindiği bir Linux sanal alanı sağlar.

[rocket\_launch

Hızlı başlangıç kılavuzu

İlk temsilci çağrınızı yapın, yanıtları yayınlayın ve özel bir temsilci oluşturun.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr)
[smart\_toy

Antigravity Agent

Varsayılan aracının özellikleri, araçları, çok formatlı girişi ve fiyatlandırması.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr)
[experiment

AI Studio'daki temsilciler

Kod yazmadan temsilci prototipi oluşturmak için görsel deneme alanı.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=tr)

## Kullanılabilir yönetilen aracı sayısı

- **[Antigravity ajanı](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr)**: Gemini 3.5 Flash tarafından desteklenen, genel amaçlı yönetilen ajan. Google tarafından barındırılan güvenli bir Linux korumalı alanında kod çalıştırır, dosyaları yönetir ve web'de arama yapar. [Özel bir temsilci oluşturmak](https://ai.google.dev/gemini-api/docs/custom-agents?hl=tr) için kendi talimatlarınız, becerileriniz ve verilerinizle genişletebilirsiniz.
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr)**: Pazar analizi, gerekli özen ve literatür incelemeleri gibi kullanım alanları için çok adımlı araştırma görevlerini planlayan, yürüten ve sentezleyen bağımsız araştırma aracısı.

## Güvenlik ve en iyi uygulamalar

Her aracı, işletim sistemi düzeyinde yalıtılmış bir korumalı alan ortamında çalışır.
Korumalı alan, varsayılan olarak sınırsız giden ağ erişimine sahiptir. İzin verilenler listesi kullanarak ağ erişimini kısıtlayabilir veya devre dışı bırakabilirsiniz.

### Ağ erişimi

Varsayılan olarak, ortamların sınırsız giden ağ erişimi vardır. Giden trafiği belirli alanlarla veya joker karakter kalıplarıyla kısıtlamak için `network` izin verilenler listesini kullanın. Yapılandırma ayrıntıları için [Ağ izin verilenler listesi](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=tr#network_allow_list) (AI Studio) veya [Ağ kuralları](https://ai.google.dev/gemini-api/docs/custom-agents?hl=tr#with_network_rules) (API) başlıklı makaleleri inceleyin.

### Harici araçlar ve API'ler

Aracıyı genişletmek için harici araçlar ve API'ler bağlayabilirsiniz. Yalnızca güvenilir kaynaklardan gelen araçları kullanın ve izinleri gereken minimum düzeyde tutun. Kimlik bilgileri, çıkış proxy'si başlık dönüşümleri aracılığıyla güvenli bir şekilde eklenebilir ve hiçbir zaman korumalı alan içinde kullanıma sunulmaz. Aracı, erişebildiği tüm kimlik bilgilerini kullanabilir. Bu nedenle, yalnızca tam kapsamlı erişim izni vermeye hazır olduğunuz kimlik bilgilerini sağlayın.

- En az ayrıcalıklı hizmet hesaplarını veya API anahtarlarını kullanın.
- Uzun ömürlü anahtarlar yerine kısa ömürlü jetonları tercih edin.
- Yalnızca tam kapsamını vermeye istekli olduğunuz kimlik bilgilerini sağlayın.
- Kimlik bilgilerini düzenli aralıklarla döndürün.

Başlık dönüşümlerini yapılandırma hakkında ayrıntılı bilgi için [Kimlik bilgileri](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr#credentials) başlıklı makaleyi inceleyin.

### İnsan gözetimi

Çıktıları (oluşturulan kod, veri dönüşümleri, yapılandırma değişiklikleri) dağıtmadan önce her zaman doğrulayın. Özellikle verileri değiştiren veya harici sistemlerle etkileşimde bulunan görevlerde bu doğrulama işlemi önemlidir.

## Fiyatlandırma

Yönetilen ajanlar, Gemini model jetonlarına ve araç kullanımına dayalı bir [kullandıkça öde modelini](https://ai.google.dev/gemini-api/docs/pricing?hl=tr#pricing-for-agents) kullanır. Tek bir etkileşim birden fazla muhakeme döngüsünü tetikleyebilir ve genellikle 100.000 ila 3.000.000 jeton tüketir. Önizleme sırasında ortam işlem ücreti **alınmaz**. Görev başına dökümler için [tahmini maliyetler](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr#availability-and-pricing) bölümüne bakın.

## Sınırlar

| Sınır | Açıklama |
| --- | --- |
| **Ortamın kullanım ömrü** | Ortamlar, 7 gün boyunca işlem yapılmadığında kalıcı olarak silinir. |
| **VM Spin-down** | Kaynakları korumak için kısa bir süre işlem yapılmadığında VM'ler kapatılır. Bir sonraki istek, durumu (baştan başlatma ile) geri yükler. |
| **Önceden Yüklenmiş Yazılım** | Python 3.12 ve Node.js 22'nin bulunduğu Ubuntu tabanlı ortam. Ortamın temel görüntüsü hakkında daha fazla bilgi için [Önceden yüklenmiş yazılım](https://ai.google.dev/gemini-api/docs/agent-environment?hl=tr#pre-installed-software) başlıklı makaleyi inceleyin. |
| **Maks. temsilci sayısı** | En fazla 1.000 yönetilen aracıya sahip olabilirsiniz. |

## Aracı çerçeveleri

Ayrıca, aşağıdaki çerçeveleri ve SDK'ları kullanarak Gemini ile ajanlar oluşturabilirsiniz:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=tr): Grafik yapılarını kullanarak durum bilgisi olan, karmaşık uygulama akışları ve çoklu ajan sistemleri oluşturun.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=tr): RAG ile geliştirilmiş iş akışları için Gemini ajanlarını özel verilerinize bağlayın.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=tr): Ortak çalışmaya dayalı, rol oynayan otonom yapay zeka temsilcilerini yönetin.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=tr): JavaScript/TypeScript'te yapay zeka destekli kullanıcı arayüzleri ve temsilciler oluşturun.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): Birlikte çalışabilen yapay zeka temsilcileri oluşturmak ve düzenlemek için kullanılan açık kaynaklı bir çerçeve.
- [**Antigravity SDK**](https://antigravity.google/product/antigravity-sdk?hl=tr): Python'da programlanabilen, Google Antigravity'yi destekleyen araçları, aracı döngüsünü ve bağlam yönetimini kullanarak bağımsız yapay zeka aracıları oluşturun.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-20 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-20 UTC."],[],[]]
