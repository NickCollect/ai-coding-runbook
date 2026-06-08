---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=pl
fetched_at: 2026-06-08T05:27:08.927833+00:00
title: "Rozwi\u0105zywanie problem\u00f3w z Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Rozwiązywanie problemów z Google AI Studio

Na tej stronie znajdziesz sugestie dotyczące rozwiązywania problemów z Google AI Studio.

## Informacje o błędach 403 Access Restricted

Jeśli zobaczysz błąd 403 – Access Restricted (Ograniczony dostęp), oznacza to, że korzystasz z Google AI Studio w sposób niezgodny z [Warunkami korzystania z usługi](https://ai.google.dev/terms?hl=pl). Jednym z częstych powodów jest to, że nie mieszkasz w [obsługiwanym regionie](https://ai.google.dev/available_regions?hl=pl).

## Rozwiązywanie problemu z odpowiedziami „Brak treści” w Google AI Studio

Jeśli treść zostanie zablokowana z jakiegokolwiek powodu, w Google AI Studio pojawi się komunikat warning **Brak treści**. Aby wyświetlić więcej szczegółów, najedź wskaźnikiem na **Brak treści** i kliknij warning **Bezpieczeństwo**.

Jeśli odpowiedź została zablokowana z powodu [ustawień bezpieczeństwa](https://ai.google.dev/docs/safety_setting?hl=pl), a Ty wziąłeś(-aś) pod uwagę [ryzyko związane z bezpieczeństwem](https://ai.google.dev/docs/safety_guidance?hl=pl) w swoim przypadku użycia, możesz zmodyfikować [ustawienia bezpieczeństwa](https://ai.google.dev/docs/safety_setting?hl=pl#safety_settings_in_makersuite), aby wpłynąć na zwróconą odpowiedź.

Jeśli odpowiedź została zablokowana, ale nie z powodu ustawień bezpieczeństwa, zapytanie lub odpowiedź mogą naruszać [Warunki korzystania z usługi](https://ai.google.dev/terms?hl=pl) lub być w inny sposób nieobsługiwane.

## Sprawdzanie wykorzystania tokenów i limitów

Gdy otworzysz prompt, przycisk **Podgląd tekstu** u dołu ekranu pokazuje aktualną liczbę tokenów użytych w treści promptu oraz maksymalną liczbę tokenów dla używanego modelu.

## Uprawnienia Google Cloud IAM w AI Studio

Członkowie projektu w chmurze Google Cloud potrzebują określonych uprawnień Identity and Access Management (IAM), aby wykonywać działania w Google AI Studio. Więcej informacji o tych tożsamościach znajdziesz w [omówieniu podmiotów zabezpieczeń IAM](https://cloud.google.com/iam/docs/principals?hl=pl).

Użytkownicy z rolami **Edytujący** lub **Właściciel** w powiązanym projekcie Google Cloud mają pełne uprawnienia do wyświetlania paneli i zarządzania kluczami interfejsu Gemini API. Użytkownicy z rolą **Przeglądający** mogą wyświetlać panele i klucze interfejsu API, ale nie mogą ich tworzyć, aktualizować ani usuwać.

Aby uzyskać większą kontrolę, zapoznaj się z tabelą poniżej, w której znajdziesz konkretne uprawnienia wymagane w przypadku poszczególnych funkcji AI Studio. Instrukcje dotyczące przyznawania tych uprawnień znajdziesz w sekcji [Przyznawanie, zmienianie i odbieranie uprawnień do zasobów](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=pl) w dokumentacji Google Cloud.

| Funkcja AI Studio | Wymagane uprawnienia | Dodatkowe wymagania |
| --- | --- | --- |
| **Wyszukaj projekt** (importowanie projektów) | `resourcemanager.projects.get` |  |
| **Zmień nazwę projektu** | `resourcemanager.projects.update` |  |
| **Wyświetlanie poziomu limitu** | Nie dotyczy |  |
| **Utwórz klucz interfejsu API** | Musisz mieć uprawnienia **Wyszukiwanie projektu** i:  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **Wyświetlanie listy kluczy interfejsu API** | Musisz mieć uprawnienia **Wyszukiwanie projektu** i:  `apikeys.keys.list` `serviceusage.services.get` | W projekcie Google Cloud musi być włączony [interfejs Generative Language API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=pl). |
| **Zmiana nazwy kluczy interfejsu API** | `apikeys.keys.update` |  |
| **Usuwanie kluczy interfejsu API** | `apikeys.keys.delete` |  |
| **Panel wykorzystania** | mieć uprawnienia **Wyszukiwanie projektu** i:  `monitoring.timeSeries.list` |  |
| **Panel limitu żądań** | mieć uprawnienia do **panelu użycia** i:  `cloudquotas.quotas.get` |  |
| **Wydatki (limit płatności)** | `billing.resourceCosts.get` (aby wyświetlić wydatki) `billing.resourcebudgets.read` (aby wyświetlić limit) `billing.resourcebudgets.write` (aby ustawić limit) |  |
| **Panel płatności** | `billing.accounts.get` |  |

### Inne kontrole dostępu

Oprócz uprawnień Google Cloud IAM AI Studio przeprowadza też kontrole zabezpieczeń i zgodności. Jeśli nie spełniasz tych wymagań, w interfejsie AI Studio lub w odpowiedziach interfejsu API może pojawić się błąd `PERMISSION_DENIED` lub błąd ograniczenia dostępu:

- **Kontrole zabezpieczeń:** Twoja prośba musi przejść automatyczne kontrole zabezpieczeń.
- **Warunki korzystania z usługi:** musisz zaakceptować Warunki korzystania z usług Google oraz Dodatkowe warunki korzystania z generatywnej AI.
- **Obsługiwany region:** musisz znajdować się w [obsługiwanym regionie](https://ai.google.dev/gemini-api/docs/available-regions?hl=pl).
- **Zaufanie i bezpieczeństwo:** projekt Google Cloud nie może być oznaczony jako nadużycie.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-29 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-29 UTC."],[],[]]
