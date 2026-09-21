---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=pt-BR
fetched_at: 2026-09-21T05:48:38.174402+00:00
title: "Criar apps no Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Criar apps no Google AI Studio

Esta página descreve como usar o Google AI Studio para criar (ou "programar") e implantar rapidamente apps que testam os recursos mais recentes do Gemini, como
[o Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br) e a [API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br). O Google AI Studio oferece suporte à criação de **apps da Web** com ambientes de execução full stack e **apps Android nativos** com Kotlin e Jetpack Compose, tudo isso usando comandos em linguagem natural.

## Primeiros passos

Comece a programar no [modo de criação](https://aistudio.google.com/apps?hl=pt-br) do Google AI Studio. Você pode começar a criar de algumas maneiras:

- **Comece com um comando**: no modo de criação, use a caixa de entrada para inserir uma
  descrição do que você quer criar. Selecione "Chips de IA" para adicionar recursos específicos, como geração de imagens ou dados do Google Maps, ao comando. Você pode até dizer o que quer usando o botão de fala para texto.
- **Botão "Estou com sorte"**: se você precisar de uma inspiração criativa, use o botão "Estou
  com sorte" e o Gemini vai gerar um comando com uma ideia de projeto
  para você começar.
- **Remixe um projeto da galeria**: abra um projeto na [Galeria
  de apps](https://aistudio.google.com/apps?source=showcase&hl=pt-br) e selecione **Copiar app**.
- **Importe um projeto do GitHub**: no modo de criação, selecione
  **Importar do GitHub** no menu **Adicionar arquivos** (ícone +) na caixa de entrada de comandos
  para importar seu código atual.

Depois de executar o comando, o código e os arquivos necessários serão gerados, com uma prévia em tempo real do seu app aparecendo no lado direito.

## O que é criado?

Quando você executa o comando, o AI Studio cria um aplicativo completo. É possível criar um **app da Web** ou um **app Android nativo** usando o seletor de plataforma.

Para **apps da Web** (padrão), o AI Studio cria um ambiente full stack que inclui:

- **Lado do cliente**: um front-end da Web (o React é o padrão).
- **Do lado do servidor**: um ambiente de execução do Node.js que permite chamadas de API seguras, conexões de banco de dados e uso de pacotes npm.

Para **apps Android**, o AI Studio gera um projeto Kotlin e Jetpack Compose que você pode visualizar em um emulador baseado em navegador, instalar em um dispositivo físico, e publicar na Google Play Store para testes. [Saiba mais sobre como criar apps Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=pt-br).

Para ver o código gerado, selecione a guia **Código** no painel de visualização à direita. O **agente do Antigravity** gerencia de forma inteligente vários arquivos na sua pilha, garantindo que as mudanças sejam propagadas corretamente.

### O agente do Antigravity

O **agente do Antigravity** é a principal funcionalidade de IA no [Google
Antigravity](https://antigravity.google?hl=pt-br). Agora, os componentes principais do
agente estão alimentando a experiência do modo de criação no Google AI Studio. Ele vai além da simples geração de código, mantendo o contexto de todo o projeto, gerenciando vários arquivos e entendendo instruções complexas para criar aplicativos full stack robustos.

As principais capacidades incluem:

- **Consciência de contexto**: mantém o contexto de comandos e estados de arquivo anteriores.
- **Gerenciamento de vários arquivos**: processa dependências em vários arquivos.
- **Execução verificada**: verifica atualizações de código para reduzir alucinações.

## Recursos full stack

O Google AI Studio libera o poder do ecossistema da Web moderna, permitindo que você crie mais do que apenas protótipos do lado do cliente.

- **Ambiente de execução e npm do lado do servidor**: use a vasta biblioteca de pacotes npm. O agente vai identificar e instalar automaticamente os pacotes necessários para seu app (por exemplo, bibliotecas específicas para visualização de dados ou clientes de API). Você também pode solicitar pacotes específicos, se quiser.
- **Gerenciamento de secrets**: armazene chaves de API e secrets com segurança no menu
  **Configurações**. Eles podem ser acessados no código do lado do servidor, mantendo-os protegidos contra exposição do lado do cliente.
- **Multiplayer**: crie experiências colaborativas em tempo real diretamente no
  AI Studio. O ambiente de execução do lado do servidor gerencia o estado e as conexões necessárias para que os usuários interajam.
- **Firebase Firestore e Authentication**: provisione e configure automaticamente o Firebase, incluindo o banco de dados do Firestore (armazenamento de dados persistente) e
  o Firebase Authentication (fluxos de login, especificamente "Fazer login com o
  Google"). O agente processa todo o processo de configuração e até mesmo grava o código no seu app para esses serviços.
- **Integrações do Google Workspace**: conecte seu app a APIs do Google Workspace, como Gmail, Planilhas, Documentos, Drive, Agenda e muito mais. O AI Studio processa toda a configuração do OAuth automaticamente.

[Saiba mais sobre como desenvolver apps full stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=pt-br)

### Apps Android

Você também pode criar apps Android nativos usando Kotlin e Jetpack Compose.
Visualize seu app em um Android Emulator baseado em navegador, instale-o em um dispositivo físico usando o adb no navegador e publique na Google Play Store para teste interno.

[Saiba mais sobre como criar apps Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=pt-br)

## Continuar criando

Depois que o Google AI Studio gerar o código inicial do seu aplicativo, você poderá continuar refinando-o:

### Crie no Google AI Studio

- **Itere com o Gemini**: use o painel de chat no **modo de criação** para pedir ao Gemini
  que faça modificações, adicione novos recursos ou mude o estilo.
- **Edite o código diretamente**: abra a **guia Código** no painel de visualização para
  fazer edições em tempo real.

### Desenvolver externamente

Para fluxos de trabalho mais avançados, você pode sincronizar ou exportar o código para trabalhar no ambiente de sua preferência:

- **Sincronizar com o GitHub**: conecte seu app a um repositório do GitHub para ativar a sincronização
  bidirecional. Você pode enviar mudanças solicitadas no AI Studio diretamente para seu repositório com mensagens de confirmação geradas por IA ou extrair mudanças feitas localmente no seu ambiente de desenvolvimento integrado ou por colegas de equipe de volta para o AI Studio. Gerencie o status de sincronização a qualquer momento na guia **GitHub** em "Configurações".
- **Fazer o download e desenvolver localmente**: exporte o código gerado como um **arquivo
  ZIP** e importe-o para o editor de código.

## Principais recursos

O Google AI Studio inclui vários recursos para tornar o processo de criação intuitivo e visual:

- **Crie e itere em apps full stack**: crie apps full stack com apenas
  um comando e itere no chat ou no **modo de anotação**. O modo de anotação permite destacar qualquer parte da interface do app e descrever a mudança desejada.
- **Compartilhe e implante seu app**: você pode compartilhar suas criações com outras pessoas para
  colaborar ou mostrar seu trabalho. Ao compartilhar, as chamadas de API são contabilizadas nos limites de uso. Se você usar modelos pagos, custos poderão ser aplicados. Quando o app estiver pronto, implante-o no Cloud Run.
- **Galeria de apps**: a galeria de apps oferece uma biblioteca visual de ideias de projetos.
  Você pode navegar pelo que é possível fazer com o Gemini, visualizar aplicativos instantaneamente e remixá-los para personalizá-los.

## Implantar ou arquivar seu app

Quando o aplicativo estiver pronto, você poderá implantá-lo:

- **Cloud Run**: implante seu aplicativo como um serviço escalonável.
  Os preços do [Google Cloud Run](https://cloud.google.com/run?hl=pt-br) podem ser aplicados com base
  no uso. Para saber mais sobre a implantação, consulte
  [Como implantar no Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pt-br).
- **GitHub**: sincronize seu projeto com um repositório do GitHub novo ou atual
  para gerenciar o código-fonte ou colaborar com colegas de equipe.

## Limitações

Esta seção lista as limitações atuais do modo de criação no Google AI Studio.

### Gerenciamento de chaves de API

Quando você cria um novo app que usa a API Gemini, o AI Studio configura automaticamente a chave da API Gemini como um secret no ambiente do lado do servidor do app.
Você pode visualizar e gerenciar essa chave no painel **Secrets**.

- **Configuração automática**: seu `GEMINI_API_KEY` é configurado para você. Nenhuma configuração manual
  é necessária para começar a criar.
- **Somente do lado do servidor**: as chaves de API são injetadas no ambiente de execução do lado do servidor e
  nunca são incluídas no código do lado do cliente.
- **Apps atuais**: para apps criados antes de 14 de maio de 2026, o agente vai
  fazer upgrade automático da integração da API Gemini para a abordagem recomendada
  do lado do servidor na próxima vez que você modificar os recursos do Gemini do app.

### Implantação fora do Google AI Studio

- **Cloud Run**: quando você implanta no Cloud Run pelo AI Studio, a chave de API é
  incluída com segurança no ambiente do lado do servidor. O app implantado vai usar sua chave de API para todas as chamadas da API Gemini dos usuários.
- **Download de ZIP**: se você fizer o download do app como um arquivo ZIP para executá-lo
  em outro lugar, será necessário configurar a variável de ambiente `GEMINI_API_KEY`
  no ambiente de hospedagem. Como as chamadas da API Gemini do seu app são feitas pelo código do lado do servidor, a chave não é exposta aos usuários finais.

### Erro ao compartilhar apps

Se você compartilhar seu app e o usuário final encontrar um erro **403 Acesso restrito** ao usar o URL compartilhado, isso poderá ser devido a um dos seguintes motivos:

- **Extensões do navegador**: extensões de privacidade, como o Privacy Badger, podem estar bloqueando o app. Desative a extensão para evitar o erro.
- **Problemas de build**: pode haver problemas com o código atual. Peça ao agente para "corrigir problemas de build com o código atual" e compartilhe o URL novamente.

## Perguntas frequentes

### O que é a criação no AI Studio?

A criação no AI Studio é uma plataforma projetada para levar você de um comando simples a um aplicativo com tecnologia de IA pronto para produção usando o Gemini. Descreva o que você quer criar com um comando, e o Gemini vai gerar um app para você. Você também pode explorar nossa galeria para ver o que é possível fazer com a API Gemini e remixar apps para personalizá-los.

### Como a criação processa minha chave da API Gemini?

Quando você cria um app que usa a API Gemini, o AI Studio configura automaticamente a chave da API Gemini como um secret do lado do servidor. As chamadas da API Gemini do seu app são feitas pelo código do lado do servidor usando essa chave, então ela nunca é exposta no navegador. Você pode ver sua chave de API no painel **Secrets** em "Configurações".

### Minha chave de API é exposta ao compartilhar apps?

Não. A chave de API é armazenada como um secret do lado do servidor e nunca é incluída no código do lado do cliente. Quando você compartilha seu app, outros usuários podem usá-lo, mas não podem ver sua chave de API.

Ao compartilhar seus apps com outras pessoas, as chamadas de API são contabilizadas nos limites de uso.
Se você usar modelos pagos, custos poderão ser aplicados. O AI Studio vai avisar durante a configuração e antes de você compartilhar se o app poderá gerar custos.

### Quem pode ver meus apps?

Por padrão, seu app é particular. Você pode compartilhar seu app com outros usuários para que eles possam usá-lo. Os usuários com quem você compartilha seu app podem ver o código e fazer um fork para os próprios fins. Se você compartilhar seu app com permissão de edição, os outros usuários poderão editar o código do seu app.

### Posso executar apps fora do AI Studio?

Sim. Você pode implantar seu app no
[Cloud Run](https://cloud.google.com/run?hl=pt-br) pelo AI Studio, o que
oferece ao app um URL público com a chave de API configurada com segurança no
ambiente do lado do servidor. Você também pode fazer o download do app como um arquivo ZIP e hospedá-lo em outro lugar. Será necessário definir a variável de ambiente `GEMINI_API_KEY` no ambiente de hospedagem. Como as chamadas da API Gemini são feitas pelo código do lado do servidor, a chave permanece segura.

Para saber mais sobre as opções de implantação, consulte [Como implantar no Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=pt-br).

### Posso desenvolver apps localmente com minhas próprias ferramentas e compartilhá-los aqui?

Sim. Você pode conectar seu app do AI Studio a um repositório do GitHub para desenvolver localmente usando o editor de código ou as ferramentas de CLI de sua preferência, enviar as mudanças para o GitHub e extrair essas atualizações diretamente para o AI Studio usando a guia **GitHub** em "Configurações".

### Como posso usar um banco de dados ou outro armazenamento com meus apps?

Os apps do AI Studio são apps padrão executados em um contêiner do Cloud Run. Você pode usar qualquer solução de armazenamento que possa se conectar a uma rede, desde que não haja um firewall impedindo o acesso de um intervalo de IP dinâmico.

Estamos trabalhando para adicionar suporte direto ao armazenamento no futuro, que poderá ser configurado diretamente no AI Studio.

### Como posso acessar o microfone, a webcam e outras APIs do navegador?

Para garantir que os espectadores estejam cientes do uso da webcam ou de outros
dispositivos por um app, exigimos um reconhecimento extra antes que o app possa acessar
estas [APIs do navegador](https://developer.mozilla.org/en-US/docs/Web/API/Navigator).
Os criadores de apps podem adicionar essas solicitações de permissão ao arquivo `metadata.json` do app. Exemplo:

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

Os valores aceitos para `requestFramePermissions` são um subconjunto dos
recursos padrão [controlados por política](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md).

### Como posso usar o GitHub com meus apps?

O AI Studio oferece suporte à sincronização bidirecional com o GitHub:

- **Importar um repositório**: no modo de criação, selecione **Importar do GitHub**
  no menu **Adicionar arquivos** (ícone +) na caixa de entrada de comandos para importar
  o código atual.
- **Vincular um repositório**: em "Configurações", abra a guia **GitHub** para criar um
  novo repositório do GitHub no seu app ou vincular a um já existente.
- **Sincronização bidirecional**: envie mudanças solicitadas no AI Studio diretamente para seu
  repositório com mensagens de confirmação geradas por IA ou extraia mudanças feitas
  externamente (como edições locais do ambiente de desenvolvimento integrado ou solicitações de envio de colegas de equipe) de volta para o AI
  Studio.
- **Resolver conflitos de mesclagem**: se as mudanças entrarem em conflito ao sincronizar com o
  GitHub, o AI Studio vai mostrar uma caixa de diálogo **Resolver conflitos** com um
  visualizador de diferenças lado a lado, permitindo que você analise as diferenças e escolha
  se quer manter a versão do AI Studio ou do GitHub para cada arquivo em conflito.

### Posso conceder acesso de edição a outros usuários no meu app?

O AI Studio não oferece suporte à edição colaborativa direta em tempo real.
No entanto, você pode colaborar com colegas de equipe vinculando seu app a um repositório compartilhado do GitHub. Os colegas de equipe podem enviar mudanças ou abrir solicitações de envio no GitHub, e você pode extrair essas atualizações para o AI Studio.

### Por que meu app foi sinalizado por violação da política?

Temos sistemas que analisam automaticamente os apps para garantir que eles obedeçam às nossas políticas. Se encontrarmos um app que viola nossas políticas, ele será removido do AI Studio. As violações de política podem incluir, entre outras:

- Apps que contêm malware, phishing ou falsificação de identidade
- Apps que mostram ou distribuem conteúdo que viola a política contra imagens de abuso sexual infantil
- Apps que mostram ou distribuem conteúdo que viola a política contra assédio
- Apps que mostram ou distribuem conteúdo que viola a política contra discurso de ódio
- Apps que mostram ou distribuem conteúdo que viola a política contra tráfico humano
- Apps que mostram ou distribuem conteúdo que viola a política contra conteúdo sexualmente explícito
- Apps que mostram ou distribuem conteúdo que viola a política contra violência e imagens sangrentas
- Apps que mostram ou distribuem conteúdo que viola a política contra conteúdo prejudicial ou perigoso

Se o app foi sinalizado por uma violação de política e você acredita que isso ocorreu por engano, envie uma contestação. Violações recorrentes das nossas políticas podem resultar no encerramento do seu acesso ao AI Studio.

### Quais são minhas responsabilidades como desenvolvedor de apps?

Como proprietário do aplicativo, você é responsável pelo comportamento dele e por todos os dados que ele processa. Isso inclui:

- **Conformidade legal e direitos de terceiros**:garantir que seu app obedeça a todas as leis e regulamentações aplicáveis e não viole os direitos de outras pessoas, incluindo direitos de propriedade intelectual e direitos de privacidade.
- **Monitoramento de conteúdo:** a conformidade com termos adicionais pode ser aplicada a
  outros serviços usados pelo seu app. Por exemplo,
  [os Termos de Serviço do Google Cloud](https://cloud.google.com/terms?hl=pt-br),
  aplicáveis ao Firestore, exigem que os clientes que hospedam conteúdo de terceiros
  publiquem políticas que definam o conteúdo proibido (por exemplo, conteúdo
  ilegal) e monitorem a presença desse conteúdo ilegal.
- **Implementação segura**:implementar as proteções e ferramentas de moderação necessárias para evitar o uso indevido do aplicativo.

Esteja ciente das [restrições de uso](https://ai.google.dev/gemini-api/terms?hl=pt-br#use-restrictions)
nos Termos de Serviço.

### Quais termos se aplicam aos apps na galeria de apps do AI Studio?

Os [Termos Adicionais de Serviço da API Gemini](https://ai.google.dev/gemini-api/terms?hl=pt-br)
se aplicam ao uso de apps apresentados na galeria de apps do AI Studio, salvo
indicação em contrário.

## A seguir

- [Desenvolvimento de apps full stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=pt-br) (Web)
- [Criar apps Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=pt-br)
- Confira exemplos na [galeria de apps](https://aistudio.google.com/apps?source=showcase&hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-11 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-11 UTC."],[],[]]
