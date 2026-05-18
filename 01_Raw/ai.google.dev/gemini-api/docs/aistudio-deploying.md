---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pt-BR
fetched_at: 2026-05-18T05:07:18.629308+00:00
title: "Implanta\u00e7\u00e3o do Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Implantação do Google AI Studio

Com o Google AI Studio, você pode implantar seus aplicativos de pilha completa diretamente
no modo de criação. Isso oferece um caminho rápido do protótipo para um ambiente de produção gerenciado e escalonável.

## Opções de implantação

Para implantar seu aplicativo no modo de criação do AI Studio, os requisitos dependem
do nível que você usa:

- [**Nível inicial do Google Cloud**](https://docs.cloud.google.com/docs/starter-tier?hl=pt-br):
  permite publicar até dois aplicativos full-stack sem configurar um
  projeto na nuvem ou uma conta de faturamento do Google Cloud.
- **Implantação padrão**: requer um projeto do Google Cloud vinculado à sua conta do AI Studio e o faturamento ativado nesse projeto.

## Sobre o nível Starter

O nível inicial do Google Cloud oferece um caminho simplificado para implantar
aplicativos no Google Cloud diretamente do Google AI Studio sem configurar
um ambiente completo do Google Cloud ou uma conta de faturamento.

Cada implantação do Google AI Studio cria um serviço correspondente no
Cloud Run. Para serviços implantados no Google AI Studio com o nível
Starter, as seguintes limitações se aplicam:

- É possível implantar até dois serviços.
- Seus serviços são implantados em uma [única região do Cloud Run](https://docs.cloud.google.com/run/docs/locations?hl=pt-br).

## Etapas de implantação do nível Starter

Depois de criar o app no modo de criação, implante-o com o nível Starter:

1. Clique no botão **Publicar** no canto superior direito.
2. Clique em **Primeiros passos**.
3. Clique em **Publicar app**.

Quando a implantação for concluída, o AI Studio vai fornecer um URL do Cloud Run em que você pode
acessar seu aplicativo ativo.

## Implantação padrão

À medida que seus aplicativos evoluem, você pode precisar de recursos além do nível Starter, como cotas mais altas, mais recursos de computação ou outros produtos do Google Cloud não disponíveis nesse nível. Para desbloquear esses recursos, você pode converter seu projeto totalmente gerenciado do nível Starter em um projeto na nuvem padrão do Google.

Isso garante que você possa dimensionar sem perder o progresso. Siga as etapas para
[criar uma conta do Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=pt-br#create-new-billing-account),
aceitar formalmente os Termos de Serviço padrão do Google Cloud e
[fazer upgrade para um projeto na nuvem padrão do Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=pt-br#upgradee).
Para mais informações, consulte
[Configuração para contas pagas](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=pt-br#paid-setup).

Para saber mais sobre os níveis de faturamento, consulte [Faturamento](https://ai.google.dev/gemini-api/docs/billing?hl=pt-br).

## Excluir sua inscrição

Se você não precisar mais do app, siga estas instruções para excluí-lo no Google AI Studio:

1. No Google AI Studio, acesse a
   [página "Apps"](https://aistudio.google.com/app/apps?hl=pt-br).
2. No menu à esquerda, selecione **Apps**.
3. Coloque o cursor sobre o app que você quer excluir.
4. Clique no ícone de lixeira no lado direito da linha para excluir o app.

## A seguir

- Saiba mais sobre o
  [nível inicial do Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=pt-br).
- Leia sobre o [faturamento](https://ai.google.dev/gemini-api/docs/billing?hl=pt-br) na API Gemini.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-16 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-16 UTC."],[],[]]
