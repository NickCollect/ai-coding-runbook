---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=fa
fetched_at: 2026-10-26T05:56:22.164940+00:00
title: "\u0648\u06cc\u0698\u06af\u06cc\u200c\u0647\u0627\u06cc \u062c\u062f\u06cc\u062f Gemini 4 Argon \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# ویژگی‌های جدید Gemini 4 Argon

‫Gemini 4 Argon (`gemini-4-argon`) جدیدترین و توانمندترین مدل ما است. این مدل می‌تواند برای مدت طولانی‌تری درباره مسائل دشوار استدلال کند تا نتایج بهتری در تکالیف پیچیده کدنویسی، عامل‌گرا، ریاضی، و علمی ارائه دهد. ‫Gemini 4 Argon ازطریق Gemini API و در Google AI Studio دردسترس است.

‫Gemini 4 Argon از پنجره زمینه‌ای یکپارچه ۱ میلیون داده‌واحدی، رمزگشایی طولانی تا ۱ میلیون داده‌واحد، و سطوح تفکر قابل‌تنظیم (`low`، `medium`، `high`) پشتیبانی می‌کند.

[experiment

امتحان کردن در AI Studio

با Gemini 4 Argon و AI Studio، برنامه‌ها را از ابتدا بسازید.](https://aistudio.google.com/apps?model=gemini-4-argon&hl=fa)
[smart\_toy

گالری برنامه

برنامه‌ها را پخش و بازآمیزی کنید، ساخته‌شده با Gemini 4 Argon.](https://aistudio.google.com/learn/gemini-4-argon-showcase?hl=fa)
[rocket\_launch

شروع کنید

با پیام‌واره‌های آغازگر، کار با Gemini 4 Argon را شروع کنید.](https://aistudio.google.com/learn/gemini-4-argon?hl=fa)

این راهنما ویژگی‌های جدید Gemini 4 Argon، تغییرات API، نمونه‌های کد، و راهنمای انتقال را توضیح می‌دهد.

## مدل جدید

| مدل | شناسه مدل | سطح پیش‌فرض «اندیشگر» | قیمت‌گذاری | شرح |
| --- | --- | --- | --- | --- |
| Gemini 4 Argon | `gemini-4-argon` | `medium` | تا ۳۰ نوامبر ۲۰۲۶ با قیمت آغازین ۲ دلار به‌ازای ۱ میلیون داده‌واحد ورودی و ۱۰ دلار به‌ازای ۱ میلیون داده‌واحد خروجی (پس‌از آن ۴ دلار به‌ازای ۱ میلیون داده‌واحد ورودی و ۲۰ دلار به‌ازای ۱ میلیون داده‌واحد خروجی) دردسترس است. برای جزئیات بیشتر، [قیمت‌گذاری](https://ai.google.dev/gemini-api/docs/pricing?hl=fa) را ببینید. | توانمندترین مدل ما که برای حل سخت‌ترین مسائل با عمق و دقت در کارهای مهندسی نرم‌افزار و دانش واقعی ساخته شده است. |

برای جزئیات کامل، به [صفحه مدل Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=fa) مراجعه کنید. برای جزئیات قیمت‌گذاری مقدماتی، به [بخش قیمت‌گذاری](#pricing) در ادامه این صفحه یا [صفحه قیمت‌گذاری](https://ai.google.dev/gemini-api/docs/pricing?hl=fa#gemini-4-argon) مراجعه کنید.

## راه‌اندازی سریع

از مثال زیر برای ارسال درخواست به `gemini-4-argon` با `thinking_level` پیش‌فرض توصیه‌شده (`medium`) و محدودیت ۶۴ هزار کد برونداد استفاده کنید:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Write a three.js script that renders a realistic 3D black hole with gravitational lensing."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
});

console.log(interaction.output_text);
```

### استراحت

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-4-argon",
    "input": "Write a three.js script that renders a realistic 3D black hole with gravitational lensing."
  }'
```

## تازه‌های Gemini 4 Argon

- **حد یکپارچه ۱ میلیون داده‌واحد ورودی-خروجی:** ورودی، اندیشگر، و خروجی یک پنجره ۱٬۰۴۸٬۵۷۶ داده‌واحدی را به‌طور مشترک استفاده می‌کنند.
- **رمزگشایی طولانی:** اکنون یک پاسخ می‌تواند از ۶۴ هزار داده‌واحد فراتر برود و به ۱ میلیون داده‌واحد منهای ورودی شما برسد. [رمزگشایی طولانی](https://ai.google.dev/gemini-api/docs/long-decode?hl=fa) را ببینید.
- **درک ویدیو عاملی به‌طور عمومی دردسترس است:** [درک ویدیو عاملی](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fa#agentic-video-understanding) اکنون به‌طور عمومی دردسترس است.
- **پشتیبانی‌شده در «عامل‌های مدیریت‌شده»:** [عامل Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fa) در «عامل‌های مدیریت‌شده» Gemini اکنون از Gemini 4 Argon پشتیبانی می‌کند.

برای مشخصات کامل، به [صفحه مدل Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=fa) مراجعه کنید. برای جزئیات قیمت‌گذاری، [صفحه قیمت‌گذاری](https://ai.google.dev/gemini-api/docs/pricing?hl=fa#gemini-4-argon) را ببینید.

## برونداد بزرگ‌تر و رمزگشایی طولانی

‫Gemini 4 Argon می‌تواند برای مسائل دشوار ریاضی، علوم، و کدنویسی بیشتر فکر کند.

- **از `thinking_level` برای کنترل عمق استدلال استفاده کنید:** سطح تفکر تعیین می‌کند که مدل قبل‌از پاسخ دادن چقدر عمیق استدلال کند. `max_output_tokens` یک حد سخت است: وقتی تفکر و خروجی باهم به آن برسند، پاسخ متوقف می‌شود، بنابراین آن را به‌اندازه کافی بالا تنظیم کنید تا پاسخ کوتاه نشود.
- **تولید کردن حداکثر ۱ میلیون داده‌واحد با اجرای پس‌زمینه‌ای:** از اجرای پس‌زمینه‌ای با `max_output_tokens` بیشتر از ۶۵٬۵۳۶ استفاده کنید تا یک پاسخ بتواند از ۶۴ هزار داده‌واحد فراتر برود و به ۱ میلیون داده‌واحد برسد. مدل پاسخ‌های طولانی را در جهش‌های حداکثر ۶۴ هزار تایی از کدواحدها تولید می‌کند و هر جهش از جایی که جهش قبلی متوقف شده است ادامه می‌یابد. با اجرای پس‌زمینه، سرورهای ما این جهش‌های ادامه‌دار را برای شما اجرا می‌کنند. چون هر پرش یک مرحله `model_output` به `interaction.steps` اضافه می‌کند، وقتی تعامل کامل شد، نوشتار را در همه مراحل `model_output` به‌هم بپیوندید.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Write a complete, rigorous proof of the prime number theorem.",
    background=True,
    generation_config={
        "max_output_tokens": 262144,
        "thinking_level": "high",
    },
)

while interaction.status in ("in_progress", "queued"):
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Each hop adds a model_output step, so join the text of all of them.
text = "".join(
    content.text
    for step in interaction.steps
    if step.type == "model_output"
    for content in step.content
    if content.type == "text"
)
print(text)
print("Status:", interaction.status)
print("Usage:", interaction.usage)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Write a complete, rigorous proof of the prime number theorem.",
  background: true,
  generation_config: {
    max_output_tokens: 262144,
    thinking_level: "high",
  },
});

while (interaction.status === "in_progress" || interaction.status === "queued") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await client.interactions.get(interaction.id);
}

// Each hop adds a model_output step, so join the text of all of them.
const text = interaction.steps
  .filter((step) => step.type === "model_output")
  .flatMap((step) => step.content ?? [])
  .filter((content) => content.type === "text")
  .map((content) => content.text)
  .join("");
console.log(text);
console.log("Status:", interaction.status);
console.log("Usage:", interaction.usage);
```

### استراحت

```
ID=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-4-argon",
    "input": "Write a complete, rigorous proof of the prime number theorem.",
    "background": true,
    "generation_config": {
      "max_output_tokens": 262144,
      "thinking_level": "high"
    }
  }' | jq -r '.id')

while true; do
  RESP=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
  STATUS=$(echo "$RESP" | jq -r '.status')
  if [[ "$STATUS" != "in_progress" && "$STATUS" != "queued" ]]; then
    echo "$RESP" | jq -r '[.steps[]? | select(.type == "model_output") | .content[]? | select(.type == "text") | .text] | join("")'
    break
  fi
  sleep 5
done
```

اجرا در پس‌زمینه ساده‌ترین راه برای اجرای رمزگشایی طولانی است. این پارامتر حلقه ادامه را در سمت سرور اجرا می‌کند تا زمانی که مدل تمام شود یا به `max_output_tokens` برسد. اگر به کنترل دقیق‌تری بر تلاش‌های مجدد، عقب‌نشینی، و مدیریت خطا نیاز دارید (یا نمی‌خواهید تعامل‌هایتان ذخیره شود)، می‌توانید از ادامه سمت کارخواه در [GenerateContent API](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=fa) استفاده کنید. ادامه سمت کارخواه نیز به‌زودی به Interactions API اضافه خواهد شد. برای جاری‌سازی، اتصال مجدد، شمارش داده‌واحد، و زمان استفاده از رمزگشایی طولانی، به [راهنمای رمزگشایی طولانی](https://ai.google.dev/gemini-api/docs/long-decode?hl=fa) مراجعه کنید.

### تنظیم کردن محدودیت‌های داده‌واحد برونداد

‫`max_output_tokens` مجموع توکن‌های تفکر و برونداد را برای پاسخ تنظیم می‌کند. آن را به‌اندازه کافی بالا تنظیم کنید تا فکر کردن پاسخ را کوتاه نکند، و به‌اندازه کافی پایین تنظیم کنید تا وقتی پیام‌واره سختی از همه آن استفاده می‌کند، هزینه محدود شود.

از این مقادیر به‌عنوان نقطه شروع استفاده کنید:

- **تکالیف استاندارد:** مقدار پیش‌فرض ۶۵٬۵۳۶ را حفظ کنید یا هیچ مقداری تنظیم نکنید.
- **برنامه‌های موجود با محدودیت کمتر از ۳۲ هزار:** `max_output_tokens` را حداقل به ۳۲٬۷۶۸ افزایش دهید. ‫Gemini 4 Argon می‌تواند نسبت‌به مدل‌های قبلی، بخش بیشتری از حد استفاده را صرف اندیشیدن کند. برای استفاده از توکن‌های کمتر، سطح تفکر را کاهش دهید.
- **استدلال و کدنویسی پیچیده:** `background: true` و `max_output_tokens` را روی ۱۳۱٬۰۷۲ یا ۲۶۲٬۱۴۴ تنظیم کنید، تا ۱٬۰۴۸٬۵۷۶ منهای نشان‌های ورودی شما.

## آشنایی با سطوح «اندیشگر»

[سطح اندیشیدن](https://ai.google.dev/gemini-api/docs/thinking?hl=fa) کنترل اصلی شما بر کیفیت، تأخیر، و استفاده از نمانه در Gemini 4 Argon است:

| سطح «اندیشگر» | استفاده از کد | زمان استفاده |
| --- | --- | --- |
| `low` | کمترین داده‌واحد، کمترین تأخیر | تکالیف ساده‌تر و کارهای حساس به هزینه. همچنین برای کارهای تحلیلی و نوشتاری که نیاز به تفکر سبک دارند مناسب است. کیفیت ممکن است در تکالیف سخت کاهش یابد. |
| `medium` (پیش‌فرض) | متعادل | برای اکثر تکلیف‌ها، ازجمله کدنویسی پیچیده و موارد استفاده عامل‌گرا، توصیه می‌شود. |
| `high` | بیشترین داده‌واحد، کندترین داده‌واحد اول | استدلال پیچیده، ریاضی و علوم سخت، و دشوارترین کدها یا وظایف عامل. برای بروندادهای طولانی، با رمزگشایی طولانی به‌خوبی جفت می‌شود. |

ارزیابی‌هایتان را در هر سه سطح اجرا کنید، سپس پایین‌ترین سطحی را که با معیارهای کیفی شما مطابقت دارد انتخاب کنید. برای کسب اطلاعات بیشتر، [راهنمای تفکر](https://ai.google.dev/gemini-api/docs/thinking?hl=fa) را ببینید.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    generation_config={
        "thinking_level": "medium"  # Balanced reasoning effort for complex tasks
    }
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  generation_config: {
    thinking_level: "medium", // Balanced reasoning effort for complex tasks
  },
});

console.log(interaction.output_text);
```

### استراحت

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-4-argon",
    "input": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    "generation_config": {
      "thinking_level": "medium"
    }
  }'
```

## ‫Gemini 4 Argon در «عامل‌های مدیریت‌شده»

[عامل Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fa) در «عامل‌های مدیریت‌شده Gemini» از Gemini 4 Argon پشتیبانی می‌کند. برای استفاده از آن، مدل را در `agent_config` تنظیم کنید:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input=(
        "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
        "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
        "Check search indexing with Google Search for site:web.dev. "
        "Format the output as a side-by-side scorecard table with prioritized fixes."
    ),
    environment="remote",
    agent_config={
        "type": "antigravity",
        "model": "gemini-4-argon",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  agent: "antigravity-preview-09-2026",
  input:
    "Audit https://web.dev for performance, Core Web Vitals, and SEO. " +
    "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. " +
    "Check search indexing with Google Search for site:web.dev. " +
    "Format the output as a side-by-side scorecard table with prioritized fixes.",
  environment: "remote",
  agent_config: {
    type: "antigravity",
    model: "gemini-4-argon",
  },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### استراحت

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google'\''s PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
    "environment": "remote",
    "agent_config": {
      "type": "antigravity",
      "model": "gemini-4-argon"
    }
  }'
```

برای گزینه‌های بیشتر، [انتخاب مدل](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fa#model-selection) را در راهنمای عامل Antigravity ببینید.

## بازبینه انتقال

```
  `/gemini-api-dev migrate my app to Gemini 4 Argon`
```

### انتقال به gemini-4-argon

- **به‌روزرسانی شناسه مدل:** رشته مدل هدف را به `gemini-4-argon` تغییر دهید.
- **`max_output_tokens` را مرور کنید:** اگر امروز آن را به‌طور صریح تنظیم کرده‌اید، افزایش آن را مدنظر قرار دهید. حداقل ۳۲٬۷۶۸ را توصیه می‌کنیم، زیرا Gemini 4 Argon می‌تواند بخش بیشتری از این حد را صرف فکر کردن کند.
- **پیکربندی سطح اندیشیدن:** `low`، `medium` (پیش‌فرض)، یا `high` را انتخاب کنید و حجم کاری‌تان را در هر سه سطح آزمایش کنید.
- **از ذخیره‌سازی صریح بافت در حافظه نهان استفاده نکنید:** ذخیره‌سازی صریح در حافظه نهان (`cachedContents` / `caches.create`) در Gemini 4 Argon پشتیبانی نمی‌شود. فراخوانی‌هایی را که `cached_content` ایجاد می‌کنند یا به آن ارجاع می‌دهند از درخواست‌هایتان بردارید. [ذخیره‌سازی ضمنی در حافظه نهان](https://ai.google.dev/gemini-api/docs/caching?hl=fa) به‌طور پیش‌فرض برای پیام‌واره‌های حداقل ۴۰۹۶ نمانه‌ای فعال است و نمانه‌های ورودی ذخیره‌شده در حافظه نهان را درصورت وجود در حافظه نهان با ۹۵٪ تخفیف ارائه می‌دهد.
- **پارامترهای نمونه‌برداری را بردارید:** `temperature`، `top_p`، و `top_k` را از درخواست‌هایتان بردارید. اگر ارائه شود، نادیده گرفته می‌شود.
- **برای بروندادهای طولانی از اجرای پس‌زمینه استفاده کنید:** برای تکلیف‌هایی که به بیش‌از ۶۴ هزار نمانه نیاز دارند، `background` را روی true و `max_output_tokens` را روی بیشتر از ۶۵٬۵۳۶ تنظیم کنید.
- **افزایش زمان اتمام مهلت کارخواه:** پیام‌واره‌های سخت ممکن است چند دقیقه طول بکشد. از اجرای پس‌زمینه استفاده کنید یا زمان اتمام مهلت کارخواه HTTP را حداقل روی ۱۵ دقیقه تنظیم کنید.
- **حفظ وضعیت مکالمه در سرور:** از `previous_interaction_id` برای مکالمه‌های چندنوبتی و فراخوانی تابع استفاده کنید.

## قیمت‌گذاری

‫Gemini 4 Argon با قیمت آغازین تا ۳۰ نوامبر ۲۰۲۶ دردسترس است:

- **داده‌واحد ورودی:** ۲٫۰۰ دلار به‌ازای هر ۱ میلیون داده‌واحد (۴٫۰۰ دلار از ۱ دسامبر ۲۰۲۶)
  - **داده‌واحدهای ورودی ذخیره‌شده در حافظه نهان:** ذخیره‌سازی ضمنی در حافظه نهان، ورودی ذخیره‌شده در حافظه نهان را تا ۹۵٪ کاهش می‌دهد و به ۰٫۱۰ دلار به‌ازای هر ۱ میلیون داده‌واحد می‌رساند (از ۱ دسامبر ۲۰۲۶، ۰٫۲۰ دلار).
- **داده‌واحدهای برونداد، شامل داده‌واحدهای اندیشیدن:** ۱۰٫۰۰ دلار به‌ازای هر ۱ میلیون داده‌واحد (۲۰٫۰۰ دلار از ۱ دسامبر ۲۰۲۶)

‫Gemini 4 Argon در سطح «رایگان» دردسترس نیست. برای مشاهده سطوح قیمت‌گذاری کامل، به [صفحه قیمت‌گذاری](https://ai.google.dev/gemini-api/docs/pricing?hl=fa#gemini-4-argon) مراجعه کنید.

## مدل‌های دیگر

- [‫Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=fa)
- [‫Gemini 3.6 Flash و ‎3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=fa)
- [دیدن همه مدل‌ها](https://ai.google.dev/gemini-api/docs/models?hl=fa)

## قدم بعدی چیست

- [راهنمای رمزگشایی طولانی](https://ai.google.dev/gemini-api/docs/long-decode?hl=fa) را برای جاری‌سازی، اتصال مجدد، و شمارش داده‌واحد بخوانید.
- در [راهنمای تفکر](https://ai.google.dev/gemini-api/docs/thinking?hl=fa) با نحوه عملکرد سطوح تفکر و خلاصه‌های تفکر آشنا شوید.
- درباره کارهای طولانی‌مدت در [راهنمای اجرای پس‌زمینه](https://ai.google.dev/gemini-api/docs/background-execution?hl=fa) بیشتر بدانید.
- پیام‌واره‌ها را در [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa) آزمایش و پالایش کنید.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-16 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-16 به‌وقت ساعت هماهنگ جهانی."],[],[]]
