---
source_url: https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=de
fetched_at: 2026-07-27T04:42:08.015677+00:00
title: "Market Research Agent mit Gemini und dem AI\u00a0SDK von Vercel \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Market Research Agent mit Gemini und dem AI SDK von Vercel

Das [AI SDK von Vercel](https://ai-sdk.dev) ist eine leistungsstarke Open-Source-Bibliothek zum
Erstellen von KI-gestützten Anwendungen, Benutzeroberflächen und Agenten in TypeScript.

In dieser Anleitung erfahren Sie, wie Sie eine Node.js-Anwendung mit TypeScript erstellen, die das AI SDK verwendet, um über den [Google Generative AI Provider](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai) eine Verbindung zur Gemini API herzustellen und eine automatisierte Markttrendanalyse durchzuführen. Die fertige Anwendung kann Folgendes:

1. Gemini mit der Google Suche verwenden, um aktuelle Markttrends zu recherchieren.
2. Strukturierte Daten aus der Recherche extrahieren, um Diagramme zu erstellen.
3. Die Recherche und die Diagramme in einem professionellen HTML-Bericht zusammenfassen und als PDF speichern.

## Vorbereitung

Für diese Anleitung benötigen Sie Folgendes:

- Einen Gemini API-Schlüssel. Sie können ihn kostenlos in [Google AI Studio](https://aistudio.google.com/apikey?hl=de) erstellen.
- [Node.js](https://nodejs.org/en/download), Version 18 oder höher.
- Einen Paketmanager wie `npm`, `pnpm`, oder `yarn`.

## Anwendung einrichten

Erstellen Sie zuerst ein neues Verzeichnis für Ihr Projekt und initialisieren Sie es.

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

### Abhängigkeiten installieren

Installieren Sie als Nächstes das AI SDK, den Google Generative AI Provider und andere erforderliche Abhängigkeiten.

### npm

```
npm install ai @ai-sdk/google zod
npm install -D @types/node tsx typescript && npx tsc --init
```

Um einen TypeScript-Compilerfehler zu vermeiden, kommentieren Sie die folgende Zeile in der generierten `tsconfig.json`-Datei aus:

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

Um einen TypeScript-Compilerfehler zu vermeiden, kommentieren Sie die folgende Zeile in der generierten `tsconfig.json`-Datei aus:

```
//"verbatimModuleSyntax": true,
```

Diese Anwendung verwendet auch die Drittanbieterpakete [Puppeteer](https://pptr.dev/)
und [Chart.js](https://www.chartjs.org) zum Rendern von Diagrammen und
zum Erstellen einer PDF-Datei:

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

Für das `puppeteer`-Paket muss ein Skript ausgeführt werden, um den Chromium-Browser herunterzuladen. Ihr Paketmanager fordert möglicherweise eine Genehmigung an. Genehmigen Sie das Skript, wenn Sie dazu aufgefordert werden.

### API-Schlüssel konfigurieren

Legen Sie die Umgebungsvariable `GOOGLE_GENERATIVE_AI_API_KEY` mit Ihrem Gemini API-Schlüssel fest. Der Google Generative AI Provider sucht automatisch in dieser Umgebungsvariable nach Ihrem API-Schlüssel.

### macOS/Linux

```
export GOOGLE_GENERATIVE_AI_API_KEY="YOUR_API_KEY_HERE"
```

### Powershell

```
setx GOOGLE_GENERATIVE_AI_API_KEY "YOUR_API_KEY_HERE"
```

## Anwendung erstellen

Erstellen wir nun die Hauptdatei für unsere Anwendung. Erstellen Sie in Ihrem Projektverzeichnis eine neue Datei mit dem Namen `main.ts`. Die Logik wird in dieser Datei Schritt für Schritt aufgebaut.

Fügen Sie der Datei `main.ts` den folgenden Code hinzu, um zu prüfen, ob alles richtig eingerichtet ist. In diesem einfachen Beispiel wird `generateText` verwendet, um eine einfache Antwort von Gemini zu erhalten.

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

Bevor Sie weitere Komplexität hinzufügen, führen Sie dieses Skript aus, um zu prüfen, ob Ihre Umgebung richtig konfiguriert ist. Führen Sie in Ihrem Terminal den folgenden Befehl aus:

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

Wenn alles richtig eingerichtet ist, wird die Antwort von Gemini in der Konsole ausgegeben.

## Marktforschung mit der Google Suche durchführen

Wenn Sie aktuelle Informationen erhalten möchten, können Sie das
[Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=de)-Tool für Gemini aktivieren. Wenn dieses Tool aktiv ist, kann das Modell im Web nach Antworten auf den Prompt suchen und gibt die verwendeten Quellen zurück.

Ersetzen Sie den Inhalt von `main.ts` durch den folgenden Code, um den ersten Schritt unserer Analyse auszuführen.

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

## Diagrammdaten extrahieren

Als Nächstes verarbeiten wir den Recherchetext, um strukturierte Daten zu extrahieren, die für Diagramme geeignet sind. Verwenden Sie die Funktion `generateObject` des AI SDK zusammen mit einem `zod`-Schema, um die genaue Datenstruktur zu definieren.

Erstellen Sie außerdem eine Hilfsfunktion, um diese strukturierten Daten in eine Konfiguration zu konvertieren, die `Chart.js` verstehen kann.

Fügen Sie der Datei `main.ts` den folgenden Code hinzu. Beachten Sie die neuen Importe und den hinzugefügten Schritt 2.

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

## Abschlussbericht erstellen

Im letzten Schritt weisen Sie Gemini an, als Experte für das Erstellen von Berichten zu fungieren.
Geben Sie die Marktforschung, die Diagrammkonfigurationen und eine klare Anleitung zum Erstellen eines HTML-Berichts an. Verwenden Sie dann
[Puppeteer](https://pptr.dev/), um diesen HTML-Code zu rendern und als PDF zu speichern.

Fügen Sie den letzten `puppeteer`-Import und Schritt 3 der Datei `main.ts` hinzu.

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

## Führen Sie Ihre Anwendung aus

Sie können die Anwendung jetzt ausführen. Führen Sie im Terminal folgenden Befehl aus:

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

Im Terminal wird eine Protokollierung angezeigt, während das Skript die einzelnen Schritte ausführt.
Nach Abschluss wird in Ihrem Projektverzeichnis eine Datei `report.pdf` mit Ihrer Marktanalyse erstellt.

Unten sehen Sie die ersten beiden Seiten eines Beispiel-PDF-Berichts:

![Marktanalysebericht](https://ai.google.dev/static/gemini-api/docs/images/market-research-pdf.jpg?hl=de)

## Weitere Ressourcen

Weitere Informationen zum Erstellen von Anwendungen mit Gemini und dem AI SDK finden Sie in den folgenden Ressourcen:

- [AI SDK-Dokumentation](https://ai-sdk.dev/docs)
- [AI SDK Google Generative AI-Dokumentation](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai)
- [AI SDK-Kochbuch: Erste Schritte mit Gemini](https://ai-sdk.dev/cookbook/guides/gemini)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-05-19 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-05-19 (UTC)."],[],[]]
