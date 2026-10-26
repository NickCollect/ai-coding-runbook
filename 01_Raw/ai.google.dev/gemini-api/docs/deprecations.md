---
source_url: https://ai.google.dev/gemini-api/docs/deprecations?hl=bn
fetched_at: 2026-10-26T05:56:15.284341+00:00
title: "Gemini-\u09a4\u09c7 \u09ac\u09a8\u09cd\u09a7 \u09b9\u09df\u09c7 \u09af\u09be\u0993\u09df\u09be \u09ab\u09bf\u099a\u09be\u09b0 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# Gemini-তে বন্ধ হয়ে যাওয়া ফিচার

এই পৃষ্ঠায় [স্টেবল (GA)](https://ai.google.dev/gemini-api/docs/models?hl=bn#stable) ও [প্রিভিউ](https://ai.google.dev/gemini-api/docs/models?hl=bn#preview) মডেল এবং Gemini API-তে ম্যানেজ করা এজেন্টের জন্য
পরিচিত ডেপ্রিকেশন শিডিউল তালিকাভুক্ত করা আছে। "**বন্ধ করা**" হল
এমন ঘোষণা যার মাধ্যমে জানানো হয় যে আমরা কোনও মডেলের জন্য আর সহায়তা প্রদান করব না এবং অদূর ভবিষ্যতে এটি
"**বন্ধ করে দেওয়া**" হবে। কোনও মডেল "**বন্ধ**" হয়ে গেলে, সেটি
সম্পূর্ণভাবে বন্ধ হয়ে যায় এবং এন্ডপয়েন্ট আর উপলভ্য থাকে না।

বন্ধ করার ঘোষণা
[রিলিজ নোট](https://ai.google.dev/gemini-api/docs/changelog?hl=bn) পৃষ্ঠায় করা হয় এবং বন্ধ করার সবচেয়ে প্রথম
তারিখ এই পৃষ্ঠায় ট্র্যাক করা হয়।
ইতিমধ্যে বন্ধ হয়ে যাওয়া মডেলগুলি ধূসর ব্যাকগ্রাউন্ড দিয়ে চিহ্নিত করা হয়।

## Gemini 3 মডেল

| **মডেল** | **রিলিজের তারিখ** | **বন্ধ করার তারিখ** | **বদলে ফেলার সাজেশন** |
| --- | --- | --- | --- |
| `gemini-3.8-flash-tts` | সেপ্টেম্বর 22, 2026 | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-3.8-flash-lite-tts` | সেপ্টেম্বর 22, 2026 | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-3.8-live` | সেপ্টেম্বর 15, 2026 | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-3.8-live-extended-thinking` | সেপ্টেম্বর 15, 2026 | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-3.8-flash` | সেপ্টেম্বর 2, 2026 | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-3.7-flash` | ১৩ আগস্ট, ২০২৬ | প্রযোজ্য নয় | `gemini-3.8-flash` (Google AI Studio-তে বেছে নেওয়ার জন্য উপলভ্য নয়; এন্ডপয়েন্ট বন্ধ হচ্ছে না এবং API অনুরোধ অটোমেটিক `gemini-3.8-flash`-এ রাউট করে) |
| `gemini-3.6-flash` | ২১ জুলাই, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-3.5-flash-lite` | ২১ জুলাই, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-3.5-flash` | ১৯ মে, ২০২৬ | প্রযোজ্য নয় | `gemini-3.6-flash` (Google AI Studio-তে বেছে নেওয়ার জন্য উপলভ্য নয়; এন্ডপয়েন্ট বন্ধ হচ্ছে না এবং API অনুরোধ অটোমেটিক `gemini-3.6-flash`-এ রাউট করে) |
| `gemini-3.1-flash-lite` | ৭ মে, ২০২৬ | ৭ মে, ২০২৭ | `gemini-3.5-flash-lite` |
| মডেল প্রিভিউ করুন | | | |
| `gemini-3.1-flash-tts-preview` | ২৬ ফেব্রুয়ারি, ২০২৬ | ১৭ নভেম্বর, ২০২৬ | `gemini-3.8-flash-tts` বা `gemini-3.8-flash-lite-tts` |
| `gemini-3.1-pro-preview` | ১৯ ফেব্রুয়ারি, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-3-flash-preview` | ১৭ ডিসেম্বর, ২০২৫ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি | `gemini-3.6-flash` |
| `gemini-3-pro-preview` | ১৮ নভেম্বর, ২০২৫ | ৯ মার্চ, ২০২৬ | `gemini-3.1-pro-preview` |
| `gemini-3.1-flash-lite-preview` | ৩ মার্চ, ২০২৬ | ২৫ মে, ২০২৬ | `gemini-3.1-flash-lite` |

## Gemini 2.5 Pro মডেল

| **মডেল** | **রিলিজের তারিখ** | **বন্ধ করার তারিখ** | **বদলে ফেলার সাজেশন** |
| --- | --- | --- | --- |
| `gemini-2.5-pro` | ১৭ জুন, ২০২৫ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| মডেল প্রিভিউ করুন | | | |
| `gemini-2.5-computer-use-preview-10-2025` | ৭ অক্টোবর, ২০২৫ | ২৮ জুলাই, ২০২৬ | `gemini-3.8-flash` |
| `gemini-2.5-pro-preview-03-25` | ৩ মার্চ, ২০২৫ | ২ ডিসেম্বর, ২০২৫ | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-05-06` | ৬ মে, ২০২৫ | ২ ডিসেম্বর, ২০২৫ | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-06-05` | ৫ জুন, ২০২৫ | ২ ডিসেম্বর, ২০২৫ | `gemini-3.1-pro-preview` |

## Gemini 2.5 Flash মডেল

| **মডেল** | **রিলিজের তারিখ** | **বন্ধ করার তারিখ** | **বদলে ফেলার সাজেশন** |
| --- | --- | --- | --- |
| `gemini-2.5-flash` | ১৭ জুন, ২০২৫ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-2.5-flash-lite` | ২২ জুলাই, ২০২৫ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| মডেল প্রিভিউ করুন | | | |
| `gemini-2.5-flash-lite-preview-09-2025` | ২৫ সেপ্টেম্বর, ২০২৫ | ৩১ মার্চ, ২০২৬ | `gemini-3.1-flash-lite` |
| `gemini-2.5-flash-preview-05-20` | ২০ মে, ২০২৫ | ১৮ নভেম্বর, ২০২৫ | `gemini-3.6-flash` |
| `gemini-2.5-flash-preview-09-25` | ২৫ সেপ্টেম্বর, ২০২৫ | ১৭ ফেব্রুয়ারি, ২০২৬ | `gemini-3.6-flash` |

## Gemini 2.0 মডেল

| **মডেল** | **রিলিজের তারিখ** | **বন্ধ করার তারিখ** | **বদলে ফেলার সাজেশন** |
| --- | --- | --- | --- |
| `gemini-2.0-flash` | ৫ ফেব্রুয়ারি, ২০২৫ | ১ জুন, ২০২৬ | `gemini-3.6-flash` |
| `gemini-2.0-flash-001` | ৫ ফেব্রুয়ারি, ২০২৫ | ১ জুন, ২০২৬ | `gemini-3.6-flash` |
| `gemini-2.0-flash-lite` | ২৫ ফেব্রুয়ারি, ২০২৫ | ১ জুন, ২০২৬ | `gemini-3.1-flash-lite` |
| `gemini-2.0-flash-lite-001` | ২৫ ফেব্রুয়ারি, ২০২৫ | ১ জুন, ২০২৬ | `gemini-3.1-flash-lite` |
| মডেল প্রিভিউ করুন | | | |
| `gemini-2.0-flash-lite-preview` | ৫ ফেব্রুয়ারি, ২০২৫ | ৯ ডিসেম্বর, ২০২৫ | `gemini-3.1-flash-lite` |
| `gemini-2.0-flash-lite-preview-02-05` | ৫ ফেব্রুয়ারি, ২০২৫ | ৯ ডিসেম্বর, ২০২৫ | `gemini-3.1-flash-lite` |

## Live API মডেল

| **মডেল** | **রিলিজের তারিখ** | **বন্ধ করার তারিখ** | **বদলে ফেলার সাজেশন** |
| --- | --- | --- | --- |
| `gemini-3.8-live` | সেপ্টেম্বর 15, 2026 | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-3.8-live-extended-thinking` | সেপ্টেম্বর 15, 2026 | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-3.5-transcribe-live` | আগস্ট ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-2.0-flash-live-001` | ৯ এপ্রিল, ২০২৫ | ৯ ডিসেম্বর, ২০২৫ | `gemini-3.8-live` |
| মডেল প্রিভিউ করুন | | | |
| `gemini-3.5-live-translate-preview` | জুন ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-3.1-flash-live-preview` | ১১ মার্চ, ২০২৬ | ১৭ নভেম্বর, ২০২৬ | `gemini-3.8-live` |
| `gemini-2.5-flash-native-audio-preview-12-2025` | ১২ ডিসেম্বর, ২০২৫ | ১৭ নভেম্বর, ২০২৬ | `gemini-3.8-live` |
| `gemini-live-2.5-flash-preview` | ১৭ জুন, ২০২৫ | ৯ ডিসেম্বর, ২০২৫ | `gemini-3.8-live` |

## অডিও মডেল

| **মডেল** | **রিলিজের তারিখ** | **বন্ধ করার তারিখ** | **বদলে ফেলার সাজেশন** |
| --- | --- | --- | --- |
| `gemini-3.5-transcribe` | আগস্ট ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| মডেল প্রিভিউ করুন | | | |
| `gemini-2.5-flash-preview-tts` | ২০ মে, ২০২৫ | ১৭ নভেম্বর, ২০২৬ | `gemini-3.8-flash-tts` বা `gemini-3.8-flash-lite-tts` |
| `gemini-2.5-pro-preview-tts` | ২০ মে, ২০২৫ | ১৭ নভেম্বর, ২০২৬ | `gemini-3.8-flash-tts` বা `gemini-3.8-flash-lite-tts` |

## এম্বেডিং মডেল

| **মডেল** | **রিলিজের তারিখ** | **বন্ধ করার তারিখ** | **বদলে ফেলার সাজেশন** |
| --- | --- | --- | --- |
| `gemini-embedding-2` | ২২ এপ্রিল, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-embedding-001` | ১৪ জুলাই, ২০২৫ | ১৪ মে, ২০২৮ | `gemini-embedding-2` |
| `text-embedding-004` | ৯ এপ্রিল, ২০২৪ | ১৪ জানুয়ারি, ২০২৬ | `gemini-embedding-2` |
| মডেল প্রিভিউ করুন | | | |
| `embedding-2-preview` | ১০ মার্চ, ২০২৬ | ১০ আগস্ট, ২০২৬ | `gemini-embedding-2` |
| `embedding-001` | ৯ এপ্রিল, ২০২৪ | ৩০ অক্টোবর, ২০২৫ | `gemini-embedding-2` |
| `embedding-gecko-001` |  | ৩০ অক্টোবর, ২০২৫ | `gemini-embedding-2` |
| `gemini-embedding-exp` |  | ৩০ অক্টোবর, ২০২৫ | `gemini-embedding-2` |
| `gemini-embedding-exp-03-07` |  | ৩০ অক্টোবর, ২০২৫ | `gemini-embedding-2` |

## Nano Banana মডেল

| **মডেল** | **রিলিজের তারিখ** | **বন্ধ করার তারিখ** | **বদলে ফেলার সাজেশন** |
| --- | --- | --- | --- |
| `gemini-nano-banana-2.1` | ৬ অক্টোবর, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-3.1-flash-lite-image` | ৩০ জুন, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-3.1-flash-image` | ২৮ মে, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি | `gemini-nano-banana-2.1` |
| `gemini-3-pro-image` | ২৮ মে, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-2.5-flash-image` | ২ অক্টোবর, ২০২৫ | ১৫ মার্চ, ২০২৭ | `gemini-3.1-flash-lite-image` |
| মডেল প্রিভিউ করুন | | | |
| `gemini-3.1-flash-image-preview` | ২৬ ফেব্রুয়ারি, ২০২৬ | ২৫ জুন, ২০২৬ | `gemini-nano-banana-2.1` |
| `gemini-3-pro-image-preview` | ২০ নভেম্বর, ২০২৫ | ২৫ জুন, ২০২৬ | `gemini-3-pro-image` |
| `gemini-2.5-flash-image-preview` | ৭ মে, ২০২৫ | ১৫ জানুয়ারি, ২০২৬ | `gemini-nano-banana-2.1` |
| `gemini-2.0-flash-preview-image-generation` | ৭ মে, ২০২৫ | ১৪ নভেম্বর, ২০২৫ | `gemini-nano-banana-2.1` |

## Imagen মডেল

| **মডেল** | **রিলিজের তারিখ** | **বন্ধ করার তারিখ** | **বদলে ফেলার সাজেশন** |
| --- | --- | --- | --- |
| `imagen-4.0-generate-001` | ২৪ জুন, ২০২৫ | ১৭ আগস্ট, ২০২৬ | `gemini-nano-banana-2.1` |
| `imagen-4.0-ultra-generate-001` | ২৪ জুন, ২০২৫ | ১৭ আগস্ট, ২০২৬ | `gemini-nano-banana-2.1` |
| `imagen-4.0-fast-generate-001` | ২৪ জুন, ২০২৫ | ১৭ আগস্ট, ২০২৬ | `gemini-nano-banana-2.1` |
| `imagen-3.0-generate-002` | ৬ ফেব্রুয়ারি, ২০২৫ | ১০ নভেম্বর, ২০২৫ | `gemini-nano-banana-2.1` |
| মডেল প্রিভিউ করুন | | | |
| `imagen-4.0-generate-preview-06-06` | ২৪ জুন, ২০২৫ | ১৭ ফেব্রুয়ারি, ২০২৬ | `gemini-nano-banana-2.1` |
| `imagen-4.0-ultra-generate-preview-06-06` | ২৪ জুন, ২০২৫ | ১৭ ফেব্রুয়ারি, ২০২৬ | `gemini-nano-banana-2.1` |

## Veo মডেল

| **মডেল** | **রিলিজের তারিখ** | **বন্ধ করার তারিখ** | **বদলে ফেলার সাজেশন** |
| --- | --- | --- | --- |
| `veo-3.0-generate-001` | ৯ সেপ্টেম্বর, ২০২৫ | ৩০ জুন, ২০২৬ | `gemini-omni-1.1-flash` অথবা [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=bn)-এ GA মডেল |
| `veo-3.0-fast-generate-001` | ৯ সেপ্টেম্বর, ২০২৫ | ৩০ জুন, ২০২৬ | `gemini-omni-1.1-flash` অথবা [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=bn)-এ GA মডেল |
| `veo-2.0-generate-001` | ৯ এপ্রিল, ২০২৫ | ৩০ জুন, ২০২৬ | `gemini-omni-1.1-flash` অথবা [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=bn)-এ GA মডেল |
| মডেল প্রিভিউ করুন | | | |
| `veo-3.1-lite-generate-preview` | ৩১ মার্চ, ২০২৬ | ২২ অক্টোবর, ২০২৬ | `gemini-omni-1.1-flash` |
| `veo-3.1-generate-preview` | ১৫ অক্টোবর, ২০২৫ | ২২ অক্টোবর, ২০২৬ | `gemini-omni-1.1-flash` |
| `veo-3.1-fast-generate-preview` | ১৫ অক্টোবর, ২০২৫ | ২২ অক্টোবর, ২০২৬ | `gemini-omni-1.1-flash` |
| `veo-3.0-generate-preview` | ৩১ জুলাই, ২০২৫ | ১২ নভেম্বর, ২০২৫ | `gemini-omni-1.1-flash` |
| `veo-3.0-fast-generate-preview` | ৩১ জুলাই, ২০২৫ | ১২ নভেম্বর, ২০২৫ | `gemini-omni-1.1-flash` |

## Gemini Omni Flash মডেল

| **মডেল** | **রিলিজের তারিখ** | **বন্ধ করার তারিখ** | **বদলে ফেলার সাজেশন** |
| --- | --- | --- | --- |
| `gemini-omni-1.1-flash` | ২৭ আগস্ট, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| মডেল প্রিভিউ করুন | | | |
| `gemini-omni-flash-preview` | ৩০ জুন, ২০২৬ | ২২ অক্টোবর, ২০২৬ | `gemini-omni-1.1-flash` |

## Lyria মডেল

| **মডেল** | **রিলিজের তারিখ** | **বন্ধ করার তারিখ** | **বদলে ফেলার সাজেশন** |
| --- | --- | --- | --- |
| `lyria-3.5` | সেপ্টেম্বর 3, 2026 | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| মডেল প্রিভিউ করুন | | | |
| `lyria-3-clip-preview` | ২৫ মার্চ, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `lyria-3-pro-preview` | ২৫ মার্চ, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি | `lyria-3.5` |
| `lyria-realtime-exp` | ২০ মে, ২০২৫ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |

## রোবোটিক্স মডেল

| **মডেল** | **রিলিজের তারিখ** | **বন্ধ করার তারিখ** | **বদলে ফেলার সাজেশন** |
| --- | --- | --- | --- |
| মডেল প্রিভিউ করুন | | | |
| `gemini-robotics-er-2-preview` | ৩০ জুলাই, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-robotics-er-2-streaming-preview` | ৩০ জুলাই, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `gemini-robotics-er-1.6-preview` | ১৪ এপ্রিল, ২০২৬ | আগস্ট 31, 2026 | `gemini-robotics-er-2-preview` |
| `gemini-robotics-er-1.5-preview` | ২৫ সেপ্টেম্বর, ২০২৫ | ৩০ এপ্রিল, ২০২৬ | `gemini-robotics-er-2-preview` |

## ম্যানেজ করা এজেন্ট

| **Agent** | **রিলিজের তারিখ** | **বন্ধ করার তারিখ** | **বদলে ফেলার সাজেশন** |
| --- | --- | --- | --- |
| এজেন্ট প্রিভিউ করুন | | | |
| `antigravity-preview-09-2026` | সেপ্টেম্বর 17, 2026 | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `deep-research-preview-04-2026` | ২১ এপ্রিল, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `deep-research-max-preview-04-2026` | ২১ এপ্রিল, ২০২৬ | বন্ধ করার কোনও তারিখ ঘোষণা করা হয়নি |  |
| `deep-research-pro-preview-12-2025` | ১১ ডিসেম্বর, ২০২৫ | ২৩ অক্টোবর, ২০২৬ | `deep-research-preview-04-2026` |
| `antigravity-preview-05-2026` | ১৯ মে, ২০২৬ | ৫ অক্টোবর, ২০২৬ | `antigravity-preview-09-2026` |

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-22 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-22 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
