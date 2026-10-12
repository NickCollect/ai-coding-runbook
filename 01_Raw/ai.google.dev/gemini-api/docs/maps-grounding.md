---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=hi
fetched_at: 2026-10-12T06:51:05.621826+00:00
title: "Google Maps \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u0917\u094d\u0930\u093e\u0909\u0902\u0921\u093f\u0902\u0917 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Google Maps की मदद से ग्राउंडिंग करना

Google Maps से सटीक जानकारी पाने की सुविधा, Gemini की जनरेटिव क्षमताओं को Google Maps के सटीक, तथ्यों पर आधारित, और अप-टू-डेट डेटा से कनेक्ट करती है. इस सुविधा की मदद से डेवलपर, अपने ऐप्लिकेशन में जगह की जानकारी का इस्तेमाल करने वाली सुविधा को आसानी से शामिल कर सकते हैं. जब किसी उपयोगकर्ता की क्वेरी में Maps के डेटा से जुड़ा कॉन्टेक्स्ट होता है, तो Gemini मॉडल, Google Maps का इस्तेमाल करता है. इससे वह उपयोगकर्ता को तथ्यों पर आधारित और अप-टू-डेट जवाब दे पाता है. ये जवाब, उपयोगकर्ता की बताई गई जगह या जगह की अनुमानित जानकारी के हिसाब से होते हैं.

- **सटीक जवाब, जो जगह के हिसाब से हों:** भौगोलिक रूप से खास क्वेरी के लिए, Google Maps के बड़े और मौजूदा डेटा का इस्तेमाल करें.
- **बेहतर तरीके से मनमुताबिक बनाना:** उपयोगकर्ता की ओर से दी गई जगहों के आधार पर, सुझाव और जानकारी को मनमुताबिक बनाना.

## अपनी प्रोफ़ाइल बनाना शुरू करें

इस उदाहरण में, Google Maps के साथ ग्राउंडिंग को अपने ऐप्लिकेशन में इंटिग्रेट करने का तरीका बताया गया है. इससे उपयोगकर्ता की क्वेरी के जवाब सटीक और जगह के हिसाब से दिए जा सकते हैं. इस प्रॉम्प्ट में, स्थानीय सुझावों के बारे में पूछा गया है. इसमें उपयोगकर्ता की जगह की जानकारी देने का विकल्प भी है. इससे Gemini मॉडल को Google Maps का डेटा इस्तेमाल करने की अनुमति मिलती है.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "What are the best Italian restaurants within a 15-minute walk from here?"))
        .tools(
            Arrays.asList(
                GoogleMaps.builder().latitude(34.050481).longitude(-118.248526).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Print the model's text response and annotations
if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
}
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("What are the best Italian restaurants within a 15-minute walk from here?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(34.050481),
                        Longitude: genai.Ptr(-118.248526),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Print the model's text response and annotations
    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Google Maps से जानकारी लेने की सुविधा कैसे काम करती है

Google Maps के साथ Grounding की सुविधा, Gemini API को Google Geo के साथ इंटिग्रेट करती है. इसके लिए, Maps API को Grounding सोर्स के तौर पर इस्तेमाल किया जाता है. जब किसी उपयोगकर्ता की क्वेरी में भौगोलिक कॉन्टेक्स्ट शामिल होता है, तब Gemini मॉडल, Google Maps से जानकारी लेने की सुविधा का इस्तेमाल कर सकता है. इसके बाद, मॉडल, दी गई जगह से जुड़े Google Maps के डेटा के आधार पर जवाब जनरेट कर सकता है.

आम तौर पर, इस प्रोसेस में ये काम शामिल होते हैं:

1. **उपयोगकर्ता की क्वेरी:** कोई उपयोगकर्ता आपके ऐप्लिकेशन पर क्वेरी सबमिट करता है.इसमें भौगोलिक जानकारी शामिल हो सकती है. उदाहरण के लिए, "मेरे आस-पास की कॉफ़ी शॉप", "सैन फ़्रांसिस्को के म्यूज़ियम".
2. **टूल का इस्तेमाल करना:** Gemini मॉडल, भौगोलिक जानकारी से जुड़े इंटेंट को पहचानकर, Grounding with Google Maps टूल का इस्तेमाल करता है. इस टूल को उपयोगकर्ता के `latitude` और `longitude` के साथ भी इस्तेमाल किया जा सकता है. यह टूल, टेक्स्ट के आधार पर खोज करने वाला टूल है. यह Maps पर खोज करने की सुविधा की तरह ही काम करता है. इसमें स्थानीय क्वेरी ("मेरे आस-पास") के लिए निर्देशांकों का इस्तेमाल किया जाएगा. वहीं, खास या गैर-स्थानीय क्वेरी पर, जगह की जानकारी का कोई असर नहीं पड़ेगा.
3. **डेटा वापस पाना:** 'Google Maps के साथ ग्राउंडिंग' सेवा, Google Maps से काम की जानकारी (जैसे, जगहें, समीक्षाएं, फ़ोटो, पते, कारोबार के खुले होने का समय) के बारे में क्वेरी करती है.
4. **भरोसेमंद स्रोतों से जानकारी लेकर जवाब जनरेट करना:** Maps से मिले डेटा का इस्तेमाल, Gemini मॉडल के जवाब में जानकारी देने के लिए किया जाता है. इससे यह पक्का किया जाता है कि जवाब में दी गई जानकारी सही और काम की हो.
5. **जवाब और एनोटेशन:** मॉडल, Google Maps के सोर्स से लिंक करने वाले इनलाइन एनोटेशन के साथ टेक्स्ट वाला जवाब देता है. इससे डेवलपर, उद्धरण दिखा पाते हैं.

## Google Maps से जानकारी लेने की सुविधा का इस्तेमाल कब और क्यों करना चाहिए

Google Maps के साथ ग्राउंडिंग की सुविधा उन ऐप्लिकेशन के लिए सबसे सही है जिन्हें सटीक, अप-टू-डेट, और जगह के हिसाब से जानकारी चाहिए. यह लोगों को काम का और उनकी दिलचस्पी के हिसाब से कॉन्टेंट उपलब्ध कराता है. इससे लोगों को बेहतर अनुभव मिलता है. यह कॉन्टेंट, Google Maps के विशाल डेटाबेस से लिया जाता है. इस डेटाबेस में, दुनिया भर की 25 करोड़ से ज़्यादा जगहों की जानकारी मौजूद है.

Google Maps से जानकारी लेने की सुविधा का इस्तेमाल तब करना चाहिए, जब आपके ऐप्लिकेशन को:

- जगह के हिसाब से पूछे गए सवालों के पूरे और सटीक जवाब दें.
- बातचीत करके ट्रिप प्लान करने वाले टूल और लोकल गाइड तैयार करना.
- जगह की जानकारी और उपयोगकर्ता की प्राथमिकताओं के आधार पर, लोकप्रिय जगहों के सुझाव दो. जैसे, रेस्टोरेंट या दुकानें.
- सोशल मीडिया, खुदरा कारोबार या खाना डिलीवर करने वाली सेवाओं के लिए, जगह की जानकारी के हिसाब से अनुभव बनाएं.

Google Maps के साथ ग्राउंडिंग की सुविधा, उन मामलों में सबसे ज़्यादा काम आती है जहां आस-पास की जगह और मौजूदा तथ्यों से जुड़ा डेटा ज़रूरी होता है. जैसे, "मेरे आस-पास सबसे अच्छी कॉफ़ी शॉप" खोजना या दिशा-निर्देश पाना.

## उपयोग के उदाहरण

Google Maps से जानकारी लेने की सुविधा का इस्तेमाल, जगह की जानकारी के हिसाब से अलग-अलग तरह के कामों के लिए किया जा सकता है.

### जगह के हिसाब से पूछे गए सवालों के जवाब देना

किसी जगह के बारे में ज़्यादा जानकारी वाले सवाल पूछें. इससे आपको Google पर लोगों की समीक्षाओं और Maps के अन्य डेटा के आधार पर जवाब मिलेंगे.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Is there a cafe near the corner of 1st and Main that has outdoor seating?"))
        .tools(
            Arrays.asList(
                GoogleMaps.builder().latitude(34.050481).longitude(-118.248526).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
}
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Is there a cafe near the corner of 1st and Main that has outdoor seating?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(34.050481),
                        Longitude: genai.Ptr(-118.248526),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### जगह की जानकारी के आधार पर मनमुताबिक अनुभव देना

किसी उपयोगकर्ता की प्राथमिकताओं और किसी खास इलाके के हिसाब से सुझाव पाएं.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Which family-friendly restaurants near here have the best playground reviews?"))
        .tools(
            Arrays.asList(GoogleMaps.builder().latitude(30.2672).longitude(-97.7431).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
}
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

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Which family-friendly restaurants near here have the best playground reviews?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(30.2672),
                        Longitude: genai.Ptr(-97.7431),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.PlaceCitation != nil {
                                c := annotation.PlaceCitation
                                name := ""
                                if c.Name != nil {
                                    name = *c.Name
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  - %s: %s\n", name, url)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### यात्रा की योजना बनाने में मदद करना

एक से ज़्यादा दिनों की यात्रा के प्लान जनरेट करना. इनमें अलग-अलग जगहों के बारे में जानकारी और वहाँ जाने का रास्ता शामिल होता है. यह सुविधा, यात्रा से जुड़े ऐप्लिकेशन के लिए सबसे सही है.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

String prompt =
    "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .tools(
            Arrays.asList(GoogleMaps.builder().latitude(37.78193).longitude(-122.40476).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// ... code to process response
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

    prompt := "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput(prompt),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleMaps{
                        Latitude:  genai.Ptr(37.78193),
                        Longitude: genai.Ptr(-122.40476),
                    }),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    // ... code to process response
    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## सेवा के इस्तेमाल से जुड़ी ज़रूरी शर्तें

इस सेक्शन में, Google Maps के साथ Grounding की सुविधा इस्तेमाल करने की ज़रूरी शर्तों के बारे में बताया गया है.

### उपयोगकर्ता को Google Maps के सोर्स के इस्तेमाल के बारे में जानकारी देना

Google Maps से मिले हर भरोसेमंद जवाब के साथ, आपको `model_output` चरण के कॉन्टेंट ब्लॉक पर सोर्स के एनोटेशन मिलेंगे. ये एनोटेशन, हर जवाब के साथ दिखेंगे. यह मेटाडेटा दिखता है:

- सोर्स यूआरएल
- नाम

Google Maps से जानकारी लेने की सुविधा के ज़रिए मिले नतीजे दिखाते समय, आपको Google Maps के जुड़े हुए सोर्स के बारे में बताना होगा. साथ ही, अपने उपयोगकर्ताओं को यह जानकारी देनी होगी:

- Google Maps के सोर्स, जनरेट किए गए कॉन्टेंट के ठीक बाद दिखने चाहिए. साथ ही, सोर्स में मौजूद कॉन्टेंट, जनरेट किए गए कॉन्टेंट से मिलता-जुलता होना चाहिए. जनरेट किए गए इस कॉन्टेंट को, Google Maps के भरोसेमंद नतीजे भी कहा जाता है.
- Google Maps के सोर्स, उपयोगकर्ता के एक इंटरैक्शन में दिखने चाहिए.

### Google Maps में किसी जगह पर ले जाने वाले लिंक के साथ Google Maps के सोर्स दिखाना

हर सोर्स एनोटेशन के लिए, लिंक की झलक इन ज़रूरी शर्तों के मुताबिक जनरेट की जानी चाहिए:

- Google Maps के टेक्स्ट [एट्रिब्यूशन के दिशा-निर्देशों](#maps-attribution-guidelines) का पालन करते हुए, हर सोर्स को Google Maps के लिए एट्रिब्यूट करें.
- जवाब में दिए गए सोर्स का नाम दिखाएं.
- एनोटेशन में मौजूद `url` का इस्तेमाल करके, सोर्स से लिंक करें.

### Google Maps में टेक्स्ट एट्रिब्यूशन के लिए दिशा-निर्देश

Google Maps में टेक्स्ट के तौर पर सोर्स एट्रिब्यूट करते समय, इन दिशा-निर्देशों का पालन करें:

- Google Maps के टेक्स्ट में किसी भी तरह का बदलाव न करें:
  - Google Maps के कैपिटलाइज़ेशन में बदलाव न करें.
  - Google Maps को एक से ज़्यादा लाइनों में न लिखें.
  - Google Maps को किसी दूसरी भाषा में स्थानीयकृत न करें.
  - एचटीएमएल एट्रिब्यूट translate="no" का इस्तेमाल करके, ब्राउज़र को Google Maps का अनुवाद करने से रोकें.

Google Maps के लिए डेटा उपलब्ध कराने वाली कुछ कंपनियों और उनके लाइसेंस की शर्तों के बारे में ज़्यादा जानने के लिए, [Google Maps और Google Earth के कानूनी नोटिस](https://www.google.com/help/legalnotices_maps/?hl=hi) देखें.

## सबसे सही तरीके

- **उपयोगकर्ता की जगह की जानकारी दें:** उपयोगकर्ता को उसकी दिलचस्पी के हिसाब से सबसे सटीक जवाब देने के लिए, `google_maps` टूल कॉन्फ़िगरेशन में हमेशा `latitude` और `longitude` शामिल करें. ऐसा तब करें, जब आपको उपयोगकर्ता की जगह की जानकारी पता हो.
- **असली उपयोगकर्ताओं को जानकारी दें:** असली उपयोगकर्ताओं को साफ़ तौर पर बताएं कि उनकी क्वेरी के जवाब देने के लिए, Google Maps के डेटा का इस्तेमाल किया जा रहा है. खास तौर पर, तब जब टूल चालू हो.
- **ज़रूरत न होने पर टॉगल बंद करें:** Google Maps के साथ ग्राउंडिंग की सुविधा डिफ़ॉल्ट रूप से बंद होती है. इसे सिर्फ़ तब चालू करें (`"tools": [{"type": "google_maps"}]`), जब किसी क्वेरी में भौगोलिक संदर्भ साफ़ तौर पर दिया गया हो. इससे परफ़ॉर्मेंस और लागत को ऑप्टिमाइज़ किया जा सकता है.

## सीमाएं

- फ़िलहाल, Google Maps के साथ बातचीत करने की सुविधा सिर्फ़ अंग्रेज़ी में उपलब्ध है. इसमें प्रॉम्प्ट और जवाब, दोनों अंग्रेज़ी में ही मिलते हैं.
- ऐसा हो सकता है कि यह टूल सभी देशों/इलाकों में उपलब्ध न हो.
- जगह की सटीक जानकारी और Maps पर उपलब्ध डेटा के आधार पर, नतीजे अलग-अलग हो सकते हैं.
- **देश या इलाके के हिसाब से उपलब्धता:** Google Maps के साथ ग्राउंडिंग की सुविधा, दुनिया भर में उपलब्ध है.
- **डिफ़ॉल्ट स्थिति:** 'Google Maps से जानकारी लेने की सुविधा' टूल डिफ़ॉल्ट रूप से बंद होता है.
  आपको इसे अपने एपीआई अनुरोधों में साफ़ तौर पर चालू करना होगा.

## कीमत और दर की सीमाएं

Google Maps से जानकारी लेने की सुविधा की कीमत, मॉडल जनरेशन के हिसाब से अलग-अलग होती है:

- **Gemini 3 और नए मॉडल:** आपके प्रोजेक्ट के लिए, हर उस सर्च क्वेरी का शुल्क लिया जाता है जिसे मॉडल पूरा करता है. Gemini 3 और नए मॉडल के लिए, हर महीने 5,000 अनुरोध मुफ़्त में किए जा सकते हैं. इसके बाद, **हर 1,000 सर्च क्वेरी के लिए 14 डॉलर** का शुल्क लिया जाता है. एक खोज प्रॉम्प्ट (मॉडल को भेजा गया आपका एपीआई अनुरोध) के जवाब में, मॉडल ज़रूरी जानकारी पाने के लिए कई सर्च क्वेरी चला सकता है. इनमें से हर क्वेरी को, टूल के बिल किए जाने वाले इस्तेमाल के तौर पर गिना जाता है.
- **Gemini 2.5 और इससे पुराने मॉडल:** आपके प्रोजेक्ट के लिए, हर सर्च प्रॉम्प्ट के हिसाब से बिल भेजा जाता है. इसके लिए, 1,000 ग्राउंडेड प्रॉम्प्ट के लिए 25 डॉलर लिए जाते हैं. किसी अनुरोध के लिए बिलिंग सिर्फ़ तब की जाती है, जब प्रॉम्प्ट से Google Maps के कम से कम एक भरोसेमंद नतीजे मिलते हैं. भले ही, उस नतीजे को पाने के लिए मॉडल ने कितनी भी सर्च क्वेरी की हों.

Google Maps से जानकारी लेने की सुविधा के लिए तय किया गया कोटा, आम तौर पर Gemini मॉडल के लिए अनुरोध संख्या सीमित करने के मुताबिक होता है. शुल्क के बारे में ज़्यादा जानकारी के लिए, [Gemini API के शुल्क वाला पेज](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) देखें.

## इन मॉडल के साथ काम करता है

Google Maps से जानकारी लेने की सुविधा, इन मॉडल के साथ काम करती है:

| मॉडल | Google Maps से सटीक जानकारी पाने की सुविधा |
| --- | --- |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=hi) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=hi) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.1 Pro की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ |
| [Gemini 3 Flash की झलक](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=hi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=hi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=hi) | ✔️ |

## इस्तेमाल किए जा सकने वाले टूल कॉम्बिनेशन

ज़्यादा मुश्किल सवालों के जवाब पाने के लिए, Google Maps के साथ-साथ पहले से मौजूद अन्य टूल का इस्तेमाल किया जा सकता है. जैसे, [Google Search के साथ ग्राउंडिंग](https://ai.google.dev/gemini-api/docs/google-search?hl=hi). यह सुविधा Gemini 3.5 Flash-Lite और इसके बाद के मॉडल पर काम करती है.
Gemini 3 मॉडल, इन बिल्ट-इन टूल को कस्टम टूल (फ़ंक्शन कॉलिंग) के साथ इस्तेमाल करने की सुविधा भी देते हैं. [टूल कॉम्बिनेशन](https://ai.google.dev/gemini-api/docs/tool-combination?hl=hi) पेज पर जाकर ज़्यादा जानें.

## आगे क्या करना है

- [उपलब्ध अन्य टूल](https://ai.google.dev/gemini-api/docs/tools?hl=hi) के बारे में जानें.
- ज़िम्मेदारी से एआई का इस्तेमाल करने के सबसे सही तरीकों और Gemini API के सुरक्षा फ़िल्टर के बारे में ज़्यादा जानने के लिए, [सुरक्षा सेटिंग से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/safety-settings?hl=hi) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-09 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-09 (UTC) को अपडेट किया गया."],[],[]]
