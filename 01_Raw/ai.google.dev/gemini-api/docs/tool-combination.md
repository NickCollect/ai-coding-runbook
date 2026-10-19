---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi
fetched_at: 2026-10-19T05:38:00.703429+00:00
title: "\u092a\u0939\u0932\u0947 \u0938\u0947 \u092e\u094c\u091c\u0942\u0926 \u091f\u0942\u0932 \u0914\u0930 \u092b\u093c\u0902\u0915\u094d\u0936\u0928 \u0915\u0949\u0932\u093f\u0902\u0917 \u0915\u094b \u090f\u0915 \u0938\u093e\u0925 \u0907\u0938\u094d\u0924\u0947\u092e\u093e\u0932 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# पहले से मौजूद टूल और फ़ंक्शन कॉलिंग को एक साथ इस्तेमाल करना

Gemini में, [पहले से मौजूद टूल](https://ai.google.dev/gemini-api/docs/tools?hl=hi), जैसे कि `google_search`, और [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) (इसे *कस्टम टूल* भी कहा जाता है) को एक साथ इस्तेमाल किया जा सकता है. इसके लिए, टूल कॉल के कॉन्टेक्स्ट के इतिहास को सेव किया जाता है और उसे दिखाया जाता है. इसमें पहले से मौजूद और कस्टम टूल के कॉम्बिनेशन इस्तेमाल किए जा सकते हैं. इससे, एजेंट के तौर पर काम करने वाले जटिल वर्कफ़्लो बनाए जा सकते हैं. उदाहरण के लिए, मॉडल आपके कारोबार के खास नियमों को लागू करने से पहले, रीयल-टाइम में वेब डेटा का इस्तेमाल कर सकता है.

यहां एक उदाहरण दिया गया है, जिसमें `google_search` और कस्टम फ़ंक्शन `getWeather` की मदद से, बिल्ट-इन और कस्टम टूल के कॉम्बिनेशन को चालू किया गया है:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");

Function customFunc =
    Function.builder()
        .name("get_user_location")
        .description("Retrieves user current location.")
        .parameters(parameters)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What is the weather like where I am right now?"))
        .tools(Arrays.asList(customFunc, new GoogleSearch()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### ऐप पर जाएं

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

    customFunc := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_user_location"),
        Description: genai.Ptr("Retrieves user current location."),
        Parameters: map[string]any{
            "type": "object",
        },
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("What is the weather like where I am right now?"),
            Tools: []interactions.Tool{
                customFunc,
                interactions.NewTool(interactions.GoogleSearch{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.8-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## यह कैसे काम करता है

Gemini 3 मॉडल, *टूल के कॉन्टेक्स्ट को शेयर करने की सुविधा* का इस्तेमाल करते हैं. इससे, पहले से मौजूद और कस्टम टूल के कॉम्बिनेशन को चालू किया जा सकता है. टूल के कॉन्टेक्स्ट को शेयर करने की सुविधा की मदद से, पहले से मौजूद टूल के कॉन्टेक्स्ट को सुरक्षित रखा जा सकता है और उसे दिखाया जा सकता है. साथ ही, उसे एक ही इंटरैक्शन में कस्टम टूल के साथ शेयर किया जा सकता है.

### टूल कॉम्बिनेशन की सुविधा चालू करना

- [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#function-declarations) को उन बिल्ट-इन टूल के साथ शामिल करें जिनका इस्तेमाल आपको करना है. इससे कॉम्बिनेशन बिहेवियर ट्रिगर होगा.

### एपीआई से मिले जवाब में शामिल चरण

इंटरैक्शन के जवाब में, एपीआई पहले से मौजूद टूल कॉल और फ़ंक्शन (कस्टम टूल) कॉल के लिए अलग-अलग चरण दिखाता है:

- **पहले से मौजूद टूल के चरण**: एपीआई इन्हें अपने-आप मैनेज करता है. इससे, बातचीत के हर चरण में कॉन्टेक्स्ट बना रहता है.
- **फ़ंक्शन कॉल के चरण**: एपीआई, आपके कस्टम फ़ंक्शन के लिए `function_call` चरण दिखाता है. फ़ंक्शन को लागू करें और नतीजे वापस दें.

### जवाब में मिले चरणों में मौजूद ज़रूरी फ़ील्ड

जवाब में मिले चरणों में कुछ फ़ील्ड, टूल के संदर्भ को बनाए रखने और टूल के कॉम्बिनेशन को चालू करने के लिए ज़रूरी होते हैं:

- **`id`**: `function_call` और `function_response` चरण में मिला. यह एक यूनीक आइडेंटिफ़ायर होता है, जो कॉल को उसके रिस्पॉन्स से मैप करता है.
- **`signature`**: यह `thought` चरणों के साथ-साथ, Gemini 3 और इसके बाद के मॉडल के लिए, टूल कॉल (जैसे, `function_call`) और नतीजे (जैसे, `function_response`) वाले सभी चरणों में मिलता है. एन्क्रिप्ट किए गए इस कॉन्टेक्स्ट की मदद से, अलग-अलग इंटरैक्शन के दौरान **टूल के कॉन्टेक्स्ट को सर्कुलेट** किया जा सकता है.

**इन फ़ील्ड को मैनेज करना:**

- **स्टेटफ़ुल मोड (सुझाया गया)**: `previous_interaction_id` का इस्तेमाल करने पर, सर्वर `id` और `signature`, दोनों फ़ील्ड को अपने-आप मैनेज करता है.
- **स्टेटलेस मोड**: बातचीत के इतिहास को मैन्युअल तरीके से मैनेज करते समय, आपको यह पक्का करना होगा कि आपने बाद के अनुरोधों में, `id` और `signature`, दोनों फ़ील्ड को मॉडल में वापस पास किया हो. इससे, प्रामाणिकता की पुष्टि की जा सकेगी और कॉन्टेक्स्ट को बनाए रखा जा सकेगा. अगर आपने पूरे जवाब वाले ऑब्जेक्ट को इतिहास में वापस भेज दिया है, तो आधिकारिक एसडीके इसे अपने-आप मैनेज कर लेते हैं.

### टूल के हिसाब से डेटा

कुछ बिल्ट-इन टूल, उपयोगकर्ता को दिखने वाले डेटा आर्ग्युमेंट दिखाते हैं. ये आर्ग्युमेंट, टूल टाइप के हिसाब से अलग-अलग होते हैं.

| टूल | उपयोगकर्ता को दिखने वाले टूल कॉल आर्ग्युमेंट (अगर कोई है) | उपयोगकर्ता को दिखने वाला टूल का जवाब (अगर कोई है) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` ब्राउज़ किए जाने वाले यूआरएल | `status`: ब्राउज़ करने की स्थिति `retrieved_url`: ब्राउज़ किए गए यूआरएल |
| **file\_search** | कोई नहीं | कोई नहीं |

## टोकन और कीमत

ध्यान दें कि अनुरोधों में मौजूद, पहले से मौजूद टूल कॉल के हिस्सों को `prompt_token_count` में गिना जाता है. टूल के इस्तेमाल से जुड़े ये इंटरमीडिएट चरण अब आपको दिखते हैं और इनका डेटा आपको वापस मिल जाता है. इसलिए, ये बातचीत के इतिहास का हिस्सा होते हैं. यह सिर्फ़ *अनुरोधों* के लिए है, *जवाबों* के लिए नहीं.

Google Search टूल पर यह नियम लागू नहीं होता. Google Search, क्वेरी लेवल पर पहले से ही अपना प्राइसिंग मॉडल लागू करता है. इसलिए, टोकन के लिए दो बार शुल्क नहीं लिया जाता. ज़्यादा जानकारी के लिए, [कीमत](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) पेज देखें.

ज़्यादा जानकारी के लिए, [टोकन](https://ai.google.dev/gemini-api/docs/tokens?hl=hi) पेज पढ़ें.

## सीमाएं

- टूल के कॉन्टेक्स्ट को शेयर करने की सुविधा चालू होने पर, डिफ़ॉल्ट रूप से `validated` मोड चालू होता है. `auto` मोड काम नहीं करता.
- `google_search` जैसे पहले से मौजूद टूल, जगह और मौजूदा समय की जानकारी पर निर्भर करते हैं. इसलिए, अगर आपके `system_instruction` या `function_declaration.description` में जगह और समय की जानकारी अलग-अलग है, तो टूल कॉम्बिनेशन की सुविधा ठीक से काम नहीं करेगी.

## इन टूल के साथ काम करता है

सर्वर-साइड (पहले से मौजूद) टूल पर, टूल के कॉन्टेक्स्ट को सर्कुलेट करने की स्टैंडर्ड प्रोसेस लागू होती है.
कोड एक्ज़ीक्यूशन भी सर्वर-साइड टूल है. हालांकि, इसमें कॉन्टेक्स्ट सर्कुलेशन के लिए, पहले से मौजूद समाधान होता है. कंप्यूटर का इस्तेमाल और फ़ंक्शन कॉलिंग, क्लाइंट-साइड टूल हैं. इनमें कॉन्टेक्स्ट सर्कुलेशन के लिए पहले से मौजूद समाधान भी होते हैं.

| टूल | प्रोग्राम चलाने वाला पक्ष | कॉन्टेक्स्ट सर्कुलेशन सपोर्ट |
| --- | --- | --- |
| [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=hi) | सर्वर-साइड | समर्थित |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi) | सर्वर-साइड | समर्थित |
| [यूआरएल का कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi) | सर्वर-साइड | समर्थित |
| [फ़ाइल खोजना](https://ai.google.dev/gemini-api/docs/file-search?hl=hi) | सर्वर-साइड | समर्थित |
| [कोड एक्ज़ीक्यूशन](https://ai.google.dev/gemini-api/docs/code-execution?hl=hi) | सर्वर-साइड | सपोर्ट करता है (पहले से मौजूद है, `code_execution` और `code_execution_result` चरणों का इस्तेमाल करता है) |
| [कंप्यूटर का इस्तेमाल](https://ai.google.dev/gemini-api/docs/computer-use?hl=hi) | क्लाइंट-साइड | इस्तेमाल किया जा सकता है (पहले से मौजूद है, `function_call` और `function_response` चरणों का इस्तेमाल करता है) |
| [कस्टम फ़ंक्शन](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) | क्लाइंट-साइड | इस्तेमाल किया जा सकता है (पहले से मौजूद है, `function_call` और `function_response` चरणों का इस्तेमाल करता है) |

## आगे क्या करना है

- Gemini API में [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) के बारे में ज़्यादा जानें.
- इन टूल के साथ काम करने की सुविधा उपलब्ध है:
  - [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=hi)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi)
  - [यूआरएल का कॉन्टेक्स्ट](https://ai.google.dev/gemini-api/docs/url-context?hl=hi)
  - [फ़ाइल सर्च](https://ai.google.dev/gemini-api/docs/file-search?hl=hi)

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-13 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-13 (UTC) को अपडेट किया गया."],[],[]]
