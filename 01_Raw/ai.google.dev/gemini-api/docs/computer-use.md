---
source_url: https://ai.google.dev/gemini-api/docs/computer-use?hl=sq
fetched_at: 2026-10-12T07:00:02.428957+00:00
title: "P\u00ebrdorimi i kompjuterit \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash është tani në dispozicion. [Provojeni](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=sq) .

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs?hl=sq)

Dërgo komente

# Përdorimi i kompjuterit

Vegla e përdorimit të kompjuterit të lejon të krijosh agjentë kontrolli për shfletuesin, celularin dhe desktopin që ndërveprojnë dhe automatizojnë detyrat. Duke përdorur pamjet e ekranit, modeli mund të "shikojë" një ekran kompjuteri dhe të "veprojë" duke gjeneruar veprime specifike të ndërfaqes së përdoruesit, si p.sh. klikimet e miut dhe hyrjet e tastierës. Në mënyrë të ngjashme me thirrjen e funksionit, do të duhet të zbatosh mjedisin e ekzekutimit në anën e klientit për të marrë dhe ekzekutuar veprimet e "Përdorimit të kompjuterit".

Për listën e modeleve të mbështetura, shiko [Versionet e modelit](#model-versions). Modelet Gemini 3.x mbështesin disa aftësi të përparuara:

- **Mbështetja për shumë mjedise:** krijo agjentë për mjediset e [shfletuesit, celularit dhe desktopit](#supported-environments).
- **Veprimet e optimizuara me synimet:** veprimet përfshijnë një fushë `intent` që shpjegon arsyetimin e modelit pas çdo hapi.
- **Politikat e konfiguruara të sigurisë:** rregullo me saktësi [sjelljen e sigurisë](#safety-policies) me kategoritë e integruara të politikave dhe anulimet.
- **Zbulimi i injektimit të kërkesës:** zgjidh [skanimin e pamjeve të ekranit](#prompt-injection) për të zbuluar udhëzime të fshehura armiqësore.

Me "Përdorimin e kompjuterit", mund të krijosh agjentë që:

- Automatizo hyrjen e të dhënave të përsëritura ose plotësimin e formularëve në uebsajte.
- Kryej testimin e automatizuar të aplikacioneve të uebit dhe flukseve të përdoruesve
- Kryej kërkime nëpër uebsajte të ndryshme (p.sh. mbledhja e informacioneve për produktet, çmimet dhe komentet nga sajtet e tregtisë në internet për të informuar për një blerje)

Këtu është një shembull minimal i inicializimit të klientit dhe dërgimit të një kërkese te modeli me veglën `computer_use` të aktivizuar për një mjedis shfletuesi:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Search for 'Gemini API' on Google.",
    tools=[{"type": "computer_use", "environment": "browser"}]
)

print(interaction)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: 'gemini-3.8-flash',
  input: "Search for 'Gemini API' on Google.",
  tools: [{ type: "computer_use", environment: "browser" }]
});

console.log(interaction);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(InteractionsInput.of("Search for 'Gemini API' on Google."))
        .tools(
            Arrays.asList(
                ComputerUse.builder().environment(EnvironmentEnum.BROWSER).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Search for 'Gemini API' on Google."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment: interactions.EnvironmentEnumBrowser.ToPointer(),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction)
}
```

## Si funksionon "Përdorimi i kompjuterit"

Për të ndërtuar një agjent me modelin e përdorimit të kompjuterit, duhet të konfigurosh një lak të vazhdueshëm midis aplikacionit tënd dhe API-së. Ja se çfarë do të bëjë kodi yt në çdo hap:

1. [**Dërgo një kërkesë te modeli**](#send-request)
   - Aplikacioni yt dërgon një kërkesë për API-në që përmban veglën e "Përdorimit të kompjuterit", cilësimet e tua të konfigurimit (si p.sh. mjedisin e synuar), kërkesën e përdoruesit dhe një pamje ekrani të ekranit aktual.
2. [**Merr përgjigjen e modelit**](#model-response)
   - Modeli analizon ekranin dhe kërkesën, duke kthyer një përgjigje
     që përfshin një `function_call` të sugjeruar që përfaqëson një veprim të ndërfaqes së përdoruesit (si p.sh. një klikim, lëvizje ose goditje taste).
   - Për **modelet Gemini 3.x**, përgjigjja përfshin gjithashtu një arsyetim `intent`
     që shpjegon se pse modeli e zgjodhi atë veprim.
   - Përgjigjja mund të përfshijë gjithashtu një `safety_decision` nga një sistem i brendshëm sigurie që e klasifikon veprimin si të rregullt/të lejuar, `require_confirmation` (që kërkon miratimin e përdoruesit) ose të bllokuar.
3. [**Ekzekuto veprimin e marrë**](#execute-actions)
   - Nëse veprimi lejohet (ose nëse përdoruesi e konfirmon atë), kodi yt në anën e klientit analizon `function_call`, shkallëzon koordinatat e normalizuara që të përputhen me portën tënde të pamjes dhe ekzekuton veprimin në mjedisin tënd të synuar duke përdorur veglat e automatizimit (si p.sh. Playwright). Nëse veprimi është i bllokuar, klienti yt duhet të ndalojë ekzekutimin ose të menaxhojë ndërprerjen.
4. [**Regjistro gjendjen e re të mjedisit**](#capture-state)
   - Pasi të përfundojë ekzekutimi i veprimit, aplikacioni yt kap një pamje të re ekrani dhe e dërgon përsëri te modeli në një `function_result` për të kërkuar hapin tjetër.

Ky proces më pas përsëritet nga hapi 2, duke kërkuar vazhdimisht veprimin e radhës nga modeli derisa detyra të përfundohet ose të ndërpritet.

![Përmbledhja e përdorimit të kompjuterit](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=sq)

## Si të zbatosh "Përdorimin e kompjuterit"

Para se të krijosh me veglën "Përdorimi i kompjuterit", do të duhet të konfigurosh:

- **Mjedisi i ekzekutimit të sigurt:** Ekzekuto agjentin tënd në një makinë virtuale ose
  kontejner të kufizuar për ta izoluar atë nga sistemi yt pritës dhe për të kufizuar ndikimin e tij të mundshëm.
  [Zbatimi i referencës](https://github.com/google/computer-use-preview/)
  përfshin një zonë testimi të bazuar në Docker që është gati për t'u përdorur dhe që mund ta përdorësh si pikënisje.
- **Menaxheri i veprimit në anën e klientit:** Zbato logjikën në anën e klientit për të ekzekutuar koordinatat, për të shkruar tekst dhe për të bërë pamje ekrani.

Shembujt e mëposhtëm përdorin një shfletues uebi si mjedis ekzekutimi dhe
[Playwright](https://playwright.dev/) si trajtuar në anën e klientit.

### 0. Konfiguro Playwright

Në fillim, instalo paketat e kërkuara:

```
pip install google-genai playwright
playwright install chromium
```

Më pas, inicializo një shembull të shfletuesit Playwright për ta përdorur për ekzekutimin:

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

### 1. Dërgo një kërkesë te modeli

Inicializo bibliotekën e klientit dhe konfiguro veglën "Përdorimi i kompjuterit". Ki parasysh se nuk ka nevojë të specifikosh madhësinë e ekranit kur lëshon një kërkesë; modeli parashikon koordinatat e pikselëve të shkallëzuara sipas lartësisë dhe gjerësisë së ekranit.

### Python

Përdor `google-genai` Python SDK (versioni `2.7.0` ose më i lartë) për të konfiguruar një kërkesë që synon mjedisin e shfletuesit:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input="Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th",
    tools=[
        {
            "type": "computer_use",
            "environment": "browser",
            "enable_prompt_injection_detection": True
        }
    ]
)

print(interaction)
```

### JavaScript

Përdor `@google/genai` Node.js SDK për të konfiguruar një kërkesë që synon mjedisin e shfletuesit:

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: 'gemini-3.8-flash',
  input: "Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th",
  tools: [
    {
      type: "computer_use",
      environment: "browser",
      enable_prompt_injection_detection: true
    }
  ]
});

console.log(interaction);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(
            InteractionsInput.of(
                "Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th"))
        .tools(
            Arrays.asList(
                ComputerUse.builder()
                    .environment(EnvironmentEnum.BROWSER)
                    .enablePromptInjectionDetection(true)
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Find a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th"),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment:                    interactions.EnvironmentEnumBrowser.ToPointer(),
                    EnablePromptInjectionDetection: genai.Ptr(true),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction)
}
```

### QETËSI

Përdor curl për të dërguar një kërkesë:

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Find me a flight from SF to Hawaii on Jun 30th, coming back on Jul 6th. Start by navigating directly to flights.google.com",
    "tools": [
      {
        "type": "computer_use",
        "environment": "browser",
        "enable_prompt_injection_detection": true
      }
    ]
  }'
```

### 2. Merr përgjigjen e modelit

Përgjigjja e modelit sugjeron një thirrje funksioni që përfshin koordinatat dhe një qëllim të personalizuar arsyetimi që shpjegon veprimin:

```
{
  "steps": [
    {
      "type": "function_call",
      "name": "click",
      "arguments": {
        "x": 450,
        "y": 120,
        "intent": "Click the search box to type the destination."
      }
    }
  ]
}
```

### 3. Ekzekuto veprimet e marra

Aplikacioni yt duhet të analizojë koordinatat e përgjigjes, t'i shkallëzojë ato nga koordinatat e normalizuara 1000x1000 dhe të ekzekutojë veprimin:

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
        print(f"  -> Executing: {fname} (Intent: {args.get('intent', 'N/A')})")

        try:
            if fname == "open_app":
                pass # Handled / already open
            elif fname in ("click", "double_click", "triple_click", "middle_click", "right_click", "move", "long_press"):
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)

                if fname == "click":
                    page.mouse.click(actual_x, actual_y)
                elif fname == "double_click":
                    page.mouse.dblclick(actual_x, actual_y)
                elif fname == "right_click":
                    page.mouse.click(actual_x, actual_y, button="right")
                elif fname == "middle_click":
                    page.mouse.click(actual_x, actual_y, button="middle")
                elif fname == "move":
                    page.mouse.move(actual_x, actual_y)
            elif fname == "type":
                actual_x = denormalize_x(args["x"], screen_width) if "x" in args else None
                actual_y = denormalize_y(args["y"], screen_height) if "y" in args else None
                text = args["text"]
                press_enter = args.get("press_enter", False)

                if actual_x is not None and actual_y is not None:
                    page.mouse.click(actual_x, actual_y)
                # Clear field first
                page.keyboard.press("Meta+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(text)
                if press_enter:
                    page.keyboard.press("Enter")
            elif fname == "navigate":
                page.goto(args["url"])
            elif fname == "go_back":
                page.go_back()
            elif fname == "go_forward":
                page.go_forward()
            elif fname == "wait":
                time.sleep(args.get("seconds", 1))
            else:
                print(f"Warning: Custom or unhandled function {fname}")

            page.wait_for_load_state(timeout=5000)
            time.sleep(1)

        except Exception as e:
            print(f"Error executing {fname}: {e}")
            action_result = {"error": str(e)}

        results.append((fname, function_call.id, action_result))

    return results
```

### JavaScript

```
function denormalizeX(x, screenWidth) {
    // Convert normalized x coordinate (0-1000) to actual pixel coordinate.
    return Math.floor((x / 1000) * screenWidth);
}

function denormalizeY(y, screenHeight) {
    // Convert normalized y coordinate (0-1000) to actual pixel coordinate.
    return Math.floor((y / 1000) * screenHeight);
}

async function executeFunctionCalls(interaction, page, screenWidth, screenHeight) {
    const results = [];
    const functionCalls = interaction.steps.filter(step => step.type === "function_call");

    for (const functionCall of functionCalls) {
        const actionResult = {};
        const fname = functionCall.name;
        const args = functionCall.arguments;
        console.log(`  -> Executing: ${fname} (Intent: ${args.intent || 'N/A'})`);

        try {
            if (fname === "open_app") {
                // Handled / already open
            } else if (["click", "double_click", "triple_click", "middle_click", "right_click", "move", "long_press"].includes(fname)) {
                const actualX = denormalizeX(args.x, screenWidth);
                const actualY = denormalizeY(args.y, screenHeight);

                if (fname === "click") {
                    await page.mouse.click(actualX, actualY);
                } else if (fname === "double_click") {
                    await page.mouse.dblclick(actualX, actualY);
                } else if (fname === "right_click") {
                    await page.mouse.click(actualX, actualY, { button: "right" });
                } else if (fname === "middle_click") {
                    await page.mouse.click(actualX, actualY, { button: "middle" });
                } else if (fname === "move") {
                    await page.mouse.move(actualX, actualY);
                }
            } else if (fname === "type") {
                const actualX = args.x !== undefined ? denormalizeX(args.x, screenWidth) : null;
                const actualY = args.y !== undefined ? denormalizeY(args.y, screenHeight) : null;
                const text = args.text;
                const pressEnter = args.press_enter || false;

                if (actualX !== null && actualY !== null) {
                    await page.mouse.click(actualX, actualY);
                }
                // Clear field first
                await page.keyboard.press("Meta+A");
                await page.keyboard.press("Backspace");
                await page.keyboard.type(text);
                if (pressEnter) {
                    await page.keyboard.press("Enter");
                }
            } else if (fname === "navigate") {
                await page.goto(args.url);
            } else if (fname === "go_back") {
                await page.goBack();
            } else if (fname === "go_forward") {
                await page.goForward();
            } else if (fname === "wait") {
                await new Promise(resolve => setTimeout(resolve, (args.seconds || 1) * 1000));
            } else {
                console.log(`Warning: Custom or unhandled function ${fname}`);
            }

            await page.waitForLoadState('load', { timeout: 5000 }).catch(() => {});
            await new Promise(resolve => setTimeout(resolve, 1000));
        } catch (e) {
            console.log(`Error executing ${fname}: ${e}`);
            actionResult.error = e.message;
        }

        results.push([fname, functionCall.id, actionResult]);
    }

    return results;
}
```

### Java

```
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.Step;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class ActionExecutor {
  int denormalizeX(int x, int screenWidth) {
    return (int) (x / 1000.0 * screenWidth);
  }

  int denormalizeY(int y, int screenHeight) {
    return (int) (y / 1000.0 * screenHeight);
  }

  List<Map<String, Object>> executeFunctionCalls(
      Interaction interaction, int screenWidth, int screenHeight) {
    List<Map<String, Object>> results = new ArrayList<>();

    for (Step step : interaction.steps().orElse(Collections.emptyList())) {
      if (step instanceof FunctionCallStep) {
        FunctionCallStep functionCall = (FunctionCallStep) step;
        String fname = functionCall.name().orElse("");
        Map<String, Object> args = functionCall.arguments().orElse(Collections.emptyMap());
        Map<String, Object> actionResult = new HashMap<>();

        System.out.println(
            "  -> Executing: " + fname + " (Intent: " + args.getOrDefault("intent", "N/A") + ")");

        try {
          if (fname.equals("click")) {
            int actualX = denormalizeX(((Number) args.get("x")).intValue(), screenWidth);
            int actualY = denormalizeY(((Number) args.get("y")).intValue(), screenHeight);
            // Perform mouse click at (actualX, actualY) using your browser automation library
          } else if (fname.equals("type")) {
            String text = (String) args.get("text");
            // Type text into active element using your browser automation library
          } else if (fname.equals("navigate")) {
            String url = (String) args.get("url");
            // Navigate browser to url
          }
        } catch (Exception e) {
          actionResult.put("error", e.getMessage());
        }

        Map<String, Object> entry = new HashMap<>();
        entry.put("name", fname);
        entry.put("callId", functionCall.id().orElse(""));
        entry.put("result", actionResult);
        results.add(entry);
      }
    }
    return results;
  }
}
```

### Go

```
package main

import (
    "fmt"

    "google.golang.org/genai/interactions/models/interactions"
)

func denormalizeX(x, screenWidth int) int {
    return int(float64(x) / 1000.0 * float64(screenWidth))
}

func denormalizeY(y, screenHeight int) int {
    return int(float64(y) / 1000.0 * float64(screenHeight))
}

func executeFunctionCalls(interaction *interactions.Interaction, screenWidth, screenHeight int) []map[string]any {
    var results []map[string]any

    for _, step := range interaction.Steps {
        if functionCall := step.FunctionCallStep; functionCall != nil {
            fname := functionCall.Name
            args := functionCall.Arguments
            actionResult := map[string]any{}

            intent := args["intent"]
            if intent == nil {
                intent = "N/A"
            }
            fmt.Printf("  -> Executing: %s (Intent: %v)\n", fname, intent)

            switch fname {
            case "click":
                xVal, _ := args["x"].(float64)
                yVal, _ := args["y"].(float64)
                actualX := denormalizeX(int(xVal), screenWidth)
                actualY := denormalizeY(int(yVal), screenHeight)
                _ = actualX
                _ = actualY
                // Perform mouse click at (actualX, actualY) using your browser automation library
            case "type":
                text, _ := args["text"].(string)
                _ = text
                // Type text into active element using your browser automation library
            case "navigate":
                url, _ := args["url"].(string)
                _ = url
                // Navigate browser to url
            }

            results = append(results, map[string]any{
                "name":   fname,
                "callId": functionCall.ID,
                "result": actionResult,
            })
        }
    }
    return results
}

func main() {
    // Example helper usage with an Interaction response
}
```

### 4. Regjistro gjendjen e re të mjedisit

Pas ekzekutimit të veprimeve, dërgo përsëri te modeli rezultatin e ekzekutimit të funksionit që ai të mund t'i përdorë këto informacione për të gjeneruar veprimin e radhës. Nëse janë ekzekutuar disa veprime (thirrje paralele), duhet të dërgosh një `function_result` për secilin prej tyre në radhën vijuese të përdoruesit.

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

### JavaScript

```
async function getFunctionResponses(page, results) {
    const screenshotBuffer = await page.screenshot({ type: 'png' });
    const screenshotBase64 = screenshotBuffer.toString('base64');
    const currentUrl = page.url();
    const functionResponses = [];

    for (const [name, callId, result] of results) {
        functionResponses.push({
            type: "function_result",
            name: name,
            call_id: callId,
            result: [
                {
                    type: "text",
                    text: JSON.stringify({ url: currentUrl, ...result })
                },
                {
                    type: "image",
                    data: screenshotBase64,
                    mime_type: "image/png"
                }
            ]
        });
    }
    return functionResponses;
}
```

### Java

```
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;
import java.util.Map;

class StateCapturer {
  List<Step> getFunctionResponses(
      byte[] screenshotBytes, String currentUrl, List<Map<String, Object>> results) {
    List<Step> functionResponses = new ArrayList<>();
    String base64Screenshot = Base64.getEncoder().encodeToString(screenshotBytes);

    for (Map<String, Object> entry : results) {
      String name = (String) entry.get("name");
      String callId = (String) entry.get("callId");
      String jsonResult = String.format("{\"url\": \"%s\"}", currentUrl);

      FunctionResultStep responseStep =
          FunctionResultStep.builder()
              .name(name)
              .callId(callId)
              .result(
                  FunctionResultStepResultUnion.of(
                      Arrays.asList(
                          TextContent.builder().text(jsonResult).build(),
                          ImageContent.builder()
                              .data(base64Screenshot)
                              .mimeType(ImageContentMimeType.IMAGE_PNG)
                              .build())))
              .build();
      functionResponses.add(responseStep);
    }
    return functionResponses;
  }
}
```

### Go

```
package main

import (
    "encoding/base64"
    "fmt"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
)

func getFunctionResponses(screenshotBytes []byte, currentURL string, results []map[string]any) []interactions.Step {
    var functionResponses []interactions.Step
    base64Screenshot := base64.StdEncoding.EncodeToString(screenshotBytes)

    for _, entry := range results {
        name, _ := entry["name"].(string)
        callID, _ := entry["callId"].(string)
        jsonResult := fmt.Sprintf(`{"url": "%s"}`, currentURL)

        responseStep := interactions.NewStep(interactions.FunctionResultStep{
            Name:   genai.Ptr(name),
            CallID: callID,
            Result: interactions.NewFunctionResultStepResultUnion([]interactions.FunctionResultSubcontent{
                interactions.NewFunctionResultSubcontent(interactions.TextContent{
                    Text: jsonResult,
                }),
                interactions.NewFunctionResultSubcontent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Screenshot),
                    MimeType: interactions.ImageContentMimeType("image/png").ToPointer(),
                }),
            }),
        })
        functionResponses = append(functionResponses, responseStep)
    }
    return functionResponses
}

func main() {
    // Example helper usage to build FunctionResultStep responses
}
```

Pasi të kesh përcaktuar se si të kapësh dhe formatosh gjendjen e mjedisit, mund t'i kombinosh të gjithë këta hapa në një cikël ekzekutimi të vazhdueshëm.

## Krijo një përsëritje të agjentit

Për të aktivizuar ndërveprimet me shumë hapa, kombino katër hapat nga seksioni [Si të zbatosh "Përdorimin e kompjuterit"](#implement-computer-use) në një lak të vetëm.
Ky cikël vazhdon të kërkojë veprime dhe t'i dërgojë rezultatet përsëri te modeli
derisa detyra të përfundojë.

Mos harro që të menaxhosh saktë historikun e bisedës duke shtuar përgjigjet e modelit dhe përgjigjet e funksionit te historiku në çdo hap.

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
        model='gemini-3.8-flash',
        input=[
            {"type": "text", "text": USER_PROMPT},
            {"type": "image", "data": base64.b64encode(initial_screenshot).decode("utf-8"), "mime_type": "image/png"}
        ],
        tools=[{
            "type": "computer_use",
            "environment": "browser",
            "enable_prompt_injection_detection": True
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
            model='gemini-3.8-flash',
            previous_interaction_id=interaction.id,
            input=function_responses,
            tools=[{
                "type": "computer_use",
                "environment": "browser",
                "enable_prompt_injection_detection": True
            }]
        )

finally:
    # Cleanup
    print("\nClosing browser...")
    browser.close()
    playwright.stop()
```

### JavaScript

```
import { chromium } from 'playwright';
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

// Constants for screen dimensions
const SCREEN_WIDTH = 1440;
const SCREEN_HEIGHT = 900;

console.log("Initializing browser...");
const browser = await chromium.launch({ headless: false });
const context = await browser.newContext({
    viewport: { width: SCREEN_WIDTH, height: SCREEN_HEIGHT }
});
const page = await context.newPage();

// Define helper functions. Copy/paste from steps 3 and 4:
// function denormalizeX(...)
// function denormalizeY(...)
// async function executeFunctionCalls(...)
// async function getFunctionResponses(...)

try {
    // Go to initial page
    await page.goto("https://ai.google.dev/gemini-api/docs");

    // Take initial screenshot
    const initialScreenshotBuffer = await page.screenshot({ type: 'png' });
    const initialScreenshotBase64 = initialScreenshotBuffer.toString('base64');
    const USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing.";
    console.log(`Goal: ${USER_PROMPT}`);

    // First interaction
    let interaction = await ai.interactions.create({
        model: 'gemini-3.8-flash',
        input: [
            { type: 'text', text: USER_PROMPT },
            { type: 'image', data: initialScreenshotBase64, mime_type: 'image/png' }
        ],
        tools: [{
            type: 'computer_use',
            environment: 'browser',
            enable_prompt_injection_detection: true
        }]
    });

    // Agent Loop
    const turnLimit = 5;
    for (let i = 0; i < turnLimit; i++) {
        console.log(`\n--- Turn ${i + 1} ---`);

        const hasFunctionCalls = interaction.steps.some(step => step.type === "function_call");
        if (!hasFunctionCalls) {
            const textResponses = [];
            for (const step of interaction.steps) {
                if (step.type === "model_output") {
                    for (const contentBlock of step.content || []) {
                        if (contentBlock.type === "text") {
                            textResponses.push(contentBlock.text);
                        }
                    }
                }
            }
            console.log("Agent finished:", textResponses.join(" "));
            break;
        }

        console.log("Executing actions...");
        const results = await executeFunctionCalls(interaction, page, SCREEN_WIDTH, SCREEN_HEIGHT);

        console.log("Capturing state...");
        const functionResponses = await getFunctionResponses(page, results);

        // Continue conversation with function responses
        interaction = await ai.interactions.create({
            model: 'gemini-3.8-flash',
            previous_interaction_id: interaction.id,
            input: functionResponses,
            tools: [{
                type: 'computer_use',
                environment: 'browser',
                enable_prompt_injection_detection: true
            }]
        });
    }
} finally {
    // Cleanup
    console.log("\nClosing browser...");
    await browser.close();
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collections;
import java.util.List;

Client client = new Client();

// Constants for screen dimensions
int screenWidth = 1440;
int screenHeight = 900;

// Capture initial screenshot from browser driver (e.g. Playwright)
byte[] initialScreenshot = new byte[0];
String base64Screenshot = Base64.getEncoder().encodeToString(initialScreenshot);
String userPrompt = "Go to ai.google.dev/gemini-api/docs and search for pricing.";
System.out.println("Goal: " + userPrompt);

ComputerUse computerUseTool =
    ComputerUse.builder()
        .environment(EnvironmentEnum.BROWSER)
        .enablePromptInjectionDetection(true)
        .build();

CreateModelInteraction initialParams =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder().text(userPrompt).build(),
                    ImageContent.builder()
                        .data(base64Screenshot)
                        .mimeType(ImageContentMimeType.IMAGE_PNG)
                        .build())))
        .tools(Arrays.asList(computerUseTool))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(initialParams)).interaction().get();

int turnLimit = 5;
for (int i = 0; i < turnLimit; i++) {
  System.out.println("\n--- Turn " + (i + 1) + " ---");

  boolean hasFunctionCalls =
      interaction.steps().orElse(Collections.emptyList()).stream()
          .anyMatch(step -> step instanceof FunctionCallStep);

  if (!hasFunctionCalls) {
    StringBuilder textResponse = new StringBuilder();
    for (Step step : interaction.steps().orElse(Collections.emptyList())) {
      if (step instanceof ModelOutputStep) {
        for (Content contentBlock :
            ((ModelOutputStep) step).content().orElse(Collections.emptyList())) {
          if (contentBlock instanceof TextContent) {
            textResponse.append(((TextContent) contentBlock).text().orElse("")).append(" ");
          }
        }
      }
    }
    System.out.println("Agent finished: " + textResponse.toString().trim());
    break;
  }

  System.out.println("Executing actions and capturing state...");
  // Execute function calls against browser driver and capture List<Step> functionResponses
  List<Step> functionResponses = new ArrayList<>();

  CreateModelInteraction nextParams =
      CreateModelInteraction.builder()
          .model("gemini-3.8-flash")
          .previousInteractionId(interaction.id().get())
          .input(InteractionsInput.ofStep(functionResponses))
          .tools(Arrays.asList(computerUseTool))
          .build();

  interaction =
      client.interactions.create(CreateInteractionRequestBody.of(nextParams)).interaction().get();
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "strings"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Constants for screen dimensions
    screenWidth := 1440
    screenHeight := 900
    _ = screenWidth
    _ = screenHeight

    // Capture initial screenshot from browser driver (e.g. Playwright)
    initialScreenshot := []byte{}
    base64Screenshot := base64.StdEncoding.EncodeToString(initialScreenshot)
    userPrompt := "Go to ai.google.dev/gemini-api/docs and search for pricing."
    fmt.Println("Goal:", userPrompt)

    computerUseTool := interactions.NewTool(interactions.ComputerUse{
        Environment:                    interactions.EnvironmentEnumBrowser.ToPointer(),
        EnablePromptInjectionDetection: genai.Ptr(true),
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{Text: userPrompt}),
                interactions.NewContent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Screenshot),
                    MimeType: interactions.ImageContentMimeType("image/png").ToPointer(),
                }),
            }),
            Tools: []interactions.Tool{computerUseTool},
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := res.Interaction

    turnLimit := 5
    for i := 0; i < turnLimit; i++ {
        fmt.Printf("\n--- Turn %d ---\n", i+1)

        hasFunctionCalls := false
        for _, step := range interaction.Steps {
            if step.FunctionCallStep != nil {
                hasFunctionCalls = true
                break
            }
        }

        if !hasFunctionCalls {
            var parts []string
            for _, step := range interaction.Steps {
                if outStep := step.ModelOutputStep; outStep != nil {
                    for _, contentBlock := range outStep.Content {
                        if textContent := contentBlock.TextContent; textContent != nil {
                            parts = append(parts, textContent.GetText())
                        }
                    }
                }
            }
            fmt.Println("Agent finished:", strings.TrimSpace(strings.Join(parts, " ")))
            break
        }

        fmt.Println("Executing actions and capturing state...")
        // Execute function calls against browser driver and capture []interactions.Step functionResponses
        var functionResponses []interactions.Step

        nextRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model:                 interactions.Model("gemini-3.8-flash"),
                PreviousInteractionID: interaction.ID,
                Input:                 interactions.NewInteractionsInput(functionResponses),
                Tools:                 []interactions.Tool{computerUseTool},
            }),
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = nextRes.Interaction
    }
}
```

## Mjediset e mbështetura

Modelet e Gemini 3.x mbështesin tri mjedise të specifikuara në `computer_use`
konfigurimet:

### Mjedisi i shfletuesit (`ENVIRONMENT_BROWSER`)

Veprimet e disponueshme nën veglën e shfletuesit:

| Emri i komandës | Përshkrimi | Argumentet (në thirrjen e funksionit) |
| --- | --- | --- |
| **kliko** | Klikimet majtas në koordinatë. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | Klikime të dyfishta në koordinatë. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | Klikime të trefishta te koordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | Klikimet në mes në koordinatë. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | Klikimet me butonin djathtas te koordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | Shtyp dhe mban shtypur butonin e miut te koordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | Lëshon butonin e miut te koordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **zhvendos** | Zhvendos kursorin në pozicionin e specifikuar. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **lloji** | Shkruan tekst. | `text`: str `press_enter`: bool (opsionale, parazgjedhja `false`) `intent`: str |
| **drag\_and\_drop** | Zvarrit një artikull nga koordinata e fillimit te koordinata e fundit. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **prit** | Vendos në pauzë ekzekutimin për një numër të specifikuar sekondash. | `seconds`: int (opsionale, parazgjedhja `1`) `intent`: str |
| **press\_key** | Shtyp tastin e specifikuar dhe e lëshon atë. | `key`: str `intent`: str |
| **key\_down** | Shtyp dhe mban shtypur tastin e specifikuar. | `key`: str `intent`: str |
| **key\_up** | Lëshon tastin e specifikuar. | `key`: str `intent`: str |
| **tast i shkurtoreve** | Shtyp kombinimin e specifikuar të tasteve. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | Kthen një pamje ekrani të ekranit aktual. | `intent`: str |
| **lëviz** | Lëviz lart, poshtë, majtas ose djathtas në një koordinatë me një distancë pikseli. | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, opsionale, parazgjedhja `300`) `intent`: str |
| **go\_back** | Navigon prapa te faqja e mëparshme e uebit në historikun e shfletuesit. | `intent`: str |
| **navigo** | Navigon drejtpërdrejt në një URL të specifikuar. | `url`: str `intent`: str |
| **go\_forward** | Navigon përpara te faqja tjetër e uebit në historikun e shfletuesit. | `intent`: str |

### Mjedisi për celular (`ENVIRONMENT_MOBILE`)

Veprimet e mjedisit të optimizuara për Android:

| Emri i komandës | Përshkrimi | Argumentet (në thirrjen e funksionit) |
| --- | --- | --- |
| **open\_app** | Hap një aplikacion me emrin e tij. | `app_name`: str `intent`: str |
| **kliko** | Klikimet majtas në koordinatë. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **list\_apps** | Liston aplikacionet e disponueshme në pajisje, duke kthyer emrat dhe emrat e paketave të tyre. | `intent`: str |
| **prit** | Vendos në pauzë ekzekutimin për një numër të specifikuar sekondash. | `seconds`: int (opsionale, parazgjedhja `1`) `intent`: str |
| **go\_back** | Navigon prapa tek ekrani ose faqja e mëparshme e uebit. | `intent`: str |
| **lloji** | Shkruan tekst. | `text`: str `press_enter`: bool (opsionale, parazgjedhja `false`) `intent`: str |
| **drag\_and\_drop** | Zvarrit një artikull nga koordinata e fillimit te koordinata e fundit. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **long\_press** | Kryen një shtypje të gjatë në një koordinatë në ekran. | `y`: int (0-999) `x`: int (0-999) `seconds`: int (Opsionale, parazgjedhja `2`) `intent`: str |
| **press\_key** | Shtyp tastin e specifikuar dhe e lëshon atë. | `key`: str `intent`: str |
| **take\_screenshot** | Kthen një pamje ekrani të ekranit aktual. | `intent`: str |

### Mjedisi i desktopit (`ENVIRONMENT_DESKTOP`)

Komandat e kursorit në nivelin e sistemit operativ të mjediseve të desktopit:

| Emri i komandës | Përshkrimi | Argumentet (në thirrjen e funksionit) |
| --- | --- | --- |
| **kliko** | Klikimet majtas në koordinatë. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **double\_click** | Klikime të dyfishta në koordinatë. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **triple\_click** | Klikime të trefishta te koordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **middle\_click** | Klikimet në mes në koordinatë. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **right\_click** | Klikimet me butonin djathtas te koordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_down** | Shtyp dhe mban shtypur butonin e miut te koordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **mouse\_up** | Lëshon butonin e miut te koordinata. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **zhvendos** | Zhvendos kursorin në pozicionin e specifikuar. | `y`: int (0-999) `x`: int (0-999) `intent`: str |
| **lloji** | Shkruan tekst. | `text`: str `press_enter`: bool (opsionale, parazgjedhja `false`) `intent`: str |
| **drag\_and\_drop** | Zvarrit një artikull nga koordinata e fillimit te koordinata e fundit. | `start_y`: int (0-999) `start_x`: int (0-999) `end_y`: int (0-999) `end_x`: int (0-999) `intent`: str |
| **prit** | Vendos në pauzë ekzekutimin për një numër të specifikuar sekondash. | `seconds`: int (opsionale, parazgjedhja `1`) `intent`: str |
| **press\_key** | Shtyp tastin e specifikuar dhe e lëshon atë. | `key`: str `intent`: str |
| **key\_down** | Shtyp dhe mban shtypur tastin e specifikuar. | `key`: str `intent`: str |
| **key\_up** | Lëshon tastin e specifikuar. | `key`: str `intent`: str |
| **tast i shkurtoreve** | Shtyp kombinimin e specifikuar të tasteve. | `keys`: `List[str]` `intent`: `str` |
| **take\_screenshot** | Kthen një pamje ekrani të ekranit aktual. | `intent`: str |
| **lëviz** | Lëviz lart, poshtë, majtas ose djathtas në një koordinatë me një distancë pikseli. | `y`: int (0-999) `x`: int (0-999) `direction`: str (`"up"`, `"down"`, `"left"`, `"right"`) `magnitude_in_pixels`: int (0-999, opsionale, parazgjedhja `300`) `intent`: str |

## Funksionet e personalizuara të përcaktuara nga përdoruesi

Mund ta zgjerosh funksionalitetin e modelit duke përfshirë funksione të personalizuara të përcaktuara nga përdoruesi. Për shembull, në skenarët e njeriut në cikël (HITL), mund të përjashtosh veprimet e paravendosura të paracaktuar dhe të regjistrosh veprime të personalizuara.

### Python

Përjashto veprimet standarde të paravendosura të shfletuesit (si p.sh. `click`) dhe regjistro një vegël të personalizuar `yield_to_user`:

```
from google import genai

client = genai.Client()

yield_to_user_tool = {
    "type": "function",
    "name": "yield_to_user",
    "description": "Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous.",
    "parameters": {
        "type": "object",
        "properties": {
            "reason": {
                "type": "string",
                "description": "The reason why the agent is yielding control to the human."
            }
        },
        "required": ["reason"]
    }
}

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Click the submit button. If you need a second factor authentication code, ask me.",
    tools=[
        {
            "type": "computer_use",
            "environment": "mobile",
            "excluded_predefined_functions": ["click"]
        },
        yield_to_user_tool
    ]
)
```

### JavaScript

Përjashto veprimet standarde të paravendosura të shfletuesit (si p.sh. `click`) dhe regjistro një vegël të personalizuar `yield_to_user`:

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const yieldToUserTool = {
    type: "function",
    name: "yield_to_user",
    description: "Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous.",
    parameters: {
        type: "object",
        properties: {
            reason: {
                type: "string",
                description: "The reason why the agent is yielding control to the human."
            }
        },
        required: ["reason"]
    }
};

const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Click the submit button. If you need a second factor authentication code, ask me.",
    tools: [
        {
            type: "computer_use",
            environment: "mobile",
            excluded_predefined_functions: ["click"]
        },
        yieldToUserTool
    ]
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> reasonProp = new HashMap<>();
reasonProp.put("type", "string");
reasonProp.put("description", "The reason why the agent is yielding control to the human.");

Map<String, Object> properties = new HashMap<>();
properties.put("reason", reasonProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Collections.singletonList("reason"));

Function yieldToUserTool =
    Function.builder()
        .name("yield_to_user")
        .description(
            "Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous.")
        .parameters(parameters)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(
            InteractionsInput.of(
                "Click the submit button. If you need a second factor authentication code, ask me."))
        .tools(
            Arrays.asList(
                ComputerUse.builder()
                    .environment(EnvironmentEnum.MOBILE)
                    .excludedPredefinedFunctions(Arrays.asList("click"))
                    .build(),
                yieldToUserTool))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    yieldToUserTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("yield_to_user"),
        Description: genai.Ptr("Yields control back to the user for assistance or verification when an automated action is unsafe or ambiguous."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "reason": map[string]any{
                    "type":        "string",
                    "description": "The reason why the agent is yielding control to the human.",
                },
            },
            "required": []string{"reason"},
        },
    })

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Click the submit button. If you need a second factor authentication code, ask me."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment:                 interactions.EnvironmentEnumMobile.ToPointer(),
                    ExcludedPredefinedFunctions: []string{"click"},
                }),
                yieldToUserTool,
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

## Menaxhimi i niveleve të arsyetimit

Për agjentët e përdorimit të kompjuterit, mund të konfigurosh nivele të ndryshme të të menduarit për të balancuar cilësinë e veprimit dhe shpejtësinë e ekzekutimit. Nivelet më të ulëta të të menduarit arrijnë përgjithësisht një ekuilibër të mirë për detyrat standarde të automatizimit.

## Siguria dhe mbrojtja

### Politikat e sigurisë po konfigurohen

Modelet e Gemini 3.x përfshijnë kategori të integruara të shërbimit të sigurisë që ndihmojnë për të përcaktuar nëse kërkohet konfirmimi i përdoruesit.

| Kategoria e politikës së sigurisë | Përshkrimi |
| --- | --- |
| `FINANCIAL_TRANSACTIONS` | Bllokon ose aktivizon konfirmimin për veprimet që përfshijnë pagesa, përfundimin e blerjes në shitje me pakicë ose mallra të rregulluara me ligj. |
| `SENSITIVE_DATA_MODIFICATION` | Mbron regjistrimet shëndetësore, financiare ose qeveritare nga modifikimi i paautorizuar. |
| `COMMUNICATION_TOOL` | Kufizon agjentin që të mos dërgojë në mënyrë autonome email-e, mesazhe bisede ose drafte. |
| `ACCOUNT_CREATION` | Kufizon agjentin që të mos regjistrojë në mënyrë autonome llogari të reja në uebsajte. |
| `DATA_MODIFICATION` | Rregullon modifikimet e përgjithshme të sistemit të skedarëve, ndarjen e të dhënave dhe fshirjen e hapësirës ruajtëse. |
| `USER_CONSENT_MANAGEMENT` | Kërkon marrjen e kontrollit nga përdoruesi për banderolat e pëlqimit për kukit dhe kërkesat për privatësinë. |
| `LEGAL_TERMS_AND_AGREEMENTS` | Parandalon që modeli të pranojë në mënyrë autonome "Kushtet e shërbimit" ose kontrata ligjërisht të detyrueshme. |

#### Zëvendësimet e sigurisë

Mund të anulosh politikat e zgjedhura duke kaluar anulimet:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Clean up the local folder by archiving old logs.",
    tools=[
        {
            "type": "computer_use",
            "environment": "desktop",
            "disabled_safety_policies": [
                "data_modification"
            ]
        }
    ]
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Clean up the local folder by archiving old logs.",
    tools: [
        {
            type: "computer_use",
            environment: "desktop",
            disabled_safety_policies: [
                "data_modification"
            ]
        }
    ]
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DisabledSafetyPolicy;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(InteractionsInput.of("Clean up the local folder by archiving old logs."))
        .tools(
            Arrays.asList(
                ComputerUse.builder()
                    .environment(EnvironmentEnum.DESKTOP)
                    .disabledSafetyPolicies(
                        Arrays.asList(DisabledSafetyPolicy.DATA_MODIFICATION))
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Clean up the local folder by archiving old logs."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment: interactions.EnvironmentEnumDesktop.ToPointer(),
                    DisabledSafetyPolicies: []interactions.DisabledSafetyPolicy{
                        interactions.DisabledSafetyPolicyDataModification,
                    },
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### Zbulimi i injektimit të kërkesës

Përdorimi në kompjuter për Gemini 3.5 Flash-Lite ose më vonë mbështet një mekanizëm të përparuar sigurie për të zbuluar sulmet e injektimit të kërkesave. Kur aktivizohet, kjo veçori kontrollon nëse një pamje ekrani e përfshirë përmban udhëzime të fshehura armiqësore (p.sh. "Shpërfill komandat e mëparshme") dhe bllokon ekzekutimin kur zbulohen.

Zbulimi i injektimit të kërkesës është një veçori me zgjedhje. Parazgjedhja është `false`.

Shembujt e mëposhtëm demonstrojnë se si të aktivizosh zbulimin e injektimit të kërkesave në konfigurimin e veglës së "Përdorimit të kompjuterit":

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Search for flight deals and summarize top results.",
    tools=[
        {
            "type": "computer_use",
            "environment": "desktop",
            "enable_prompt_injection_detection": True,
        }
    ],
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Search for flight deals and summarize top results.",
    tools: [
        {
            type: "computer_use",
            environment: "desktop",
            enablePromptInjectionDetection: true,
        }
    ]
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(InteractionsInput.of("Search for flight deals and summarize top results."))
        .tools(
            Arrays.asList(
                ComputerUse.builder()
                    .environment(EnvironmentEnum.DESKTOP)
                    .enablePromptInjectionDetection(true)
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Search for flight deals and summarize top results."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment:                    interactions.EnvironmentEnumDesktop.ToPointer(),
                    EnablePromptInjectionDetection: genai.Ptr(true),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### cURL

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions?key=${GEMINI_API_KEY}" \
-H 'Content-Type: application/json' \
-d '{
  "model": "gemini-3.8-flash",
  "input": "Search for flight deals and summarize top results.",
  "tools": [
    {
      "type": "computer_use",
      "environment": "desktop",
      "enable_prompt_injection_detection": true
    }
  ]
}'
```

### Prano vendimin për sigurinë

Përgjigjja mund të përfshijë një parametër `safety_decision` në argumentet e thirrjes së funksionit:

```
{
  "steps": [
    {
      "type": "function_call",
      "name": "click",
      "arguments": {
        "x": 60,
        "y": 100,
        "safety_decision": {
          "explanation": "Must check check-box",
          "decision": "require_confirmation"
        }
      }
    }
  ]
}
```

Nëse `safety_decision` është `require_confirmation`, kërkoji përdoruesit fundor. Nëse përdoruesi e konfirmon, cakto `safety_acknowledgement` në `function_result`.

### Python

```
def get_safety_confirmation(safety_decision):
    # Prompt user for confirmation
    print(f"Safety confirmation required: {safety_decision.get('explanation', '')}")
    return "CONTINUE" # Or TERMINATE

# Inside execute_function_calls, check for safety_decision:
if 'safety_decision' in function_call.arguments:
    decision = get_safety_confirmation(function_call.arguments['safety_decision'])
    if decision == "TERMINATE":
        break
    # Include safety_acknowledgement inside the action result
    action_result["safety_acknowledgement"] = True
```

### Praktikat më të mira të sigurisë

Përdorimi i kompjuterit paraqet rreziqe unike për sigurinë dhe funksionimin, pasi një model që vepron në emër të një përdoruesi mund të hasë përmbajtje të pabesueshme në ekrane ose mund të bëjë gabime në ekzekutimin e veprimeve. Zbato praktikat më të mira të mëposhtme për të mbrojtur të dhënat dhe sistemet e përdoruesve:

1. **Me ndërveprim njerëzor (HITL):**
   - **Zbato konfirmimin e përdoruesit:** Kur përgjigjja e sigurisë tregon
     `require_confirmation`, kërkoji përdoruesit miratimin.
   - **Jep udhëzime të personalizuara për sigurinë:** Zbato një udhëzim të personalizuar të sistemit për të përcaktuar dhe zbatuar kufijtë e tu të sigurisë. Për shembull:

     ### Python

     ```
     from google import genai

     client = genai.Client()

     system_instruction = """
     ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

     This is your first and most important check. If the next required action falls
     into any of the following categories, you MUST stop immediately, and seek the
     user's explicit permission.

     **Procedure for Seeking Confirmation:**
     * **For Consequential Actions:** Perform all preparatory steps (e.g., navigating,
       filling out forms, typing a message). You will ask for confirmation **AFTER**
       all necessary information is entered on the screen, but **BEFORE** you perform
       the final, irreversible action (e.g., before clicking "Send", "Submit",
       "Confirm Purchase", "Share").
     * **For Prohibited Actions:** If the action is strictly forbidden (e.g., accepting
       legal terms, solving a CAPTCHA), you must first inform the user about the
       required action and ask for their confirmation to proceed.

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
     """

     interaction = client.interactions.create(
         model="gemini-3.8-flash",
         system_instruction=system_instruction,
         input="Prepare a draft but do not send.",
         tools=[{
             "type": "computer_use",
             "environment": "browser"
         }]
     )
     ```

     ### JavaScript

     ```
     import { GoogleGenAI } from '@google/genai';

     const ai = new GoogleGenAI();

     const systemInstruction = `
     ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

     This is your first and most important check. If the next required action falls
     into any of the following categories, you MUST stop immediately, and seek the
     user's explicit permission.

     **Procedure for Seeking Confirmation:**
     * **For Consequential Actions:** Perform all preparatory steps (e.g., navigating,
       filling out forms, typing a message). You will ask for confirmation **AFTER**
       all necessary information is entered on the screen, but **BEFORE** you perform
       the final, irreversible action (e.g., before clicking "Send", "Submit",
       "Confirm Purchase", "Share").
     * **For Prohibited Actions:** If the action is strictly forbidden (e.g., accepting
       legal terms, solving a CAPTCHA), you must first inform the user about the
       required action and ask for their confirmation to proceed.

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

     If an action does **NOT** fall under the conditions for \`USER_CONFIRMATION\`,
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
     `;

     const interaction = await ai.interactions.create({
         model: "gemini-3.8-flash",
         system_instruction: systemInstruction,
         input: "Prepare a draft but do not send.",
         tools: [{
             type: "computer_use",
             environment: "browser"
         }]
     });
     ```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.ComputerUse;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.EnvironmentEnum;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

String systemInstruction =
    "## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**\n\n"
        + "This is your first and most important check. If the next required action falls "
        + "into any of the following categories, you MUST stop immediately, and seek the "
        + "user's explicit permission.\n\n"
        + "## **RULE 2: Default Behavior (ACTUATE)**\n\n"
        + "If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`, "
        + "your default behavior is to **Actuate**.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .systemInstruction(systemInstruction)
        .input(InteractionsInput.of("Prepare a draft but do not send."))
        .tools(
            Arrays.asList(
                ComputerUse.builder().environment(EnvironmentEnum.BROWSER).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    systemInstruction := "## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**\n\n" +
        "This is your first and most important check. If the next required action falls " +
        "into any of the following categories, you MUST stop immediately, and seek the " +
        "user's explicit permission.\n\n" +
        "## **RULE 2: Default Behavior (ACTUATE)**\n\n" +
        "If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`, " +
        "your default behavior is to **Actuate**."

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:             interactions.Model("gemini-3.8-flash"),
            SystemInstruction: genai.Ptr(systemInstruction),
            Input:             interactions.NewInteractionsInput("Prepare a draft but do not send."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.ComputerUse{
                    Environment: interactions.EnvironmentEnumBrowser.ToPointer(),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

1. **Mjedisi i ekzekutimit të sigurt:** Ekzekuto agjentin tënd në një mjedis të sigurt dhe të kufizuar
   për të kufizuar ndikimin e tij të mundshëm. Kjo mund të jetë një makinë virtuale e izoluar (VM), një kontejner (p.sh. Docker) ose një profil i dedikuar shfletuesi me leje të kufizuara. Shiko
   [zbatimin referues të GitHub](https://github.com/google/computer-use-preview/)
   për udhëzimet e konfigurimit të mjedisit të provës duke përdorur Docker.
2. **Pastrimi i hyrjes:** Pastro të gjithë tekstin e gjeneruar nga përdoruesi në kërkesa për të
   zbutur rrezikun e udhëzimeve të paqëllimshme ose injektimit të kërkesave. Kjo është një shtresë e dobishme sigurie, por nuk është një zëvendësim për një mjedis të sigurt ekzekutimi.
3. **Mbrojtjet për përmbajtjet:** Përdor mbrojtjet dhe API-të e sigurisë së përmbajtjeve për të vlerësuar hyrjet e përdoruesve, hyrjet dhe daljet e veglave, si dhe përgjigjet e agjentit për përshtatshmërinë, injektimin e kërkesave dhe zbulimin e shmangies së kufizimeve.
4. **Listat e lejimeve dhe listat e bllokimeve:** Zbato mekanizmat e filtrimit për të kontrolluar se ku mund të navigojë modeli dhe çfarë mund të bëjë ai. Një listë bllokimesh e uebsajteve të ndaluara është një pikë e mirë fillimi, ndërsa një listë lejimesh më kufizuese është edhe më e sigurt.
5. **Vëzhgueshmëria dhe regjistrimi:** Mbaj regjistra të detajuar për korrigjimin, auditimin dhe reagimin ndaj incidenteve. Klienti yt duhet të regjistrojë kërkesat, pamjet e ekranit, veprimet e sugjeruara nga modeli (`function_call`), përgjigjet e sigurisë dhe të gjitha veprimet e ekzekutuara në fund nga klienti.
6. **Menaxhimi i mjedisit:** Siguro që mjedisi i ndërfaqes grafike të përdoruesit është i qëndrueshëm.
   Dritaret kërcyese, njoftimet ose ndryshimet e papritura në strukturë mund ta ngatërrojnë modelin. Nis nga një gjendje e njohur dhe e pastër për çdo detyrë të re nëse është e mundur.

## Versionet e modelit

Mund ta përdorësh "Përdorimin e kompjuterit" me modelet e mëposhtme:

- [**Gemini 3.8 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=sq) (`gemini-3.8-flash`): Modeli i rekomanduar për përdorimin në kompjuter, i cili përmban ndërveprim me ndërfaqen e përdoruesit me saktësi të lartë dhe thirrje të besueshme të veglave.
- [**Gemini 3.5 Flash-Lite**](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=sq) (`gemini-3.5-flash-lite`): Një model me kosto efektive dhe me vonesë të ulët që mbështet përdorimin në kompjuter.
- [**Pamja paraprake e Gemini 3 Flash**](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=sq) (`gemini-3-flash-preview`): Pamja paraprake e modelit që mbështet përdorimin në kompjuter.

## Çfarë ka më pas

- Eksperimento me "Përdorimin e kompjuterit" në [mjedisin e demonstrimit të Browserbase](http://gemini.browserbase.com).
- Shiko [Zbatimin e referencës](https://github.com/google/computer-use-preview) për shembullin e kodit.
- Mëso rreth veglave të tjera të Gemini API:
  - [Thirrja e funksionit](https://ai.google.dev/gemini-api/docs/function-calling?hl=sq)
  - [Argumentimi me "Kërko në Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=sq)

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-09 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-09 UTC."],[],[]]
