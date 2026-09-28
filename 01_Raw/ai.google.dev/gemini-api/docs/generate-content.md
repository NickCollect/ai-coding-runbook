---
source_url: https://ai.google.dev/gemini-api/docs/generate-content?hl=tr
fetched_at: 2026-09-28T06:16:43.233645+00:00
title: "Gemini API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/generate-content?hl=tr)

# Gemini API

Gemini API; Gemini, Veo ve Nano Banana gibi araçlarla istemden üretime en hızlı geçişi sağlar. Bu üretken modelleri uygulamalarınıza entegre ederek metin ve resim oluşturabilir, çok formatlı girişleri analiz edebilir ve sohbet aracısı oluşturabilirsiniz.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.8-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3.8-flash", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

[Oluşturmaya başlama](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)

---

## Modellerle tanışın

[Tümünü görüntüleyin](https://ai.google.dev/gemini-api/docs/models?hl=tr)

[auto\_awesome
Gemini 3.1 Pro
Yeni

En akıllı modelimiz, en son teknoloji ürünü akıl yürütme üzerine inşa edilmiş olup çok formatlı anlama konusunda dünyanın en iyisidir.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=tr)
[spark
Gemini 3.6 Flash
Yeni

Ajan ve çok formatlı görevlerde yüksek performans sunmak için hız ile zekayı dengeleyen en yeni modelimiz.](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=tr)
[spark
Gemini 3.5 Flash

Maliyetinin çok daha düşük olmasına rağmen daha büyük modellerle yarışan Frontier sınıfı performans.](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=tr)
[graphic\_eq
Gemini 3.8 Flash TTS
Yeni

İfade dolu oyunculuk, özel ses tasarımı ve ses kopyalama özelliklerine sahip, stüdyo kalitesinde metin okuma modeli.](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=tr)
[spark
Gemini 3.5 Flash-Lite
Yeni

Yüksek hacimli, maliyet açısından hassas ve düşük gecikmeli yüksek gönderim hacmiyle alt aracı görevleri için optimize edilmiş model.](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=tr)
[spark
Gemini 3.1 Flash-Lite

Gemini 3 serisinin performans ve kalitesine sahip, yüksek hacimli ve maliyete duyarlı model.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr)
[spark
Gemini 3 Flash

Maliyetinin çok daha düşük olmasına rağmen daha büyük modellerle yarışan Frontier sınıfı performans.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=tr)
[🍌
Nano Banana 2 ve Nano Banana Pro

En gelişmiş görüntü üretme ve düzenleme modelleri](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)
[video\_library
Veo 3.1

Doğal ses özelliğine sahip, son teknolojiyle geliştirilen video üretme modelimiz.](https://ai.google.dev/gemini-api/docs/video?hl=tr)
[spark
Gemini Robotics

Gemini'ın ajan tabanlı yeteneklerini robotik alana taşıyan ve fiziksel dünyada gelişmiş akıl yürütme imkanı sunan bir görsel-dil modeli (VLM).](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=tr)

## Özellikleri keşfedin

[imagesmode

Yerel görüntü üretme (Nano Banana)

Gemini 2.5 Flash Image ile bağlamı yüksek görselleri doğrudan oluşturup düzenleyin.](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)
[article

Uzun Bağlam

Gemini modellerine milyonlarca jeton girin ve yapılandırılmamış resimler, videolar ve dokümanlardan bilgi edinin.](https://ai.google.dev/gemini-api/docs/long-context?hl=tr)
[code

Yapılandırılmış Çıkışlar

Gemini'ın, otomatik işleme için uygun bir yapılandırılmış veri biçimi olan JSON ile yanıt vermesini sağlayın.](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr)
[functions

İşlev Çağrısı

Gemini'ı harici API'lere ve araçlara bağlayarak ajans iş akışları oluşturun.](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)
[videocam

Veo 3.1 ile video üretimi

Son teknolojiyle geliştirilen modelimizle metin veya görüntü istemlerinden yüksek kaliteli video içerikleri oluşturun.](https://ai.google.dev/gemini-api/docs/video?hl=tr)
[android\_recorder

Live API ile Sesli Ajanlar

Live API ile anında ses uygulamaları ve aracıları oluşturun.](https://ai.google.dev/gemini-api/docs/live-api?hl=tr)
[build

Araçlar

Google Arama, URL Bağlamı, Google Haritalar, Kod Yürütme ve Bilgisayar Kullanımı gibi yerleşik araçlar aracılığıyla Gemini'ı dünyaya bağlayın.](https://ai.google.dev/gemini-api/docs/tools?hl=tr)
[stacks

Belge Anlama

Tam çok formatlı anlayışla veya diğer metin tabanlı dosya türleriyle 1.000 sayfaya kadar PDF dosyası işleyin.](https://ai.google.dev/gemini-api/docs/document-processing?hl=tr)
[cognition\_2

Düşünen

Düşünme yeteneklerinin, karmaşık görevler ve ajanlar için akıl yürütmeyi nasıl iyileştirdiğini keşfedin.](https://ai.google.dev/gemini-api/docs/thinking?hl=tr)

[Google AI Studio

İstemleri test edin, API anahtarlarınızı yönetin, kullanımı izleyin ve prototipler oluşturun.](https://aistudio.google.com?hl=tr)
[group

Geliştirici Topluluğu

Diğer geliştiricilere ve Google mühendislerine soru sorarak çözümler bulabilirsiniz.](https://discuss.ai.google.dev/c/gemini-api/4?hl=tr)
[menu\_book

API Referansı

Gemini API hakkında ayrıntılı bilgiyi resmi referans belgelerinde bulabilirsiniz.](https://ai.google.dev/api?hl=tr)
[sensors

Durum

Gemini API, Google AI Studio ve model hizmetlerimizin durumunu kontrol edin.](https://aistudio.google.com/status?hl=tr)

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-24 UTC.

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-24 UTC."],[],[]]
