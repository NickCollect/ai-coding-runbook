---
source_url: https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=es-419
fetched_at: 2026-08-03T04:33:59.787286+00:00
title: "Agente de investigaci\u00f3n de mercado con Gemini y el SDK de IA de Vercel \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Agente de investigación de mercado con Gemini y el SDK de IA de Vercel

El [SDK de IA de Vercel](https://ai-sdk.dev) es una potente biblioteca de código abierto para compilar aplicaciones, interfaces de usuario y agentes potenciados por IA en TypeScript.

En esta guía, se explica cómo compilar una aplicación de Node.js con TypeScript que usa el SDK de IA para conectarse con la API de Gemini a través del [proveedor de IA generativa de Google](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai) y realizar análisis automatizados de tendencias del mercado. La aplicación final hará lo siguiente:

1. Usa Gemini con la Búsqueda de Google para investigar las tendencias actuales del mercado.
2. Extrae datos estructurados de la investigación para generar gráficos.
3. Combina la investigación y los gráficos en un informe HTML profesional y guárdalo como PDF.

## Requisitos previos

Para completar esta guía, necesitarás lo siguiente:

- Una clave de API de Gemini Puedes crear una gratis en [Google AI Studio](https://aistudio.google.com/apikey?hl=es-419).
- [Node.js](https://nodejs.org/en/download) versión 18 o posterior
- Un administrador de paquetes, como `npm`, `pnpm` o `yarn`

## Cómo configurar tu aplicación

Primero, crea un directorio nuevo para tu proyecto y, luego, inicialízalo.

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

### hilo

```
mkdir market-trend-app
cd market-trend-app
yarn init -y
```

### Instala dependencias

A continuación, instala el SDK de IA, el proveedor de IA generativa de Google y otras dependencias necesarias.

### npm

```
npm install ai @ai-sdk/google zod
npm install -D @types/node tsx typescript && npx tsc --init
```

Para evitar un error del compilador de TypeScript, comenta la siguiente línea en el archivo `tsconfig.json` generado:

```
//"verbatimModuleSyntax": true,
```

### pnpm

```
pnpm add ai @ai-sdk/google zod
pnpm add -D @types/node tsx typescript
```

### hilo

```
yarn add ai @ai-sdk/google zod
yarn add -D @types/node tsx typescript && yarn tsc --init
```

Para evitar un error del compilador de TypeScript, comenta la siguiente línea en el archivo `tsconfig.json` generado:

```
//"verbatimModuleSyntax": true,
```

Esta aplicación también usará los paquetes de terceros [Puppeteer](https://pptr.dev/) y [Chart.js](https://www.chartjs.org) para renderizar gráficos y crear un PDF:

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

### hilo

```
yarn add puppeteer chart.js
yarn add -D @types/chart.js
```

El paquete `puppeteer` requiere que se ejecute una secuencia de comandos para descargar el navegador Chromium. Es posible que el administrador de paquetes te solicite aprobación, así que asegúrate de aprobar el script cuando se te solicite.

### Configura tu clave de API

Establece la variable de entorno `GOOGLE_GENERATIVE_AI_API_KEY` con tu clave de la API de Gemini. El proveedor de IA generativa de Google busca automáticamente tu clave de API en esta variable de entorno.

### macOS/Linux

```
export GOOGLE_GENERATIVE_AI_API_KEY="YOUR_API_KEY_HERE"
```

### PowerShell

```
setx GOOGLE_GENERATIVE_AI_API_KEY "YOUR_API_KEY_HERE"
```

## Crea tu aplicación

Ahora, creemos el archivo principal de nuestra aplicación. Crea un archivo nuevo llamado `main.ts` en el directorio de tu proyecto. Compilarás la lógica en este archivo paso a paso.

Para realizar una prueba rápida y asegurarte de que todo esté configurado correctamente, agrega el siguiente código a `main.ts`. En este ejemplo básico, se usa `generateText` para obtener una respuesta simple de Gemini.

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

Antes de agregar más complejidad, ejecuta esta secuencia de comandos para verificar que tu entorno esté configurado correctamente. Ejecuta el siguiente comando en la terminal:

### npm

```
npx tsc && node main.js
```

### pnpm

```
pnpm tsx main.ts
```

### hilo

```
yarn tsc && node main.js
```

Si todo está configurado correctamente, verás la respuesta de Gemini impresa en la consola.

## Realiza una investigación de mercado con la Búsqueda de Google

Para obtener información actualizada, puedes habilitar la herramienta [Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419) para Gemini. Cuando esta herramienta está activa, el modelo puede buscar en la Web para responder la instrucción y mostrará las fuentes que usó.

Reemplaza el contenido de `main.ts` con el siguiente código para realizar el primer paso de nuestro análisis.

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

## Cómo extraer datos de gráficos

A continuación, procesaremos el texto de investigación para extraer datos estructurados adecuados para los gráficos. Usa la función `generateObject` del SDK de IA junto con un esquema `zod` para definir la estructura de datos exacta.

También crea una función auxiliar para convertir estos datos estructurados en una configuración que `Chart.js` pueda comprender.

Agrega el siguiente código a `main.ts`. Observa las nuevas importaciones y el "Paso 2" agregado.

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

## Genera el informe final

En el último paso, indícale a Gemini que actúe como un redactor experto de informes.
Proporcionarle la investigación de mercado, las configuraciones de los gráficos y un conjunto claro de instrucciones para crear un informe HTML Luego, usa [Puppeteer](https://pptr.dev/) para renderizar este HTML y guardarlo como PDF.

Agrega la importación final de `puppeteer` y "Paso 3" a tu archivo `main.ts`.

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

## Ejecuta tu aplicación

Ya puedes ejecutar la aplicación. Ejecuta el siguiente comando en tu terminal:

### npm

```
npx tsc && node main.js
```

### pnpm

```
pnpm tsx main.ts
```

### hilo

```
yarn tsc && node main.js
```

Verás el registro en tu terminal a medida que la secuencia de comandos ejecute cada paso.
Cuando se complete, se creará un archivo `report.pdf` que contendrá tu análisis de mercado en el directorio del proyecto.

A continuación, verás las dos primeras páginas de un informe en PDF de ejemplo:

![Informe de análisis de mercado](https://ai.google.dev/static/gemini-api/docs/images/market-research-pdf.jpg?hl=es-419)

## Más recursos

Para obtener más información sobre cómo compilar con Gemini y el SDK de IA, explora estos recursos:

- [Documentos del SDK de IA](https://ai-sdk.dev/docs)
- [Documentos sobre la IA generativa de Google del SDK de IA](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai)
- [Recetario del SDK de IA: Comienza a usar Gemini](https://ai-sdk.dev/cookbook/guides/gemini)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-19 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-19 (UTC)"],[],[]]
