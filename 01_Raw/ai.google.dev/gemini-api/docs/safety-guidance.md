---
source_url: https://ai.google.dev/gemini-api/docs/safety-guidance?hl=fr
fetched_at: 2026-09-28T06:31:57.134140+00:00
title: "Consignes de s\u00e9curit\u00e9 et d'exactitude \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Consignes de sécurité et d'exactitude

Les modèles d'intelligence artificielle générative sont des outils puissants, mais ils ont leurs limites. Leur polyvalence et leur applicabilité peuvent parfois entraîner des résultats inattendus, tels que des résultats inexacts, biaisés ou choquants. Le post-traitement et l'évaluation manuelle rigoureuse sont essentiels pour limiter le risque de préjudice lié à ces résultats.

Les modèles fournis par l'API Gemini peuvent être utilisés pour une grande variété d'applications d'IA générative et de traitement du langage naturel (TLN). L'utilisation de ces fonctions n'est disponible que via l'API Gemini ou l'application Web Google AI Studio. Votre utilisation de l'API Gemini est également soumise au [Règlement sur les utilisations interdites de l'IA générative](https://policies.google.com/terms/generative-ai/use-policy?hl=fr) et aux [Conditions d'utilisation de l'API Gemini](https://ai.google.dev/terms?hl=fr).

Les grands modèles de langage (LLM) sont très utiles, car ce sont des outils de création qui peuvent traiter de nombreuses tâches linguistiques différentes. Malheureusement, cela signifie également qu'ils peuvent générer des résultats inattendus, y compris des textes choquants, insensibles ou factuellement incorrects. De plus, la polyvalence incroyable de ces modèles rend difficile de prédire exactement les types de résultats indésirables qu'ils pourraient produire. Bien que l'API Gemini ait été conçue en tenant compte des [Principes de Google en matière d'IA](https://ai.google/principles/?hl=fr), il incombe aux développeurs d'appliquer ces modèles de manière responsable. Pour aider les développeurs à créer des applications sûres et responsables, l'API Gemini propose un filtrage de contenu intégré ainsi que des paramètres de sécurité ajustables selon quatre dimensions de préjudice. Pour en savoir plus, consultez le guide sur les [paramètres de sécurité](https://ai.google.dev/gemini-api/docs/safety-settings?hl=fr). Elle propose également l'ancrage avec la recherche Google pour améliorer la factualité, mais cette fonctionnalité peut être désactivée pour les développeurs dont les cas d'utilisation sont plus créatifs et ne visent pas à rechercher des informations.

Ce document vise à vous présenter certains risques de sécurité qui peuvent survenir lors de l'utilisation de LLM et à vous recommander les dernières consignes de conception et de développement en matière de sécurité. (Notez que les lois et règlements peuvent également imposer des restrictions, mais ces considérations ne sont pas abordées dans ce guide.)

Voici les étapes recommandées pour créer des applications avec des LLM :

- Comprendre les risques liés à la sécurité de votre application
- Envisager des ajustements pour limiter les risques de sécurité
- Effectuer des tests de sécurité adaptés à votre cas d'utilisation
- Solliciter les commentaires des utilisateurs et surveiller l'utilisation

Les phases d'ajustement et de test doivent être itératives jusqu'à ce que vous atteigniez des performances adaptées à votre application.

![Cycle d&#39;implémentation du modèle](https://ai.google.dev/static/gemini-api/docs/images/safety_diagram.png?hl=fr)

## Comprendre les risques liés à la sécurité de votre application

Dans ce contexte, la sécurité est définie comme la capacité d'un LLM à éviter de nuire à ses utilisateurs, par exemple en générant un langage toxique ou du contenu qui promeut des stéréotypes. Les modèles disponibles via l'API Gemini ont été conçus en tenant compte des [principes concernant l'IA de Google](https://ai.google/principles/?hl=fr). Votre utilisation de cette API est soumise au [Règlement sur les utilisations interdites de l'IA générative](https://policies.google.com/terms/generative-ai/use-policy?hl=fr). L'API fournit des filtres de sécurité intégrés pour aider à résoudre certains problèmes courants des modèles de langage, tels que le langage toxique et les discours incitant à la haine, et pour s'efforcer d'être inclusif et d'éviter les stéréotypes. Toutefois, chaque application peut présenter un ensemble de risques différent pour ses utilisateurs. En tant que propriétaire de l'application, vous êtes donc responsable de la connaissance de vos utilisateurs et des préjudices potentiels que votre application peut causer, et de vous assurer que votre application utilise les LLM de manière sûre et responsable.

Lors de cette évaluation, vous devez tenir compte de la probabilité qu'un préjudice se produise, déterminer sa gravité et définir des mesures d'atténuation. Par exemple, une application qui génère des essais basés sur des événements factuels devra faire plus attention à éviter les informations incorrectes qu'une application qui génère des histoires fictives à des fins de divertissement. Pour commencer à explorer les risques potentiels pour la sécurité, vous pouvez effectuer des recherches sur vos utilisateurs finaux et sur les autres personnes susceptibles d'être affectées par les résultats de votre application. Cela peut prendre de nombreuses formes, y compris la recherche d'études de pointe dans le domaine de votre application, l'observation de la façon dont les utilisateurs utilisent des applications similaires, ou la réalisation d'une étude utilisateur, d'une enquête ou d'entretiens informels avec des utilisateurs potentiels.

### Conseils avancés

- Parlez à un groupe diversifié d'utilisateurs potentiels de votre population cible au sujet de votre application et de son objectif prévu afin d'obtenir une perspective plus large sur les risques potentiels et d'ajuster les critères de diversité si nécessaire.
- Le [cadre de gestion des risques liés à l'IA](https://www.nist.gov/itl/ai-risk-management-framework) publié par le National Institute of Standards and Technology (NIST), un organisme gouvernemental américain, fournit des conseils plus détaillés et des ressources d'apprentissage supplémentaires pour la gestion des risques liés à l'IA.
- La publication de DeepMind sur les [risques éthiques et sociaux liés aux préjudices causés par les modèles de langage](https://arxiv.org/abs/2112.04359) décrit en détail les façons dont les applications de modèles de langage peuvent causer des préjudices.

## Envisagez de faire des ajustements pour limiter les risques liés à la sécurité et à la factualité.

Maintenant que vous comprenez les risques, vous pouvez décider comment les atténuer. Déterminer les risques à prioriser et les mesures à prendre pour essayer de les éviter est une décision essentielle, semblable au tri des bugs dans un projet logiciel. Une fois que vous avez déterminé les priorités, vous pouvez commencer à réfléchir aux types de mesures d'atténuation les plus appropriés. Souvent, des modifications simples peuvent faire la différence et réduire les risques.

Par exemple, lorsque vous concevez une application, pensez aux éléments suivants :

- **Réglez la sortie du modèle** pour mieux refléter ce qui est acceptable dans le contexte de votre application. Le réglage peut rendre la sortie du modèle plus prévisible et cohérente, et donc aider à atténuer certains risques.
- **Fournissez une méthode d'entrée qui facilite des sorties plus sûres.** L'entrée exacte que vous fournissez à un LLM peut faire la différence dans la qualité de la sortie. Il vaut la peine d'expérimenter avec les invites d'entrée pour trouver ce qui fonctionne le plus sûrement dans votre cas d'utilisation, car vous pouvez ensuite fournir une UX qui le facilite. Par exemple, vous pouvez limiter les utilisateurs à choisir uniquement dans une liste déroulante d'invites d'entrée, ou proposer des suggestions pop-up avec des phrases descriptives qui, selon vous, fonctionnent de manière sûre dans le contexte de votre application.
- **Bloquer les entrées dangereuses et filtrer les sorties avant qu'elles ne soient présentées à l'utilisateur** : dans des situations simples, les listes de blocage permettent d'identifier et de bloquer les mots ou expressions dangereux dans les requêtes ou les réponses, ou d'exiger que des examinateurs humains modifient ou bloquent manuellement ce type de contenu.
- **Utiliser des classificateurs entraînés pour étiqueter chaque requête en fonction des préjudices potentiels ou des signaux antagonistes** Vous pouvez alors appliquer diverses stratégies de traitement des requêtes en fonction du préjudice détecté. Par exemple, si l'entrée est manifestement antagoniste ou abusive par nature, elle peut être bloquée et une réponse prédéfinie peut être générée à la place.
  **Conseil avancé** : Si les signaux déterminent que le résultat est dangereux, l'application peut utiliser les options suivantes :

  - Affichez un message d'erreur ou une sortie prédéfinie.
  - Réessayez le prompt, au cas où une autre sortie sécurisée serait générée, car parfois le même prompt génère des sorties différentes.
- **Mise en place de mesures de protection contre l'utilisation abusive délibérée**, par exemple en attribuant à chaque utilisateur un ID unique et en imposant une limite au volume de requêtes utilisateur pouvant être envoyées au cours d'une période donnée. Une autre mesure de protection consiste à essayer de se prémunir contre une éventuelle injection de prompt. L'injection de prompt, tout comme l'injection SQL, permet aux utilisateurs malveillants de concevoir un prompt d'entrée qui manipule la sortie du modèle, par exemple en envoyant un prompt d'entrée qui demande au modèle d'ignorer tous les exemples précédents. Pour en savoir plus sur l'utilisation abusive délibérée, consultez le [Règlement sur l'utilisation interdite de l'IA générative](https://policies.google.com/terms/generative-ai/use-policy?hl=fr).
- **Ajuster la fonctionnalité à quelque chose qui présente un risque intrinsèquement plus faible** : les tâches dont le champ d'application est plus restreint (par exemple, extraire des mots clés de passages de texte) ou qui font l'objet d'une plus grande supervision humaine (par exemple, générer du contenu court qui sera examiné par un humain) présentent souvent un risque plus faible. Par exemple, au lieu de créer une application pour rédiger une réponse à un e-mail à partir de zéro, vous pouvez la limiter à l'expansion d'un plan ou à la suggestion d'autres formulations.
- **Ajuster les paramètres de sécurité pour le contenu nuisible afin de réduire la probabilité de voir des réponses potentiellement dangereuses.** L'API Gemini fournit des paramètres de sécurité que vous pouvez ajuster lors de la phase de prototypage pour déterminer si votre application nécessite une configuration de sécurité plus ou moins restrictive. Vous pouvez ajuster ces paramètres dans cinq catégories de filtres pour restreindre ou autoriser certains types de contenus. Consultez le [guide sur les paramètres de sécurité](https://ai.google.dev/gemini-api/docs/safety-settings?hl=fr) pour en savoir plus sur les paramètres de sécurité ajustables disponibles dans l'API Gemini.
- **Réduisez le risque d'inexactitudes factuelles ou d'hallucinations en activant l'ancrage avec la recherche Google.** N'oubliez pas que de nombreux modèles d'IA sont expérimentaux et peuvent présenter des informations factuellement inexactes, halluciner ou produire des résultats problématiques. La fonctionnalité d'ancrage avec la recherche Google associe le modèle Gemini à des contenus Web en temps réel et fonctionne avec toutes les langues disponibles. Cela permet à Gemini de fournir des réponses plus précises et de citer des sources vérifiables au-delà de la date limite des connaissances des modèles.

## Effectuez des tests de sécurité adaptés à votre cas d'utilisation.

Les tests sont un élément clé de la création d'applications robustes et sécurisées, mais leur étendue, leur portée et leurs stratégies varient. Par exemple, un générateur d'haïkus juste pour le plaisir est susceptible de présenter des risques moins graves qu'une application conçue pour être utilisée par des cabinets d'avocats afin de résumer des documents juridiques et d'aider à rédiger des contrats. Toutefois, le générateur d'haïkus peut être utilisé par une plus grande variété d'utilisateurs, ce qui signifie que le risque de tentatives d'attaque ou même d'entrées nuisibles involontaires peut être plus élevé. Le contexte d'implémentation est également important. Par exemple, une application dont les résultats sont examinés par des experts humains avant toute action peut être considérée comme moins susceptible de produire des résultats nuisibles que la même application sans une telle supervision.

Il n'est pas rare de devoir effectuer plusieurs itérations de modifications et de tests avant de se sentir prêt à lancer une application, même pour celles qui présentent un risque relativement faible. Deux types de tests sont particulièrement utiles pour les applications d'IA :

- L'**évaluation comparative de la sécurité** consiste à concevoir des métriques de sécurité qui reflètent les façons dont votre application pourrait être dangereuse en fonction de la façon dont elle est susceptible d'être utilisée. Il s'agit ensuite de tester les performances de votre application par rapport à ces métriques à l'aide d'ensembles de données d'évaluation. Il est recommandé de réfléchir aux niveaux minimaux acceptables des métriques de sécurité avant de tester, afin de pouvoir 1) évaluer les résultats des tests par rapport à ces attentes et 2) rassembler l'ensemble de données d'évaluation en fonction des tests qui évaluent les métriques qui vous intéressent le plus.

  **Conseils avancés :**

  - Méfiez-vous de la dépendance excessive aux approches "prêtes à l'emploi", car vous devrez probablement créer vos propres ensembles de données de test à l'aide d'évaluateurs humains pour les adapter pleinement au contexte de votre application.
  - Si vous avez plusieurs métriques, vous devrez décider comment faire un compromis si un changement entraîne des améliorations pour une métrique au détriment d'une autre. Comme pour l'ingénierie des performances, vous pouvez vous concentrer sur les performances dans le pire des cas dans votre ensemble d'évaluation plutôt que sur les performances moyennes.
- Les **tests contradictoires** consistent à essayer de manière proactive de casser votre application. L'objectif est d'identifier les points faibles afin que vous puissiez prendre les mesures nécessaires pour y remédier. Les tests contradictoires peuvent demander beaucoup de temps et d'efforts aux évaluateurs experts dans votre application. Toutefois, plus vous en effectuez, plus vous avez de chances de repérer les problèmes, en particulier ceux qui se produisent rarement ou seulement après des exécutions répétées de l'application.

  - Les tests antagonistes permettent d'évaluer systématiquement un modèle de ML dans le but de savoir comment il se comporte quand des entrées malveillantes ou accidentellement nuisibles lui sont fournies :
    - Une entrée peut être malveillante lorsqu'elle a clairement été conçue pour générer un résultat dangereux ou nuisible. Par exemple, demander à un modèle de génération de texte de générer un discours haineux à l'égard d'une religion particulière.
    - Une entrée est accidentellement nuisible lorsqu'elle est inoffensive en elle-même, mais qu'elle produit un résultat nuisible. Par exemple, lorsqu'un modèle de génération de texte est invité à décrire une personne appartenant à une ethnie particulière et qu'il génère un contenu raciste.
  - Ce qui distingue un test contradictoire d'une évaluation standard, c'est la composition des données utilisées pour le test. Pour les tests contradictoires, sélectionnez les données de test les plus susceptibles de générer des résultats problématiques à partir du modèle. Cela signifie sonder le comportement du modèle pour tous les types de préjudices possibles, y compris les exemples rares ou inhabituels et les cas extrêmes qui sont pertinents pour les règles de sécurité. Elle doit également inclure la diversité dans les différentes dimensions d'une phrase, telles que la structure, le sens et la longueur. Pour en savoir plus sur les éléments à prendre en compte lors de la création d'un ensemble de données de test, consultez les [pratiques de Google en matière d'IA responsable concernant l'équité](https://ai.google/responsibilities/responsible-ai-practices/?category=fairness&hl=fr).
    **Conseils avancés :**
  - Utilisez des [tests automatisés](https://www.deepmind.com/blog/red-teaming-language-models-with-language-models?hl=fr) au lieu de la méthode traditionnelle qui consiste à faire appel à des équipes rouges pour tenter de pirater votre application. Dans les tests automatisés, l'équipe rouge est un autre modèle de langage qui recherche des textes d'entrée susceptibles de générer des résultats dangereux à partir du modèle testé.

## Surveiller les problèmes

Même si vous testez et atténuez les problèmes, vous ne pouvez jamais garantir la perfection. Planifiez donc à l'avance comment repérer et résoudre les problèmes qui surviennent. Les approches courantes incluent la configuration d'un canal surveillé permettant aux utilisateurs de partager leurs commentaires (par exemple, une évaluation par pouce levé/baissé) et la réalisation d'une étude utilisateur pour solliciter de manière proactive les commentaires d'un groupe diversifié d'utilisateurs. Cette approche est particulièrement utile si les schémas d'utilisation sont différents des attentes.

### Conseils avancés

- Lorsque les utilisateurs fournissent des commentaires sur les produits d'IA, cela peut considérablement améliorer les performances de l'IA et l'expérience utilisateur au fil du temps. Par exemple, cela peut vous aider à choisir de meilleurs exemples pour l'optimisation des requêtes. Le [chapitre sur le contrôle et le feedback](https://pair.withgoogle.com/chapter/feedback-controls/) du [guide Google sur les personnes et l'IA](https://pair.withgoogle.com/guidebook/chapters) met en évidence les principaux points à prendre en compte lors de la conception de mécanismes de feedback.

## Étapes suivantes

- Consultez le guide sur les [paramètres de sécurité](https://ai.google.dev/gemini-api/docs/safety-settings?hl=fr) pour en savoir plus sur les paramètres de sécurité ajustables disponibles via l'API Gemini.
- Consultez l'[introduction aux requêtes](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=fr) pour commencer à rédiger vos premières requêtes.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/05 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/05 (UTC)."],[],[]]
