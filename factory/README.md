# FinancialData — usine de développement autonome locale (v0.1)

## État opérationnel courant — 2026-11-06

**Le titre v0.1 et les limites historiques ci-dessous décrivent la fondation initiale, non l'état complet du dépôt.** Deux tâches autonomes de codage ont été produites, validées, publiées et attestées en runs GitHub `42283853272` et `42283964239`. La chaîne hébergée `PLAN → CODE → VALIDATE → PUBLISH → ATTEST` est active pour les blueprints gouvernés. L'entrée de conversation est [ARRIVAL.md](ARRIVAL.md) ; l'installation dans un autre dépôt s'appuie sur [PORTABILITY.md](PORTABILITY.md). Le codeur général via modèle externe n'a pas de secrets fournisseurs vérifiés ; l'auto-qualification de nouvelles tâches au-delà des deux templates doit encore être développée avec garde-fous. La dernière autorité d'état reste `state.json` et les derniers runs GitHub.


## Portée et statut

Ce dépôt dispose d'un premier moteur exécutable en Python standard, sans dépendance au MCP, à Codex ou à une API de modèle d'IA. Il relie les fichiers de mémoire existants à un état de tâches exploitable par les agents.

**Limite explicite :** le moteur exécute les audits déterministes mais n'est pas encore un codeur IA hébergé fonctionnant 24 h/24. Les tâches de type agent_code doivent être prises en charge par un agent de code autorisé. Aucune fausse déclaration d'exécution n'est permise.

## Sources d'autorité (inchangées)

- ROADMAP.md : programmes et objectifs P0 à P8.
- TODO.md : travaux existants et nouvelles tâches à planifier.
- SUIVI.md : point de reprise opérationnel métier.
- GOVERNANCE.md, AGENTS.md, CLAUDE.md : règles et permissions.
- DECISIONS.md : décisions validées.
- factory/state.json : projection opérationnelle versionnée des programmes, tâches, agents et événements, sans remplacer la mémoire canonique.
- factory/evidence/ : rapports d'audit datés et identifiés.

L'architecture SOURCE → RAW → MAPPED → CANONICAL → DERIVED → ANALYTICS n'est pas modifiée. La politique main-only sans PR est respectée. Aucun lien obligatoire avec le MCP.

## Utilisation

Depuis la racine du dépôt :

    python -m factory.engine bootstrap
    python -m factory.engine audit
    python -m factory.engine status
    python -m factory.engine admit --agent audit-01 --capabilities audit
    python -m factory.engine run --agent audit-01 --max-tasks 20

Pour un agent codeur connecté :

    python -m factory.engine admit --agent coder-01 --capabilities coder
    python -m factory.engine next --agent coder-01

Le résultat de next fournit une tâche existante, son identifiant et ses critères. L'agent intervient selon les règles de gouvernance, produit les tests et une preuve. Après validation du travail :

    python -m unittest discover -s factory/tests -v
    python -m factory.engine complete --agent coder-01 --task-id IDENTIFIANT_REEL --evidence "commit:SHA; tests:PASS; source:REFERENCES"

En cas d'obstacle avéré, la commande block possède les mêmes paramètres. Ne pas marquer DONE sans preuve concrète.

## Les six mécanismes

1. **Programmes** : P0, P1, P1-R, P1-FRESH, P2..P8, reliés à ROADMAP.md.
2. **Fabrique de tâches** : conversion déterministe des cases TODO.md ; identifiants stables, critères, priorités et dépendances extensibles ; synchronisation additive et non destructive.
3. **Agent orchestration** : admission nominative par capacité (audit/coder), prise en charge exclusive locale, lease, reprise idempotente, ordre déterministe.
4. **Exécution** : actions d'audit automatisables ; remise structurée d'une tâche de code à l'agent autorisé, sans exécution shell arbitraire.
5. **Validation** : tests unitaires, audit du manifeste SOURCE et du registre SHA, workflow GitHub Actions de vérification en lecture seule.
6. **Preuves / continuité** : journal interne horodaté et chaîné par SHA-256, Git SHA observé, références de preuves, statuts, reprise depuis l'état sérialisé.

## Sécurité et absence de régression

La fabrique n'écrit que sous factory/. Elle ne réécrit ni les PDF, ni les CSV SOURCE, ni les décisions et fichiers métier. Aucune commande issue du titre d'une tâche ne sera exécutée comme programme.

Le contrôle des registres SHA porte sur leur structure : les octets PDF externes à GitHub ne sont pas prétendus revérifiés. La cohérence du manifeste est évaluée sans jamais fabriquer les lignes absentes.

Le verrou local protège seulement un processus sur une machine. Ce n'est **pas** un verrou distribué entre deux agents hébergés sur des machines distinctes. Avant toute écriture multi-agent vers main, une coordination distante et un contrôle de révision GitHub doivent être ajoutés.

Le workflow Actions est en lecture seule (permissions contents: read). Il exécute les tests et dépose un rapport d'audit comme artefact, sans publier directement une mutation métier ni prétendre déployer une application.

Le codeur autonome permanent, les agents IA et une future connexion au MCP sont des étapes supplémentaires : ne pas les déclarer opérationnels à ce stade.

## Entrée canonique d'un agent

GOVERNANCE.md → AGENTS.md → CLAUDE.md → SUIVI.md → DECISIONS.md → TODO.md → ROADMAP.md → factory/README.md → bootstrap → admit → next/run → test → evidence → suivi.

Toute session doit vérifier l'état de main, les travaux existants, et préserver les décisions validées. Après modification significative, mettre à jour SUIVI.md, TODO.md et DECISIONS.md si nécessaire.

## Extension hébergée FD-AUTONOMY-V1

L'implémentation initiale ci-dessus reste valide. Le raccordement [factory/CONTINUITY.md](CONTINUITY.md) ajoute maintenant un workflow hébergé qui enchaîne les unités de travail sans faire dépendre le dépôt du MCP. Le registre reste factory/state.json ; tasking.py ajoute de façon additive les travaux et UTL blueprints, coder.py appelle un véritable modèle Claude, publisher.py gère publication directe main et attestation du workflow. Deux tâches de code P1 non destructives servent de premiers travaux admissibles.

Activation : dans GitHub > Settings > Secrets and variables > Actions, définir le secret ANTHROPIC_API_KEY et les variables ANTHROPIC_MODEL (identifiant Claude disponible) et FD_AUTONOMY_ENABLED=true. L'exécuteur traite un travail à la fois, toutes les 15 minutes et sur workflow_dispatch ; une continuation explicite est demandée après publication. L'absence de ces paramètres interdit de prétendre à un codage autonome opérationnel. Les coûts API et les runs Actions dépendent du fournisseur et des paramètres du compte. Les jobs codage, validation et publication sont séparés : les tests de code généré ne reçoivent pas de clé de modèle ni de permission Git d'écriture.

### Bootstrap autonome et opt-out

L'extension D036 fournit factory/templates.py : un codeur déterministe réel pour les deux travaux P1 de vérification SOURCE. Ces deux travaux n'exigent pas de secret et utilisent les mêmes contrôles sécurité, unités, CI et publication. Pour les tâches nouvelles qui n'ont pas de template, la génération Claude nécessite ANTHROPIC_API_KEY et ANTHROPIC_MODEL. Le workflow peut se déclencher par push/dispatch/schedule ; définir FD_AUTONOMY_ENABLED=false pour mettre en pause les travaux de génération. Les deux premières tâches doivent être attestées sur GitHub avant de considérer le bootstrap autonome prouvé.

### Politique de reprise et d'échec opérationnelle

Le workflow gère les états BACKLOG → PUBLISHED_PENDING_CI → DONE/BLOCKED et le registre des UTL dans factory/state.json. La publication n'est autorisée qu'après validation dans un job sans secret. Un échec GENERATE/VALIDATE est enregistré avec l'identifiant du run GitHub, une seule fois par run ; trois échecs distincts font passer la tâche et ses UTL restantes en BLOCKED. Aucune répétition non bornée de dépenses modèle. Après le dernier travail admissible, la continuité est explicitement NO_ADMISSIBLE_AUTONOMOUS_TASK ; cela n'implique pas que les travaux financiers P1 sont terminés. Voir factory/CONTINUITY.md et factory/HANDOFF.json.

## Entrée conversationnelle canonique — FD-AGENT-ARRIVAL-V1

Tout nouvel agent codeur commence par [ARRIVAL.md](ARRIVAL.md), quel que soit l'outil de conversation. Commande diagnostique sans écriture : `python -m factory.entry --role coder --agent agent-session`. Le compte GitHub doit être authentifié séparément : cette commande ne prouve pas l'identité d'une connexion. Le diagnostic peut être obtenu directement via le connecteur GitHub en consultant les mêmes fichiers et les runs. Il oriente vers la qualification des tâches existantes lorsque le catalogue READY est vide. Voir [PORTABILITY.md](PORTABILITY.md) pour installer une usine similaire dans **un autre dépôt après audit**, sans exporter la gouvernance BRVM ou main-only.

## Tranche suivante — qualification automatique P1

La documentation technique actuelle de la nouvelle extension est `factory/PROGRAM_FACTORY.md`. Le moteur ne s'arrête plus à une liste figée de deux tâches : quand aucune tâche READY ne reste, le pipeline de réconciliation examine des règles de qualification de programme **explicites et contrôlées**. Les deux premiers diagnostics sont déterministes, sûrs et en lecture seule. Pour les tâches non couvertes par ces règles, aucune fabrication arbitraire de blueprint ou de résultat métier n'est permise. `factory/provider.py` expose la commande `python -m factory.provider status` et l'appel réel Claude lorsque les paramètres sont disponibles.
