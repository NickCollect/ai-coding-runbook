---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/flex-inference?hl=pt-BR
fetched_at: 2026-10-05T06:43:58.724680+00:00
title: "Infer\u00eancia flex\u00edvel \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=pt-br)

Envie comentários

# Inferência flexível

Descrição: saiba como otimizar custos com o nível de inferência Flex

A API Gemini Flex é um nível de inferência que oferece uma redução de custo de 50% em comparação com as taxas padrão, em troca de latência variável e disponibilidade de melhor esforço. Ela foi projetada para cargas de trabalho tolerantes à latência que exigem processamento síncrono, mas não precisam da performance em tempo real da API padrão.

## Como usar o Flex

Para usar o nível Flex, especifique `service_tier` como `flex` no corpo da solicitação. Por padrão, as solicitações usam o nível padrão se esse campo for omitido.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Analyze this dataset for trends...",
        config={"service_tier": "flex"},
    )
    print(response.text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
    const response = await ai.models.generateContent({
      model: "gemini-3.6-flash",
      contents: "Analyze this dataset for trends...",
      config: { serviceTier: "flex" },
    });
    console.log(response.text);
  } catch (e) {
    console.log(`Flex request failed: ${e}`);
  }
}

await main();
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        genai.Text("Analyze this dataset for trends..."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        log.Printf("Flex request failed: %v", err)
        return
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Summarize the latest research on quantum computing."}]
  }],
  "service_tier": "flex"
}'
```

## Como a inferência Flex funciona

A inferência Gemini Flex preenche a lacuna entre a API padrão e o tempo de resposta de 24 horas
da [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br). Ela usa capacidade de computação fora do horário de pico e "descartável" para fornecer uma solução econômica para tarefas em segundo plano e fluxos de trabalho sequenciais.

| Recurso | Flex | Prioridade | Padrão | Lote |
| --- | --- | --- | --- | --- |
| **Preços** | 50% de desconto | 75 a 100% a mais que o padrão | Preço total | 50% de desconto |
| **Latência** | Minutos (1 a 15 min de destino) | Baixa (segundos) | Segundos a minutos | Até 24 horas |
| **Confiabilidade** | Melhor esforço (descartável) | Alta (não descartável) | Alta / média-alta | Alta (para capacidade de processamento) |
| **Interface** | Síncrona | Síncrona | Síncrona | Assíncrona |

### Principais benefícios

- **Eficiência de custo**: economia substancial para avaliações de não produção, agentes em segundo plano e aprimoramento de dados.
- **Baixa fricção**: não é necessário gerenciar objetos em lote, IDs de jobs ou pesquisas. Basta adicionar um único parâmetro às solicitações atuais.
- **Fluxos de trabalho síncronos**: ideal para cadeias de API sequenciais em que a próxima solicitação depende da saída da anterior, tornando-a mais flexível do que o lote para fluxos de trabalho de agentes.

### Casos de uso

- **Avaliações off-line**: execução de testes de regressão ou placares de líderes "LLM como juiz".
- **Agentes em segundo plano**: tarefas sequenciais, como atualizações de CRM, criação de perfis ou moderação de conteúdo, em que minutos de atraso são aceitáveis.
- **Pesquisa limitada pelo orçamento**: experimentos acadêmicos que exigem alto volume de tokens em um orçamento limitado.

### Limites de taxas

O tráfego de inferência Flex é contabilizado nos limites de [taxa](https://aistudio.google.com/rate-limit?hl=pt-br) gerais. Ele não
oferece limites de taxa estendidos, como a [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br).

### Capacidade descartável

O tráfego Flex é tratado com menor prioridade. Se houver um pico no tráfego padrão, as solicitações Flex poderão ser interrompidas ou removidas para garantir a capacidade de usuários de alta prioridade. Se você estiver procurando inferência de alta prioridade, confira
[Inferência de prioridade](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pt-br)

### Códigos de erro

Quando a capacidade do Flex não estiver disponível ou o sistema estiver congestionado, a API vai retornar códigos de erro padrão:

- **503 Service Unavailable**: o sistema está na capacidade máxima.
- **429 Too Many Requests**: limites de taxa ou esgotamento de recursos.

### Responsabilidade do cliente

- **Nenhum fallback do lado do servidor**: para evitar cobranças inesperadas, o sistema não vai
  fazer upgrade automático de uma solicitação Flex para o nível padrão se a capacidade do Flex estiver
  cheia.
- **Novas tentativas**: é necessário implementar sua própria lógica de nova tentativa do lado do cliente com
  espera exponencial.
- **Tempos limite**: como as solicitações Flex podem ficar em uma fila, recomendamos
  aumentar os tempos limite do lado do cliente para 10 minutos ou mais para evitar o fechamento prematuro
  da conexão.

## Ajustar janelas de tempo limite

É possível configurar tempos limite por solicitação para a API REST e bibliotecas de cliente, e tempos limite globais apenas ao usar as bibliotecas de cliente.

Sempre verifique se o tempo limite do lado do cliente abrange a janela de paciência do servidor pretendida (por exemplo, 600 segundos ou mais para filas de espera Flex). Os SDKs esperam valores de tempo limite em milissegundos.

### Tempos limite por solicitação

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="why is the sky blue?",
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 900000}
        },
    )
except Exception as e:
    print(f"Flex request failed: {e}")

# Example with streaming
try:
    response = client.models.generate_content_stream(
        model="gemini-3.6-flash",
        contents=["List 5 ideas for a sci-fi movie."],
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 60000}
        }
        # Per-request timeout for the streaming operation
    )
    for chunk in response:
        print(chunk.text, end="")

except Exception as e:
    print(f"An error occurred during streaming: {e}")
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const client = new GoogleGenAI({});

 async function main() {
     try {
         const response = await client.models.generateContent({
             model: "gemini-3.6-flash",
             contents: "why is the sky blue?",
             config: {
               serviceTier: "flex",
               httpOptions: {timeout: 900000}
             },
         });
     } catch (e) {
         console.log(`Flex request failed: ${e}`);
     }

     // Example with streaming
     try {
         const response = await client.models.generateContentStream({
             model: "gemini-3.6-flash",
             contents: ["List 5 ideas for a sci-fi movie."],
             config: {
                 serviceTier: "flex",
                 httpOptions: {timeout: 60000}
             },
         });
         for await (const chunk of response.stream) {
             process.stdout.write(chunk.text());
         }
     } catch (e) {
         console.log(`An error occurred during streaming: ${e}`);
     }
 }

 await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "google.golang.org/api/iterator"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    timeoutCtx, cancel := context.WithTimeout(ctx, 900*time.Second)
    defer cancel()

    _, err = client.Models.GenerateContent(
        timeoutCtx,
        "gemini-3.6-flash",
        genai.Text("why is the sky blue?"),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        fmt.Printf("Flex request failed: %v\n", err)
    }

    // Example with streaming
    streamTimeoutCtx, streamCancel := context.WithTimeout(ctx, 60*time.Second)
    defer streamCancel()

    iter := client.Models.GenerateContentStream(
        streamTimeoutCtx,
        "gemini-3.6-flash",
        genai.Text("List 5 ideas for a sci-fi movie."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    for {
        response, err := iter.Next()
        if err == iterator.Done {
            break
        }
        if err != nil {
            fmt.Printf("An error occurred during streaming: %v\n", err)
            break
        }
        fmt.Print(response.Candidates[0].Content.Parts[0])
    }
}
```

### REST

Ao fazer chamadas REST, é possível controlar os tempos limite usando uma combinação de cabeçalhos HTTP e opções `curl`:

- **Cabeçalho `X-Server-Timeout` (tempo limite do lado do servidor)**: esse cabeçalho sugere uma duração de tempo limite preferencial (padrão de 600 segundos) para o servidor da API Gemini. O servidor vai tentar respeitar isso, mas não é garantido. O valor precisa estar em segundos.
- **`--max-time` em `curl` (tempo limite do lado do cliente)**: a opção `curl --max-time
  <seconds>` define um limite rígido para o tempo total (em segundos) que `curl`
  vai esperar para que toda a operação seja concluída. Essa é uma proteção do lado do cliente.

```
 # Set a server timeout hint of 120 seconds and a client-side curl timeout of 125 seconds.
 curl --max-time 125 \
   -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "X-Server-Timeout: 120" \
   -d '{
   "contents": [{
     "parts":[{"text": "Summarize the latest research on quantum computing."}]
   }],
   "service_tier": "flex"
 }'
```

### Tempos limite globais

Se você quiser que todas as chamadas de API feitas por uma instância `genai.Client` específica (somente bibliotecas de cliente) tenham um tempo limite padrão, configure isso ao inicializar o cliente usando `http_options` e `genai.types.HttpOptions`.

### Python

```
from google import genai
from google.genai import types

global_timeout_ms = 120000

client_with_global_timeout = genai.Client(
    http_options=types.HttpOptions(timeout=global_timeout_ms)
)

try:
    # Calling generate_content using global timeout...
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.6-flash",
        contents="Summarize the history of AI development since 2000.",
        config={"service_tier": "flex"},
    )
    print(response.text)

    # A per-request timeout will *override* the global timeout for that specific call.
    shorter_timeout = 30000
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.6-flash",
        contents="Provide a very brief definition of machine learning.",
        config={
            "service_tier": "flex",
            "http_options":{"timeout": shorter_timeout}
        }  # Overrides the global timeout
    )

    print(response.text)

except TimeoutError:
    print(
        f"A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
    )
except Exception as e:
    print(f"An error occurred: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const globalTimeoutMs = 120000;

const clientWithGlobalTimeout = new GoogleGenAI({httpOptions: {timeout: globalTimeoutMs}});

async function main() {
    try {
        // Calling generate_content using global timeout...
        const response1 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.6-flash",
            contents: "Summarize the history of AI development since 2000.",
            config: { serviceTier: "flex" },
        });
        console.log(response1.text());

        // A per-request timeout will *override* the global timeout for that specific call.
        const shorterTimeout = 30000;
        const response2 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.6-flash",
            contents: "Provide a very brief definition of machine learning.",
            config: {
                serviceTier: "flex",
                httpOptions: {timeout: shorterTimeout}
            }  // Overrides the global timeout
        });

        console.log(response2.text());

    } catch (e) {
        if (e.name === 'TimeoutError' || e.message?.includes('timeout')) {
            console.log(
                "A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
            );
        } else {
            console.log(`An error occurred: ${e}`);
        }
    }
}

await main();
```

### Go

```
 package main

 import (
     "context"
     "fmt"
     "log"
     "time"

     "google.golang.org/genai"
 )

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     model := client.GenerativeModel("gemini-3.6-flash")

     // Go uses context for timeouts, not client options.
     // Set a default timeout for requests.
     globalTimeout := 120 * time.Second
     fmt.Printf("Using default timeout of %v seconds.\n", globalTimeout.Seconds())

     fmt.Println("Calling generate_content (using default timeout)...")
     ctx1, cancel1 := context.WithTimeout(ctx, globalTimeout)
     defer cancel1()
     resp1, err := model.GenerateContent(ctx1, genai.Text("Summarize the history of AI development since 2000."), &genai.GenerateContentConfig{ServiceTier: "flex"})
     if err != nil {
         log.Printf("Request 1 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 1 successful.")
         fmt.Println(resp1.Text())
     }

     // A different timeout can be used for other requests.
     shorterTimeout := 30 * time.Second
     fmt.Printf("\nCalling generate_content with a shorter timeout of %v seconds...\n", shorterTimeout.Seconds())
     ctx2, cancel2 := context.WithTimeout(ctx, shorterTimeout)
     defer cancel2()
     resp2, err := model.GenerateContent(ctx2, genai.Text("Provide a very brief definition of machine learning."), &genai.GenerateContentConfig{
         ServiceTier: "flex",
     })
     if err != nil {
         log.Printf("Request 2 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 2 successful.")
         fmt.Println(resp2.Text())
     }
 }
```

## Implementar novas tentativas

Como o Flex é descartável e falha com erros 503, confira um exemplo de implementação opcional da lógica de nova tentativa para continuar com solicitações com falha:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.models.generate_content(
                model="gemini-3.6-flash",
                contents="Analyze this batch statement.",
                config={"service_tier": "flex"},
            )
        except Exception as e:
            # Check for 503 Service Unavailable or 429 Rate Limits
            print(e.code)
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                # Fallback to standard on last strike (Optional)
                print("Flex exhausted, falling back to Standard...")
                return client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents="Analyze this batch statement."
                )

# Usage
response = call_with_retry()
print(response.text)
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const ai = new GoogleGenAI({});

 async function sleep(ms) {
   return new Promise(resolve => setTimeout(resolve, ms));
 }

 async function callWithRetry(maxRetries = 3, baseDelay = 5) {
   for (let attempt = 0; attempt < maxRetries; attempt++) {
     try {
       console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
       const response = await ai.models.generateContent({
         model: "gemini-3.6-flash",
         contents: "Analyze this batch statement.",
         config: { serviceTier: 'flex' },
       });
       return response;
     } catch (e) {
       if (attempt < maxRetries - 1) {
         const delay = baseDelay * (2 ** attempt);
         console.log(`Flex busy, retrying in ${delay}s...`);
         await sleep(delay * 1000);
       } else {
         console.log("Flex exhausted, falling back to Standard...");
         return await ai.models.generateContent({
           model: "gemini-3.6-flash",
           contents: "Analyze this batch statement.",
         });
       }
     }
   }
 }

 async function main() {
     const response = await callWithRetry();
     console.log(response.text);
 }

 await main();
```

### Go

```
 package main

 import (
     "context"
     "fmt"
     "log"
     "math"
     "time"

     "google.golang.org/genai"
 )

 func callWithRetry(ctx context.Context, client *genai.Client, maxRetries int, baseDelay time.Duration) (*genai.GenerateContentResponse, error) {
     modelName := "gemini-3.6-flash"
     content := genai.Text("Analyze this batch statement.")
     flexConfig := &genai.GenerateContentConfig{
         ServiceTier: "flex",
     }

     for attempt := 0; attempt < maxRetries; attempt++ {
         log.Printf("Attempt %d: Calling Flex tier...", attempt+1)
         resp, err := client.Models.GenerateContent(ctx, modelName, content, flexConfig)
         if err == nil {
             return resp, nil
         }

         log.Printf("Attempt %d failed: %v", attempt+1, err)

         if attempt < maxRetries-1 {
             delay := time.Duration(float64(baseDelay) * math.Pow(2, float64(attempt)))
             log.Printf("Flex busy, retrying in %v...", delay)
             time.Sleep(delay)
         } else {
             log.Println("Flex exhausted, falling back to Standard...")
             return client.Models.GenerateContent(ctx, modelName, content)
         }
     }
     return nil, fmt.Errorf("retries exhausted") // Should not be reached
 }

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     resp, err := callWithRetry(ctx, client, 3, 5*time.Second)
     if err != nil {
         log.Fatalf("Failed after retries: %v", err)
     }
     fmt.Println(resp.Text())
 }
```

## Preços

A inferência Flex tem preço de 50% da [API padrão](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br)
e é faturada por token.

## Modelos compatíveis

Os seguintes modelos oferecem suporte à inferência Flex:

| Modelo | inferência Flex |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=pt-br) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=pt-br) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=pt-br) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pt-br) | ✔️ |
| [Pré-lançamento de imagens do Gemini 3 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=pt-br) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pt-br) | ✔️ |
| [Criação de imagens do Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pt-br) | ✔️ |

## A seguir

Leia sobre outras opções de [inferência e otimização](https://ai.google.dev/gemini-api/docs/optimization?hl=pt-br) do Gemini:

- [Inferência de prioridade](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pt-br) para latência ultrabaixa.
- [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br) para processamento assíncrono em até 24 horas.
- [Armazenamento em cache de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br) para reduzir os custos de token de entrada.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-12 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-12 UTC."],[],[]]
