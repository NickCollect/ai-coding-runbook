---
source_url: https://ai.google.dev/gemini-api/docs/transcribe?hl=hi
fetched_at: 2026-10-05T06:41:17.294711+00:00
title: "\u0911\u0921\u093f\u092f\u094b \u0915\u094b \u091f\u0947\u0915\u094d\u0938\u094d\u091f \u092e\u0947\u0902 \u092c\u0926\u0932\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# ऑडियो को टेक्स्ट में बदलना

Gemini API, ऑडियो फ़ाइलों में मौजूद बोली को Gemini 3.5 Transcribe मॉडल (`gemini-3.5-transcribe`) का इस्तेमाल करके टेक्स्ट में बदलता है. Gemini की ऑडियो समझने की क्षमताओं के आधार पर, यह सटीक ट्रांसक्रिप्शन उपलब्ध कराता है. इसमें भाषा की पहचान अपने-आप होती है, बोलने वाले की पहचान होती है, शब्द-लेवल के टाइमस्टैंप होते हैं, और कस्टम शब्दावली के बारे में सुझाव मिलते हैं. इसमें [स्मार्ट ट्रांसक्रिप्शन](#transcription-modes) मोड भी मिलता है. इसमें शब्दों को सही तरीके से व्यवस्थित करने और फ़ॉर्मैट करने की सुविधा होती है.

किसी ऑडियो फ़ाइल को टेक्स्ट में बदलने के लिए, ऑडियो अपलोड करें और उसे `gemini-3.5-transcribe` को भेजें:

### Python

```
from google import genai

client = genai.Client()

audio_file = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const audioFile = await client.files.upload({
  file: "path/to/sample.mp3",
  config: { mime_type: "audio/mp3" },
});

const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
});

console.log(interaction.output_text);
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
# First upload the file via the Files API, then pass its URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

## खास जानकारी देने वाला बटन

Gemini 3.5 Transcribe को, बोली को लिखाई में बदलने के टास्क के लिए ऑप्टिमाइज़ किया गया है. यह अलग-अलग लहज़ों, बैकग्राउंड के शोर, और कई भाषाओं में की गई बातचीत को समझ सकता है.

मुख्य सुविधाओं में ये शामिल हैं:

- **अपने-आप बोली पहचानने की सुविधा (एएसआर):** यह [85 से ज़्यादा स्थानीय भाषाओं](#supported-languages) का पता अपने-आप लगाती है. यह सुविधा, मैन्युअल कॉन्फ़िगरेशन के बिना, एक वाक्य और अलग-अलग वाक्यों के बीच कोड-स्विचिंग को मैनेज करती है.
- **कस्टम शब्दावली:** इसमें 1,000 वाक्यांशों को पास करके, डोमेन के हिसाब से शब्दों, छोटे नामों, और सही नामों को पहचानने की सुविधा को बेहतर बनाया जाता है.
- **स्पीकर डायराइज़ेशन:** यह सुविधा, एक से ज़्यादा लोगों की आवाज़ में अंतर करती है और बोले गए सेगमेंट को अलग-अलग लेबल असाइन करती है.
- **शब्द-लेवल के टाइमस्टैंप:** इससे पहचाने गए हर शब्द के शुरू और खत्म होने के समय के सटीक ऑफ़सेट जनरेट होते हैं.
- **स्मार्ट ट्रांसक्रिप्शन:** यह सुविधा, बोलने में होने वाली रुकावटों, फ़िलर शब्दों, और दोहराव को हटा देती है. साथ ही, टेक्स्ट को व्यवस्थित फ़ॉर्मैट में बदल देती है.
- **फ़ॉर्मैट करना और सामान्य बनाना:** इसमें कैपिटल लेटर का इस्तेमाल करना, विराम चिह्न लगाना, और टेक्स्ट को सामान्य बनाना शामिल है. जैसे, "2 करोड़ 60 लाख डॉलर" को "2.6 करोड़ डॉलर" में बदलना.

ऑडियो कॉन्टेंट के आधार पर तर्क करने या सवालों के जवाब देने के लिए, [ऑडियो समझने की सुविधा](https://ai.google.dev/gemini-api/docs/audio?hl=hi) का इस्तेमाल करें. टेक्स्ट-टू-स्पीच ऑडियो सिंथेसिस के लिए, [टेक्स्ट-टू-स्पीच](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi) का इस्तेमाल करें.

## भाषा की पहचान करने और सुझाव पाने की सुविधा

डिफ़ॉल्ट रूप से, मॉडल बोली जा रही भाषा का पता अपने-आप लगा लेता है. यह सुविधा, बोलने वालों के कोड-स्विच करने पर, भाषाओं के बीच डाइनैमिक तरीके से स्विच करती है.

अपने-आप पहचान होने की सुविधा का इस्तेमाल करने के लिए, `language_codes` को शामिल न करें या खाली सूची दें:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "language_codes": [],
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      language_codes: [],
    },
  },
});
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    LanguageCodes: []string{},
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "language_codes": []
      }
    }
  }'
```

अगर आपको पहले से ही भाषा के बारे में पता है, तो ट्रांसक्रिप्शन की सटीकता को बेहतर बनाने के लिए, `language_codes` में BCP-47 भाषा कोड डालें ([इस्तेमाल की जा सकने वाली भाषाएं](#supported-languages) देखें):

### Python

```
generation_config = {
    "transcription_config": {
        "language_codes": ["es-ES"],
    }
}
```

### JavaScript

```
const generationConfig = {
  transcription_config: {
    language_codes: ["es-ES"],
  },
};
```

### ऐप पर जाएं

```
package main

import (
    "google.golang.org/genai/interactions/models/interactions"
)

func main() {
    generationConfig := &interactions.GenerationConfig{
        TranscriptionConfig: &interactions.TranscriptionConfig{
            LanguageCodes: []string{"es-ES"},
        },
    }
    _ = generationConfig
}
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "language_codes": ["es-ES"]
    }
  }
}
```

## कस्टम शब्दावली

आपके पास स्पीच मॉडल को, सामान्य तौर पर इस्तेमाल न होने वाले शब्दों, तकनीकी शब्दों, ब्रैंड के नामों या व्यक्तिवाचक संज्ञाओं के बारे में बताने का विकल्प होता है. `custom_vocabulary` ऐरे में ज़्यादा से ज़्यादा 1,000 शब्द डालें. आम तौर पर, 100 शब्दों तक के लिए सबसे अच्छे नतीजे मिलते हैं:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"],
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      custom_vocabulary: ["Gemini", "Kubernetes", "BigQuery"],
    },
  },
});
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    CustomVocabulary: []string{"Gemini", "Kubernetes", "BigQuery"},
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "custom_vocabulary": ["Gemini", "Kubernetes", "BigQuery"]
      }
    }
  }'
```

## स्पीकर डायराइज़ेशन

स्पीकर डायराइज़ेशन की सुविधा, रिकॉर्डिंग में मौजूद अलग-अलग आवाज़ों की पहचान करती है. साथ ही, हर सेगमेंट को स्पीकर आइडेंटिफ़ायर के साथ टैग करती है. जैसे, `spk_1` या `spk_2`. ज़्यादा से ज़्यादा आठ स्पीकर इस्तेमाल किए जा सकते हैं. हालांकि, तीन या इससे ज़्यादा स्पीकर के लिए एट्रिब्यूशन की सुविधा, एक्सपेरिमेंट के तौर पर उपलब्ध है.

`mode` में `diarization_mode` को कॉन्फ़िगर करके, डायराइज़ेशन की सुविधा चालू करें:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": {
                "type": "verbatim",
                "diarization_mode": "speaker",
            },
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: {
        type: "verbatim",
        diarization_mode: "speaker",
      },
    },
  },
});
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.NewTranscriptionMode(interactions.VerbatimTranscriptionMode{
                        DiarizationMode: genai.Ptr("speaker"),
                    }))),
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": {
          "type": "verbatim",
          "diarization_mode": "speaker"
        }
      }
    }
  }'
```

## शब्दों के लेवल पर टाइमस्टैंप

शब्द-लेवल के टाइमस्टैंप से, ऑडियो स्ट्रीम में पहचाने गए हर शब्द के शुरू और खत्म होने के सटीक ऑफ़सेट मिलते हैं.

`mode` में जाकर `timestamp_granularities` को कॉन्फ़िगर करके, टाइमस्टैंप की सुविधा चालू करें:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": {
                "type": "verbatim",
                "timestamp_granularities": ["word"],
            },
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: {
        type: "verbatim",
        timestamp_granularities: ["word"],
      },
    },
  },
});
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.NewTranscriptionMode(interactions.VerbatimTranscriptionMode{
                        TimestampGranularities: []string{"word"},
                    }))),
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": {
          "type": "verbatim",
          "timestamp_granularities": ["word"]
        }
      }
    }
  }'
```

स्पीकर लेबल और शब्द के टाइमस्टैंप, दोनों पाने के लिए `mode` में `diarization_mode` और `timestamp_granularities` को एक साथ इस्तेमाल किया जा सकता है:

### Python

```
generation_config = {
    "transcription_config": {
        "mode": {
            "type": "verbatim",
            "diarization_mode": "speaker",
            "timestamp_granularities": ["word"],
        },
    }
}
```

### JavaScript

```
const generationConfig = {
  transcription_config: {
    mode: {
      type: "verbatim",
      diarization_mode: "speaker",
      timestamp_granularities: ["word"],
    },
  },
};
```

### ऐप पर जाएं

```
package main

import (
    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
)

func main() {
    generationConfig := &interactions.GenerationConfig{
        TranscriptionConfig: &interactions.TranscriptionConfig{
            Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.NewTranscriptionMode(interactions.VerbatimTranscriptionMode{
                DiarizationMode:        genai.Ptr("speaker"),
                TimestampGranularities: []string{"word"},
            }))),
        },
    }
    _ = generationConfig
}
```

### REST

```
{
  "generation_config": {
    "transcription_config": {
      "mode": {
        "type": "verbatim",
        "diarization_mode": "speaker",
        "timestamp_granularities": ["word"]
      }
    }
  }
}
```

## बोले जा रहे शब्दों को टेक्स्ट में बदलने के मोड

Gemini 3.5 Transcribe, `mode` पैरामीटर के ज़रिए ट्रांसक्रिप्शन के दो मोड सपोर्ट करता है:

- **`verbatim` (डिफ़ॉल्ट)**: इसमें बोले गए हर शब्द की सटीक ट्रांसक्रिप्ट मिलती है. इसमें फ़िलर शब्दों ("अम्", "अह", "जैसे", "आपको पता है"), दोहराव, ठहराव, और गलत शुरुआत को भी शामिल किया जाता है. इस मोड (`{"type": "verbatim", ...}`) में, टाइमस्टैंप और स्पीकर डायराइज़ेशन की सुविधा कॉन्फ़िगर की जाती है.
- **`smart` (स्मार्ट ट्रांसक्रिप्शन)**: यह सुविधा, ट्रांसक्रिप्ट को पढ़ने के लिए ऑप्टिमाइज़ करती है. इसके लिए, यह पोस्ट-प्रोसेसिंग की बेहतर तकनीक का इस्तेमाल करती है:
  - **बातचीत में रुकावट डालने वाले शब्दों को हटाना**: बातचीत में रुकावट डालने वाले शब्दों, हकलाने, और गलत शुरुआत को हटाता है.
  - **बोले गए शब्दों को तुरंत ठीक करना**: बोले गए शब्दों को तुरंत ठीक करता है. उदाहरण के लिए, *"चलो मंगलवार को मिलते हैं, नहीं नहीं, बुधवार को दो बजे"* को *"चलो बुधवार को दोपहर 2 बजे मिलते हैं"* में बदल देता है.
  - **स्ट्रक्चर्ड फ़ॉर्मैटिंग अपने-आप होना**: यह सुविधा, बोले गए शब्दों को पैराग्राफ़, नंबर वाली सूचियों, बुलेट पॉइंट, फ़ॉर्मैट की गई तारीखों, मुद्राओं, और संख्याओं में अपने-आप व्यवस्थित करती है.
  - **व्याकरण से जुड़ी अशुद्धियों को ठीक करना**: इसमें विराम चिह्न, वाक्य के पहले अक्षर को कैपिटल करना, और वाक्य के फ़्लो को ठीक करना शामिल है.

| ऑडियो कॉन्टेंट | `verbatim` आउटपुट | `smart` (स्मार्ट ट्रांसक्रिप्शन) आउटपुट |
| --- | --- | --- |
| "अरे, तो मीटिंग के लिए, मुझे लगता है कि हमें, अह, एलिस को न्योता देना चाहिए और, नहीं नहीं, बॉब और कैरल को न्योता देना चाहिए." | "मीटिंग के लिए, हमें एलिस को न्योता देना चाहिए. नहीं, हमें बॉब और कैरल को न्योता देना चाहिए." | "मीटिंग के लिए, हमें बॉब और कैरल को न्योता भेजना चाहिए." |
| "पहले आइटम की समीक्षा करो, दूसरे आइटम के लिए बजट तय करो, तीसरे आइटम के लिए समयसीमा तय करो, और रीकैप भेजो" | "first item review budget second item finalize timeline third item send recap" | "1. बजट की समीक्षा करें 2. टाइमलाइन को फ़ाइनल करें 3. रीकैप भेजें" |

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type,
        }
    ],
    generation_config={
        "transcription_config": {
            "mode": "smart",
        }
    },
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
  model: "gemini-3.5-transcribe",
  input: [
    {
      type: "audio",
      uri: audioFile.uri,
      mime_type: audioFile.mimeType,
    },
  ],
  generation_config: {
    transcription_config: {
      mode: "smart",
    },
  },
});
console.log(interaction.output_text);
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

    audioFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.5-transcribe"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.AudioContent{
                    URI:      genai.Ptr(audioFile.URI),
                    MimeType: interactions.AudioContentMimeType(audioFile.MIMEType).ToPointer(),
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                TranscriptionConfig: &interactions.TranscriptionConfig{
                    Mode: genai.Ptr(interactions.NewTranscriptionConfigMode(interactions.TranscriptionConfigModeEnumSmart)),
                },
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-transcribe",
    "input": [
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ],
    "generation_config": {
      "transcription_config": {
        "mode": "smart"
      }
    }
  }'
```

## ट्रांसक्रिप्शन के आउटपुट को पार्स किया जा रहा है

पूरी ट्रांसक्रिप्ट का टेक्स्ट, `interaction.output_text` में दिखाया जाता है.

`timestamp_granularities` या `diarization_mode` चालू होने पर, एपीआई इंटरैक्शन के कॉन्टेंट से जुड़े शब्द-लेवल के एनोटेशन की ज़्यादा जानकारी भी दिखाता है.

शब्दों के टाइमस्टैंप और स्पीकर के बोलने की बारी की जानकारी निकालने और उसे दोहराने का तरीका यहां बताया गया है:

### Python

```
def extract_word_annotations(interaction):
    words = []
    for step in getattr(interaction, "steps", []) or []:
        for content in getattr(step, "content", []) or []:
            for annotation in getattr(content, "annotations", []) or []:
                if getattr(annotation, "type", None) == "word_info":
                    words.append(annotation)
    return words

words = extract_word_annotations(interaction)

for w in words:
    speaker = f"[{w.speaker}] " if getattr(w, "speaker", None) else ""
    start = getattr(w, "start_offset", "")
    end = getattr(w, "end_offset", "")
    timing = f"({start} -> {end}) " if start and end else ""
    print(f"{speaker}{timing}{w.text}")
```

### JavaScript

```
function extractWordAnnotations(interaction) {
  const words = [];
  for (const step of interaction.steps ?? []) {
    for (const content of step.content ?? []) {
      for (const annotation of content.annotations ?? []) {
        if (annotation.type === "word_info") {
          words.push(annotation);
        }
      }
    }
  }
  return words;
}

const words = extractWordAnnotations(interaction);

for (const w of words) {
  const speaker = w.speaker ? `[${w.speaker}] ` : "";
  const timing = (w.start_offset && w.end_offset) ? `(${w.start_offset} -> ${w.end_offset}) ` : "";
  console.log(`${speaker}${timing}${w.text}`);
}
```

### ऐप पर जाएं

```
package main

import (
    "fmt"

    "google.golang.org/genai/interactions/models/interactions"
)

func extractWordAnnotations(interaction *interactions.Interaction) []*interactions.WordInfo {
    var words []*interactions.WordInfo
    if interaction == nil {
        return words
    }
    for _, step := range interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    for _, annotation := range content.TextContent.Annotations {
                        if annotation.WordInfo != nil {
                            words = append(words, annotation.WordInfo)
                        }
                    }
                }
            }
        }
    }
    return words
}

func main() {
    var interaction *interactions.Interaction
    words := extractWordAnnotations(interaction)

    for _, w := range words {
        speaker := ""
        if w.Speaker != nil && *w.Speaker != "" {
            speaker = fmt.Sprintf("[%s] ", *w.Speaker)
        }
        timing := ""
        if w.StartOffset != nil && w.EndOffset != nil {
            timing = fmt.Sprintf("(%s -> %s) ", *w.StartOffset, *w.EndOffset)
        }
        fmt.Printf("%s%s%s\n", speaker, timing, w.GetText())
    }
}
```

### REST

```
{
  "id": "interactions/abc123xyz",
  "status": "completed",
  "steps": [
    {
      "id": "step_001",
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Hello world",
          "annotations": [
            {
              "type": "word_info",
              "text": "Hello",
              "speaker": "spk_1",
              "start_offset": "0.100s",
              "end_offset": "0.450s"
            },
            {
              "type": "word_info",
              "text": "world",
              "speaker": "spk_1",
              "start_offset": "0.500s",
              "end_offset": "0.850s"
            }
          ]
        }
      ]
    }
  ]
}
```

## इस्तेमाल की जा सकने वाली भाषाएं

Gemini 3.5 Transcribe के लिए, इन भाषाओं और BCP-47 भाषा कोड का इस्तेमाल किया जा सकता है:

| भाषा | BCP-47 कोड | भाषा | BCP-47 कोड |
| --- | --- | --- | --- |
| अफ़्रीकान्स | `af-ZA` | जापानी | `ja-JP` |
| अमहैरिक | `am-ET` | जावानीज़ | `jv-ID` |
| अरबी (मिस्र) | `ar-EG` | Kabuverdianu | `kea-CV` |
| आर्मीनियन | `hy-AM` | कन्नड़ | `kn-IN` |
| असमिया | `as-IN` | कज़ाक | `kk-KZ` |
| अज़रबैजानी | `az-AZ` | कोरियन | `ko-KR` |
| बेलारूसी | `be-BY` | किर्गिज़ | `ky-KG` |
| बांग्ला (बांग्लादेश) | `bn-BD` | लातवियन | `lv-LV` |
| बांग्ला (भारत) | `bn-IN` | लिंगाला | `ln-CD` |
| बोस्नियन | `bs-BA` | लिथुएनियन | `lt-LT` |
| बल्गैरियन | `bg-BG` | मैसेडोनियन | `mk-MK` |
| बल्गेरियन (ऐरोमेनियन) | `rup-BG` | मलय | `ms-MY` |
| बर्मीज़ | `my-MM` | मलयालम | `ml-IN` |
| कैंटोनीज़ (ट्रेडिशनल) | `yue-Hant-HK` | मोल्टीज़ | `mt-MT` |
| कैटलैन | `ca-ES` | मैंडरिन चाइनीज़ (सिंप्लिफ़ाइड) | `cmn-Hans-CN` |
| सेबुआनो | `ceb` | मराठी | `mr-IN` |
| सेंट्रल खमेर | `km-KH` | मंगोलियन | `mn-MN` |
| क्रोएशियन | `hr-HR` | नेपाली | `ne-NP` |
| चेक | `cs-CZ` | नॉर्वीजन | `nb-NO` |
| डैनिश | `da-DK` | ओड़िया | `or-IN` |
| डच | `nl-NL` | पोलिश | `pl-PL` |
| अंग्रेज़ी (ग्रेट ब्रिटेन) | `en-GB` | पॉर्चुगीज़ (ब्राज़ील) | `pt-BR` |
| अंग्रेज़ी (भारत) | `en-IN` | पॉर्चगीज़ (पुर्तगाल) | `pt-PT` |
| अंग्रेज़ी (संयुक्त राज्य अमेरिका) | `en-US` | पंजाबी | `pa-IN` |
| एस्टोनियन | `et-EE` | पंजाबी (गुरमुखी लिपि) | `pa-Guru-IN` |
| फ़ारसी | `fa-IR` | रोमानियन | `ro-RO` |
| फ़िलिपीनी | `fil-PH` | रूसी | `ru-RU` |
| फ़िनिश | `fi-FI` | सर्बियन | `sr-RS` |
| फ़्रांसीसी | `fr-FR` | सिंधी (अरबी लिपि) | `sd-Arab-IN` |
| गैलिशियन | `gl-ES` | स्लोवाक | `sk-SK` |
| जॉर्जियन | `ka-GE` | स्लोवेनियन | `sl-SI` |
| जर्मन | `de-DE` | स्पैनिश (लैटिन अमेरिका) | `es-419` |
| ग्रीक | `el-GR` | स्पैनिश (संयुक्त राज्य अमेरिका) | `es-US` |
| गुजराती | `gu-IN` | स्वाहिली (केन्या) | `sw-KE` |
| हौसा | `ha-NG` | स्वीडिश | `sv-SE` |
| हिब्रू | `he-IL` | ताजिक | `tg-TJ` |
| हिन्दी | `hi-IN` | तेलुगु | `te-IN` |
| हंगेरियन | `hu-HU` | थाई | `th-TH` |
| आइसलैंडिक | `is-IS` | टर्किश | `tr-TR` |
| इंडियन इंग्लिश | `en-IN` | यूक्रेनियन | `uk-UA` |
| इंडोनेशियन | `id-ID` | उज़्बेक | `uz-UZ` |
| इटैलियन | `it-IT` | वियतनामीज़ | `vi-VN` |

## इस्तेमाल किए जा सकने वाले ऑडियो फ़ॉर्मैट

Gemini 3.5 Transcribe में, इन ऑडियो फ़ॉर्मैट के MIME टाइप इस्तेमाल किए जा सकते हैं:

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG - `audio/ogg`
- FLAC - `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16 - `audio/l16`
- Opus - `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM - `audio/webm`

इस्तेमाल किए जा सकने वाले MIME टाइप और पैरामीटर स्कीमा की पूरी सूची देखने के लिए, [Interactions API का रेफ़रंस](https://ai.google.dev/api/interactions-api?hl=hi#Resource:Content) देखें.

## पैरामीटर का रेफ़रंस

`generation_config` में मौजूद `transcription_config` ऑब्जेक्ट में फ़ील्ड सेट करके, ट्रांसक्रिप्शन की सुविधा कॉन्फ़िगर करें:

| फ़ील्ड | टाइप | ब्यौरा |
| --- | --- | --- |
| `language_codes` | स्ट्रिंग का कलेक्शन | BCP-47 भाषा कोड (जैसे, `["en-US"]`). अगर इसे शामिल नहीं किया जाता है या यह खाली (`[]`) है, तो मॉडल अपने-आप भाषा की पहचान कर लेता है और कोड-स्विचिंग को मैनेज करता है. |
| `custom_vocabulary` | स्ट्रिंग का कलेक्शन | बोली पहचानने की सुविधा को बेहतर बनाने के लिए,ज़्यादा से ज़्यादा 1, 000 कस्टम शब्द, संक्षिप्त नाम या व्यक्तिवाचक संज्ञाएं. यह सुविधा, स्पीकर डायराइज़ेशन और शब्द-लेवल के टाइमस्टैंप के साथ काम नहीं करती. |
| `mode` | ऑब्जेक्ट या स्ट्रिंग | बोले जा रहे शब्दों को टेक्स्ट में बदलने की सुविधा का कॉन्फ़िगरेशन. यह `"smart"` या वर्बैटिम मोड ऑब्जेक्ट (`{"type": "verbatim", ...}`) स्वीकार करता है. डिफ़ॉल्ट रूप से, वर्बैटिम ट्रांसक्रिप्शन पर सेट होता है. |
| `mode.type` | स्ट्रिंग | *(सिर्फ़ वर्बैटिम मोड के लिए)* मोड आइडेंटिफ़ायर. इसे हमेशा `"verbatim"` पर सेट किया जाता है. |
| `mode.timestamp_granularities` | स्ट्रिंग का कलेक्शन | *(सिर्फ़ वर्बैटिम मोड के लिए)* जवाब में शामिल किए जाने वाले टाइमस्टैंप की फ़्रीक्वेंसी. शब्द की शुरुआत और खत्म होने के ऑफ़सेट चालू करने के लिए, `["word"]` पास करें. कस्टम शब्दावली के साथ काम नहीं करता. |
| `mode.diarization_mode` | स्ट्रिंग | *(सिर्फ़ वर्बैटिम मोड के लिए)* डायराइज़ेशन मोड. अलग-अलग स्पीकर की पहचान करने और उन्हें लेबल करने के लिए, `"speaker"` पास करें. कस्टम शब्दावली के साथ काम नहीं करता. |

## सबसे सही तरीके

- **साफ़ ऑडियो उपलब्ध कराएं:** पक्का करें कि ऑडियो रिकॉर्डिंग में आवाज़ साफ़ सुनाई दे और क्लिप में आवाज़ न कटे.
- **ऑडियो की भाषा के बारे में जानकारी दें:** अगर आपको ऑडियो की भाषा के बारे में पहले से पता है, तो `language_codes` को सेट करें, ताकि ऑडियो को टेक्स्ट में ज़्यादा सटीक तरीके से बदला जा सके.
- **कस्टम शब्दावली को टारगेट करना:** `custom_vocabulary` में, रोज़मर्रा के आम शब्दों के बजाय सिर्फ़ अलग-अलग डोमेन के शब्द, ब्रैंड के नाम या संज्ञाएं शामिल करें.
- **ज़्यादा बड़ी रिकॉर्डिंग के लिए, Files API का इस्तेमाल करें:** अगर फ़ाइल कुछ सेकंड से ज़्यादा लंबी है, तो `client.files.upload` का इस्तेमाल करके फ़ाइल अपलोड करें. साथ ही, मॉडल को वापस मिला फ़ाइल यूआरआई पास करें.

## सीमाएं

- **ऑडियो की अवधि:** स्टैंडर्ड यूनरी अनुरोधों में, एक घंटे तक की ऑडियो फ़ाइलें इस्तेमाल की जा सकती हैं. स्पीकर के हिसाब से लेबलिंग या शब्द-लेवल के टाइमस्टैंप जैसी सुविधाएं चालू होने पर, ऑडियो प्रोसेसिंग सिर्फ़ 30 मिनट तक की जा सकती है.
- **शब्द के लेवल पर टाइमस्टैंप:** शब्द के लेवल पर टाइमस्टैंप की सुविधा चालू करने से, ट्रांसक्रिप्शन की कुल सटीकता कम हो सकती है.
- **स्पीकर डायराइज़ेशन:** स्पीकर डायराइज़ेशन की सुविधा, ज़्यादा से ज़्यादा आठ स्पीकर के लिए काम करती है. तीन या इससे ज़्यादा स्पीकर के लिए, स्पीकर एट्रिब्यूशन की सुविधा अभी एक्सपेरिमेंट के तौर पर उपलब्ध है.
- **कस्टम शब्दावली:** `custom_vocabulary` में ज़्यादा से ज़्यादा 1,000 शब्द दिए जा सकते हैं. हालांकि, आम तौर पर 100 शब्दों से ही सबसे अच्छे नतीजे मिलते हैं. `custom_vocabulary` को स्पीकर के हिसाब से शब्दों को अलग-अलग करने या शब्द-लेवल के टाइमस्टैंप के साथ इस्तेमाल नहीं किया जा सकता. एपीआई, उन अनुरोधों को अस्वीकार कर देता है जिनमें `custom_vocabulary` के साथ इनमें से किसी भी सुविधा का इस्तेमाल किया गया हो.
- **मोड के साथ काम करने की सुविधा:** स्मार्ट ट्रांसक्रिप्शन (`"smart"`) को `timestamp_granularities` या `diarization_mode` के साथ इस्तेमाल नहीं किया जा सकता.

## आगे क्या करना है

- लाइव एपीआई का इस्तेमाल करके, [बोली को लेख में बदलने की सुविधा से जुड़ी गाइड](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=hi) की मदद से, रीयल-टाइम में ऑडियो स्ट्रीम करें.
- ऑडियो कॉन्टेंट का विश्लेषण करने, उसकी खास जानकारी पाने या उससे जुड़े सवाल पूछने के लिए, [ऑडियो को समझने की सुविधा](https://ai.google.dev/gemini-api/docs/audio?hl=hi) का इस्तेमाल करें.
- [लिखे गए शब्दों को सुनने की सुविधा](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi) का इस्तेमाल करके, टेक्स्ट से ऑडियो बनाने का तरीका जानें.
- मॉडल की कीमत और टोकन की सीमाओं के बारे में जानने के लिए, [कीमत वाला पेज](https://ai.google.dev/gemini-api/docs/pricing?hl=hi#gemini-3.5-transcribe) देखें.
- मीडिया फ़ाइलों को अपलोड करने और मैनेज करने के बारे में ज़्यादा जानने के लिए, [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) गाइड देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-24 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-24 (UTC) को अपडेट किया गया."],[],[]]
