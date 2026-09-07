---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=tr
fetched_at: 2026-09-07T05:35:43.209903+00:00
title: "Ajan tabanl\u0131 g\u00f6r\u00fc\u015f yetenekleri \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Ajan tabanlı görüş yetenekleri

Gemini Robotics ER modelleri, resimleri değiştirmek ve yanıt vermeden önce mantık uygulamak için Python kodu yazıp yürütebilir. Bu sayfada, kod yürütme örnekleri (yakınlaştırma ve kırpma ile nesne tespit etme, cihaz okuma, sıvı ölçümü, devre kartı okuma ve görüntü ek açıklaması) ele alınmaktadır.

Bu örnekleri kendi kullanım alanınıza uyarlamak için istem metnini ve yüklenen resim dosyasını kendinizinkilerle değiştirin. Ayrıca, istemdeki istenen JSON şemasını uygulamanızın ihtiyaç duyduğu çıkış yapısına uyacak şekilde ayarlayabilir veya çıkış biçimini ve doğruluğunu zorunlu kılmak için `system_instruction` ekleyebilirsiniz.

Çalıştırılabilir kodun tamamı için [Robotics cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)'a (Robotik yemek kitabı) bakın.

## Düşünme düzeyi

Gecikmeyi doğrulukla değiştirmek için düşünme düzeyini kontrol edebilirsiniz. Nesne tespit etme gibi uzamsal görevler, düşük düşünme seviyesinde iyi performans gösterir. Sayma veya ağırlık tahmini gibi karmaşık görevler, daha yüksek bir düşünme seviyesinden yararlanır.

Aşağıdaki örnekte, karmaşık bir sayma görevi için düşünme düzeyi `high` olarak ayarlanmıştır:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('scene.jpeg', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        "Identify and count all objects on the table."
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    )
)

print(response.text)
```

Ayrıntılar için [Thinking](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=tr) (Düşünme) bölümüne bakın.

## Nesne tespit etme (yakınlaştırma ve kırpma)

Aşağıdaki örnekte, nesneleri algılarken ve sınırlayıcı kutuları döndürürken daha net bir görünüm için kodu yürütme özelliğini kullanarak bir resmi nasıl yakınlaştırıp kırpacağınız gösterilmektedir.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Return JSON in the format {label: val, y: val, x: val, y2: val, x2: val} for
the compostable objects in this scene. Please Zoom and crop the image for a
clearer view. Return an annotated image of the final result with the bounding
boxes drawn on it to the API caller as a part of your process.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

Model çıkışı, aşağıdaki JSON yanıtına benzer olacaktır:

```
[
  {"label": "compostable", "y": 256, "x": 482, "y2": 295, "x2": 546},
  {"label": "compostable", "y": 317, "x": 478, "y2": 350, "x2": 542},
  {"label": "compostable", "y": 586, "x": 556, "y2": 668, "x2": 595},
  {"label": "compostable", "y": 463, "x": 669, "y2": 511, "x2": 718},
  {"label": "compostable", "y": 178, "x": 565, "y2": 250, "x2": 609}
]
```

Aşağıdaki resimde, modelden döndürülen kutular gösterilmektedir.

![Bulunan nesnelerin sınırlayıcı kutularını gösteren bir örnek](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-bounding-boxes.png?hl=tr)

## Analog bir göstergeyi okuma ve mantık uygulama

Aşağıdaki örnekte, analog bir ölçüm cihazını okumak ve zaman hesaplamaları yapmak için modelin nasıl kullanılacağı gösterilmektedir. JSON çıkışını zorunlu kılmak için sistem talimatı kullanır.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('gauge.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read the current value from this gauge. Then, calculate how long
        it will take at the current rate for the value to reach maximum.
        Reply in JSON: {"current_value": val, "max_value": val,
        "time_to_max_minutes": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## Bir kaptaki sıvıyı ölçme

Aşağıdaki örnekte, bir kaptaki sıvı seviyesini ölçmek için kod yürütmenin nasıl kullanılacağı gösterilmektedir.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('fluid.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Measure the amount of fluid in the container. Reply in JSON:
        {"fluid_level_ml": val, "container_capacity_ml": val,
        "percentage_full": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## Devre kartındaki işaretleri okuma

Aşağıdaki örnekte, devre kartındaki işaretleri okumak için kod yürütmenin nasıl kullanılacağı gösterilmektedir.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('circuit_board.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read all visible component labels and markings on this circuit
        board. Reply in JSON: {"components": [{"label": val,
        "location": [y, x]}]}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

![Bir devre kartındaki işaretleri gösteren örnek](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-circuit-board.png?hl=tr)

## Resim ek açıklaması

Aşağıdaki örnekte, kod yürütme özelliğini kullanarak bir resmi nasıl açıklayacağınız (ör. imha talimatları için ok çizme) ve değiştirilen resmi nasıl döndüreceğiniz gösterilmektedir.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Look at this image and return it as an annotated version using arrows of
different colors to represent which items should go in which bins for
disposal. You must return the final image to the API caller.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

Aşağıda örnek bir resim girişi verilmiştir.

![Okumak için saat gösteren bir örnek](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-image-annotation.png?hl=tr)

Model çıkışı aşağıdaki gibi olur:

```
  The annotated image shows the suggested disposal locations for the items on the table:
  - **Green bin (Compost/Organic)**: Green chili, red chili, grapes, and cherries.
  - **Blue bin (Recycling)**: Yellow crushed can and plastic container.
  - **Black bin (Trash)**: Chocolate bar wrapper, Welch's packet, and white tissue.
```

## Sırada ne var?

- [Görev düzenleme](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=tr): Özel robot API'leri içeren uzun vadeli görevler.
- [Yayın özellikli robotik](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=tr): Gerçek zamanlı çift yönlü yayın (yalnızca Gemini Robotics ER 2).
- [Video anlama](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=tr): Anları bulma ve ilerleme sınıflandırması (yalnızca Gemini Robotics ER 2).

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-04 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-04 UTC."],[],[]]
