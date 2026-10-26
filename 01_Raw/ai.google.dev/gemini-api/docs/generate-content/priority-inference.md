---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=bn
fetched_at: 2026-10-26T05:52:20.600553+00:00
title: "\u0985\u0997\u09cd\u09b0\u09be\u09a7\u09bf\u0995\u09be\u09b0 \u09b8\u0982\u0995\u09cd\u09b0\u09be\u09a8\u09cd\u09a4 \u0985\u09a8\u09c1\u09ae\u09be\u09a8 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs/generate-content?hl=bn)

মতামত জানান

# অগ্রাধিকার সংক্রান্ত অনুমান

বিবরণ: প্রায়োরিটি ইনফারেন্স টিয়ারের মাধ্যমে কীভাবে লেটেন্সি অপ্টিমাইজ করতে হয় তা জানুন

Gemini Priority API হল একটি প্রিমিয়াম ইনফারেন্স টিয়ার যা
ব্যবসায়িক-গুরুত্বপূর্ণ ওয়ার্কলোডের জন্য ডিজাইন করা হয়েছে। এর জন্য কম লেটেন্সি ও প্রিমিয়াম
প্রাইস পয়েন্টে সবচেয়ে বেশি নির্ভরযোগ্যতা প্রয়োজন। অগ্রাধিকার টিয়ার ট্রাফিককে স্ট্যান্ডার্ড API এবং
ফ্লেক্স টিয়ার ট্রাফিকের উপরে অগ্রাধিকার দেওয়া হয়।

GenerateContent API
ও Interactions API এন্ডপয়েন্ট জুড়ে [লেভেল ২ ও লেভেল ৩](https://ai.google.dev/gemini-api/docs/billing?hl=bn#about-billing) ব্যবহারকারীদের জন্য প্রায়োরিটি ইনফারেন্স উপলভ্য।

## কীভাবে প্রায়োরিটি ব্যবহার করতে হয়

প্রায়োরিটি টিয়ার ব্যবহার করতে, অনুরোধের বডিতে `service_tier` ফিল্ডটি
`priority`-এ সেট করুন। ফিল্ডটি বাদ দেওয়া হলে ডিফল্ট টিয়ার স্ট্যান্ডার্ড হিসেবে সেট করা হয়।

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### জাভাস্ক্রিপ্ট

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3.8-flash",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
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
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## অগ্রাধিকার অনুমান কীভাবে কাজ করে

অগ্রাধিকার ইনফারেন্স, অনুরোধগুলিকে অত্যন্ত গুরুত্বপূর্ণ কম্পিউট কিউতে রুট করে, যা ব্যবহারকারী নিজে ইন্টার‌্যাক্ট করতে পারেন এমন অ্যাপ্লিকেশনের জন্য
অনুমানযোগ্য, দ্রুত পারফর্ম্যান্স অফার করে। এর প্রাথমিক
মেকানিজম হল, ডাইনামিক সীমা অতিক্রম করা ট্রাফিকের জন্য স্ট্যান্ডার্ড প্রসেসিংয়ে
সার্ভার-সাইড ডাউনগ্রেড করা, যাতে অনুরোধ ব্যর্থ না হয়ে অ্যাপ্লিকেশন
স্থিতিশীল থাকে।

| ফিচার | অগ্রাধিকার | মানক | ফ্লেক্স | ব্যাচ |
| --- | --- | --- | --- | --- |
| **দাম** | স্ট্যান্ডার্ডের চেয়ে ৭৫-১০০% বেশি | সম্পূর্ণ দাম | ৫০% ছাড় | ৫০% ছাড় |
| **লেটেন্সি** | সেকেন্ড | সেকেন্ড থেকে মিনিট | মিনিট (১–১৫ মিনিটের লক্ষ্য) | ২৪ ঘণ্টা পর্যন্ত |
| **নির্ভরযোগ্যতা** | বেশি (নন-শেডেবল) | বেশি / মাঝারি-বেশি | সামঞ্জস্যপূর্ণ প্রচেষ্টা (শেডেবল) | বেশি (থ্রুপুটের জন্য) |
| **ইন্টারফেস** | সিঙ্ক্রোনাস | সিনক্রোনাস | সিনক্রোনাস | অসমনিয়ত |

### প্রধান সুবিধা

- **কম লেটেন্সি**: ইন্ট্যার‍্যাক্টিভ,
  ব্যবহারকারী-কেন্দ্রিক AI টুলের জন্য সেকেন্ডে উত্তর দেওয়ার সময়কে মাথায় রেখে ডিজাইন করা হয়েছে।
- **অত্যন্ত নির্ভরযোগ্য**: ট্রাফিককে সবচেয়ে বেশি গুরুত্ব দেওয়া হয় এবং
  সেটি কোনওভাবেই বাদ দেওয়া যায় না।
- **গ্রেসফুল ডিগ্রেডেশন**: ট্রাফিক স্পাইক ডায়নামিক সীমা অতিক্রম করলে,
  প্রসেস করার জন্য অটোমেটিক স্ট্যান্ডার্ড টিয়ারে ডাউনগ্রেড করা হয়,
  যাতে পরিষেবা বন্ধ না হয়।
- **কম ঘর্ষণ**: স্ট্যান্ডার্ড ও Flex টিয়ারের মতো একই সিঙ্ক্রোনাস `generateContent` পদ্ধতি ব্যবহার করে।

### যেসব ক্ষেত্রে ব্যবহার করা যাবে

যেসব ব্যবসায়িক-গুরুত্বপূর্ণ ওয়ার্কফ্লোতে পারফর্ম্যান্স
ও নির্ভরযোগ্যতা সবচেয়ে গুরুত্বপূর্ণ, সেগুলির জন্য অগ্রাধিকার ভিত্তিক প্রসেসিং আদর্শ।

- **ইন্টার‍্যাক্টিভ AI অ্যাপ্লিকেশন**: গ্রাহক পরিষেবা চ্যাটবট ও কোপাইলট যেখানে
  ব্যবহারকারীরা প্রিমিয়াম পেমেন্ট করেন এবং দ্রুত, ধারাবাহিক উত্তর আশা করেন।
- **রিয়েল-টাইম সিদ্ধান্ত গ্রহণকারী ইঞ্জিন**: লাইভ টিকিট ট্রায়াজ বা জালিয়াতি শনাক্তকরণের মতো অত্যন্ত নির্ভরযোগ্য, কম লেটেন্সি
  ফলাফল প্রয়োজন এমন সিস্টেম।
- **প্রিমিয়াম গ্রাহক ফিচার**: যেসব ডেভেলপারকে পেমেন্ট করা গ্রাহকদের জন্য আরও বেশি পরিষেবা স্তরের উদ্দেশ্য (SLO)
  গ্যারান্টি দিতে হয়।

### রেটের সীমা

[সামগ্রিক ইন্ট্যার‍্যাক্টিভ ট্রাফিক রেট লিমিটের](https://aistudio.google.com/rate-limit?hl=bn) মধ্যে গণনা করা হলেও, অগ্রাধিকার ভিত্তিক ব্যবহারের নিজস্ব রেট লিমিট থাকে। অগ্রাধিকার ইনফারেন্সের জন্য ডিফল্ট রেট লিমিট হল
**মডেল / টিয়ারের জন্য স্ট্যান্ডার্ড রেট লিমিটের ০.৩ গুণ**

### সাবলীল ডাউনগ্রেড লজিক

কনজেশন হওয়ার কারণে প্রায়োরিটি সীমা পেরিয়ে গেলে, ওভারফ্লো অনুরোধ 503 বা 429 সমস্যার কারণে
ব্যর্থ হওয়ার পরিবর্তে স্ট্যান্ডার্ড প্রসেসিংয়ে
**অটোমেটিক ও সুন্দরভাবে** ডাউনগ্রেড করা হয়। ডাউনগ্রেড করা অনুরোধের জন্য স্ট্যান্ডার্ড রেটে বিল করা হয়, প্রায়োরিটি প্রিমিয়াম রেটে নয়।

### ক্লায়েন্টের দায়িত্ব

- **প্রতিক্রিয়া মনিটর করা**: API প্রতিক্রিয়ায় ডেভেলপারদের `x-gemini-service-tier`
  হেডার মনিটর করা উচিত যাতে অনুরোধ ঘনঘন ডাউনগ্রেড হয়ে
  `standard`-এ পরিণত হচ্ছে কিনা তা শনাক্ত করা যায়।
- **আবার চেষ্টা করা**: ক্লায়েন্টদের অবশ্যই স্ট্যান্ডার্ড এররের জন্য আবার চেষ্টা করার লজিক/এক্সপোনেনশিয়াল ব্যাকঅফ প্রয়োগ করতে হবে, যেমন `DEADLINE_EXCEEDED`।

## দাম

প্রিফিক্স ইনফারেন্সের দাম [স্ট্যান্ডার্ড API](https://ai.google.dev/gemini-api/docs/pricing?hl=bn)-এর চেয়ে ৭৫-১০০% বেশি এবং টোকেন পিছু বিল করা হয়।

## যেসব মডেলে কাজ করে

নিম্নলিখিত মডেলগুলি প্রায়োরিটি ইনফারেন্স সাপোর্ট করে:

| মডেল | অগ্রাধিকার অনুমান |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=bn) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=bn) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=bn) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=bn) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=bn) | ✔️ |
| [Gemini 3.1 Pro প্রিভিউ](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=bn) | ✔️ |
| [Gemini 3 Flash প্রিভিউ](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=bn) | ✔️ |
| [Gemini 3 Pro ইমেজ প্রিভিউ](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=bn) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=bn) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=bn) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=bn) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=bn) | ✔️ |

## এর পরে কী করতে হবে

Gemini-র অন্যান্য [ইনফারেন্স ও অপ্টিমাইজেশন](https://ai.google.dev/gemini-api/docs/optimization?hl=bn) বিকল্প সম্পর্কে পড়ুন:

- খরচ ৫০% কমানোর জন্য [Flex inference](https://ai.google.dev/gemini-api/docs/flex-inference?hl=bn)।
- ২৪ ঘণ্টার মধ্যে অ্যাসিঙ্ক্রোনাস প্রসেসিংয়ের জন্য [ব্যাচ API](https://ai.google.dev/gemini-api/docs/batch-api?hl=bn)।
- ইনপুট টোকেনের খরচ কমানোর জন্য [কন্টেক্সট ক্যাশিং](https://ai.google.dev/gemini-api/docs/caching?hl=bn)।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-13 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-13 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
