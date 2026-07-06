---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=ar
fetched_at: 2026-07-06T05:10:14.939436+00:00
title: "\u202bGemini Developer API \u0645\u0642\u0627\u0631\u0646\u0629\u064b \u0628\u0645\u0646\u0635\u0629 \u0648\u0643\u064a\u0644 Gemini Enterprise \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# ‫Gemini Developer API مقارنةً بمنصة وكيل Gemini Enterprise

عند تطوير حلول الذكاء الاصطناعي التوليدي باستخدام Gemini، تقدّم Google منتجَين من واجهات برمجة التطبيقات:
[Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=ar) و[Gemini Enterprise Agent Platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=ar).

توفّر Gemini Developer API أسرع طريقة لإنشاء التطبيقات المستندة إلى Gemini وتجهيزها للإصدار العلني وتوسيع نطاقها. يجب أن يستخدم معظم المطوّرين Gemini Developer API ما لم تكن هناك حاجة إلى عناصر تحكّم خاصة بالمؤسسات.

توفّر Gemini Enterprise Agent Platform نظامًا شاملاً يتضمّن ميزات وخدمات جاهزة للمؤسسات من أجل إنشاء تطبيقات الذكاء الاصطناعي التوليدي ونشرها، استنادًا إلى Google Cloud Platform.

لقد بسّطنا مؤخرًا عملية نقل البيانات بين هاتين الخدمتَين. يمكن الآن الوصول إلى كلّ من Gemini
Developer API وGemini Enterprise Agent Platform API من خلال حزمة
[Google Gen AI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=ar) الموحّدة.

## مقارنة الرموز البرمجية

تحتوي هذه الصفحة على مقارنات جنبًا إلى جنب بين الرموز البرمجية في أدلة البدء السريع لكلّ من Gemini Developer API وGemini Enterprise Agent Platform لإنشاء النصوص.

### Python

يمكنك الوصول إلى كلّ من Gemini Developer API وGemini Enterprise Agent Platform من خلال مكتبة `google-genai`. راجِع صفحة [المكتبات](https://ai.google.dev/gemini-api/docs/libraries?hl=ar) للاطّلاع على تعليمات حول كيفية تثبيت `google-genai`.

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini Enterprise Agent Platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript وTypeScript

يمكنك الوصول إلى كلّ من Gemini Developer API وGemini Enterprise Agent Platform من خلال مكتبة `@google/genai`. راجِع صفحة [المكتبات](https://ai.google.dev/gemini-api/docs/libraries?hl=ar) للاطّلاع على تعليمات حول كيفية
تثبيت `@google/genai`.

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini Enterprise Agent Platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### انتقال

يمكنك الوصول إلى كلّ من Gemini Developer API وGemini Enterprise Agent Platform من خلال مكتبة `google.golang.org/genai`. راجِع صفحة [المكتبات](https://ai.google.dev/gemini-api/docs/libraries?hl=ar) للاطّلاع على تعليمات حول كيفية
تثبيت `google.golang.org/genai`.

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini Enterprise Agent Platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", genai.Text("Tell me about New York?"), nil)

}
```

### حالات الاستخدام والمنصات الأخرى

راجِع الأدلة الخاصة بحالات الاستخدام في [مستندات Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=ar)
و[مستندات Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=ar)
للاطّلاع على المنصات وحالات الاستخدام الأخرى.

## اعتبارات نقل البيانات

عند نقل البيانات:

- عليك استخدام حسابات خدمة Google Cloud للمصادقة. راجِع [مستندات Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=ar)
  لمزيد من المعلومات.
- يمكنك استخدام مشروعك الحالي على Google Cloud
  (المشروع نفسه الذي استخدمته لإنشاء مفتاح واجهة برمجة التطبيقات) أو يمكنك
  [إنشاء مشروع جديد على Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=ar).
- قد تختلف المناطق المتوافقة بين Gemini Developer API وGemini Enterprise Agent Platform API. [راجِع قائمة المناطق المتوافقة مع الذكاء الاصطناعي التوليدي على Google Cloud.](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=ar)
- يجب إعادة تدريب أي نماذج أنشأتها في Google AI Studio في Gemini Enterprise Agent Platform.

إذا لم تعُد بحاجة إلى استخدام مفتاح Gemini API لـ Gemini Developer API، اتّبِع أفضل الممارسات الأمنية واحذفه.

لحذف مفتاح واجهة برمجة التطبيقات:

1. [افتح صفحة بيانات اعتماد Google Cloud API.](https://console.cloud.google.com/apis/credentials?hl=ar)
2. ابحث عن مفتاح واجهة برمجة التطبيقات الذي تريد حذفه وانقر على رمز **الإجراءات**.
3. انقر على **حذف مفتاح واجهة برمجة التطبيقات**.
4. في النافذة المنبثقة **حذف بيانات الاعتماد** ، انقر على **حذف**.

   يستغرق نشر حذف مفتاح واجهة برمجة التطبيقات بضع دقائق. بعد اكتمال عملية النشر، يتم رفض أي زيارات تستخدم مفتاح واجهة برمجة التطبيقات المحذوف.

## الخطوات التالية

- راجِع
  [نظرة عامة على الذكاء الاصطناعي التوليدي على Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview?hl=ar)
  لمزيد من المعلومات حول حلول الذكاء الاصطناعي التوليدي على Gemini Enterprise Agent Platform.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
