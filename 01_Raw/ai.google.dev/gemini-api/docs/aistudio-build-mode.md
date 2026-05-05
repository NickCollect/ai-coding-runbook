---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=pt-BR
fetched_at: 2026-05-05T19:45:28.118754+00:00
title: "Criar apps no Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Criar apps no Google AI Studio

Esta página descreve como usar o Google AI Studio para criar (ou "programar") e implantar rapidamente apps que testam os recursos mais recentes do Gemini, como
[o Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br) e a [API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br). O Google AI Studio agora oferece suporte a **ambientes de execução
full stack**, permitindo que você crie aplicativos robustos com lógica do lado do servidor,
gerenciamento seguro de secrets e suporte a pacotes npm, tudo usando comandos em linguagem natural.

## Primeiros passos

Comece a programar no [modo de criação](https://aistudio.google.com/apps?hl=pt-br) do Google AI Studio. Você pode começar a criar de algumas maneiras:

- **Comece com um comando**: no modo de criação, use a caixa de entrada para inserir uma
  descrição do que você quer criar. Selecione "Chips de IA" para adicionar recursos específicos, como geração de imagens ou dados do Google Maps, ao comando. Você pode até dizer o que quer usando o botão de fala para texto.
- **Botão "Estou com sorte"**: se você precisar de uma inspiração criativa, use o botão "Estou
  com sorte" e o Gemini vai gerar um comando com uma ideia de projeto
  para você começar.
- **Remixe um projeto da galeria**: abra um projeto na [Galeria
  de apps](https://aistudio.google.com/apps?source=showcase&hl=pt-br) e selecione **Copiar app**.

Depois de executar o comando, o código e os arquivos necessários serão gerados, com uma prévia em tempo real do seu app aparecendo no lado direito.

## O que é criado?

Quando você executa o comando, o AI Studio cria um aplicativo completo. Por padrão, ele cria um ambiente full stack que pode incluir:

- **Lado do cliente**: um front-end da Web (o React é o padrão).
- **Do lado do servidor**: um ambiente de execução do Node.js que permite chamadas de API seguras, conexões de banco de dados e uso de pacotes npm.

Para ver o código gerado, selecione a guia **Código** no painel de visualização à direita. O **agente Antigravity** gerencia de forma inteligente vários arquivos na sua pilha, garantindo que as mudanças sejam propagadas corretamente.

### O agente Antigravity

O **agente Antigravity** é a principal funcionalidade de IA no [Google
Antigravity](https://antigravity.google?hl=pt-br). Agora, os componentes principais do
harness do agente estão alimentando a experiência do modo de criação no Google AI Studio. Ele vai além da simples geração de código, mantendo o contexto de todo o projeto, gerenciando vários arquivos e entendendo instruções complexas para criar aplicativos full stack robustos.

As principais capacidades incluem:

- **Consciência de contexto**: mantém o contexto de comandos e estados de arquivos anteriores.
- **Gerenciamento de vários arquivos**: processa dependências em vários arquivos.
- **Execução verificada**: verifica atualizações de código para reduzir alucinações.

## Recursos full stack

O Google AI Studio libera o poder do ecossistema da Web moderna, permitindo que você crie mais do que apenas protótipos do lado do cliente.

- **Ambiente de execução e npm do lado do servidor**: use a vasta biblioteca de pacotes npm. O agente vai identificar e instalar automaticamente os pacotes necessários para seu app (por exemplo, bibliotecas específicas para visualização de dados ou clientes de API). Você também pode solicitar pacotes específicos, se quiser.
- **Gerenciamento de secrets**: armazene chaves de API e secrets com segurança no menu
  **Configurações**. Eles podem ser acessados no código do lado do servidor, mantendo-os protegidos contra exposição do lado do cliente.
- **Multiplayer**: crie experiências colaborativas em tempo real diretamente no
  AI Studio. O ambiente de execução do lado do servidor gerencia o estado e as conexões necessárias para que os usuários interajam.
- **Integração do Firebase**: provisione e configure automaticamente o Firebase,
  incluindo o banco de dados do Firestore (armazenamento de dados persistente) e
  a autenticação do Firebase (fluxos de login, especificamente "Fazer login com o Google").
  O agente processa todo o processo de configuração e até mesmo grava o código no seu app para esses serviços.

[Saiba mais sobre o desenvolvimento de apps full stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=pt-br)

## Continuar criando

Depois que o Google AI Studio gerar o código inicial do seu aplicativo, você poderá continuar refinando-o:

### Crie no Google AI Studio

- **Itere com o Gemini**: use o painel de chat no **modo de criação** para pedir ao Gemini
  que faça modificações, adicione novos recursos ou mude o estilo.
- **Edite o código diretamente**: abra a **guia Código** no painel de visualização para
  fazer edições em tempo real.

### Desenvolver externamente

Para fluxos de trabalho mais avançados, você pode exportar o código e trabalhar no ambiente preferido:

- **Faça o download e desenvolva localmente**: exporte o código gerado como um **arquivo
  ZIP** e importe-o para o editor de código.
- **Enviar para o GitHub**: integre o código aos processos de desenvolvimento e
  implantação atuais enviando-o para um **repositório do GitHub**.

## Principais recursos

O Google AI Studio inclui vários recursos para tornar o processo de criação intuitivo e visual:

- **Crie e itere em apps full stack**: crie apps full stack com apenas
  um comando e itere no chat ou no **modo de anotação**. O modo de anotação permite destacar qualquer parte da interface do app e descrever a mudança desejada.
- **Compartilhe e implante seu app**: você pode compartilhar suas criações com outras pessoas para
  colaborar ou mostrar seu trabalho. Quando o app estiver pronto, implante-o no Cloud Run.
- **Galeria de apps**: a galeria de apps oferece uma biblioteca visual de ideias de projetos.
  Você pode navegar pelo que é possível fazer com o Gemini, visualizar aplicativos instantaneamente e remixá-los para personalizá-los.

## Implantar ou arquivar o app

Quando o aplicativo estiver pronto, você poderá implantá-lo:

- **Google Cloud Run**: implante seu aplicativo como um serviço escalonável.
  Os preços do [Google Cloud Run](https://cloud.google.com/run?hl=pt-br) podem ser aplicados com base
  no uso.
- **GitHub**: exporte seu projeto para um repositório do GitHub.

## Limitações

Esta seção lista as limitações atuais do modo de criação no Google AI Studio.

### Segurança da chave de API

- **Lado do cliente**: nunca use chaves de API reais diretamente no código do lado do cliente.
- **Lado do servidor**: use o recurso de gerenciamento de secrets para processar chaves sensíveis
  com segurança no ambiente de execução do lado do servidor.

### Implantação fora do Google AI Studio

- Embora seja possível implantar seu app no Cloud Run para um URL público, essa configuração usará sua chave de API para todas as chamadas da API Gemini dos usuários.
  - Os apps JavaScript são executados no lado do cliente. Portanto, garanta que as chaves de API tenham apenas acesso mínimo para evitar vazamentos ou uso indevido de dados. Por exemplo, outras lojas de pesquisa de arquivos do mesmo projeto podem ser acessíveis aos usuários por esse mecanismo.
- Implantação externa segura: para executar um app com segurança fora do AI Studio (por exemplo, depois de fazer o download do arquivo ZIP), é necessário mover a lógica que usa a chave de API para um componente do lado do servidor para evitar a exposição da chave aos usuários finais. Isso não é necessário se você implantar usando o Cloud Run.
- Aviso de exposição de chaves: não é recomendável substituir o marcador de posição por uma chave de API real em um ambiente do lado do cliente, porque a chave ficará visível para qualquer usuário.

### Erro ao compartilhar apps

Se você compartilhar seu app e o usuário final encontrar um erro **403 Acesso restrito** ao usar o URL compartilhado, isso poderá ocorrer devido a um dos seguintes motivos:

- **Extensões do navegador**: extensões de privacidade, como o Privacy Badger, podem estar bloqueando o app. Desative a extensão para evitar o erro.
- **Problemas de build**: pode haver problemas com o código atual. Peça ao agente para "corrigir problemas de build com o código atual" e compartilhe o URL novamente.

## Perguntas frequentes

### O que é a criação no AI Studio?

A criação no AI Studio é uma plataforma projetada para levar você de um comando simples a um aplicativo com tecnologia de IA pronto para produção usando o Gemini. Descreva o que você quer criar com um comando, e o Gemini vai gerar um app para você. Você também pode explorar nossa galeria para ver o que é possível fazer com a API Gemini e remixar apps para personalizá-los.

### Por que a criação chama a API Gemini do código do lado do cliente?

Normalmente, a prática recomendada é chamar a API Gemini do lado do servidor para não expor a chave de API. No entanto, o AI Studio tem um proxy de API Gemini para chamadas do lado do cliente, que anexa a chave de API sem expô-la no código. Por enquanto, geramos chamadas do lado do cliente para usar esse proxy, já que ele simplifica o código e permite que você compartilhe seu app com outras pessoas sem precisar fornecer uma chave de API.

### Minha chave de API é exposta ao compartilhar apps?

Não use uma chave de API real no seu app. Use um valor de marcador de posição.
`process.env.GEMINI_API_KEY` é definido como um valor de marcador de posição que você pode usar.
Quando outro usuário usa seu app, o AI Studio faz o proxy das chamadas para a API Gemini, substituindo o valor do marcador de posição por *a chave de API do usuário* (não a sua).
Não use uma chave de API real no seu app, porque o código fica visível para qualquer pessoa que possa visualizar o app.

### Quem pode ver meus apps?

Por padrão, seu app é particular. Você pode compartilhar seu app com outros usuários para que eles possam usá-lo. Os usuários com quem você compartilha seu app podem ver o código e fazer um fork para fins próprios. Se você compartilhar seu app com permissão para edição, os outros usuários poderão editar o código do seu app.

### Posso executar apps fora do AI Studio?

Você pode implantar seu app no [Cloud Run](https://cloud.google.com/run?hl=pt-br)
pelo AI Studio, o que vai dar ao seu app um URL público. Ele é implantado com um servidor proxy que mantém sua chave de API privada. No entanto, o app implantado usará sua chave de API para todas as chamadas da API Gemini dos usuários. Você também pode fazer o download do app como um arquivo ZIP. Se você substituir o valor do marcador de posição por uma chave de API real, ele ainda vai funcionar. No entanto, *não* implante seu app dessa forma, porque qualquer usuário poderá ver a chave de API. Para
executar um app com segurança fora do AI Studio, é necessário
[mover algumas lógicas do lado do servidor](https://ai.google.dev/gemini-api/tutorials/web-app?lang=python&hl=pt-br),
para que a chave de API não seja mais exposta.

### Posso desenvolver apps localmente com minhas próprias ferramentas e compartilhá-los aqui?

Essa funcionalidade ainda não está disponível. Estamos animados para oferecer suporte a mais casos de uso de apps no futuro. Envie feedback se tiver algo específico em mente.

### Como posso usar um banco de dados ou outro armazenamento com meus apps?

Os apps do AI Studio são apps padrão executados em um contêiner do Cloud Run. Você pode usar qualquer solução de armazenamento a que possa se conectar por uma rede, desde que não haja um firewall que impeça o acesso de um intervalo de IP dinâmico.

Estamos trabalhando para adicionar suporte direto ao armazenamento no futuro, que você poderá configurar diretamente no AI Studio.

### Como posso acessar o microfone, a webcam e outras APIs do navegador?

Para garantir que os espectadores estejam cientes do uso da webcam ou de outros
dispositivos de um app, exigimos um reconhecimento extra antes que o app possa acessar
essas [APIs do navegador](https://developer.mozilla.org/en-US/docs/Web/API/Navigator).
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
recursos padrão [controlados por políticas](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md).

### Como posso usar o GitHub com meus apps?

A integração do GitHub do AI Studio permite criar um repositório para seu trabalho e confirmar as mudanças mais recentes. No momento, não oferecemos suporte ao pull de mudanças remotas.

### Posso conceder acesso de edição a outros usuários no meu app?

Isso ainda não é oferecido, mas será em breve.

### Por que meu app foi sinalizado por violação da política?

Temos sistemas que analisam automaticamente os apps para garantir que eles estejam em conformidade com nossas políticas. Se encontrarmos um app que viola nossas políticas, ele será removido do AI Studio. As violações de políticas podem incluir, entre outras:

- Apps que contêm malware, phishing ou falsificação de identidade
- Apps que mostram ou distribuem conteúdo que viola a política de imagens de abuso sexual infantil
- Apps que mostram ou distribuem conteúdo que viola a política de assédio
- Apps que mostram ou distribuem conteúdo que viola a política contra discurso de ódio
- Apps que mostram ou distribuem conteúdo que viola a política de tráfico humano
- Apps que mostram ou distribuem conteúdo que viola a política de conteúdo sexualmente explícito
- Apps que mostram ou distribuem conteúdo que viola a política de violência e imagens sangrentas
- Apps que mostram ou distribuem conteúdo que viola a política de conteúdo nocivo ou perigoso

Se o app foi sinalizado por uma violação da política e você acredita que isso ocorreu por engano, envie uma contestação. Violações recorrentes das nossas políticas podem resultar no encerramento do seu acesso ao AI Studio.

### Quais são minhas responsabilidades como desenvolvedor de apps?

Lembre-se de que, como proprietário do aplicativo, você é responsável pelo comportamento dele e por todos os dados que ele processa. Isso inclui:

- **Conformidade legal e direitos de terceiros**:garantir que seu app esteja em conformidade com todas as leis e regulamentações aplicáveis e não viole os direitos de outras pessoas, incluindo direitos de propriedade intelectual e direitos de privacidade.
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
se aplicam ao uso de apps apresentados na galeria de apps do AI Studio, a menos que
indicado de outra forma.

## A seguir

- [Desenvolvimento de apps full stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=pt-br)
- Confira exemplos na [galeria de apps](https://aistudio.google.com/apps?source=showcase&hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-04-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-04-29 UTC."],[],[]]
