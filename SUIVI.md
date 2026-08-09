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

## Roadmap canonique

Le plan complet est dans `ROADMAP.md`.

Séquence :

`P0 GOUVERNANCE → P1 SOURCE/INVENTAIRE → P1-FRESH COLLECTEUR → P2 RAW SCHEMA → P3 RAW EXTRACTION → P4 QUALITY/LINEAGE → P5 MAPPED → P6 CANONICAL → P7 DERIVED → P8 ANALYTICS`.

Architecture de données inchangée : `SOURCE → RAW → MAPPED → CANONICAL → DERIVED → ANALYTICS`.

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
- plan collecteur V2 documenté ;
- roadmap de bout en bout créée.

### Collecteur V1 — compréhension validée

La V1 contient 48 slugs historiques, parcourt les pages BRVM et leur pagination, récupère les PDF, classe par année candidate, normalise certains noms et ignore un fichier local existant/non vide.

Limite critique : pas de manifeste/hash/versioning distant ; une correction derrière la même URL peut être manquée.

Décision : V1 conservée ; future V2 incrémentale après P1/manifeste et dry-run validé.

### Émetteurs P1 inventoriés

1. SIVC — 53 fichiers — `inventory/SIVC.md`
2. BOABF — 57 fichiers — `inventory/BOABF.md`
3. BOAB — 59 fichiers — `inventory/BOAB.md`
4. BOAC — 60 fichiers — `inventory/BOAC.md`
5. BOAM — 44 fichiers — `inventory/BOAM.md`
6. BOAN — 60 fichiers — `inventory/BOAN.md`
7. BOAS — 43 fichiers — `inventory/BOAS.md`

### Deltas de fraîcheur documentés

- BOAC : EF 2025 et T1 2026 au minimum ;
- BOAM : T3 2025, EF 2025 et T1 2026 au minimum ;
- BOAN : S2/annuels 2025 et T1 2026 au minimum ;
- BOAS : T1 2026 et états financiers T1 2026 au minimum.

Statut : `REMOTE_DELTA_IDENTIFIED`.

Aucun de ces deltas n'est téléchargé automatiquement pendant P1.

### Progression P1

- inventaires dossiers/fichiers documentés : **7 / 48** ;
- restant : **41** ;
- hash global : `NOT_COMPLETE` ;
- périodes économiques exhaustives : `NOT_COMPLETE` ;
- manifeste machine-lisible consolidé : `NOT_COMPLETE`.

## Prochaine action exacte

Continuer P1 sans refaire les sept premiers inventaires.

Prochain émetteur dans l'ordre historique du collecteur V1 : **BNBC — Bernabé Côte d'Ivoire**.

Procédure :

1. lister le dossier BNBC ;
2. inventorier tous les sous-dossiers ;
3. inventorier tous les fichiers ;
4. créer `inventory/BNBC.md` ;
5. signaler dossiers vides, `divers`, collisions, versions et anomalies d'attribution ;
6. comparer au catalogue BRVM courant si utile ;
7. mettre à jour `TODO.md` et `SUIVI.md`.

## Règle anti-perte de contexte

Avant toute reprise, lire dans cet ordre :

1. `GOVERNANCE.md`
2. `AGENTS.md`
3. `CLAUDE.md`
4. `ROADMAP.md`
5. `SUIVI.md`
6. `DECISIONS.md`
7. `TODO.md`
8. `SOURCES.md`
9. `inventory/README.md`
10. `docs/BRVM_COLLECTOR_V2_PLAN.md`

## Point de reprise exact

`P1_IN_PROGRESS → INVENTORY_COMPLETE_7_OF_48 → NEXT = BNBC`
