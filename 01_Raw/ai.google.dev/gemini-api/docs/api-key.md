---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=ar
fetched_at: 2026-06-01T06:08:47.094064+00:00
title: "\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u0645\u0641\u0627\u062a\u064a\u062d \u0648\u0627\u062c\u0647\u0629 \u0628\u0631\u0645\u062c\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642\u0627\u062a \u0641\u064a Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# استخدام مفاتيح واجهة برمجة التطبيقات في Gemini

لاستخدام Gemini API، يجب أن يكون لديك مفتاح واجهة برمجة التطبيقات. توضّح هذه الصفحة كيفية إنشاء مفاتيحك وإدارتها في Google AI Studio، بالإضافة إلى كيفية إعداد بيئتك لاستخدامها في الرمز البرمجي.

[إنشاء مفتاح واجهة Gemini API أو عرضه](https://aistudio.google.com/app/apikey?hl=ar)

## مفاتيح واجهة برمجة التطبيقات

يمكنك إنشاء جميع مفاتيح Gemini API وإدارتها من صفحة [مفاتيح API](https://aistudio.google.com/app/apikey?hl=ar) في **Google AI Studio**.

بعد الحصول على مفتاح واجهة برمجة التطبيقات، تتوفّر لك الخيارات التالية للربط بواجهة Gemini API:

- [ضبط مفتاح واجهة برمجة التطبيقات كمتغيّر بيئة](#set-api-env-var)
- [تقديم مفتاح واجهة برمجة التطبيقات بشكلٍ صريح](#provide-api-key-explicitly)

لإجراء الاختبار الأوّلي، يمكنك ترميز مفتاح واجهة برمجة التطبيقات بشكل ثابت، ولكن يجب أن يكون ذلك مؤقتًا فقط لأنّه غير آمن. يمكنك العثور على أمثلة على الترميز الثابت لمفتاح واجهة برمجة التطبيقات في قسم [توفير مفتاح واجهة برمجة التطبيقات بشكل صريح](#provide-api-key-explicitly).

## مشاريع Google Cloud

تُعد [مشاريع Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=ar) أساسية لاستخدام خدمات Google Cloud (مثل Gemini API) وإدارة الفوترة والتحكّم في المتعاونين والأذونات. يوفّر Google AI
Studio واجهة بسيطة لمشاريعك على Google Cloud.

إذا لم يسبق لك إنشاء أي مشاريع، عليك إنشاء مشروع جديد أو استيراد مشروع من Google Cloud إلى Google AI Studio. ستعرض صفحة **المشاريع** في Google AI Studio جميع المفاتيح التي لديها الإذن الكافي لاستخدام Gemini API. راجِع قسم [استيراد المشاريع](#import-projects) للحصول على التعليمات.

### المشروع التلقائي

بالنسبة إلى المستخدمين الجدد، بعد قبول بنود الخدمة، ينشئ Google AI Studio مشروعًا ومفتاحًا تلقائيًا على Google Cloud لتسهيل الاستخدام. يمكنك إعادة تسمية هذا المشروع في Google AI Studio من خلال الانتقال إلى طريقة عرض **المشاريع** في **لوحة البيانات**، والنقر على زر الإعدادات المكوّن من 3 نقاط بجانب أحد المشاريع، ثم اختيار **إعادة تسمية المشروع**. لن يتم إنشاء مشروع تلقائي للمستخدمين الحاليين أو المستخدمين الذين لديهم حسابات على Google Cloud.

## استيراد المشاريع

يرتبط كل مفتاح لواجهة Gemini API بمشروع على Google Cloud. لا يعرض Google AI Studio تلقائيًا كل مشاريعك على السحابة الإلكترونية. يجب استيراد المشاريع التي تريدها من خلال البحث عن الاسم أو رقم تعريف المشروع في مربّع الحوار **استيراد المشاريع**. للاطّلاع على قائمة كاملة بالمشاريع التي يمكنك الوصول إليها، انتقِل إلى Cloud Console.

إذا لم تستورد أي مشاريع على السحابة الإلكترونية بعد، اتّبِع الخطوات التالية لاستيراد مشروع Google Cloud وإنشاء مفتاح:

1. انتقِل إلى [Google AI Studio](https://aistudio.google.com?hl=ar).
2. افتح **لوحة البيانات** من اللوحة الجانبية على يمين الصفحة.
3. اختَر **المشاريع**.
4. انقر على الزر **استيراد المشاريع** في صفحة **المشاريع**.
5. ابحث عن مشروع Google Cloud الذي تريد استيراده واختَره، ثم انقر على الزر **استيراد**.

بعد استيراد مشروع، انتقِل إلى صفحة **مفاتيح واجهة برمجة التطبيقات** من قائمة **لوحة البيانات**، ثم أنشِئ مفتاح واجهة برمجة تطبيقات في المشروع الذي استوردته للتو.

## القيود

في ما يلي القيود المفروضة على إدارة مفاتيح واجهة برمجة التطبيقات ومشاريع Google Cloud في Google AI Studio.

- يمكنك إنشاء 10 مشاريع كحدّ أقصى في كل مرة من صفحة **المشاريع** في Google AI Studio.
- يمكنك تسمية المشاريع والمفاتيح وإعادة تسميتها.
- تعرض صفحتا **مفاتيح واجهة برمجة التطبيقات** و**المشاريع** 100 مفتاح و50 مشروعًا كحد أقصى.
- لا يتم عرض سوى مفاتيح واجهة برمجة التطبيقات التي لا تتضمّن أي قيود أو التي تقتصر على Generative Language API.

للحصول على إذن إضافي بإدارة مشاريعك، بما في ذلك تعديل مفاتيح واجهة برمجة التطبيقات وتقييدها، انتقِل إلى
[صفحة بيانات الاعتماد في Google Cloud Console](https://console.cloud.google.com/apis/credentials?hl=ar).
في Cloud Console، يمكنك اختيار مشروعك والنقر على مفتاح واجهة برمجة تطبيقات حالي، ثم حصر استخدامه على **Generative Language API**.

## ضبط مفتاح واجهة برمجة التطبيقات كمتغيّر بيئي

في حال ضبطت متغيّر البيئة `GEMINI_API_KEY` أو `GOOGLE_API_KEY`، سيختار العميل مفتاح واجهة برمجة التطبيقات تلقائيًا عند استخدام إحدى [مكتبات Gemini API](https://ai.google.dev/gemini-api/docs/libraries?hl=ar). ننصحك بضبط أحد المتغيرَين فقط، ولكن في حال ضبط كليهما، ستكون الأولوية للمتغير `GOOGLE_API_KEY`.

إذا كنت تستخدم REST API أو JavaScript على المتصفّح، عليك تقديم مفتاح واجهة برمجة التطبيقات بشكل صريح.

في ما يلي كيفية ضبط مفتاح واجهة برمجة التطبيقات محليًا كمتغيّر بيئة
`GEMINI_API_KEY` باستخدام أنظمة تشغيل مختلفة.

### ‫Linux/macOS - Bash

‫Bash هو إعداد شائع للوحدة الطرفية في نظامَي التشغيل Linux وmacOS. يمكنك التحقّق ممّا إذا كان لديك ملف إعدادات من خلال تنفيذ الأمر التالي:

```
~/.bashrc
```

إذا كان الردّ هو "No such file or directory"، عليك إنشاء هذا الملف وفتحه من خلال تنفيذ الأوامر التالية، أو استخدام `zsh`:

```
touch ~/.bashrc
open ~/.bashrc
```

بعد ذلك، عليك ضبط مفتاح واجهة برمجة التطبيقات من خلال إضافة أمر التصدير التالي:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

بعد حفظ الملف، طبِّق التغييرات من خلال تنفيذ الأمر التالي:

```
source ~/.bashrc
```

### ‫macOS - Zsh

‫Zsh هو إعداد شائع للوحدة الطرفية في نظامَي التشغيل Linux وmacOS. يمكنك التحقّق ممّا إذا كان لديك ملف إعدادات من خلال تنفيذ الأمر التالي:

```
~/.zshrc
```

إذا كان الردّ هو "No such file or directory"، عليك إنشاء هذا الملف وفتحه من خلال تنفيذ الأوامر التالية، أو استخدام `bash`:

```
touch ~/.zshrc
open ~/.zshrc
```

بعد ذلك، عليك ضبط مفتاح واجهة برمجة التطبيقات من خلال إضافة أمر التصدير التالي:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

بعد حفظ الملف، طبِّق التغييرات من خلال تنفيذ الأمر التالي:

```
source ~/.zshrc
```

### Windows

1. ابحث عن "متغيرات البيئة" في شريط البحث.
2. اختَر تعديل **إعدادات النظام**. قد يُطلب منك تأكيد رغبتك في إجراء ذلك.
3. في مربّع حوار إعدادات النظام، انقر على الزر الذي يحمل التصنيف **متغيرات البيئة**.
4. ضمن **متغيّرات المستخدم** (للمستخدم الحالي) أو **متغيّرات النظام** (تنطبق على جميع المستخدمين الذين يستخدمون الجهاز)، انقر على **جديد...**
5. حدِّد اسم المتغيّر على النحو التالي: `GEMINI_API_KEY`. حدِّد مفتاح Gemini API كقيمة المتغيّر.
6. انقر على **حسنًا** لتطبيق التغييرات.
7. افتح جلسة طرفية جديدة (cmd أو Powershell) للحصول على المتغير الجديد.

## توفير مفتاح واجهة برمجة التطبيقات بشكل صريح

في بعض الحالات، قد تحتاج إلى تقديم مفتاح واجهة برمجة التطبيقات بشكل صريح. على سبيل المثال:

- إذا كنت بصدد إجراء طلب بيانات من واجهة برمجة التطبيقات بسيط وتفضّل ترميز مفتاح واجهة برمجة التطبيقات بشكل ثابت.
- تريد التحكّم بشكل صريح بدون الحاجة إلى الاعتماد على الاكتشاف التلقائي لمتغيرات البيئة من خلال مكتبات Gemini API
- أنت تستخدم بيئة لا تتوافق مع متغيرات البيئة (مثل الويب) أو تجري طلبات REST.

في ما يلي أمثلة على كيفية تقديم مفتاح واجهة برمجة التطبيقات بشكلٍ صريح:

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

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
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### جافا

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.5-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
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

## الحفاظ على أمان مفتاح واجهة برمجة التطبيقات

عامِل مفتاح Gemini API مثل كلمة المرور. في حال تعرّض مشروعك للاختراق، يمكن للآخرين استخدام حصته، وتحمّل الرسوم (في حال تفعيل الفوترة)، والوصول إلى بياناتك الخاصة، مثل الملفات.

### قواعد الأمان المهمة

- **الحفاظ على سرية المفاتيح**: قد تتيح مفاتيح واجهة برمجة التطبيقات الخاصة بـ Gemini الوصول إلى بيانات حساسة يعتمد عليها تطبيقك.

  - **لا تُدرِج مفاتيح واجهة برمجة التطبيقات في نظام التحكّم بالمصادر أبدًا.** لا تحفَظ مفتاح واجهة برمجة التطبيقات في أنظمة التحكم في الإصدارات، مثل Git.
  - **يجب عدم عرض مفاتيح واجهة برمجة التطبيقات من جهة العميل.** لا تستخدِم مفتاح واجهة برمجة التطبيقات مباشرةً
    في تطبيقات الويب أو الأجهزة الجوّالة في مرحلة الإنتاج. يمكن استخراج المفاتيح في الرمز البرمجي من جهة العميل (بما في ذلك مكتبات JavaScript/TypeScript وطلبات REST).
- **تقييد الوصول**: يمكنك تقييد استخدام مفتاح واجهة برمجة التطبيقات بعناوين IP أو مراجع HTTP أو تطبيقات Android/iOS معيّنة حيثما أمكن ذلك.
- **تقييد الاستخدام**: فعِّل واجهات برمجة التطبيقات الضرورية فقط لكل مفتاح.
- **إجراء عمليات تدقيق منتظمة**: يجب تدقيق مفاتيح واجهة برمجة التطبيقات بانتظام وتغييرها بشكل دوري.

### أفضل الممارسات

- **استخدام طلبات من جهة الخادم مع مفاتيح واجهة برمجة التطبيقات** إنّ الطريقة الأكثر أمانًا لاستخدام مفتاح واجهة برمجة التطبيقات هي طلب Gemini API من تطبيق من جهة الخادم حيث يمكن الحفاظ على سرية المفتاح.
- **استخدام رموز مميزة مؤقتة للوصول من جهة العميل (Live API فقط):** للوصول مباشرةً إلى Live API من جهة العميل، يمكنك استخدام رموز مميزة مؤقتة. وتكون هذه النماذج أقل عرضة للمخاطر الأمنية ويمكن استخدامها في عملية الإنتاج. راجِع دليل [الرموز المميزة المؤقتة](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=ar) لمزيد من المعلومات.
- **ننصحك بإضافة قيود إلى مفتاحك:** يمكنك الحدّ من أذونات المفتاح
  من خلال إضافة [قيود على مفتاح واجهة برمجة التطبيقات](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=ar#add-api-restrictions).
  ويقلّل ذلك من الأضرار المحتملة في حال تسرُّب المفتاح.

للاطّلاع على بعض أفضل الممارسات العامة، يمكنك أيضًا مراجعة [مقالة الدعم](https://support.google.com/googleapi/answer/6310037?hl=ar) هذه.

## تأمين مفاتيح واجهة برمجة التطبيقات غير المقيدة

تكون مفاتيح واجهة برمجة التطبيقات غير المشروطة عرضة للجهات المسيئة والاستخدام غير المصرّح به. اعتبارًا من 19 يونيو 2026، سيتم إيقاف مفاتيح الزيارات غير المقيّدة في Gemini API بهدف تحسين الأمان.

**هذا يعني أنّ طلباتك إلى Gemini API ستفشل إذا لم تتّخذ أي إجراء.**

لمواصلة استخدام Gemini API بدون انقطاع، عليك تأمين مفاتيح حركة المرور
من خلال إضافة قيود في
[AI Studio](https://aistudio.google.com/api-keys?hl=ar).

في [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys?hl=ar)، سيظهر لك بانر لإعلامك عندما تكون مفاتيح واجهة برمجة التطبيقات غير مقيّدة. يمكنك الاطّلاع على المفاتيح غير المشروطة واستخدام الخدمة خلال آخر 90 يومًا.

بالنسبة إلى المفاتيح غير المحظورة، عليك اختيار أحد الخيارَين التاليَين:

- استخدِم المفتاح مع Gemini API فقط.
- استخدِم المفتاح في واجهات برمجة التطبيقات الأخرى غير Gemini.

### حصر استخدام المفتاح في Gemini API فقط

إذا أردت حصر استخدام المفتاح في Gemini API فقط، يمكنك حماية مفتاحك في
[AI Studio](https://aistudio.google.com/api-keys?hl=ar) من خلال النقر على الزر
**حصر الاستخدام في Gemini API**.

### فرض قيود على استخدام المفتاح في واجهات برمجة التطبيقات غير التابعة لـ Gemini

إذا أردت حصر استخدام المفتاح على غير Gemini API، اتّبِع الخطوات التالية:

1. انتقِل إلى
   [صفحة بيانات الاعتماد في Google Cloud Console](https://console.cloud.google.com/apis/credentials?hl=ar).
2. تأكَّد من اختيار المشروع بشكل صحيح.
3. اختَر مفتاح واجهة برمجة التطبيقات.
4. وسِّع القائمة المنسدلة **قيود واجهة برمجة التطبيقات**، وطبِّق قيود الخدمة على مفتاح واجهة برمجة التطبيقات.

إذا أردت تعديل المفاتيح باستخدام قيود حالية أو قيود تمت إضافتها حديثًا، انتقِل إلى [Google Cloud Console](https://console.cloud.google.com/apis/credentials?hl=ar).

## المفاتيح المحظورة

اعتبارًا من 7 مايو 2026، ستحظر واجهة Gemini API مفاتيح واجهة برمجة التطبيقات غير المقيدة
التي لم يتم استخدامها لفترة طويلة. سيظهر للمستخدمين علامة **محظور** بجانب مفتاحهم على [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys?hl=ar)، وسيكون عليهم إنشاء مفتاح جديد أو استخدام مفتاح بديل مقيّد لمواصلة استخدام Gemini API.

## تحديد المشاكل في إنشاء مفتاح واجهة برمجة التطبيقات وحلّها

في Google AI Studio، قد يظهر زر **إنشاء مفتاح واجهة برمجة تطبيقات** غير متاح، مع الرسالة: "*ليس لديك الإذن بإنشاء مفتاح في هذا المشروع*".

يحدث ذلك عندما لا تتوفّر لديك الأذونات اللازمة داخل المشروع لإنشاء مفتاح جديد:

- **`resourcemanager.projects.get`**: تسمح هذه الإذن لـ AI Studio بالتحقّق من توفّر المشروع.
- **`apikeys.keys.create`**: يسمح بإنشاء مفتاح واجهة برمجة التطبيقات نفسه.
- **`serviceusage.services.enable`**: مطلوبة لضمان تفعيل Gemini API في المشروع.
- **`iam.serviceAccounts.create`**: يتطلّب كل مفتاح جديد لواجهة برمجة التطبيقات الآن [حساب خدمة](https://docs.cloud.google.com/docs/authentication/api-keys?hl=ar#api-keys-bound-sa) مرتبطًا، ويتم إنشاؤه عند إنشاء مفتاح واجهة برمجة التطبيقات.
- **`iam.serviceAccountApiKeyBindings.create`**: مطلوب لربط حساب الخدمة الذي تم إنشاؤه حديثًا بمفتاح واجهة برمجة التطبيقات.

لحلّ مشكلة الأذونات، اطلب من مشرف المشروع أو مشرف مؤسستك إذا كان المشروع تابعًا [لمؤسسة](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access?hl=ar) منحك دورًا يتضمّن الأذونات المذكورة أعلاه (مثل "محرّر المشروع" أو دور مخصّص).

إذا لم يكن لديك إذن وصول إداري إلى مشروع، يمكنك إنشاء مشروع جديد غير مرتبط بمؤسسة لإنشاء مفاتيحك.

للاطّلاع على قائمة كاملة بأذونات "إدارة الهوية وإمكانية الوصول" المطلوبة لجميع ميزات Google AI Studio (مثل عرض الاستخدام أو حدود المعدّل أو الفوترة)، راجِع [دليل تحديد المشاكل وحلّها في AI Studio](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=ar#iam-permissions).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
