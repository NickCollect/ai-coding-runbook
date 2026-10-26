---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=bn
fetched_at: 2026-10-26T05:57:23.403706+00:00
title: "\u09b0\u09bf\u09b2\u09bf\u099c \u09a8\u09cb\u099f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# রিলিজ নোট

এই পৃষ্ঠায় Gemini API-তে করা আপডেট সম্পর্কে ডকুমেন্টেশন রয়েছে।

## ১৩ অক্টোবর, ২০২৬

- **Gemini 4 Argon (`gemini-4-argon`) জেনেরাল অ্যাভেইলেবিলিটি (GA)**: রিলিজ করা হয়েছে
  [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=bn) (`gemini-4-argon`),
  জটিল কোডিং, এজেন্টিক, গণিত ও বিজ্ঞান সংক্রান্ত
  টাস্কের জন্য তৈরি আমাদের সবচেয়ে দক্ষ মডেল।

  API পরিবর্তন, মূল্য এবং মাইগ্রেশন সংক্রান্ত নির্দেশিকা পেতে,
  [Gemini 4 Argon-এ নতুন কী আছে](https://ai.google.dev/gemini-api/docs/latest-model?hl=bn) দেখুন।

## ৮ অক্টোবর, ২০২৬

- **Gemini 3.7 Flash বন্ধ হয়ে যাওয়া**:
  [`gemini-3.7-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.7?hl=bn) বন্ধ হয়ে গেছে
  এবং এর পরিবর্তে [`gemini-3.8-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=bn) এসেছে।
  Google AI Studio-তে এটি আর বেছে নেওয়ার জন্য উপলভ্য নেই এবং `gemini-3.7-flash`-এ API অনুরোধ
  অটোমেটিক `gemini-3.8-flash`-এ রাউট করা হয়। আপনার মডেল স্ট্রিং
  `gemini-3.8-flash`-এ আপডেট করুন এবং
  [Gemini 3.8 Flash গাইড](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=bn) পর্যালোচনা করুন।
- **Gemini 3.5 Flash বন্ধ হয়ে যাওয়া**:
  [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=bn) বন্ধ হয়ে গেছে
  এবং এর পরিবর্তে [`gemini-3.6-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=bn) এসেছে।
  Google AI Studio-তে এটি আর বেছে নেওয়ার জন্য উপলভ্য নেই এবং
  `gemini-3.5-flash`-তে API অনুরোধ অটোমেটিক `gemini-3.6-flash`-তে রাউট করা হয়। আপনার মডেল স্ট্রিং `gemini-3.6-flash` (বা
  [`gemini-3.8-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=bn))-এ
  আপডেট করুন এবং [Gemini 3.6 Flash গাইড](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=bn)
  ভালো করে দেখে নিন।
- **Deep Research Agent `deep-research-pro-preview-12-2025` বন্ধ করা**:
  `deep-research-pro-preview-12-2025` এজেন্ট বন্ধ করা হয়েছে এবং
  **২৩ অক্টোবর,
  ২০২৬**-এ [বন্ধ করে দেওয়া হবে](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn#managed-agents)।

  আপনার অনুরোধ নতুন [Deep
  Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=bn) এজেন্ট ভার্সনে মাইগ্রেট করুন:

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=bn):
    দ্রুততা ও কার্যকারিতার জন্য ডিজাইন করা হয়েছে, ক্লায়েন্ট UI-তে স্ট্রিম করার জন্য আদর্শ।
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=bn):
    অটোমেটিক প্রসঙ্গ সংগ্রহ ও সিন্থেসিসের জন্য সর্বাধিক ব্যাপকতা।

  মাইগ্রেট করতে, আপনার `interactions.create`-এ `agent` প্যারামিটার আপডেট করুন
  `deep-research-pro-preview-12-2025` থেকে
  `deep-research-preview-04-2026` (বা `deep-research-max-preview-04-2026`) পর্যন্ত অনুরোধ।

## ৬ অক্টোবর, ২০২৬

- **Gemini Nano Banana 2.1 জেনারেলি অ্যাভেলেবেল (GA)**: রিলিজ করা হয়েছে
  [Gemini Nano Banana 2.1](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1?hl=bn)
  (`gemini-nano-banana-2.1`), লেটেস্ট হাই-এফিশিয়েন্সি ইমেজ জেনারেশন এবং
  কনভারসেশনাল এডিটিং মডেল। Nano Banana 2
  ([`gemini-3.1-flash-image`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=bn))-এর আপডেট,
  এটি Flash-লেভেল স্পিড ও খরচ সাশ্রয় বজায় রাখার পাশাপাশি
  ভিজ্যুয়াল কোয়ালিটি, প্রম্পট মেনে চলা, মাল্টি-টার্ন
  ক্যারেক্টার কনসিস্টেন্সি, টেক্সট রেন্ডারিং এবং `1K`, `2K` ও `4K`
  রেজোলিউশন জুড়ে ওয়াইড ও প্যানোরামিক অ্যাস্পেক্ট রেশিও
  জেনারেট (`1:4`, `4:1`, `1:8`, `8:1`) করার ক্ষেত্রে উল্লেখযোগ্য উন্নতি করে।

  শুরু করতে [ইমেজ জেনারেশন গাইড](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn) দেখুন।
- **বন্ধ করে দেওয়ার ঘোষণা**: `gemini-3.1-flash-image` মডেলটি
  বন্ধ করে দেওয়া হয়েছে (বন্ধ করার তারিখ ঘোষণা করা হয়নি)। [`gemini-nano-banana-2.1`](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1?hl=bn)-এ
  মাইগ্রেট করুন।

## সেপ্টেম্বর 22, 2026

- **Gemini 3.8 Flash TTS এবং Gemini 3.8 Flash-Lite TTS সাধারণত উপলভ্য
  (GA)**: আমাদের নেক্সট-জেনারেশন টেক্সট-টু-স্পিচ (TTS) অডিও মডেল এবং
  Gemini API Voices এন্ডপয়েন্ট (`/v1beta/voices`) রিলিজ করা হয়েছে:

  - **[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=bn)
    (`gemini-3.8-flash-tts`)**: স্টুডিও-গ্রেড ভয়েস ফিডেলিটি, সূক্ষ্ম অভিনয়, আঞ্চলিক উপভাষা এবং
    দীর্ঘ-ফর্ম মাল্টি-টার্ন স্থিতিশীলতার জন্য তৈরি করা ফ্ল্যাগশিপ ক্রিয়েটিভ TTS মডেল।
  - **[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=bn)
    (`gemini-3.8-flash-lite-tts`)**: দ্রুত, সাশ্রয়ী TTS মডেল যা হাই-থ্রুপুট প্রোডাকশন এবং রিয়েল-টাইম ভয়েস এজেন্ট ক্যাসকেডের জন্য `gemini-3.1-flash-tts-preview`-এর পরিবর্তে ব্যবহার করার জন্য তৈরি করা হয়েছে।
  - **[ভয়েস ডিজাইন](https://ai.google.dev/gemini-api/docs/voice-design?hl=bn),
    [ভয়েস রেপ্লিকেশন](https://ai.google.dev/gemini-api/docs/voice-replication?hl=bn) এবং
    [এক্সটেন্ডেড ভয়েস লাইব্রেরি](https://ai.google.dev/gemini-api/docs/speech-generation?hl=bn#voice-library)**:
    টেক্সট প্রম্পট থেকে স্থায়ী কাস্টম ভোকাল পার্সোনা তৈরি করুন, সম্মতি যাচাইকরণের মাধ্যমে
    ভয়েস রেপ্লিকেট করুন এবং ১৫০টিরও বেশি আগে থেকে তৈরি করা ও কাস্টম
    ভয়েস কোয়েরি করুন।

  শুরু করতে [টেক্সট-টু-স্পিচ নির্দেশিকা](https://ai.google.dev/gemini-api/docs/speech-generation?hl=bn)
  দেখুন।

## সেপ্টেম্বর 18, 2026

- **Gemini 2.5 মডেল অ্যাক্সেস সংক্রান্ত আপডেট**: সকলের জন্য
  নির্ভরযোগ্য পারফর্ম্যান্স নিশ্চিত করতে, আমরা 2.5 মডেলের অ্যাক্সেস সেইসব ব্যবহারকারীদের মধ্যে সীমাবদ্ধ করছি যারা
  অতীতে সেগুলি অ্যাক্টিভভাবে ব্যবহার করেছেন। এইসব মডেল আর ব্যবহার করা হয় না এবং API-এর মাধ্যমে পরবর্তী বিজ্ঞপ্তি না আসা পর্যন্ত এগুলি
  পরিবেশন করা চালিয়ে যাওয়া হবে। যেকোনও নতুন
  প্রোজেক্টের জন্য, আমাদের লেটেস্ট মডেল ব্যবহার করুন: 3.5 Flash-Lite বা 3.8 Flash. এর ফলে
  চলমান পুরনো ওয়ার্কফ্লো এবং
  নতুন অ্যাপ্লিকেশনের জন্য পর্যাপ্ত ক্যাপাসিটি বজায় রাখতে পারি।

## ১৭ সেপ্টেম্বর, ২০২৬

- **Antigravity Agent 09-2026**: রিলিজ করা হয়েছে `antigravity-preview-09-2026`,
  যা `antigravity-preview-05-2026`-এর পরিবর্তে ব্যবহার করা হয় এবং -এর ব্যবহার বন্ধ করা হয়েছে।

  আপনি যদি রিমোট স্যান্ডবক্সে (`environment: "remote"`) রান করেন এবং শুধুমাত্র
  `output_text` বা `model_output` ধাপ পড়েন, তাহলে এজেন্ট স্ট্রিং আপডেট করুন এবং অন্য কিছু
  পরিবর্তন করবেন না।

  আপনি লোকালি টুল (`local_environment`) রান করালে অথবা `function_call`
  ধাপ পার্স করলে, বিল্ট-ইন টুল পরিবর্তন হয়ে যায়। প্যারামিটার snake\_case-এর পরিবর্তে PascalCase ব্যবহার করে এবং ফাইল এডিট সম্পূর্ণভাবে আবার লেখার পরিবর্তে লাইন-রেঞ্জ রিপ্লেসমেন্ট ব্যবহার করে।

  | ক্ষমতা | 05-2026 | 09-2026 |
  | --- | --- | --- |
  | ফাইল তৈরি করা | `write_file(path, content)` | `write_to_file(TargetFile, CodeContent, Overwrite, Description)` |
  | ফাইল এডিট করা | `write_file(path, content)`, সম্পূর্ণ আবার লিখুন | `replace_file_content(TargetFile, StartLine, EndLine, TargetContent, ReplacementContent)` |
  | ফাইল রিডিং | `read_file(path, offset, limit)`, বাইট অফসেট | `view_file(AbsolutePath, StartLine, EndLine, ContentOffset)` |
  | ডিরেক্টরি লিস্টিং | `list_files(path)` | `list_dir(DirectoryPath)` |
  | ফাইল ও কোড সার্চ | কিছুই না, এজেন্ট শেল কমান্ড ব্যবহার করেছে | `find_by_name(SearchDirectory, Pattern, MaxDepth)` ও `grep_search(SearchPath, Query, IsRegex)` |
  | Shell এক্সিকিউশন | `code_execution(command, timeout_seconds)` | অপরিবর্তিত রয়েছে |
  | ওয়েব সার্চ | `google_search(queries)` | পরিবর্তিত হয়নি |

  [Antigravity এজেন্ট](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=bn) গাইড দেখুন।
  ৫ অক্টোবর, ২০২৬-এ `antigravity-preview-05-2026` বন্ধ হয়ে যাবে, এটি
  [বন্ধ হয়ে যাওয়া](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn#managed-agents) পৃষ্ঠায় ট্র্যাক করা হয়।

## সেপ্টেম্বর 15, 2026

- **Gemini 3.8 Live এবং Gemini 3.8 Live এক্সটেন্ডেড থিঙ্কিং সাধারণত উপলভ্য
  (GA)**: Live API ব্যবহার করে রিয়েল-টাইম ভয়েস অ্যাপ্লিকেশনের জন্য দুটি নতুন অডিও-টু-অডিও মডেল রিলিজ করা হয়েছে:

  - **Gemini 3.8 Live** ([`gemini-3.8-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=bn)): বেশিরভাগ কম-লেটেন্সি ভয়েস এজেন্ট অভিজ্ঞতা
    এবং রিজনিংয়ের কারণে দেরি না করে রিয়েল-টাইম ডায়ালগের জন্য
    ডিফল্ট বিকল্প। এতে ইন্টারলিভড রিজনিং, ডিফল্ট
    অ্যাসিঙ্ক্রোনাস ফাংশন কলিং এবং সম্পূর্ণ সেশন ক্লায়েন্ট কন্টেন্ট আপডেট করার সুবিধা রয়েছে।
  - **Gemini 3.8 Live Extended Thinking**
    ([`gemini-3.8-live-extended-thinking`](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=bn)): হাই-রিজনিং
    অডিও-টু-অডিও মডেল যা লাইভ অডিও ইন্টার‍্যাকশনের সময় ব্যাকগ্রাউন্ড রিজনিংয়ে সাহায্য করে, ব্যাকগ্রাউন্ড রিজনিংয়ের বেশি প্রয়োজন হলে এটি ব্যবহার করার সাজেশন দেওয়া হয়।

  শুরু করতে, [Live API গাইড](https://ai.google.dev/gemini-api/docs/live-api?hl=bn),
  [ক্ষমতা সংক্রান্ত গাইড](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=bn) এবং
  [চিন্তাভাবনা সংক্রান্ত গাইড](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=bn) দেখুন।

## সেপ্টেম্বর 3, 2026

- **Lyria 3.5 জেনেরাল অ্যাভেইলেবিলিটি (GA)**: Google-এর মিউজিক জেনারেশন মডেলের
  পরবর্তী জেনারেশন রিলিজ করা হয়েছে:

  - [`lyria-3.5`](https://ai.google.dev/gemini-api/docs/models/lyria-3.5?hl=bn):
    উন্নত মিউজিক্যাল কোহেরেন্স, স্বাভাবিক ভোকাল এবং
    সূক্ষ্ম-গ্রেনড ডিউরেশন ও স্ট্রাকচারাল কন্ট্রোল সহ সম্পূর্ণ দৈর্ঘ্যের গান তৈরি করা।

  মডেলটি টেক্সট ও ছবি ইনপুট হিসেবে নেয় এবং হাই-ফিডেলিটি ৪৪.১ kHz
  স্টিরিও অডিও তৈরি করে। বিস্তারিত তথ্য ও কোড স্যাম্পেলের জন্য
  [মিউজিক জেনারেশন](https://ai.google.dev/gemini-api/docs/music-generation?hl=bn) গাইড দেখুন।

## ২ সেপ্টেম্বর, ২০২৬

- **Gemini 3.8 Flash সাধারণভাবে উপলভ্য (GA)**: রিলিজ করা হয়েছে
  `gemini-3.8-flash`, আমাদের সবচেয়ে বুদ্ধিদীপ্ত Flash মডেল, যা
  লং-হরাইজন সফ্টওয়্যার ইঞ্জিনিয়ারিং, অটোনোমাস এজেন্ট এবং জটিল এন্টারপ্রাইজ
  ওয়ার্কফ্লোর জন্য তৈরি করা হয়েছে।

  শুরু করতে, [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=bn) মডেল পৃষ্ঠা এবং
  [Gemini 3.8 Flash গাইড](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=bn) দেখুন।

## সেপ্টেম্বর 1, 2026

- **এজেন্টিক ভিডিও বোঝা**: ইন্ট্যার‍্যাকশন ও
  GenerateContent API জুড়ে
  Gemini 3.7 Flash, 3.6 Flash ও 3.5 Flash-Lite-এর জন্য এজেন্টিক ভিডিও বোঝার সুবিধা রিলিজ করা হয়েছে। মডেলটি ভিডিও টাইমলাইন ডায়নামিক নেভিগেট করে,
  চাহিদা অনুযায়ী ট্রান্সক্রিপ্ট, ফ্রেম বা অডিও ট্র্যাকের অনুরোধ করে। এই পদ্ধতিতে স্ট্যাটিক প্রসেসিংয়ের তুলনায়
  বড় দৈর্ঘ্যের কন্টেন্টের জন্য ৮৮% পর্যন্ত কম টোকেন ব্যবহার করা হয়।

  শুরু করতে, [এজেন্টিক ভিডিও আন্ডারস্ট্যান্ডিং](https://ai.google.dev/gemini-api/docs/video-understanding?hl=bn#agentic-video-understanding) গাইড দেখুন।

## ২৭ আগস্ট, ২০২৬

- **Gemini Omni Flash জেনারেলি অ্যাভেলেবেল (GA)**: রিলিজ করা হয়েছে
  `gemini-omni-1.1-flash`, আমাদের দ্রুত, কথোপকথনমূলক ভিডিও
  জেনারেট ও এডিট করার মডেলের GA ভার্সন। এই রিলিজে উল্লেখযোগ্য নতুন
  ক্ষমতা অন্তর্ভুক্ত আছে:

  - **ভিডিও এক্সটেনশন**: `extend` টাস্ক ব্যবহার করে বা সরাসরি প্রম্পটের মাধ্যমে
    কোনও ক্লিপের শেষে কন্টিনিউয়েশন জেনারেট করে,
    আগে থেকে থাকা ভিডিও নির্বিঘ্নে এক্সটেন্ড করুন।
  - **ইন্টারপোলেশন (প্রথম + শেষ ফ্রেম)**: সর্বাধিক ২টি ছবি সহ `image_to_video` টাস্ক ব্যবহার করে
    দুটি ছবির মধ্যে ট্রানজিশন সহ একটি ভিডিও জেনারেট করুন।
  - **রেজোলিউশন কন্ট্রোল**: `video_config`-এ নতুন `resolution` প্যারামিটার
    `360p`, `720p` (ডিফল্ট), `1080p` এবং `4k` আউটপুট সাপোর্ট করে।
    আপস্কেলিং ব্যবহার করে 1080p ও 4K আউটপুট তৈরি করা হয়।

  আগে থেকে থাকা `gemini-omni-flash-preview` এন্ডপয়েন্ট ৩০ সেপ্টেম্বর, ২০২৬-এ বন্ধ হয়ে যাবে।

  শুরু করতে, [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=bn) মডেল পৃষ্ঠা
  এবং [omni নির্দেশিকা](https://ai.google.dev/gemini-api/docs/omni?hl=bn) দেখুন।

## ২৬ আগস্ট, ২০২৬

- **Gemini 3.5 Transcribe সাধারণভাবে উপলভ্য (GA)**: Gemini-র অডিও বোঝার ক্ষমতার উপর ভিত্তি করে দুটি ডেডিকেটেড
  স্পিচ-টু-টেক্সট মডেল রিলিজ করা হয়েছে:

  - **Gemini 3.5 Transcribe** (`gemini-3.5-transcribe`): ৮৫টিরও বেশি ভাষায় উচ্চারণ-ভিত্তিক ভাষা শনাক্তকরণ, স্পিকার ডায়েরাইজেশন, শব্দ-লেভেল টাইমস্ট্যাম্প এবং কাস্টম শব্দভাণ্ডার বায়াসিং (১,০০০টি শব্দ পর্যন্ত) সহ উচ্চ-নির্ভুলতা, কম-লেটেন্সি নন-স্ট্রিমিং স্পিচ-টু-টেক্সট।
  - **Gemini 3.5 Transcribe Live** (`gemini-3.5-transcribe-live`):
    লাইভ API ব্যবহার করে WebSockets-এর মাধ্যমে কম লেটেন্সি, দ্বিমুখী স্ট্রিমিং স্পিচ-টু-টেক্সট
    ফিচার, অন্তর্বর্তী ও চূড়ান্ত ট্রান্সক্রিপশন ইভেন্ট,
    স্মার্ট ট্রান্সক্রিপশন মোড এবং একাধিক ভয়েস অ্যাক্টিভিটি ডিটেকশন (VAD)
    স্ট্র্যাটেজি।

  শুরু করতে,
  [অডিও ট্রান্সক্রিপশন গাইড](https://ai.google.dev/gemini-api/docs/transcribe?hl=bn),
  [লাইভ ট্রান্সক্রিপশন গাইড](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=bn) এবং
  [Gemini 3.5 Transcribe মডেল পৃষ্ঠা](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=bn) দেখুন।

## ১৩ আগস্ট, ২০২৬

- **Gemini 3.7 Flash সাধারণভাবে উপলভ্য (GA)**: কোডিং ও এজেন্টের জন্য আমাদের সবচেয়ে
  ইন্টেলিজেন্ট ওয়ার্কহর্স মডেল রিলিজ করা হয়েছে:

  - **Gemini 3.7 Flash** (`gemini-3.7-flash`): সফটওয়্যার ইঞ্জিনিয়ারিং, ওয়েব ডেভেলপমেন্ট ও এজেন্টিক ওয়ার্কফ্লো জুড়ে উল্লেখযোগ্য উন্নতি, ৩১ ডিসেম্বর, ২০২৬ পর্যন্ত শুরুর দিকের দামে উপলভ্য।

  শুরু করতে, [Gemini 3.7 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash?hl=bn) মডেল পৃষ্ঠা
  এবং [লেটেস্ট মডেল গাইড](https://ai.google.dev/gemini-api/docs/latest-model?hl=bn) দেখুন।

## ৩০ জুলাই, ২০২৬

- **সর্বজনীন প্রিভিউতে Gemini Robotics ER 2**: রোবোটিক্সের জন্য দুটি নতুন এমবডিড
  রিজনিং মডেল এন্ডপয়েন্ট রিলিজ করা হয়েছে:

  - `gemini-robotics-er-2-preview`: উন্নত স্থানিক যুক্তি, এজেন্টিক
    কোড এক্সিকিউশন, একাধিক ধাপের টুল অর্কেস্ট্রেশন, ভিডিও মোমেন্ট খোঁজা,
    প্রগ্রেস ক্লাসিফিকেশন এবং একাধিক রোবটের কোঅর্ডিনেশন।
  - `gemini-robotics-er-2-streaming-preview`: Live API ব্যবহার করে রিয়েল-টাইম টেক্সট স্ট্রিমিংয়ের জন্য অপ্টিমাইজ করা হয়েছে, যা দ্বিমুখী অডিও ও ভিডিও ইনপুট সহ কম-লেটেন্সি রোবট এজেন্টকে সক্ষম করে।

  উভয় মডেল এন্ডপয়েন্ট টেক্সট, ছবি, ভিডিও ও অডিও ইনপুট গ্রহণ করে এবং
  ফিজিক্যাল রোবট অ্যাকশনের জন্য ব্লকিং আচরণ সহ ফাংশন কলিং সাপোর্ট করে।
  শুরু করতে, [Gemini Robotics ER ওভারভিউ](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=bn) দেখুন। রিয়েল-টাইম স্ট্রিমিংয়ের
  ব্যবহারিক প্রয়োগের জন্য, [স্ট্রিমিং সহ রোবোটিক্স](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=bn) দেখুন।
- **বন্ধ করে দেওয়ার ঘোষণা**: `gemini-robotics-er-1.6-preview` মডেল
  ৩১ আগস্ট, ২০২৬-এ [বন্ধ করে দেওয়া হবে](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn)।

## ২১ জুলাই, ২০২৬

- **Gemini 3.6 Flash এবং Gemini 3.5 Flash-Lite সাধারণভাবে উপলভ্য (GA)**:
  আমাদের লেটেস্ট 3.x Flash মডেলের স্টেবল, প্রোডাকশন-রেডি ভার্সন রিলিজ করা হয়েছে:

  - **Gemini 3.6 Flash** (`gemini-3.6-flash`): 3.5 Flash-এর তুলনায় কম দামে উন্নত টোকেন
    দক্ষতা এবং কোড/এজেন্টিক প্ল্যানিংয়ের ক্ষমতা প্রদান করে, আউটপুট ভার্বোসিটি সম্পর্কে ডেভেলপারদের মতামত সমাধান করে।
  - **Gemini 3.5 Flash-Lite** (`gemini-3.5-flash-lite`): কম লেটেন্সি, অত্যন্ত সাশ্রয়ী সাব-এজেন্ট বিকল্প অফার করে যা
    অটোমেশনের জন্য ডিজাইন করা হয়েছে।

  আরও জানতে, [Gemini 3.6 Flash গাইড](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=bn) দেখুন।
- **বন্ধ হয়ে যাওয়া প্যারামিটার**: স্যাম্পলিং প্যারামিটার `temperature`, `top_p`
  এবং `top_k` এখন বন্ধ হয়ে গেছে। আরও তথ্যের জন্য
  [Gemini 3.6 Flash গাইড](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=bn#sampling-parameter-deprecation)
  দেখুন।

## ৬ জুলাই, ২০২৬

- Interactions API-এর জন্য [ডেভেলপার লগ](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=bn)
  সাপোর্ট: কাজ করে এমন Interactions API কলের লগ এখন
  [AI Studio ড্যাশবোর্ডে](https://aistudio.google.com/logs?hl=bn) দেখা যাবে।

## ৩০ জুন, ২০২৬

- **পাবলিক প্রিভিউতে Gemini Omni Flash**: `gemini-omni-flash-preview`-এ রিলিজ করা হয়েছে,
  এটি হাই-পারফর্ম্যান্স মাল্টিমডেল মডেল যা হাই-স্পিড ভিডিও জেনারেশন
  ও কথোপকথনের মাধ্যমে ভিডিও এডিটিংয়ের জন্য ডিজাইন করা হয়েছে। [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=bn) ব্যবহার করে,
  আপনি টেক্সট বিবরণ থেকে 720p-তে ৩–১০ সেকেন্ডের ভিডিও তৈরি করতে বা স্থির ছবি অ্যানিমেট করতে পারবেন,
  এবং তারপর কথোপকথনের মাধ্যমে আউটপুট এডিট ও রিফাইন করতে পারবেন। শুরু করতে, [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=bn) গাইড এবং
  [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=bn) মডেল কার্ড দেখুন।
- জেনেরাল অ্যাভেইলেবিলিটিতে (GA) `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite) রিলিজ করা হয়েছে, এটি আমাদের বিল্ট-ইন মাল্টিমডেল মডেল যা আল্ট্রা-লো লেটেন্সি এবং সাশ্রয়ী মূল্যে ইমেজ জেনারেশন ও এডিটিংয়ের জন্য অপ্টিমাইজ করা হয়েছে। [Gemini 3.1
  Flash Lite Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=bn) মডেল
  কার্ড এবং [ইমেজ জেনারেশন](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn) গাইড দেখুন।

## ২৪ জুন, ২০২৬

- **কম্পিউটার ব্যবহার**: Gemini 3.5 Flash-এ
  [কম্পিউটার ব্যবহার](https://ai.google.dev/gemini-api/docs/computer-use?hl=bn) টুলের জন্য পাবলিক প্রিভিউ সাপোর্ট লঞ্চ করা হয়েছে। এই
  রিলিজে ইনটেন্ট সহ সরলীকৃত অ্যাকশন, ব্রাউজার, মোবাইল ও ডেস্কটপ এনভায়রনমেন্টের জন্য
  বিল্ট-ইন সহায়তা, কনফিগার করা যায় এমন নিরাপত্তা নীতি এবং
  উন্নত প্রম্পট ইঞ্জেকশন ডিটেকশন অন্তর্ভুক্ত আছে।

## ১৭ জুন, ২০২৬

- **স্পিচ জেনারেশনের জন্য স্ট্রিমিং সাপোর্ট**: `streamGenerateContent`-এর মাধ্যমে স্ট্রিমিং (এবং Interactions API-তে `stream: true`) এখন
  `gemini-3.1-flash-tts-preview` মডেলের জন্য কাজ করে। আরও জানতে, [টেক্সট-টু-স্পিচ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=bn#streaming) গাইড দেখুন।

## ১৫ জুন, ২০২৬

- **বন্ধ করার ঘোষণা**: নিম্নলিখিত ছবি জেনারেশন মডেলগুলি
  বন্ধ করা হচ্ছে এবং **১৭ আগস্ট, ২০২৬** তারিখে [বন্ধ করে দেওয়া হবে](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn):

  - **Imagen 4 এবং Gemini 3 ইমেজ মডেল**:
    - `imagen-4.0-generate-001`
    - `imagen-4.0-ultra-generate-001`
    - `imagen-4.0-fast-generate-001`

  আপনার কোড নতুন স্টেবল বা প্রিভিউ এন্ডপয়েন্টে মাইগ্রেট করতে, [Gemini বন্ধ হয়ে যাওয়া](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn#imagen-models) পৃষ্ঠা দেখুন।
- **বন্ধ করে দেওয়ার ঘোষণা**: নিম্নলিখিত ভিডিও জেনারেশন মডেলগুলি
  বন্ধ করে দেওয়া হচ্ছে এবং **৩০ জুন, ২০২৬** থেকে [বন্ধ হয়ে যাবে](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn):

  - **Veo মডেল**:
    - `veo-2.0-generate-001`
    - `veo-3.0-generate-001`
    - `veo-3.0-fast-generate-001`

  পরিষেবা যাতে বন্ধ না হয়ে যায়, তার জন্য আপনার ইন্টিগ্রেশন আপডেট করুন, যাতে Veo 3.1 প্রিভিউ মডেল আইডি
  (`veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`) অথবা
  [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=bn)-এর মাধ্যমে উপলভ্য
  3.1 GA মডেল ব্যবহার করা যায়।
- **বন্ধ করার ঘোষণা**: পরীক্ষামূলক GMP Contextual View টুল (Grounding with Google Maps আউটপুটের জন্য একটি নির্দিষ্ট ইন্টারফেস) **১৫ জুন, ২০২৬** তারিখে [বন্ধ হয়ে যাবে](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn):

## ১ জুন, ২০২৬

- নিম্নলিখিত Gemini 2.0 মডেল এখন [বন্ধ করে দেওয়া](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn) হয়েছে:

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

  এর পরিবর্তে [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=bn) বা
  [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=bn)
  ব্যবহার করুন।

## ২৮ মে, ২০২৬

- আমাদের নেটিভ
  ভিজ্যুয়াল মডেলের সাধারণভাবে উপলভ্য (GA) ভার্সন `gemini-3.1-flash-image` (Nano Banana 2) এবং `gemini-3-pro-image` (Nano Banana Pro) রিলিজ করা হয়েছে, এগুলি হল [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=bn)
  এবং [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=bn)।
- **ভিডিও-টু-ইমেজ জেনারেশন সংক্রান্ত সহায়তা**: আপনি এখন টেক্সট প্রম্পটের পাশাপাশি মাল্টিমোডাল কনটেক্সট হিসেবে ভিডিও ফাইল (সরাসরি আপলোড বা সর্বজনীন YouTube URL-এর মাধ্যমে) পাস করতে পারবেন। এর ফলে খুব ভালো কোয়ালিটির থাম্বনেল, সিনেমাটিক মুভি পোস্টার বা সারসংক্ষেপের ইনফোগ্রাফিক তৈরি করা যাবে। এই ফিচারটি শুধুমাত্র `gemini-3.1-flash-image` মডেলে
  কাজ করে। আরও জানতে, [ভিডিও-টু-ইমেজ জেনারেশন](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn#video-to-image)
  গাইড দেখুন।
- বন্ধ করার ঘোষণা: `gemini-3.1-flash-image-preview` এবং
  `gemini-3-pro-image-preview` মডেলগুলি বন্ধ করা হচ্ছে
  এবং ২৫ জুন, ২০২৬ তারিখে সেগুলি [বন্ধ করে দেওয়া হবে](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn)।

## ২৫ মে, ২০২৬

- `gemini-3.1-flash-lite-preview` মডেল
  [বন্ধ করা](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn) হয়েছে। পরিবর্তে
  [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=bn) ব্যবহার করুন।

## ১৯ মে, ২০২৬

- `gemini-3.5-flash`-এ রিলিজ করা হয়েছে, [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=bn)-এর
  জেনেরাল অ্যাভেইলেবিলিটি (GA) ভার্সন,
  এজেন্টিক ও কোডিং টাস্কে ফ্রন্টিয়ার পারফর্ম্যান্স বজায় রাখার জন্য
  আমাদের সবচেয়ে ইন্টেলিজেন্ট মডেল। `gemini-flash-latest`-এর পিছনে এখন এই মডেলটি কাজ করে।
- পাবলিক প্রিভিউতে **Gemini API-তে Managed Agents** লঞ্চ করা হয়েছে। এটি ডেভেলপারদের
  নিরাপদ, আইসোলেটেড Google-হোস্ট করা Linux স্যান্ডবক্স এনভায়রনমেন্টে রান করে এমন অটোনোমাস, স্টেটফুল এজেন্ট
  তৈরি ও ডিপ্লয় করতে দেয়। আরও জানতে,
  [এজেন্ট ওভারভিউ](https://ai.google.dev/gemini-api/docs/agents?hl=bn) পৃষ্ঠা এবং
  [কুইকস্টার্ট](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=bn) দেখুন।
- পাবলিক প্রিভিউতে, সাধারণ-উদ্দেশ্য **Antigravity Agent** ম্যানেজ করা এজেন্ট, [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=bn) প্রকাশ করা হয়েছে।
  Antigravity এজেন্ট নিজের স্যান্ডবক্স কন্টেনারের মধ্যে স্বয়ংক্রিয়ভাবে পরিকল্পনা, রিজনিং, কোড লেখা ও এক্সিকিউট করা,
  ফাইল ম্যানেজ করা এবং ওয়েব ব্রাউজ করতে পারে। কোড স্যাম্পেল ও স্পেসিফিকেশনের জন্য
  [Antigravity এজেন্ট](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=bn) গাইড দেখুন।

## ৭ মে, ২০২৬

- `gemini-3.1-flash-lite`-এ রিলিজ করা হয়েছে, জেনেরাল অ্যাভেইলেবিলিটি (GA) ভার্সন
  [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=bn),
  স্পিড, স্কেল ও খরচ সাশ্রয়ের জন্য অপ্টিমাইজ করা হয়েছে।
- বন্ধ হয়ে যাওয়া সংক্রান্ত ঘোষণা: `gemini-3.1-flash-lite-preview` মডেলটি
  ৫/১১/২৬-এ বন্ধ হয়ে যাচ্ছে এবং ২৫ মে, ২০২৬-এ
  [বন্ধ করে দেওয়া হবে](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn)।

## ৬ মে, ২০২৬

- **আসন্ন ব্রেকিং পরিবর্তন**: [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=bn)
  অনুরোধ ও উত্তর স্কিমা (`outputs` → `steps`) এবং আউটপুট ফর্ম্যাট
  কনফিগারেশন (`response_format`) পরিবর্তন করা হচ্ছে। নতুন স্কিমা **২৬ মে** থেকে ডিফল্ট হিসেবে সেট করা হবে এবং পুরনো স্কিমা **৮ জুন** থেকে সরিয়ে দেওয়া হবে।
  আরও জানতে
  [মাইগ্রেশন গাইড](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=bn)
  দেখুন।

## ৫ মে, ২০২৬

- মাল্টিমোডাল সার্চের সুবিধা দিতে **ফাইল সার্চ** আপডেট করা হয়েছে। আপনি এখন `gemini-embedding-2` মডেল ব্যবহার করে ছবি নেটিভভাবে
  এম্বেড ও সার্চ করতে পারবেন।
  গ্রাউন্ডিং মেটাডেটায় এখন ভিজ্যুয়াল উদ্ধৃতির জন্য `media_id` এবং
  `page_numbers` অন্তর্ভুক্ত থাকে যা তথ্য কোথায় পাওয়া গেছে তা নির্দেশ করে। আরও
  জানতে, [ফাইল সার্চ](https://ai.google.dev/gemini-api/docs/file-search?hl=bn) গাইড দেখুন।

## ৪ মে, ২০২৬

- ব্যাচ API এবং দীর্ঘমেয়াদী
  অপারেশনের জন্য পোলিং ওয়ার্কফ্লো প্রতিস্থাপন করতে Gemini API-তে ইভেন্ট-ড্রিভেন [ওয়েবহুক](https://ai.google.dev/gemini-api/docs/webhooks?hl=bn)
  সাপোর্ট লঞ্চ করা হয়েছে।

## ৩০ এপ্রিল, ২০২৬

- `gemini-robotics-er-1.5-preview` মডেলটি
  [বন্ধ করে দেওয়া](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn) হয়েছে। এর পরিবর্তে
  [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=bn) ব্যবহার করুন।

## ২২ এপ্রিল, ২০২৬

- `gemini-embedding-2`-এ জেনারেলি অ্যাভেলেবল (GA) হিসেবে রিলিজ করা হয়েছে।
  আরও জানতে, [এম্বেডিং](https://ai.google.dev/gemini-api/docs/embeddings?hl=bn) পৃষ্ঠা দেখুন।

## ২১ এপ্রিল, ২০২৬

- কোলাবরেটিভ প্ল্যানিং, ভিজ্যুয়ালাইজেশন সাপোর্ট, MCP সার্ভার ইন্টিগ্রেশন এবং ফাইল সার্চ সহ [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=bn)
  এজেন্টের নতুন ভার্সন রিলিজ করা হয়েছে:

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=bn): দ্রুত ও দক্ষতার সাথে কাজ করার জন্য ডিজাইন করা হয়েছে, ক্লায়েন্ট UI-তে স্ট্রিম করার জন্য আদর্শ।
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=bn): অটোমেটিক প্রসঙ্গ সংগ্রহ ও সিন্থেসিসের জন্য
    সর্বাধিক বোধগম্যতা।

## ১৫ এপ্রিল, ২০২৬

- আমরা [Gemini 3.1 Flash TTS প্রিভিউ](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=bn) লঞ্চ করেছি। এটি আমাদের কম খরচে,
  সাবলীল ও কন্ট্রোল করা যায় এমন টেক্সট-টু-স্পিচ মডেল। আরও জানতে
  [টেক্সট-টু-স্পিচ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=bn) ডকুমেন্ট পড়ুন।

## ১৪ এপ্রিল, ২০২৬

- `gemini-robotics-er-1.6-preview` রিলিজ করা হয়েছে, এটি আমাদের আপডেট করা রোবোটিক্স মডেল।
  এতে এখন ইনস্ট্রুমেন্ট রিডিং, উন্নত স্পেশিয়াল ও ফিজিক্যাল রিজনিংয়ের মতো নতুন ক্ষমতা রয়েছে। আরও জানতে, [Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=bn) পৃষ্ঠা এবং
  [ব্লগ](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=bn) দেখুন।
- বন্ধ করে দেওয়ার ঘোষণা: `gemini-robotics-er-1.5-preview` মডেলটি
  ৩০ এপ্রিল, ২০২৬ তারিখে প্যাসিফিক স্ট্যান্ডার্ড টাইম (PST) সকাল ৯টায়
  [বন্ধ করে দেওয়া](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn) হবে।

## ২ এপ্রিল, ২০২৬

- `gemma-4-26b-a4b-it` এবং `gemma-4-31b-it` রিলিজ করা হয়েছে, যা
  [AI Studio](https://aistudio.google.com?hl=bn)-তে এবং Gemini API-এর মাধ্যমে উপলভ্য,
  [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=bn) লঞ্চের অংশ হিসেবে।

## ১ এপ্রিল, ২০২৬

- নতুন [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=bn) এবং [Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=bn) ইনফারেন্স টিয়ার চালু করা হয়েছে, যা খরচ বা লেটেন্সি অপ্টিমাইজ করার জন্য আরও বিকল্প অফার করে।

## ৩১ মার্চ, ২০২৬

- Veo 3.1 Lite প্রিভিউ, [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=bn) লঞ্চ করা হয়েছে, এটি আমাদের সবচেয়ে
  সাশ্রয়ী [ভিডিও জেনারেশন](https://ai.google.dev/gemini-api/docs/video?hl=bn) মডেল, যা দ্রুত ইটারেশন এবং
  হাই-ভলিউম অ্যাপ্লিকেশন তৈরির জন্য ডিজাইন করা হয়েছে।
- `gemini-2.5-flash-lite-preview-09-2025` মডেল বন্ধ করে দেওয়া হয়েছে। এর পরিবর্তে
  [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=bn) ব্যবহার করুন।

## ২৬ মার্চ, ২০২৬

- রিলিজ করা হয়েছে [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=bn), লেটেস্ট
  অডিও-টু-অডিও (A2A) মডেল যা রিয়েল-টাইম ডায়ালগ ও ভয়েস-ফার্স্ট
  AI অ্যাপ্লিকেশনের জন্য ডিজাইন করা হয়েছে। শুরু করতে [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=bn) ডকুমেন্ট
  পড়ুন।

## ২৫ মার্চ, ২০২৬

- [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=bn) মিউজিক জেনারেশন
  মডেল লঞ্চ করা হয়েছে: [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=bn)
  (৩০-সেকেন্ডের ক্লিপ) এবং [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=bn)
  (সম্পূর্ণ দৈর্ঘ্যের গান)। দুটি মডেলই টেক্সট ও ইমেজ ইনপুট গ্রহণ করে এবং
  হাই-কোয়ালিটি, ৪৮ কিলোহার্টজ স্টেরিও অডিও জেনারেট করে। বিস্তারিত তথ্য ও কোড স্যাম্পেলের জন্য
  [মিউজিক জেনারেশন](https://ai.google.dev/gemini-api/docs/music-generation?hl=bn) গাইড দেখুন।

## ২৩ মার্চ, ২০২৬

- AI Studio-তে [প্রিপে ও পোস্টপে বিলিং প্ল্যান](https://ai.google.dev/gemini-api/docs/billing?hl=bn)
  রিলিজ করা হয়েছে। আগে থেকে থাকা অ্যাকাউন্ট প্রভাবিত হতে পারে; আরও তথ্যের জন্য [বিলিং](https://ai.google.dev/gemini-api/docs/billing?hl=bn) ডকুমেন্টেশন পড়ুন।

## ১৮ মার্চ, ২০২৬

- নতুন [বিল্ট-ইন টুল ও ফাংশন কলিংয়ের কম্বিনেশন](https://ai.google.dev/gemini-api/docs/tool-combination?hl=bn) ফিচার রিলিজ করা হয়েছে, এর ফলে
  একটি API কলে কাস্টম ফাংশন কলিং
  টুলের পাশাপাশি Gemini-এর বিল্ট-ইন টুল ব্যবহার করা যাবে।
- [Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=bn#supported_models)
  এখন থেকে Gemini 3 মডেলে কাজ করবে।

## ১৬ মার্চ, ২০২৬

- ব্যবহারকারীর বিলিং অভিজ্ঞতা আরও ভালো করতে,
  নতুন করে সাজানো [ব্যবহারের টিয়ার](https://ai.google.dev/gemini-api/docs/billing?hl=bn#about-billing)
  এবং [বিলিং অ্যাকাউন্টের খরচ সংক্রান্ত ক্যাপ](https://ai.google.dev/gemini-api/docs/billing?hl=bn#tier-spend-caps)
  পরিচয় করানো হয়েছে।

## ১২ মার্চ, ২০২৬

- AI Studio-তে বিলিংয়ের জন্য [প্রোজেক্ট-লেভেল খরচ সীমা](https://ai.google.dev/gemini-api/docs/billing?hl=bn#project-spend-caps) চালু করা হয়েছে।

## ১০ মার্চ, ২০২৬

- `gemini-embedding-2-preview` রিলিজ করা হয়েছে, এটি আমাদের প্রথম মাল্টিমোডাল এম্বেডিং মডেল।
  এটি টেক্সট, ছবি, ভিডিও, অডিও ও PDF ইনপুট সাপোর্ট করে,
  সমস্ত মোডালিটি একটি ইউনিফায়েড এম্বেডিং স্পেসে ম্যাপ করে। আরও জানতে, [এম্বেডিং](https://ai.google.dev/gemini-api/docs/embeddings?hl=bn) দেখুন।
- বন্ধ হয়ে যাওয়া সংক্রান্ত ঘোষণা: `gemini-2.5-flash-lite-preview-09-2025` মডেল
  ৩১ মার্চ, ২০২৬-এ [বন্ধ হয়ে যাবে](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn)।

## ৯ মার্চ, ২০২৬

- Gemini 3 Pro প্রিভিউ মডেল [বন্ধ করা](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn) হয়েছে। `gemini-3-pro-preview` এখন
  [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=bn)-এ পয়েন্ট করে।

## ৩ মার্চ, ২০২৬

- Gemini 3.1 Flash-Lite প্রিভিউ লঞ্চ করা হয়েছে, এটি Gemini 3 সিরিজের প্রথম Flash-Lite মডেল।
  স্পেসিফিকেশন, নির্দিষ্ট
  আপডেট ও ডেভেলপার নির্দেশিকা পেতে [মডেল পৃষ্ঠা](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=bn) পড়ুন।

## ২৬ ফেব্রুয়ারি, ২০২৬

- Nano Banana 2, [Gemini 3.1 Flash Image
  Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=bn) লঞ্চ করা হয়েছে, এটি একটি অত্যন্ত দক্ষ
  মডেল যা স্পিড ও হাই-ভলিউম ব্যবহারের জন্য অপ্টিমাইজ করা হয়েছে।
- বন্ধ করার ঘোষণা: Gemini 3 Pro প্রিভিউ (`gemini-3-pro-preview`)
  ৯ মার্চ, ২০২৬-এ [বন্ধ করে দেওয়া হবে](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn)।

## ১৯ ফেব্রুয়ারি, ২০২৬

- নতুন Gemini 3 সিরিজের ফ্যামিলিতে আমাদের লেটেস্ট ইটারেশন [Gemini 3.1 Pro প্রিভিউ](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=bn) রিলিজ করা হয়েছে।
- একটি আলাদা এন্ডপয়েন্ট `gemini-3.1-pro-preview-customtools` লঞ্চ করা হয়েছে, যা
  ব্যাশ ও টুলের মিশ্রণ ব্যবহার করে তৈরি করা ব্যবহারকারীদের জন্য কাস্টম টুলকে অগ্রাধিকার দেওয়ার ক্ষেত্রে
  আরও ভালো।

## ১৮ ফেব্রুয়ারি, ২০২৬

- বন্ধ হয়ে যাওয়ার ঘোষণা: ১ জুন, ২০২৬ থেকে নিম্নলিখিত মডেলগুলি
  [বন্ধ হয়ে যাবে](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn):

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## ১৭ ফেব্রুয়ারি, ২০২৬

- নিম্নলিখিত মডেলগুলি [বন্ধ করা](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn) হয়েছে:

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## ২৯ জানুয়ারি, ২০২৬

- `gemini-3-pro-preview` এবং
  `gemini-3-flash-preview`-এ কম্পিউটার ব্যবহার টুল চালু করা হয়েছে।

## ২১ জানুয়ারি, ২০২৬

- `latest`-এর অ্যালিয়াস পরিবর্তন করা হয়েছে:

  - `gemini-pro-latest` পাল্টে `gemini-3-pro-preview` করা হয়েছে
  - `gemini-flash-latest` পাল্টে `gemini-3-flash-preview` করা হয়েছে

## ১৫ জানুয়ারি, ২০২৬

- বন্ধ করে দেওয়ার ঘোষণা: নিম্নলিখিত মডেলগুলি ১৭ ফেব্রুয়ারি, ২০২৬-এ
  [বন্ধ করে দেওয়া](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn) হবে:

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- `gemini-2.5-flash-image-preview` মডেল বন্ধ করে দেওয়া হয়েছে।

## ১৪ জানুয়ারি, ২০২৬

- `text-embedding-004` মডেল [বন্ধ করে দেওয়া](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn) হয়েছে।

## ১৩ জানুয়ারি, ২০২৬

- [Veo](https://ai.google.dev/gemini-api/docs/video?hl=bn)-এর জন্য 4k আউটপুট রেজোলিউশন যোগ করা হয়েছে এবং
  সব রেজোলিউশনে পোর্ট্রেট ভিডিওর জন্য আরও সহায়তা যোগ করা হয়েছে।

## ১২ জানুয়ারি, ২০২৬

- মডেল লাইফসাইকেল ফিচার লঞ্চ করা হয়েছে। কিছু মডেল এখন লাইফসাইকেল স্টেজ ও
  বন্ধ হয়ে যাওয়ার টাইমলাইন উল্লেখ করবে। আরও তথ্যের জন্য নিম্নলিখিত ডকুমেন্টেশন
  দেখুন:

  - [মডেলের পর্যায়](https://ai.google.dev/api/generate-content?hl=bn#ModelStatus)

## ৮ জানুয়ারি, ২০২৬

- Gemini API-এর জন্য ডেটা ইনপুট সোর্স হিসেবে Cloud Storage বাকেট এবং যেকোনও পাবলিক ও প্রাইভেট DB
  প্রি-সাইন করা URL-এর জন্য সহায়তা লঞ্চ করা হয়েছে। এছাড়াও, ফাইলের সাইজের সীমা
  ২০ এমবি থেকে ১০০ এমবিতে বাড়ানো হয়েছে। আরও জানতে, [ফাইল ইনপুট পদ্ধতি
  সংক্রান্ত নির্দেশিকা](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=bn) দেখুন।

## ১৯ ডিসেম্বর, ২০২৫

- v1beta-তে Interactions API-তে একটি ব্রেকিং পরিবর্তন করা হয়েছে। থিঙ্কিং মডেলে "চিন্তাভাবনা"র ধারণার সাথে আরও ভালোভাবে মানানসই করতে `total_reasoning_tokens` ফিল্ডের নাম পরিবর্তন করে
  `total_thought_tokens` করা হয়েছে।

## ১৭ ডিসেম্বর, ২০২৫

- Gemini 3 Flash প্রিভিউ লঞ্চ করা হয়েছে, `gemini-3-flash-preview`, যা দ্রুত
  ফ্রন্টিয়ার-ক্লাস পারফর্ম্যান্স প্রদান করে যা অনেক কম
  খরচে অনেক বড় মডেলের সাথে প্রতিদ্বন্দ্বিতা করতে পারে। আপগ্রেড করা ভিজ্যুয়াল ও স্পেশিয়াল রিজনিং এবং এজেন্টিক কোডিং
  ক্ষমতা সহ। কিছু নতুন ফিচার সম্পর্কে ডকুমেন্টেশন পড়ুন, এর মধ্যে রয়েছে:

  - [মাল্টিমোডাল ফাংশন রেসপন্স](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn#multimodal)
  - [ছবি সহ কোড এক্সিকিউশন](https://ai.google.dev/gemini-api/docs/code-execution?hl=bn#images)

## ১২ ডিসেম্বর, ২০২৫

- `gemini-2.5-flash-native-audio-preview-12-2025`,
  Live API-এর জন্য নতুন নেটিভ অডিও মডেল রিলিজ করা হয়েছে। এই আপডেট জটিল ওয়ার্কফ্লো ম্যানেজ করার ক্ষেত্রে মডেলের
  ক্ষমতা উন্নত করে। আরও জানতে, [Live API গাইড](https://ai.google.dev/gemini-api/docs/live-guide?hl=bn) এবং
  [Gemini 2.5 Flash নেটিভ অডিও](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=bn) দেখুন।

## ১১ ডিসেম্বর, ২০২৫

- Interactions API লঞ্চ করা হয়েছে। এই API, Gemini মডেল ও এজেন্টের সাথে ইন্টার‍্যাক্ট করার জন্য
  একটি ইউনিফায়েড ইন্টারফেস প্রদান করে। আরও জানতে, [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=bn) গাইড দেখুন।
- প্রিভিউতে Gemini Deep Research এজেন্ট লঞ্চ করা হয়েছে। এটি
  একাধিক ধাপের রিসার্চ টাস্কের জন্য স্বয়ংক্রিয়ভাবে প্ল্যান, এক্সিকিউট ও সিন্থেসাইজ করতে
  পারে। বিস্তারিত জানতে [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=bn) গাইড দেখুন।

## ১০ ডিসেম্বর, ২০২৫

- আমাদের [টেক্সট-টু-স্পিচ মডেল](https://ai.google.dev/gemini-api/docs/speech-generation?hl=bn), Gemini 2.5 Flash TTS প্রিভিউ
  (কম লেটেন্সির জন্য অপ্টিমাইজ করা) এবং Gemini 2.5 Pro TTS প্রিভিউ (কোয়ালিটির জন্য অপ্টিমাইজ করা
  ) সহ উন্নত এক্সপ্রেসিভিটি, নির্ভুল পেসিং এবং সাবলীল
  ডায়ালগ লঞ্চ করা হয়েছে।

## ৯ ডিসেম্বর, ২০২৫

- নিম্নলিখিত Gemini Live API মডেল এখন বন্ধ করা হয়েছে:
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## ৫ ডিসেম্বর, ২০২৫

- [Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=bn)-এর জন্য Gemini 3 বিলিং ৫ জানুয়ারি, ২০২৬ থেকে শুরু হবে।

## ৪ ডিসেম্বর, ২০২৫

- বন্ধ করে দেওয়ার ঘোষণা: `gemini-2.5-flash-image-preview` মডেলটি ১৫ জানুয়ারি, ২০২৬-এ
  বন্ধ করে দেওয়া হবে।

## ৩ ডিসেম্বর, ২০২৫

- বন্ধ করার ঘোষণা: `text-embedding-004` মডেলটি ১৪ জানুয়ারি, ২০২৬-এ বন্ধ করে দেওয়া হবে।

## ২০ নভেম্বর, ২০২৫

- Gemini 3 Pro Image Preview রিলিজ করা হয়েছে, `gemini-3-pro-image-preview`, যা
  Nano Banana মডেলের পরবর্তী ভার্সন। আরও জানতে [ইমেজ জেনারেশন](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn) পৃষ্ঠাটি পড়ুন।

## ১৮ নভেম্বর, ২০২৫

- প্রথম Gemini 3 সিরিজের মডেল, `gemini-3-pro-preview` লঞ্চ করা হয়েছে, এটি আমাদের
  অত্যাধুনিক রিজনিং ও মাল্টিমোডাল বোঝার মডেল, এতে শক্তিশালী
  এজেন্টিক ও কোডিং ক্ষমতা রয়েছে।

  বুদ্ধিমত্তা ও পারফর্ম্যান্সের উন্নতি ছাড়াও,
  Gemini 3 Pro প্রিভিউতে এইসব বিষয়ে নতুন আচরণ দেখা যায়:

  - [মিডিয়া রেজোলিউশন](https://ai.google.dev/gemini-api/docs/media-resolution?hl=bn)
  - [চিন্তার স্বাক্ষর](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=bn)
  - [থিঙ্কিং লেভেল](https://ai.google.dev/gemini-api/docs/thinking?hl=bn#thinking-levels)

  মাইগ্রেশন, নতুন ফিচার ও স্পেসিফিকেশন সম্পর্কে জানতে
  [Gemini 3 ডেভেলপার গাইড](https://ai.google.dev/gemini-api/docs/gemini-3?hl=bn) পড়ুন।

## ১১ নভেম্বর, ২০২৫

- বন্ধ হয়ে যাওয়া সংক্রান্ত ঘোষণা: নিম্নলিখিত মডেলগুলি বন্ধ হয়ে যাবে:

  - ১২ নভেম্বর:

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - ১৪ নভেম্বর:

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## ১০ নভেম্বর, ২০২৫

- নিম্নলিখিত মডেল বন্ধ করা হয়েছে:

  - `imagen-3.0-generate-002`

  পরিবর্তে [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=bn#imagen-4) ব্যবহার করুন। আরও তথ্যের জন্য
  [Gemini-র বন্ধ হয়ে যাওয়া ফিচার সংক্রান্ত টেবিল](https://ai.google.dev/gemini-api/docs/deprecations?hl=bn) দেখুন।

## ৬ নভেম্বর, ২০২৫

- পাবলিক প্রিভিউতে File Search API লঞ্চ করা হয়েছে, এর ফলে ডেভেলপাররা
  তাদের নিজস্ব ডেটা থেকে উত্তর জেনারেট করতে পারবেন। আরও তথ্যের জন্য নতুন [ফাইল সার্চ](https://ai.google.dev/gemini-api/docs/file-search?hl=bn) পৃষ্ঠা পড়ুন।

## ৪ নভেম্বর, ২০২৫

- [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn)-এর জন্য, ছবির ইনপুট
  টোকেন সংখ্যা ১২৯০ থেকে কমিয়ে ২৫৮ করা হয়েছে, এর ফলে ছবি এডিট করার খরচ
  কমে গেছে।
- বন্ধ হয়ে যাওয়া সংক্রান্ত ঘোষণা: নিম্নলিখিত মডেলগুলি বন্ধ হয়ে যাবে:

  - ১৮ নভেম্বর:

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - ২ ডিসেম্বর:

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - ৯ ডিসেম্বর:

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## ২৯ অক্টোবর, ২০২৫

- Gemini API-এর জন্য নতুন [লগিং ও ডেটাসেট](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=bn) টুল
  লঞ্চ করা হয়েছে।

## ২০ অক্টোবর, ২০২৫

- নিম্নলিখিত Gemini Live API মডেল এখন বন্ধ করা হয়েছে:

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  আপনি এর পরিবর্তে `gemini-2.5-flash-native-audio-preview-09-2025` ব্যবহার করতে পারেন।
- বন্ধ করার ঘোষণা: `gemini-2.0-flash-live-001` এবং
  `gemini-live-2.5-flash-preview` ৯ ডিসেম্বর, ২০২৫ থেকে বন্ধ হয়ে যাচ্ছে।

## ১৭ অক্টোবর, ২০২৫

- **Google Maps-এর মাধ্যমে গ্রাউন্ডিং** এখন
  সাধারণভাবে উপলভ্য। আরও তথ্যের জন্য, [Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=bn) ডকুমেন্টেশন দেখুন।

## ১৫ অক্টোবর, ২০২৫

- পাবলিক প্রিভিউতে [Veo 3.1 এবং 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=bn#veo-3.1) মডেল রিলিজ করা হয়েছে, যার মধ্যে নতুন ফিচারগুলি হল:

  - Veo-র মাধ্যমে তৈরি করা ভিডিওর দৈর্ঘ্য বাড়ানো।
  - ভিডিও তৈরি করতে সর্বাধিক তিনটি ছবি রেফারেন্স হিসেবে ব্যবহার করা হচ্ছে।
  - ভিডিও তৈরি করার জন্য প্রথম ও শেষ ফ্রেমের ছবি প্রদান করা।

  এছাড়াও, এই লঞ্চের মাধ্যমে Veo 3 আউটপুট ভিডিওর সময়সীমার জন্য আরও বিকল্প যোগ করা হয়েছে: ৪, ৬
  এবং ৮ সেকেন্ড।
- বন্ধ করার ঘোষণা: `veo-3.0-generate-preview` এবং
  `veo-3.0-fast-generate-preview` ১২ নভেম্বর, ২০২৫ থেকে বন্ধ হয়ে যাবে।

## ৭ অক্টোবর, ২০২৫

- [Gemini 2.5 Computer Use Preview](https://ai.google.dev/gemini-api/docs/computer-use?hl=bn) লঞ্চ করা হয়েছে

## ২ অক্টোবর, ২০২৫

- Gemini 2.5 Flash Image GA লঞ্চ করা হয়েছে: [Gemini-র মাধ্যমে ইমেজ জেনারেশন](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn)

## ২৯ সেপ্টেম্বর, ২০২৫

- নিম্নলিখিত Gemini 1.5 মডেল এখন বন্ধ করা হয়েছে:
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## ২৫ সেপ্টেম্বর, ২০২৫

- প্রিভিউতে Gemini Robotics ER 1.5 মডেল রিলিজ করা হয়েছে। আপনার রোবোটিক্স অ্যাপ্লিকেশনের জন্য কীভাবে মডেল ব্যবহার করবেন তা জানতে
  [রোবোটিক্স ওভারভিউ](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=bn)
  দেখুন।
- নিচে উল্লেখ করা প্রিভিউ মডেল লঞ্চ করা হয়েছে:

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  বিস্তারিত জানতে [মডেল](https://ai.google.dev/gemini-api/docs/models?hl=bn) পৃষ্ঠা দেখুন।

## ২৩ সেপ্টেম্বর, ২০২৫

- `gemini-2.5-flash-native-audio-preview-09-2025`-এ রিলিজ করা হয়েছে,
  উন্নত ফাংশন কলিং
  ও স্পিচ কাট অফ হ্যান্ডলিং সহ Live API-এর জন্য নতুন নেটিভ অডিও মডেল। আরও জানতে, [Live API গাইড](https://ai.google.dev/gemini-api/docs/live-guide?hl=bn) এবং
  [Gemini 2.5 Flash নেটিভ অডিও](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.5-flash-native-audio) দেখুন।

## ১৬ সেপ্টেম্বর, ২০২৫

- বন্ধ করার ঘোষণা: নিম্নলিখিত মডেলগুলি অক্টোবর ২০২৫-এ বন্ধ করে দেওয়া হবে:

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  লেটেস্ট এম্বেডিং
  মডেলের বিবরণ পেতে [এম্বেডিং](https://ai.google.dev/gemini-api/docs/embeddings?hl=bn) পৃষ্ঠা দেখুন।

## ১০ সেপ্টেম্বর, ২০২৫

- [Batch API-তে Embeddings মডেল](https://ai.google.dev/gemini-api/docs/batch-api?hl=bn#batch-embedding)-এর জন্য
  সহায়তা রিলিজ করা হয়েছে এবং
  [OpenAI কম্প্যাটিবিলিটি লাইব্রেরি](https://ai.google.dev/gemini-api/docs/openai?hl=bn#batch)-তে Batch API যোগ করা হয়েছে যাতে
  ব্যাচ কোয়েরি আরও সহজে শুরু করা যায়।

## ৯ সেপ্টেম্বর, ২০২৫

- Veo 3 ও Veo 3 Fast GA লঞ্চ করা হয়েছে, এতে কম দাম ও
  অ্যাসপেক্ট রেশিও, রেজোলিউশন ও সিডিংয়ের নতুন বিকল্প রয়েছে। আরও
  তথ্যের জন্য
  [Veo ডকুমেন্টেশন](https://ai.google.dev/gemini-api/docs/video?hl=bn#model-features) পড়ুন।

## ২৬ আগস্ট, ২০২৫

- [Gemini 2.5 ইমেজ প্রিভিউ](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.5-flash-image-preview) লঞ্চ করা হয়েছে,
  এটি আমাদের লেটেস্ট নেটিভ ইমেজ জেনারেশন মডেল।

## ১৮ আগস্ট, ২০২৫

- জেনেরাল অ্যাভেইলেবিলিটি (GA)-তে [URL কন্টেক্সট টুল](https://ai.google.dev/gemini-api/docs/url-context?hl=bn) রিলিজ করা হয়েছে, এটি প্রম্পটে অতিরিক্ত কন্টেক্সট হিসেবে URL প্রদান করার টুল। `gemini-2.0-flash` মডেলের সাথে URL কন্টেক্সট ব্যবহার করার জন্য সহায়তা
  (এক্সপেরিমেন্টাল রিলিজের সময় উপলভ্য) এক সপ্তাহের মধ্যে বন্ধ করে দেওয়া হবে।

## ১৪ আগস্ট, ২০২৫

- সাধারণভাবে উপলভ্য (GA) হিসেবে Imagen 4 Ultra, Standard ও Fast মডেল রিলিজ করা হয়েছে।
  আরও জানতে, [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=bn) পৃষ্ঠা দেখুন।

## ৭ আগস্ট, ২০২৫

- `allow_adult` সেটিং এখন বিধিনিষেধযুক্ত অঞ্চলে
  ইমেজ থেকে ভিডিও জেনারেশনের ক্ষেত্রে উপলভ্য। আরও জানতে
  [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=bn#veo-model-parameters)
  পৃষ্ঠা দেখুন।

## ৩১ জুলাই, ২০২৫

- Veo 3 প্রিভিউ মডেলের জন্য ছবি-থেকে-ভিডিও জেনারেশন লঞ্চ করা হয়েছে।
- Veo 3 Fast প্রিভিউ মডেল রিলিজ করা হয়েছে।
- Veo 3 সম্পর্কে আরও জানতে, [Veo](https://ai.google.dev/gemini-api/docs/video?hl=bn) পৃষ্ঠা দেখুন।

## ২২ জুলাই, ২০২৫

- রিলিজ করা হয়েছে `gemini-2.5-flash-lite`, আমাদের দ্রুত, কম খরচের, উচ্চ-পারফর্ম্যান্সের Gemini
  2.5 মডেল। আরও জানতে, [Gemini 2.5
  Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.5-flash-lite) দেখুন।

## ১৭ জুলাই, ২০২৫

- `veo-3.0-generate-preview` লঞ্চ করা হয়েছে, এটি Veo-এর লেটেস্ট আপডেট যা
  অডিও জেনারেশনের সাথে ভিডিও নিয়ে এসেছে। Veo 3 সম্পর্কে আরও জানতে, [Veo](https://ai.google.dev/gemini-api/docs/video?hl=bn) পৃষ্ঠা দেখুন।
- Imagen 4 Standard ও Ultra-এর জন্য বর্ধিত রেট সীমা। আরও জানতে
  [রেট সীমা](https://ai.google.dev/gemini-api/docs/rate-limits?hl=bn) পৃষ্ঠা দেখুন।

## ১৪ জুলাই, ২০২৫

- আমাদের টেক্সট এম্বেডিং মডেলের স্টেবল ভার্সন
  `gemini-embedding-001` রিলিজ করা হয়েছে। আরও জানতে, [এম্বেডিং](https://ai.google.dev/gemini-api/docs/embeddings?hl=bn) দেখুন। `gemini-embedding-exp-03-07`
  মডেলটি ১৪ আগস্ট, ২০২৫-এ বন্ধ করে দেওয়া হবে।

## ৭ জুলাই, ২০২৫

- Gemini API ব্যাচ মোড লঞ্চ করা হয়েছে। অনুরোধগুলি ব্যাচ আপ করুন এবং সেগুলি প্রক্রিয়া করার জন্য পাঠান
  অ্যাসিঙ্ক্রোনাসভাবে। আরও জানতে, [ব্যাচ মোড](https://ai.google.dev/gemini-api/docs/batch-mode?hl=bn) দেখুন।

## ২৬ জুন, ২০২৫

- প্রিভিউ মডেল `gemini-2.5-pro-preview-05-06` এবং
  `gemini-2.5-pro-preview-03-25` এখন
  লেটেস্ট স্থিতিশীল ভার্সন `gemini-2.5-pro`-এ রিডাইরেক্ট করছে।
- `gemini-2.5-pro-exp-03-25` বন্ধ করা হয়েছে।

## ২৪ জুন, ২০২৫

- Imagen 4 Ultra ও স্ট্যান্ডার্ড প্রিভিউ মডেল রিলিজ করা হয়েছে। আরও জানতে, [ছবি তৈরি করা](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn) পৃষ্ঠা দেখুন।

## ১৭ জুন, ২০২৫

- আমাদের সবচেয়ে শক্তিশালী মডেলের স্টেবেল ভার্সন `gemini-2.5-pro` রিলিজ করা হয়েছে,
  যা এখন অ্যাডাপ্টিভ থিঙ্কিংয়ের সুবিধা প্রদান করে। আরও জানতে, [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.5-pro)
  এবং [Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=bn) দেখুন। `gemini-2.5-pro-preview-05-06`
  ২৬ জুন, ২০২৫-এ `gemini-2.5-pro`-এ রিডাইরেক্ট করা হবে।
- `gemini-2.5-flash` রিলিজ করা হয়েছে, এটি আমাদের প্রথম স্টেবেল 2.5 Flash মডেল। আরও
  জানতে, [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.5-flash) দেখুন।
  `gemini-2.5-flash-preview-04-17` ১৫ জুলাই, ২০২৫-এ বন্ধ হয়ে যাবে।
- `gemini-2.5-flash-lite-preview-06-17` রিলিজ করা হয়েছে, এটি কম খরচে, হাই-পারফর্ম্যান্স
  Gemini 2.5 মডেল। আরও জানতে, [Gemini 2.5 Flash-Lite
  প্রিভিউ](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.5-flash-lite) দেখুন।

## ৫ জুন, ২০২৫

- আমাদের সবচেয়ে শক্তিশালী মডেলের নতুন ভার্সন `gemini-2.5-pro-preview-06-05` রিলিজ করা হয়েছে,
  এখন এতে অ্যাডাপ্টিভ থিঙ্কিংয়ের সুবিধা রয়েছে। আরও জানতে, [Gemini 2.5 Pro প্রিভিউ](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.5-pro-preview-06-05)
  এবং [Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=bn) দেখুন।
  ২৬ জুন, ২০২৫-এ `gemini-2.5-pro-preview-05-06`-কে `gemini-2.5-pro`-এ রিডাইরেক্ট করা হবে।

## ২৭ মে, ২০২৫

- শেষ উপলভ্য টিউনিং মডেল, Gemini 1.5 Flash 001, বন্ধ করে দেওয়া হয়েছে।
  কোনও মডেলেই আর টিউনিং কাজ করে না।
  [Gemini API-এর মাধ্যমে ফাইন-টিউনিং](https://ai.google.dev/gemini-api/docs/model-tuning?hl=bn) দেখুন।

## ২০ মে, ২০২৫

**API আপডেট:**

- ক্লিপিং ইন্টারভাল এবং কনফিগার করা যায় এমন ফ্রেম রেট স্যাম্পলিং ব্যবহার করে
  [কাস্টম ভিডিও প্রিপ্রসেসিং](https://ai.google.dev/gemini-api/docs/video-understanding?hl=bn#customize-video-processing)-এর
  জন্য সহায়তা লঞ্চ করা হয়েছে।
- মাল্টি-টুল ব্যবহার করার সুবিধা লঞ্চ করা হয়েছে, যা একই
  `generateContent` অনুরোধে
  [কোড এক্সিকিউশন](https://ai.google.dev/gemini-api/docs/code-execution?hl=bn) এবং
  [Grounding with Google Search](https://ai.google.dev/gemini-api/docs/grounding?hl=bn) কনফিগার করতে সাহায্য করে।
- Live API-তে
  [অ্যাসিঙ্ক্রোনাস ফাংশন কলের](https://ai.google.dev/gemini-api/docs/live-tools?hl=bn#async-function-calling)
  জন্য সহায়তা চালু করা হয়েছে।
- প্রম্পটে অতিরিক্ত প্রসঙ্গ হিসেবে URL প্রদান করার জন্য একটি পরীক্ষামূলক
  [URL প্রসঙ্গ টুল](https://ai.google.dev/gemini-api/docs/url-context?hl=bn)
  লঞ্চ করা হয়েছে।

**মডেল আপডেট:**

- `gemini-2.5-flash-preview-05-20`-এ, Gemini
  [প্রিভিউ](https://ai.google.dev/gemini-api/docs/models?hl=bn#model-versions) মডেল রিলিজ করা হয়েছে যা
  দাম-পারফর্ম্যান্স ও অ্যাডাপ্টিভ থিঙ্কিংয়ের জন্য অপ্টিমাইজ করা হয়েছে। আরও জানতে, [Gemini 2.5 Flash প্রিভিউ](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.5-flash-preview)
  এবং [Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=bn) দেখুন।
- [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.5-pro-preview-tts)
  এবং
  [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.5-flash-preview-tts)
  মডেল রিলিজ করা হয়েছে, যা এক বা দুজন স্পিকারের সাথে
  [স্পিচ জেনারেট করতে](https://ai.google.dev/gemini-api/docs/speech-generation?hl=bn) পারে।
- `lyria-realtime-exp` মডেল রিলিজ করা হয়েছে, যা রিয়েল টাইমে
  [মিউজিক জেনারেট করে](https://ai.google.dev/gemini-api/docs/music-generation?hl=bn)।
- নেটিভ অডিও আউটপুট ক্ষমতা সহ Live API-এর জন্য নতুন Gemini মডেল,
  `gemini-2.5-flash-preview-native-audio-dialog` এবং
  `gemini-2.5-flash-exp-native-audio-thinking-dialog` রিলিজ করা হয়েছে। আরও
  জানতে, [Live API গাইড](https://ai.google.dev/gemini-api/docs/live-guide?hl=bn#native-audio-output) এবং
  [Gemini 2.5 Flash নেটিভ অডিও](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.5-flash-native-audio) দেখুন।
- `gemma-3n-e4b-it` প্রিভিউ রিলিজ করা হয়েছে, যা
  [AI Studio](https://aistudio.google.com?hl=bn)-তে এবং Gemini API-এর মাধ্যমে উপলভ্য,
  [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=bn) লঞ্চের অংশ হিসেবে।

## ৭ মে, ২০২৫

- ছবি তৈরি ও এডিট করার জন্য প্রিভিউ মডেল হিসেবে
  `gemini-2.0-flash-preview-image-generation` রিলিজ করা হয়েছে। আরও জানতে, [ছবি
  জেনারেট করা](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn) এবং
  [Gemini 2.0 Flash প্রিভিউ ছবি
  জেনারেট করা](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.0-flash-preview-image-generation) দেখুন।

## ৬ মে, ২০২৫

- কোড ও ফাংশন কলিংয়ে উন্নতি সহ আমাদের সবচেয়ে শক্তিশালী
  মডেলের নতুন ভার্সন `gemini-2.5-pro-preview-05-06` প্রকাশ করা হয়েছে। `gemini-2.5-pro-preview-03-25`
  মডেলের নতুন ভার্সনের দিকে অটোমেটিক পয়েন্ট করবে।

## ১৭ এপ্রিল, ২০২৫

- `gemini-2.5-flash-preview-04-17`-এ, Gemini
  [প্রিভিউ](https://ai.google.dev/gemini-api/docs/models?hl=bn#model-versions) মডেল রিলিজ করা হয়েছে যা
  দাম-পারফর্ম্যান্স ও অ্যাডাপ্টিভ থিঙ্কিংয়ের জন্য অপ্টিমাইজ করা হয়েছে। আরও জানতে, [Gemini 2.5 Flash প্রিভিউ](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.5-flash-preview)
  এবং [Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=bn) দেখুন।

## ১৬ এপ্রিল, ২০২৫

- [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.0-flash)-এর জন্য
  কনটেক্সট ক্যাশিং লঞ্চ করা হয়েছে।

## ৯ এপ্রিল, ২০২৫

**মডেল আপডেট:**

- `veo-2.0-generate-001` রিলিজ করা হয়েছে, এটি সাধারণভাবে উপলভ্য (GA) টেক্সট- ও
  ছবি-থেকে-ভিডিও মডেল, যা বিস্তারিত ও শৈল্পিক
  ভিডিও তৈরি করতে পারে। আরও জানতে, [Veo ডকুমেন্টেশন](https://ai.google.dev/gemini-api/docs/video?hl=bn) দেখুন।
- `gemini-2.0-flash-live-001` রিলিজ করা হয়েছে, এটি বিলিং চালু থাকা
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=bn) মডেলের পাবলিক প্রিভিউ ভার্সন।

  - **উন্নত সেশন ম্যানেজমেন্ট ও নির্ভরযোগ্যতা**

    - **সেশন আবার চালু করা:** সাময়িক নেটওয়ার্ক
      বিঘ্ন চলাকালীন সেশন চালু রাখা। API এখন সার্ভার-সাইড সেশন স্টেট স্টোরেজ (সর্বাধিক ২৪ ঘণ্টা পর্যন্ত) কাজ করে এবং আপনি যেখানে শেষ করেছিলেন সেখান থেকে আবার কানেক্ট ও
      চালু করার জন্য হ্যান্ডেল (session\_resumption) প্রদান করে।
    - **কন্টেক্সট কম্প্রেশনের মাধ্যমে দীর্ঘ সেশন:** আগের সময়সীমার বাইরেও
      বর্ধিত ইন্টার‍্যাকশন চালু করুন। কন্টেক্সট উইন্ডো কনফিগার করুন
      স্লাইডিং উইন্ডো মেকানিজমের মাধ্যমে কম্প্রেস করুন যাতে অটোমেটিক ম্যানেজ করা যায়
      কন্টেক্সট দৈর্ঘ্য। এর ফলে কন্টেক্সট সংক্রান্ত সীমার কারণে হঠাৎ করে বন্ধ হয়ে যাওয়া আটকানো যায়।
    - **কানেকশন বন্ধ হওয়ার বিজ্ঞপ্তি:** কানেকশন বন্ধ হওয়ার আগে `GoAway` সার্ভার
      মেসেজ পান, যাতে কানেকশন বন্ধ হওয়ার আগে
      প্রয়োজনীয় ব্যবস্থা নেওয়া যায়।
  - **ইন্টার‌্যাকশন ডায়নামিক্সের উপর আরও নিয়ন্ত্রণ**
  - **কনফিগার করা যায় এমন ভয়েস অ্যাক্টিভিটি ডিটেকশন (VAD):** সংবেদনশীলতার
    লেভেল বেছে নিন অথবা সম্পূর্ণভাবে অটোমেটিক VAD বন্ধ করে দিন এবং ম্যানুয়াল টার্ন কন্ট্রোলের জন্য নতুন ক্লায়েন্ট ইভেন্ট
    (`activityStart`, `activityEnd`) ব্যবহার করুন।
  - **কনফিগার করা যায় এমন ইন্টারাপশন হ্যান্ডলিং:** ব্যবহারকারীর ইনপুট
    মডেলের উত্তরে বাধা দেবে কিনা তা ঠিক করুন।
  - **কনফিগার করা যায় এমন টার্ন কভারেজ:** API সব
    অডিও ও ভিডিও ইনপুট একটানা প্রসেস করবে নাকি শুধু তখনই ক্যাপচার করবে যখন
    শেষ ব্যবহারকারীকে কথা বলতে দেখা যাবে তা বেছে নিন।
  - **কনফিগার করা যায় এমন মিডিয়া রেজোলিউশন:** ইনপুট মিডিয়ার জন্য রেজোলিউশন বেছে নিয়ে
    কোয়ালিটি বা টোকেন ব্যবহারের জন্য অপ্টিমাইজ করুন।
  - **আরও সমৃদ্ধ আউটপুট ও ফিচার**
  - **আরও বেশি ভয়েস ও ভাষার বিকল্প:** অডিও আউটপুটের জন্য দুটি নতুন ভয়েস ও
    ৩০টি নতুন ভাষা থেকে বেছে নিন। আউটপুট ভাষা এখন
    `speechConfig`-এর মধ্যে কনফিগার করা যাবে।
  - **টেক্সট স্ট্রিমিং:** টেক্সট উত্তর তৈরি হওয়ার সাথে সাথে ইনক্রিমেন্টাল হিসেবে তা পান, যাতে ব্যবহারকারীকে দ্রুত দেখানো যায়।
  - **টোকেন ব্যবহার সংক্রান্ত রিপোর্টিং:** সার্ভার মেসেজের `usageMetadata` ফিল্ডে দেওয়া বিস্তারিত
    টোকেন সংখ্যা থেকে ব্যবহার সম্পর্কে ইনসাইট পান,
    মোডালিটি ও প্রম্পট বা উত্তর ফেজ অনুযায়ী ভেঙে দেখানো হয়।

## ৪ এপ্রিল, ২০২৫

- `gemini-2.5-pro-preview-03-25`, বিলিং চালু করা পাবলিক প্রিভিউ Gemini 2.5 Pro ভার্সন
  প্রকাশ করা হয়েছে। আপনি ফ্রি টিয়ারে `gemini-2.5-pro-exp-03-25` ব্যবহার করা
  চালিয়ে যেতে পারবেন।

## ২৫ মার্চ, ২০২৫

- `gemini-2.5-pro-exp-03-25` রিলিজ করা হয়েছে, এটি একটি পাবলিক এক্সপেরিমেন্টাল Gemini মডেল
  যেখানে থিঙ্কিং মোড সবসময় ডিফল্ট হিসেবে চালু থাকে।
  আরও জানতে, [Gemini 2.5 Pro এক্সপেরিমেন্টাল](https://ai.google.dev/gemini-api/docs/models?hl=bn#gemini-2.5-pro-preview-03-25) দেখুন।

## ১২ মার্চ, ২০২৫

**মডেল আপডেট:**

- ছবি তৈরি ও এডিট করতে পারে এমন একটি এক্সপেরিমেন্টাল [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn#gemini)
  মডেল লঞ্চ করা হয়েছে।
- `gemma-3-27b-it`-এ রিলিজ করা হয়েছে, [AI Studio](https://aistudio.google.com?hl=bn)-তে এবং Gemini API-এর মাধ্যমে উপলভ্য,
  [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=bn) লঞ্চের অংশ হিসেবে।

**API আপডেট:**

- মিডিয়া সোর্স হিসেবে
  [YouTube URL](https://ai.google.dev/gemini-api/docs/vision?hl=bn#youtube)-এর জন্য সহায়তা যোগ করা হয়েছে।
- ২০ এমবির কম সাইজের
  [ইনলাইন ভিডিও](https://ai.google.dev/gemini-api/docs/vision?hl=bn#inline-video) যোগ করার সুবিধা যোগ করা হয়েছে।

## ১১ মার্চ, ২০২৫

**SDK আপডেট:**

- পাবলিক প্রিভিউতে
  [TypeScript ও JavaScript-এর জন্য Google Gen AI SDK](https://googleapis.github.io/js-genai)
  প্রকাশ করা হয়েছে।

## ৭ মার্চ, ২০২৫

**মডেল আপডেট:**

- পাবলিক প্রিভিউতে `gemini-embedding-exp-03-07`রিলিজ করা হয়েছে, একটি
  [পরীক্ষামূলক](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=bn)
  Gemini-ভিত্তিক এম্বেডিং মডেল।

## ২৮ ফেব্রুয়ারি, ২০২৫

**API আপডেট:**

- [টুল হিসেবে সার্চ করুন](https://ai.google.dev/gemini-api/docs/grounding?hl=bn)
  ফিচার `gemini-2.0-pro-exp-02-05`-এ যোগ করা হয়েছে, এটি Gemini 2.0 Pro-এর
  উপর ভিত্তি করে তৈরি একটি পরীক্ষামূলক মডেল।

## ২৫ ফেব্রুয়ারি, ২০২৫

**মডেল আপডেট:**

- `gemini-2.0-flash-lite` রিলিজ করা হয়েছে, এটি হল
  [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=bn#gemini-2.0-flash-lite)-এর একটি সাধারণভাবে উপলভ্য (GA) ভার্সন।
  এটি স্পিড, স্কেল ও খরচ কমানোর জন্য অপ্টিমাইজ করা হয়েছে।

## ১৯ ফেব্রুয়ারি, ২০২৫

**AI Studio আপডেট:**

- [অতিরিক্ত অঞ্চলে](https://ai.google.dev/gemini-api/docs/available-regions?hl=bn)
  (কসোভো, গ্রিনল্যান্ড ও ফ্যারো দ্বীপপুঞ্জ) সহায়তা।

**API আপডেট:**

- [অতিরিক্ত অঞ্চল](https://ai.google.dev/gemini-api/docs/available-regions?hl=bn)
  (কসোভো, গ্রিনল্যান্ড ও ফ্যারো দ্বীপপুঞ্জ)
  -এর জন্য সহায়তা।

## ১৮ ফেব্রুয়ারি, ২০২৫

**মডেল আপডেট:**

- Gemini 1.0 Pro আর কাজ করে না। কোন কোন মডেল কাজ করে তার তালিকা দেখতে, [Gemini মডেল](https://ai.google.dev/gemini-api/docs/models/gemini?hl=bn) দেখুন।

## ১১ ফেব্রুয়ারি, ২০২৫

**API আপডেট:**

- [OpenAI লাইব্রেরি কম্প্যাটিবিলিটি](https://ai.google.dev/gemini-api/docs/openai?hl=bn)
  সম্পর্কিত আপডেট।

## ৬ ফেব্রুয়ারি, ২০২৫

**মডেল আপডেট:**

- `imagen-3.0-generate-002` রিলিজ করা হয়েছে, এটি হল
  [Gemini API-তে Imagen 3](https://ai.google.dev/gemini-api/docs/imagen?hl=bn)-এর সাধারণভাবে উপলভ্য (GA) ভার্সন।

**SDK আপডেট:**

- পাবলিক প্রিভিউয়ের জন্য [Java-র জন্য Google Gen AI SDK](https://github.com/googleapis/java-genai)
  রিলিজ করা হয়েছে।

## ৫ ফেব্রুয়ারি, ২০২৫

**মডেল আপডেট:**

- `gemini-2.0-flash-001` রিলিজ করা হয়েছে, এটি
  [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=bn#gemini-2.0-flash)-এর জেনেরাল অ্যাভেইলেবিলিটি (GA) ভার্সন যা
  শুধুমাত্র টেক্সট আউটপুট সাপোর্ট করে।
- `gemini-2.0-pro-exp-02-05`-এ রিলিজ করা হয়েছে,
  Gemini 2.0 Pro-এর একটি [এক্সপেরিমেন্টাল](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=bn) পাবলিক
  প্রিভিউ ভার্সন।
- `gemini-2.0-flash-lite-preview-02-05`রিলিজ করা হয়েছে, একটি পরীক্ষামূলক পাবলিক
  প্রিভিউ [মডেল](https://ai.google.dev/gemini-api/docs/models/gemini?hl=bn#gemini-2.0-flash-lite)
  যা খরচ কমানোর জন্য অপ্টিমাইজ করা হয়েছে।

**API আপডেট:**

- কোড এক্সিকিউশনে
  [ফাইল ইনপুট ও গ্রাফ আউটপুট](https://ai.google.dev/gemini-api/docs/code-execution?hl=bn#input-output)
  ফিচার যোগ করা হয়েছে।

**SDK আপডেট:**

- জেনেরাল অ্যাভেইলেবিলিটি (GA)-তে
  [Python-এর জন্য Google Gen AI SDK](https://googleapis.github.io/python-genai/)
  রিলিজ করা হয়েছে।

## ২১ জানুয়ারি, ২০২৫

**মডেল আপডেট:**

- `gemini-2.0-flash-thinking-exp-01-21` রিলিজ করা হয়েছে, এটি
  [Gemini 2.0 Flash Thinking মডেল](https://ai.google.dev/gemini-api/docs/thinking?hl=bn)-এর
  পিছনে থাকা মডেলের লেটেস্ট প্রিভিউ ভার্সন।

## ১৯ ডিসেম্বর, ২০২৪

**মডেল আপডেট:**

- পাবলিক প্রিভিউয়ের জন্য Gemini 2.0 Flash Thinking মোড রিলিজ করা হয়েছে। Thinking Mode হল
  একটি টেস্ট-টাইম কম্পিউট মডেল যা কোনও উত্তর তৈরি করার সময়
  মডেলের চিন্তাভাবনা প্রক্রিয়া দেখতে দেয় এবং আরও শক্তিশালী
  যুক্তিপূর্ণ ক্ষমতা সহ উত্তর তৈরি করে।

  আমাদের [ওভারভিউ
  পৃষ্ঠা](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=bn) থেকে Gemini 2.0 Flash Thinking মোড সম্পর্কে আরও পড়ুন।

## ১১ ডিসেম্বর, ২০২৪

**মডেল আপডেট:**

- পাবলিক প্রিভিউয়ের জন্য [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=bn#gemini-2.0-flash)
  রিলিজ করা হয়েছে। Gemini 2.0 Flash Experimental-এর ফিচারের আংশিক তালিকা:
  - Gemini 1.5 Pro-এর থেকে দ্বিগুণ দ্রুত
  - আমাদের Live API-এর মাধ্যমে দ্বিমুখী স্ট্রিমিং
  - টেক্সট, ছবি ও স্পিচের মাধ্যমে মাল্টিমোডাল উত্তর জেনারেশন
  - কোড
    এক্সিকিউশন, সার্চ, ফাংশন কলিং ও আরও অনেক কিছুর মতো ফিচার ব্যবহার করতে মাল্টি-টার্ন রিজনিং সহ বিল্ট-ইন টুলের ব্যবহার

আমাদের [ওভারভিউ
পৃষ্ঠা](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=bn) থেকে Gemini 2.0 Flash সম্পর্কে আরও জানুন।

## ২১ নভেম্বর, ২০২৪

**মডেল আপডেট:**

- `gemini-exp-1121` রিলিজ করা হয়েছে, এটি আরও শক্তিশালী পরীক্ষামূলক Gemini API মডেল।

**মডেল আপডেট:**

- `gemini-1.5-flash-002` ব্যবহার করার জন্য `gemini-1.5-flash-latest` এবং `gemini-1.5-flash` মডেলের ছদ্মনাম আপডেট করা হয়েছে।
  - `top_k` প্যারামিটার পরিবর্তন করুন: `gemini-1.5-flash-002`
    মডেল ১ থেকে ৪১ (এক্সক্লুসিভ) পর্যন্ত `top_k` ভ্যালু সাপোর্ট করে।
    ৪০-এর বেশি ভ্যালু ৪০-এ পরিবর্তন করা হবে।

## ১৪ নভেম্বর, ২০২৪

**মডেল আপডেট:**

- `gemini-exp-1114` রিলিজ করা হয়েছে, এটি একটি শক্তিশালী পরীক্ষামূলক Gemini API মডেল।

## ৮ নভেম্বর, ২০২৪

**API আপডেট:**

- OpenAI লাইব্রেরি / REST API-তে [Gemini-র জন্য সহায়তা](https://ai.google.dev/gemini-api/docs/openai?hl=bn) যোগ করা হয়েছে।

## ৩১ অক্টোবর, ২০২৪

**API আপডেট:**

- [Grounding with Google Search-এর জন্য সহায়তা](https://ai.google.dev/gemini-api/docs/grounding?hl=bn) যোগ করা হয়েছে।

## ৩ অক্টোবর, ২০২৪

**মডেল আপডেট:**

- আমাদের সবচেয়ে ছোট Gemini
  API মডেলের স্টেবল ভার্সন `gemini-1.5-flash-8b-001` রিলিজ করা হয়েছে।

## ২৪ সেপ্টেম্বর, ২০২৪

**মডেল আপডেট:**

- সাধারণ উপলভ্যতার জন্য Gemini 1.5 Pro ও 1.5 Flash-এর দুটি নতুন স্টেবল
  ভার্সন `gemini-1.5-pro-002` ও `gemini-1.5-flash-002` রিলিজ করা হয়েছে।
- `gemini-1.5-pro-002` ব্যবহার করার জন্য `gemini-1.5-pro-latest` মডেল কোড
  এবং `gemini-1.5-flash-002` ব্যবহার করার জন্য `gemini-1.5-flash-latest` মডেল কোড আপডেট করা হয়েছে।
- `gemini-1.5-flash-8b-exp-0827`-এর পরিবর্তে `gemini-1.5-flash-8b-exp-0924` রিলিজ করা হয়েছে।
- Gemini API এবং AI Studio-র জন্য [নাগরিকের সততা সংক্রান্ত সুরক্ষা ফিল্টার](https://ai.google.dev/gemini-api/docs/safety-settings?hl=bn#safety-filters)
  রিলিজ করা হয়েছে।
- Python ও NodeJS-এ Gemini 1.5 Pro ও 1.5 Flash-এর জন্য দুটি নতুন প্যারামিটার রিলিজ করা হয়েছে:
  [`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=bn#FIELDS.frequency_penalty) এবং
  [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=bn#FIELDS.presence_penalty)।

## ১৯ সেপ্টেম্বর, ২০২৪

**AI Studio আপডেট:**

- মডেলের দেওয়া উত্তরে থাম্বস-আপ ও থাম্বস-ডাউন বোতাম যোগ করা হয়েছে, যাতে ব্যবহারকারীরা
  উত্তরের কোয়ালিটি সম্পর্কে মতামত জানাতে পারেন।

**API আপডেট:**

- Google Cloud ক্রেডিটের জন্য সহায়তা যোগ করা হয়েছে, যা এখন Gemini API ব্যবহারের জন্য
  ব্যবহার করা যেতে পারে।

## ১৭ সেপ্টেম্বর, ২০২৪

**AI Studio আপডেট:**

- **Colab-এ খুলুন** বোতাম যোগ করা হয়েছে যা একটি Colab নোটবুকে প্রম্পট – এবং এটি রান করানোর
  কোড – এক্সপোর্ট করে। এই ফিচারে এখনও
  টুল (JSON মোড, ফাংশন কলিং বা কোড এক্সিকিউশন) সহ প্রম্পট করার সুবিধা নেই।

## ১৩ সেপ্টেম্বর, ২০২৪

**AI Studio আপডেট:**

- তুলনা মোডের জন্য সহায়তা যোগ করা হয়েছে, যা আপনাকে বিভিন্ন মডেল ও প্রম্পট জুড়ে উত্তর তুলনা করতে দেয় যাতে আপনার ব্যবহারের ক্ষেত্রে সবচেয়ে উপযুক্ত উত্তর খুঁজে পেতে পারেন।

## ৩০ আগস্ট, ২০২৪

**মডেল আপডেট:**

- Gemini 1.5 Flash-এ
  [মডেল কনফিগারেশনের মাধ্যমে JSON স্কিমা প্রদান করা](https://ai.google.dev/gemini-api/docs/json-mode?hl=bn#supply-schema-in-config) যায়।

## ২৭ আগস্ট, ২০২৪

**মডেল আপডেট:**

- নিম্নলিখিত
  [পরীক্ষামূলক মডেল](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=bn) রিলিজ করা হয়েছে:
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## ৯ আগস্ট, ২০২৪

**API আপডেট:**

- [PDF প্রসেস করার](https://ai.google.dev/gemini-api/docs/document-processing?hl=bn) জন্য অতিরিক্ত সহায়তা।

## ৫ আগস্ট, ২০২৪

**মডেল আপডেট:**

- Gemini 1.5 Flash-এর জন্য ফাইন-টিউনিং সাপোর্ট রিলিজ করা হয়েছে।

## ১ আগস্ট, ২০২৪

**মডেল আপডেট:**

- `gemini-1.5-pro-exp-0801`-এ, [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=bn#gemini-1.5-pro)-এর একটি নতুন এক্সপেরিমেন্টাল ভার্সন রিলিজ করা হয়েছে।

## ১২ জুলাই, ২০২৪

**মডেল আপডেট:**

- Google AI পরিষেবা ও টুল থেকে Gemini 1.0 Pro Vision-এর জন্য সহায়তা সরিয়ে দেওয়া হয়েছে।

## ২৭ জুন, ২০২৪

**মডেল আপডেট:**

- Gemini 1.5 Pro-এর 2M কনটেক্সট উইন্ডোর জন্য জেনেরাল অ্যাভেইলেবিলিটি রিলিজ।

**API আপডেট:**

- [কোড এক্সিকিউশন](https://ai.google.dev/gemini-api/docs/code-execution?hl=bn)-এর জন্য সহায়তা যোগ করা হয়েছে।

## ১৮ জুন, ২০২৪

**API আপডেট:**

- [কন্টেক্সট ক্যাশে করার](https://ai.google.dev/gemini-api/docs/caching?hl=bn) জন্য সহায়তা যোগ করা হয়েছে।

## ১২ জুন, ২০২৪

**মডেল আপডেট:**

- Gemini 1.0 Pro Vision বন্ধ করে দেওয়া হয়েছে।

## ২৩ মে, ২০২৪

**মডেল আপডেট:**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=bn#gemini-1.5-pro)
  (`gemini-1.5-pro-001`) সাধারণত উপলভ্য (GA)।
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=bn#gemini-1.5-flash)
  (`gemini-1.5-flash-001`) সাধারণভাবে উপলভ্য (GA)।

## ১৪ মে, ২০২৪

**API আপডেট:**

- Gemini 1.5 Pro-এর জন্য 2M কনটেক্সট উইন্ডো চালু করা হয়েছে (অপেক্ষা তালিকা)।
- Gemini 1.0 Pro-এর জন্য 'যখন ব্যবহার করবেন তখন পেমেন্ট করুন' [বিলিং](https://ai.google.dev/gemini-api/docs/billing?hl=bn) চালু করা হয়েছে, Gemini 1.5 Pro এবং Gemini 1.5 Flash-এর জন্য বিলিং শীঘ্রই চালু করা হবে।
- Gemini 1.5 Pro-এর আসন্ন পেড টিয়ারের জন্য রেট লিমিট বাড়ানো হয়েছে।
- [File API](https://ai.google.dev/api/rest/v1beta/files?hl=bn)-তে বিল্ট-ইন ভিডিও সাপোর্ট যোগ করা হয়েছে।
- [File API](https://ai.google.dev/api/rest/v1beta/files?hl=bn)-তে প্লেন টেক্সট কাজ করে।
- প্যারালাল ফাংশন কলিংয়ের জন্য সহায়তা যোগ করা হয়েছে, যা একবারে একাধিক কল
  ফেরত পাঠায়।

## ১০ মে, ২০২৪

**মডেল আপডেট:**

- প্রিভিউতে [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=bn#gemini-1.5-flash)
  (`gemini-1.5-flash-latest`) রিলিজ করা হয়েছে।

## ৯ এপ্রিল, ২০২৪

**মডেল আপডেট:**

- প্রিভিউতে [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=bn#gemini-1.5-pro)
  (`gemini-1.5-pro-latest`) রিলিজ করা হয়েছে।
- নতুন টেক্সট এম্বেডিং মডেল, `text-embeddings-004` রিলিজ করা হয়েছে, যা 768-এর কম সাইজের
  [ইলাস্টিক এম্বেডিং](https://ai.google.dev/gemini-api/docs/embeddings?hl=bn#elastic-embedding)
  সাপোর্ট করে।

**API আপডেট:**

- প্রম্পটে ব্যবহারের জন্য সাময়িকভাবে মিডিয়া ফাইল স্টোর করতে [File API](https://ai.google.dev/api/rest/v1beta/files?hl=bn) রিলিজ করা হয়েছে।
- টেক্সট, ছবি ও অডিও ডেটার মাধ্যমে প্রম্পট করার সুবিধা যোগ করা হয়েছে, যা
  *মাল্টিমোডাল* প্রম্পটিং নামেও পরিচিত। আরও জানতে, [মিডিয়া সহ প্রম্পট করা](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=bn) দেখুন।
- [সিস্টেম নির্দেশাবলী](https://ai.google.dev/gemini-api/docs/system-instructions?hl=bn)
  বিটাতে রিলিজ করা হয়েছে।
- যোগ করা হয়েছে
  [ফাংশন কলিং মোড](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn#function_calling_mode),
  যা ফাংশন কলিংয়ের জন্য এক্সিকিউশন আচরণকে সংজ্ঞায়িত করে।
- `response_mime_type` কনফিগারেশন বিকল্পের জন্য সহায়তা যোগ করা হয়েছে, যা আপনাকে
  [JSON ফর্ম্যাটে](https://ai.google.dev/gemini-api/docs/api-overview?hl=bn#json)
  উত্তর দেওয়ার অনুরোধ করতে দেয়।

## ১৯ মার্চ, ২০২৪

**মডেল আপডেট:**

- Google AI Studio-তে অথবা Gemini API-এর মাধ্যমে
  [Gemini 1.0 Pro টিউনিং করার](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/)
  জন্য সহায়তা যোগ করা হয়েছে।

## ১৩ ডিসেম্বর ২০২৩

**মডেল আপডেট:**

- gemini-pro: বিভিন্ন ধরনের টাস্কের জন্য নতুন টেক্সট মডেল। ক্ষমতা ও দক্ষতার
  মধ্যে ভারসাম্য বজায় রাখে।
- gemini-pro-vision: বিভিন্ন ধরনের টাস্কের জন্য নতুন মাল্টিমোডাল মডেল।
  ক্ষমতা ও দক্ষতার মধ্যে ভারসাম্য বজায় রাখে।
- embedding-001: নতুন এম্বেডিং মডেল।
- aqa: একটি নতুন বিশেষভাবে টিউন করা মডেল যা প্রশ্নের উত্তর দেওয়ার জন্য প্রশিক্ষিত
  জেনারেট করা উত্তর গ্রাউন্ডিং করার জন্য টেক্সট প্যাসেজ ব্যবহার করে।

আরও তথ্যের জন্য [Gemini মডেল](https://ai.google.dev/gemini-api/docs/models/gemini?hl=bn) দেখুন।

**API ভার্সন আপডেট:**

- v1: স্থিতিশীল API চ্যানেল।
- v1beta: বিটা চ্যানেল। এই চ্যানেলে এমন ফিচার আছে যা
  ডেভেলপ করা হচ্ছে।

আরও তথ্যের জন্য [API ভার্সন সংক্রান্ত বিষয়](https://ai.google.dev/gemini-api/docs/api-versions?hl=bn) দেখুন।

**API আপডেট:**

- `GenerateContent` হল চ্যাট ও টেক্সটের জন্য একটি একক ইউনিফায়েড এন্ডপয়েন্ট।
- `StreamGenerateContent` পদ্ধতির মাধ্যমে স্ট্রিমিং উপলভ্য।
- মাল্টিমোডাল ক্ষমতা: ছবি হল নতুন সমর্থিত মোডালিটি
- নতুন বিটা ফিচার:
  - [ফাংশন কলিং](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn)
  - Attributed Question Answering (AQA)
- আপডেট করা ক্যান্ডিডেট সংখ্যা: Gemini মডেল শুধুমাত্র ১টি ক্যান্ডিডেট দেখায়।
- বিভিন্ন Safety Settings এবং SafetyRating বিভাগ। আরও বিবরণের জন্য
  [নিরাপত্তা সেটিংস](https://ai.google.dev/gemini-api/docs/safety-settings?hl=bn) দেখুন।
- Gemini মডেলের জন্য টিউনিং মডেল এখনও কাজ করে না (কাজ চলছে)।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-14 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-14 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
