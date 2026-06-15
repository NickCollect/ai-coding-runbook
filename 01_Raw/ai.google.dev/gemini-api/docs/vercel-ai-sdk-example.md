---
source_url: https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=pl
fetched_at: 2026-06-15T06:20:24.051593+00:00
title: "Agent do bada\u0144 rynku z\u00a0Gemini i\u00a0pakietem AI SDK od Vercel \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Agent do badań rynku z Gemini i pakietem AI SDK od Vercel

[AI SDK od Vercel](https://ai-sdk.dev) to zaawansowana biblioteka open source do tworzenia aplikacji, interfejsów użytkownika i agentów opartych na AI w TypeScript.

Z tego przewodnika dowiesz się, jak utworzyć aplikację w Node.js z TypeScriptem, która korzysta z pakietu AI SDK do łączenia się z interfejsem Gemini API za pomocą [dostawcy generatywnej AI od Google](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai) i przeprowadzania automatycznej analizy trendów rynkowych. Ostateczna aplikacja:

1. Używaj Gemini z wyszukiwarką Google, aby badać aktualne trendy rynkowe.
2. Wyodrębnij z badań dane strukturalne, aby wygenerować wykresy.
3. Połącz wyniki badań i wykresy w profesjonalny raport HTML i zapisz go jako plik PDF.

## Wymagania wstępne

Aby skorzystać z tego przewodnika, potrzebujesz:

- Klucz interfejsu Gemini API. Możesz go utworzyć bezpłatnie w [Google AI Studio](https://aistudio.google.com/apikey?hl=pl).
- [Node.js](https://nodejs.org/en/download) w wersji 18 lub nowszej.
- Menedżer pakietów, np. `npm`, `pnpm` lub `yarn`.

## Konfigurowanie aplikacji

Najpierw utwórz nowy katalog projektu i go zainicjuj.

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

### włóczka

```
mkdir market-trend-app
cd market-trend-app
yarn init -y
```

### Instalowanie zależności

Następnie zainstaluj pakiet AI SDK, dostawcę Google Generative AI i inne niezbędne zależności.

### npm

```
npm install ai @ai-sdk/google zod
npm install -D @types/node tsx typescript && npx tsc --init
```

Aby uniknąć błędu kompilatora TypeScript, dodaj komentarz do tego wiersza w wygenerowanym pliku `tsconfig.json`:

```
//"verbatimModuleSyntax": true,
```

### pnpm

```
pnpm add ai @ai-sdk/google zod
pnpm add -D @types/node tsx typescript
```

### włóczka

```
yarn add ai @ai-sdk/google zod
yarn add -D @types/node tsx typescript && yarn tsc --init
```

Aby uniknąć błędu kompilatora TypeScript, dodaj komentarz do tego wiersza w wygenerowanym pliku `tsconfig.json`:

```
//"verbatimModuleSyntax": true,
```

Ta aplikacja będzie też używać pakietów innych firm [Puppeteer](https://pptr.dev/) i [Chart.js](https://www.chartjs.org) do renderowania wykresów i tworzenia plików PDF:

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

### włóczka

```
yarn add puppeteer chart.js
yarn add -D @types/chart.js
```

Pakiet `puppeteer` wymaga uruchomienia skryptu, aby pobrać przeglądarkę Chromium. Menedżer pakietów może poprosić o zatwierdzenie, więc gdy pojawi się odpowiedni komunikat, zatwierdź skrypt.

### Konfigurowanie klucza interfejsu API

Ustaw zmienną środowiskową `GOOGLE_GENERATIVE_AI_API_KEY` za pomocą klucza interfejsu Gemini API. Dostawca generatywnej AI od Google automatycznie wyszukuje klucz interfejsu API w tej zmiennej środowiskowej.

### macOS/Linux

```
export GOOGLE_GENERATIVE_AI_API_KEY="YOUR_API_KEY_HERE"
```

### Powershell

```
setx GOOGLE_GENERATIVE_AI_API_KEY "YOUR_API_KEY_HERE"
```

## Tworzenie aplikacji

Teraz utwórzmy główny plik aplikacji. Utwórz w katalogu projektu nowy plik o nazwie `main.ts`. Logikę tego pliku będziesz tworzyć krok po kroku.

Aby szybko sprawdzić, czy wszystko jest prawidłowo skonfigurowane, dodaj ten kod do pliku `main.ts`. W tym podstawowym przykładzie użyto znacznika `generateText`, aby uzyskać prostą odpowiedź od Gemini.

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

Zanim dodasz więcej złożoności, uruchom ten skrypt, aby sprawdzić, czy środowisko jest prawidłowo skonfigurowane. Uruchom w terminalu to polecenie:

### npm

```
npx tsc && node main.js
```

### pnpm

```
pnpm tsx main.ts
```

### włóczka

```
yarn tsc && node main.js
```

Jeśli wszystko jest prawidłowo skonfigurowane, w konsoli zobaczysz odpowiedź Gemini.

## Przeprowadzanie badań rynku za pomocą wyszukiwarki Google

Aby uzyskać aktualne informacje, możesz włączyć w Gemini narzędzie [wyszukiwarka Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl). Gdy to narzędzie jest aktywne, model może przeszukiwać internet, aby odpowiedzieć na prompta, i zwracać użyte źródła.

Zastąp zawartość pliku `main.ts` poniższym kodem, aby wykonać pierwszy krok analizy.

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

## Wyodrębnianie danych z wykresu

Następnie przetworzymy tekst badawczy, aby wyodrębnić z niego uporządkowane dane odpowiednie do tworzenia wykresów. Użyj funkcji `generateObject` pakietu AI SDK wraz ze schematem `zod`, aby zdefiniować dokładną strukturę danych.

Utwórz też funkcję pomocniczą, która przekształci te uporządkowane dane w konfigurację zrozumiałą dla `Chart.js`.

Dodaj do pliku `main.ts` ten kod: Zwróć uwagę na nowe polecenia import i dodany „Krok 2”.

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

## Generowanie raportu końcowego

Na ostatnim etapie poproś Gemini o pełnienie roli eksperta w zakresie pisania raportów.
Podaj mu wyniki badań rynku, konfiguracje wykresów i jasne instrukcje dotyczące tworzenia raportu HTML. Następnie użyj [Puppeteer](https://pptr.dev/), aby wyrenderować ten kod HTML i zapisać go jako plik PDF.

Dodaj do pliku `main.ts` ostatnią instrukcję importu i „Krok 3”.`puppeteer`

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

## Uruchamianie aplikacji

Możesz teraz uruchomić aplikację. Uruchom w terminalu to polecenie:

### npm

```
npx tsc && node main.js
```

### pnpm

```
pnpm tsx main.ts
```

### włóczka

```
yarn tsc && node main.js
```

W terminalu zobaczysz logowanie podczas wykonywania każdego kroku skryptu.
Po zakończeniu w katalogu projektu zostanie utworzony plik `report.pdf` zawierający analizę rynku.

Poniżej znajdziesz pierwsze 2 strony przykładowego raportu w formacie PDF:

![Raport analizy rynku](https://ai.google.dev/static/gemini-api/docs/images/market-research-pdf.jpg?hl=pl)

## Dodatkowe zasoby

Więcej informacji o tworzeniu aplikacji z użyciem Gemini i pakietu AI SDK znajdziesz w tych materiałach:

- [Dokumentacja pakietu AI SDK](https://ai-sdk.dev/docs)
- [Dokumentacja pakietu SDK Google Generative AI](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai)
- [Przewodnik po pakiecie AI SDK: pierwsze kroki z Gemini](https://ai-sdk.dev/cookbook/guides/gemini)

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-19 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-19 UTC."],[],[]]
