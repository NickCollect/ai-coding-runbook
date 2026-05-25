---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=pt-BR
fetched_at: 2026-05-25T05:19:17.115968+00:00
title: "Como usar chaves da API Gemini \u00a0|\u00a0 Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Como usar chaves da API Gemini

Para usar a API Gemini, você precisa de uma chave de API. Nesta página, você vai aprender a criar e gerenciar chaves no Google AI Studio, além de configurar seu ambiente para usá-las no código.

[Criar ou visualizar uma chave da API Gemini](https://aistudio.google.com/app/apikey?hl=pt-br)

## Chaves de API

**Você pode criar e gerenciar todas as suas chaves de API Gemini na página [Chaves de API](https://aistudio.google.com/app/apikey?hl=pt-br)** do Google AI Studio.

Depois de ter uma chave de API, você tem as seguintes opções para se conectar à
API Gemini:

- [Definir sua chave de API como uma variável de ambiente](#set-api-env-var)
- [Fornecer sua chave de API explicitamente](#provide-api-key-explicitly)

Para testes iniciais, você pode codificar uma chave de API, mas isso só deve ser
temporário, já que não é seguro. Confira exemplos de codificação da chave de API na seção [Fornecer a chave de API explicitamente](#provide-api-key-explicitly).

## Projetos do Google Cloud

Os [projetos do Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=pt-br)
são fundamentais para usar os serviços do Google Cloud (como a API Gemini),
gerenciar o faturamento e controlar colaboradores e permissões. O Google AI Studio oferece uma interface leve para seus projetos do Google Cloud.

Se você ainda não tiver criado nenhum projeto, crie um ou importe um do Google Cloud para o Google AI Studio. A página **Projetos** no Google AI
Studio mostra todas as chaves com permissão suficiente para usar a API
Gemini. Consulte a seção [Importar projetos](#import-projects) para instruções.

### Projeto padrão

Para novos usuários, depois de aceitar os Termos de Serviço, o Google AI Studio cria um
projeto do Google Cloud e uma chave de API padrão para facilitar o uso. Para renomear esse projeto no Google AI Studio, acesse a visualização **Projetos** no **Painel**, clique no botão de configurações de três pontos ao lado de um projeto e escolha **Renomear projeto**. Os usuários atuais ou que já têm contas do Google Cloud não terão um projeto padrão criado.

## Importar projetos

Cada chave de API Gemini está associada a um projeto na nuvem do Google. Por padrão, o Google AI Studio não mostra todos os seus projetos do Cloud. Para importar os projetos desejados, pesquise o nome ou ID do projeto na caixa de diálogo **Importar projetos**. Para conferir uma lista completa dos projetos a que você tem acesso, acesse o console do Cloud.

Se você ainda não importou nenhum projeto na nuvem, siga estas etapas para importar um projeto do Google Cloud e criar uma chave:

1. Acesse o [Google AI Studio](https://aistudio.google.com?hl=pt-br).
2. Abra o **Painel** no painel lateral.
3. Selecione **Projetos**.
4. Selecione o botão **Importar projetos** na página **Projetos**.
5. Pesquise e selecione o projeto na nuvem do Google que você quer importar e clique no botão **Importar**.

Depois que um projeto for importado, acesse a página **Chaves de API** no menu **Painel** e crie uma chave de API no projeto que você acabou de importar.

## Limitações

Confira abaixo as limitações do gerenciamento de chaves de API e projetos do Google Cloud no
Google AI Studio.

- É possível criar no máximo 10 projetos por vez na página **Projetos** do Google AI Studio.
- É possível nomear e renomear projetos e chaves.
- As páginas **Chaves de API** e **Projetos** mostram um máximo de 100 chaves e 50 projetos.
- Somente as chaves de API sem restrições ou restritas à API
  Generative Language são mostradas.

Para ter mais acesso de gerenciamento aos seus projetos, incluindo a modificação e a restrição de chaves de API, acesse a [página de credenciais do console do Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pt-br).
No console do Cloud, selecione seu projeto, clique em uma chave de API e restrinja o acesso à **API Generative Language**.

## Definir a chave de API como uma variável de ambiente

Se você definir a variável de ambiente `GEMINI_API_KEY` ou `GOOGLE_API_KEY`, a chave de API será capturada automaticamente pelo cliente ao usar uma das [bibliotecas da API Gemini](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br). Recomendamos que você defina apenas uma dessas variáveis, mas, se as duas forem definidas, `GOOGLE_API_KEY` terá precedência.

Se você estiver usando a API REST ou JavaScript no navegador, será necessário
fornecer a chave de API explicitamente.

Veja como definir sua chave de API localmente como a variável de ambiente
`GEMINI_API_KEY` com diferentes sistemas operacionais.

### Linux/macOS: Bash

O Bash é uma configuração comum de terminal do Linux e do macOS. Para verificar se você tem um arquivo de configuração para ele, execute o seguinte comando:

```
~/.bashrc
```

Se a resposta for "No such file or directory", crie e abra o arquivo executando os seguintes comandos ou use `zsh`:

```
touch ~/.bashrc
open ~/.bashrc
```

Em seguida, defina sua chave de API adicionando o seguinte comando de exportação:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Depois de salvar o arquivo, aplique as mudanças executando:

```
source ~/.bashrc
```

### macOS: Zsh

O Zsh é uma configuração comum de terminal do Linux e do macOS. Para verificar se você tem um arquivo de configuração para ele, execute o seguinte comando:

```
~/.zshrc
```

Se a resposta for "No such file or directory", crie e abra o arquivo executando os seguintes comandos ou use `bash`:

```
touch ~/.zshrc
open ~/.zshrc
```

Em seguida, defina sua chave de API adicionando o seguinte comando de exportação:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Depois de salvar o arquivo, aplique as mudanças executando:

```
source ~/.zshrc
```

### Windows

1. Pesquise "Variáveis de ambiente" na barra de pesquisa.
2. Escolha modificar as **Configurações do sistema**. Talvez seja necessário confirmar que você quer fazer isso.
3. Na caixa de diálogo de configurações do sistema, clique no botão **Variáveis de ambiente**.
4. Em **Variáveis de usuário** (para o usuário atual) ou **Variáveis do sistema** (aplicável a todos os usuários que usam a máquina), clique em **Nova...**
5. Especifique o nome da variável como `GEMINI_API_KEY`. Especifique sua chave de API Gemini como o valor da variável.
6. Clique em **OK** para aplicar as mudanças.
7. Abra uma nova sessão de terminal (cmd ou PowerShell) para receber a nova variável.

## Fornecer a chave de API explicitamente

Em alguns casos, talvez seja necessário fornecer uma chave de API explicitamente. Exemplo:

- Você está fazendo uma chamada de API simples e prefere codificar a chave de API.
- Você quer controle explícito sem precisar depender da descoberta automática de
  variáveis de ambiente pelas bibliotecas da API Gemini.
- Você está usando um ambiente em que as variáveis de ambiente não são compatíveis (por exemplo, a Web) ou está fazendo chamadas REST.

Confira abaixo exemplos de como fornecer uma chave de API explicitamente:

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
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
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.5-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Mantenha sua chave de API segura

Trate sua chave da API Gemini como uma senha. Se ela for comprometida, outras pessoas poderão usar a cota do seu projeto, gerar cobranças (se o faturamento estiver ativado) e acessar seus dados particulares, como arquivos.

### Regras de segurança críticas

- **Mantenha as chaves confidenciais**: as chaves de API do Gemini podem acessar dados sensíveis de que seu aplicativo depende.

  - **Nunca confirme chaves de API no controle de origem.** Não faça check-in da chave de API em sistemas de controle de versões como o Git.
  - **Nunca exponha chaves de API no lado do cliente.** Não use sua chave de API diretamente em apps da Web ou para dispositivos móveis em produção. As chaves no código do lado do cliente (incluindo nossas bibliotecas JavaScript/TypeScript e chamadas REST) podem ser extraídas.
- **Restrinja o acesso**: limite o uso da chave de API a endereços IP, referenciadores HTTP ou apps para Android/iOS específicos, sempre que possível.
- **Restrinja o uso**: ative apenas as APIs necessárias para cada chave.
- **Faça auditorias regulares**: audite e alterne as chaves de API periodicamente.

### Práticas recomendadas

- **Use chamadas do lado do servidor com chaves de API**: a maneira mais segura de usar sua chave de API é chamar a API Gemini de um aplicativo do lado do servidor em que a chave pode ser mantida em sigilo.
- **Use tokens efêmeros para acesso do lado do cliente (somente API Live)**: para acesso direto do lado do cliente à API Live, use tokens efêmeros. Elas têm menos riscos de segurança e podem ser adequadas para uso em produção. Consulte o guia de
  [tokens efêmeros](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=pt-br) para mais
  informações.
- **Considere adicionar restrições à sua chave**:é possível limitar as permissões de uma chave
  adicionando [restrições de chave de API](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=pt-br#add-api-restrictions).
  Isso minimiza os possíveis danos se a chave vazar.

Para conferir algumas práticas recomendadas gerais, consulte este
[artigo de suporte](https://support.google.com/googleapi/answer/6310037?hl=pt-br).

## Proteger chaves de API irrestritas

As chaves de API sem restrições são vulneráveis a usuários mal-intencionados e uso não autorizado. A partir de 19 de junho de 2026, para melhorar a segurança, a API Gemini vai
descontinuar o suporte para chaves de tráfego sem restrições.

**Isso significa que suas solicitações da API Gemini vão falhar se você não fizer nada.**

Para continuar usando a API Gemini sem interrupções, proteja suas chaves de tráfego
adicionando restrições no
[AI Studio](https://aistudio.google.com/api-keys?hl=pt-br).

Em [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys?hl=pt-br), você
vai encontrar um banner para avisar quando as chaves de API não tiverem restrições. Você pode ver
quais chaves não têm restrições e o uso do serviço nos últimos 90 dias.

Para chaves sem restrições, escolha uma das seguintes opções:

- Use a chave apenas para a API Gemini.
- Use a chave para uso de APIs que não são do Gemini.

### Restringir a chave somente à API Gemini

Se quiser restringir a chave apenas à API Gemini, proteja-a no
[AI Studio](https://aistudio.google.com/api-keys?hl=pt-br) clicando no botão
**Restringir à API Gemini**.

### Restringir a chave para uso de APIs que não são do Gemini

Se você quiser restringir a chave para uso de APIs que não são do Gemini:

1. Acesse a
   [página de credenciais do console do Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pt-br).
2. Verifique se o projeto está selecionado corretamente.
3. Selecione uma chave de API.
4. Abra o menu suspenso **Restrições de API** e aplique restrições de serviço à chave de API.

Se quiser modificar chaves com restrições atuais ou recém-adicionadas, acesse
o
[Console do Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pt-br).

## Chaves bloqueadas

A partir de 7 de maio de 2026, a API Gemini vai bloquear chaves de API irrestritas
que estiverem inativas por um longo período. Esses usuários vão encontrar uma tag **Bloqueada** para a chave em [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys?hl=pt-br) e precisarão gerar uma nova chave ou usar uma chave restrita alternativa para continuar usando a API Gemini.

## Solução de problemas na criação de chaves de API

No Google AI Studio, o botão **Criar chave de API** pode aparecer indisponível, com a mensagem: *Você não tem permissão para criar uma chave neste projeto*.

Isso ocorre quando você não tem as permissões necessárias no projeto para gerar uma nova chave:

- **`resourcemanager.projects.get`**: permite que o AI Studio verifique a existência do projeto.
- **`apikeys.keys.create`**: permite a geração da própria chave de API.
- **`serviceusage.services.enable`**: necessário para garantir que a API Gemini esteja
  ativa no projeto.

Para corrigir suas permissões, peça ao administrador do projeto ou da organização (se o projeto pertencer a uma [organização](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access?hl=pt-br)) para conceder a você um papel com as permissões listadas acima, como Editor de projetos ou um papel personalizado.

Se você não tiver acesso administrativo a um projeto, crie um novo que não esteja associado a uma organização para gerar suas chaves.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-19 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-19 UTC."],[],[]]
