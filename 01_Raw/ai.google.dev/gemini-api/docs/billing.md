---
source_url: https://ai.google.dev/gemini-api/docs/billing?hl=pt-BR
fetched_at: 2026-06-01T06:04:08.908509+00:00
title: "Faturamento \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Faturamento

Este guia oferece uma visão geral das diferentes opções de faturamento da API Gemini, explica como ativar o faturamento e monitorar o uso e fornece respostas para perguntas frequentes sobre o faturamento.

## Sobre faturamento e níveis

O faturamento da API Gemini é baseado no seu histórico de pagamentos.

| Nível de uso | Qualificação | [Limite do nível de faturamento](#spend-caps) |
| --- | --- | --- |
| **Free** (link em francês) | [Projeto ativo](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br#google-cloud-projects) ou teste sem custo financeiro | N/A |
| **Nível 1** | [Configurar e vincular uma conta de faturamento ativa](#setup-billing) | US$ 250,00 |
| **Nível 2** | Pagamento de US $100 + 3 dias desde o primeiro pagamento bem-sucedido | US$ 2.000 |
| **Nível 3** | Pago US $1.000 + 30 dias desde o primeiro pagamento bem-sucedido | US$ 20.000 a US$ 100.000 ou mais |

As novas contas começam no nível sem custo financeiro, que permite o acesso a [determinados modelos](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br) na API Gemini e no AI Studio, até os [limites de taxa](https://aistudio.google.com/rate-limit?hl=pt-br) do nível sem custo financeiro dos modelos.

Para implantar seus aplicativos diretamente do modo de build, use o
**nível Starter do Google Cloud**. Com esse nível, é possível publicar até dois aplicativos de pilha completa sem configurar um projeto na nuvem do Google ou uma conta de faturamento.
Consulte [Como fazer a implantação no Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pt-br) para
detalhes e consulte a [documentação do nível inicial do Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=pt-br) para mais informações.

Para acessar limites de taxa mais altos, usar modelos avançados e garantir que seus comandos e respostas **não** sejam usados para melhorar os produtos do Google\*, [vincule uma conta de faturamento](#setup-billing) e [faça um pré-pagamento](#prepay) para mudar para os planos pagos.
Em seguida, você vai passar para níveis mais altos com base no gasto acumulado e na idade da conta. No nível 3, talvez você possa mudar para o faturamento [pós-pago](#postpay).

Os níveis, os limites de taxa e os limites máximos da conta de faturamento são determinados no nível da [conta de faturamento](#cloud-billing).

\* *Privacidade de dados de nível empresarial: para mais informações sobre o uso de dados
para serviços pagos, consulte os [Termos de Serviço](https://ai.google.dev/gemini-api/terms?hl=pt-br#data-use-paid).*

## Configurar o faturamento para acessar o nível pago

Você pode criar um projeto e configurar o faturamento ou importar um projeto existente para
fazer upgrade para o nível pago no [Google AI Studio](https://aistudio.google.com/projects?hl=pt-br).
Fazer upgrade do nível sem custo financeiro para o nível pago significa vincular uma conta de faturamento e [fazer um pré-pagamento](#prepay) para adicionar um mínimo de US $10 (ou o equivalente em outras moedas) de créditos à sua conta.

1. Acesse a página [Chaves de API](https://aistudio.google.com/api-keys?hl=pt-br), [Projetos](https://aistudio.google.com/projects?hl=pt-br) ou qualquer lugar em que o botão **Configurar faturamento** apareça no AI Studio.
   - Por padrão, os novos usuários têm um [projeto e uma chave de API](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br#google-cloud-projects) criados para eles.
   - Se você precisar de uma nova chave, clique em [**Criar chave de API**](https://aistudio.google.com/api-keys?hl=pt-br) e siga a caixa de diálogo para adicionar um par chave-projeto à tabela.
2. Encontre o projeto do nível sem custo financeiro que você quer fazer upgrade para o nível pago e clique em **Configurar faturamento** na coluna *Nível de faturamento*.
3. Se você nunca configurou uma conta de faturamento do Google:
   - Você vai precisar selecionar seu país para concordar com os Termos de Serviço.
   - Em seguida, preencha ou confirme suas informações de contato e forma de pagamento para continuar.
4. Se você já configurou contas de faturamento do Google:
   - Será necessário escolher uma das suas contas de faturamento.
   - Se não quiser usar nenhuma das suas contas, clique em **Adicionar nova conta de faturamento** e preencha ou confirme suas informações de contato e forma de pagamento para continuar.
5. Em seguida, você vai:
   - Foi solicitado que você fizesse um pré-pagamento mínimo de US $10 para concluir a configuração do faturamento (ou seja, sua conta foi atribuída automaticamente ao plano de faturamento [pré-pago](#prepay)).
   - Escolha entre os planos de faturamento [Pré-pago](#prepay) e [Pós-pago](#postpay) para sua conta.
   - Atribuído a um plano de faturamento [pós-pago](#postpay) por um período intermediário até que o novo sistema pré-pago seja propagado para todos os usuários (a partir de 23 de março de 2026).
6. Depois de fazer o pré-pagamento ou selecionar o pós-pago, a configuração da conta será concluída.

### Fazer upgrade para o próximo nível pago

Se você já estiver em um nível pago e atender aos [critérios](#about-billing)
para uma mudança de plano, vai receber um upgrade automático para o próximo nível
(sujeito a [tempos de processamento](#processing-times)).

## Verificar o status de faturamento

Depois de [vincular uma conta de faturamento](#setup-billing) ao seu projeto, você
pode monitorar o status dela na
[página de faturamento do AI Studio](https://aistudio.google.com/billing?hl=pt-br). Ao contrário do nível sem custo financeiro, o status do nível pago é dinâmico. Embora seu nível de uso seja determinado pelo histórico da conta, a API Gemini só vai atender às solicitações se você tiver um saldo de crédito [pré-pago](#prepay) positivo.

Na página [Projetos](https://aistudio.google.com/projects?hl=pt-br), é possível
ver o nível e o plano de faturamento do projeto na coluna *Nível de faturamento*. Todas as ações de status de faturamento que você precisa realizar em um projeto são mostradas nas colunas *Nível de faturamento* ou *Status*:

- ***Configurar faturamento*** se o projeto não tiver uma conta de faturamento vinculada.
- ***Configurar pré-pago*** se o projeto tiver uma conta de faturamento anexada, mas precisar usar um plano de faturamento [pré-pago](#prepay) que precisa ser configurado.
- "***Nenhum crédito disponível***" se a conta de faturamento for necessária para comprar créditos, mas a conta para pagamentos de pré-pagamento não estiver configurada ou o saldo de crédito disponível estiver esgotado.

Clique em qualquer uma das mensagens para continuar com as ações necessárias.

## Monitorar o uso

É possível monitorar o uso da API Gemini no
[Google AI Studio](https://aistudio.google.com/usage?hl=pt-br) em **Painel** >
**Uso**.

## Planos de faturamento

Os planos de faturamento da API Gemini e do AI Studio se enquadram em duas categorias que determinam quando você paga pelo uso: pré-pagamento e pós-pagamento. Você pode verificar seu plano de faturamento atribuído e gerenciar as formas de pagamento na página [Faturamento do AI Studio](https://aistudio.google.com/billing?hl=pt-br).

### Pré-pagamento

No plano de faturamento pré-pago, você compra créditos para o saldo de pré-pagamento antes de usar a API Gemini, e os custos de uso da API são deduzidos do saldo de crédito pré-pago [quase em tempo real](#processing-times).
Você pode fazer um pré-pagamento [adicionando créditos](#buy-credits) à sua conta ou configurando a [recarga automática](#auto-reload). Depois da compra, os créditos não usados expiram após 12 meses e [não são reembolsáveis](#refunds), exceto após [mudar para uma conta pós-paga](#postpay).

Quando o saldo de crédito pré-pago na conta de faturamento chegar a US $0, todas as chaves de API em todos os projetos vinculados a essa conta de faturamento vão parar de funcionar simultaneamente.
Os créditos pré-pagos se aplicam apenas aos custos de uso da API Gemini. Eles não podem ser usados para pagar por outros serviços do Google Cloud.

Os novos usuários usam o plano de faturamento pré-pago por padrão. Os projetos anteriores à introdução dos planos de faturamento pré-pago e pós-pago talvez precisem [atualizar os detalhes de faturamento do projeto](#verify-billing) antes de continuar usando a API Gemini.

*Observe que o pré-pagamento não está disponível para contas [faturadas (ou off-line)](https://docs.cloud.google.com/billing/docs/concepts?hl=pt-br#billing_account_types).*

#### Comprar créditos

Você pode comprar créditos manualmente antes de usar a API Gemini para carregá-los no saldo de crédito da sua conta de pré-pagamento.

Para comprar créditos, acesse a página [Faturamento do AI Studio](https://aistudio.google.com/billing?hl=pt-br) e selecione **Comprar créditos**.
A compra mínima é de US $10. O valor máximo de créditos que você pode pagar antecipadamente é de US$ 5.000.

#### Atualizar automaticamente

A recarga automática é um recurso opcional que recarrega automaticamente o saldo de crédito pré-pago quando ele está baixo. Isso é útil para evitar interrupções no serviço.

Você pode configurar a recarga automática e conferir o status dela no card *Créditos disponíveis* na página [Faturamento do AI Studio](https://aistudio.google.com/billing?hl=pt-br). Clique em **Configurar recarga automática** ou
**Gerenciar recarga automática** para definir sua forma de pagamento, o valor da recarga e o
saldo mínimo que aciona um pagamento de recarga.

### Pós-pagamento

No plano de faturamento pós-pago, sua conta do Cloud Billing acumula custos, e você
recebe uma cobrança automática no fim do mês ou quando os custos atingem um
[limite de gastos atribuído automaticamente](#tier-spend-caps) com base no nível da conta.
O pagamento é cobrado na forma de pagamento vinculada à sua conta de pagamentos pós-pagos, que pode ser gerenciada na página [Faturamento do AI Studio](https://aistudio.google.com/billing?hl=pt-br).

Quando você atender aos [critérios do nível 3](#about-billing), poderá
mudar manualmente do plano pré-pago para o pós-pago. Para mudar de plano, clique no botão **Mudar para pós-pagamento**, que aparece no canto superior direito da página [Faturamento do AI Studio](https://aistudio.google.com/billing?hl=pt-br) quando sua conta se qualifica.

Na página **Faturamento**, você pode conferir seu saldo, datas de vencimento e pagamentos anteriores, além de fazer pagamentos e gerenciar formas de pagamento.

Ao [configurar o faturamento](#setup-billing) de um novo projeto, se você se qualificar para o pós-pagamento, poderá escolher entre pré-pagamento e pós-pagamento na caixa de diálogo [configuração de faturamento](#setup-billing).

Depois de mudar uma conta do Cloud Billing para usar o plano de faturamento pós-pago, todos os projetos vinculados a essa conta também serão mudados para o plano pós-pago. Não é possível mover essa conta de faturamento de volta para o plano de faturamento pré-pago. Você pode
mover um projeto para uma conta de faturamento com um plano de faturamento diferente para mudar
o ciclo de cobrança dele. Consulte a documentação do Cloud sobre [gerenciar
o faturamento de projetos](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=pt-br).

Saiba mais sobre o ciclo de cobrança pós-pagamento no [guia do Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=pt-br).

## Limites de gastos

A API Gemini oferece suporte a limites de gastos mensais nos níveis da conta de faturamento e do projeto. Esses controles foram criados para proteger sua conta contra
excedentes inesperados e o ecossistema para garantir a disponibilidade do serviço.

*Observação: os limites de gastos não estão disponíveis para contas [faturadas (ou off-line)](https://docs.cloud.google.com/billing/docs/concepts?hl=pt-br#billing_account_types).*

### Limites de gastos do projeto

É possível definir seus próprios limites de gastos [para envolvidos no projeto](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br#google-cloud-projects) no AI Studio.
Isso é útil se você tiver vários projetos na mesma conta de faturamento e quiser garantir que cada um tenha acesso a um limite de gastos cumulativo suficiente.

As contas com as [funções](https://docs.cloud.google.com/iam/docs/roles-overview?hl=pt-br) de editor, proprietário ou administrador do projeto podem definir limites de gastos por projeto no AI Studio na página [Gasto](https://aistudio.google.com/spend?hl=pt-br) em **Limite de gastos mensais** > **Editar limite de gastos**.

Para detalhes sobre as permissões específicas do IAM do Google Cloud necessárias para visualizar ou editar limites de gastos e informações de faturamento no AI Studio, consulte o [guia de solução de problemas do AI Studio](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=pt-br#iam-permissions).

Se você [mover um projeto para uma conta de faturamento diferente](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=pt-br#change_the_billing_account_for_a_project),
o limite de gastos definido para esse projeto vai persistir, mas os gastos acumulados
serão redefinidos para US $0 no novo ciclo de faturamento.

Tarefas de longa duração, como conclusões no [modo em lote](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br) e sessões de agente, podem gerar excedentes além do limite de gastos do projeto.

Os tempos de processamento dos dados de faturamento podem ter um atraso de até 10 minutos no AI Studio. Você pode ter excedentes além do limite do projeto se os dados de faturamento não forem processados antes do acúmulo de mais cobranças.

### Limites de gastos por nível da conta de faturamento

Cada [nível](#about-billing) tem um limite máximo de gasto mensal:

| Nível de uso | Limite de gastos |
| --- | --- |
| **Free** (link em francês) | N/A |
| **Nível 1** | US$ 250,00 |
| **Nível 2** | US$ 2.000 |
| **Nível 3** | US$ 20.000 a US$ 100.000 |

Os limites de uso mensais são obrigatórios para a API Gemini no nível da [conta de faturamento](#cloud-billing). Embora os limites padrão sejam predefinidos, é possível [solicitar um aumento](https://docs.google.com/forms/d/e/1FAIpQLSdiP6BWJyNNN65lnwnlOr-5Kv0MOFp0jLQyqi_ixVCfddqWBw/viewform?hl=pt-br) para acomodar um uso maior. O gasto total é agregado em todos os projetos vinculados que têm o serviço da API Gemini ativado. Quando o total acumulado da conta atinge o limite do nível, o serviço é pausado para todos os projetos vinculados a essa conta de faturamento até o início do próximo ciclo de faturamento (o primeiro dia de cada mês).

#### Avaliar os gastos da sua conta de faturamento

Para avaliar seus gastos mensais históricos e determinar se os novos [limites de gastos por nível da conta de faturamento](#tier-spend-caps) vão afetar seus projetos em andamento, siga estas etapas:

1. No console do Google Cloud, acesse a página [Relatórios da conta do Cloud Billing](https://console.cloud.google.com/billing/reports?hl=pt-br).
   - Se você tiver mais de uma conta de faturamento, escolha a conta do Cloud
     Billing que tem os relatórios de custo que você quer visualizar.
2. O relatório usa "Agrupar por serviço" como padrão no "Mês atual". Você vai encontrar **API Gemini** na coluna **Serviço** e o gasto total na coluna **Custo de uso** da tabela.
3. Para ver custos granulares limitados ao uso da API Gemini, defina o filtro **Agrupar por** para **SKU** e o filtro **Serviços** para **API Gemini**.
4. Ajuste o filtro **Período por data de uso** para o intervalo desejado e avalie seu gasto histórico em um período.

## Tempos de processamento

Os indicadores e atualizações de faturamento nem sempre acontecem em tempo real.

- **Uso de crédito**: os custos de uso geralmente são descontados do seu saldo em minutos.
- **Confirmação do pagamento**: embora a maioria dos pagamentos com cartão seja instantânea, algumas formas de pagamento (como transferências bancárias) podem levar vários dias para serem compensadas. Os serviços só são retomados ou atualizados após a confirmação oficial da compra de créditos.
- **Upgrades de nível**: após um pagamento bem-sucedido ou quando você atende aos [critérios de upgrade](#about-billing), os upgrades de nível geralmente são refletidos em até 10 minutos.
- **Gráficos de detalhamento do custo total**: os gráficos que mostram o detalhamento do custo total nas páginas [Faturamento](https://aistudio.google.com/billing?hl=pt-br) e [Gasto](https://aistudio.google.com/spend?hl=pt-br) podem levar até 24 horas para serem atualizados.

Leia os guias do Cloud Billing sobre [ciclo de cobrança](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=pt-br#delayed-billing) e [latências de transação](https://docs.cloud.google.com/billing/docs/how-to/view-history?hl=pt-br#missing-transactions) para saber mais sobre possíveis atrasos no faturamento.

## Reembolsos

Não é possível receber reembolsos em contas de faturamento **pré-pagas**, exceto ao mudar de tipo de conta.

**Quando uma conta pré-paga muda para o tipo pós-pago** (depois que você atende aos [critérios](#about-billing) e [faz upgrade manual](#postpay) da conta), a conta pré-paga é encerrada, e todos os créditos pré-pagos restantes são reembolsados automaticamente para a forma de pagamento registrada.

Se você [encerrar](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=pt-br#close-a-billing-account) sua conta pré-paga por qualquer motivo que não seja o upgrade para pós-paga, todos os créditos pré-pagos restantes serão perdidos.

Os créditos comprados expiram após um ano. Após o vencimento, os créditos são perdidos e não podem ser recuperados.

As contas **pós-pagamento** seguem a [política de reembolso do Google Cloud](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=pt-br#request_a_refund).

## Contas do Cloud Billing

A API Gemini usa [contas do Cloud Billing](https://cloud.google.com/billing/docs/concepts?hl=pt-br) para serviços de faturamento, que você pode [configurar diretamente no AI Studio](#setup-billing).
Use o AI Studio para acompanhar os gastos, entender os custos e fazer pagamentos.

Os níveis, os limites de taxa e os limites máximos da conta de faturamento são determinados no nível da conta de faturamento.

### Projetos e chaves de API

Todos os [projetos](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br#google-cloud-projects) vinculados a uma conta de faturamento do Cloud herdam o nível de uso e os limites de taxa e de conta associados. Se você [mudar um projeto](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=pt-br#change_the_billing_account_for_a_project)
de uma conta de faturamento para outra, o nível dele e, consequentemente, os limites de taxa e
os limites da conta vão mudar para o nível da nova conta de faturamento.

O gasto cumulativo (em todos os produtos do Google Cloud) e a idade da conta em todos os projetos vinculados a uma conta de faturamento contam para as [qualificações de nível](#about-billing) dessa conta.

É possível [desvincular um projeto](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=pt-br#disable_billing_for_a_project)
da conta de faturamento para voltar ao nível sem custo financeiro.

As [chaves de API](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br) são credenciais geradas em um projeto.
Elas não têm configurações de faturamento independentes. Elas herdam os limites de nível e o status de faturamento do projeto. O uso cumulativo de todas as chaves em um projeto conta para o limite de gastos desse projeto e o gasto total da conta de faturamento.

## Perguntas frequentes

As seções a seguir fornecem respostas para perguntas frequentes.

### Por que estou recebendo uma cobrança?

O preço da API Gemini é baseado no seguinte:

- Contagem de tokens de entrada
- Contagem de tokens de saída
- Contagem de tokens em cache
- Duração do armazenamento de tokens em cache

Para informações sobre preços, consulte a [página de preços](https://ai.google.dev/pricing?hl=pt-br).

### Onde posso ver minha cota?

Você pode conferir sua cota e os limites do sistema no [AI Studio](https://aistudio.google.com/usage?hl=pt-br).

### Como faço para mudar para um nível de limite de taxa mais alto ou solicitar mais cota?

Você vai receber mais cota automaticamente quando sua conta atingir os próximos [requisitos de nível](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pt-br#usage-tiers).

### Posso usar a API Gemini sem custo financeiro no EEE (incluindo a UE), no Reino Unido e na Suíça?

Sim, oferecemos o nível sem custo financeiro e o nível pago em [várias regiões](https://ai.google.dev/gemini-api/docs/available-regions?hl=pt-br).

### Se eu configurar o faturamento com a API Gemini, vou receber uma cobrança pelo uso do Google AI Studio?

O uso do AI Studio continua sem custos financeiros, a menos que os usuários vinculem uma chave de API paga para
acessar recursos pagos.
Depois de vincular uma chave de API paga como parte de um projeto pago no AI Studio, você vai receber uma cobrança pelo uso do AI Studio com essa chave. Você pode alternar entre projetos do nível pago e projetos do nível sem custo financeiro conforme necessário usando as respectivas chaves de API vinculadas a cada tipo.

### Se eu estiver no nível sem custo financeiro, como faço upgrade para níveis mais altos?

Para acessar níveis mais altos, configure o faturamento no seu projeto. Clique em [**Configurar
faturamento**](#setup-billing) no Google AI Studio. Isso vai orientar você na
seleção ou criação de uma conta do Cloud Billing. Se você precisar usar o modelo de faturamento pré-pago, o processo **Configurar faturamento** vai orientar você na criação da sua conta pré-paga vinculada à conta do Cloud Billing.

### Posso usar 1 milhão de tokens no nível sem custo financeiro?

O nível sem custos financeiros da API Gemini varia de acordo com o modelo selecionado. Por enquanto, você
pode testar a janela de contexto de 1 milhão de tokens das seguintes maneiras:

- No Google AI Studio
- Com planos sem custos financeiros para modelos selecionados
- Com planos pós-pagos

### Posso voltar para o nível sem custo financeiro depois de fazer upgrade para níveis mais altos (pagos)?

Para fazer downgrade para o nível sem custo financeiro, [desative o faturamento](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=pt-br#disable_billing_for_a_project)
em cada um dos projetos que você quer fazer downgrade.

### Como posso calcular o número de tokens que estou usando?

Use o método [`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=pt-br#count_tokens)
para contar o número de tokens. Consulte o [guia de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) para saber mais sobre eles.

### Se eu me inscrever na minha primeira conta do Cloud Billing pelo AI Studio, ainda vou receber um teste sem custo financeiro do Google Cloud?

Ao se inscrever na sua primeira conta do Cloud Billing, o [teste sem custo financeiro do Google Cloud](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=pt-br#free-trial) começa, e você recebe um [crédito de boas-vindas](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=pt-br#welcome-credits) de US $300.
No entanto, esses créditos não podem ser usados para pagar pelo uso do AI Studio. Você pode usar o crédito de boas-vindas para pagar por outros serviços qualificados no Google Cloud (observação: depois que esses créditos forem efetivados ou expirarem (em 90 dias), os custos de uso adicionais serão faturados automaticamente na sua forma de pagamento estabelecida).

### Posso usar meu crédito de boas-vindas do Google Cloud com a API Gemini?

Não, o [crédito de boas-vindas](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=pt-br#welcome-credits) do Google Cloud ou o crédito do teste sem custo financeiro não podem ser usados na API Gemini ou no AI Studio.

Se você recebeu um crédito de boas-vindas do Google Cloud antes de ele se tornar inelegível, poderá gastar os créditos restantes na API Gemini e no AI Studio até que eles expirem (após 90 dias).

### O teste sem custo financeiro do Google Cloud se aplica ao uso da API Gemini?

Não. A partir de março de 2026, os custos de uso da API Gemini serão especificamente excluídos do programa [Teste sem custos financeiros do Google Cloud de US$300](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=pt-br#free-trial).

### Como o faturamento é processado?

O faturamento da API Gemini é processado pelo sistema de [faturamento do Cloud](https://cloud.google.com/billing/docs/concepts?hl=pt-br). Saiba mais sobre a configuração de faturamento no produto do Cloud Billing na [documentação do Cloud Billing](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=pt-br).

### Sou cobrado por solicitações com falha?

Se a solicitação falhar com um erro 400 ou 500, não haverá cobrança pelos tokens usados. No entanto, a solicitação ainda será deduzida da sua cota.

### O `GetTokens` é faturado?

As solicitações para a API `GetTokens` não são faturadas e não são contabilizadas na cota de inferência.

### Como meus dados do Google AI Studio são tratados se eu tiver uma conta de API paga?

Consulte os [Termos de Serviço](https://ai.google.dev/gemini-api/terms?hl=pt-br#paid-services) para detalhes sobre como os dados são tratados quando o Cloud Billing está ativado (consulte "Como o Google usa seus dados" em "Serviços pagos"). Vale lembrar que seus comandos do Google AI Studio são tratados de acordo com os mesmos termos de "Serviços pagos", desde que pelo menos um projeto de API tenha o faturamento ativado. Para verificar isso, acesse a [página da chave de API Gemini](https://aistudio.google.com/api-keys?hl=pt-br) e confira se há projetos marcados como "Pago" em "Plano".

### O que é o faturamento pré-pago e quem precisa usar esse modelo?

Com o faturamento pré-pago, os usuários da API Gemini no AI Studio podem comprar créditos na pré-venda.
A partir de 23 de março de 2026, os novos usuários do AI Studio talvez precisem usar o plano de faturamento pré-pago. Durante o processo de [Configurar faturamento](#setup-billing) do AI Studio, a interface vai orientar você pelo fluxo de configuração de faturamento e indicar se é necessário fazer um pré-pagamento.

### Como faço para comprar créditos de pré-pagamento? Há um valor mínimo ou máximo?

Você pode [comprar créditos](#buy-credits) na página de faturamento do AI Studio. Durante o processo de compra, a interface vai mostrar o valor mínimo de pré-compra necessário para sua região e nível, além de um valor máximo que pode estar na sua conta de uma só vez.

### Posso configurar minha conta pré-paga para comprar mais créditos automaticamente conforme necessário?

Sim, recomendamos que você configure a [recarga automática](#auto-reload) nas configurações de faturamento do AI Studio. Você especifica um saldo de crédito de "gatilho" (por exemplo, "quando meu saldo ficar abaixo de R $30") e um "valor de recarga" (por exemplo, "adicionar R $100").

### Posso receber um reembolso pelos meus créditos não utilizados?

Todos os créditos de API pré-pagos expiram após um ano e não podem ser reembolsados. Leia a [política de reembolso para contas pré-pagas](#refunds).

### Meus créditos pré-pagos expiram?

Sim, os créditos expiram 12 meses após a data da compra.

### O que acontece quando meu saldo de crédito pré-pago chega a R $0?

Todos os serviços da API Gemini em todos os projetos pagos por essa conta pré-paga do Cloud Billing serão interrompidos imediatamente para evitar mais cobranças. Seus projetos
não vão passar automaticamente para o nível sem custo financeiro.

Para restaurar o serviço no seu nível pago atual, [compre mais créditos](#buy-credits). Depois de comprar créditos, você poderá usar a API Gemini. Pode haver um [atraso](#processing-times) enquanto nossos sistemas são atualizados para refletir seu saldo de crédito.

Opcionalmente, para fazer downgrade para o nível sem custo financeiro, você pode [desativar o faturamento](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=pt-br#disable_billing_for_a_project)
nos projetos em que você quer fazer downgrade.

### Por que meu uso parou mesmo com um saldo de crédito pré-pago maior que R $0?

Talvez você tenha atingido o [limite de uso](#tier-spend-caps) do seu nível atual.
Os limites de uso aumentam automaticamente à medida que você avança para níveis mais altos. O uso da API Gemini no AI Studio também pode ser afetado pelo [status da sua conta do Cloud Billing](#missed-payment).

### Por que o saldo de crédito da minha conta pré-paga está negativo?

Devido à complexidade dos nossos sistemas de faturamento e processamento, pode haver [atrasos](#processing-times) na nossa capacidade de interromper o uso depois que você consumir todos os seus créditos. Esse uso em excesso pode aparecer como um saldo de crédito negativo no painel de faturamento do AI Studio. Se isso acontecer, o serviço será pausado, e o saldo negativo será deduzido da sua próxima compra de crédito.

Para evitar uma pausa no serviço da API Gemini, recomendamos configurar a [recarga automática](#auto-reload) para comprar mais créditos automaticamente quando o saldo ficar abaixo de um valor especificado.

### Posso usar meus créditos pré-pagos em outros serviços do Google Cloud, como a Gemini Enterprise Agent Platform?

Não, os créditos de pré-pagamento são estritamente vinculados ao uso da API Gemini. Qualquer
outro serviço do Google Cloud que você usar (Compute, Storage, Gemini Enterprise Agent Platform) será cobrado usando
o [ciclo de cobrança do Cloud](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=pt-br) padrão.

### Posso mudar para um plano de faturamento pós-pago?

Quando você estabelece um histórico de pagamentos e [atinge um nível qualificado](#about-billing) para o plano de faturamento pós-pago, é possível transferir todos os custos futuros de uso da API Gemini para um [ciclo de cobrança pós-pago](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=pt-br#view-your-charging-cycle) padrão e consolidado do Google Cloud.

### O que acontece com meus créditos pré-pagos se eu mudar para o pós-pago?

Ao fazer upgrade para o [pós-pagamento](#postpay), o Cloud Billing encerra sua conta para pagamentos pré-paga, desativa a [recarga automática](#auto-reload) e reembolsa automaticamente os créditos pré-pagos não utilizados (sujeito ao tempo padrão de processamento de reembolso).

### Onde posso ver meu saldo de crédito pré-pago e histórico de transações?

Todo o gerenciamento de saldo e o histórico de transações da API Gemini precisam ser feitos diretamente na guia "Faturamento" do Google AI Studio.

### Por que aparece a mensagem "O tipo de conta de faturamento está inativo ou não é compatível"?

As interações de pagamentos na [página de faturamento do AI Studio](https://aistudio.google.com/billing?hl=pt-br) podem ser bloqueadas e substituídas pela mensagem "O tipo de conta de faturamento está inativo ou não é compatível" se o tipo ou status da conta de faturamento selecionada não for qualificado para o nível pago do AI Studio.

Verifique o [Console do Cloud](https://console.cloud.google.com/billing/?hl=pt-br) para conferir o status da sua conta de faturamento. Um tipo inelegível pode ser *Conta de teste sem custo financeiro*. Nesse caso, [ative o faturamento](#setup-billing) no AI Studio para se qualificar. Um estado inativo pode ser *Encerrado*. Nesse caso, é possível [reabrir a conta](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=pt-br).

### Os custos de uso da API Gemini vão aparecer no console do Google Cloud?

Sim, os custos da API Gemini, assim como os custos associados a outros serviços do Google Cloud pagos pela sua conta do Cloud Billing, podem ser consultados nas [páginas de gerenciamento de custos](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle?hl=pt-br#cost-reports) no [console do Cloud Billing](https://console.cloud.google.com/billing?hl=pt-br). Observação: só é possível gerenciar seu saldo de crédito pré-pago no AI Studio.

### Por que meu uso da API Gemini não aparece no console do Cloud Billing, mas aparece no faturamento do AI Studio, junto com o consumo dos meus créditos?

O Google Cloud e o AI Studio informam dados de uso ao Cloud Billing em intervalos variados. Devido à complexidade dos nossos sistemas de faturamento e processamento, pode haver um atraso entre o uso dos serviços e a disponibilização do uso e dos custos para visualização no Cloud Billing. Normalmente, os detalhes de custo ficam disponíveis em um dia, mas às vezes podem demorar mais de 24 horas.
Saiba mais sobre o faturamento atrasado na [documentação do Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=pt-br#delayed-billing).

### Se eu usar outros serviços do Google Cloud com custos sujeitos a um ciclo de cobrança pós-pago, o que acontece se eu não fizer um pagamento?

Se você não pagar por outros serviços do Google Cloud, seu acesso à API Gemini
no AI Studio poderá ser suspenso, **independente de quantos créditos pré-pagos você tiver
disponíveis**. O uso do AI Studio é feito por uma conta do Cloud Billing do Google Cloud, que pode compartilhar o faturamento pré-pago do AI Studio e o pós-pago de outros serviços do Cloud. Um problema com seu saldo pós-pago interrompe todos os serviços vinculados a essa
conta. O uso da API Gemini será suspenso se sua conta do Cloud Billing for sinalizada por problemas como:

- Um saldo em atraso ou vencido
- Um pagamento recusado
- Uma forma de pagamento inválida ou expirada

Para restaurar o serviço, [resolva o problema da conta pós-paga](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=pt-br#resolving-declined-payments) no console do Google Cloud Billing. Depois de resolver o problema, você vai recuperar o acesso aos seus créditos e serviços pré-pagos da API Gemini.

### Onde posso receber ajuda com o faturamento?

Para receber ajuda com o faturamento, consulte
[Receber suporte do Cloud Billing](https://cloud.google.com/support/billing?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-29 UTC."],[],[]]
