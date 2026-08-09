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

`P0 GOUVERNANCE → P1 SOURCE/INVENTAIRE + P1-R RECOGNITION → P1-FRESH COLLECTEUR → P2 RAW SCHEMA → P3 RAW EXTRACTION → P4 QUALITY/LINEAGE → P5 MAPPED → P6 CANONICAL → P7 DERIVED → P8 ANALYTICS`.

Architecture de données inchangée : `SOURCE → RAW → MAPPED → CANONICAL → DERIVED → ANALYTICS`.

## P0 — Gouvernance initiale

**STATUT : COMPLETE**

## P1 — Inventaire documentaire exhaustif

**STATUT : IN_PROGRESS / BATCH_FAST**

### Changement de cadence validé

Décision `D031` : l'inventaire est un moyen, pas la finalité.

Dorénavant :

- traiter les métadonnées Drive par lots d'émetteurs ;
- éviter la rédaction répétitive lorsqu'aucune anomalie n'existe ;
- réserver la revue détaillée aux dossiers vides, versions, doublons, erreurs d'attribution et autres exceptions ;
- poursuivre jusqu'à 48/48 plus rapidement.

### P1-R — PDF_RECOGNITION_DISCOVERY

**STATUT : ACTIVE_IN_PARALLEL**

Référence : `docs/PDF_RECOGNITION_STRATEGY.md`.

But : reconnaître les structures nécessaires à la future création automatique des bases de données sans prétendre avoir déjà réalisé P3.

À profiler en parallèle :

- rapports annuels anciens/récents ;
- états financiers détaillés ;
- T1/T3/S1/S2 ;
- CAC/attestations ;
- documents divers/révisés.

À reconnaître :

- type de document/état ;
- pages/sections/tableaux ;
- géométrie lignes/colonnes/cellules ;
- labels et codes source ;
- périodes/comparatifs ;
- unités/multiplicateurs/devises ;
- scopes ;
- faits financiers, opérationnels, corporate, audit, réglementaires et textuels.

Objectif : produire un moteur générique `PDF → reconnaissance → faits candidats → validation → RAW database`, pas 48 parseurs spécifiques.

### Socle P1 terminé

- racine `RAPO / Rapport V2` vérifiée ;
- 48 dossiers société confirmés ;
- script historique `telecharger_rapports_brvm.py` confirmé et analysé ;
- méthode d'inventaire directe documentée ;
- règle d'attribution émetteur documentée ;
- plan collecteur V2 documenté ;
- roadmap de bout en bout créée ;
- stratégie de reconnaissance PDF créée.

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
- manifeste machine-lisible consolidé : `NOT_COMPLETE` ;
- profils PDF réutilisables : `IN_PROGRESS`.

## Prochaine action exacte

Continuer P1 en **lots de plusieurs émetteurs**, à partir de **BNBC — Bernabé Côte d'Ivoire**, sans refaire les sept premiers.

En parallèle, enrichir les profils de reconnaissance uniquement lorsqu'un nouveau type de document/tableau/metric/scope est découvert.

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
10. `docs/PDF_RECOGNITION_STRATEGY.md`
11. `docs/BRVM_COLLECTOR_V2_PLAN.md`

## Point de reprise exact

`P1_BATCH_FAST → INVENTORY_COMPLETE_7_OF_48 → NEXT_BATCH_START = BNBC + P1-R ACTIVE`
