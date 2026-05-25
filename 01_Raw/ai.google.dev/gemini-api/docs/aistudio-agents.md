---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=pt-BR
fetched_at: 2026-05-25T05:21:00.575242+00:00
title: "Agentes no playground do AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Agentes no playground do AI Studio

O ambiente de testes do Google AI Studio oferece uma interface visual para criar protótipos e aprender a criar agentes gerenciados sem precisar criar e escrever chamadas de API.

Para começar, acesse a guia **Ambiente de testes** no painel de navegação do Google AI Studio e ative a opção **Agentes**.

## Modelos pré-criados

A guia **Agentes** tem uma série de modelos que pré-configuram o agente Antigravity definindo configurações de ferramentas e ambiente. Todos os modelos são de código aberto e publicados no
repositório [google-gemini/gemini-managed-agents-templates](https://github.com/google-gemini/gemini-managed-agents-templates/). Explorar esses modelos é uma ótima maneira de aprender a criar e estruturar seu próprio agente gerenciado.

Por exemplo, ao escolher o modelo de rádio de IA, todas as ferramentas permitidas são ativadas e um arquivo `AGENTS.md` especializado e habilidades para produção de programas de rádio são vinculados. Você pode conferir essas configurações na interface do ambiente de testes na seção **Ambiente** clicando no botão **Fontes**.

## Configuração da ferramenta

Nas configurações do agente no ambiente de testes, é possível ativar ou desativar o acesso às seguintes ferramentas integradas:

- **Pesquisa Google**:acesse a Web aberta para informações em tempo real.
- **Contexto de URL**:busque e analise o conteúdo de texto de URLs de páginas da Web específicas.
- **Execução de código**:execute comandos Bash e Python diretamente no ambiente de sandbox isolado.
- **Ferramentas do sistema de arquivos**:leia, grave, liste e exclua arquivos no espaço de trabalho.

## Configuração do ambiente

Os agentes gerenciados são executados em um sandbox Linux seguro e efêmero (o ambiente) que fornece o espaço de trabalho e as ferramentas necessárias para operar. Para saber mais, consulte o guia do ambiente de agentes gerenciados [gerenciados](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br).

### Como controlar o comportamento do agente

O comportamento, a personalidade e os recursos do agente são determinados principalmente pelos arquivos presentes no ambiente dele. O agente detecta e carrega automaticamente as configurações de uma pasta `.agents` especial:

- **`AGENTS.md`**: pré-carregado no contexto do agente para definir instruções e personalidade do sistema.
- **`SKILL.md`**: localizado nas pastas de habilidades respectivas (por exemplo, `.agents/skills/my-skill/SKILL.md`) para definir recursos e fluxos de trabalho específicos.

### Como provisionar o ambiente

É possível configurar o ambiente a ser usado pelo agente montando arquivos nele antes de iniciar uma sessão. Você pode criar um novo ambiente montando fontes ou restaurar um anterior:

- **Para criar um novo ambiente**, clique em **Adicionar fontes** no painel de configurações do ambiente e escolha entre os seguintes tipos de origem:

| Tipo de origem | Descrição | Caminho de montagem |
| --- | --- | --- |
| **Arquivos inline** | Escreva ou cole arquivos de configuração, conjuntos de dados de simulação ou scripts de utilitários (até 100 KB) diretamente na interface do ambiente de testes. | Caminho de destino definido pelo usuário (por exemplo, `/workspace/scripts/parser.py`). |
| **Google Cloud Storage** | Monte um bucket público ou privado do Cloud Storage.  Os buckets particulares exigem um token do portador OAuth 2.0 padrão. Para mais informações, consulte [Fontes particulares](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br#private-sources). | Mapeia um caminho de bucket do GCS (por exemplo, `gs://your-bucket-name/data/`) para um diretório do espaço de trabalho (por exemplo, `/workspace/data/`). |
| **Repositórios do GitHub** | Clone bases de código públicas ou privadas.  Os repositórios particulares exigem autenticação básica com seu token de acesso pessoal (PAT) do GitHub. Para mais informações, consulte [Fontes particulares](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br#private-sources). | Clonado diretamente em `/workspace/` (normalmente em `/workspace/<repo-name>`). |

- **Para restaurar um ambiente anterior**, você pode [reutilizar um ID de ambiente existente](#reusing-an-existing-environment-id) para clonar e ramificar o estado exato dele.

### Como reutilizar um ID de ambiente existente

Se você já dedicou tempo à configuração de um ambiente de sandbox, não precisa começar do zero. Para usar um ambiente existente:

1. Acesse o painel "Ambientes" no AI Studio e ative a opção **Tipo** para **Existente**.
2. Insira o **ID do ambiente** (por exemplo, `env_abc123`).

Para mais informações, consulte [Configurar um ambiente](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pt-br#configure-an-environment). Também é possível recuperar o ID do ambiente da sessão atual na guia "Ambiente" da interface.

Depois de enviar sua primeira mensagem ao agente, a configuração do ambiente será corrigida para essa sessão. Não é possível montar novas fontes ou modificar a lista de permissões de rede enquanto a interação estiver em execução.

## Fazer o download do ambiente

Depois que um ambiente é criado, é possível fazer o download do snapshot dele a qualquer momento usando o botão **Fazer o download** nas configurações do ambiente de testes do AI Studio para recuperar arquivos de ambiente como um arquivo tar.

## Segurança e gerenciamento de custos

### Como gerenciar o consumo de tokens

Ao contrário de uma solicitação de chat padrão que produz uma única saída, o agente Antigravity executa um fluxo de trabalho autônomo. Ele planeja, executa o código, observa os resultados e itera. Isso significa que um único comando pode resultar em um consumo ilimitado de tokens.

Para gerenciar os custos, **forneça critérios de encerramento claros nos comandos e limite as tarefas para o agente**. Um bom exemplo pode ser um comando como *Analise a solicitação de pull e pare depois de gerar o resumo do Markdown.
Não tente escrever a correção por conta própria*.

### Custos adicionais

Por padrão, todos os modelos de agente no ambiente de testes têm acesso ao serviço da API Gemini e podem fazer chamadas de API do ambiente para atender às solicitações. Isso pode gerar custos adicionais que não serão refletidos no consumo de tokens.

Da mesma forma, se você adicionar outros serviços externos, o agente poderá gerar custos adicionais chamando esses serviços em seu nome.

### Lista de permissões de rede

Por padrão, no AI Studio, todas as solicitações de rede de saída do ambiente de sandbox do agente são controladas e restritas para garantir a segurança. Para conceder ao agente a capacidade de acessar APIs externas, serviços da Web ou gerenciadores de pacotes, é necessário declará-los explicitamente:

1. Acesse o painel "Ambientes" no AI Studio.
2. Selecione o botão **regras** ao lado de **Rede**.
3. No painel **Configuração de rede**, clique em **Adicionar à lista de permissões** e preencha os detalhes relevantes:
   - **Restrição de domínio**:somente os domínios específicos ou padrões curinga adicionados à lista podem ser acessados pela máquina virtual do agente. Por exemplo, é possível inserir domínios exatos como `api.github.com` ou padrões amplos como `*.googleapis.com`.
   - **Adicionar cabeçalho HTTP e injeção de token**:use a opção **Adicionar cabeçalho HTTP** para injetar com segurança as credenciais necessárias (como um token de API) para um domínio específico. Essas credenciais são transmitidas com segurança por um proxy de saída e nunca são expostas diretamente como texto bruto dentro do sandbox do agente.

Sempre tenha cuidado ao adicionar domínios à lista de permissões. Conceder acesso do agente a serviços autenticados significa que ele pode agir em seu nome, o que pode levar a ações não intencionais se não for monitorado com cuidado.

### Práticas recomendadas para credenciais

Se o fluxo de trabalho exigir que o agente seja autenticado com serviços externos, você será responsável por provisionar e definir o escopo dessas credenciais. Siga estas diretrizes para reduzir o risco:

- **Use credenciais de privilégio mínimo**:crie contas de serviço ou chaves de API com apenas as permissões necessárias para o agente. Evite transmitir credenciais com acesso amplo ou administrativo.
- **Prefira tokens de curta duração**:sempre que possível, use credenciais ou tokens com limite de tempo que expiram em vez de chaves de API de longa duração.
- **Suponha acesso total**:o agente pode usar qualquer credencial a que tiver acesso para concluir a tarefa que você atribuiu a ele. Forneça apenas credenciais cujo escopo completo de acesso você esteja disposto a conceder.
- **Gire as credenciais regularmente**:trate as credenciais compartilhadas com o agente da mesma forma que qualquer credencial programática; gire-as em uma programação regular.

### Como conectar ferramentas e APIs externas

É possível conectar ferramentas e APIs externas (como servidores do Protocolo de Contexto de Modelo / MCP) para ampliar os recursos do agente. Ao fazer isso:

- Conecte apenas ferramentas de fontes confiáveis. Uma ferramenta maliciosa ou mal escrita pode expor dados ou realizar ações não intencionais.
- Configure as ferramentas com as permissões mínimas necessárias para seu caso de uso. Se uma ferramenta oferece suporte ao modo somente leitura, prefira-o, a menos que as gravações sejam estritamente necessárias.
- Antes de conectar uma ferramenta a uma fonte de dados de produção, teste-a com dados de amostra ou sintéticos para verificar se o agente a usa conforme o esperado.

### Supervisão humana

Os agentes podem raciocinar, planejar e executar fluxos de trabalho com várias etapas com um alto grau de autonomia. Embora isso seja poderoso, também significa que você precisa aplicar a supervisão adequada, especialmente para tarefas que modificam dados ou interagem com sistemas externos.

Sempre verifique as saídas críticas, como código gerado, transformações de dados ou mudanças de configuração, antes de implantá-las.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-20 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-20 UTC."],[],[]]
