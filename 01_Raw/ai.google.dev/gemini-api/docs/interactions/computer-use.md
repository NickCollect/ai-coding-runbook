---
source_url: https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=tr
fetched_at: 2026-06-01T05:58:50.549197+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Bilgisayar Kullanımı

Bilgisayar Kullanımı, görevlerle etkileşime giren ve görevleri otomatikleştiren tarayıcı kontrol temsilcileri oluşturmanıza olanak tanır. Model, ekran görüntülerini kullanarak bilgisayar ekranını "görebilir" ve fare tıklamaları ile klavye girişleri gibi belirli kullanıcı arayüzü işlemleri oluşturarak "hareket edebilir". İşlev çağrısına benzer şekilde, Bilgisayar Kullanımı işlemlerini almak ve yürütmek için istemci tarafı uygulama kodunu yazmanız gerekir.

Bilgisayar Kullanımı ile aşağıdaki özelliklere sahip temsilciler oluşturabilirsiniz:

- Web sitelerinde tekrarlayan veri girişini veya form doldurma işlemlerini otomatikleştirin.
- Web uygulamalarının ve kullanıcı akışlarının otomatik testini gerçekleştirme
- Çeşitli web sitelerinde araştırma yapma (ör. satın alma işlemi hakkında bilgi vermek için e-ticaret sitelerinden ürün bilgileri, fiyatlar ve yorumlar toplama)

Bilgisayar Kullanımı özelliğini test etmenin en kolay yolu [referans uygulama](https://github.com/google/computer-use-preview/) veya [Browserbase demo ortamı](http://gemini.browserbase.com) üzerinden test etmektir.

## Bilgisayar Kullanımı nasıl çalışır?

Bilgisayar Kullanımı modeliyle bir tarayıcı kontrolü aracısı oluşturmak için aşağıdakileri yapan bir aracı döngüsü uygulayın:

1. [**Modele istek gönderme**](#send-request)

   - Bilgisayar Kullanımı aracını ve isteğe bağlı olarak özel kullanıcı tanımlı işlevleri veya hariç tutulan işlevleri API isteğinize ekleyin.
   - Bilgisayar Kullanımı modeline kullanıcının isteğini girin.
2. [**Model yanıtını alma**](#model-response)

   - Bilgisayar Kullanımı modeli, kullanıcı isteğini ve ekran görüntüsünü analiz eder ve bir kullanıcı arayüzü işlemini temsil eden önerilen `function_call`'ı içeren bir yanıt oluşturur (ör. "(x,y) koordinatına tıklayın" veya "metin yazın"). ComputerUse modeli tarafından desteklenen tüm kullanıcı arayüzü işlemlerinin açıklaması için [Desteklenen işlemler](#supported-actions) başlıklı makaleyi inceleyin.
   - API yanıtı, modelin önerdiği işlemi kontrol eden dahili bir güvenlik sisteminden gelen `safety_decision` de içerebilir. Bu
     `safety_decision` işlemi şu şekilde sınıflandırır:
     - **Normal / izin verilen:** İşlem güvenli olarak kabul edilir. Bu durum, `safety_decision` simgesinin olmamasıyla da gösterilebilir.
     - **Onay gerektiriyor (`require_confirmation`):** Model, riskli olabilecek bir işlem (ör. "çerez banner'ını kabul et" seçeneğini tıklama) gerçekleştirmek üzere.
3. [**Alınan işlemi yürütün**](#execute-actions)

   - İstemci tarafı kodunuz `function_call` ve beraberindeki `safety_decision` değerini alır.
     - **Normal / izin verilen:** `safety_decision` simgesi normal/izin verilen olarak gösteriliyorsa (veya `safety_decision` simgesi yoksa) istemci tarafı kodunuz, hedef ortamınızda (ör. web tarayıcısı) belirtilen `function_call` işlevini yürütebilir.
     - **Onay gerektirir:** `safety_decision`, onay gerektirdiğini gösteriyorsa uygulamanız, `function_call` yürütülmeden önce son kullanıcıdan onay istemelidir. Kullanıcı onaylarsa işlemi yürütmeye devam edin. Kullanıcı reddederse işlemi yürütmeyin.
4. [**Yeni ortam durumunu yakalama**](#capture-state)

   - İşlem yürütüldüyse istemciniz, `function_result` kapsamında Bilgisayar Kullanımı modeline geri göndermek için GUI'nin ve mevcut URL'nin yeni bir ekran görüntüsünü alır.
   - Bir işlem güvenlik sistemi tarafından engellendiyse veya kullanıcı tarafından onaylanmadıysa uygulamanız modele farklı bir geri bildirim biçimi gönderebilir ya da etkileşimi sonlandırabilir.

Bu işlem, sonraki işlemi önermek için yeni ekran görüntüsünü ve devam eden hedefi kullanan modelle 2. adımdan itibaren tekrarlanır. Döngü, görev tamamlanana, bir hata oluşana veya işlem sonlandırılana kadar (ör. "engelleme" güvenlik yanıtı veya kullanıcı kararı nedeniyle) devam eder.

![Bilgisayar Kullanımına Genel Bakış](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=tr)

## Bilgisayar Kullanımı nasıl uygulanır?

Bilgisayar Kullanımı aracıyla oluşturmaya başlamadan önce aşağıdakileri ayarlamanız gerekir:

- **Güvenli yürütme ortamı:** Güvenlik nedeniyle, Bilgisayar Kullanımı aracınızı güvenli ve kontrollü bir ortamda (ör. sınırlı izinlere sahip bir sanal makine, kapsayıcı veya özel tarayıcı profili) çalıştırmanız gerekir.
- **İstemci tarafı işlem işleyici:** Model tarafından oluşturulan işlemleri yürütmek ve her işlemden sonra ortamın ekran görüntülerini almak için istemci tarafı mantığını uygulamanız gerekir.

Bu bölümdeki örneklerde, yürütme ortamı olarak tarayıcı, istemci taraflı işlem işleyici olarak ise [Playwright](https://playwright.dev/) kullanılır. Bu örnekleri çalıştırmak için gerekli bağımlılıkları yüklemeniz ve bir Playwright tarayıcı örneği başlatmanız gerekir.

#### Playwright'ı yükleme

```
    pip install google-genai playwright
    playwright install chromium
```

#### Playwright tarayıcı örneğini başlatma

```
    from playwright.sync_api import sync_playwright

    # 1. Configure screen dimensions for the target environment
    SCREEN_WIDTH = 1440
    SCREEN_HEIGHT = 900

    # 2. Start the Playwright browser
    # In production, utilize a sandboxed environment.
    playwright = sync_playwright().start()
    # Set headless=False to see the actions performed on your screen
    browser = playwright.chromium.launch(headless=False)

    # 3. Create a context and page with the specified dimensions
    context = browser.new_context(
        viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT}
    )
    page = context.new_page()

    # 4. Navigate to an initial page to start the task
    page.goto("https://www.google.com")

    # The 'page', 'SCREEN_WIDTH', and 'SCREEN_HEIGHT' variables
    # will be used in the steps below.
```

Android ortamına genişletmeye yönelik örnek kod, [Özel kullanıcı tanımlı işlevleri kullanma](#custom-functions) bölümünde yer almaktadır.

### 1. Modele istek gönderme

API isteğinize Computer Use (Bilgisayar Kullanımı) aracını ekleyin ve modele, kullanıcının hedefini içeren bir istem gönderin. Bilgisayar Kullanımı desteklenen modellerden birini kullanmanız gerekir. Aksi takdirde hata alırsınız:

- `gemini-2.5-computer-use-preview-10-2025`
- `gemini-3-flash-preview`

İsteğe bağlı olarak aşağıdaki parametreleri de ekleyebilirsiniz:

- **Hariç tutulan işlemler:** [Desteklenen kullanıcı arayüzü işlemleri](#supported-actions) listesinde, modelin yapmasını istemediğiniz işlemler varsa bu işlemleri `excluded_predefined_functions` olarak belirtin.
- **Kullanıcı tanımlı işlevler:** Bilgisayar Kullanımı aracına ek olarak özel kullanıcı tanımlı işlevler de eklemek isteyebilirsiniz.

İstek gönderirken görüntü boyutunu belirtmenize gerek olmadığını unutmayın.
Model, piksel koordinatlarını ekranın yüksekliğine ve genişliğine göre ölçekleyerek tahmin eder.

### Python

```
from google import genai

client = genai.Client()

# Specify predefined functions to exclude (optional)
excluded_functions = ["drag_and_drop"]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    input="Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout.",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "excluded_predefined_functions": excluded_functions
        }
    ]
)

print(interaction)
```

Özel işlevlerin kullanıldığı bir örnek için [Özel kullanıcı tanımlı işlevleri kullanma](#custom-functions) başlıklı makaleye bakın.

### 2. Model yanıtını alma

Bilgisayar Kullanımı aracı etkinleştirildiğinde model, görevi tamamlamak için kullanıcı arayüzü işlemlerinin gerekli olduğunu belirlerse bir veya daha fazla `function_call` adımla yanıt verir.
Bilgisayar Kullanımı, paralel işlev çağrısını destekler. Bu sayede model, tek bir dönüşte birden fazla işlem döndürebilir.

Örnek bir model yanıtı aşağıda verilmiştir.

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "I will type the search query into the search bar. The search bar is in the center of the page."
        }
      ]
    },
    {
      "type": "function_call",
      "name": "type_text_at",
      "arguments": {
        "x": 371,
        "y": 470,
        "text": "highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping",
        "press_enter": true
      }
    }
  ]
}
```

### 3. Alınan işlemleri yürütme

Uygulama kodunuzun model yanıtını ayrıştırması, işlemleri yürütmesi ve sonuçları toplaması gerekir.

Aşağıdaki örnek kod, Computer Use model yanıtından işlev çağrılarını ayıklar ve bunları Playwright ile yürütülebilecek işlemlere çevirir.
Model, giriş resminin boyutlarından bağımsız olarak normalleştirilmiş koordinatlar (0-999) çıkarır. Bu nedenle, çeviri adımının bir parçası da bu normalleştirilmiş koordinatları tekrar gerçek piksel değerlerine dönüştürmektir.

Bilgisayar Kullanımı modeliyle kullanım için önerilen ekran boyutu (1440, 900)'dür. Model, sonuçların kalitesi etkilenebilse de herhangi bir çözünürlükte çalışır.

Bu örnekte yalnızca en yaygın 3 kullanıcı arayüzü işlemi (`open_web_browser`, `click_at` ve `type_text_at`) için uygulama yer aldığını unutmayın. Üretim kullanım alanları için, `excluded_predefined_functions` olarak açıkça eklemediğiniz sürece [Desteklenen işlemler](#supported-actions) listesindeki diğer tüm kullanıcı arayüzü işlemlerini uygulamanız gerekir.

### Python

```
from typing import Any, List, Tuple
import time

def denormalize_x(x: int, screen_width: int) -> int:
    """Convert normalized x coordinate (0-1000) to actual pixel coordinate."""
    return int(x / 1000 * screen_width)

def denormalize_y(y: int, screen_height: int) -> int:
    """Convert normalized y coordinate (0-1000) to actual pixel coordinate."""
    return int(y / 1000 * screen_height)

def execute_function_calls(interaction, page, screen_width, screen_height):
    results = []
    function_calls = [
        step for step in interaction.steps if step.type == "function_call"
    ]

    for function_call in function_calls:
        action_result = {}
        fname = function_call.name
        args = function_call.arguments
        print(f"  -> Executing: {fname}")

        try:
            if fname == "open_web_browser":
                pass # Already open
            elif fname == "click_at":
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)
                page.mouse.click(actual_x, actual_y)
            elif fname == "type_text_at":
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)
                text = args["text"]
                press_enter = args.get("press_enter", False)

                page.mouse.click(actual_x, actual_y)
                # Simple clear (Command+A, Backspace for Mac)
                page.keyboard.press("Meta+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(text)
                if press_enter:
                    page.keyboard.press("Enter")
            else:
                print(f"Warning: Unimplemented or custom function {fname}")

            # Wait for potential navigations/renders
            page.wait_for_load_state(timeout=5000)
            time.sleep(1)

        except Exception as e:
            print(f"Error executing {fname}: {e}")
            action_result = {"error": str(e)}

        results.append((fname, function_call.id, action_result))

    return results
```

### 4. Yeni ortam durumunu yakalama

İşlemleri yürüttükten sonra, işlev yürütme sonucunu modele geri gönderin. Böylece model, bu bilgileri kullanarak sonraki işlemi oluşturabilir. Birden fazla işlem (paralel çağrı) yürütüldüyse sonraki kullanıcı dönüşünde her biri için bir `function_result` göndermeniz gerekir.

### Python

```
import json
import base64

def get_function_responses(page, results):
    screenshot_bytes = page.screenshot(type="png")
    current_url = page.url
    function_responses = []
    for name, call_id, result in results:
        function_responses.append({
            "type": "function_result",
            "name": name,
            "call_id": call_id,
            "result": [
                {
                    "type": "text",
                    "text": json.dumps({"url": current_url, **result})
                },
                {
                    "type": "image",
                    "data": base64.b64encode(screenshot_bytes).decode("utf-8"),
                    "mime_type": "image/png"
                }
            ]
        })
    return function_responses
```

## Aracı döngüsü oluşturma

Çok adımlı etkileşimleri etkinleştirmek için [Bilgisayar kullanımını uygulama](#implement-computer-use) bölümündeki dört adımı bir döngüde birleştirin.
Hem model yanıtlarını hem de işlev yanıtlarınızı ekleyerek görüşme geçmişini doğru şekilde yönetmeyi unutmayın.

Bu kod örneğini çalıştırmak için:

- [Gerekli Playwright bağımlılıklarını](#implement-computer-use) yükleyin.
- [(3) Alınan işlemleri yürütün](#execute-actions) ve [(4) Yeni ortam durumunu yakalayın](#capture-state) adımlarındaki yardımcı işlevleri tanımlayın.

### Python

```
import time
from typing import Any, List, Tuple
from playwright.sync_api import sync_playwright

from google import genai

client = genai.Client()

# Constants for screen dimensions
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

# Setup Playwright
print("Initializing browser...")
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT})
page = context.new_page()

# Define helper functions. Copy/paste from steps 3 and 4
# def denormalize_x(...)
# def denormalize_y(...)
# def execute_function_calls(...)
# def get_function_responses(...)

try:
    # Go to initial page
    page.goto("https://ai.google.dev/gemini-api/docs")

    # Take initial screenshot
    initial_screenshot = page.screenshot(type="png")
    USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing."
    print(f"Goal: {USER_PROMPT}")

    # First interaction
    interaction = client.interactions.create(
        model='gemini-2.5-computer-use-preview-10-2025',
        input=[
            {"type": "text", "text": USER_PROMPT},
            {"type": "image", "data": base64.b64encode(initial_screenshot).decode("utf-8"), "mime_type": "image/png"}
        ],
        tools=[{
            "type": "computer_use",
            "environment": "browser"
        }]
    )

    # Agent Loop
    turn_limit = 5
    for i in range(turn_limit):
        print(f"\n--- Turn {i+1} ---")

        has_function_calls = any(
            step.type == "function_call"
            for step in interaction.steps
        )
        if not has_function_calls:
            text_response = " ".join([
                content_block.text for step in interaction.steps if step.type == "model_output"
                for content_block in step.content if content_block.type == "text"
            ])
            print("Agent finished:", text_response)
            break

        print("Executing actions...")
        results = execute_function_calls(interaction, page, SCREEN_WIDTH, SCREEN_HEIGHT)

        print("Capturing state...")
        function_responses = get_function_responses(page, results)

        # Continue conversation with function responses
        interaction = client.interactions.create(
            model='gemini-2.5-computer-use-preview-10-2025',
            previous_interaction_id=interaction.id,
            input=function_responses,
            tools=[{
                "type": "computer_use",
                "environment": "browser"
            }]
        )

finally:
    # Cleanup
    print("\nClosing browser...")
    browser.close()
    playwright.stop()
```

## Özel kullanıcı tanımlı işlevleri kullanma

İsteğinize, modelin işlevselliğini genişletmek için isteğe bağlı olarak özel kullanıcı tanımlı işlevler ekleyebilirsiniz. Aşağıdaki örnekte, tarayıcıya özgü işlemler hariç tutulurken `open_app`, `long_press_at` ve `go_home` gibi özel kullanıcı tanımlı işlemler eklenerek Bilgisayar Kullanımı modeli ve aracı mobil kullanım alanlarına uyarlanmıştır. Model, tarayıcı dışı ortamlarda görevleri tamamlamak için bu özel işlevleri standart kullanıcı arayüzü işlemleriyle birlikte akıllıca çağırabilir.

### Python

```
from typing import Optional, Dict, Any

from google import genai

client = genai.Client()

SYSTEM_PROMPT = """You are operating an Android phone. Today's date is October 15, 2023, so ignore any other date provided.
* To provide an answer to the user, *do not use any tools* and output your answer on a separate line. IMPORTANT: Do not add any formatting or additional punctuation/text, just output the answer by itself after two empty lines.
* Make sure you scroll down to see everything before deciding something isn't available.
* You can open an app from anywhere. The icon doesn't have to currently be on screen.
* Unless explicitly told otherwise, make sure to save any changes you make.
* If text is cut off or incomplete, scroll or click into the element to get the full text before providing an answer.
* IMPORTANT: Complete the given task EXACTLY as stated. DO NOT make any assumptions that completing a similar task is correct.  If you can't find what you're looking for, SCROLL to find it.
* If you want to edit some text, ONLY USE THE `type` tool. Do not use the onscreen keyboard.
* Quick settings shouldn't be used to change settings. Use the Settings app instead.
* The given task may already be completed. If so, there is no need to do anything.
"""

# Custom function definitions for mobile
custom_functions = [
    {
        "type": "function",
        "name": "open_app",
        "description": "Opens an app by name.",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {"type": "string", "description": "Name of the app to open"},
                "intent": {"type": "string", "description": "Optional deep-link or action"}
            },
            "required": ["app_name"]
        }
    },
    {
        "type": "function",
        "name": "long_press_at",
        "description": "Long-press at a specific screen coordinate.",
        "parameters": {
            "type": "object",
            "properties": {
                "x": {"type": "integer", "description": "X coordinate"},
                "y": {"type": "integer", "description": "Y coordinate"}
            },
            "required": ["x", "y"]
        }
    },
    {
        "type": "function",
        "name": "go_home",
        "description": "Navigates to the device home screen.",
        "parameters": {"type": "object", "properties": {}}
    }
]

# Exclude browser-specific functions
excluded_functions = [
    "open_web_browser",
    "search",
    "navigate",
    "hover_at",
    "scroll_document",
    "go_forward",
    "key_combination",
    "drag_and_drop",
]

interaction = client.interactions.create(
    model='gemini-2.5-computer-use-preview-10-2025',
    system_instruction=SYSTEM_PROMPT,
    input="Open Chrome, then long-press at 200,400.",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "excluded_predefined_functions": excluded_functions
        },
        *custom_functions
    ]
)

print(interaction)
```

## Desteklenen kullanıcı arayüzü işlemleri

Model, `function_call` kullanarak aşağıdaki kullanıcı arayüzü işlemlerini isteyebilir. İstemci tarafı kodunuz, bu işlemlerin yürütme mantığını uygulamalıdır. Örnekler için [referans
uygulamaya](https://github.com/google/computer-use-preview) bakın.

| Komut Adı | Açıklama | Bağımsız değişkenler (işlev çağrısında) | Örnek İşlev Çağrısı |
| --- | --- | --- | --- |
| **open\_web\_browser** | Web tarayıcısını açar. | Yok | `{"name": "open_web_browser", "arguments": {}}` |
| **wait\_5\_seconds** | Dinamik içeriğin yüklenmesine veya animasyonların tamamlanmasına olanak tanımak için yürütmeyi 5 saniye duraklatır. | Yok | `{"name": "wait_5_seconds", "arguments": {}}` |
| **go\_back** | Tarayıcının geçmişinde önceki sayfaya gider. | Yok | `{"name": "go_back", "arguments": {}}` |
| **go\_forward** | Tarayıcının geçmişinde sonraki sayfaya gider. | Yok | `{"name": "go_forward", "arguments": {}}` |
| **search** | Varsayılan arama motorunun ana sayfasına (ör. Google) gider. Yeni bir arama görevine başlamak için kullanışlıdır. | Yok | `{"name": "search", "arguments": {}}` |
| **navigate** | Tarayıcıyı doğrudan belirtilen URL'ye yönlendirir. | `url`: str | `{"name": "navigate", "arguments": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | Web sayfasında belirli bir koordinattaki tıklamalar. X ve Y değerleri 1.000 x 1.000'lik bir ızgaraya dayanır ve ekran boyutlarına göre ölçeklendirilir. | `y`: int (0-999), `x`: int (0-999) | `{"name": "click_at", "arguments": {"y": 300, "x": 500}}` |
| **hover\_at** | Fareyi web sayfasında belirli bir koordinata getirir. Alt menüleri göstermek için kullanışlıdır. x ve y, 1000x1000'lik bir ızgaraya dayanır. | `y`: int (0-999) `x`: int (0-999) | `{"name": "hover_at", "arguments": {"y": 150, "x": 250}}` |
| **type\_text\_at** | Belirli bir koordinata metin yazar. Varsayılan olarak önce alanı temizler ve yazdıktan sonra ENTER tuşuna basar ancak bunlar devre dışı bırakılabilir. x ve y, 1000x1000'lik bir ızgaraya dayanır. | `y`: int (0-999), `x`: int (0-999), `text`: str, `press_enter`: bool (isteğe bağlı, varsayılan değer True), `clear_before_typing`: bool (isteğe bağlı, varsayılan değer True) | `{"name": "type_text_at", "arguments": {"y": 250, "x": 400, "text": "search query", "press_enter": false}}` |
| **key\_combination** | "Control+C" veya "Enter" gibi klavye tuşlarına ya da kombinasyonlarına basın. İşlemleri (ör. "Enter" tuşuyla form gönderme) veya pano işlemlerini tetiklemek için kullanışlıdır. | `keys`: str (ör. "enter", "control+c"). | `{"name": "key_combination", "arguments": {"keys": "Control+A"}}` |
| **scroll\_document** | Tüm web sayfasını "yukarı", "aşağı", "sola" veya "sağa" kaydırır. | `direction`: str ("up", "down", "left" veya "right") | `{"name": "scroll_document", "arguments": {"direction": "down"}}` |
| **scroll\_at** | Belirli bir öğeyi veya alanı, belirtilen yönde belirli bir büyüklükte (x, y) koordinatında kaydırır. Koordinatlar ve büyüklük (varsayılan 800), 1000x1000'lik bir ızgaraya dayanır. | `y`: int (0-999), `x`: int (0-999), `direction`: str ("up", "down", "left", "right"), `magnitude`: int (0-999, İsteğe bağlı, varsayılan 800) | `{"name": "scroll_at", "arguments": {"y": 500, "x": 500, "direction": "down", "magnitude": 400}}` |
| **drag\_and\_drop** | Bir öğeyi başlangıç koordinatından (x, y) sürükleyip hedef koordinata (destination\_x, destination\_y) bırakır. Tüm koordinatlar 1000x1000'lik bir ızgaraya dayanır. | `y`: int (0-999), `x`: int (0-999), `destination_y`: int (0-999), `destination_x`: int (0-999) | `{"name": "drag_and_drop", "arguments": {"y": 100, "x": 100, "destination_y": 500, "destination_x": 500}}` |

## Güvenlik

### Güvenlik kararını onaylama

Modele verilen yanıt, işleme bağlı olarak modelin önerdiği işlemi kontrol eden dahili bir güvenlik sisteminden gelen `safety_decision` de içerebilir.

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "I have evaluated step 2. It seems Google detected unusual traffic and is asking me to verify I'm not a robot. I need to click the 'I'm not a robot' checkbox located near the top left (y=98, x=95)."
        }
      ]
    },
    {
      "type": "function_call",
      "name": "click_at",
      "arguments": {
        "x": 60,
        "y": 100,
        "safety_decision": {
          "explanation": "I have encountered a CAPTCHA challenge that requires interaction. I need you to complete the challenge by clicking the 'I'm not a robot' checkbox and any subsequent verification steps.",
          "decision": "require_confirmation"
        }
      }
    }
  ]
}
```

`safety_decision` `require_confirmation` ise işleme devam etmeden önce son kullanıcıdan onayını almanız gerekir. [Hizmet şartlarına](https://ai.google.dev/gemini-api/terms?hl=tr) göre, insan onayı isteklerini atlamanıza izin verilmez.

Bu kod örneği, işlemi yürütmeden önce son kullanıcıdan onay ister. Kullanıcı işlemi onaylamazsa döngü sonlandırılır. Kullanıcı işlemi onaylarsa işlem yürütülür ve `safety_acknowledgement` alanı `True` olarak işaretlenir.

### Python

```
import termcolor

def get_safety_confirmation(safety_decision):
    """Prompt user for confirmation when safety check is triggered."""
    termcolor.cprint("Safety service requires explicit confirmation!", color="red")
    print(safety_decision["explanation"])

    decision = ""
    while decision.lower() not in ("y", "n", "ye", "yes", "no"):
        decision = input("Do you wish to proceed? [Y]es/[N]o\n")

    if decision.lower() in ("n", "no"):
        return "TERMINATE"
    return "CONTINUE"

def execute_function_calls(interaction, page, screen_width, screen_height):

    # ... Extract function calls from response ...

    for function_call in function_calls:
        extra_fr_fields = {}

        # Check for safety decision
        if 'safety_decision' in function_call.arguments:
            decision = get_safety_confirmation(function_call.arguments['safety_decision'])
            if decision == "TERMINATE":
                print("Terminating agent loop")
                break
            extra_fr_fields["safety_acknowledgement"] = True # Safety acknowledgement

        # ... Execute function call and append to results ...
```

Kullanıcı onaylarsa güvenlik onayını `function_result` bölümüne eklemeniz gerekir.

```
```python
function_responses.append({
    "type": "function_result",
    "name": name,
    "call_id": function_call.id,
    "result": [
        {
            "type": "text",
            "text": json.dumps({
                "url": current_url,
                "safety_acknowledgement": True,
                **extra_fr_fields
            })
        },
        {
            "type": "image",
            "data": base64.b64encode(screenshot_bytes).decode("utf-8"),
            "mime_type": "image/png"
        }
    ]
})
```
```

### Güvenlikle ilgili en iyi uygulamalar

Bilgisayar Kullanımı, geliştiricilerin dikkat etmesi gereken yeni riskler sunan yeni bir araçtır:

- **Güvenilmeyen içerikler ve dolandırıcılık:** Model, kullanıcının amacına ulaşmaya çalışırken güvenilmeyen bilgi kaynaklarına ve ekrandaki talimatlara güvenebilir. Örneğin, kullanıcının hedefi Pixel telefon satın almaksa ve model "Anketi tamamlarsanız ücretsiz Pixel" dolandırıcılığıyla karşılaşırsa modeli anketi tamamlama ihtimali vardır.
- **Bazen istenmeyen işlemler:** Model, kullanıcının amacını veya web sayfası içeriğini yanlış yorumlayarak yanlış düğmeyi tıklama ya da yanlış formu doldurma gibi hatalı işlemler yapabilir. Bu durum, görevlerin başarısız olmasına veya veri hırsızlığına yol açabilir.
- **Politika ihlalleri:** API'nin özellikleri, Google'ın politikalarını ([Üretken Yapay Zeka Yasaklanan Kullanım Politikası](https://policies.google.com/terms/generative-ai/use-policy?hl=tr) ve [Gemini API Ek Hizmet Şartları](https://ai.google.dev/gemini-api/terms?hl=tr)) ihlal eden faaliyetlere yönlendirilebilir (kasıtlı veya kasıtsız olarak). Bu tanım, bir sistemin bütünlüğünü etkileyebilecek, güvenliği tehlikeye atabilecek, güvenlik önlemlerini atlayabilecek, tıbbi cihazları kontrol edebilecek vb. işlemleri içerir.

Bu riskleri gidermek için aşağıdaki güvenlik önlemlerini ve en iyi uygulamaları kullanabilirsiniz:

1. **İnsanların dahil edilmesi (HITL):**

   - **Kullanıcı onayını uygulayın:** Güvenlik yanıtı `require_confirmation` gösterdiğinde yürütmeden önce kullanıcı onayını uygulamanız gerekir. Örnek kod için [Güvenlik kararını onaylama](#safety-decisions) başlıklı makaleyi inceleyin.
   - **Özel güvenlik talimatları sağlama:** Geliştiriciler, yerleşik kullanıcı onay kontrollerine ek olarak, kendi güvenlik politikalarını zorunlu kılan özel bir [sistem talimatı](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr#system-instructions) ekleyebilir. Bu talimat, belirli model işlemlerini engellemek veya modelin belirli yüksek riskli geri döndürülemez işlemleri yapmadan önce kullanıcı onayı almak için kullanılabilir. Modelle etkileşimde bulunurken ekleyebileceğiniz özel bir güvenlik sistemi talimatı örneğini aşağıda bulabilirsiniz.

     #### Güvenlik talimatı örnekleri

     Özel güvenlik kurallarınızı sistem talimatı olarak ayarlayın:

     ```
         ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

         This is your first and most important check. If the next required action falls
         into any of the following categories, you MUST stop immediately, and seek the
         user's explicit permission.

         **Procedure for Seeking Confirmation:**  * **For Consequential Actions:**
         Perform all preparatory steps (e.g., navigating, filling out forms, typing a
         message). You will ask for confirmation **AFTER** all necessary information is
         entered on the screen, but **BEFORE** you perform the final, irreversible action
         (e.g., before clicking "Send", "Submit", "Confirm Purchase", "Share").  * **For
         Prohibited Actions:** If the action is strictly forbidden (e.g., accepting legal
         terms, solving a CAPTCHA), you must first inform the user about the required
         action and ask for their confirmation to proceed.

         **USER_CONFIRMATION Categories:**

         *   **Consent and Agreements:** You are FORBIDDEN from accepting, selecting, or
             agreeing to any of the following on the user's behalf. You must ask the
             user to confirm before performing these actions.
             *   Terms of Service
             *   Privacy Policies
             *   Cookie consent banners
             *   End User License Agreements (EULAs)
             *   Any other legally significant contracts or agreements.
         *   **Robot Detection:** You MUST NEVER attempt to solve or bypass the
             following. You must ask the user to confirm before performing these actions.
         *   CAPTCHAs (of any kind)
             *   Any other anti-robot or human-verification mechanisms, even if you are
                 capable.
         *   **Financial Transactions:**
             *   Completing any purchase.
             *   Managing or moving money (e.g., transfers, payments).
             *   Purchasing regulated goods or participating in gambling.
         *   **Sending Communications:**
             *   Sending emails.
             *   Sending messages on any platform (e.g., social media, chat apps).
             *   Posting content on social media or forums.
         *   **Accessing or Modifying Sensitive Information:**
             *   Health, financial, or government records (e.g., medical history, tax
                 forms, passport status).
             *   Revealing or modifying sensitive personal identifiers (e.g., SSN, bank
                 account number, credit card number).
         *   **User Data Management:**
             *   Accessing, downloading, or saving files from the web.
             *   Sharing or sending files/data to any third party.
             *   Transferring user data between systems.
         *   **Browser Data Usage:**
             *   Accessing or managing Chrome browsing history, bookmarks, autofill data,
                 or saved passwords.
         *   **Security and Identity:**
             *   Logging into any user account.
             *   Any action that involves misrepresentation or impersonation (e.g.,
                 creating a fan account, posting as someone else).
         *   **Insurmountable Obstacles:** If you are technically unable to interact with
             a user interface element or are stuck in a loop you cannot resolve, ask the
             user to take over.
         ---

         ## **RULE 2: Default Behavior (ACTUATE)**

         If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`,
         your default behavior is to **Actuate**.

         **Actuation Means:**  You MUST proactively perform all necessary steps to move
         the user's request forward. Continue to actuate until you either complete the
         non-consequential task or encounter a condition defined in Rule 1.

         *   **Example 1:** If asked to send money, you will navigate to the payment
             portal, enter the recipient's details, and enter the amount. You will then
             **STOP** as per Rule 1 and ask for confirmation before clicking the final
             "Send" button.
         *   **Example 2:** If asked to post a message, you will navigate to the site,
             open the post composition window, and write the full message. You will then
             **STOP** as per Rule 1 and ask for confirmation before clicking the final
             "Post" button.

             After the user has confirmed, remember to get the user's latest screen
             before continuing to perform actions.

         # Final Response Guidelines:
         Write final response to the user in the following cases:
         - User confirmation
         - When the task is complete or you have enough information to respond to the user
     ```
2. **Güvenli yürütme ortamı:** Aracınızı, olası etkisini sınırlamak için güvenli ve korumalı bir ortamda (ör. korumalı bir sanal makine (VM), kapsayıcı (ör. Docker) veya sınırlı izinlere sahip özel bir tarayıcı profili) çalıştırın.
3. **Giriş temizleme:** İstenmeyen talimatlar veya istem enjeksiyonu riskini azaltmak için istemlerdeki kullanıcı tarafından oluşturulan tüm metinleri temizleyin. Bu, faydalı bir güvenlik katmanı olsa da güvenli bir yürütme ortamının yerini almaz.
4. **İçerik koruma sınırları:** Kullanıcı girişlerini, araç giriş ve çıkışını, aracının yanıtını uygunluk, istem ekleme ve jailbreak algılama açısından değerlendirmek için koruma sınırlarını ve [içerik güvenliği API'lerini](https://ai.google.dev/gemma/docs/shieldgemma?hl=tr) kullanın.
5. **İzin verilenler ve engellenenler listeleri:** Modelin nereye gidebileceğini ve neler yapabileceğini kontrol etmek için filtreleme mekanizmalarını uygulayın. Yasaklanmış web sitelerinin engellenenler listesi iyi bir başlangıç noktasıdır. Daha kısıtlayıcı bir izin verilenler listesi ise daha da güvenlidir.
6. **Gözlemlenebilirlik ve günlük kaydı:** Hata ayıklama, denetleme ve olaylara müdahale için ayrıntılı günlükler tutun. Müşteriniz istemleri, ekran görüntülerini, model tarafından önerilen işlemleri (function\_call), güvenlik yanıtlarını ve nihayetinde müşteri tarafından gerçekleştirilen tüm işlemleri günlüğe kaydetmelidir.
7. **Ortam yönetimi:** GUI ortamının tutarlı olmasını sağlayın.
   Beklenmedik pop-up'lar, bildirimler veya düzendeki değişiklikler modelin kafasını karıştırabilir. Mümkünse her yeni görev için bilinen ve temiz bir durumdan başlayın.

## Model sürümleri

`gemini-3-flash-preview`'da Bilgisayar Kullanımı için yerleşik destek bulunduğunu unutmayın. Araca erişmek için ayrı bir modele ihtiyacınız yoktur.

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | **Gemini API**  `gemini-2.5-computer-use-preview-10-2025` |
| saveDesteklenen veri türleri | **Giriş**  Resim, metin  **Çıkış**  Metin |
| token\_autoJeton sınırları[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) | **Giriş jetonu sınırı**  128.000  **Çıkış jetonu sınırı**  64.000 |
| 123Sürümleri | Daha fazla bilgi için [model sürümü kalıplarını](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#model-versions) okuyun.  - Önizleme: `gemini-2.5-computer-use-preview-10-2025` |
| calendar\_monthSon güncelleme | Ekim 2025 |

## Sırada ne var?

- [Browserbase demo ortamında](http://gemini.browserbase.com) bilgisayar kullanımıyla ilgili denemeler yapın.
- Örnek kod için [Referans uygulama](https://github.com/google/computer-use-preview) bölümüne göz atın.
- Diğer Gemini API araçları hakkında bilgi edinin:
  - [İşlev çağırma](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=tr)
  - [Google Arama ile temellendirme](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=tr)

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-28 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-28 UTC."],[],[]]
