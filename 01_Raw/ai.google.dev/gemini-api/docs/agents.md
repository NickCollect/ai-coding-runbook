---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=tr
fetched_at: 2026-05-05T13:11:38.911017+00:00
title: "Arac\u0131lara Genel Bak\u0131\u015f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

- [Ana Sayfa](https://ai.google.dev/gemini-api/docs/Ana Sayfa)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/Dokümanlar)

Geri bildirim gönderin

# Aracılara Genel Bakış

Aracılar, karmaşık ve çok adımlı görevleri gerçekleştirmek ve belirli hedeflere ulaşmak için Gemini modellerinden, bir dizi araçtan ve akıl yürütme özelliklerinden yararlanan sistemlerdir. Tek bir model çağrısının aksine, bir aracı planlama yapabilir, bir dizi işlemi yürütebilir, harici sistemlerle etkileşimde bulunabilir ve kullanıcının isteğini karşılamak için bilgileri sentezleyebilir.

Gemini API ile aşağıdaki gibi özellikleri kullanarak güçlü aracıları oluşturabilirsiniz:

- **[Gemini modelleri](https://ai.google.dev/gemini-api/docs/Gemini modelleri):** Akıl yürütme ve dil anlayışı sağlayan temel zeka.
- **[Araçlar](https://ai.google.dev/gemini-api/docs/Araçlar):** Modeli gerçek dünyadaki bilgilere ve işlemlere bağlayan özellikler. Bunlar yerleşik araçlar (ör. Google Arama, Haritalar, Kod Yürütme) veya özel araçlar olabilir.
- **[İşlev çağrısı](https://ai.google.dev/gemini-api/docs/İşlev çağrısı):** Kendi özel araçlarınızı ve API'lerinizi Gemini modeline tanımlayıp bağlama mekanizmasıdır.
- **[Düşünme](https://ai.google.dev/gemini-api/docs/Düşünme):** Modelin karmaşık görevler için akıl yürütme ve planlama becerisini geliştiren özellikler.
- **[Uzun bağlam](https://ai.google.dev/gemini-api/docs/Uzun bağlam):** Aracıların, uzun süren etkileşimler boyunca durumu ve bilgileri korumasını sağlar.

## Kullanılabilir temsilciler

- **[Derin Araştırma Temsilcisi](https://ai.google.dev/gemini-api/docs/Derin Araştırma Temsilcisi):** Pazar analizi, gerekli özen ve literatür incelemeleri gibi kullanım alanları için çok adımlı araştırma görevlerini planlayan, yürüten ve sentezleyen bağımsız bir temsilci.

## Ajan oluşturma

Temsilciler, çok adımlı görevleri tamamlamak için modelleri ve araçları kullanır. Gemini, akıl yürütme özellikleri ("beyin") ve temel araçlar ("eller") sunsa da genellikle aracının belleğini yönetmek, planlama döngüleri oluşturmak ve karmaşık araç zincirleme işlemleri gerçekleştirmek için bir orkestrasyon çerçevesine ihtiyacınız olur.

Çok adımlı iş akışlarında güvenilirliği en üst düzeye çıkarmak için modelin nasıl akıl yürüteceğini ve planlayacağını açıkça kontrol eden talimatlar oluşturmanız gerekir. Gemini, genel olarak güçlü bir akıl yürütme yeteneği sunsa da karmaşık ajanlar, sorunlar karşısında ısrarcı olma, risk değerlendirmesi ve proaktif planlama gibi belirli davranışları zorunlu kılan istemlerden yararlanır.

Bu istemleri tasarlama stratejileri için [Agentic iş akışları](https://ai.google.dev/gemini-api/docs/Agentic iş akışları) bölümüne bakın. Aşağıda, çeşitli yapay zeka ölçütlerinde performansı yaklaşık %5 oranında artıran bir [sistem
talimatı](https://ai.google.dev/gemini-api/docs/sistemtalimatı) örneği verilmiştir.

## Aracı çerçeveleri

Gemini, aşağıdakiler gibi önde gelen açık kaynaklı aracı çerçeveleriyle entegre olur:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/**LangChain / LangGraph**): Grafik yapılarını kullanarak durum bilgisi olan, karmaşık uygulama akışları ve çoklu ajan sistemleri oluşturun.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/**LlamaIndex**): RAG ile geliştirilmiş iş akışları için Gemini ajanlarını özel verilerinize bağlayın.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/**CrewAI**): Ortak çalışmaya dayalı, rol oynayan otonom yapay zeka temsilcilerini yönetin.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/**Vercel AI SDK**): JavaScript/TypeScript'te yapay zeka destekli kullanıcı arayüzleri ve temsilciler oluşturun.
- [**Google ADK**](https://ai.google.dev/gemini-api/docs/**Google ADK**): Birlikte çalışabilen yapay zeka temsilcileri oluşturmak ve düzenlemek için kullanılan açık kaynaklı bir çerçeve.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://ai.google.dev/gemini-api/docs/Creative Commons Atıf 4.0 Lisansı) altında ve kod örnekleri [Apache 2.0 Lisansı](https://ai.google.dev/gemini-api/docs/Apache 2.0 Lisansı) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://ai.google.dev/gemini-api/docs/Google Developers Site Politikaları)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-04-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?
