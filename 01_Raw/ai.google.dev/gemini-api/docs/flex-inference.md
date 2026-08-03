---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=ar
fetched_at: 2026-08-03T04:32:07.345408+00:00
title: "\u0627\u0644\u0627\u0633\u062a\u0646\u062a\u0627\u062c \u0627\u0644\u0645\u0631\u0646 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الاستنتاج المرن

‫Gemini Flex API هو مستوى استنتاج يتيح خفض التكلفة بنسبة% 50 مقارنةً بالأسعار العادية، مقابل وقت استجابة متغيّر وتوفّر بأفضل جهد ممكن. تم تصميم هذه الفئة لأحمال العمل التي يمكنها تحمّل التأخير وتتطلّب معالجة متزامنة ولكنها لا تحتاج إلى الأداء في الوقت الفعلي الذي توفّره واجهة برمجة التطبيقات العادية.

## كيفية استخدام Flex

لاستخدام فئة Flex، حدِّد `service_tier` على أنّه `flex` في طلبك. تستخدم الطلبات تلقائيًا الفئة العادية في حال حذف هذا الحقل.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.6-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
    });
    console.log(interaction.output_text);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## طريقة عمل الاستدلال المرن

تساعد Gemini Flex Inference في سد الفجوة بين واجهة برمجة التطبيقات العادية ومدة التنفيذ البالغة 24 ساعة في [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar). تستفيد هذه الخدمة من سعة الحوسبة "القابلة للتخفيض" في غير أوقات الذروة لتوفير حلّ فعّال من حيث التكلفة للمهام التي تعمل في الخلفية وسير العمل التسلسلي.

| الميزة | التعبير | الأولوية | خطة "الرزمة العادية" | مجمّعة |
| --- | --- | --- | --- | --- |
| **الأسعار** | خصم بنسبة% 50 | أكثر من خطة Standard بنسبة تتراوح بين %75 و%100 | السعر الكامل | خصم بنسبة% 50 |
| **وقت الاستجابة** | الدقائق (المدة المستهدَفة من دقيقة واحدة إلى 15 دقيقة) | منخفض (ثوانٍ) | من ثوانٍ إلى دقائق | ما يصل إلى 24 ساعة |
| **الموثوقية** | أفضل جودة ممكنة (يمكن التضحية بها) | عالية (غير قابلة للإزالة) | مرتفع / مرتفع إلى حد ما | عالية (لمعدّل نقل البيانات) |
| **الواجهة** | متزامن | متزامن | متزامن | غير متزامن |

### المزايا الرئيسية

- **فعالية التكلفة**: تحقيق وفورات كبيرة في التكاليف عند إجراء عمليات التقييم غير الإنتاجية، واستخدام البرامج في الخلفية، وإثراء البيانات
- **سهولة الاستخدام**: ما عليك سوى إضافة مَعلمة واحدة إلى طلباتك الحالية.
- **نماذج سير العمل المتزامنة**: هي الأنسب لسلاسل واجهات برمجة التطبيقات المتسلسلة التي يعتمد فيها الطلب التالي على ناتج الطلب السابق، ما يجعلها أكثر مرونة من "المعالجة المجمّعة" لنماذج سير العمل المستندة إلى الوكلاء.

### حالات الاستخدام

- **التقييمات بلا إنترنت**: إجراء اختبارات الانحدار أو قوائم الصدارة باستخدام "نماذج اللغة الكبيرة كحكم"
- **الوكلاء الذين يعملون في الخلفية**: المهام المتسلسلة، مثل تعديلات نظام إدارة علاقات العملاء أو إنشاء الملفات الشخصية أو الإشراف على المحتوى، حيث يمكن قبول تأخيرات لعدة دقائق
- **البحث المقيّد بالميزانية**: تجارب أكاديمية تتطلّب عددًا كبيرًا من الرموز المميزة بميزانية محدودة.

### حدود معدّل الاستخدام

يتم احتساب عدد الزيارات الناتجة عن استنتاج Flex ضمن [حدود المعدّل](https://aistudio.google.com/rate-limit?hl=ar) العامة، ولا يوفّر حدود معدّل موسّعة مثل [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar).

### السعة القابلة للخفض

يتم التعامل مع الزيارات المرنة بأولوية أقل. في حال حدوث ارتفاع مفاجئ في عدد الزيارات العادية، قد يتم إيقاف طلبات Flex أو إزالتها لضمان توفّر سعة للمستخدمين ذوي الأولوية العالية. إذا كنت تبحث عن استنتاج ذي أولوية عالية، يمكنك الاطّلاع على [الاستنتاج ذو الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar).

### رموز الخطأ

عندما تكون السعة المرنة غير متاحة أو يكون النظام مزدحمًا، ستعرض واجهة برمجة التطبيقات رموز الخطأ العادية التالية:

- **‫503 الخدمة غير متاحة**: يتلقّى النظام عدد طلبات كبير جدًا في الوقت الحالي.
- **429 Too Many Requests**: تجاوز حدود المعدّل أو استنفاد الموارد

### مسؤولية العميل

- **عدم توفّر خيار احتياطي من جهة الخادم**: لمنع فرض رسوم غير متوقّعة، لن يرقّي النظام تلقائيًا طلبًا من فئة Flex إلى فئة Standard إذا كانت سعة Flex ممتلئة.
- **عمليات إعادة المحاولة**: يجب تنفيذ منطق إعادة المحاولة من جهة العميل باستخدام خوارزمية الرقود الأسي الثنائي.
- **مهلات**: بما أنّ طلبات Flex قد تبقى في صفّ الانتظار، ننصحك بزيادة المهلات من جهة العميل إلى 10 دقائق أو أكثر لتجنُّب إغلاق الاتصال قبل الأوان.

## تعديل فترات المهلة

يمكنك ضبط مهلات زمنية لكل طلب في واجهة REST API ومكتبات العملاء.
احرص دائمًا على أن يغطي المهلة الزمنية من جهة العميل فترة انتظار الخادم المقصودة (على سبيل المثال، 600 ثانية أو أكثر لقوائم انتظار Flex). تتوقّع حِزم SDK قيم المهلة بالملي ثانية.

### انتهاء المهلة لكل طلب

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.6-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

## تنفيذ عمليات إعادة المحاولة

بما أنّ Flex يمكن إيقافه مؤقتًا ويتعذّر تنفيذه بسبب أخطاء 503، إليك مثال على التنفيذ الاختياري لمنطق إعادة المحاولة لمواصلة الطلبات التي تعذّر تنفيذها:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.6-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.6-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.6-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.6-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

## الأسعار

يتم تحديد سعر Flex inference بنسبة% 50 من [سعر واجهة برمجة التطبيقات العادية](https://ai.google.dev/gemini-api/docs/pricing?hl=ar)
ويتم تحصيل الرسوم لكل رمز مميز.

## النماذج المتوافقة

تتيح الطُرز التالية استنتاج Flex:

| الطراز | Flex inference |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ar) | ✔️ |
| [‫Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ar) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) | ✔️ |
| [‫Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ✔️ |
| [إصدار تجريبي من Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) | ✔️ |
| [معاينة Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ar) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ✔️ |

## الخطوات التالية

- [استنتاج الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar) لوقت الاستجابة الفائق السرعة
- [الرموز المميزة](https://ai.google.dev/gemini-api/docs/tokens?hl=ar): فهم الرموز المميزة

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
