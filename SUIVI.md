# SUIVI — financialdata

Dernière mise à jour : 2026-08-09

## Point de reprise courant

Le dépôt `Patricked-code/financialdata` est la mémoire persistante et le dépôt canonique du chantier.

### Règle Git active

- `main` uniquement ;
- aucune branche ;
- aucune PR normale.

### Règle universelle des agents

Tout agent doit reprendre le projet au point officiel, préserver l'existant et continuer sans régression.

## P0 — Gouvernance initiale

**STATUT : COMPLETE**

## P1 — Inventaire documentaire exhaustif

**STATUT : IN_PROGRESS**

### Socle P1 terminé

- racine `RAPO / Rapport V2` vérifiée ;
- 48 dossiers société confirmés ;
- script historique `telecharger_rapports_brvm.py` confirmé et analysé ;
- méthode d'inventaire directe documentée ;
- règle d'attribution émetteur documentée ;
- comparaison possible avec la BRVM courante documentée ;
- plan d'évolution du collecteur : `docs/BRVM_COLLECTOR_V2_PLAN.md`.

### Collecteur V1 — compréhension validée

La V1 :

- contient 48 slugs historiques ;
- parcourt les pages `rapports-societe-cotes/<slug>` ;
- suit la pagination ;
- récupère les PDF `/sites/default/files/` ;
- déduit l'année depuis le nom ;
- normalise certains noms ;
- ajoute des suffixes en cas de collision ;
- ignore un fichier local existant et non vide.

Limite critique : pas de manifeste/hash/versioning distant ; une correction derrière la même URL peut être manquée.

Décision : V1 conservée comme référence ; future V2 incrémentale après P1.

### Collecteur V2 — design seulement

`DISCOVER → COMPARE_MANIFEST → DOWNLOAD_DELTA → HASH → VALIDATE → VERSION_LINK → STORE → REPORT`

La V2 devra suivre URL source, titre BRVM, première/dernière observation, hash, métadonnées HTTP, versions, doublons et changements d'univers émetteur.

**Ne pas implémenter/activer avant le manifeste P1 et un dry-run validé.**

### Émetteurs P1 inventoriés

1. SIVC — 53 fichiers — `inventory/SIVC.md`
2. BOABF — 57 fichiers — `inventory/BOABF.md`
3. BOAB — 59 fichiers — `inventory/BOAB.md`
4. BOAC — 60 fichiers — `inventory/BOAC.md`
5. BOAM — 44 fichiers — `inventory/BOAM.md`

### Deltas de fraîcheur déjà identifiés

BOAC : la BRVM courante publie EF 2025 et T1 2026 alors que le Drive inventorié ne possède pas leur équivalent évident.

BOAM : la BRVM courante publie au minimum T3 2025, EF 2025 et T1 2026 absents de leur équivalent évident dans le Drive inventorié.

Statut : `REMOTE_DELTA_IDENTIFIED`.

Ces documents ne sont pas encore téléchargés par le projet ; ils servent à valider le besoin du futur collecteur incrémental.

### Progression P1

- inventaires dossiers/fichiers documentés : **5 / 48** ;
- restant : **43** ;
- hash global : `NOT_COMPLETE` ;
- périodes économiques exhaustives : `NOT_COMPLETE` ;
- manifeste machine-lisible consolidé : `NOT_COMPLETE`.

## Prochaine action exacte

Continuer P1 sans refaire les cinq premiers inventaires.

Prochain émetteur dans l'ordre historique : **BOAN — Bank of Africa Niger**.

Procédure :

1. lister le dossier BOAN ;
2. inventorier les sous-dossiers ;
3. inventorier tous les fichiers ;
4. créer `inventory/BOAN.md` ;
5. signaler dossiers vides, `divers`, versions, anomalies d'attribution ;
6. comparer au catalogue BRVM courant si utile pour la fraîcheur ;
7. mettre à jour `TODO.md` et `SUIVI.md`.

## Règle anti-perte de contexte

Avant toute reprise : lire `GOVERNANCE.md`, `AGENTS.md`, `CLAUDE.md`, ce fichier, `DECISIONS.md`, `TODO.md`, `SOURCES.md`, `inventory/README.md` et `docs/BRVM_COLLECTOR_V2_PLAN.md`.

## Point de reprise exact

`P1_IN_PROGRESS → INVENTORY_COMPLETE_5_OF_48 → NEXT = BOAN`
