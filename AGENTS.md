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

## Règle n°3 — Ne jamais inventer les données

Les documents sources sont la preuve primaire. Une donnée absente, ambiguë ou illisible doit être signalée, pas reconstruite arbitrairement.

## Règle n°4 — Respecter les couches

`SOURCE → RAW → MAPPED → CANONICAL → DERIVED → ANALYTICS`

Ne pas injecter des calculs ou normalisations dans RAW.

## Règle n°5 — Documenter chaque évolution

Toute étape significative doit mettre à jour la mémoire persistante appropriée, en particulier `SUIVI.md`, `DECISIONS.md` et `TODO.md`.

## Règle n°6 — Vérification avant de déclarer terminé

Avant de dire qu'une tâche est terminée :

- vérifier l'état réel de `main` ;
- vérifier les fichiers modifiés ;
- vérifier la cohérence avec la gouvernance ;
- vérifier que la mémoire de reprise reflète la réalité ;
- vérifier qu'aucune branche n'a été créée.
