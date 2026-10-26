---
source_url: https://ai.google.dev/gemini-api/docs/transcribe?hl=bn
fetched_at: 2026-10-26T05:54:18.281727+00:00
title: "\u0985\u09a1\u09bf\u0993 \u099f\u09cd\u09b0\u09be\u09a8\u09cd\u09b8\u0995\u09cd\u09b0\u09bf\u09aa\u09b6\u09a8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# অডিও ট্রান্সক্রিপশন

Gemini API, Gemini 3.5 Transcribe মডেল (`gemini-3.5-transcribe`) ব্যবহার করে অডিও ফাইলের স্পিচকে টেক্সটে কনভার্ট করে। Gemini-র অডিও বোঝার ক্ষমতার উপর ভিত্তি করে, এটি অটোমেটিক ভাষা শনাক্তকরণ, স্পিকার ডায়েরাইজেশন, শব্দ-লেভেল টাইমস্ট্যাম্প এবং কাস্টম শব্দভাণ্ডার সংক্রান্ত ইঙ্গিত সহ সঠিক ট্রান্সক্রিপশন প্রদান করে। এছাড়াও, এটি [স্মার্ট ট্রান্সক্রিপশন](#transcription-modes) মোড প্রদান করে, যার মধ্যে ডিসফ্লুয়েন্সি রিমুভাল ও স্মার্ট ফর্ম্যাটিং ফিচার রয়েছে।

কোনও অডিও ফাইল ট্রান্সক্রাইব করতে, অডিও আপলোড করে `gemini-3.5-transcribe`-এ পাস করুন:

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

### বিশ্রাম

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

## এক নজরে

Gemini 3.5 Transcribe স্পিচ-টু-টেক্সট টাস্কের জন্য অপ্টিমাইজ করা হয়েছে। এটি বিভিন্ন অ্যাকসেন্ট, ব্যাকগ্রাউন্ডের আওয়াজ ও একাধিক ভাষায় কথোপকথন ম্যানেজ করে।

মূল কার্যকারিতার মধ্যে এগুলি অন্তর্ভুক্ত:

- **অটোমেটিক স্পিচ রিকগনিশন (ASR):** [৮৫টির বেশি লোকেলে](#supported-languages) অটোমেটিক ভাষা শনাক্ত করে। ম্যানুয়াল কনফিগারেশন ছাড়াই ইন্ট্রা-সেন্টেন্স এবং ইন্টার-সেন্টেন্সিয়াল কোড-সুইচিং ম্যানেজ করে।
- **কাস্টম শব্দভাণ্ডার:** ১,০০০টি পর্যন্ত বাক্যাংশ পাস করার মাধ্যমে ডোমেন-নির্দিষ্ট শব্দ, সংক্ষিপ্ত রূপ এবং সঠিক নামের প্রতি পক্ষপাতিত্ব শনাক্ত করে।
- **স্পিকার ডায়ারিাইজেশন:** একাধিক স্পিকারের মধ্যে পার্থক্য করে এবং স্পোকেন সেগমেন্টকে আলাদা লেবেলে অ্যাট্রিবিউট করে।
- **শব্দ-লেভেল টাইমস্ট্যাম্প:** প্রতিটি শনাক্ত করা শব্দের জন্য শুরু ও শেষ হওয়ার সঠিক সময় অফসেট জেনারেট করে।
- **স্মার্ট ট্রান্সক্রিপশন:** তোতলামি, ফিলার শব্দ, পুনরাবৃত্তি সরিয়ে দেয় এবং স্ট্রাকচার্ড ফর্ম্যাটিং প্রয়োগ করে।
- **ফর্ম্যাটিং ও নরমালাইজেশন:** বড় হাতের অক্ষর, যতিচিহ্ন ও ইনভার্স টেক্সট নরমালাইজেশন প্রয়োগ করে, যেমন "ছাব্বিশ মিলিয়ন ডলার" থেকে "$২৬ মিলিয়ন" হিসেবে কনভার্ট করা।

অডিও কন্টেন্টের উপর সাধারণ অডিও রিজনিং বা প্রশ্নের উত্তর দেওয়ার জন্য, [অডিও বোঝা](https://ai.google.dev/gemini-api/docs/audio?hl=bn) ব্যবহার করুন। টেক্সট-টু-স্পিচ অডিও সিন্থেসিসের জন্য, [টেক্সট-টু-স্পিচ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=bn) ব্যবহার করুন।

## ভাষা শনাক্তকরণ ও ইঙ্গিত

ডিফল্ট হিসেবে, মডেলটি অটোমেটিক কথ্য ভাষা শনাক্ত করে। স্পিকার কোড-সুইচ করলে এটি ডায়নামিকভাবে ভাষা পরিবর্তন করে।

অটোমেটিক শনাক্তকরণ ব্যবহার করতে, `language_codes` বাদ দিন বা একটি খালি তালিকা প্রদান করুন:

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

### বিশ্রাম

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

আপনি আগে থেকে ভাষা জানলে, ট্রান্সক্রিপশনের নির্ভুলতা উন্নত করতে `language_codes`-এ BCP-47 ভাষার কোড নির্দিষ্ট করুন ([কাজ করে এমন ভাষা](#supported-languages) দেখুন):

### Python

```
generation_config = {
    "transcription_config": {
        "language_codes": ["es-ES"],
    }
}
```

### জাভাস্ক্রিপ্ট

```
const generationConfig = {
  transcription_config: {
    language_codes: ["es-ES"],
  },
};
```

### খুলুন

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

### বিশ্রাম

```
{
  "generation_config": {
    "transcription_config": {
      "language_codes": ["es-ES"]
    }
  }
}
```

## কাস্টম শব্দভাণ্ডার

আপনি স্পিচ মডেলকে বিরল শব্দ, টেকনিক্যাল জার্গন, ব্র্যান্ডের নাম বা প্রপার নাউনের দিকে চালিত করতে পারেন। `custom_vocabulary` অ্যারেতে সর্বাধিক ১,০০০টি শব্দ প্রদান করুন (সাধারণত সর্বাধিক ১০০টি শব্দ প্রদান করলে সেরা ফলাফল পাওয়া যায়):

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

### বিশ্রাম

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

## স্পিকার ডায়ারাইজেশন

স্পিকার ডায়ারিাইজেশন রেকর্ডিংয়ে বিভিন্ন ভয়েস শনাক্ত করে এবং প্রতিটি সেগমেন্টকে `spk_1` বা `spk_2`-এর মতো স্পিকার শনাক্তকারী দিয়ে ট্যাগ করে। সর্বাধিক ৮ জন স্পিকারের ভয়েস শনাক্ত করা যায় (৩ বা তার বেশি স্পিকারের ভয়েস শনাক্ত করার ফিচারটি পরীক্ষামূলক)।

`mode`-এর মধ্যে `diarization_mode` কনফিগার করে ডায়ারাইজেশন চালু করুন:

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

### বিশ্রাম

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

## শব্দ-লেভেল টাইমস্ট্যাম্প

শব্দ-লেভেল টাইমস্ট্যাম্প অডিও স্ট্রিমে প্রতিটি শনাক্ত করা শব্দের জন্য সঠিক শুরু এবং শেষ অফসেট প্রদান করে।

`mode`-এর মধ্যে `timestamp_granularities` কনফিগার করে টাইমস্ট্যাম্প চালু করুন:

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

### বিশ্রাম

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

বক্তার লেবেল ও শব্দের টাইমস্ট্যাম্প, দুটিই পেতে আপনি `mode`-এ `diarization_mode` ও `timestamp_granularities` একত্রিত করতে পারবেন:

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

### বিশ্রাম

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

## ট্রান্সক্রিপশন মোড

Gemini 3.5 Transcribe `mode` প্যারামিটারের মাধ্যমে দুটি ট্রান্সক্রিপশন মোড সাপোর্ট করে:

- **`verbatim` (ডিফল্ট)**: যা বলা হয়েছে তার হুবহু ট্রান্সক্রিপ্ট প্রদান করে, যার মধ্যে ফিলার শব্দ ("উম", "উহ", "যেমন", "আপনি জানেন"), পুনরাবৃত্তি, বিরতি এবং ভুল শুরু অন্তর্ভুক্ত থাকে। এই মোডে (`{"type": "verbatim", ...}`) টাইমস্ট্যাম্প ও স্পিকার ডায়ারাইজেশন কনফিগার করা হয়।
- **`smart` (স্মার্ট ট্রান্সক্রিপশন)**: ইন্টেলিজেন্ট পোস্ট-প্রসেসিং প্রয়োগ করে পড়ার জন্য ট্রান্সক্রিপ্ট অপ্টিমাইজ করে:
  - **ডিসফ্লুয়েন্সি রিমুভাল**: কথোপকথনের ফিলার শব্দ, তোতলানো এবং ভুল শুরু বাদ দেয়।
  - **ইনলাইন সেল্ফ-কারেকশন**: সরাসরি স্পোকেন কারেকশন সমাধান করে (যেমন, *"চলুন মঙ্গলবার দেখা করি, আসলে না, বুধবার দুপুর দুটোয়"* হয়ে যায় *"চলুন বুধবার দুপুর ২:০০টায় দেখা করি"*)।
  - **অটোমেটিক স্ট্রাকচার্ড ফর্ম্যাটিং**: আপনার বলা কথা অটোমেটিক প্যারাগ্রাফ, নম্বরযুক্ত তালিকা, বুলেট পয়েন্ট, ফর্ম্যাট করা তারিখ, মুদ্রা ও নম্বরে সাজিয়ে দেয়।
  - **ব্যাকরণগত ক্লিন-আপ**: স্বাভাবিক যতিচিহ্ন, বাক্যের কেসিং ও ফ্লো প্রয়োগ করে।

| স্পোকেন অডিও | `verbatim`টি আউটপুট | `smart` (স্মার্ট ট্রান্সক্রিপশন) আউটপুট |
| --- | --- | --- |
| "উম, মিটিংয়ের জন্য আমার মনে হয়, আমাদের, উম, অ্যালিসকে আমন্ত্রণ জানানো উচিত, না দাঁড়াও, বব ও ক্যারলকে।" | "মিটিংয়ের জন্য আমার মনে হয় আমাদের অ্যালিসকে আমন্ত্রণ জানানো উচিত এবং বব ও ক্যারলকে নয়।" | "মিটিংয়ের জন্য, আমার মনে হয় আমাদের বব ও ক্যারলকে আমন্ত্রণ জানানো উচিত।" |
| "প্রথম আইটেম বাজেট পর্যালোচনা করা দ্বিতীয় আইটেম টাইমলাইন চূড়ান্ত করা তৃতীয় আইটেম রিক্যাপ পাঠানো" | "প্রথম আইটেম বাজেট পর্যালোচনা দ্বিতীয় আইটেম টাইমলাইন চূড়ান্ত করা তৃতীয় আইটেম রিক্যাপ পাঠানো" | "১. বাজেট পর্যালোচনা করুন ২। টাইমলাইন চূড়ান্ত করুন ৩. রিক্যাপ পাঠান" |

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

### বিশ্রাম

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

## ট্রান্সক্রিপশন আউটপুট পার্স করা হচ্ছে

সম্পূর্ণ ট্রান্সস্ক্রিপ্ট টেক্সট `interaction.output_text`-এ ফেরত পাঠানো হয়েছে।

`timestamp_granularities` বা `diarization_mode` চালু করা থাকলে, API ইন্টার‍্যাকশন কন্টেন্টের সাথে অ্যাটাচ করা শব্দ-লেভেল অ্যানোটেশনও ফিরিয়ে দেয়।

শব্দের টাইমস্ট্যাম্প এবং স্পিকারের টার্ন কীভাবে এক্সট্র্যাক্ট এবং ইটারেট করতে হয় তা এখানে দেওয়া হল:

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

### বিশ্রাম

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
              "end_offset": "0.400s"
            },
            {
              "type": "word_info",
              "text": "world",
              "speaker": "spk_1",
              "start_offset": "0.500s",
              "end_offset": "0.800s"
            }
          ]
        }
      ]
    }
  ]
}
```

## যেসব ভাষায় এটি ব্যবহার করা যায়

Gemini 3.5 Transcribe-এর জন্য নিম্নলিখিত ভাষা এবং BCP-47 ভাষা কোড কাজ করে:

| ভাষা | BCP-47 কোড | ভাষা | BCP-47 কোড |
| --- | --- | --- | --- |
| আফ্রিকান্স | `af-ZA` | জাপানি | `ja-JP` |
| আমহারীক | `am-ET` | জাভানীয় | `jv-ID` |
| আরবি (মিশর) | `ar-EG` | কাবোভার্ডিয়ানু | `kea-CV` |
| আর্মেনীয় | `hy-AM` | কন্নড় | `kn-IN` |
| অসমিয়া | `as-IN` | কাজাখ | `kk-KZ` |
| আজারবাইজানি | `az-AZ` | কোরিয়ান | `ko-KR` |
| বেলারুশিয়ান | `be-BY` | কিরগিজ | `ky-KG` |
| বাংলা (বাংলাদেশ) | `bn-BD` | লাটভিয়ান | `lv-LV` |
| বাংলা (ভারত) | `bn-IN` | লিঙ্গালা | `ln-CD` |
| বসনিয়ান | `bs-BA` | লিথুয়ানিয়ান | `lt-LT` |
| বুলগেরিয়ান | `bg-BG` | ম্যাসিডোনীয় | `mk-MK` |
| বুলগেরিয়ান (অ্যারোমানিয়ান) | `rup-BG` | মালয় | `ms-MY` |
| বার্মিজ | `my-MM` | মালায়লাম | `ml-IN` |
| ক্যান্টনিজ (ঐতিহ্যশালী) | `yue-Hant-HK` | মল্টিজ | `mt-MT` |
| কাতালান | `ca-ES` | ম্যান্ডারিন চাইনিজ (সরলীকৃত) | `cmn-Hans-CN` |
| সেবুয়ানো | `ceb` | মারাঠি | `mr-IN` |
| কেন্দ্রীয় খমের | `km-KH` | মঙ্গোলীয়ান | `mn-MN` |
| ক্রোয়েশিয়ান | `hr-HR` | নেপালি | `ne-NP` |
| চেক | `cs-CZ` | নরওয়েজিয়ান | `nb-NO` |
| ড্যানিশ | `da-DK` | ওড়িয়া | `or-IN` |
| ডাচ | `nl-NL` | পোলিশ | `pl-PL` |
| ইংরেজি (গ্রেট ব্রিটেন) | `en-GB` | পর্তুগিজ (ব্রাজিল) | `pt-BR` |
| ইংরাজি (ভারত) | `en-IN` | পর্তুগিজ (পর্তুগাল) | `pt-PT` |
| ইংরেজি (মার্কিন যুক্তরাষ্ট্র) | `en-US` | পঞ্জাবি | `pa-IN` |
| এস্তোনিয়ান | `et-EE` | পাঞ্জাবি (গুরুমুখী লিপি) | `pa-Guru-IN` |
| ফার্সি | `fa-IR` | রোমানিয়ান | `ro-RO` |
| ফিলিপিনো | `fil-PH` | রুশ | `ru-RU` |
| ফিনিশ | `fi-FI` | সার্বিয় | `sr-RS` |
| ফরাসী | `fr-FR` | সিন্ধি (আরবি স্ক্রিপ্ট) | `sd-Arab-IN` |
| গ্যালিশিয় | `gl-ES` | স্লোভাক | `sk-SK` |
| জর্জিয়ান | `ka-GE` | স্লোভেনিয়ান | `sl-SI` |
| জার্মান | `de-DE` | স্প্যানিশ (ল্যাটিন আমেরিকা) | `es-419` |
| গ্রিক | `el-GR` | স্প্যানিশ (মার্কিন যুক্তরাষ্ট্র) | `es-US` |
| গুজরাতি | `gu-IN` | সোয়াহিলি (কেনিয়া) | `sw-KE` |
| হাউসা | `ha-NG` | সুইডিশ | `sv-SE` |
| হিব্রু | `he-IL` | তাজিক | `tg-TJ` |
| হিন্দি | `hi-IN` | তেলুগু | `te-IN` |
| হাঙ্গেরিয়ান | `hu-HU` | থাই | `th-TH` |
| আইসল্যান্ডিক | `is-IS` | তুর্কি | `tr-TR` |
| ভারতীয় ইংরেজি | `en-IN` | ইউক্রেনিয়ান | `uk-UA` |
| ইন্দোনেশিয়ান | `id-ID` | উজবেক | `uz-UZ` |
| ইতালিয়ান | `it-IT` | ভিয়েতনামিজ | `vi-VN` |

## কাজ করে এমন অডিও ফর্ম্যাট

Gemini 3.5 Transcribe নিম্নলিখিত অডিও ফর্ম্যাট MIME-এর প্রকার সাপোর্ট করে:

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

কাজ করে এমন MIME-এর প্রকার ও প্যারামিটার স্কিমার সম্পূর্ণ তালিকার জন্য, [Interactions API রেফারেন্স](https://ai.google.dev/api/interactions-api?hl=bn#Resource:Content) দেখুন।

## প্যারামিটার রেফারেন্স

`generation_config`-এ `transcription_config` অবজেক্টের মধ্যে ফিল্ড সেট করে ট্রান্সক্রিপশন কনফিগার করুন:

| ফিল্ড | ধরন | বিবরণ |
| --- | --- | --- |
| `language_codes` | স্ট্রিংয়ের অ্যারে | BCP-47 ভাষা কোড (যেমন, `["en-US"]`)। বাদ দেওয়া হলে বা খালি (`[]`) থাকলে, মডেল অটোমেটিক ভাষা শনাক্ত করে এবং কোড-সুইচিং ম্যানেজ করে। |
| `custom_vocabulary` | স্ট্রিংয়ের অ্যারে | স্পিচ রিকগনিশনকে প্রভাবিত করতে ১,০০০টি পর্যন্ত কাস্টম শব্দ, সংক্ষিপ্ত রূপ বা নামবাচক বিশেষ্য। স্পিকার ডায়ারাইজেশন এবং শব্দ-লেভেল টাইমস্ট্যাম্পের সাথে মানানসই নয়। |
| `mode` | অবজেক্ট বা স্ট্রিং | ট্রান্সক্রিপশন মোড কনফিগারেশন। `"smart"` বা ভারবাটিম মোড অবজেক্ট (`{"type": "verbatim", ...}`) গ্রহণ করে। ডিফল্ট হিসেবে ভারবাটিম ট্রান্সক্রিপশন সেট করা থাকে। |
| `mode.type` | স্ট্রিং | *(শুধুমাত্র ভারবাটিম মোড)* মোড শনাক্তকারী। সবসময় `"verbatim"` হিসেবে সেট করা আছে। |
| `mode.timestamp_granularities` | স্ট্রিংয়ের অ্যারে | *(শুধুমাত্র ভারবাটিম মোড)* ফেরত পাঠানোর জন্য টাইমস্ট্যাম্পের গ্রানুলারিটি। শব্দের শুরু ও শেষ অফসেট চালু করতে `["word"]` পাস করুন। কাস্টম শব্দভাণ্ডারের সাথে মানানসই নয়। |
| `mode.diarization_mode` | স্ট্রিং | *(শুধুমাত্র ভারবাটিম মোড)* ডায়রাইজেশন মোড। আলাদা আলাদা বক্তাকে শনাক্ত ও লেবেল করতে `"speaker"` পাস করুন। কাস্টম শব্দভাণ্ডারের সাথে মানানসই নয়। |

## পেশাদার পদ্ধতি

- **স্পষ্ট অডিও প্রদান করুন:** অডিও রেকর্ডিংয়ে ভয়েস যেন স্পষ্ট ও আলাদাভাবে শোনা যায় এবং গুরুতর ক্লিপিং এড়িয়ে চলুন।
- **জানা থাকলে ভাষার ইঙ্গিত দিন:** আপনি আগে থেকে অডিওর ভাষা জানলে, নির্ভুলতা বাড়াতে `language_codes` নির্দিষ্ট করুন।
- **টার্গেট কাস্টম শব্দভাণ্ডার:** `custom_vocabulary`-এ সাধারণ দৈনন্দিন শব্দের পরিবর্তে শুধুমাত্র স্বতন্ত্র ডোমেন শব্দ, ব্র্যান্ডের নাম বা প্রপার নাউন অন্তর্ভুক্ত করুন।
- **বড় রেকর্ডিংয়ের জন্য Files API ব্যবহার করুন:** কয়েক সেকেন্ডের চেয়ে বড় ফাইলের ক্ষেত্রে, `client.files.upload` ব্যবহার করে ফাইল আপলোড করুন এবং রিটার্ন করা ফাইল URI মডেলে পাস করুন।

## সীমাবদ্ধতা

- **অডিওর সময়সীমা:** স্ট্যান্ডার্ড ইউনারি অনুরোধে সর্বাধিক ১ ঘণ্টার অডিও ফাইল কাজ করে। স্পিকার ডায়ারিাইজেশন বা শব্দ-লেভেল টাইমস্ট্যাম্পের মতো ফিচার চালু থাকলে অডিও প্রসেসিং ৩০ মিনিটে সীমিত থাকে।
- **শব্দ-লেভেল টাইমস্ট্যাম্প:** শব্দ-লেভেল টাইমস্ট্যাম্প চালু করলে সামগ্রিক ট্রান্সক্রিপশনের নির্ভুলতা কমে যেতে পারে।
- **স্পিকার ডায়ারাইজেশন:** স্পিকার ডায়ারাইজেশন সর্বাধিক ৮ জন স্পিকারের ক্ষেত্রে কাজ করে। ৩ বা তার বেশি স্পিকারের জন্য স্পিকার অ্যাট্রিবিউশন পরীক্ষামূলক পর্যায়ে আছে।
- **কাস্টম শব্দভাণ্ডার:** আপনি `custom_vocabulary`-এ সর্বাধিক ১,০০০টি শব্দ দিতে পারেন, তবে সাধারণত সর্বাধিক ১০০টি শব্দ দিলে সেরা ফলাফল পাওয়া যায়। আপনি স্পিকার ডায়েরাইজেশন বা শব্দ-লেভেল টাইমস্ট্যাম্পের সাথে `custom_vocabulary` একত্রিত করতে পারবেন না; API সেইসব অনুরোধ বাতিল করে দেয় যেগুলি যেকোনও ফিচারের সাথে `custom_vocabulary` নির্দিষ্ট করে।
- **মোড কম্প্যাটিবিলিটি:** স্মার্ট ট্রান্সক্রিপশন (`"smart"`) `timestamp_granularities` বা `diarization_mode`-এর সাথে একত্রিত করা যাবে না।

## এর পরে কী করতে হবে

- Live API ব্যবহার করে [লাইভ ট্রান্সক্রিপশন গাইড](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=bn)-এর মাধ্যমে রিয়েল-টাইম অডিও স্ট্রিম করুন।
- অডিও কন্টেন্ট বিশ্লেষণ, সারসংক্ষেপ বা কোয়েরি করতে [অডিও বোঝা](https://ai.google.dev/gemini-api/docs/audio?hl=bn) এক্সপ্লোর করুন।
- [টেক্সট-টু-স্পিচ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=bn) ব্যবহার করে কীভাবে টেক্সট থেকে অডিও সিন্থেসাইজ করতে হয় তা জানুন।
- মডেলের দাম ও টোকেন সীমা জানতে [দাম সংক্রান্ত পৃষ্ঠা](https://ai.google.dev/gemini-api/docs/pricing?hl=bn#gemini-3.5-transcribe) চেক করুন।
- মিডিয়া ফাইল আপলোড ও ম্যানেজ করা সম্পর্কে আরও জানতে [Files API](https://ai.google.dev/gemini-api/docs/files?hl=bn) গাইড দেখুন।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-23 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-23 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
