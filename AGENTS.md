# AGENTS.md — Règles universelles des agents

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
2. `CLAUDE.md`
3. `SUIVI.md`
4. `DECISIONS.md`
5. `TODO.md`
6. `ARCHITECTURE.md`
7. `DATA_MODEL.md`
8. `SOURCES.md`
9. documentation pertinente sous `docs/`

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
