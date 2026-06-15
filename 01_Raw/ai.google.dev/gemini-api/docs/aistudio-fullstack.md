---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=pt-BR
fetched_at: 2026-06-15T06:28:56.866048+00:00
title: "Desenvolver apps full-stack no Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Desenvolver apps full-stack no Google AI Studio

O Google AI Studio agora oferece suporte a desenvolvimento full stack, permitindo que você crie
aplicativos que vão além dos protótipos do lado do cliente. Com um
tempo de execução do lado do servidor, é possível gerenciar secrets, se conectar a APIs externas e criar
experiências multiplayer em tempo real.

## Tempo de execução do lado do servidor

Os aplicativos do Google AI Studio agora podem incluir um componente do lado do servidor (Node.js).
Isso permite que você:

- **Executar lógica do lado do servidor**: execute código que não deve ser exposto ao
  cliente.
- **Acessar pacotes npm**: o [Antigravity Agent](https://antigravity.google/docs/agent?hl=pt-br)
  pode instalar e usar pacotes do vasto ecossistema npm.
- **Processar secrets**: use chaves de API e credenciais com segurança.

### Usar pacotes npm

Não é necessário executar `npm install` manualmente. Basta pedir ao agente para adicionar
funcionalidades que exigem um pacote, e ele vai cuidar da instalação e da
importação.

**Exemplo**: > "Use `axios` para buscar dados da API externa."

## Gerenciar secrets com segurança

Com o código do lado do servidor e o gerenciamento de secrets, agora é possível criar apps que
interagem com o mundo.

### Chave da API Gemini

Quando você cria um novo app que usa a API Gemini, o AI Studio configura automaticamente seu `GEMINI_API_KEY` como um segredo do lado do servidor. Não é necessário fazer nenhuma configuração manual. É possível conferir essa chave no painel **Secrets**, em "Configurações". As chamadas da API Gemini do seu
app são feitas com código do lado do servidor usando essa chave, então
ela nunca é exposta no navegador.

### Chaves de API de terceiros

Para outros serviços, é possível adicionar chaves de API manualmente:

- **APIs de terceiros**: conecte-se a serviços como Stripe, SendGrid ou APIs REST personalizadas.
- **Bancos de dados**: conecte-se a bancos de dados externos (por exemplo, via Supabase, Firebase ou MongoDB Atlas) para manter os dados além da sessão.

Ao criar apps para o mundo real, muitas vezes é necessário se conectar a serviços de terceiros (como Twilio, Slack ou bancos de dados) que exigem chaves de API. É possível adicionar chaves manualmente seguindo estas etapas:

1. **Adicionar um secret**: acesse o menu **Configurações** no Google AI Studio e procure a seção "Secrets".
2. **Armazene sua chave**: adicione suas chaves de API ou tokens secretos aqui.
3. **Acesso no código**: o agente pode gravar um código do lado do servidor que acessa esses
   segredos com segurança (normalmente por variáveis de ambiente), garantindo que eles
   nunca sejam expostos ao navegador do lado do cliente.

Quando necessário, o agente também vai mostrar um card no chat pedindo para você adicionar chaves sempre que um novo segredo for necessário ou quando uma nova chave for detectada nas variáveis de ambiente do projeto.

### Integração do Firebase para banco de dados e autenticação

Agora, o Google AI Studio facilita a adição de um banco de dados ou autenticação ao seu
app usando uma
[integração do Firebase](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=pt-br).
O agente Antigravity pode provisionar e configurar automaticamente os seguintes serviços para você:

- **Banco de dados do Firestore**: um banco de dados de nuvem NoSQL flexível e escalonável para armazenar
  e sincronizar dados para desenvolvimento do lado do cliente e do lado do servidor.
- **Firebase Authentication**: permite que os usuários façam login com segurança no seu
  aplicativo usando fluxos de "Login do Google".

Basta pedir ao agente para "adicionar um banco de dados ao meu app" ou "configurar o Google Sign-In" que ele vai cuidar da configuração e da geração de código necessárias.

Com o Firebase, você pode começar sem custos financeiros e, se quiser, aumentar a escala com uma conta paga
quando estiver pronto para mais cota ou para usar recursos pagos.

## APIs do Google Workspace

Com o Google AI Studio, você cria apps que se conectam às APIs do Google Workspace para que os usuários trabalhem com dados reais: e-mails, planilhas, documentos, eventos da agenda e muito mais, tudo no seu app. Não é mais necessário configurar um projeto na nuvem do Google, configurar o OAuth ou gerenciar a API manualmente.

### Como funciona

Você pode adicionar uma integração do Workspace de duas maneiras:

- **Descreva no painel de chat**: basta dizer ao agente o que você quer no painel de chat na parte de baixo. Por exemplo, *"Crie um rastreador de despesas que registre recibos na minha Planilha Google"* ou *"Crie um painel que resuma minhas mensagens não lidas do Gmail"*.
- **Selecionar no painel de integrações**: abra o painel **Integrações** na barra lateral direita do modo de criação e ative o app do Workspace que você quer conectar.

Quando você adiciona um app do Workspace, o AI Studio automaticamente:

1. Conecta a API do Google necessária para seu app.
2. Gera o código do lado do servidor para chamar a API.
3. Adiciona um fluxo seguro de "Fazer login com o Google" para que os usuários finais do seu app possam
   autorizar o acesso aos próprios dados.

### Apps com suporte

Os seguintes apps do Google Workspace estão disponíveis:

| App | O que você pode criar |
| --- | --- |
| Google Agenda | Ler, criar e gerenciar eventos e agendas |
| Google Chat | Ler e interagir com conversas e espaços em grupo |
| Google Docs | Criar, ler, atualizar e formatar documentos |
| Google Drive | Organizar, pesquisar e gerenciar arquivos e pastas |
| Formulários Google | Criar pesquisas, atualizar perguntas e recuperar respostas |
| Gmail | Ler, enviar e gerenciar conteúdo de e-mail |
| Google Keep | Gerenciar notas, listas e anexos |
| Google Meet | Agendar e gerenciar videochamadas |
| Contatos | Sincronizar e gerenciar contatos |
| Google Planilhas | Ler, gravar e formatar dados de planilhas |
| Google Slides | Criar e modificar apresentações |
| Google Tarefas | Criar, gerenciar e organizar tarefas |

### Autenticação e permissões

Como criador, você não precisa configurar clientes OAuth, gerenciar credenciais ou configurar um projeto na nuvem do Google. O AI Studio faz tudo isso para você.

Os apps com APIs do Workspace integradas usam a opção "Fazer login com o Google" para autenticar
usuários finais. Quando um usuário abre seu app, ele é solicitado a fazer login e conceder
as permissões específicas de que o app precisa (por exemplo, acesso somente leitura ao
calendário ou a capacidade de editar uma planilha). O app só acessa os dados da pessoa que o está usando. Cada usuário autoriza o acesso à própria conta.

### Exemplos de comandos

Confira algumas ideias para começar a usar as integrações do Workspace:

- *"Crie um app que leia meu Google Agenda e rascunhe e-mails de preparação no
  Gmail para cada reunião."*
- *"Crie uma ferramenta que pegue um documento Google e gere uma apresentação de resumo de cinco slides nas Apresentações Google."*
- *"Crie um rastreador de despesas em que eu envie um recibo, o Gemini extraia os detalhes e registre uma nova linha na minha planilha Google."*

### Configurar o OAuth

Um caso de uso importante para o gerenciamento de secrets é configurar o OAuth para se conectar a outros sites ou apps. Quando o comando incluir instruções sobre como se conectar a um
app de terceiros que exige autenticação OAuth, o agente vai fornecer
instruções sobre como configurar o OAuth para esse aplicativo. Estas instruções
incluem os URLs de callback necessários para configurar seu aplicativo OAuth.
Você também pode encontrar os URLs de callback em **Integrações** no painel "Configurações".

## Crie experiências multiplayer

O ambiente de execução full-stack ativa recursos de colaboração em tempo real.

- **Estado em tempo real**: você pode pedir ao agente para criar recursos como "um chat ao vivo", "uma lousa colaborativa" ou "um jogo multijogador".
- **Sessões sincronizadas**: o servidor gerencia o estado, permitindo que vários usuários interajam com a mesma instância do aplicativo em tempo real.

**Exemplo de comando**: > "Transforme isso em um jogo multiplayer em que os jogadores possam ver os cursores uns dos outros".

### Dicas para testar apps multiplayer

Você pode testar o modo multiplayer de duas maneiras antes de implantar o app.

1. Abra o app no modo de criação do Google AI Studio em várias guias. Ao
   desenvolver no modo de build, seu app fica em um contêiner de desenvolvimento. Abrir o app em várias guias permite simular vários jogadores usando o app.
2. Compartilhe o app com outras pessoas usando o menu **Compartilhar** no canto superior direito.
   Em seguida, use o **URL compartilhado** na guia **Integrações**
   do menu **Compartilhar** para usar o app com os jogadores que receberam
   o compartilhamento.

## Práticas recomendadas

- **Chamadas da API Gemini**: seu `GEMINI_API_KEY` é configurado automaticamente como um
  segredo do lado do servidor. Faça chamadas da API Gemini no seu código do lado do servidor usando
  essa chave. Ele pode ser acessado no painel **Secrets**.
- **Segurança de secrets**: sempre use o gerenciador de secrets para chaves sensíveis.
  Nunca codifique essas informações nos seus arquivos.
- **Separação de responsabilidades**: mantenha a lógica da interface no framework do lado do cliente (React/Angular) e a lógica de negócios/processamento de dados no lado do servidor.
- **Tratamento de erros**: verifique se o código do lado do servidor processa erros de maneira robusta
  de chamadas de API externas para evitar falhas no app.

## A seguir

- [Criar apps no Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=pt-br)
- [Como implantar pelo Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pt-br)
- [App Gallery](https://aistudio.google.com/apps?source=showcase&hl=pt-br)

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-19 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-19 UTC."],[],[]]
