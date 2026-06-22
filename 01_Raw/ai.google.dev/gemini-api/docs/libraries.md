---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=pt-BR
fetched_at: 2026-06-22T06:32:28.214147+00:00
title: "Bibliotecas da API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Bibliotecas da API Gemini

Ao criar com a API Gemini, recomendamos usar o **SDK da IA generativa do Google**.
Essas são as bibliotecas oficiais e prontas para produção que desenvolvemos e mantemos
para as linguagens mais usadas. Eles estão em [Disponibilidade geral](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br#new-libraries) e são usados em toda a nossa documentação e exemplos oficiais.

Se você nunca usou a API Gemini, siga nosso [guia de início rápido](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br) para começar.

## Suporte e instalação de idiomas

O SDK da IA generativa do Google está disponível para as linguagens Python, JavaScript/TypeScript, Go e
Java. É possível instalar a biblioteca de cada linguagem usando gerenciadores de pacotes ou acessar os repositórios do GitHub para mais informações:

### Python

- Biblioteca: [`google-genai`](https://pypi.org/project/google-genai)
- Repositório do GitHub: [googleapis/python-genai](https://github.com/googleapis/python-genai)
- Instalação: `pip install google-genai`

### JavaScript

- Biblioteca: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- Repositório do GitHub: [googleapis/js-genai](https://github.com/googleapis/js-genai)
- Instalação: `npm install @google/genai`

### Go

- Biblioteca: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- Repositório do GitHub: [googleapis/go-genai](https://github.com/googleapis/go-genai)
- Instalação: `go get google.golang.org/genai`

### Java

- Biblioteca: `google-genai`
- Repositório do GitHub: [googleapis/java-genai](https://github.com/googleapis/java-genai)
- Instalação: se você estiver usando o Maven, adicione o seguinte às dependências:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

- Biblioteca: `Google.GenAI`
- Repositório do GitHub: [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- Instalação: `dotnet add package Google.GenAI`

## Disponibilidade geral

Em maio de 2025, o SDK da IA generativa do Google atingiu a disponibilidade geral (GA) em
todas as plataformas compatíveis e é a biblioteca recomendada para acessar a API Gemini.
Elas são estáveis, têm suporte total para uso em produção e são mantidas ativamente.
Eles oferecem acesso aos recursos mais recentes e a melhor performance ao trabalhar com o Gemini.

Se você estiver usando uma das nossas bibliotecas legadas,
recomendamos migrar para ter acesso aos recursos mais recentes e
aproveitar o melhor desempenho ao trabalhar com o Gemini. Consulte a seção [bibliotecas legadas](https://ai.google.dev/gemini-api/docs/libraries?hl=pt-br#previous-sdks) para mais informações.

## Bibliotecas legadas e migração

Se você estiver usando uma das nossas bibliotecas legadas, recomendamos que
[migre para as novas bibliotecas](https://ai.google.dev/gemini-api/docs/migrate?hl=pt-br).

As bibliotecas legadas não oferecem acesso a recursos recentes, como a [API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br) e o [Veo](https://ai.google.dev/gemini-api/docs/video?hl=pt-br), e serão descontinuadas em 30 de novembro de 2025.

O status de suporte de cada biblioteca legada varia, conforme detalhado na tabela a seguir:

| Idioma | Biblioteca legada | Status de compatibilidade | Biblioteca recomendada |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | Não mantido ativamente | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | Não é mantido ativamente | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | Não é mantido ativamente | `google.golang.org/genai` |
| **Dart e Flutter** | `google_generative_ai` | Não mantido ativamente | Use o [Genkit Dart](https://genkit.dev/docs/dart/get-started/) ou o [Firebase AI Logic](https://pub.dev/packages/firebase_ai) |
| **Swift** | `generative-ai-swift` | Não é mantido ativamente | Usar o [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=pt-br) |
| **Android** | `generative-ai-android` | Não mantido ativamente | Usar o [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=pt-br) |

**Observação para desenvolvedores Java**:não havia um SDK Java legado fornecido pelo Google para a API Gemini. Portanto, não é necessário migrar de uma biblioteca anterior do Google. Você
pode começar diretamente com a nova biblioteca na seção
[Suporte a idiomas e instalação](#install).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-28 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-28 UTC."],[],[]]
