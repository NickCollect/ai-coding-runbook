---
source_url: https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=id
fetched_at: 2026-05-05T20:03:21.329067+00:00
title: "Agen Riset Pasar dengan Gemini dan AI SDK dari Vercel \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Agen Riset Pasar dengan Gemini dan AI SDK dari Vercel

[AI SDK dari Vercel](https://ai-sdk.dev) adalah library open source yang canggih untuk
membangun aplikasi, antarmuka pengguna, dan agen yang didukung AI di TypeScript.

Panduan ini akan memandu Anda membangun aplikasi Node.js dengan TypeScript
yang menggunakan AI SDK untuk terhubung dengan Gemini API melalui [Google Generative AI Provider](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai) dan melakukan analisis tren pasar otomatis. Aplikasi akhir akan:

1. Menggunakan Gemini dengan Google Penelusuran untuk meneliti tren pasar saat ini.
2. Mengekstrak data terstruktur dari riset untuk membuat diagram.
3. Menggabungkan riset dan diagram ke dalam laporan HTML profesional dan menyimpannya sebagai PDF.

## Prasyarat

Untuk menyelesaikan panduan ini, Anda memerlukan:

- Kunci Gemini API. Anda dapat membuatnya secara gratis di [Google AI Studio](https://aistudio.google.com/apikey?hl=id).
- [Node.js](https://nodejs.org/en/download) versi 18 atau yang lebih baru.
- Pengelola paket, seperti `npm`, `pnpm`, atau `yarn`.

## Menyiapkan aplikasi Anda

Pertama, buat direktori baru untuk project Anda dan lakukan inisialisasi.

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

### yarn

```
mkdir market-trend-app
cd market-trend-app
yarn init -y
```

### Menginstal dependensi

Selanjutnya, instal AI SDK, Google Generative AI Provider, dan dependensi lain yang diperlukan.

### npm

```
npm install ai @ai-sdk/google zod
npm install -D @types/node tsx typescript && npx tsc --init
```

Untuk mencegah error pengompilasi TypeScript, beri komentar pada baris berikut di `tsconfig.json` yang dihasilkan:

```
//"verbatimModuleSyntax": true,
```

### pnpm

```
pnpm add ai @ai-sdk/google zod
pnpm add -D @types/node tsx typescript
```

### yarn

```
yarn add ai @ai-sdk/google zod
yarn add -D @types/node tsx typescript && yarn tsc --init
```

Untuk mencegah error pengompilasi TypeScript, beri komentar pada baris berikut di `tsconfig.json` yang dihasilkan:

```
//"verbatimModuleSyntax": true,
```

Aplikasi ini juga akan menggunakan paket pihak ketiga [Puppeteer](https://pptr.dev/)
dan [Chart.js](https://www.chartjs.org) untuk merender diagram dan
membuat PDF:

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

### yarn

```
yarn add puppeteer chart.js
yarn add -D @types/chart.js
```

Paket `puppeteer` mengharuskan Anda menjalankan skrip untuk mendownload browser Chromium. Pengelola paket Anda mungkin akan meminta persetujuan, jadi pastikan Anda menyetujui skrip saat diminta.

### Mengonfigurasi kunci API Anda

Tetapkan variabel lingkungan `GOOGLE_GENERATIVE_AI_API_KEY` dengan kunci Gemini API Anda. Google Generative AI Provider akan otomatis mencari kunci API Anda di variabel lingkungan ini.

### MacOS/Linux

```
export GOOGLE_GENERATIVE_AI_API_KEY="YOUR_API_KEY_HERE"
```

### Powershell

```
setx GOOGLE_GENERATIVE_AI_API_KEY "YOUR_API_KEY_HERE"
```

## Membuat aplikasi Anda

Sekarang, mari kita buat file utama untuk aplikasi kita. Buat file baru bernama `main.ts` di direktori project Anda. Anda akan membangun logika dalam file ini langkah demi langkah.

Untuk pengujian cepat guna memastikan semuanya disiapkan dengan benar, tambahkan kode berikut ke `main.ts`. Contoh dasar ini menggunakan `generateText` untuk mendapatkan respons sederhana dari Gemini.

```
import { google } from "@ai-sdk/google";
import { generateText } from "ai";

async function main() {
  const { text } = await generateText({
    model: google("gemini-3-flash-preview"),
    prompt: 'What is plant-based milk?',
  });

  console.log(text);
}

main().catch(console.error);
```

Sebelum menambahkan kompleksitas lainnya, jalankan skrip ini untuk memverifikasi bahwa lingkungan Anda dikonfigurasi dengan benar. Jalankan perintah berikut di terminal.

### npm

```
npx tsc && node main.js
```

### pnpm

```
pnpm tsx main.ts
```

### yarn

```
yarn tsc && node main.js
```

Jika semuanya disiapkan dengan benar, Anda akan melihat respons Gemini dicetak ke konsol.

## Melakukan riset pasar dengan Google Penelusuran

Untuk mendapatkan informasi terbaru, Anda dapat mengaktifkan alat
[Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id) untuk Gemini. Jika alat ini aktif, model dapat menelusuri web untuk menjawab perintah dan akan menampilkan sumber yang digunakannya.

Ganti konten `main.ts` dengan kode berikut untuk melakukan langkah pertama analisis kita.

```
import { google } from "@ai-sdk/google";
import { generateText } from "ai";

async function main() {
  // Step 1: Search market trends
  const { text: marketTrends, sources } = await generateText({
    model: google("gemini-3-flash-preview"),
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

## Mengekstrak data diagram

Selanjutnya, mari kita proses teks riset untuk mengekstrak data terstruktur yang sesuai untuk diagram. Gunakan fungsi `generateObject` AI SDK bersama dengan skema `zod` untuk menentukan struktur data yang tepat.

Buat juga fungsi helper untuk mengonversi data terstruktur ini menjadi konfigurasi yang dapat dipahami `Chart.js`.

Tambahkan kode berikut ke `main.ts`. Perhatikan impor baru dan "Langkah 2" yang ditambahkan.

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
    model: google("gemini-3-flash-preview"),
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
    model: google("gemini-3-flash-preview"),
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

## Membuat laporan akhir

Pada langkah terakhir, instruksikan Gemini untuk bertindak sebagai penulis laporan ahli.
Berikan riset pasar, konfigurasi diagram, dan serangkaian petunjuk yang jelas untuk membangun laporan HTML. Kemudian, gunakan
[Puppeteer](https://pptr.dev/) untuk merender HTML ini dan menyimpannya sebagai PDF.

Tambahkan impor `puppeteer` akhir dan "Langkah 3" ke file `main.ts` Anda.

```
// ... (imports from previous step)
import puppeteer from "puppeteer";

// ... (createChartConfig helper function from previous step)

async function main() {
  // ... (Step 1 and 2 from previous step)

  // Step 3: Generate the final HTML report and save it as a PDF
  const { text: htmlReport } = await generateText({
    model: google("gemini-3-flash-preview"),
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

## Menjalankan aplikasi Anda

Anda kini siap menjalankan aplikasi. Jalankan perintah berikut di terminal:

### npm

```
npx tsc && node main.js
```

### pnpm

```
pnpm tsx main.ts
```

### yarn

```
yarn tsc && node main.js
```

Anda akan melihat logging di terminal saat skrip menjalankan setiap langkah.
Setelah selesai, file `report.pdf` yang berisi analisis pasar Anda akan dibuat di direktori project Anda.

Di bawah ini, Anda akan melihat dua halaman pertama dari contoh laporan PDF:

![Laporan analisis pasar](https://ai.google.dev/static/gemini-api/docs/images/market-research-pdf.jpg?hl=id)

## Aset lainnya

Untuk mengetahui informasi selengkapnya tentang cara membangun dengan Gemini dan AI SDK, pelajari referensi berikut:

- [Dokumen AI SDK](https://ai-sdk.dev/docs)
- [Dokumen AI SDK Google Generative AI](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai)
- [Cookbook AI SDK: Memulai Gemini](https://ai-sdk.dev/cookbook/guides/gemini)

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-04-29 UTC."],[],[]]
