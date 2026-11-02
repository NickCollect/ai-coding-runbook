---
source_url: https://ai.google.dev/gemini-api/docs/cli?hl=bn
fetched_at: 2026-11-02T07:02:58.510601+00:00
title: "Gemini API CLI \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# Gemini API CLI

Gemini API CLI (`gemini-api`) হল একটি স্টেটলেস, জিরো-ডিপেন্ডেন্সি কমান্ড-লাইন
ক্লায়েন্ট যা শেল অ্যাক্সেস সহ AI এজেন্টের জন্য তৈরি করা হয়েছে (এবং স্ক্রিপ্ট ও CI থেকে ব্যবহারযোগ্য)।
আপনার কোডিং এজেন্ট
তারপর টেক্সট ও মিডিয়া তৈরি করতে, ফাইল বিশ্লেষণ করতে এবং
[Gemini ম্যানেজ করা এজেন্ট](https://ai.google.dev/gemini-api/docs/agents?hl=bn)-কে টাস্ক ডেলিগেট করতে পারবে। এটি Antigravity,
Claude Code, Codex, Cursor, OpenClaw, Hermes বা যেকোনও শেল এনভায়রনমেন্টের সাথে কাজ করে।

প্রতিটি ফিচার [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=bn)-তে
স্ট্যান্ডার্ড শেল কমান্ড হিসেবে রান করে। এজেন্ট সাবপ্রসেস, আপনার টার্মিনাল বা CI পাইপলাইন থেকে একই
কমান্ড রান করুন:

```
# 1. Install on macOS or Linux
curl -fsSL https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.sh | bash

# 2. Set your API key
export GEMINI_API_KEY="YOUR_API_KEY"

# 3. Generate media, analyze a file, or launch a background managed agent
gemini-api image "Minimalist isometric icon of a cloud database" --out ./assets/db-icon.jpg
gemini-api analyze -i ./docs/quarterly-report.pdf "Summarize the key findings in three bullets."
gemini-api agent run "Compare WebRTC SFU architectures and cite sources" \
  --agent deep-research-preview-04-2026 \
  --background \
  --stream=false
```

## সঠিক Gemini টুল বেছে নিন

আপনার প্রোজেক্টে SDK কোড যোগ না করে শেল থেকে সরাসরি Gemini-কে **কল** করার জন্য কোনও এজেন্ট বা স্ক্রিপ্টের প্রয়োজন হলে `gemini-api` ব্যবহার করুন। আপনি যখন কোনও অ্যাপ্লিকেশনে Gemini **বিল্ড**
করছেন তখন SDK এবং
[কোডিং এজেন্ট সেট-আপ](https://ai.google.dev/gemini-api/docs/coding-agents?hl=bn) ব্যবহার করুন:

| টুল | এর কাজ কী | কখন ব্যবহার করবেন |
| --- | --- | --- |
| **Gemini API CLI** (`gemini-api`) | যেকোনও শেল থেকে Gemini মডেল ও ম্যানেজ করা এজেন্টকে কল করে। | আপনার কোডিং এজেন্ট, শেল স্ক্রিপ্ট বা CI জবকে মিডিয়া তৈরি করতে, ফাইল বিশ্লেষণ করতে বা কোনও প্রোজেক্টের উপর নির্ভর না করে ব্যাকগ্রাউন্ড রিসার্চ এজেন্ট চালাতে হবে। |
| **[Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=bn)** | Python, TypeScript, JavaScript, Go, Java বা C# কোডে Gemini ক্লায়েন্ট লাইব্রেরি ইমপোর্ট করে। | আপনি নিজের অ্যাপ্লিকেশন, ব্যাকএন্ড পরিষেবা বা রিয়েল-টাইম [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=bn) সেশনে Gemini ফিচার তৈরি করছেন। |
| **[Gemini Docs MCP ও স্কিল](https://ai.google.dev/gemini-api/docs/coding-agents?hl=bn)** | কোডিং এজেন্টদের লাইভ ডকুমেন্টেশন সার্চ এবং বর্তমান SDK নিয়ম প্রদান করে। | আপনার কোডিং এজেন্ট অ্যাপ্লিকেশন কোড লিখছে যা Google GenAI SDK ইমপোর্ট করে। |

## এটি কীভাবে কাজ করে

র REST কল এবং ইন্টার‍্যাক্টিভ CLI-এর কারণে প্রায়ই কোডিং এজেন্টের সমস্যা হয়। Base64
মিডিয়া কনটেক্সট উইন্ডো পূরণ করে, ইন্টার‍্যাক্টিভ প্রম্পট সাবপ্রসেস ব্লক করে এবং পুরনো
ট্রেনিং ডেটার কারণে হ্যালুসিনেটেড ফ্ল্যাগ দেখা যায়।

চারটি ডিজাইন সংক্রান্ত পছন্দ এজেন্টদের জন্য `gemini-api`-কে নির্ভরযোগ্য করে তোলে:

- **অফলাইন স্কিমা লুক-আপ:** কমান্ড ট্রি ([KDL](https://kdl.dev)-এ) প্রিন্ট করতে `--usage` পাস করুন অথবা `--body`
  অনুরোধের জন্য JSON স্কিমা প্রিন্ট করতে `--schema` পাস করুন।
- **ডিস্কে ফাইল, `stdout`-এ পাথ:** মিডিয়া ও ট্রান্সক্রিপশন কমান্ড ডিস্কে ফাইল লেখে এবং শুধু আউটপুট পাথ প্রিন্ট করে, বাইনারি ডেটা কনটেক্সটের বাইরে রাখে।
- **ড্রাই রান ও স্ট্রাকচার্ড আউটপুট:** `--dry-run` ইনপুট যাচাই করে, ক্রেডেনশিয়াল
  এডিট করে এবং অফলাইনে HTTP অনুরোধের প্রিভিউ দেখায়। মেশিনের ক্ষেত্রে গ্রহণযোগ্য আউটপুটের জন্য
  `-o json`, `-o toon` বা `--jq` পাস করুন। `stderr`-এ স্ট্রাকচার্ড JSON সমস্যা
  ফেরত পেতে `--agent-mode` যোগ করুন এবং
  ব্যর্থতা ম্যানেজ করতে [এক্সিট কোড](https://ai.google.dev/gemini-api/docs/cli?hl=bn#exit-codes) চেক করুন। আপনি `--interactive` পাস না করলে
  কমান্ড কখনই প্রম্পট করে না।
- **ডিফল্ট হিসেবে স্টেটলেস:** কমান্ড কোনও লুকানো লোকাল স্টেট রাখে না। চেন
  `--previous-interaction-id`, আপলোড করা
  `files/<id>` URI বা ব্যাকগ্রাউন্ড ইন্টার‍্যাকশন আইডির সাথে স্পষ্টভাবে মাল্টি-স্টেপ কাজ।

`-o json`-এর মাধ্যমে, মিডিয়া কমান্ড এখনও ডিস্কে ফাইল লেখে এবং `stdout`-এ মেটাডেটা
প্রিন্ট করে:

```
{
  "kind": "image",
  "mime_type": "image/jpeg",
  "path": "/path/to/project/assets/db-icon.jpg",
  "response_id": "v1_...",
  "size_bytes": 2914159,
  "status": "completed"
}
```

## শুরু করুন

CLI ইনস্টল করুন, আপনার `PATH`-এ `gemini-api` রাখুন, `GEMINI_API_KEY` সেট করুন এবং আপনার কোডিং এজেন্টে
ব্যবহারের নিয়ম যোগ করুন।

### ১. বাইনারি ইনস্টল করুন

### macOS এবং Linux

```
curl -fsSL https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.sh | bash
```

নির্দিষ্ট রিলিজ ইনস্টল করতে, `GEMINI_VERSION`-কে রিলিজ ট্যাগে সেট করুন:

```
curl -fsSL https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.sh | GEMINI_VERSION=<release-tag> bash
```

### Windows (PowerShell)

```
iwr -useb https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.ps1 | iex
```

### খুলুন

```
go install github.com/google-gemini/gemini-api-cli/cmd/gemini-api@latest
```

### প্রি-বিল্ট বাইনারি

[GitHub রিলিজ](https://github.com/google-gemini/gemini-api-cli/releases)
থেকে macOS, Linux ও Windows-এর জন্য ভার্সন করা আর্কাইভ ডাউনলোড করুন
এবং আপনার `PATH`-এ `gemini-api` রাখুন। Docker ইমেজ ও CI-তে সঠিক ভার্সন পিন করতে
আগে থেকে তৈরি আর্কাইভ ব্যবহার করুন।

### ২. যাচাইকরণ কনফিগার ও যাচাই করুন

[Google AI Studio](https://aistudio.google.com/apikey?hl=bn)-তে একটি API key তৈরি করুন (
[API key](https://ai.google.dev/gemini-api/docs/api-key?hl=bn) দেখুন)। আপনার শেলে `GEMINI_API_KEY` সেট করুন এবং
আপনার এজেন্টের সাবপ্রসেস এনভায়রনমেন্ট:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

লোকাল ওয়ার্কস্টেশনে, আপনি নিজের OS কীচেনে (macOS
কীচেন, Linux সিক্রেট সার্ভিস বা Windows ক্রেডেনশিয়াল ম্যানেজার) 'কী' সেভ করতে পারবেন। পরিবর্তে `~/.config/gemini-api/config.yaml`-এ 'কী' স্টোর করতে `--no-keyring` পাস করুন:

```
# Save to your OS keychain (or run gemini-api configure --interactive)
gemini-api configure --api-key "YOUR_API_KEY"

# Check the active credential source, then preview a request offline
gemini-api whoami
gemini-api generate "Confirm CLI setup in one sentence." --dry-run
```

### ৩. আপনার এজেন্টকে নির্দেশাবলী দিন

আপনার প্রোজেক্টের `AGENTS.md`, `CLAUDE.md`, `.cursorrules` বা
সিস্টেম প্রম্পটে এই স্নিপেট যোগ করুন যাতে আপনার কোডিং এজেন্ট জানতে পারে যে কীভাবে `gemini-api` ব্যবহার করতে হয়:

```
## Gemini API CLI (`gemini-api`)

You have access to `gemini-api` through the shell. Use it to generate text or media (images, speech, music, video), analyze documents and recordings, or run and manage Gemini managed agents.

1. Run `gemini-api --help` or `gemini-api --usage` to choose a command, and `gemini-api <command> --schema` before building a `--body` JSON payload.
2. Preview unfamiliar or complex calls offline with `--dry-run -o json`.
3. For a single JSON result or `--jq` filtering on `generate` or `agent run`, pass `--stream=false -o json`.
4. To chain multi-step workflows, capture the output paths that media and transcription commands print to stdout, and the `id` values returned by `generate` or `agent run`.
```

তারপর আপনার কোডিং এজেন্টকে আগের মতোই প্রম্পট করুন:

```
Build a landing page for our developer tool. Use Gemini to generate a hero
illustration and a 15-second welcome voiceover, and start a background Deep
Research agent to compare competing CLI onboarding flows. Wire the assets and
findings into the page.
```

## কমান্ড

সব কমান্ডের তালিকা দেখতে `gemini-api --help` রান করুন অথবা ইন্টার‍্যাক্টিভভাবে সেগুলি ব্রাউজ করতে
`gemini-api explore` রান করুন।

| গ্রুপ | কমান্ড | এর কাজ কী |
| --- | --- | --- |
| তৈরি করুন | `image` | ছবি তৈরি বা এডিট করে (`-i`), JPEG ফাইল লেখে এবং এর পাথ প্রিন্ট করে। |
| তৈরি করুন | `tts` | ২৪ kHz মোনো WAV স্পিচ (এক বা দুটি স্পিকার) সিন্থেসাইজ করে এবং আউটপুট পাথ প্রিন্ট করে। |
| তৈরি করুন | `music` | মিউজিক ট্র্যাক বা লুপ জেনারেট করে, অডিও ফাইল লেখে এবং এর পাথ প্রিন্ট করে। |
| তৈরি করুন | `video` | MP4 ক্লিপ জেনারেট বা এডিট করে এবং সম্পূর্ণ না হওয়া পর্যন্ত অপেক্ষা করে (`--async` অবিলম্বে একটি আইডি রিটার্ন করে)। |
| তৈরি করুন | `generate` | টেক্সট জেনারেট করে এবং `stdout`-এ স্ট্রিম করে (`--stream=false` একটি সম্পূর্ণ ফলাফল রিটার্ন করে)। |
| বোঝা | `analyze` | PDF, ছবি, অডিও, ভিডিও, CSV ও টেক্সট ফাইল বা সর্বজনীন YouTube URL সম্পর্কে প্রশ্নের উত্তর দেয়। |
| বোঝা | `transcribe` | স্পিকার-লেবেলযুক্ত, টাইমস্ট্যাম্প করা ট্রান্সক্রিপ্ট (`md`, `text`, `json`, অথবা `srt`) লেখে এবং আউটপুট পাথ প্রিন্ট করে। |
| এজেন্ট ম্যানেজ করা | `agent` | ম্যানেজ করা এজেন্ট (`run`, `status`, `cancel`, `delete-interaction`) রান করে এবং কাস্টম এজেন্ট সংজ্ঞা (`create`, `list`, `get`, `delete`) ম্যানেজ করে। |
| এজেন্ট ম্যানেজ করা | `environments`, `credentials`, `webhooks`, `triggers` | ম্যানেজ করা এজেন্টের জন্য স্যান্ডবক্স এনভায়রনমেন্ট, সেভ করা ক্রেডেনশিয়াল, ওয়েবহুক ডেলিভারি এবং শিডিউল করা রান কনফিগার করে। |
| সেট-আপ ও ফাইল | `configure`, `auth`, `whoami` | ক্রেডেনশিয়াল ও ডিফল্ট কনফিগার করে এবং অ্যাক্টিভ যাচাইকরণের স্ট্যাটাস দেখায়। |
| সেট-আপ ও ফাইল | `files` | Files API-তে ফাইল আপলোড, তালিকাভুক্ত, পরিদর্শন ও মুছে দেয়। |
| সেট-আপ ও ফাইল | `models` | উপলভ্য মডেলের তালিকা দেখায়। |

## ওয়ার্কফ্লো

প্রতিটি কমান্ড ডিফল্ট হিসেবে এমন একটি মডেল ব্যবহার করে যা তার টাস্কের জন্য উপযুক্ত। অন্য মডেল বেছে নিতে
`--model` (`-m`) পাস করুন। উপলভ্য বিকল্পের তালিকা দেখতে `gemini-api models` রান করুন।

### ইমেজ জেনারেশন ও এডিটিং

ওয়েব বা মোবাইল UI তৈরি করা এজেন্টরা [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn)-এর সাহায্যে প্লেসহোল্ডার, আইকন ও অনেক বড় ছবি
জেনারেট করতে পারবেন। ছবি এডিট করতে `-i`-এর সাথে জেনারেট করা
পাথ পাস করুন:

```
# Generate a 16:9 image at 2K resolution (512, 1K, 2K, or 4K) and capture its path
HERO_PATH=$(gemini-api image "Friendly robot mascot in a sunlit workshop, space on left for headline" \
  --aspect-ratio 16:9 \
  --image-size 2K \
  --out ./public/images/hero.jpg)

# Edit the generated image
gemini-api image "Add a winter scarf and soft snowfall outside the window" \
  -i "$HERO_PATH" \
  --out ./public/images/hero-winter.jpg
```

রেফারেন্স ইমেজ একত্রিত করতে `-i` একাধিকবার পাস করুন, যেমন কোনও চরিত্র এবং
স্টাইল গাইড।

### টেক্সট-টু-স্পিচ

`gemini-api tts` UI কিউ, অ্যাক্সেসিবিলিটি প্রিভিউ এবং ন্যারেট করা ওয়াকথ্রু-এর জন্য ২৪ kHz WAV অডিও সিন্থেসাইজ করে। ডিফল্ট ভয়েস হল `Kore`; `--voice`-এর মাধ্যমে
অন্য একটি বেছে নিন। দুই-স্পিকারের ডায়ালগের জন্য, প্রম্পটে প্রতিটি টার্ন লেবেল করুন এবং
স্পিকারদের ভয়েসের সাথে ম্যাপ করুন:

```
gemini-api tts "Build succeeded. All integration tests passed." \
  --voice Aoede \
  --out ./public/audio/build-ok.wav

gemini-api tts "Alice: Welcome to the release walkthrough! Bob: Let's look at what shipped today." \
  --multi-speaker "Alice=Kore,Bob=Puck" \
  --out ./public/audio/release-intro.wav
```

### মিউজিক ও ভিডিও

[Lyria](https://ai.google.dev/gemini-api/docs/music-generation?hl=bn)-র সাহায্যে আসল ট্র্যাক কম্পোজ করুন এবং
[Gemini Omni](https://ai.google.dev/gemini-api/docs/video?hl=bn)-র সাহায্যে MP4 ক্লিপ তৈরি করুন:

```
gemini-api music "Warm ambient synth and acoustic guitar background loop, 95 BPM" \
  --out ./public/audio/bg-loop.mp3

gemini-api video "A drone shot of a mountain landscape at sunrise." \
  --aspect-ratio 16:9 \
  --resolution 1080p \
  --out ./public/video/mountain-sunrise.mp4
```

ডিফল্ট হিসেবে, `video` কমান্ড জেনারেশন শেষ হওয়ার জন্য অপেক্ষা করে এবং ডিস্কে
MP4 ফাইল লেখে। অবিলম্বে ইন্টার‍্যাকশন আইডি ফেরত পেতে `--async` পাস করুন, তারপর
পরে `gemini-api video --resume <id> --out <path>` রান করুন। আগে থেকে থাকা ছবি অ্যানিমেট করতে
`-i` পাস করুন।

### টেক্সট তৈরি করা

`gemini-api generate` `stdout`-এ টেক্সট স্ট্রিম করে:

```
gemini-api generate "Write a one-paragraph welcome message for new users of a note-taking app."
```

প্রম্পটে পাইপ টেক্সট করতে `--stdin` যোগ করুন। আগের ইন্টার‍্যাকশন চালিয়ে যেতে
`--previous-interaction-id` পাস করুন।

### ডকুমেন্ট বিশ্লেষণ ও ট্রান্সক্রিপশন

`analyze` PDF, স্প্রেডশিট, স্ক্রিনশট, অডিও ও ভিডিও ফাইল এবং সর্বজনীন YouTube URL সম্পর্কে প্রশ্নের উত্তর দেয়। `transcribe` ডিস্কে ফর্ম্যাট করা ট্রান্সক্রিপ্ট
(`md`, `text`, `json`, অথবা `srt`) লেখে:

```
gemini-api analyze -i ./docs/product-brief.pdf "List the open questions and who owns each one." > open-questions.md

gemini-api transcribe -i ./fixtures/customer-call.mp4 --format srt --out ./fixtures/customer-call.srt
```

ফাইল তুলনা করতে `analyze`-এ একাধিকবার `-i` পাস করুন, যেমন আগে-ও-পরে
স্ক্রিনশট।

`gemini-api` সর্বাধিক ১৪ এমবি (base64 এনকোডিংয়ের পরে ২০ এমবি) পর্যন্ত লোকাল ফাইল ইনলাইন পাঠায়।
বড় ফাইলের ক্ষেত্রে, `files upload --wait`-এর মাধ্যমে একবার আপলোড করুন এবং ফেরত পাওয়া
`files/<id>` URI আবার ব্যবহার করুন:

```
FILE_URI=$(gemini-api files upload ./recordings/all-hands.mp4 --wait)

gemini-api analyze -i "$FILE_URI" "List action items with owners and timestamps."
gemini-api transcribe -i "$FILE_URI" --format json --out ./recordings/all-hands.json
```

### এজেন্ট রান ও ম্যানেজ করা

আপনার কোডিং এজেন্ট, মাল্টি-স্টেপ রিসার্চ বা স্যান্ডবক্স করা টাস্ক
[Gemini ম্যানেজড এজেন্ট](https://ai.google.dev/gemini-api/docs/agents?hl=bn)-কে ডেলিগেট করতে পারে, যেমন
[Deep Research এজেন্ট](https://ai.google.dev/gemini-api/docs/deep-research?hl=bn)। স্ট্রিম খোলা রাখার পরিবর্তে অবিলম্বে একটি ইন্টার‍্যাকশন আইডি পেতে
`--background --stream=false` পাস করুন:

```
# Launch a Deep Research job in the background and capture its interaction ID
RESEARCH_ID=$(gemini-api agent run "Compare open-source vector index benchmarks and cite primary papers." \
  --agent deep-research-preview-04-2026 \
  --background \
  --stream=false \
  --jq '.id')

# Check status or fetch the finished result while continuing other work
gemini-api agent status "$RESEARCH_ID" -o json
```

চলমান কাজ বন্ধ করতে `gemini-api agent cancel <id>` রান করুন। এছাড়াও, আপনি `agent run`-এর সাহায্যে
রিমোট স্যান্ডবক্সে [Antigravity এজেন্ট](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=bn)
লঞ্চ করতে পারেন অথবা `agent create`, `list`, `get` ও `delete`-এর সাহায্যে
[কাস্টম এজেন্ট](https://ai.google.dev/gemini-api/docs/custom-agents?hl=bn) ম্যানেজ করতে পারেন। এজেন্ট স্যান্ডবক্স কনফিগার করতে
[এনভায়রনমেন্ট](https://ai.google.dev/gemini-api/docs/agent-environment?hl=bn) দেখুন।

## কাস্টম অনুরোধের প্রধান অংশ

ডেডিকেটেড ফ্ল্যাগ ছাড়া বিকল্পের জন্য,
`--body` (ইনলাইন বা `@file.json` হিসেবে) সহ একটি র [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=bn) JSON পেলোড পাস করুন। `response_format`
স্কিমা, ফাংশন-কলিং টুল, `generation_config` বা `"store": false` সেট করতে `--body` পাস করুন। সঠিক ফিল্ড চেক করতে প্রথমে
`gemini-api <command> --schema` রান করুন:

```
# Inspect the JSON Schema for the request body
gemini-api generate --schema > generate-schema.json

# Return schema-constrained JSON and skip storing the interaction
cat logs.txt | gemini-api generate "Extract every error message from these logs." \
  --stdin \
  --body '{
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {"errors": {"type": "array", "items": {"type": "string"}}},
        "required": ["errors"]
      }
    },
    "store": false
  }'
```

`--body` কমান্ড ফ্ল্যাগের সাথে মার্জ করে। উভয়ই একই কী সেট করলে, এক্সিট কোড `2` সহ
কমান্ড কাজ করে না, তাই পরস্পরবিরোধী ইনপুট দ্রুত কাজ করা বন্ধ করে দেয়।

## কোড থেকে বেরিয়ে আসুন

প্রতিটি কমান্ড একটি টাইপ করা এক্সিট কোড রিটার্ন করে যাতে স্ক্রিপ্ট এবং এজেন্টরা
ত্রুটি টেক্সট পার্স না করেই ব্যর্থতাগুলি পরিচালনা করতে পারে। যেমন, `3` যাচাইকরণ সংক্রান্ত সমস্যা
এবং `2` ভুল কমান্ড সিনট্যাক্স সিগন্যাল করে:

| কোড | অর্থ |
| --- | --- |
| `0` | কমান্ডটি সফল হয়েছে। |
| `1` | রানটাইম বা API সংক্রান্ত সমস্যা, যেমন নেটওয়ার্ক কাজ না করা, রেট লিমিট বা ব্যাকগ্রাউন্ড জব কাজ না করা। |
| `2` | ব্যবহার বা যাচাইকরণ সংক্রান্ত সমস্যা, যেমন অজানা ফ্ল্যাগ, ইনপুট না থাকা বা ডুপ্লিকেট `--body` কী। |
| `3` | যাচাইকরণ বা অনুমোদন সংক্রান্ত সমস্যা, যেমন API কী বা টোকেন না থাকা বা ভুল হওয়া। |

প্রতিটি কমান্ডের মাধ্যমে শেয়ার করা গ্লোবাল ফ্ল্যাগ তালিকাভুক্ত করতে `gemini-api --help-global` রান করুন
(যাচাইকরণ, আউটপুট, নেটওয়ার্ক ও ডায়াগনস্টিক)।

## সীমাবদ্ধতা

- স্ট্রিমিং কমান্ডের (`generate` এবং `agent run`) জন্য `--stream=false` প্রয়োজন
  যখন `-o json` বা `--jq`-এর সাথে একত্রিত হয়ে একটি JSON রেসপন্স
  অবজেক্ট রিটার্ন করে।
- ইনলাইন `-i` ফাইল ইনপুট ক্যাপ ১৪ এমবি র ফাইল ডেটা (২০ এমবি অনুরোধ পেলোড
  base64 এনকোডিং সহ)। `gemini-api files upload`-এর মাধ্যমে বড় ফাইল আপলোড করুন।
  Files API ৪৮ ঘণ্টা পরে আপলোড করা ফাইল মুছে দেয়।
- `gemini-api` স্ট্যান্ডার্ড HTTP অনুরোধ, SSE স্ট্রিমিং ও অ্যাসিঙ্ক
  পোলিং সাপোর্ট করে, তবে দ্বিমুখী WebSocket নয়। রিয়েল-টাইম ভয়েস ও ভিডিও
  স্ট্রিমিংয়ের জন্য, [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=bn)-এর সাথে
  [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=bn) ব্যবহার করুন।

## এর পরে কী করতে হবে

- [কোডিং এজেন্ট সেট-আপ](https://ai.google.dev/gemini-api/docs/coding-agents?hl=bn)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=bn)
- [Gemini ম্যানেজড এজেন্ট](https://ai.google.dev/gemini-api/docs/agents?hl=bn)
- [GitHub-এ gemini-api-cli](https://github.com/google-gemini/gemini-api-cli)

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-28 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-28 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
