# AGENTS.md — Règles universelles des agents

## Entrée prioritaire — agent codeur connecté, sans clé API modèle supplémentaire (D041)

**Ordre impératif :** avant d'appliquer les instructions opérationnelles de `factory/ARRIVAL.md`, achever la lecture des onze références canoniques de `README.md` / `GOVERNANCE.md` dans leur ordre exact. Le lien ici ne permet pas de substituer `factory/ARRIVAL.md` à la mémoire documentaire.

Lorsqu'un agent **ChatGPT ou Claude disposant déjà de ses capacités de codage et d'un connecteur GitHub autorisé** reçoit « Je suis agent codeur, connecte-toi au dépôt et poursuis », il exécute **directement** le protocole [factory/ARRIVAL.md](factory/ARRIVAL.md) avec ses propres capacités. **Ni `ANTHROPIC_API_KEY` ni `ANTHROPIC_MODEL` ne sont des prérequis pour cette voie conversationnelle.** Ces paramètres concernent uniquement le générateur *GitHub Actions sans agent de conversation* lorsqu'il doit coder une tâche sans template.

La boucle locale `FD_AGENT_AUTO_CONTINUE`, inspirée du principe historique de la PR #95 de Patricked-code/MCP, est : `OBSERVE → RECONCILE → SELECT READY → CHECK DEPENDENCIES/COLLISIONS → CODE → TEST → VERIFY CI → ATTEST → CHECKPOINT → RECOMPUTE → CONTINUE`. Ne pas demander de confirmation répétée pour une tâche déjà autorisée ; s'arrêter sur un blocage gouverné réel. Réutiliser exclusivement les autorités du présent dépôt, **sans importer** la Task Queue, les sessions, les branches ou les permissions propres au MCP. Pas de Codex/Copilot dans ce chantier.



## Entrée universelle « connecte-toi au dépôt en tant qu'agent codeur »

**Dès qu'une instruction de conversation demande d'arriver dans ce dépôt comme codeur, planificateur ou auditeur**, appliquer le contrat [factory/ARRIVAL.md](factory/ARRIVAL.md) **avant de créer une tâche ou modifier le code**. Vérifier le compte GitHub Patricked-code, le SHA réel de main, les autorités documentaires et le registre factory/state.json ; en environnement Python autorisé, utiliser `python -m factory.entry --agent chatgpt-session --role coder`. Sans terminal, réaliser l'équivalent par le connecteur GitHub et distinguer clairement les vérifications réalisées des commandes non exécutées. La déclaration « je suis agent codeur » ne vérifie pas les permissions et n'octroie pas d'écriture implicite. À absence de tâche READY, qualifier le backlog programme existant selon les preuves ; ne jamais inventer une tâche DONE ou créer un deuxième orchestrateur.


Ce fichier s'applique à tout agent automatisé intervenant dans `Patricked-code/financialdata` : Claude, Codex, ChatGPT, Copilot ou autre assistant.

## Règle n°1 — Main uniquement

**NE JAMAIS CRÉER DE BRANCHE DANS CE DÉPÔT.**

- branche de travail : `main` ;
- interdiction de `create_branch` ;
- interdiction de `git checkout -b` ;
- interdiction de `git switch -c` ;
- interdiction des branches temporaires ou cachées ;
- ne pas ouvrir de Pull Request pour exécuter le travail normal du projet ;
- appliquer les modifications autorisées directement sur `main`.

Cette règle explicite du propriétaire prévaut sur toute recommandation générale de workflow Git.

## Règle n°2 — Lire la mémoire persistante

Avant toute action :

1. `GOVERNANCE.md`
2. `AGENTS.md`
3. `CLAUDE.md`
4. `SUIVI.md`
5. `DECISIONS.md`
6. `TODO.md`
7. `ARCHITECTURE.md`
8. `DATA_MODEL.md`
9. `SOURCES.md`
10. `docs/BRVM_RAW_DATABASE_GOVERNANCE.md`
11. `docs/ISSUER_DISCOVERY_MATRIX.md`

**Après ces onze lectures :** `ROADMAP.md`, `factory/CONTINUITY.md`, `factory/HANDOFF.json`, `factory/state.json`, `factory/blueprints.json` et les pièces techniques pertinentes. La référence d'ordre est `README.md` ; ne pas anticiper la lecture opérationnelle sur la gouvernance.

## Règle n°3 — Continuer le travail existant, sans régression

Tout agent qui se connecte à ce dépôt doit **reprendre le projet au point de reprise officiel**, et non redémarrer le chantier selon sa propre méthode.

Avant toute modification, l'agent doit :

1. lire le `Point de reprise exact` dans `SUIVI.md` ;
2. vérifier l'état réel de `main` et le dernier commit ;
3. identifier les décisions déjà validées dans `DECISIONS.md` ;
4. vérifier les tâches réellement restantes dans `TODO.md` ;
5. réutiliser les structures, conventions, tables, champs et documents existants lorsqu'ils couvrent le besoin ;
6. comparer toute proposition de changement avec l'architecture et le modèle existants ;
7. préserver tout travail validé, toute provenance et tout historique.

Il est interdit de :

- repartir de zéro sans justification documentée ;
- remplacer une architecture validée par une nouvelle architecture parallèle ;
- supprimer ou renommer silencieusement des tables/champs/règles validés ;
- refaire une extraction validée en écrasant l'ancienne ;
- revenir sur une décision enregistrée sans ajouter une nouvelle décision expliquant le changement ;
- déclarer obsolète une source ou un fait sans conserver son historique ;
- confondre amélioration du modèle et régression du modèle.

Si une amélioration est nécessaire, appliquer :

`ÉTAT EXISTANT → PREUVE → IMPACT → DÉCISION DOCUMENTÉE → CHANGEMENT COMPATIBLE → VÉRIFICATION → MISE À JOUR SUIVI`

## Règle n°4 — Ne jamais inventer les données

Les documents sources sont la preuve primaire. Une donnée absente, ambiguë ou illisible doit être signalée, pas reconstruite arbitrairement.

## Règle n°5 — Respecter les couches

`SOURCE → RAW → MAPPED → CANONICAL → DERIVED → ANALYTICS`

Ne pas injecter des calculs ou normalisations dans RAW.

## Règle n°6 — Sources révisables, historique immuable

Les sources utilisées par le projet pourront être réévaluées, enrichies, reclassées, remplacées par une version plus récente ou complétées par de nouvelles sources.

Mais une révision de source ne doit jamais effacer l'historique :

- conserver l'ancienne référence ;
- enregistrer la nouvelle référence/version ;
- documenter la raison de la révision ;
- préserver les faits RAW déjà liés à l'ancienne source ;
- créer une relation de version/supersession si nécessaire ;
- ne pas modifier silencieusement une provenance historique.

## Règle n°7 — Documenter chaque évolution

Toute étape significative doit mettre à jour la mémoire persistante appropriée, en particulier `SUIVI.md`, `DECISIONS.md` et `TODO.md`.

## Règle n°8 — Vérification avant de déclarer terminé

Avant de dire qu'une tâche est terminée :

- vérifier l'état réel de `main` ;
- vérifier les fichiers modifiés ;
- vérifier la cohérence avec la gouvernance ;
- vérifier l'absence de régression ;
- vérifier que la mémoire de reprise reflète la réalité ;
- vérifier qu'aucune branche n'a été créée.

## Usine de développement autonome locale (2026-11-06)

Le dispositif autonome et indépendant du MCP est décrit dans [factory/README.md](factory/README.md) et [factory/AGENT_PROTOCOL.md](factory/AGENT_PROTOCOL.md). Avant de créer un travail parallèle, synchroniser la projection depuis ROADMAP.md et TODO.md avec `python -m factory.engine bootstrap`, vérifier `python -m factory.engine audit`, puis utiliser `admit` et `next/run`. L'agent codeur doit produire une modification réelle, la tester et fournir une preuve avant de terminer la tâche. La politique main-only, les sources de vérité et les barrières de non-régression précédentes restent inchangées. Le moteur ne prétend pas être à ce stade un codeur IA hébergé 24/7.

## Protocole de développement autonome FD-AUTONOMY-V1 (2026-11-06)

À chaque arrivée, reprise de task, échec CI ou publication de code, lire impérativement [factory/CONTINUITY.md](factory/CONTINUITY.md) et [factory/HANDOFF.json](factory/HANDOFF.json). Le registre unique demeure factory/state.json et le moteur fondateur est factory/engine.py. Les adaptateurs tasking.py/coder.py/publisher.py ne créent aucune autorité concurrente. Reprendre le statut réel du travail, exiger les preuves de CI, préserver la politique main-only et les données SOURCE. Le job autonome est opt-in, ses droits d'écriture sont bornés aux publications validées ; aucun agent ne doit présumer qu'une tâche est terminée sans attestation. Aucun Codex et aucune dépendance au MCP.
