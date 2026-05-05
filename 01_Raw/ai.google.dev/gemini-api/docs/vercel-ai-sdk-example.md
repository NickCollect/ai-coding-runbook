---
source_url: https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=pt-BR
fetched_at: 2026-05-05T19:51:43.666492+00:00
title: "Agente de pesquisa de mercado com o Gemini e o SDK de IA da Vercel \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Agente de pesquisa de mercado com o Gemini e o SDK de IA da Vercel

O [SDK de IA da Vercel](https://ai-sdk.dev) (em inglês) é uma biblioteca de código aberto avançada para
criar aplicativos, interfaces de usuário e agentes com tecnologia de IA em TypeScript.

Este guia vai orientar você na criação de um aplicativo Node.js com TypeScript
que usa o SDK de IA para se conectar à API Gemini pelo [provedor de IA generativa do Google](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai) e realizar análises automatizadas de tendências de mercado. O aplicativo final vai:

1. Use o Gemini com a Pesquisa Google para pesquisar as tendências atuais do mercado.
2. Extrair dados estruturados da pesquisa para gerar gráficos.
3. Combine a pesquisa e os gráficos em um relatório HTML profissional e salve como PDF.

## Pré-requisitos

Para concluir este guia, você vai precisar do seguinte:

- Uma chave da API Gemini. Você pode criar uma sem custo financeiro no [Google AI Studio](https://aistudio.google.com/apikey?hl=pt-br).
- [Node.js](https://nodejs.org/en/download) versão 18 ou mais recente.
- Um gerenciador de pacotes, como `npm`, `pnpm` ou `yarn`.

## Configurar o aplicativo

Primeiro, crie um diretório para seu projeto e inicialize-o.

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

### novelo

```
mkdir market-trend-app
cd market-trend-app
yarn init -y
```

### Instalar dependências

Em seguida, instale o SDK de IA, o provedor de IA generativa do Google e outras
dependências necessárias.

### npm

```
npm install ai @ai-sdk/google zod
npm install -D @types/node tsx typescript && npx tsc --init
```

Para evitar um erro do compilador TypeScript, coloque a seguinte linha em comentário no
`tsconfig.json` gerado:

```
//"verbatimModuleSyntax": true,
```

### pnpm

```
pnpm add ai @ai-sdk/google zod
pnpm add -D @types/node tsx typescript
```

### novelo

```
yarn add ai @ai-sdk/google zod
yarn add -D @types/node tsx typescript && yarn tsc --init
```

Para evitar um erro do compilador TypeScript, coloque a seguinte linha em comentário no
`tsconfig.json` gerado:

```
//"verbatimModuleSyntax": true,
```

Esse aplicativo também vai usar os pacotes de terceiros [Puppeteer](https://pptr.dev/) e [Chart.js](https://www.chartjs.org) para renderizar gráficos e criar um PDF:

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

### novelo

```
yarn add puppeteer chart.js
yarn add -D @types/chart.js
```

O pacote `puppeteer` exige a execução de um script para baixar o navegador
Chromium. O gerenciador de pacotes pode pedir aprovação. Portanto, aprove o script quando solicitado.

### Configurar a chave de API

Defina a variável de ambiente `GOOGLE_GENERATIVE_AI_API_KEY` com sua chave de API Gemini. O provedor de IA generativa do Google procura automaticamente sua chave de API nessa variável de ambiente.

### MacOS/Linux

```
export GOOGLE_GENERATIVE_AI_API_KEY="YOUR_API_KEY_HERE"
```

### Powershell

```
setx GOOGLE_GENERATIVE_AI_API_KEY "YOUR_API_KEY_HERE"
```

## Criar o aplicativo

Agora, vamos criar o arquivo principal do nosso aplicativo. Crie um arquivo chamado
`main.ts` no diretório do projeto. Você vai criar a lógica neste arquivo
etapa por etapa.

Para um teste rápido e garantir que tudo esteja configurado corretamente, adicione o seguinte
código a `main.ts`. Este exemplo básico usa `generateText` para receber uma resposta simples do Gemini.

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

Antes de adicionar mais complexidade, execute este script para verificar se o ambiente
está configurado corretamente. Execute o comando a seguir no terminal.

### npm

```
npx tsc && node main.js
```

### pnpm

```
pnpm tsx main.ts
```

### novelo

```
yarn tsc && node main.js
```

Se tudo estiver configurado corretamente, a resposta do Gemini vai aparecer no console.

## Fazer pesquisas de mercado com a Pesquisa Google

Para receber informações atualizadas, ative a ferramenta [Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br) no Gemini. Quando essa ferramenta está ativa, o modelo pode pesquisar na Web para responder ao comando e retorna as fontes usadas.

Substitua o conteúdo de `main.ts` pelo código a seguir para realizar a primeira etapa da nossa análise.

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

## Extrair dados do gráfico

Em seguida, vamos processar o texto da pesquisa para extrair dados estruturados adequados para gráficos. Use a função `generateObject` do SDK de IA com um esquema `zod`
para definir a estrutura de dados exata.

Crie também uma função auxiliar para converter esses dados estruturados em uma configuração que o `Chart.js` possa entender.

Adicione o seguinte código a `main.ts`: Observe as novas importações e a adição da "Etapa 2".

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

## Gerar o relatório final

Na etapa final, instrua o Gemini a agir como um especialista em redação de relatórios.
Forneça a pesquisa de mercado, as configurações de gráfico e um conjunto claro de instruções para criar um relatório em HTML. Em seguida, use o
[Puppeteer](https://pptr.dev/) para renderizar esse HTML e salvá-lo como um PDF.

Adicione a importação final de `puppeteer` e "Etapa 3" ao arquivo `main.ts`.

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

## Execute o aplicativo

Agora você já pode executar o aplicativo. Execute o seguinte comando no
terminal:

### npm

```
npx tsc && node main.js
```

### pnpm

```
pnpm tsx main.ts
```

### novelo

```
yarn tsc && node main.js
```

Você verá o registro no terminal à medida que o script executa cada etapa.
Quando concluído, um arquivo `report.pdf` com sua análise de mercado será criado no diretório do projeto.

Confira abaixo as duas primeiras páginas de um exemplo de relatório em PDF:

![Relatório de análise de mercado](https://ai.google.dev/static/gemini-api/docs/images/market-research-pdf.jpg?hl=pt-br)

## Outros recursos

Para mais informações sobre como criar com o Gemini e o SDK de IA,
confira estes recursos:

- [Documentos do SDK de IA](https://ai-sdk.dev/docs)
- [Documentação da IA generativa do Google do SDK de IA](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai)
- [Livro de receitas do SDK de IA: comece a usar o Gemini](https://ai-sdk.dev/cookbook/guides/gemini)

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-04-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-04-29 UTC."],[],[]]
