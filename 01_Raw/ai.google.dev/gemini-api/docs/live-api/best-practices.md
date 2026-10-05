---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=tr
fetched_at: 2026-10-05T06:38:56.333133+00:00
title: "Live API ile ilgili en iyi uygulamalar \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Live API ile ilgili en iyi uygulamalar

Bu kılavuzda, Live API kullanımınızı optimize etmek için uygulayabileceğiniz en iyi uygulamalar ele alınmaktadır.
Genel bakış ve yaygın kullanım alanlarına ilişkin örnek kod için [Live API'yi kullanmaya başlama](https://ai.google.dev/gemini-api/docs/live?hl=tr) sayfasını inceleyin.

## Net sistem talimatları tasarlama

Live API'den en iyi performansı almak için, sırasıyla aracı kişiliğini, sohbet kurallarını ve koruma duvarlarını tanımlayan net bir şekilde tanımlanmış bir dizi sistem talimatı (SI) kullanmanızı öneririz.

En iyi sonuçları elde etmek için her bir aracıyı ayrı bir SI olarak ayırın.

1. **Ajan kişiliğini belirtin:** Ajanın adı, rolü ve tercih edilen özellikleri hakkında ayrıntılı bilgi verin. Aksanı belirtmek istiyorsanız tercih edilen çıkış dilini de (ör. İngilizce konuşan biri için İngiliz aksanı) belirttiğinizden emin olun.
2. **Sohbet kurallarını belirtin:** Bu kuralları, modelin uymasını beklediğiniz sıraya göre yerleştirin. Görüşmenin tek seferlik öğeleri ile görüşme döngüleri arasındaki farkı belirtin. Örneğin:

   - **Tek seferlik öğe:** Müşterinin ayrıntılarını (ör. ad, konum, bağlılık kartı numarası) bir kez toplama.
   - **Sohbet döngüsü:** Kullanıcı, önerileri, fiyatlandırmayı, iadeleri ve teslimatı tartışabilir ve konudan konuya geçmek isteyebilir. Modele, kullanıcı istediği sürece bu sohbet döngüsüne katılmasının sorun olmadığını bildir.
3. **Bir akış içindeki araç çağrılarını ayrı cümlelerde belirtin:** Örneğin, bir müşterinin ayrıntılarını toplamak için tek seferlik bir adımda `get_user_info` işlevinin çağrılması gerekiyorsa şunları söyleyebilirsiniz: *İlk adımınız kullanıcı bilgilerini toplamak. Öncelikle kullanıcıdan adını, konumunu ve bağlılık kartı numarasını vermesini isteyin. Ardından, bu ayrıntılarla `get_user_info` işlevini çağırın.*
4. **Gerekli tüm koruma önlemlerini ekleyin:** Modelin yapmasını istemediğiniz genel sohbet koruma önlemlerini sağlayın. *x* gerçekleşirse modelin *y* yapmasını istediğinize dair belirli örnekler verebilirsiniz. Hâlâ istediğiniz hassasiyet düzeyine ulaşamıyorsanız modele hassas olması için yol göstermek üzere *kesinlikle* kelimesini kullanın.

## Araçları hassas bir şekilde tanımlama

Live API ile araçları kullanırken araç tanımlarınızda net olun.
Gemini'a hangi koşullarda araç çağrısı yapılması gerektiğini söyleyin. Daha fazla bilgi için örnek bölümündeki [Araç tanımları](#tool-definitions-example) konusuna bakın.

## Etkili istemler oluşturma

- **Net istemler kullanın:** İstemlerde modellerin ne yapması ve ne yapmaması gerektiğine dair örnekler verin. İstemleri, her karakter veya rol için tek bir istemle sınırlamaya çalışın. Uzun ve çok sayfalı istemler yerine istem zincirleme özelliğini kullanabilirsiniz. Model, tek işlev çağrısı içeren görevlerde en iyi performansı gösterir.
- **Başlangıç komutları ve bilgileri sağlama:** Live API, yanıt vermeden önce kullanıcı girişi bekler. Live API'nin görüşmeyi başlatması için kullanıcıyı selamlamasını veya görüşmeye başlamasını isteyen bir istem ekleyin. Canlı API'nin bu karşılama mesajını kişiselleştirmesi için kullanıcı hakkında bilgi ekleyin.

## Dili belirtme

Live API ses modelleri, kullanıcının konuştuğu dili otomatik olarak algılayıp uyum sağlar ve açık bir dil kodu gerektirmez.

Modelin belirli bir dilde yanıt vermesini istiyorsanız sistem talimatlarınıza bir talimat ekleyin:

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## Canlı Yayın

Anlık ses özelliğini uygularken aşağıdaki en iyi uygulamaları göz önünde bulundurun:

- **Parça Boyutu ve Gecikme**: Sesi 20 ms ile 40 ms arasındaki parçalar halinde gönderin.
- **Kesintileri İşleme**: Kullanıcı, model yanıt verirken konuştuğunda sunucu, `"interrupted": true` ile birlikte `server_content` mesajı gönderir. Aracının kullanıcıyla konuşmaya devam etmesini önlemek için istemci tarafındaki ses arabelleğinizi hemen atmanız gerekir.

## Bağlam yönetimi

Yerel ses jetonları hızla biriktiği için (yaklaşık 25 jeton/saniye) uzun oturumlarda `ContextWindowCompressionConfig` kullanın.

## İstemci arabelleğe alma

Göndermeden önce giriş sesini önemli ölçüde (ör. 1 saniye) arabelleğe almayın. Gecikmeyi en aza indirmek için küçük parçalar (20 ms - 100 ms) gönderin.

## Yeniden örnekleme

İstemci uygulamanızın, iletimden önce mikrofon girişini (genellikle 44,1 kHz veya 48 kHz) 16 kHz'ye yeniden örneklediğinden emin olun.

## Oturum yönetimi

Oturum yaşam döngüsünü yönetmek ve güvenilir bir kullanıcı deneyimi sağlamak için aşağıdaki yönergeleri uygulayın:

- **Bağlam penceresi sıkıştırmasını etkinleştirme:** Ses jetonları saniyede yaklaşık 25 jeton hızında birikir. Sıkıştırma olmadan yalnızca sesli oturumlar 15 dakika, sesli ve görüntülü oturumlar ise 2 dakika ile sınırlıdır. Oturumları sınırsız süreye uzatmak için [bağlam penceresi sıkıştırmasını](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=tr#context-window-compression) etkinleştirin.
- **Oturuma devam etme özelliğini uygulayın:** Sunucu, WebSocket bağlantısını düzenli olarak sıfırlayabilir. Bağlamı kaybetmeden sorunsuz bir şekilde yeniden bağlanmak için [oturum devam ettirme](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=tr#session-resumption) özelliğini kullanın. `SessionResumptionUpdate` iletilerinden en son devam ettirme jetonunu saklayın ve yeniden bağlanırken bunu işleyici olarak iletin. Devam ettirme jetonları, son oturumun sona ermesinden sonraki 2 saat boyunca geçerlidir.
- **GoAway mesajlarını işleme:** Sunucu, bağlantıyı sonlandırmadan önce bir [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=tr#goaway-message) mesajı gönderir. Bu mesajı dinleyin ve bağlantı kapanmadan önce
  `timeLeft` alanını kullanarak bağlantıyı düzgün bir şekilde sonlandırın veya yeniden bağlanın.
- **Yanıt oluşturma işleminin tamamlanmasıyla ilgili sinyaller:** Modelin yanıt oluşturmayı ne zaman tamamladığını öğrenmek için [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=tr#generation-complete-message) mesajını kullanın. Böylece uygulamanız kullanıcı arayüzünü güncelleyebilir veya bir sonraki işleme geçebilir.

Uygulama ayrıntıları için [Oturum yönetimi](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=tr) başlıklı makaleye bakın.

## Örnekler

Bu örnekte, modelin kariyer koçu olarak performansını yönlendirmek için hem en iyi uygulamalar hem de [sistem talimatı tasarımıyla ilgili yönergeler](#system-instruction-guidelines) bir araya getirilmiştir.

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### Araç tanımları

Bu JSON, kariyer koçu örneğinde çağrılan ilgili işlevleri tanımlar.
İşlevleri tanımlarken en iyi sonuçları elde etmek için işlevlerin adlarını, açıklamalarını, parametrelerini ve çağırma koşullarını ekleyin.

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

## Fiyatlandırma ve faturalandırma

Gemini Live API, yalnızca jeton kullanımına göre faturalandırılır. Live API, kalıcı bir WebSocket oturumu sürdürdüğünden faturalandırma, etkin bağlam penceresine dayalı olarak bileşik bir modeli izler.

### Oturum bağlam penceresi (bileşik maliyetler)

API, oturum bağlam penceresinde bulunan tüm jetonlar için dönüş başına ücret alır. "Dönüş", bir kullanıcı girişi ve modelin buna karşılık gelen yanıtı olarak tanımlanır.

- **Birikim:** Bağlam penceresi, mevcut dönüşteki yeni jetonların yanı sıra önceki dönüşlerde birikmiş tüm jetonları içerir.
- **Yeniden faturalandırma:** Geçmiş jetonlar yeniden işlenir ve yapılandırılmış bağlam penceresi boyutunuza kadar her yeni dönüşte hesaba katılır. Oturum uzadıkça sohbet geçmişi yeniden işlendiği için dönüş başına maliyet artar.

### Ses jetonları ve transkriptler

Live API, doğal olarak çok formatlıdır. Akustik nüansı ve tonu korumak için sohbet geçmişini ham ses jetonları olarak saklar.

- **Ses faturalandırması:** API, her dönüşte biriken doğal ses jetonları için standart ses girişi oranında fatura keser.
- **Transkripsiyon ek ücreti:** Ses-metin transkripsiyonu etkinleştirildiğinde (`inputAudioTranscription` veya `outputAudioTranscription`), API, standart ses jetonu maliyetlerine ek olarak transkripsiyon için oluşturulan tüm metin jetonlarını metin jetonu çıkış oranında ücretlendirir.

### Bağlam sınırlarıyla maliyetleri yönetme

Uzun oturumlarda sınırsız maliyet artışını önlemek için bağlam penceresi boyutunuzu `contextWindowCompression` kullanarak yapılandırın.

Bir sıkıştırma tetikleyicisi (ör.25.000 jeton) ve kayan pencere (ör.8.000 jeton) ayarlayarak eşik değerine ulaşıldığında API, eski jetonları otomatik olarak çıkarır. API, sonraki dönüşler için yalnızca saklanan geçmiş ve yeni jetonlar üzerinden faturalandırma yapar.

### Proaktif ses

Proaktif ses etkinleştirildiğinde API, Live API dinlerken giriş jetonları için tüm süre boyunca ücret alır ve çıkış jetonları için yalnızca API yanıt verdiğinde ücret alır.

- **Gemini 3.8 ile ilgili not:** Proaktif ses, `gemini-3.8-live` ve `gemini-3.8-live-extended-thinking`'de kalıcı olarak etkinleştirilir.
- **Gemini 3.1 ile ilgili not:** Proaktif ses özelliği `gemini-3.1-flash-live-preview`'da desteklenmez. Bu modelde API, yalnızca girişi aktif olarak yayınladığınızda ses için faturalandırır.

Ayrıntılı fiyatlandırma bilgileri için [Gemini API fiyatlandırma sayfasını](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-17 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-17 UTC."],[],[]]
