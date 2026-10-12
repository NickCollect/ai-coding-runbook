---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=ru
fetched_at: 2026-10-12T07:07:24.258142+00:00
title: "\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0430\u0433\u0435\u043d\u0442\u0430 \u0434\u043b\u044f \u043d\u0430\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u043a\u043e\u0434\u0430 \u0438 \u0440\u0435\u0441\u0443\u0440\u0441\u044b \u0434\u043b\u044f \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u043e\u0432 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Флэш-память Gemini 3.8 теперь доступна. [Попробуйте!](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs?hl=ru)

Отправить отзыв

# Настройка агента для написания кода и ресурсы для разработчиков

Агенты для написания кода на основе ИИ используют данные для обучения, собранные до определенной даты. Из-за этого агенты часто предлагают устаревшие модели (`gemini-1.5`), более ранние версии SDK (`google-generativeai`) или устаревшие шаблоны кода.

Подключив агента к официальным ресурсам для разработчиков Gemini, вы поможете ему писать точный код с помощью актуальных моделей, SDK `google-genai` и [API взаимодействий](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ru).

Вы можете предоставить агенту по написанию кода доступ к документации и правилам Gemini четырьмя способами:

## Сводка ресурсов агента

| Ресурс | Что можно делать с помощью этого инструмента | Доступность |
| --- | --- | --- |
| **[Навыки агента Gemini](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ru#available-skills)** | Пошаговые правила, шаблоны SDK и вспомогательные скрипты для определенных функций (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`). | Предварительно установлен в [AI Studio Build](https://ai.studio/build); можно установить с помощью `skills.sh`, Context7 или управляемых агентов. |
| **[Gemini Docs MCP Server](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ru#mcp-setup)** | Поиск в реальном времени (`gemini_search_docs`) и чтение всей страницы (`gemini_get_doc`) во всей документации. | Поддерживается в Claude Code, Cursor, OpenAI Codex и VS Code. |
| **[Плагин Gemini API](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ru#gemini-api-plugin)** | Пакет с официальными навыками Gemini, сервером MCP для Документов и инструментами для работы с ключами API. | Antigravity. |
| **[Документы, распознаваемые машиной](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ru#machine-readable-docs)** | Очистка страниц Markdown и индексов `llms.txt`. | Все страницы документации на сайте `ai.google.dev/gemini-api/docs`. |

## Как установить специализированные действия агента Gemini

Навыки агента предоставляют агенту по написанию кода процедурные правила, названия текущих моделей и шаблоны кода SDK. Вам не нужно добавлять в запрос длинные инструкции – агент загружает навыки только при необходимости. Это поможет агенту избежать устаревших SDK и использовать современные шаблоны Gemini.

Навыки работают вместе с MCP-сервером Gemini Документов. Если на устройстве агента не установлен сервер MCP, навык переходит на [`llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=ru). Подробнее о том, [как работают навыки Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=ru)…

### Установка с помощью CLI (`skills.sh` или Context7)

Установите навыки с помощью файла [skills.sh](https://skills.sh) (рекомендуется) или [Context7](https://context7.com):

```
# List all available skills in the repository
npx skills add google-gemini/gemini-skills --list

# Install a specific skill globally with skills.sh
npx skills add google-gemini/gemini-skills --skill <skill-name> --global

# Or install with Context7
npx ctx7 skills install /google-gemini/gemini-skills <skill-name>
```

### Доступные навыки

#### `gemini-api-dev`

Навыки создания приложений с помощью [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ru) и официальных SDK Gemini API (`google-genai` для Python и `@google/genai` для TypeScript). Этот навык включает:

- Генерация текста, многоходовые диалоги, потоковая передача, структурированные выходные данные и вызов функций
- Генерация изображений, преобразование текста в речь и мультимодальные запросы
- Управление состоянием чата на стороне сервера, выполнение в фоновом режиме, Deep Research и управляемые агенты
- Названия текущих моделей и перенос устаревшего кода `generateContent` или `google-generativeai`

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### `gemini-live-api-dev`

Навык создания приложений для потоковой передачи аудио и видео в реальном времени с помощью [Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ru). Этот навык включает:

- Управление сеансами WebSocket, временные токены клиента и возобновление сеансов
- Потоковая передача аудио, видео и текста с обнаружением голосовой активности (VAD) и поддержкой перебивания.
- Обоснование ответа (расширенное мышление), асинхронные вызовы инструментов без блокировки, транскрипция и перевод речи в реальном времени

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### `gemini-omni-flash-api`

Навык для создания и редактирования видео с помощью Gemini Omni Flash с использованием Interactions API. Включает вспомогательные скрипты (`upload_file.py`, `generate_video.py`, `prep_video.py`, `inspect_video.py`) и охватывает:

- Создание видео из текста и составление запросов
- Переходы между первым и последним кадрами и генерация видео на основе референсных изображений
- Расширения для видео и рабочие процессы предварительной обработки медиаконтента

```
npx skills add google-gemini/gemini-skills --skill gemini-omni-flash-api --global
```

### Как подключить специализированные действия в управляемых агентах

При запуске управляемых агентов с помощью Interactions API вы можете подключить репозиторий `google-gemini/gemini-skills` к рабочей области агента. Подробная информация приведена в [руководстве по навыкам Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=ru).

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

## Как подключить MCP-сервер Gemini Docs

Общедоступный **MCP-сервер Gemini Docs** (`https://gemini-api-docs-mcp.dev`) предоставляет вашему агенту прямой доступ ко всему сайту с документацией. Ваш агент может искать и читать страницы документации, чтобы проверять схемы запросов, ограничения моделей и новые функции:

- `gemini_search_docs`: ищет в документации Gemini API по теме или запросу.
- `gemini_get_doc`: читает весь контент в формате Markdown на определенной странице документации.

### Быстрая настройка

Чтобы автоматически настроить обнаруженных агентов кодирования, выполните следующую команду в терминале или корневом каталоге проекта:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

### Настройка по среде

### Claude Code

Выполните в терминале следующую команду:

```
$ claude mcp add --transport http geminiDocs https://gemini-api-docs-mcp.dev
```

### Курсор

Добавить в `~/.cursor/mcp.json` (глобально) или `.cursor/mcp.json` (в проекте):

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

Выполните в терминале следующую команду:

```
$ codex mcp add geminiDocs --url https://gemini-api-docs-mcp.dev
```

Или добавьте в `~/.codex/config.toml`:

```
[mcp_servers.geminiDocs]
url = "https://gemini-api-docs-mcp.dev"
```

### VS Code (Copilot)

Добавить в папку "`.vscode/mcp.json`" в рабочей области:

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

## Плагин Gemini API

Если вы используете **Antigravity**, самый быстрый способ настроить рабочее пространство – **плагин Gemini API**. Он включает MCP-сервер Gemini Docs, все официальные навыки Gemini (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`) и инструменты для работы с ключами API.

- **Установка в Antigravity (интерфейс):** перейдите в раздел **Настройки > Специальные возможности > Плагины Google** и скачайте **Gemini API**.
- **Установка с помощью CLI:**
  `bash
  agy plugin install https://github.com/google-gemini/gemini-skills`

## Документация, доступная для машинного считывания

Стандартные веб-страницы содержат HTML-теги, панели навигации и скрипты, которые занимают место в окне контекста. `ai.google.dev` предоставляет конечные точки, которые можно считывать с помощью машинного обучения, чтобы агенты и скрипты могли получать чистый код Markdown напрямую:

- **`llms.txt` index**
  ([`https://ai.google.dev/gemini-api/docs/llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=ru)):
  список всех страниц документации по Gemini API со ссылками на каждую из них.
- **Прямые URL Markdown (`.md.txt`).** Добавьте `.md.txt` к любому URL документации на сайте `ai.google.dev` (например, [`https://ai.google.dev/gemini-api/docs/coding-agents.md.txt`](https://ai.google.dev/gemini-api/docs/coding-agents.md.txt?hl=ru)), чтобы получить исходный код Markdown для сохраненных запросов, правил `AGENTS.md` или автоматизированных скриптов.

## Рекомендуемые правила проекта (`AGENTS.md`)

Файл правил проекта (`AGENTS.md`, `.cursorrules` или `CLAUDE.md`) задает базовые правила, которые загружаются в начале каждого сеанса агента. Добавьте эти правила в корневой каталог проекта, чтобы агенты по умолчанию использовали текущие модели и SDK:

```
# Gemini API Guidelines

- Before writing Gemini API code, consult the `geminiDocs` MCP server (`gemini_search_docs` / `gemini_get_doc`) or `https://ai.google.dev/gemini-api/docs/llms.txt`.
- Always use the current Gemini API SDK (`google-genai` for Python, `@google/genai` for TypeScript/JavaScript). Never use legacy SDKs (`google-generativeai` or `@google/generative-ai`).
- Use the Interactions API (`client.interactions.create`) for new applications unless a specific feature requires `generateContent`.
- Use current recommended models (see https://ai.google.dev/gemini-api/docs/models) and avoid deprecated models.
```

## Проверка и устранение неполадок

### Проверка правильности настроек

Чтобы проверить настройки, попросите агента программирования:

```
Look up the request schema for the Gemini Interactions API in the documentation.
```

Настроенный агент будет использовать `gemini_search_docs` на сервере MCP `geminiDocs` и писать код с помощью `client.interactions.create` с SDK `google-genai` или `@google/genai`.

### Команды статуса

| Среда | Подтверждение MCP | Подтверждение навыков |
| --- | --- | --- |
| **Claude Code** | Запуск по расписанию: `/mcp` | Запуск по расписанию: `/skills` |
| **Курсор** | Откройте **Настройки > Функции > MCP**. | Откройте **Настройки > Правила**. |
| **OpenAI Codex** | Запуск по расписанию: `codex mcp list` | Проверьте `.codex/skills/` или `~/.codex/skills/` |
| **Antigravity** | Откройте **Настройки > Подключения**. | Откройте **Настройки > Правила** или выполните команду `/skills list`. |
| **VS Code (Copilot)** | Откройте **Расширения > MCP** или панель вывода. | Нажмите **Выбрать инструменты** в чате Copilot. |

### Устранение неполадок

- **Не удалось обнаружить навык или MCP-сервер.** Перезапустите редактор (Cursor или VS Code) или сеанс терминала (Claude Code или Codex). Большинство агентов загружают MCP-серверы и навыки только при запуске.
- **Конфликт глобальных навыков.** Если ваш агент игнорирует глобально установленный навык, установите его в корневой каталог проекта без `--global`:
  `bash
  npx skills add google-gemini/gemini-skills --skill gemini-api-dev`
- **Правила игнорируются.** Убедитесь, что файл `AGENTS.md`, `.cursorrules` или `CLAUDE.md` находится в корневом каталоге проекта.

## Дальнейшие действия

- [Руководство по навыкам Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=ru)
- [Навыки работы с Gemini API на GitHub](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ru)
- [Доступные модели](https://ai.google.dev/gemini-api/docs/models?hl=ru)
- [Библиотеки и SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=ru)

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-06 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-06 UTC."],[],[]]
