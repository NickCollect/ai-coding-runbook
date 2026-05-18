---
source_url: https://ai.google.dev/gemini-api/docs/partner-integration?hl=pt-BR
fetched_at: 2026-05-18T05:13:43.092468+00:00
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

Este guia descreve as estratégias arquitetônicas para criar bibliotecas, plataformas e gateways com base na API Gemini. Ele detalha as compensações técnicas entre o uso dos SDKs oficiais da GenAI, a API direta (REST/gRPC) e a camada de compatibilidade do OpenAI.

Use este guia se você estiver criando ferramentas para outros desenvolvedores, como frameworks de código aberto, gateways corporativos ou agregadores de SaaS, e precisar otimizar a higiene de dependências, o tamanho do pacote ou a paridade de recursos.

## O que é a integração de parceiros?

Um parceiro é qualquer pessoa que esteja criando uma integração entre a API Gemini e desenvolvedores de usuários finais. Categorizamos os parceiros em quatro arquétipos. Identificar qual deles corresponde mais de perto vai ajudar você a escolher o caminho de integração certo.

#### Framework de ecossistema

- **Quem você é**:mantenedor de um framework de código aberto (por exemplo, LangChain, LlamaIndex, Spring AI) ou clientes específicos do idioma.
- **Seu objetivo**:ampla compatibilidade. Você quer que sua biblioteca funcione em qualquer ambiente escolhido pelo usuário sem forçar conflitos.

#### Plataforma de execução e de borda

- **Quem você é**:plataformas SaaS, gateways de IA ou provedores de infraestrutura em nuvem (por exemplo, Vercel, Cloudflare, Zapier) em que a execução de código acontece em ambientes restritos.
- **Seu objetivo**:performance. Você precisa de baixa latência, tamanho mínimo do pacote e inicializações a frio rápidas.

#### Agregador

- **Quem você é**:plataformas, proxies ou "Model Gardens" internos que normalizam o acesso em muitos provedores de LLM diferentes (por exemplo, OpenAI, Anthropic, Google) em uma única interface.
- **Seu objetivo**:portabilidade e uniformidade.

#### Gateway corporativo

- **Quem você é**:equipes internas de engenharia de plataforma em grandes empresas que criam "caminhos ideais" para centenas de desenvolvedores internos.
- **Seu objetivo**:padronização, governança e autenticação unificada.

## Resumo comparativo

**Prática recomendada global:** todos os parceiros precisam enviar o [`x-goog-api-client`
cabeçalho](#client-id), independentemente do caminho escolhido.

| Se você for... | Caminho recomendado | Principal benefício | Principal compensação | Prática recomendada |
| --- | --- | --- | --- | --- |
| **Gateway corporativo, framework de ecossistema** | **[SDK da GenAI do Google](#genai-sdk)** | **Paridade e velocidade da plataforma de agentes do Gemini Enterprise**. Processamento integrado para tipos, autenticação e recursos complexos (por exemplo, uploads de arquivos). Migração perfeita para o Google Cloud. | **Peso da dependência**. As dependências transitivas podem ser complexas e fora do seu controle. Limitado a linguagens compatíveis (Python/Node/Go/Java). | **Bloquear versões**. Fixe as versões do SDK nas imagens de base internas para garantir a estabilidade entre as equipes. |
| **Framework de ecossistema, plataformas de borda e agregadores** | **[API direta](#rest)**  *(REST / gRPC)* | **Dependências zero**. Você controla o cliente HTTP e o tamanho exato do pacote. Acesso total a todos os recursos da API e do modelo. | **Alto custo para desenvolvedores**. As estruturas JSON podem ser profundamente aninhadas e exigem validação manual e verificação de tipo rigorosas. | **Usar especificações OpenAPI**. Automatize a geração de tipos usando nossas especificações oficiais em vez de escrevê-las manualmente. |
| **Agregador que usa SDKs do OpenAI que exigem apenas fluxos de trabalho baseados em texto**  *(Otimização para portabilidade legada)* | **[Compatibilidade com o OpenAI](#openai)** | **Portabilidade instantânea**. Reutilize códigos ou bibliotecas compatíveis com o OpenAI. | **Limite de recursos**. Os recursos específicos do modelo (vídeo nativo, armazenamento em cache) podem não estar disponíveis. | **Plano de migração**. Use isso para validação rápida, mas planeje fazer upgrade para a API direta para ter o recurso completo da API. |

## Integração do SDK da GenAI do Google

Para frameworks, a implementação do [SDK da GenAI do Google](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br)
é geralmente o caminho mais simples, considerando o menor número de linhas de código em linguagens compatíveis.

Para equipes de plataforma internas, o principal resultado é geralmente um "caminho ideal" que permite que os engenheiros de produtos se movam rapidamente, obedecendo às políticas de segurança.

**Benefícios:**

- **Interface unificada para migração da plataforma de agentes do Gemini Enterprise**:os desenvolvedores internos geralmente criam protótipos usando chaves de API (API Gemini) e implantam na plataforma de agentes do Gemini Enterprise (IAM) para conformidade de produção. O SDK abstrai essas diferenças de autenticação.
  Da mesma forma, para frameworks, é possível implementar um caminho de código e oferecer suporte a dois conjuntos de usuários.
- **Auxiliares do lado do cliente**:o SDK inclui utilitários idiomáticos que reduzem o código boilerplate para tarefas complexas.
  - *Exemplos*:suporte a objetos de imagem `PIL` diretamente em comandos, chamadas de função automáticas e tipos abrangentes.
- **Acesso a recursos do dia zero**:novos recursos da API estão disponíveis no momento do lançamento pelos SDKs.
- **Melhor suporte à geração de código**:a instalação local do SDK expõe definições de tipo e docstrings a assistentes de programação (por exemplo, Cursor, Copilot).
  Esse contexto melhora a precisão da geração de código em comparação com a geração de solicitações REST brutas.

**A compensação:**

- **Peso e complexidade da dependência**:os SDKs têm as próprias dependências, o que pode aumentar o tamanho do pacote e o risco da cadeia de suprimentos.
- **Controle de versão**:novos recursos da API são geralmente fixados em versões mínimas do SDK.
  Talvez seja necessário enviar atualizações aos usuários para acessar novos recursos ou modelos, o que, em alguns casos, pode exigir mudanças em dependências transitivas que afetam os usuários.
- **Limites de protocolo**:os SDKs oferecem suporte apenas a HTTPS para a API principal e WebSockets (WSS) para a API Live. O gRPC não é compatível com clientes de SDK de alto nível.
- **Suporte a idiomas**:os SDKs oferecem suporte às versões *atuais* de idiomas. Se você precisar oferecer suporte a versões EOL (por exemplo, Python 3.9), será necessário manter um fork.

**Prática recomendada:**

- **Bloquear versões**:fixe a versão do SDK nas imagens de base internas para garantir a estabilidade entre as equipes.

## Integração direta com a API

Se você estiver distribuindo uma biblioteca para milhares de desenvolvedores, executando em um ambiente restrito ou criando um agregador que exige os recursos de ponta do Gemini, talvez seja necessário fazer a integração diretamente com a API usando REST ou gRPC.

**Benefícios:**

- **Acesso total aos recursos**:ao contrário da camada de compatibilidade do OpenAI, o uso direto da API ativa recursos específicos do Gemini, como upload para a API File, criação de armazenamento em cache de conteúdo e uso da API Live bidirecional.
- **Dependências mínimas**:em um ambiente em que as dependências são sensíveis devido ao tamanho ou aos custos de auditoria. O uso direto da API por meio de uma biblioteca padrão, como `fetch`, ou por um wrapper, como `httpx`, garante que a biblioteca permaneça leve.
- **Independente de linguagem**:esse é o único caminho para linguagens não cobertas pelos SDKs, como Rust, PHP e Ruby, já que não há restrições de linguagem.
- **Performance**:a API direta não tem custo de inicialização, minimizando as inicializações a frio em funções sem servidor.

**A compensação:**

- **Implementação manual da plataforma de agentes do Gemini Enterprise**:ao contrário do SDK, o uso direto da API não processa automaticamente as diferenças de autenticação entre o AI Studio (chave de API) e a plataforma de agentes do Gemini Enterprise (IAM). É necessário implementar gerenciadores de autenticação separados se você quiser oferecer suporte aos dois ambientes.
- **Sem tipos ou auxiliares nativos**:você não recebe conclusões de código ou verificações de tempo de compilação para objetos de solicitação, a menos que os implemente por conta própria. Não há "auxiliares" de cliente (por exemplo, conversores de função para esquema), então você precisa escrever essa lógica manualmente.

**Prática recomendada**

Exibimos uma especificação legível por máquina que pode ser usada para gerar definições de tipo para sua biblioteca, evitando que você as escreva manualmente. Faça o download da especificação durante o processo de build, gere os tipos e envie o código compilado.

- **Endpoint**:`https://generativelanguage.googleapis.com/$discovery/OPENAPI3_0`

## Integração do SDK do OpenAI

Se você é uma plataforma que prioriza um esquema unificado (conclusões de chat do OpenAI) em vez de recursos específicos do modelo, esse é o trajeto mais rápido.

**Benefícios:**

- **Baixa fricção**:geralmente, é possível adicionar suporte ao Gemini mudando o `baseURL` e a `apiKey`. Essa é uma maneira rápida de integrar implementações "Traga sua própria chave", adicionando suporte ao Gemini sem escrever um novo código.
- **Restrições**:esse caminho só é recomendado se você estiver restrito ao SDK do OpenAI e não precisar de recursos avançados do Gemini, como a API File, ou adicionar manualmente suporte a ferramentas como o embasamento com a Pesquisa Google.

**A compensação:**

- **Limitações de recursos**:a camada de compatibilidade oferece limitações aos recursos principais do Gemini. As ferramentas disponíveis do lado do servidor variam entre as plataformas e podem exigir processamento manual para funcionar com as ferramentas da API Gemini.
- **Sobrecarga de tradução**:como o esquema do OpenAI não é mapeado 1:1 para a arquitetura do Gemini, a dependência da camada de compatibilidade introduz algumas complexidades que exigem mais trabalho de implementação para serem resolvidas, como mapear uma ferramenta de "pesquisa" do usuário para a ferramenta de plataforma certa.
  Se você precisar de uma quantidade significativa de casos especiais, talvez seja mais valioso usar um SDK ou API dedicado para cada plataforma.

**Prática recomendada**

Sempre que possível, faça a integração diretamente com a API Gemini. No entanto, para máxima compatibilidade, considere usar uma biblioteca que reconheça diferentes provedores e possa processar o mapeamento de ferramentas e mensagens para você.

## Prática recomendada para todos os parceiros: identificação do cliente

Ao fazer chamadas para a API Gemini como uma plataforma ou biblioteca, é necessário identificar o cliente usando o cabeçalho `x-goog-api-client`.

Isso permite que o Google identifique seus segmentos de tráfego específicos e, se a biblioteca estiver produzindo um padrão de erro específico, podemos entrar em contato para ajudar na depuração.

Use o formato `company-product/version` (por exemplo, `acme-framework/1.2.0`).

### Exemplos de implementação

### SDK da GenAI

Ao fornecer o cliente da API, o SDK anexa automaticamente o cabeçalho personalizado aos cabeçalhos internos.

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

### SDK do OpenAI

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
  os SDKs da GenAI.
- Navegue pela [referência da API](https://ai.google.dev/api?hl=pt-br).
- Leia o [guia de compatibilidade do OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-13 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-13 UTC."],[],[]]
