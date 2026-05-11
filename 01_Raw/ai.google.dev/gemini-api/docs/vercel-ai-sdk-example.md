---
source_url: https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=vi
fetched_at: 2026-05-11T04:58:31.919356+00:00
title: "Market Research Agent (\u0110\u1ea1i l\u00fd nghi\u00ean c\u1ee9u th\u1ecb tr\u01b0\u1eddng) b\u1eb1ng Gemini v\u00e0 AI SDK c\u1ee7a Vercel \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Market Research Agent (Đại lý nghiên cứu thị trường) bằng Gemini và AI SDK của Vercel

[AI SDK của Vercel](https://ai-sdk.dev) là một thư viện mã nguồn mở mạnh mẽ để
xây dựng các ứng dụng, giao diện người dùng và tác nhân dựa trên AI trong TypeScript.

Hướng dẫn này sẽ hướng dẫn bạn cách xây dựng một ứng dụng Node.js bằng TypeScript sử dụng AI SDK để kết nối với Gemini API thông qua [Nhà cung cấp AI tạo sinh của Google](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai) và thực hiện phân tích xu hướng thị trường tự động. Ứng dụng cuối cùng sẽ:

1. Sử dụng Gemini với Google Tìm kiếm để nghiên cứu các xu hướng thị trường hiện tại.
2. Trích xuất dữ liệu có cấu trúc từ nghiên cứu để tạo biểu đồ.
3. Kết hợp nghiên cứu và biểu đồ thành một báo cáo HTML chuyên nghiệp và lưu báo cáo đó dưới dạng tệp PDF.

## Điều kiện tiên quyết

Để hoàn thành hướng dẫn này, bạn cần:

- Khoá Gemini API. Bạn có thể tạo một khoá miễn phí trong [Google AI Studio](https://aistudio.google.com/apikey?hl=vi).
- [Node.js](https://nodejs.org/en/download) phiên bản 18 trở lên.
- Trình quản lý gói, chẳng hạn như `npm`, `pnpm`, hoặc `yarn`.

## Thiết lập ứng dụng

Trước tiên, hãy tạo một thư mục mới cho dự án của bạn và khởi chạy thư mục đó.

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

### Cài đặt phần phụ thuộc

Tiếp theo, hãy cài đặt AI SDK, nhà cung cấp AI tạo sinh của Google và các phần phụ thuộc cần thiết khác.

### npm

```
npm install ai @ai-sdk/google zod
npm install -D @types/node tsx typescript && npx tsc --init
```

Để ngăn lỗi trình biên dịch TypeScript, hãy nhận xét dòng sau trong `tsconfig.json` đã tạo:

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

Để ngăn lỗi trình biên dịch TypeScript, hãy nhận xét dòng sau trong `tsconfig.json` đã tạo:

```
//"verbatimModuleSyntax": true,
```

[Chart.js](https://www.chartjs.org)

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

Gói `puppeteer` yêu cầu chạy một tập lệnh để tải trình duyệt Chromium xuống. Trình quản lý gói có thể yêu cầu bạn phê duyệt, vì vậy hãy đảm bảo bạn phê duyệt tập lệnh khi được nhắc.

### Định cấu hình khoá API

Đặt biến môi trường `GOOGLE_GENERATIVE_AI_API_KEY` bằng khoá Gemini API. Nhà cung cấp AI tạo sinh của Google sẽ tự động tìm khoá API của bạn trong biến môi trường này.

### MacOS/Linux

```
export GOOGLE_GENERATIVE_AI_API_KEY="YOUR_API_KEY_HERE"
```

### Powershell

```
setx GOOGLE_GENERATIVE_AI_API_KEY "YOUR_API_KEY_HERE"
```

## Tạo ứng dụng

Bây giờ, hãy tạo tệp chính cho ứng dụng của chúng ta. Tạo một tệp mới có tên là `main.ts` trong thư mục dự án của bạn. Bạn sẽ xây dựng logic trong tệp này từng bước một.

Để kiểm tra nhanh nhằm đảm bảo mọi thứ được thiết lập đúng cách, hãy thêm mã sau vào `main.ts`. Ví dụ cơ bản này sử dụng `generateText` để nhận câu trả lời đơn giản từ Gemini.

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

Trước khi thêm độ phức tạp, hãy chạy tập lệnh này để xác minh rằng môi trường của bạn được định cấu hình đúng cách. Chạy lệnh sau trong thiết bị đầu cuối:

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

Nếu mọi thứ được thiết lập đúng cách, bạn sẽ thấy câu trả lời của Gemini được in ra bảng điều khiển.

## Nghiên cứu thị trường bằng Google Tìm kiếm

Để nhận thông tin mới nhất, bạn có thể bật công cụ
[Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) cho Gemini. Khi công cụ này hoạt động, mô hình có thể tìm kiếm trên web để trả lời câu lệnh và sẽ trả về các nguồn mà mô hình đã sử dụng.

Thay thế nội dung của `main.ts` bằng mã sau để thực hiện bước đầu tiên trong quá trình phân tích.

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

## Trích xuất dữ liệu biểu đồ

Tiếp theo, hãy xử lý văn bản nghiên cứu để trích xuất dữ liệu có cấu trúc phù hợp với biểu đồ. Sử dụng hàm `generateObject` của AI SDK cùng với lược đồ `zod` để xác định cấu trúc dữ liệu chính xác.

Ngoài ra, hãy tạo một hàm trợ giúp để chuyển đổi dữ liệu có cấu trúc này thành cấu hình mà `Chart.js` có thể hiểu.

Thêm mã sau vào `main.ts`. Lưu ý các lần nhập mới và "Bước 2" đã thêm.

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

## Tạo báo cáo hoàn chỉnh

Ở bước cuối cùng, hãy hướng dẫn Gemini đóng vai trò là người viết báo cáo chuyên gia.
Cung cấp cho Gemini nghiên cứu thị trường, cấu hình biểu đồ và một tập hợp hướng dẫn rõ ràng để xây dựng báo cáo HTML. Sau đó, hãy sử dụng
[Puppeteer](https://pptr.dev/) để kết xuất HTML này và lưu dưới dạng tệp PDF.

Thêm lần nhập `puppeteer` cuối cùng và "Bước 3" vào tệp `main.ts`.

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

## Chạy ứng dụng

Bây giờ, bạn đã sẵn sàng chạy ứng dụng. Thực thi lệnh sau trong thiết bị đầu cuối:

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

Bạn sẽ thấy nhật ký trong thiết bị đầu cuối khi tập lệnh thực thi từng bước.
Sau khi hoàn tất, một tệp `report.pdf` chứa nội dung phân tích thị trường sẽ được tạo trong thư mục dự án của bạn.

Dưới đây, bạn sẽ thấy 2 trang đầu tiên của báo cáo PDF mẫu:

![Báo cáo phân tích thị trường](https://ai.google.dev/static/gemini-api/docs/images/market-research-pdf.jpg?hl=vi)

## Tài nguyên khác

Để biết thêm thông tin về cách xây dựng bằng Gemini và AI SDK, hãy khám phá các tài nguyên sau:

- [Tài liệu về AI SDK](https://ai-sdk.dev/docs)
- [Tài liệu về AI SDK AI tạo sinh của Google](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai)
- [Sổ tay AI SDK: Bắt đầu sử dụng Gemini](https://ai-sdk.dev/cookbook/guides/gemini)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
