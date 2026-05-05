---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=pt-BR
fetched_at: 2026-05-05T19:45:48.655911+00:00
title: "API Gemini Developer x plataforma de agentes do Gemini Enterprise \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# API Gemini Developer x plataforma de agentes do Gemini Enterprise

Ao desenvolver soluções de IA generativa com o Gemini, o Google oferece dois produtos de API:
a [API Gemini Developer](https://ai.google.dev/gemini-api/docs?hl=pt-br) e a [API da plataforma de agentes do Gemini Enterprise](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=pt-br).

A API Gemini Developer oferece o caminho mais rápido para criar, produzir e escalonar aplicativos com tecnologia Gemini. A maioria dos desenvolvedores deve usar a API Gemini Developer, a menos que haja necessidade de controles empresariais específicos.

A plataforma de agentes do Gemini Enterprise oferece um ecossistema abrangente de recursos e serviços prontos para empresas para criar e implantar aplicativos de IA generativa com o suporte do Google Cloud Platform.

Simplificamos recentemente a migração entre esses serviços. Agora, a API Gemini Developer e a API da plataforma de agentes do Gemini Enterprise podem ser acessadas pelo [SDK de IA Generativa do Google](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br) unificado.

## Comparação de código

Esta página tem comparações de código lado a lado entre os guias de início rápido da API Gemini Developer e da plataforma de agentes do Gemini Enterprise para geração de texto.

### Python

É possível acessar a API Gemini Developer e os serviços da plataforma de agentes do Gemini Enterprise pela biblioteca `google-genai`. Consulte a página de [bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br)
para instruções sobre como instalar `google-genai`.

### API Gemini Developer

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### API da plataforma de agentes do Gemini Enterprise

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript e TypeScript

É possível acessar a API Gemini Developer e os serviços da plataforma de agentes do Gemini Enterprise pela biblioteca `@google/genai`. Consulte a página de [bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br) para instruções sobre como
instalar `@google/genai`.

### API Gemini Developer

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### API da plataforma de agentes do Gemini Enterprise

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

É possível acessar a API Gemini Developer e os serviços da plataforma de agentes do Gemini Enterprise pela biblioteca `google.golang.org/genai`. Consulte a página de [bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br) para instruções sobre como
instalar `google.golang.org/genai`.

### API Gemini Developer

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", genai.Text("Tell me about New York?"), nil)

}
```

### API da plataforma de agentes do Gemini Enterprise

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", genai.Text("Tell me about New York?"), nil)

}
```

### Outros casos de uso e plataformas

Consulte os guias específicos de casos de uso na [documentação da API Gemini Developer](https://ai.google.dev/gemini-api/docs?hl=pt-br)
e na [documentação da plataforma de agentes do Gemini Enterprise](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=pt-br)
para outras plataformas e casos de uso.

## Considerações sobre a migração

Ao migrar:

- Você precisará usar contas de serviço do Google Cloud para autenticar. Consulte a [documentação da plataforma de agentes do Gemini Enterprise](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=pt-br)
  para mais informações.
- É possível usar seu projeto atual do Google Cloud
  (o mesmo usado para gerar a chave de API) ou
  [criar um novo projeto do Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=pt-br).
- As regiões com suporte podem ser diferentes entre a API Gemini Developer e a API da plataforma de agentes do Gemini Enterprise. Veja a lista de
  [regiões compatíveis com IA generativa no Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=pt-br).
- Todos os modelos criados no Google AI Studio precisam ser treinados novamente na plataforma de agentes do Gemini Enterprise.

Se você não precisar mais usar sua chave da API Gemini para a API Gemini Developer, siga as práticas recomendadas de segurança e exclua a chave.

Para excluir uma chave de API:

1. Abra a
   [página Credenciais da API Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pt-br).
2. Encontre a chave de API que você quer excluir e clique no ícone **Ações**.
3. Selecione **Excluir chave de API**.
4. No modal **Excluir credencial**, selecione **Excluir**.

   A remoção de uma chave de API leva alguns minutos para ser propagada. Após o término da propagação, todo tráfego que usar a chave de API excluída será recusado.

## Próximas etapas

- Consulte a
  [visão geral da IA generativa na plataforma de agentes do Gemini Enterprise](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/multimodal/overview?hl=pt-br)
  para saber mais sobre as soluções de IA generativa na plataforma de agentes do Gemini Enterprise.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-04-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-04-29 UTC."],[],[]]
