---
source_url: https://ai.google.dev/gemini-api/docs/partner-integration?hl=pt-BR
fetched_at: 2026-05-05T20:05:44.063238+00:00
title: "Integra\u00e7\u00f5es de parceiros e bibliotecas \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Integrações de parceiros e bibliotecas

Este guia descreve estratégias arquitetônicas para criar bibliotecas, plataformas e gateways com base na API Gemini. Ele detalha as compensações técnicas
entre o uso dos SDKs oficiais de IA generativa, da API Direct (REST/gRPC) e da
camada de compatibilidade do OpenAI.

Use este guia se você estiver criando ferramentas para outros desenvolvedores, como
estruturas de código aberto, gateways corporativos ou agregadores de SaaS, e precisar
otimizar a higiene de dependências, o tamanho do pacote ou a paridade de recursos.

## O que é a integração de parceiros?

Um parceiro é qualquer pessoa que esteja criando uma integração entre a API Gemini e desenvolvedores
de usuários finais. Categorizamos os parceiros em quatro arquétipos. Identificar qual delas corresponde mais ao seu caso vai ajudar você a escolher o caminho de integração certo.

#### Framework do ecossistema

- **Quem você é**:mantenedor de um framework de código aberto (por exemplo, LangChain, LlamaIndex, Spring AI) ou clientes específicos de linguagem.
- **Seu objetivo**:compatibilidade ampla. Você quer que sua biblioteca funcione em qualquer ambiente escolhido pelo usuário sem forçar conflitos.

#### Plataforma de ambiente de execução e de borda

- **Quem você é**:plataformas SaaS, gateways de IA ou provedores de infraestrutura de nuvem (por exemplo, Vercel, Cloudflare, Zapier) em que a execução de código acontece em ambientes restritos.
- **Seu objetivo**:desempenho. Você precisa de baixa latência, tamanho mínimo do pacote e
  inicializações a frio rápidas.

#### Agregador

- **Quem você é**:plataformas, proxies ou "Model Gardens" internos que normalizam o acesso em vários provedores de LLM diferentes (por exemplo, OpenAI, Anthropic, Google) em uma única interface.
- **Seu objetivo**:portabilidade e uniformidade.

#### Gateway empresarial

- **Quem você é**:equipes internas de engenharia de plataforma em grandes empresas que criam "caminhos dourados" para centenas de desenvolvedores internos.
- **Seu objetivo**:padronização, governança e autenticação unificada.

## Resumo comparativo

**Prática recomendada global**:todos os parceiros precisam enviar o [cabeçalho `x-goog-api-client`](#client-id), seja qual for o caminho escolhido.

| Se você é... | Caminho recomendado | Principal benefício | Compensação principal | Prática recomendada |
| --- | --- | --- | --- | --- |
| **Gateway empresarial, framework de ecossistema** | **[SDK da IA generativa do Google](#genai-sdk)** | **Paridade e velocidade da plataforma de agentes do Gemini Enterprise**. Tratamento integrado para tipos, autenticação e recursos complexos (por exemplo, uploads de arquivos). Migração perfeita para o Google Cloud. | **Peso da dependência**. As dependências transitivas podem ser complexas e estar fora do seu controle. Limitado às linguagens compatíveis (Python/Node/Go/Java). | **Bloquear versões**. Fixe as versões do SDK nas imagens de base internas para garantir a estabilidade entre as equipes. |
| **Framework de ecossistema, plataformas de borda e agregadores** | **[API Direct](#rest)**  *(REST / gRPC)* | **Sem dependências**. Você controla o cliente HTTP e o tamanho exato do pacote. Acesso total a todos os recursos de API e modelo. | **Alta sobrecarga do desenvolvedor.** As estruturas JSON podem ser profundamente aninhadas e exigem validação manual e verificação de tipo rigorosas. | **Use especificações OpenAPI.** Automatize a geração de tipos usando nossas especificações oficiais em vez de escrevê-las à mão. |
| **Agregador que usa SDKs da OpenAI que exigem apenas fluxos de trabalho baseados em texto**  *(otimização para portabilidade legada)* | **[Compatibilidade com a OpenAI](#openai)** | **Portabilidade instantânea.** Reutilizar códigos ou bibliotecas compatíveis com a OpenAI. | **Teto de recursos.** Recursos específicos do modelo (vídeo nativo, armazenamento em cache) podem não estar disponíveis. | **Plano de migração**. Use isso para validação rápida, mas planeje fazer upgrade para a API Direct e ter acesso a todos os recursos da API. |

## Integração do SDK de IA generativa do Google

Para frameworks, a implementação do [SDK do Google GenAI](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br)
é geralmente o caminho mais simples, já que tem o menor número de linhas de código em linguagens
compatíveis.

Para equipes internas de plataforma, o principal resultado é geralmente um "caminho ideal"
que permite que os engenheiros de produtos trabalhem rapidamente e cumpram as políticas de
segurança.

**Benefícios:**

- **Interface unificada para migração da plataforma de agentes do Gemini Enterprise**:os desenvolvedores internos geralmente criam protótipos usando chaves de API (API Gemini) e implantam na plataforma de agentes do Gemini Enterprise (IAM) para conformidade de produção. O SDK abstrai essas diferenças de autenticação.
  Da mesma forma, para frameworks, você pode implementar um codepath e oferecer suporte a dois conjuntos de usuários.
- **Auxiliares do lado do cliente**:o SDK inclui utilitários idiomáticos que reduzem o boilerplate para tarefas complexas.
  - *Exemplos*:suporte a objetos de imagem `PIL` diretamente em comandos, chamadas automáticas de função e tipos abrangentes.
- **Acesso a recursos no dia zero**:os novos recursos da API ficam disponíveis no momento do lançamento
  pelos SDKs.
- **Melhor suporte à geração de código**:a instalação do SDK local expõe definições de tipo e docstrings a assistentes de programação (por exemplo, Cursor, Copilot).
  Esse contexto melhora a precisão da geração de código em comparação com a geração de solicitações REST brutas.

**A compensação:**

- **Peso e complexidade da dependência**:os SDKs têm dependências próprias, o que pode aumentar o tamanho do pacote e o risco da cadeia de suprimentos.
- **Controle de versões**:os novos recursos da API geralmente são fixados em versões mínimas do SDK.
  Talvez seja necessário enviar atualizações para os usuários acessarem novos recursos ou modelos,
  o que, em alguns casos, pode exigir mudanças em dependências transitivas que
  afetam seus usuários.
- **Limites de protocolo**:os SDKs são compatíveis apenas com HTTPS para a API principal e
  WebSockets (WSS) para a API Live. O gRPC não é compatível com os
  clientes SDK de alto nível.
- **Suporte a idiomas**:os SDKs são compatíveis com as versões *atuais* dos idiomas. Se você precisar oferecer suporte a versões EOL (por exemplo, Python 3.9), será necessário manter um fork.

**Prática recomendada:**

- **Bloquear versões**:fixe a versão do SDK nas imagens de base internas para garantir a estabilidade entre as equipes.

## Integração direta de API

Se você estiver distribuindo uma biblioteca para milhares de desenvolvedores, executando em um ambiente restrito ou criando um agregador que exija os recursos mais recentes do Gemini, talvez seja necessário fazer a integração diretamente com a API usando REST ou gRPC.

**Benefícios:**

- **Acesso ao recurso completo**:ao contrário da camada de compatibilidade da OpenAI, usar a API diretamente ativa recursos específicos do Gemini, como fazer upload para a API File, criar armazenamento em cache de conteúdo e usar a API Live bidirecional.
- **Dependências mínimas**:em um ambiente em que as dependências são sensíveis devido ao tamanho ou aos custos de auditoria. Usar a API diretamente por uma
  biblioteca padrão, como `fetch`, ou por um wrapper, como `httpx`, garante que sua
  biblioteca permaneça leve.
- **Independente de linguagem**:esse é o único caminho para linguagens não cobertas pelos SDKs, como Rust, PHP e Ruby, já que não há restrições de linguagem.
- **Performance**:a API Direct não tem sobrecarga de inicialização, minimizando as inicializações a frio em funções sem servidor.

**A compensação:**

- **Implementação manual da plataforma de agentes do Gemini Enterprise**:ao contrário do SDK, usar a API diretamente não processa automaticamente as diferenças de autenticação entre o AI Studio (chave de API) e a plataforma de agentes do Gemini Enterprise (IAM). É necessário implementar manipuladores de autenticação separados se você quiser oferecer suporte aos dois ambientes.
- **Sem tipos ou helpers nativos**:você não recebe preenchimentos de código nem verificações de tempo de compilação para objetos de solicitação, a menos que os implemente por conta própria. Não há "ajudantes" de cliente (por exemplo, conversores de função para esquema), então você precisa escrever essa lógica manualmente.

**Prática recomendada**

Exibimos uma especificação legível por máquina que pode ser usada para gerar definições de tipo para sua biblioteca, evitando que você as escreva à mão. Faça o download da
especificação durante o processo de build, gere os tipos e envie o código compilado.

- **Endpoint**:`https://generativelanguage.googleapis.com/$discovery/OPENAPI3_0`

## Integração do SDK da OpenAI

Se você for uma plataforma que prioriza um esquema unificado (OpenAI Chat Completions) em vez de recursos específicos do modelo, esse é o trajeto mais rápido.

**Benefícios:**

- **Baixa fricção**:muitas vezes, é possível adicionar suporte ao Gemini mudando o `baseURL`
  e o `apiKey`. Essa é uma maneira rápida de integrar implementações de "Traga sua própria chave", adicionando suporte do Gemini sem escrever um novo código.
- **Restrições**:esse caminho só é recomendado se você estiver restrito ao SDK da
  OpenAI e não precisar de recursos avançados do Gemini, como a API File,
  ou adicionar manualmente suporte para ferramentas como o embasamento com a Pesquisa Google.

**A compensação:**

- **Limitações de recursos**:a camada de compatibilidade limita os recursos principais do Gemini. As ferramentas disponíveis do lado do servidor variam entre as plataformas e podem exigir manipulação manual para funcionar com as ferramentas da API Gemini.
- **Sobrecarga de tradução**:como o esquema da OpenAI não tem mapeamento 1:1 com a arquitetura do Gemini, confiar na camada de compatibilidade introduz algumas complexidades que exigem trabalho extra de implementação para resolver, como mapear uma ferramenta de "pesquisa" do usuário para a ferramenta de plataforma certa.
  Se você precisar de uma quantidade significativa de tratamento especial, talvez seja mais valioso usar um SDK ou uma API dedicada para cada plataforma.

**Prática recomendada**

Sempre que possível, faça a integração diretamente com a API Gemini. No entanto, para máxima compatibilidade, considere usar uma biblioteca que conheça diferentes provedores e possa processar o mapeamento de ferramentas e mensagens para você.

## Prática recomendada para todos os parceiros: identificação do cliente

Ao fazer chamadas para a API Gemini como uma plataforma ou biblioteca, é necessário
identificar seu cliente usando o cabeçalho `x-goog-api-client`.

Isso permite que o Google identifique seus segmentos de tráfego específicos. Se a biblioteca estiver produzindo um padrão de erro específico, podemos entrar em contato para ajudar na depuração.

Use o formato `company-product/version` (por exemplo, `acme-framework/1.2.0`).

### Exemplos de implementação

### SDK de IA generativa

Ao fornecer o cliente de API, o SDK anexa automaticamente o cabeçalho personalizado aos cabeçalhos internos.

```
from google import genai

client = genai.Client(
    api_key="...",
    http_options={
        "headers": {
            "x-goog-api-client": "acme-framework/1.2.0",
        }
    }
)
```

### API direta (REST)

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H 'x-goog-api-client: acme-framework/1.2.0' \
    -d '{...}'
```

### SDK da OpenAI

```
from openai import OpenAI

client = OpenAI(
    api_key="...",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    default_headers={
        "x-goog-api-client": "acme-framework-oai/1.2.0",
    }
)
```

## Próximas etapas

- Acesse a [visão geral da biblioteca](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br) para saber mais sobre
  os SDKs da IA generativa
- Consulte a [referência da API](https://ai.google.dev/api?hl=pt-br).
- Leia o [guia de compatibilidade da OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br)

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-04-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-04-29 UTC."],[],[]]
