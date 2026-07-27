---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/files?hl=pt-BR
fetched_at: 2026-07-27T04:33:57.389880+00:00
title: "API Files \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# API Files

O Gemini pode processar vários tipos de dados de entrada, incluindo texto, imagens e áudio, ao mesmo tempo.

Este guia mostra como trabalhar com arquivos de mídia usando a API Files. As operações básicas são as mesmas para arquivos de áudio, imagens, vídeos, documentos e outros tipos de arquivos compatíveis.

Para orientações sobre comandos de arquivo, consulte a seção [Guia de comandos de arquivo](https://ai.google.dev/gemini-api/docs/files?hl=pt-br#prompt-guide).

## Carregar um arquivo

Você pode usar a API Files para fazer upload de um arquivo de mídia. Sempre use a API Files quando o tamanho total da solicitação (incluindo arquivos, comando de texto, instruções do sistema etc.) for maior que 100 MB. Para arquivos PDF, o limite é de 50 MB.

O código a seguir faz upload de um arquivo e o usa em uma chamada para
`generateContent`.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=["Describe this audio clip", myfile]
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Describe this audio clip",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}
defer client.Files.Delete(ctx, file.Name)

resp, err := client.Models.GenerateContent(ctx, "gemini-3.5-flash", []*genai.Content{
  {
    Parts: []*genai.Part{
      genai.NewPartFromFile(*file),
      genai.NewPartFromText("Describe this audio clip"),
    },
  },
}, nil)

if err != nil {
    log.Fatal(err)
}

printResponse(resp)
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D "${tmp_header_file}" \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Receber metadados de um arquivo

Para verificar se a API armazenou o arquivo enviado e receber os metadados dele, chame `files.get`.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
file_name = myfile.name
myfile = client.files.get(name=file_name)
print(myfile)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const fileName = myfile.name;
  const fetchedFile = await ai.files.get({ name: fileName });
  console.log(fetchedFile);
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}

gotFile, err := client.Files.Get(ctx, file.Name)
if err != nil {
    log.Fatal(err)
}
fmt.Println("Got file:", gotFile.Name)
```

### REST

```
# file_info.json was created in the upload example
name=$(jq ".file.name" file_info.json)
# Get the file of interest to check state
curl https://generativelanguage.googleapis.com/v1beta/files/$name \
-H "x-goog-api-key: $GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq ".file.name" file_info.json)
echo name=$name
file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri
```

## Listar arquivos enviados

O código a seguir recebe uma lista de todos os arquivos enviados:

### Python

```
from google import genai

client = genai.Client()

print('My files:')
for f in client.files.list():
    print(' ', f.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const listResponse = await ai.files.list({ config: { pageSize: 10 } });
  for await (const file of listResponse) {
    console.log(file.name);
  }
}

await main();
```

### Go

```
for file, err := range client.Files.All(ctx) {
  if err != nil {
    log.Fatal(err)
  }
  fmt.Println(file.Name)
}
```

### REST

```
echo "My files: "

curl "https://generativelanguage.googleapis.com/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Excluir arquivos enviados

Os arquivos são excluídos automaticamente após 48 horas. Também é possível excluir manualmente um
arquivo enviado:

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
client.files.delete(name=myfile.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const fileName = myfile.name;
  await ai.files.delete({ name: fileName });
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}
client.Files.Delete(ctx, file.Name)
```

### REST

```
curl --request "DELETE" https://generativelanguage.googleapis.com/v1beta/files/$name \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Informações de uso

É possível usar a API Files para fazer upload e interagir com arquivos de mídia. Com a API Files, é possível armazenar até 20 GB de arquivos por projeto, com um tamanho máximo de 2 GB por arquivo. Os arquivos são armazenados por 48 horas. Durante esse período, você pode
usar a API para receber metadados sobre os arquivos, mas não é possível fazer o download deles.
A API Files está disponível sem custo financeiro em todas as regiões onde a API Gemini está disponível.

## Estratégias de solicitação de arquivos

Esta seção oferece orientações e práticas recomendadas para usar arquivos de mídia com
comandos para a API Gemini.

A capacidade de usar vários tipos de dados nos comandos oferece mais flexibilidade em termos de tarefas que podem ser realizadas com a API Gemini. Por
exemplo, você pode enviar para o modelo a foto de uma refeição deliciosa e pedir que ele escreva
um pequeno blog sobre ela.

|  |  |
| --- | --- |
| **Comando** | **Resposta** |
| Escreva uma postagem curta e interessante para o blog com base nessa foto. A foto deve incluir uma descrição da refeição e falar sobre a preparação das refeições.   Cookies | Preparar refeições é uma ótima maneira de economizar tempo e dinheiro, além de ajudar você a comer de forma mais saudável. Essa refeição é um ótimo exemplo de uma refeição saudável e deliciosa que pode ser preparada com antecedência.  Essa refeição inclui arroz integral, legumes assados e frango teriyaki. O arroz integral é um carboidrato saudável e complexo que vai dar energia sustentada. Os vegetais assados são uma ótima maneira de receber sua dose diária de vitaminas e minerais, e o frango teriyaki é uma opção deliciosa e rica em proteínas.  Além disso, ela é muito fácil de preparar. Basta cozinhar o arroz integral, assar os legumes e preparar o frango teriyaki. Depois de tudo cozido, divida em recipientes para marmita e guarde na geladeira. Assim, você pode pegar um recipiente e sair para trabalhar nas manhãs agitadas.  Se você quer uma refeição saudável e deliciosa que pode ser preparada com antecedência, essa é uma ótima opção. Ele é cheio de nutrientes e sabor, e vai deixar você satisfeito.  Que venham muitas refeições deliciosas e saudáveis! |

Se você estiver com problemas para receber a saída desejada de comandos que usam arquivos de mídia, há algumas estratégias que podem ajudar. As seções a seguir fornecem abordagens de design e dicas de solução de problemas para melhorar os comandos que usam entrada multimodal.

É possível melhorar os prompts multimodais seguindo estas práticas recomendadas:

- ### [Conceitos básicos do design de comandos](#specific-instructions)

  - **Seja específico nas instruções**: crie instruções claras e concisas que deixem pouco espaço para interpretações equivocadas.
  - **Adicione alguns exemplos ao comando**: use exemplos realistas de few-shot para ilustrar o que você quer alcançar.
  - **Detalhamento por etapas**: divida tarefas complexas em submetas gerenciáveis para guiar o modelo pelo processo.
  - **Especifique o formato de saída**: no comando, peça que a saída esteja no formato desejado, como markdown, JSON, HTML e muito mais.
  - **Coloque sua imagem em primeiro lugar nos comandos de imagem única**: o Gemini processa entradas de imagem e texto em qualquer ordem, mas para comandos com uma única imagem, o desempenho pode ser melhor se a imagem (ou vídeo) for colocada antes no comando de texto. No entanto, nos comandos que exigem que as imagens sejam altamente intercaladas com textos para fazer sentido, use a ordem mais natural.
- ### [Como solucionar problemas do comando multimodal](#troubleshooting)

  - **Se o modelo não estiver desenhando informações da parte relevante da imagem**: solte dicas com os aspectos da imagem de que você quer que o comando extraia informações.
  - **Se a saída do modelo for muito genérica (não personalizada o suficiente para a entrada de imagem/vídeo)**: no início do comando, peça para o modelo descrever as imagens ou o vídeo antes de fornecer a tarefa ou peça ao modelo para consultar o conteúdo da imagem.
  - **Para resolver problemas de qual parte falhou**: peça para o modelo descrever a imagem ou explicar o raciocínio para avaliar o entendimento inicial dele.
  - **Se o comando resultar em conteúdo alucinado**: diminua a configuração de temperatura ou peça ao modelo descrições mais curtas para diminuir a probabilidade de extrapolar detalhes.
  - **Ajuste os parâmetros de amostragem**: teste diferentes configurações de temperatura e as seleções de top-k para ajustar a criatividade do modelo.

### Especificar as instruções

As instruções têm mais sucesso quando são claras e detalhadas. Se você tiver uma saída específica em mente, é melhor incluir esse requisito no comando para garantir a saída desejada.

Para essa imagem de uma placa de aeroporto, pedir ao modelo apenas "descrever esta imagem" pode gerar uma descrição geral. Se você precisa que o modelo analise a hora e a cidade a partir da imagem, inclua essa solicitação diretamente no comando.

| Comando | Resposta do modelo |
| --- | --- |
| Descreva esta imagem. | A imagem mostra um painel de chegadas e partidas do aeroporto. |

| **Comando atualizado** | **Resposta aprimorada** |
| --- | --- |
| Horários de viagem Analise a hora e a cidade no quadro do aeroporto mostrado nesta imagem em uma lista. | - 10:50 Moscow - 11:05 Edimburgo - 11:05 Londres - 11:10 Bucareste - 11:30 Kiev - 11:35 Dublin - 11:45 Midlands Orientais - 12:15 Sófia - 12:30 Londres - 12:30 Newcastle - 12:40 São Petersburgo - 12:40 Londres - 12:45 Manchester |

### Adicionar alguns exemplos

O modelo Gemini pode aceitar várias entradas que podem ser usadas como exemplos para entender a
saída que você quer. Adicionar esses exemplos pode ajudar o modelo a identificar os padrões e aplicar a relação entre as imagens fornecidas e as respostas ao novo exemplo. Isso também é chamado de aprendizado "few-shot".

No exemplo abaixo, a saída inicial é escrita na forma de frase e também contém o país (Brasil). Suponha que você queira a saída em um formato ou estilo diferente e queira
apenas a cidade, não o país. Adicionar alguns exemplos ao comando pode fazer com que o modelo responda da maneira desejada.

| **Comando** | **Resposta do modelo** |
| --- | --- |
| Horários de viagem Determine a cidade junto com o ponto de referência. | O ponto turístico é a estátua do Cristo Redentor no Rio de Janeiro, Brasil. |

| **Comando atualizado** | **Resposta aprimorada** |
| --- | --- |
| Determine a cidade junto com o ponto de referência. coliseu | cidade: Roma, ponto de referência: o Coliseu. |
| Cidade Proibida | cidade: Pequim, ponto de referência: Cidade Proibida |
| Cidade Proibida | cidade: Rio de Janeiro, ponto de referência: estátua do Cristo Redentor |

### Detalhar por etapas

Para tarefas complexas, como as que exigem compreensão e raciocínio visual, pode ser útil dividir a tarefa em etapas menores e mais diretas. Também poderia ser eficaz se você
pedisse diretamente ao modelo para “pensar passo a passo” no comando.

| Comando | Resposta do modelo |
| --- | --- |
| Quando vou ficar sem papel higiênico? | Em breve, você só tem mais três rolos. |

| **Comando atualizado** | **Resposta aprimorada** |
| --- | --- |
| 1. Primeiro, conte quantos rolos de papel higiênico há nessa imagem.  2. Em seguida, determine a quantidade de papel higiênico que uma pessoa usa por dia.  3. Calcule quanto tempo esses rolos de papel higiênico vão durar. | 1. Há três rolos de papel higiênico nesta imagem.  2. Uma pessoa usa cerca de 20 folhas de papel higiênico por dia.  3. Se cada rolo tiver 200 páginas, cada um deles durará cerca de 10 dias. Portanto, os três rolos durarão cerca de um mês. |

Problemas matemáticos ou outros tipos de problemas são ótimos candidatos para pedir que o modelo pense em etapas.

| **Comando** | **Resposta** |
| --- | --- |
| Qual é o quarto termo na sequência? | -135 |

A resposta do modelo está incorreta. Algumas maneiras de melhorar isso é pedir ao modelo que analise o problema antes de responder ao comando.

| **Comando** | **Resposta** |
| --- | --- |
| Analise a fórmula na imagem primeiro.  Depois, com base na fórmula, responda "qual é o quarto termo na sequência?". | *Clique para abrir o resultado* $$ b(n) = b(n-1) \* (-3) $$  $$ b(1) = 15 $$   1. Substitua n = 4 na fórmula:  $$ b(4) = b(4-1) \* (-3) $$  $$ b(4) = b(3) \* (-3) $$ 2. Não sabemos o valor de b(3), portanto, substitua n = 3 na fórmula:  $$ b(3) = b(3-1) \* (-3) $$  $$ b(3) = b(2) \* (-3) $$ 3. Não sabemos o valor de b(2), portanto, substitua n = 2 na fórmula:  $$ b(2) = b(2-1) \* (-3) $$  $$ b(2) = b(1) \* (-3) $$ 4. Sabemos que o valor de b(1) é 15, portanto, substitua-o na fórmula:  $$ b(2) = 15 \* (-3) $$  $$ b(2) = -45 $$ 5. Agora que sabemos o valor de b(2), substitua-o na fórmula por b(3):  $$ b(3) = b(2) \* (-3) $$  $$ b(3) = -45 \* (-3) $$  $$ b(3) = 135 $$ 6. Agora que sabemos o valor de b(3), substitua-o na fórmula por b(4):  $$ b(4) = b(3) \* (-3) $$  $$ b(4) = 135 \* (-3) $$  $$ b(4) = -405 $$   Portanto, o quarto termo na sequência é -405. |

A resposta do modelo está correta. Agora, para simplificar ainda mais, peça ao modelo que pense em etapas detalhadas.

| **Comando atualizado** | **Resposta aprimorada** |
| --- | --- |
| Qual é o quarto termo na sequência? Pense em etapas. | O primeiro termo é 15.  O segundo termo é b(1) \* (-3) = 15 \* (-3) = -45.  O terceiro termo é b(2) \* (-3) = -45 \* (-3) = 135.  O quarto termo é b(3) \* (-3) = 135 \* (-3) = -405. |

### especifique o formato das respostas

Um problema comum é a necessidade de a saída do modelo estar em um determinado formato
(por exemplo, markdown, JSON, HTML), especialmente se ela precisar ser ingerida por uma tarefa downstream. Você pode tentar produzir saídas nesse formato instruindo o modelo a fazer isso no comando. Veja dois exemplos:

| Comando | Resposta do modelo |
| --- | --- |
| Analise a tabela nesta imagem no formato markdown | | Assunto | Status | Tempo | Data de início | Prazo |  | ------- | ------ | ---- | ---------- | ------ |  | Matemática | Concluído | 1h30 | 29/11/2023 | 01/12/2023 |  | Geografia | Concluído | 30 min | 02/12/2023 | 04/12/2023 |  | Física | Em andamento | 2h | 03/12/2023 | 05/12/2023 |  | Biologia | Não começou | 6 horas | 02/11/2016 | 06/12/2023 | |

| **Comando** | **Resposta do modelo** |
| --- | --- |
| Forneça uma lista com todos os atributos a seguir:  Ingredientes, tipo de culinária, vegetariano ou não, no formato JSON | ```` ```json ````  `{`  `"ingredients": [`  `"rice",`  `"shrimp",`  `"clams",`  `"mussels",`  `"peas",`  `"tomatoes",`  `"onions",`  `"garlic",`  `"olive oil",`  `"paprika",`  `"salt",`  `"pepper"`  `],`  `"type of cuisine": "Spanish",`  `"vegetarian": false`  `}`  ```` ``` ```` |

### Colocar a imagem em primeiro lugar nos comandos com uma imagem

O Gemini pode interpretar imagens e textos em qualquer ordem nos comandos, mas inserir uma imagem individual antes do comando de texto pode gerar resultados melhores.
Nos exemplos a seguir, você vai notar que a imagem vem antes do texto em
cada comando.

### solucionar problemas do comando multimodal

Se você não receber uma resposta útil, talvez seja necessário resolver problemas do comando. Aqui estão algumas estratégias que você pode tentar.

#### Se o modelo não estiver desenhando informações da parte relevante da imagem

Para receber uma resposta mais específica, indique de quais aspectos da imagem
você quer que o comando extraia informações para embasar sua resposta.

| Comando | Resposta do modelo |
| --- | --- |
| Quantos dias essas fraldas vão durar para um bebê? | As fraldas durarão 198 dias antes de acabarem. |

| **Comando atualizado** | **Resposta aprimorada** |
| --- | --- |
| Quanto tempo essas fraldas vão durar?  Determine a idade da criança e o número total de fraldas na caixa com base no peso total.  Divida o total pelo número de fraldas usadas diariamente por uma criança. | A caixa contém 198 fraldas. Ela também informa que as fraldas são para crianças que pesam de 9 a 16 quilos.  Crianças nessa faixa de peso geralmente têm de 1 a 2 anos de idade.  Uma criança de dois anos costuma usar 6 fraldas por dia, logo, as fraldas vão durar cerca de 33 dias (198/6). |

#### Se a saída do modelo for muito genérica e não for personalizada o suficiente para a entrada de imagem

Para ajudar o modelo a adaptar a resposta às imagens, peça para ele descrever
as imagens antes de realizar a tarefa de raciocínio.

| Comando | Resposta do modelo |
| --- | --- |
| O que há em comum entre essas imagens? | As quatro imagens são exemplos de fotografia de paisagem. |

| **Comando atualizado** | **Resposta aprimorada** |
| --- | --- |
| Primeiro, descreva o que está em cada imagem em detalhes. O que há em comum entre essas imagens? | A primeira imagem mostra uma pessoa fazendo as malas. A segunda imagem mostra um corredor vazio de um shopping. A terceira imagem mostra um rolo de papel higiênico. A quarta imagem mostra um mar escuro e tempestuoso.  O ponto em comum entre essas imagens é que todas são exemplos de espaços liminais. Espaços liminais são lugares ou situações que estão entre dois outros lugares ou situações. Elas costumam ser caracterizadas por um senso de incerteza ou ambiguidade.  A primeira imagem mostra a pessoa entre o momento em que está em casa e viajando. A segunda imagem mostra o corredor entre duas lojas. A terceira imagem é de papel higiênico, que pode representar um banheiro. Um banheiro é um espaço de transição entre domínios privados e públicos. É um lugar onde nos preparamos para entrar ou sair do mundo exterior.  A quarta imagem mostra o mar entre calmo e tempestuoso.  Espaços liminais podem ser empolgantes e perturbadores. Eles podem ser um lugar de recomeço ou de fim. Eles podem ser um local de reflexão ou ação. |

Você também pode tentar pedir explicitamente ao modelo para se referir ao que está na imagem.

| **Comando atualizado** | **Resposta aprimorada** |
| --- | --- |
| O que há em comum entre essas imagens? Consulte o que está nas imagens na sua resposta. | Todas as imagens são relacionadas a viagens. A primeira imagem mostra uma pessoa fazendo as malas, a segunda mostra um corredor vazio de um shopping, a terceira imagem mostra uma pilha de papel higiênico e a quarta mostra um mar escuro e violento.  Todas essas imagens são relacionadas a viagens, porque são tudo o que as pessoas precisam ou usam quando viajam. A primeira imagem mostra uma pessoa fazendo as malas, que é algo que as pessoas fazem quando viajam. A segunda imagem mostra um corredor vazio de um shopping, que é um lugar onde as pessoas costumam comprar itens para viagens. A terceira imagem mostra uma pilha de papel higiênico, algo que as pessoas costumam usar quando estão viajando. A quarta imagem mostra um mar escuro e tempestuoso, algo que as pessoas encontram com frequência quando estão viajando. |

As mesmas dicas funcionam para resultados criativos de imagens. No exemplo a seguir com o coelho, pedir explicitamente ao modelo para incluir aspectos da imagem pode melhorar a saída.

| Comando | Resposta do modelo |
| --- | --- |
| Você pode me escrever um poema sobre esta imagem? | Coelhinho peludo e marrom  Pulando pelo campo, para cima e para baixo.  Suas orelhas são tão longas e sua cauda tão pequena!  Você é a criatura mais fofa de todas.  Você morde a grama, tão verde e doce,  E pula quando me vê.  Mas sempre serei seu amigo,  Coelhinho, até o fim. |

| **Comando atualizado** | **Resposta aprimorada** |
| --- | --- |
| Você pode escrever um poema descritivo e dramático sobre esta imagem e incluir o local? | Coelhinho no verde  Orelhas tão compridas e pontudas.  O que você vê lá fora,  À distância, onde você olha?  É o oceano azul,  Brilhando na tonalidade do sol?  Ou as ondas que quebram e rugem,  Um ritmo que você adora?  Coelhinho, fale a verdade:  O que chama sua atenção de verdade?  É a brisa salgada,  Ou o choro das gaivotas te agrada?  Talvez seja a vastidão de tudo isso,  Um mundo tão grande e pequeno.  Um lugar onde os sonhos podem andar,  e aventuras podem ser livres.  Coelhinho me pergunto o que você sonha,  Sentado na grama, tão sereno.  Você quer explorar as profundezas  Ou ficar na terra para dar um salto?  Seja o que for, coelhinho!  Deixe a faísca da maravilha brilhar.  Nos seus sonhos e aspirações,  há um mundo esperando sua criação. |

#### Solução de problemas em qual parte do prompt falhou

Pode ser difícil saber se um comando falhou porque o modelo
não **entendeu a imagem** ou se ele entendeu a imagem
mas não executou as **etapas de raciocínio** corretas.
Para fazer essa diferenciação, peça ao modelo que descreva o que aparece na imagem.

No exemplo a seguir, se o modelo responder com um lanche que parece diferente quando combinado com chá (como pipoca), primeiro é possível resolver problemas para determinar se o modelo reconheceu corretamente que a imagem contém chá.

| Comando | Prompt de solução de problemas |
| --- | --- |
| Que lanchinho eu posso fazer em 1 minuto e que combina com este? | Descreva o que há na imagem. |

Outra estratégia é pedir que o modelo explique o raciocínio dele. Isso pode ajudar você a filtrar qual parte do raciocínio está incorreta, se houver.

| Comando | Prompt de solução de problemas |
| --- | --- |
| Que lanchinho eu posso fazer em 1 minuto e que combina com este? | Que lanchinho eu posso fazer em 1 minuto e que combina com este? Explique o motivo. |

## A seguir

- Escreva seus próprios comandos multimodais usando o [Google AI Studio](http://aistudio.google.com?hl=pt-br).
- Para informações sobre como usar a API Gemini Files para
  fazer upload de arquivos de mídia e incluí-los nos seus comandos, consulte os guias
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=pt-br), [Áudio](https://ai.google.dev/gemini-api/docs/audio?hl=pt-br) e
  [Processamento de documentos](https://ai.google.dev/gemini-api/docs/document-processing?hl=pt-br).
- Para mais orientações sobre o design de comandos, como ajuste de parâmetros de amostragem, consulte a página
  [Estratégias de comandos](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-29 UTC."],[],[]]
