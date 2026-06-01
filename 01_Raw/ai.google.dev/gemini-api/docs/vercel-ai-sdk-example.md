---
source_url: https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=tr
fetched_at: 2026-06-01T06:03:08.323842+00:00
title: "Vercel'in Gemini ve AI SDK'si ile Pazar Ara\u015ft\u0131rmas\u0131 Temsilcisi \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Vercel'in Gemini ve AI SDK'si ile Pazar Araştırması Temsilcisi

[Vercel'in AI SDK'sı](https://ai-sdk.dev), TypeScript'te yapay zeka destekli uygulamalar, kullanıcı arayüzleri ve aracıları oluşturmak için kullanılan güçlü bir açık kaynak kitaplıktır.

Bu kılavuzda, [Google Üretken Yapay Zeka Sağlayıcısı](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai) aracılığıyla Gemini API'ye bağlanmak ve otomatik pazar trendi analizi yapmak için yapay zeka SDK'sını kullanan TypeScript ile bir Node.js uygulaması oluşturma adımları açıklanmaktadır. Son uygulama:

1. Mevcut pazar trendlerini araştırmak için Google Arama ile Gemini'ı kullanın.
2. Grafik oluşturmak için araştırmadan yapılandırılmış verileri ayıklayın.
3. Araştırmayı ve grafikleri profesyonel bir HTML raporunda birleştirip PDF olarak kaydedin.

## Ön koşullar

Bu kılavuzu tamamlamak için ihtiyacınız olanlar:

- Gemini API anahtarı. [Google AI Studio](https://aistudio.google.com/apikey?hl=tr)'da ücretsiz olarak oluşturabilirsiniz.
- [Node.js](https://nodejs.org/en/download) 18 veya sonraki sürümler.
- `npm`, `pnpm` veya `yarn` gibi bir paket yöneticisi.

## Uygulamanızı ayarlama

Öncelikle projeniz için yeni bir dizin oluşturun ve bu dizini başlatın.

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

### yumak

```
mkdir market-trend-app
cd market-trend-app
yarn init -y
```

### Bağımlıları yükleme

Ardından, yapay zeka SDK'sını, Google Üretken Yapay Zeka sağlayıcısını ve diğer gerekli bağımlılıkları yükleyin.

### npm

```
npm install ai @ai-sdk/google zod
npm install -D @types/node tsx typescript && npx tsc --init
```

TypeScript derleyici hatasını önlemek için oluşturulan `tsconfig.json` dosyasında aşağıdaki satırı yorum satırı yapın:

```
//"verbatimModuleSyntax": true,
```

### pnpm

```
pnpm add ai @ai-sdk/google zod
pnpm add -D @types/node tsx typescript
```

### yumak

```
yarn add ai @ai-sdk/google zod
yarn add -D @types/node tsx typescript && yarn tsc --init
```

TypeScript derleyici hatasını önlemek için oluşturulan `tsconfig.json` dosyasında aşağıdaki satırı yorum satırı yapın:

```
//"verbatimModuleSyntax": true,
```

Bu uygulama, grafikleri oluşturmak ve PDF oluşturmak için [Puppeteer](https://pptr.dev/) ve [Chart.js](https://www.chartjs.org) adlı üçüncü taraf paketlerini de kullanır:

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

### yumak

```
yarn add puppeteer chart.js
yarn add -D @types/chart.js
```

`puppeteer` paketinin Chromium tarayıcısını indirmek için bir komut dosyası çalıştırması gerekir. Paket yöneticiniz onay isteyebilir. Bu nedenle, istendiğinde komut dosyasını onayladığınızdan emin olun.

### API anahtarınızı yapılandırma

`GOOGLE_GENERATIVE_AI_API_KEY` ortam değişkenini Gemini API anahtarınızla ayarlayın. Google Üretken Yapay Zeka Sağlayıcısı, API anahtarınızı bu ortam değişkeninde otomatik olarak arar.

### MacOS/Linux

```
export GOOGLE_GENERATIVE_AI_API_KEY="YOUR_API_KEY_HERE"
```

### Powershell

```
setx GOOGLE_GENERATIVE_AI_API_KEY "YOUR_API_KEY_HERE"
```

## Uygulamanızı oluşturma

Şimdi uygulamamızın ana dosyasını oluşturalım. Proje dizininizde
`main.ts` adlı yeni bir dosya oluşturun. Bu dosyada mantığı adım adım oluşturacaksınız.

Her şeyin doğru şekilde ayarlandığından emin olmak için hızlı bir test yapmak üzere aşağıdaki kodu `main.ts`'ya ekleyin. Bu temel örnekte, Gemini'dan basit bir yanıt almak için `generateText` kullanılıyor.

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

Daha fazla karmaşıklık eklemeden önce ortamınızın doğru şekilde yapılandırıldığını doğrulamak için bu komut dosyasını çalıştırın. Terminalinizde aşağıdaki komutu çalıştırın:

### npm

```
npx tsc && node main.js
```

### pnpm

```
pnpm tsx main.ts
```

### yumak

```
yarn tsc && node main.js
```

Her şey doğru şekilde ayarlanmışsa Gemini'ın yanıtı konsola yazdırılır.

## Google Arama ile pazar araştırması yapma

Güncel bilgilere ulaşmak için Gemini'da [Google Arama](https://ai.google.dev/gemini-api/docs/google-search?hl=tr) aracını etkinleştirebilirsiniz. Bu araç etkinken model, istemi yanıtlamak için web'de arama yapabilir ve kullandığı kaynakları döndürür.

Analizimizin ilk adımını gerçekleştirmek için `main.ts` içeriğini aşağıdaki kodla değiştirin.

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

## Grafik verilerini ayıklama

Ardından, araştırma metnini işleyerek grafiklere uygun yapılandırılmış verileri çıkaralım. Tam veri yapısını tanımlamak için `generateObject` işlevini `zod` şemasıyla birlikte kullanın.

Ayrıca, bu yapılandırılmış verileri `Chart.js`'nın anlayabileceği bir yapılandırmaya dönüştürmek için yardımcı bir işlev oluşturun.

Aşağıdaki kodu `main.ts` dosyasına ekleyin. Yeni içe aktarmaları ve eklenen "2. adım"ı inceleyin.

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

## Son raporu oluşturma

Son adımda, Gemini'a uzman bir rapor yazarı gibi davranmasını söyleyin.
Pazar araştırması, grafik yapılandırmaları ve HTML raporu oluşturmayla ilgili net talimatlar sağlayın. Ardından, bu HTML'yi oluşturmak ve PDF olarak kaydetmek için [Puppeteer](https://pptr.dev/)'ı kullanın.

Nihai `puppeteer` içe aktarma işlemini ve "3. Adım"ı `main.ts` dosyanıza ekleyin.

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

## Uygulamanızı çalıştırma

Artık uygulamayı çalıştırmaya hazırsınız. Terminalinizde aşağıdaki komutu çalıştırın:

### npm

```
npx tsc && node main.js
```

### pnpm

```
pnpm tsx main.ts
```

### yumak

```
yarn tsc && node main.js
```

Komut dosyası her adımı uyguladığında terminalinizde günlük kaydı görürsünüz.
İşlem tamamlandığında, pazar analizinizin yer aldığı bir `report.pdf` dosyası proje dizininizde oluşturulur.

Aşağıda, örnek bir PDF raporunun ilk iki sayfasını görebilirsiniz:

![Pazar analizi raporu](https://ai.google.dev/static/gemini-api/docs/images/market-research-pdf.jpg?hl=tr)

## Diğer kaynaklar

Gemini ve Yapay Zeka SDK'sı ile geliştirme hakkında daha fazla bilgi edinmek için şu kaynakları inceleyin:

- [AI SDK belgeleri](https://ai-sdk.dev/docs)
- [Yapay Zeka SDK'sı Google Üretken Yapay Zeka belgeleri](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai)
- [AI SDK cookbook: Get Started with Gemini](https://ai-sdk.dev/cookbook/guides/gemini) (AI SDK yemek kitabı: Gemini'ı kullanmaya başlama)

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-19 UTC."],[],[]]
