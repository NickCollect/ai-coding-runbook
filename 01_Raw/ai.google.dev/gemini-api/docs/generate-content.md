---
source_url: https://ai.google.dev/gemini-api/docs/generate-content?hl=bn
fetched_at: 2026-10-12T06:50:20.760663+00:00
title: "Gemini API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

জেমিনি ৩.৮ ফ্ল্যাশ এখন পাওয়া যাচ্ছে। [ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=bn) ।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs/generate-content?hl=bn)

# Gemini API

Gemini API হল Gemini, Veo,
Nano Banana ও আরও অনেক কিছুর মাধ্যমে প্রম্পট থেকে প্রোডাকশনে যাওয়ার সবচেয়ে দ্রুত উপায়। এটি আপনাকে টেক্সট ও ছবি জেনারেট করতে, মাল্টিমোডাল ইনপুট বিশ্লেষণ করতে এবং
কথোপকথনমূলক এজেন্ট তৈরি করতে আপনার
অ্যাপ্লিকেশনে এইসব জেনারেটিভ মডেল ইন্টিগ্রেট করতে দেয়।

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

[তৈরি করা শুরু করুন](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=bn)

---

## মডেলদের সাথে পরিচিত হন

[সবকটি দেখুন](https://ai.google.dev/gemini-api/docs/models?hl=bn)

[auto\_awesome
Gemini 3.1 Pro
নতুন

আমাদের সবচেয়ে বুদ্ধিমান মডেল, মাল্টিমোডাল বোঝার জন্য বিশ্বের সেরা, সব অত্যাধুনিক রিজনিংয়ের উপর ভিত্তি করে তৈরি।](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=bn)
[spark
Gemini 3.6 Flash
নতুন

আমাদের লেটেস্ট মডেল যা এজেন্টিক ও মাল্টিমোডাল টাস্কে শক্তিশালী পারফর্ম্যান্স ডেলিভার করার জন্য স্পিড ও ইন্টেলিজেন্সের মধ্যে ব্যালেন্স করে।](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=bn)
[graphic\_eq
Gemini 3.8 Flash TTS
নতুন

এক্সপ্রেসিভ অ্যাক্টিং, কাস্টম ভয়েস ডিজাইন ও ভয়েস রেপ্লিকেশন সহ স্টুডিও-গ্রেড টেক্সট-টু-স্পিচ মডেল।](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=bn)
[spark
Gemini 3.5 Flash-Lite
নতুন

কম লেটেন্সি ও হাই থ্রুপুট সাব-এজেন্ট টাস্কের জন্য অপ্টিমাইজ করা বেশি ভলিউম ও খরচ-সংবেদনশীল মডেল।](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=bn)
[spark
Gemini 3.1 Flash-Lite

Gemini 3 সিরিজের পারফর্ম্যান্স ও কোয়ালিটি সহ হাই-ভলিউম, খরচ-সংবেদনশীল মডেল।](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=bn)
[spark
Gemini 3 Flash

ফ্রন্টিয়ার-ক্লাস পারফর্ম্যান্স যা অনেক কম খরচে বড় মডেলের সাথে প্রতিদ্বন্দ্বিতা করতে পারে।](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=bn)
[🍌
Nano Banana

অত্যাধুনিক ইমেজ জেনারেশন ও এডিটিং মডেল।](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn)
[video\_library
Veo 3.1

আমাদের অত্যাধুনিক ভিডিও জেনারেশন মডেল, সাথে নেটিভ অডিও।](https://ai.google.dev/gemini-api/docs/video?hl=bn)
[spark
Gemini Robotics

একটি ভিশন-ল্যাঙ্গুয়েজ মডেল (VLM) যা রোবোটিক্সের ক্ষেত্রে Gemini-র এজেন্ট সংক্রান্ত ক্ষমতা নিয়ে আসে এবং বাস্তব জগতে উন্নত রিজনিং করার সুবিধা দেয়।](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=bn)

## ক্ষমতা এক্সপ্লোর করা

[imagesmode

নেটিভ ইমেজ জেনারেশন (Nano Banana)

Gemini 2.5 Flash Image-এর মাধ্যমে অত্যন্ত প্রাসঙ্গিক ছবি নেটিভভাবে তৈরি ও এডিট করুন।](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn)
[article

অনেক বড় প্রসঙ্গ

Gemini মডেলে লক্ষ লক্ষ টোকেন ইনপুট করুন এবং আনস্ট্রাকচার্ড ছবি, ভিডিও ও ডকুমেন্ট থেকে তথ্য পান।](https://ai.google.dev/gemini-api/docs/long-context?hl=bn)
[code

স্ট্রাকচার্ড আউটপুট

Gemini-কে JSON-এর মাধ্যমে উত্তর দেওয়ার জন্য সীমাবদ্ধ করুন, এটি হল অটোমেটিক প্রসেসিংয়ের জন্য উপযুক্ত একটি স্ট্রাকচার্ড ডেটা ফর্ম্যাট।](https://ai.google.dev/gemini-api/docs/structured-output?hl=bn)
[functions

ফাংশন কলিং

এক্সটার্নাল API ও টুলের সাথে Gemini কানেক্ট করে এজেন্টিক ওয়ার্কফ্লো তৈরি করুন।](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn)
[videocam

Veo 3.1-এর মাধ্যমে ভিডিও জেনারেশন

আমাদের অত্যাধুনিক মডেলের সাহায্যে টেক্সট বা ছবির প্রম্পট থেকে খুব ভালো কোয়ালিটির ভিডিও কন্টেন্ট তৈরি করুন।](https://ai.google.dev/gemini-api/docs/video?hl=bn)
[android\_recorder

Live API সহ ভয়েস এজেন্ট

Live API-এর সাহায্যে রিয়েল-টাইম ভয়েস অ্যাপ্লিকেশন ও এজেন্ট তৈরি করুন।](https://ai.google.dev/gemini-api/docs/live-api?hl=bn)
[build

টুল

Google Search, URL Context, Google Maps, Code Execution ও Computer Use-এর মতো বিল্ট-ইন টুলের মাধ্যমে Gemini-কে বিশ্বের সাথে কানেক্ট করুন।](https://ai.google.dev/gemini-api/docs/tools?hl=bn)
[stacks

ডকুমেন্ট বোঝা

সম্পূর্ণ মাল্টিমোডাল জ্ঞান বা অন্যান্য টেক্সট-ভিত্তিক ফাইলের ধরন সহ সর্বাধিক ১০০০ পৃষ্ঠার পিডিএফ ফাইল প্রসেস করুন।](https://ai.google.dev/gemini-api/docs/document-processing?hl=bn)
[cognition\_2

Thinking

জটিল টাস্ক ও এজেন্টের ক্ষেত্রে চিন্তাশক্তি কীভাবে যুক্তিনির্ভর কারণ নির্ণয় করার ক্ষমতাকে উন্নত করে তা এক্সপ্লোর করুন।](https://ai.google.dev/gemini-api/docs/thinking?hl=bn)

[Google AI Studio

প্রম্পট পরীক্ষা করা, API কী ম্যানেজ করা, ব্যবহার মনিটর করা এবং প্রোটোটাইপ তৈরি করা।](https://aistudio.google.com?hl=bn)
[group

ডেভেলপার কমিউনিটি

অন্যান্য ডেভেলপার ও Google ইঞ্জিনিয়ারদের থেকে প্রশ্ন জিজ্ঞাসা ও সমাধান খুঁজে নেওয়া।](https://discuss.ai.google.dev/c/gemini-api/4?hl=bn)
[menu\_book

API রেফারেন্স

অফিসিয়াল রেফারেন্স ডকুমেন্টেশনে Gemini API সম্পর্কে বিস্তারিত তথ্য পাবেন।](https://ai.google.dev/api?hl=bn)
[sensors

স্ট্যাটাস

Gemini API, Google AI Studio ও আমাদের মডেল পরিষেবার স্ট্যাটাস চেক করুন।](https://aistudio.google.com/status?hl=bn)

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-09 UTC-তে শেষবার আপডেট করা হয়েছে।

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-09 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
