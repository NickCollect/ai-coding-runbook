---
source_url: https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=ar
fetched_at: 2026-08-17T02:18:21.586456+00:00
title: "\u0623\u062f\u0627\u0629 Market Research Agent \u0627\u0644\u0645\u0633\u062a\u0646\u062f\u0629 \u0625\u0644\u0649 Gemini \u0648\u062d\u0632\u0645\u0629 \u062a\u0637\u0648\u064a\u0631 \u0627\u0644\u0628\u0631\u0627\u0645\u062c (SDK) \u0627\u0644\u0645\u0633\u062a\u0646\u062f\u0629 \u0625\u0644\u0649 \u0627\u0644\u0630\u0643\u0627\u0621 \u0627\u0644\u0627\u0635\u0637\u0646\u0627\u0639\u064a \u0645\u0646 Vercel \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# أداة Market Research Agent المستندة إلى Gemini وحزمة تطوير البرامج (SDK) المستندة إلى الذكاء الاصطناعي من Vercel

‫[AI SDK من Vercel](https://ai-sdk.dev) هي مكتبة قوية مفتوحة المصدر تتيح إنشاء تطبيقات وواجهات مستخدم ووكلاء مستندين إلى الذكاء الاصطناعي في TypeScript.

سيرشدك هذا الدليل إلى كيفية إنشاء تطبيق Node.js باستخدام TypeScript
يستخدِم حزمة تطوير البرامج (SDK) المستندة إلى الذكاء الاصطناعي للتواصل مع واجهة Gemini API من خلال [مزوّد الذكاء الاصطناعي التوليدي من Google](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai) وإجراء تحليل آلي لاتجاهات السوق. سيتضمّن التطبيق النهائي ما يلي:

1. استخدِم Gemini مع "بحث Google" للبحث عن مؤشرات السوق الحالية.
2. استخراج بيانات منظَّمة من البحث لإنشاء رسوم بيانية
3. يمكنك دمج البحث والرسومات البيانية في تقرير HTML احترافي وحفظه كملف PDF.

## المتطلبات الأساسية

لإكمال هذا الدليل، ستحتاج إلى:

- مفتاح Gemini API يمكنك إنشاء واحد مجانًا في [Google AI Studio](https://aistudio.google.com/apikey?hl=ar).
- الإصدار 18 من [Node.js](https://nodejs.org/en/download) أو الإصدارات الأحدث
- أداة إدارة الحِزم، مثل `npm` أو `pnpm` أو `yarn`

## إعداد تطبيقك

أولاً، أنشئ دليلاً جديدًا لمشروعك وابدأ تهيئته.

### npm

```
mkdir market-trend-app
cd market-trend-app
npm init -y
```

### pnpm

```
mkdir market-trend-app
cd market-trend-app
pnpm init
```

### خيط غزل

```
mkdir market-trend-app
cd market-trend-app
yarn init -y
```

### تثبيت الحِزم التابعة

بعد ذلك، ثبِّت حزمة تطوير البرامج للذكاء الاصطناعي ومزوّد خدمة الذكاء الاصطناعي التوليدي من Google والتبعيات الأخرى اللازمة.

### npm

```
npm install ai @ai-sdk/google zod
npm install -D @types/node tsx typescript && npx tsc --init
```

لتجنُّب حدوث خطأ في برنامج الترجمة البرمجية TypeScript، علِّق على السطر التالي في ملف `tsconfig.json` الذي تم إنشاؤه:

```
//"verbatimModuleSyntax": true,
```

### pnpm

```
pnpm add ai @ai-sdk/google zod
pnpm add -D @types/node tsx typescript
```

### خيط غزل

```
yarn add ai @ai-sdk/google zod
yarn add -D @types/node tsx typescript && yarn tsc --init
```

لتجنُّب حدوث خطأ في برنامج الترجمة البرمجية TypeScript، علِّق على السطر التالي في ملف `tsconfig.json` الذي تم إنشاؤه:

```
//"verbatimModuleSyntax": true,
```

سيستخدم هذا التطبيق أيضًا حِزم الجهات الخارجية [Puppeteer](https://pptr.dev/)
و[Chart.js](https://www.chartjs.org) لعرض الرسوم البيانية
وإنشاء ملف PDF:

### npm

```
npm install puppeteer chart.js
npm install -D @types/chart.js
```

### pnpm

```
pnpm add puppeteer chart.js
pnpm add -D @types/chart.js
```

### خيط غزل

```
yarn add puppeteer chart.js
yarn add -D @types/chart.js
```

تتطلّب حزمة `puppeteer` تنفيذ نص برمجي لتنزيل متصفّح Chromium. قد يطلب منك مدير الحِزم الموافقة، لذا احرص على الموافقة على البرنامج النصي عند مطالبتك بذلك.

### ضبط مفتاح واجهة برمجة التطبيقات

اضبط متغيّر البيئة `GOOGLE_GENERATIVE_AI_API_KEY` باستخدام مفتاح Gemini API. يبحث "موفّر الذكاء الاصطناعي التوليدي من Google" تلقائيًا عن مفتاح واجهة برمجة التطبيقات في متغيّر البيئة هذا.

### ‫MacOS/Linux

```
export GOOGLE_GENERATIVE_AI_API_KEY="YOUR_API_KEY_HERE"
```

### Powershell

```
setx GOOGLE_GENERATIVE_AI_API_KEY "YOUR_API_KEY_HERE"
```

## إنشاء تطبيقك

الآن، لننشئ الملف الرئيسي لتطبيقنا. أنشئ ملفًا جديدًا باسم
`main.ts` في دليل مشروعك. ستنشئ منطقًا في هذا الملف
خطوة بخطوة.

لإجراء اختبار سريع للتأكّد من إعداد كل شيء بشكل صحيح، أضِف الرمز التالي إلى `main.ts`. يستخدم هذا المثال الأساسي `generateText` للحصول على ردّ بسيط من Gemini.

```
import { google } from "@ai-sdk/google";
import { generateText } from "ai";

async function main() {
  const { text } = await generateText({
    model: google("gemini-3.5-flash"),
    prompt: 'What is plant-based milk?',
  });

  console.log(text);
}

main().catch(console.error);
```

قبل إضافة المزيد من التعقيد، شغِّل هذا النص البرمجي للتأكّد من أنّ بيئتك
تم إعدادها بشكل صحيح. نفِّذ الأمر التالي في الوحدة الطرفية:

### npm

```
npx tsc && node main.js
```

### pnpm

```
pnpm tsx main.ts
```

### خيط غزل

```
yarn tsc && node main.js
```

إذا تم إعداد كل شيء بشكل صحيح، سيظهر ردّ Gemini مطبوعًا على وحدة التحكّم.

## إجراء أبحاث السوق باستخدام "بحث Google"

للحصول على معلومات حديثة، يمكنك تفعيل أداة
[بحث Google](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) في Gemini. عندما تكون هذه الأداة
مفعّلة، يمكن للنموذج البحث على الويب للرد على الطلب وسيعرض
المصادر التي استخدمها.

استبدِل محتوى `main.ts` بالرمز التالي لتنفيذ الخطوة الأولى من التحليل.

```
import { google } from "@ai-sdk/google";
import { generateText } from "ai";

async function main() {
  // Step 1: Search market trends
  const { text: marketTrends, sources } = await generateText({
    model: google("gemini-3.5-flash"),
    tools: {
      google_search: google.tools.googleSearch({}),
    },
    prompt: `Search the web for market trends for plant-based milk in North America for 2024-2025.
          I need to know the market size, key players and their market share, and primary consumer drivers.
          `,
  });

  console.log("Market trends found:\n", marketTrends);
  // To see the sources, uncomment the following line:
  // console.log("Sources:\n", sources);
}

main().catch(console.error);
```

## استخراج بيانات الرسم البياني

بعد ذلك، لنعالج نص البحث لاستخراج بيانات منظَّمة مناسبة للرسومات البيانية. استخدِم الدالة `generateObject` في حزمة تطوير البرامج (SDK) الخاصة بالذكاء الاصطناعي مع مخطط `zod` لتحديد بنية البيانات الدقيقة.

أنشئ أيضًا دالة مساعدة لتحويل هذه البيانات المنظَّمة إلى إعداد يمكن أن يفهمه `Chart.js`.

أضِف الرمز التالي إلى `main.ts`. لاحظ عمليات الاستيراد الجديدة و "الخطوة 2" المضافة.

```
import { google } from "@ai-sdk/google";
import { generateText, generateObject } from "ai";
import { z } from "zod/v4";
import { ChartConfiguration } from "chart.js";

// Helper function to create Chart.js configurations
function createChartConfig({labels, data, label, type, colors,}: {
  labels: string[];
  data: number[];
  label: string;
  type: "bar" | "line";
  colors: string[];
}): ChartConfiguration {
  return {
    type: type,
    data: {
      labels: labels,
      datasets: [
        {
          label: label,
          data: data,
          borderWidth: 1,
          ...(type === "bar" && { backgroundColor: colors }),
          ...(type === "line" && colors.length > 0 && { borderColor: colors[0] }),
        },
      ],
    },
    options: {
      animation: { duration: 0 }, // Disable animations for static PDF rendering
    },
  };
}

async function main() {
  // Step 1: Search market trends
  const { text: marketTrends, sources } = await generateText({
    model: google("gemini-3.5-flash"),
    tools: {
      google_search: google.tools.googleSearch({}),
    },
    prompt: `Search the web for market trends for plant-based milk in North America for 2024-2025.
          I need to know the market size, key players and their market share, and primary consumer drivers.
          `,
  });

  console.log("Market trends found.");

  // Step 2: Extract chart data
  const { object: chartData } = await generateObject({
    model: google("gemini-3.5-flash"),
    schema: z.object({
      chartConfigurations: z
        .array(
          z.object({
            type: z.enum(["bar", "line"]).describe('The type of chart to generate. Either "bar" or "line"',),
            labels: z.array(z.string()).describe("A list of chart labels"),
            data: z.array(z.number()).describe("A list of the chart data"),
            label: z.string().describe("A label for the chart"),
            colors: z.array(z.string()).describe('A list of colors to use for the chart, e.g. "rgba(255, 99, 132, 0.8)"',),
          }),
        )
        .describe("A list of chart configurations"),
    }),
    prompt: `Given the following market trends text, come up with a list of 1-3 meaningful bar or line charts
    and generate chart data.
    
Market Trends:
${marketTrends}
`,
  });

  const chartConfigs = chartData.chartConfigurations.map(createChartConfig);

  console.log("Chart configurations generated.");
}

main().catch(console.error);
```

## إنشاء التقرير النهائي

في الخطوة الأخيرة، اطلب من Gemini أن يتولّى دور كاتب تقارير خبير.
زوِّدها بأبحاث السوق وإعدادات الرسم البياني ومجموعة واضحة من التعليمات لإنشاء تقرير بتنسيق HTML. بعد ذلك، استخدِم
[Puppeteer](https://pptr.dev/) لعرض ملف HTML هذا وحفظه كملف PDF.

أضِف عملية الاستيراد النهائية `puppeteer` و "الخطوة 3" إلى ملف `main.ts`.

```
// ... (imports from previous step)
import puppeteer from "puppeteer";

// ... (createChartConfig helper function from previous step)

async function main() {
  // ... (Step 1 and 2 from previous step)

  // Step 3: Generate the final HTML report and save it as a PDF
  const { text: htmlReport } = await generateText({
    model: google("gemini-3.5-flash"),
    prompt: `You are an expert financial analyst and report writer.
    Your task is to generate a comprehensive market analysis report in HTML format.

    **Instructions:**
    1.  Write a full HTML document.
    2.  Use the provided "Market Trends" text to write the main body of the report. Structure it with clear headings and paragraphs.
    3.  Incorporate the provided "Chart Configurations" to visualize the data. For each chart, you MUST create a unique <canvas> element and a corresponding <script> block to render it using Chart.js.
    4.  Reference the "Sources" at the end of the report.
    5.  Do not include any placeholder data; use only the information provided.
    6.  Return only the raw HTML code.

    **Chart Rendering Snippet:**
    Include this script in the head of the HTML: <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    For each chart, use a structure like below, ensuring the canvas 'id' is unique for each chart, and apply the correspinding config:

    ---
    <div style="width: 800px; height: 600px;">
      <canvas id="chart1"></canvas>
    </div>
    <script>
      new Chart(document.getElementById('chart1'), config);
    </script>
    ---
    (For the second chart, use 'chart2' and the corresponding config, and so on.)

    **Data:**
    - Market Trends: ${marketTrends}
    - Chart Configurations: ${JSON.stringify(chartConfigs)}
    - Sources: ${JSON.stringify(sources)}
    `,
  });

  // LLMs may wrap the HTML in a markdown code block, so strip it.
  const finalHtml = htmlReport.replace(/^```html\n/, "").replace(/\n```$/, "");

  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setContent(finalHtml);
  await page.pdf({ path: "report.pdf", format: "A4" });
  await browser.close();

  console.log("\nReport generated successfully: report.pdf");
}

main().catch(console.error);
```

## تشغيل تطبيقك

أنت الآن جاهز لتشغيل التطبيق. نفِّذ الأمر التالي في الوحدة الطرفية:

### npm

```
npx tsc && node main.js
```

### pnpm

```
pnpm tsx main.ts
```

### خيط غزل

```
yarn tsc && node main.js
```

ستظهر لك عملية التسجيل في نافذة الأوامر أثناء تنفيذ البرنامج النصي لكل خطوة.
بعد اكتمال العملية، سيتم إنشاء ملف `report.pdf` يحتوي على تحليل السوق في دليل مشروعك.

في ما يلي أول صفحتَين من نموذج تقرير بتنسيق PDF:

![تقرير تحليل السوق](https://ai.google.dev/static/gemini-api/docs/images/market-research-pdf.jpg?hl=ar)

## موارد أخرى

لمزيد من المعلومات حول إنشاء التطبيقات باستخدام Gemini وAI SDK، يمكنك الاطّلاع على الموارد التالية:

- [مستندات حزمة تطوير البرامج (SDK) المستندة إلى الذكاء الاصطناعي](https://ai-sdk.dev/docs)
- [مستندات "الذكاء الاصطناعي التوليدي من Google" الخاصة بحزمة تطوير البرامج (SDK)](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai)
- [كتاب وصفات حزمة تطوير البرامج (SDK) المستندة إلى الذكاء الاصطناعي: بدء استخدام Gemini](https://ai-sdk.dev/cookbook/guides/gemini)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-19 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-19 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
