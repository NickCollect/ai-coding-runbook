---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=tr
fetched_at: 2026-08-24T02:33:37.656028+00:00
title: "Mekansal ak\u0131l y\u00fcr\u00fctme \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Mekansal akıl yürütme

Gemini Robotics ER modelleri, nesneleri işaret edebilir, videoda takip edebilir, sınırlayıcı kutularla algılayabilir ve hareket yörüngeleri oluşturabilir. Bu sayfadaki tüm örneklerde `generateContent` ile doğal dil istemleri kullanılır.

Çalıştırılabilir kodun tamamı için [Robotics cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)'a (Robotik yemek kitabı) bakın.

## Nesneleri işaret etme

Aşağıdaki örnekte, bir resimdeki belirli nesneler bulunur ve bu nesnelerin normalleştirilmiş `[y, x]` koordinatları döndürülür:

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

# Load your image
with open("my-image.png", 'rb') as f:
    image_bytes = f.read()

image_response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
        PROMPT
    ],
    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    )
)

print(image_response.text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-2-preview:generateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "'"${IMAGE_BASE64}"'"
            }
          },
          {
            "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
          }
        ]
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "high"
      }
    }
  }'
```

Çıktı, her biri `point` (normalleştirilmiş `[y, x]` koordinatları) ve nesneyi tanımlayan bir `label` içeren nesnelerden oluşan bir JSON dizisi olacaktır.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

Aşağıdaki resimde, bu noktaların nasıl gösterilebileceğine dair bir örnek verilmiştir:

![Resimdeki nesnelerin noktalarını gösteren bir örnek](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=tr)

## Videodaki nesneleri izleme

Gemini Robotics ER 2, nesneleri zaman içinde takip etmek için video karelerini de analiz edebilir. Desteklenen video biçimlerinin listesi için [Video girişleri](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr#supported-formats) bölümüne bakın.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your video
with open("my-video.mp4", 'rb') as f:
    video_bytes = f.read()

prompt = """
          Point to the red ball in every frame where it appears.
          The answer should follow the json format: [{"point": [y, x],
          "label": <label>}, ...]. The points are in [y, x] format
          normalized to 0-1000. Return one entry per frame that contains
          the object.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-2-preview",
  contents=[
    types.Part.from_bytes(
      data=video_bytes,
      mime_type='video/mp4',
    ),
    prompt
  ],
  config = types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(thinking_level="high")
  )
)

print(image_response.text)
```

## Nesne tespit etme ve sınırlayıcı kutular

Noktalara ek olarak, modelden algılanan nesneler için daha fazla mekansal ayrıntı sağlayan 2 boyutlu sınırlayıcı kutular döndürmesini de isteyebilirsiniz.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open("my-image.png", 'rb') as f:
    image_bytes = f.read()

prompt = """
          Detect all objects in this image and return bounding boxes.
          The answer should follow the JSON format:
          [{"label": <label>, "y": <y_min>, "x": <x_min>,
            "y2": <y_max>, "x2": <x_max>}, ...]
          where coordinates are normalized to 0-1000.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-2-preview",
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/png',
    ),
    prompt
  ],
  config = types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(thinking_level="low")
  )
)

print(image_response.text)
```

## Yörüngeler

Gemini Robotics ER 2, robot hareketini yönlendirmek için yararlı olan ve bir yörüngeyi tanımlayan nokta dizileri oluşturabilir.

Bu örnekte, kırmızı kalemi bir düzenleyiciye taşımak için ara yol noktalarının tahmini de dahil olmak üzere bir yörünge isteniyor. Kod, yalnızca istemi gösterecek şekilde kısaltıldı.

### Python

```
prompt = """
          Generate a trajectory for the robotic arm to pick up the red pen
          and place it in the organizer. Return a list of waypoints as JSON:
          [{"step": <int>, "point": [y, x], "action": <description>}, ...]
          where coordinates are normalized to 0-1000.
        """
```

## Dizüstü bilgisayar için yer açma

Bu örnekte, Gemini Robotics ER'ın bir alan hakkında nasıl akıl yürütebileceği gösterilmektedir. İstemde, başka bir öğeye yer açmak için hangi nesnenin taşınması gerektiği soruluyor.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('path/to/image-with-objects.jpg', 'rb') as f:
    image_bytes = f.read()

prompt = """
          Point to the object that I need to remove to make room for my laptop
          The answer should follow the JSON format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-2-preview",
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/jpeg',
    ),
    prompt
  ],
  config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(thinking_level="high")
  )
)

print(image_response.text)
```

Yanıtta, kullanıcının sorusunu yanıtlayan nesnenin 2 boyutlu koordinatı yer alır. Bu örnekte, dizüstü bilgisayara yer açmak için taşınması gereken nesne söz konusudur.

```
[
  {"point": [672, 301], "label": "The object that I need to remove to make room for my laptop"}
]
```

![Başka bir nesne için hangi nesnenin taşınması gerektiğini gösteren örnek](https://ai.google.dev/static/gemini-api/docs/images/robotics/spatial-reasoning.png?hl=tr)

## Öğle yemeği hazırlama

Model, çok adımlı görevlerle ilgili talimatlar da verebilir ve her adım için ilgili nesneleri gösterebilir. Bu örnekte, modelin bir beslenme çantasını hazırlamak için bir dizi adımı nasıl planladığı gösterilmektedir.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('path/to/image-of-lunch.jpg', 'rb') as f:
    image_bytes = f.read()

prompt = """
          Explain how to pack the lunch box and lunch bag. Point to each
          object that you refer to. Each point should be in the format:
          [{"point": [y, x], "label": }], where the coordinates are
          normalized between 0-1000.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-2-preview",
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/jpeg',
    ),
    prompt
  ],
  config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(thinking_level="high")
  )
)

print(image_response.text)
```

Bu istemin yanıtı, resim girişinden yola çıkarak bir öğle yemeği çantasını nasıl paketleyeceğinizle ilgili adım adım talimatlar içerir.

**Giriş resmi**

![Yemek kutusu ve içine konulacak öğelerin resmi](https://ai.google.dev/static/gemini-api/docs/images/robotics/packing-lunch.png?hl=tr)

**Model çıkışı**

```
Based on the image, here is a plan to pack the lunch box and lunch bag:

1.  **Pack the fruit into the lunch box.** Place the [apple](apple), [banana](banana), [red grapes](red grapes), and [green grapes](green grapes) into the [blue lunch box](blue lunch box).
2.  **Add the spoon to the lunch box.** Put the [blue spoon](blue spoon) inside the lunch box as well.
3.  **Close the lunch box.** Secure the lid on the [blue lunch box](blue lunch box).
4.  **Place the lunch box inside the lunch bag.** Put the closed [blue lunch box](blue lunch box) into the [brown lunch bag](brown lunch bag).
5.  **Pack the remaining items into the lunch bag.** Place the [blue snack bar](blue snack bar) and the [brown snack bar](brown snack bar) into the [brown lunch bag](brown lunch bag).

Here is the list of objects and their locations:
*   [{"point": [899, 440], "label": "apple"}]
*   [{"point": [814, 363], "label": "banana"}]
*   [{"point": [727, 470], "label": "red grapes"}]
*   [{"point": [675, 608], "label": "green grapes"}]
*   [{"point": [706, 529], "label": "blue lunch box"}]
*   [{"point": [864, 517], "label": "blue spoon"}]
*   [{"point": [499, 401], "label": "blue snack bar"}]
*   [{"point": [614, 705], "label": "brown snack bar"}]
*   [{"point": [448, 501], "label": "brown lunch bag"}]
```

## Sırada ne var?

- [Ajan tabanlı yetenekler](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=tr): Kod yürütme, enstrüman okuma, görüntü açıklama.
- [Görev düzenleme](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=tr): Özel robot API'leri içeren uzun vadeli görevler.
- [Yayın özellikli robotik](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=tr): Gerçek zamanlı çift yönlü yayın (yalnızca Gemini Robotics ER 2).
- [Video anlama](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=tr): Anları bulma ve ilerleme sınıflandırması (yalnızca Gemini Robotics ER 2).

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
