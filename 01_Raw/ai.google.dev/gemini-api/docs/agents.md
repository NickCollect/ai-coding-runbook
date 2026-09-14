---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=pl
fetched_at: 2026-09-14T05:50:04.734107+00:00
title: "Informacje o\u00a0agentach \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Informacje o agentach

Zarządzane agenty w Gemini API zapewniają konfigurowalny szkielet agenta. Pojedyncze wywołanie interfejsu API powoduje udostępnienie piaskownicy Linux, w której agent samodzielnie wnioskuje, wykonuje kod, zarządza plikami i przegląda internet.

[rocket\_launch

Krótkie wprowadzenie

Wykonaj pierwsze wywołanie agenta, przesyłaj odpowiedzi strumieniowo i utwórz niestandardowego agenta.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl)
[smart\_toy

Agent Antigravity

Możliwości, narzędzia, dane wejściowe multimodalne i ceny domyślnego agenta.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl)
[experiment

Agenci w AI Studio

Wizualne środowisko testowe do tworzenia prototypów agentów bez pisania kodu.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=pl)

## Dostępne zarządzane agenty

- **[agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl)**: zarządzany agent do zwykłych obciążeń oparty na Gemini 3.8 Flash. Uruchamia kod, zarządza plikami i wyszukuje informacje w internecie w bezpiecznej piaskownicy Linux hostowanej przez Google. Za pomocą `agent_config` możesz skonfigurować model bazowy (np. Gemini 3.7 Flash, Gemini 3.6 Flash lub Gemini 3.5 Flash) i rozszerzyć go o własne instrukcje, umiejętności i dane, aby [utworzyć niestandardowego agenta](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl).
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl)**: autonomiczny agent badawczy
  który planuje, wykonuje i syntetyzuje wieloetapowe zadania badawcze na potrzeby takich przypadków użycia
  jak analiza rynku, należyta staranność i przeglądy literatury.

## Bezpieczeństwo i sprawdzone metody

Każdy agent działa w środowisku piaskownicy, które jest izolowane na poziomie systemu operacyjnego.
Piaskownica ma domyślnie nieograniczony dostęp do sieci wychodzącej. Możesz ograniczyć lub wyłączyć dostęp do sieci za pomocą listy dozwolonych.

### Dostęp do sieci

Domyślnie środowiska mają nieograniczony dostęp do sieci wychodzącej. Użyj listy dozwolonych `network`, aby ograniczyć ruch wychodzący do określonych domen lub wzorców z symbolami wieloznacznymi. Szczegółowe informacje o konfiguracji znajdziesz w sekcji
[Lista dozwolonych sieci](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=pl#network_allow_list) (AI
Studio) lub [Reguły sieciowe](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl#with_network_rules)
(API).

### Narzędzia i interfejsy API zewnętrzne

Aby rozszerzyć możliwości agenta, możesz połączyć go z narzędziami i interfejsami API zewnętrznymi. Używaj tylko narzędzi z zaufanych źródeł i ogranicz uprawnienia do minimum. Dane logowania można bezpiecznie wstrzykiwać za pomocą transformacji nagłówków serwera proxy ruchu wychodzącego. Nigdy nie są one udostępniane w piaskownicy. Agent może używać dowolnych danych logowania, do których ma dostęp, dlatego udostępniaj tylko te dane logowania, których pełny zakres uprawnień chcesz przyznać.

- Używaj kont usługi lub kluczy API o jak najmniejszych uprawnieniach.
- Zamiast kluczy długoterminowych używaj tokenów krótkoterminowych.
- Udostępniaj tylko te dane logowania, których pełny zakres uprawnień chcesz przyznać.
- Regularnie wykonuj rotację danych logowania.

Więcej informacji o konfigurowaniu transformacji nagłówków znajdziesz w sekcji
[Dane logowania](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl#credentials).

### Nadzór człowieka

Zanim wdrożysz wyniki (wygenerowany kod, transformacje danych, zmiany konfiguracji), zawsze je sprawdź, zwłaszcza w przypadku zadań, które modyfikują dane lub wchodzą w interakcje z systemami zewnętrznymi.

## Ceny

Zarządzane agenty korzystają z modelu [płatność według wykorzystania](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#pricing-for-agents) opartego na tokenach modelu Gemini i korzystaniu z narzędzi. Pojedyncza interakcja może wywołać wiele pętli wnioskowania, które zwykle zużywają od 100 tys. do 3 mln tokenów. W okresie korzystania z wersji przedpremierowej **nie naliczamy opłat** za obliczenia w środowisku. Zobacz [szacunkowe koszty](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl#availability-and-pricing)
podziału na zadania. Zarządzane agenty są też dostępne w ramach bezpłatnego pakietu z bezpłatnym limitem liczby żądań i limitem wykorzystania.

## Limity

| Limit | Opis |
| --- | --- |
| **Okres istnienia środowiska** | Środowiska są trwale usuwane po 7 dniach nieaktywności. |
| **Wyłączanie maszyny wirtualnej** | Aby oszczędzać zasoby, maszyny wirtualne wyłączają się po krótkim okresie nieaktywności. Następne żądanie przywraca stan (z uruchomieniem „na zimno”). |
| **Zainstalowane oprogramowanie** | Środowisko oparte na Ubuntu z Pythonem 3.12 i Node.js 22. Więcej informacji o obrazie bazowym środowiska znajdziesz w sekcji [Zainstalowane oprogramowanie](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl#pre-installed-software). |
| **Maksymalna liczba agentów** | Możesz mieć maksymalnie 1000 zarządzanych agentów. |

## Platformy agentów

Możesz też tworzyć agentów za pomocą Gemini, korzystając z tych platform i pakietów SDK:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=pl): Twórz
  złożone przepływy aplikacji ze stanem i systemy wieloagentowe za pomocą struktur
  grafów.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=pl): łącz agentów Gemini z
  danymi prywatnymi, aby korzystać z przepływów pracy z rozszerzonym wyszukiwaniem generatywnym.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=pl): zarządzaj autonomicznymi agentami AI, którzy współpracują i odgrywają role.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=pl): Build
  twórz interfejsy użytkownika i agentów opartych na AI w JavaScript/TypeScript.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): platforma
  open source do tworzenia i zarządzania interoperacyjnymi agentami AI.
- [**Antigravity SDK**](https://antigravity.google/product/antigravity-sdk?hl=pl): Twórz
  autonomiczne agenty AI za pomocą tych samych narzędzi, pętli agenta i zarządzania
  kontekstem, które są używane w Google Antigravity. Możesz je programować w Pythonie.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-10 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-10 UTC."],[],[]]
