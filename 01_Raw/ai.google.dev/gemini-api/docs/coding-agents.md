---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=sq
fetched_at: 2026-10-19T05:40:26.012944+00:00
title: "Konfigurimi i agjentit t\u00eb kodimit dhe burimet p\u00ebr zhvilluesit \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon tani është i disponueshëm. [Provoje](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=sq).

![](https://ai.google.dev/_static/images/translated.svg?hl=sq)

Google përdor teknologjinë e IA-së për të përkthyer përmbajtjet në gjuhën tënde të preferuar. Përkthimet nga IA-ja mund të përmbajnë gabime.

- [Faqja kryesore](https://ai.google.dev/?hl=sq)
- [Gemini API](https://ai.google.dev/gemini-api?hl=sq)
- [Dokumentet](https://ai.google.dev/gemini-api/docs?hl=sq)

Dërgo komente

# Konfigurimi i agjentit të kodimit dhe burimet për zhvilluesit

Agjentët e kodimit me IA-në mbështeten në të dhënat e trajnimit që ndërpriten në një datë të caktuar. Për këtë arsye, agjentët shpesh sugjerojnë modele të zhvlerësuara (`gemini-1.5`), SDK-të më të vjetra (`google-generativeai`) ose modele të vjetruara të kodeve.

Lidhja e agentit tënd me burimet zyrtare të zhvilluesve të Gemini e ndihmon atë të shkruajë kode të sakta duke përdorur modelet aktuale, SDK-në e `google-genai` dhe [API-në e Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=sq).

Mund t'i japësh qasje agjentit të kodimit te dokumentacioni dhe rregullat e Gemini në katër mënyra:

## Përmbledhja e burimeve të agjentit

| Burimi | Çfarë ofron | Disponueshmëria |
| --- | --- | --- |
| **[Aftësitë e Gemini Agent](https://ai.google.dev/gemini-api/docs/coding-agents?hl=sq#available-skills)** | Rregullat hap pas hapi, modelet e SDK-së dhe skriptet ndihmëse për veçori specifike (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`). | Instaluar paraprakisht në [AI Studio Build](https://ai.studio/build); instalo me `skills.sh`, Context7 ose "Agjentët e menaxhuar". |
| **[Serveri MCP i "Dokumenteve" të Gemini](https://ai.google.dev/gemini-api/docs/coding-agents?hl=sq#mcp-setup)** | Kërkimi në drejtpërdrejt (`gemini_search_docs`) dhe leximet e faqeve të plota (`gemini_get_doc`) në të gjithë dokumentacionin. | Mbështetur në Claude Code, Cursor, OpenAI Codex dhe VS Code. |
| **[Shtesa e Gemini API](https://ai.google.dev/gemini-api/docs/coding-agents?hl=sq#gemini-api-plugin)** | Paketa e integruar me aftësitë zyrtare të Gemini, serverin MCP të "Dokumenteve" dhe veglat e çelësave të API-së. | Antigravity. |
| **[Dokumente të lexueshme nga makineria](https://ai.google.dev/gemini-api/docs/coding-agents?hl=sq#machine-readable-docs)** | Pastro faqet e "Shënimeve të formatuara" dhe indekset e `llms.txt`. | Të gjitha faqet e dokumentacionit në `ai.google.dev/gemini-api/docs`. |

## Instalo aftësitë e Gemini Agent

Aftësitë e agjentit i japin agjentit të kodimit rregullat procedurale, emrat aktualë të modeleve dhe
modelet e kodeve të SDK-së. Në vend që të shtosh udhëzime të gjata te kërkesa jote, agjenti yt i ngarkon aftësitë vetëm kur është e nevojshme. Kjo e ndihmon agjentin tënd të shmangë SDK-të e zhvlerësuara dhe të përdorë modelet moderne të Gemini.

Aftësitë funksionojnë në krah të serverit MCP të Gemini Docs. Nëse agjenti yt nuk ka të instaluar serverin MCP, aftësia kthehet te
[`llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=sq). Për të mësuar më shumë rreth mënyrës se si funksionojnë aftësitë, lexo [udhëzuesin e aftësive të Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=sq).

### Instalo me CLI (`skills.sh` ose Context7)

Instalo aftësitë duke përdorur [skills.sh](https://skills.sh) (rekomandohet) ose
[Context7](https://context7.com):

```
# List all available skills in the repository
npx skills add google-gemini/gemini-skills --list

# Install a specific skill globally with skills.sh
npx skills add google-gemini/gemini-skills --skill <skill-name> --global

# Or install with Context7
npx ctx7 skills install /google-gemini/gemini-skills <skill-name>
```

### Aftësitë e disponueshme

#### `gemini-api-dev`

Aftësia për të ndërtuar aplikacione me [API-n e ndërveprimeve](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=sq) dhe SDK-të zyrtare të Gemini API
(`google-genai` për Python dhe `@google/genai` për TypeScript). Kjo aftësi
mbulon:

- Gjenerimi i tekstit, biseda me shumë kthesa, transmetimi, daljet e strukturuara dhe thirrja e funksioneve
- Gjenerimi i imazheve, teksti në ligjërim (TTS) dhe hyrjet multimodale
- Menaxhimi i gjendjes së bisedës nga ana e serverit, ekzekutimi në sfond, Deep
  Research dhe agjentët e menaxhuar
- Emrat e modeleve aktuale dhe migrimi i kodit të sistemit të vjetër `generateContent` ose `google-generativeai`

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### `gemini-live-api-dev`

Aftësia për të krijuar aplikacione të transmetimit të audios dhe videos në kohë reale me
[Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=sq). Kjo aftësi mbulon:

- Menaxhimi i seancës së WebSocket, kodet e përkohshme të klientit dhe vazhdimi i seancës
- Transmetimi i audios, videos dhe tekstit me zbulimin e aktivitetit zanor (VAD) dhe
  mbështetjen e ndërprerjes
- Arsyetimi në sfond (mendimi i zgjeruar), thirrjet asinkrone jo bllokuese të veglave, transkriptimi dhe përkthimi i ligjërimit në çast

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### `gemini-omni-flash-api`

Aftësia për të gjeneruar dhe modifikuar video me Gemini Omni Flash duke përdorur API-n e "Ndërveprimeve". Përfshin skriptet ndihmëse (`upload_file.py`,
`generate_video.py`, `prep_video.py`, `inspect_video.py`) dhe mbulon:

- Gjenerimi i videos nga teksti dhe krijimi i kërkesës
- Tranzicionet e kuadrit të parë dhe të fundit dhe gjenerimi i videove i udhëhequr nga referencat
- Shtesat e videos dhe flukset e punës për parapërpunimin e mediave

```
npx skills add google-gemini/gemini-skills --skill gemini-omni-flash-api --global
```

### Montoni aftësitë në agjentët e menaxhuar

Kur ekzekuton agjentë të menaxhuar në distancë me API-n e ndërveprimeve, mund të montosh depon e `google-gemini/gemini-skills` në hapësirën e punës të agjentit. Shiko
[udhëzuesin e aftësive të Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=sq)
për detaje:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Build a script that generates a 5-second video of a neon cityscape.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/google-gemini/gemini-skills",
                "target": ".agents",
            }
        ],
    },
)
```

## Lidh serverin MCP të "Dokumenteve" të Gemini

**Serveri publik MCP i Gemini Docs** (`https://gemini-api-docs-mcp.dev`) i jep
agjentit tënd qasje të drejtpërdrejtë në të gjithë sajtin e dokumentacionit. Agjenti yt mund të kërkojë dhe të lexojë faqet e dokumentacionit për të kontrolluar skemat e kërkesave, kufijtë e modeleve dhe veçoritë e reja:

- `gemini_search_docs`: Kërkon në dokumentacionin e Gemini API sipas temës ose kërkesës.
- `gemini_get_doc`: Lexon përmbajtjen e plotë të Markdown të një faqeje specifike dokumentacioni.

### Konfigurimi i shpejtë

Ekzekuto këtë komandë në terminalin ose rrënjën e projektit për të konfiguruar automatikisht agjentët e kodimit që janë zbuluar:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

### Konfigurimi sipas mjedisit

### Claude Code

Ekzekuto në terminalin tënd:

```
$ claude mcp add --transport http geminiDocs https://gemini-api-docs-mcp.dev
```

### Kursori

Shto te `~/.cursor/mcp.json` (globale) ose `.cursor/mcp.json` (projekt):

```
{
  "mcpServers": {
    "geminiDocs": {
      "url": "https://gemini-api-docs-mcp.dev"
    }
  }
}
```

### OpenAI Codex

Ekzekuto në terminalin tënd:

```
$ codex mcp add geminiDocs --url https://gemini-api-docs-mcp.dev
```

Ose shto te `~/.codex/config.toml`:

```
[mcp_servers.geminiDocs]
url = "https://gemini-api-docs-mcp.dev"
```

### VS Code (Copilot)

Shto te "`.vscode/mcp.json`" në vendin tënd të punës:

```
{
  "servers": {
    "geminiDocs": {
      "type": "http",
      "url": "https://gemini-api-docs-mcp.dev"
    }
  }
}
```

## Shtesa e Gemini API

Nëse përdor **Antigravity**, **shtesa e Gemini API** është mënyra më e shpejtë për të konfiguruar hapësirën tënde të punës. Ai përfshin serverin MCP të Gemini Docs, të gjitha aftësitë zyrtare të Gemini (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`) dhe veglat e çelësave të API-së në një shkarkim të vetëm.

- **Instalo në Antigravity (UI):** Shko te **Cilësimet > Personalizimet > Krijo me shtesat e Google** dhe shkarko **Gemini API**.
- **Instalo me CLI:**
  `bash
  agy plugin install https://github.com/google-gemini/gemini-skills`

## Dokumentacioni i lexueshëm nga makineria

Faqet standarde të uebit përfshijnë etiketa HTML, shiritat e navigimit dhe skriptet që zënë hapësirën e dritares së kontekstit. `ai.google.dev` ofron pika përfundimtare të lexueshme nga makina në mënyrë që agjentët dhe skriptet të mund të marrin drejtpërdrejt "Shënimin e formatit" të pastër:

- Indeksi i **`llms.txt`**
  ([`https://ai.google.dev/gemini-api/docs/llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=sq)):
  Liston të gjitha faqet e dokumentacionit të Gemini API me lidhje për secilën faqe.
- **URL-të e drejtpërdrejta të Markdown (`.md.txt`)**: Shto `.md.txt` në çdo URL të dokumentacionit në `ai.google.dev` (për shembull,
  [`https://ai.google.dev/gemini-api/docs/coding-agents.md.txt`](https://ai.google.dev/gemini-api/docs/coding-agents.md.txt?hl=sq))
  për të marrë burimin e pastër të Markdown për kërkesat e ruajtura, rregullat e `AGENTS.md` ose skriptet e automatizuara.

## Rregullat e rekomanduara të projektit (`AGENTS.md`)

Një skedar rregullash projekti (`AGENTS.md`, `.cursorrules` ose `CLAUDE.md`) përcakton rregullat bazë që ngarkohen në fillim të çdo seance të agjentit. Shto këto udhëzime në rrënjën e projektit që agjentët e kodimit të parazgjedhin modelet dhe SDK-të aktuale:

```
# Gemini API Guidelines

- Before writing Gemini API code, consult the `geminiDocs` MCP server (`gemini_search_docs` / `gemini_get_doc`) or `https://ai.google.dev/gemini-api/docs/llms.txt`.
- Always use the current Gemini API SDK (`google-genai` for Python, `@google/genai` for TypeScript/JavaScript). Never use legacy SDKs (`google-generativeai` or `@google/generative-ai`).
- Use the Interactions API (`client.interactions.create`) for new applications unless a specific feature requires `generateContent`.
- Use current recommended models (see https://ai.google.dev/gemini-api/docs/models) and avoid deprecated models.
```

## Verifiko dhe zgjidh problemet

### Verifiko konfigurimin tënd

Për të testuar konfigurimin, pyet agjentin tënd të kodimit:

```
Look up the request schema for the Gemini Interactions API in the documentation.
```

Një agjent i konfiguruar do të përdorë `gemini_search_docs` në serverin e MCP-së `geminiDocs` dhe do të shkruajë kod duke përdorur `client.interactions.create` me `google-genai` ose SDK-në `@google/genai`.

### Komandat e statusit

| Mjedisi | Verifikimi i MCP-së | Verifikimi i aftësive |
| --- | --- | --- |
| **Claude Code** | Ekzekuto `/mcp` | Ekzekuto `/skills` |
| **Kursori** | Hap **Cilësimet > Veçoritë > MCP** | Hap **Cilësimet > Rregullat** |
| **OpenAI Codex** | Ekzekuto `codex mcp list` | Kontrollo `.codex/skills/` ose `~/.codex/skills/` |
| **Antigravity** | Hap **Personalizimet > Lidhjet** | Hap **Personalizimet > Rregullat** ose ekzekuto `/skills list` |
| **VS Code (Copilot)** | Hap **Shtesat > MCP** ose panelin e daljes | Kliko te **Zgjidh veglat** te "Biseda me Copilot" |

### Zgjidhja e problemeve

- **Serveri i aftësive ose MCP nuk u zbulua:** Rinis seancën e modifikuesit (Cursor ose VS Code) ose terminalit (Claude Code ose Codex). Shumica e agjentëve ngarkojnë serverët MCP dhe aftësitë vetëm kur fillojnë.
- **Konflikt i aftësisë globale:** Nëse agjenti yt shpërfill një aftësi të instaluar në nivel global, instalo aftësinë në rrënjën e projektit tënd pa `--global`:
  `bash
  npx skills add google-gemini/gemini-skills --skill gemini-api-dev`
- **Rregullat e shpërfillura:** Sigurohu që skedari yt `AGENTS.md`, `.cursorrules` ose `CLAUDE.md`
  është në direktorinë rrënjë të projektit tënd.

## Çfarë ka më pas

- [Udhëzuesi i aftësive të Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=sq)
- [Aftësitë e Gemini API në GitHub](https://github.com/google-gemini/gemini-skills)
- [API-ja e ndërveprimeve](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=sq)
- [Modelet e disponueshme](https://ai.google.dev/gemini-api/docs/models?hl=sq)
- [Bibliotekat dhe SDK-të](https://ai.google.dev/gemini-api/docs/libraries?hl=sq)

Dërgo komente

Përveçse siç përcaktohet ndryshe, përmbajtja e kësaj faqeje është e licencuar sipas [licencës së atribuimit 4.0 të Creative Commons](https://creativecommons.org/licenses/by/4.0/) dhe kampionët e kodit janë licencuar sipas [licencës së Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Për detaje, shiko [Politikat e sajtit të Google Developers](https://developers.google.com/site-policies?hl=sq). Java është një markë tregtare e regjistruar e Oracle dhe/ose filialeve të tij.

Përditësimi i fundit: 2026-10-06 UTC.

Duhet të na tregosh më shumë?

[[["E lehtë për t'u kuptuar","easyToUnderstand","thumb-up"],["E zgjidhi problemin tim","solvedMyProblem","thumb-up"],["Tjetër","otherUp","thumb-up"]],[["Mungojnë informacionet që më nevojiten","missingTheInformationINeed","thumb-down"],["Shumë e ndërlikuar/shumë hapa","tooComplicatedTooManySteps","thumb-down"],["E papërditësuar","outOfDate","thumb-down"],["Problem përkthimi","translationIssue","thumb-down"],["Problem me kampionët/kodin","samplesCodeIssue","thumb-down"],["Tjetër","otherDown","thumb-down"]],["Përditësimi i fundit: 2026-10-06 UTC."],[],[]]
