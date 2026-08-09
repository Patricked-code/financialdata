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

`P0 GOUVERNANCE → P1 SOURCE/INVENTAIRE + P1-R RECOGNITION → P1-FRESH COLLECTEUR → P2 RAW SCHEMA → P3 RAW EXTRACTION → P4 QUALITY/LINEAGE → P5 MAPPED → P6 CANONICAL → P7 DERIVED → P8 ANALYTICS`.

Architecture : `SOURCE → RAW → MAPPED → CANONICAL → DERIVED → ANALYTICS`.

## P0 — Gouvernance

**COMPLETE**

## P1 — Inventaire SOURCE

**IN_PROGRESS / BATCH_FAST**

### Progression

- émetteurs inventoriés : **37 / 48** ;
- PDF recensés : **2 271** ;
- restant : **11 émetteurs**.

### Lot 33–37

- CABC : 29 dossiers 1998–2025 + `divers`, **90 PDF** ;
- SICC : 25 dossiers, **19 PDF**, 2014 absent et pas de dossier 2024/2025 observé ;
- STBC : 29 dossiers 1998–2025 + `divers`, **91 PDF**, plusieurs révisions candidates 2025 ;
- SMBC : 28 dossiers 1998–2025, **106 PDF**, total corrigé par scission parentée 36 + 70 ;
- SDCC : 29 dossiers 1998–2025 + `divers`, **92 PDF**, total corrigé par scission parentée 36 + 56.

### SDCC — confirmation P1-R

Le corpus 2019 contient des documents SYSCOHADA révisé, IFRS individuel et IFRS consolidé. Cela confirme une règle déjà acquise : `accounting_framework_raw` et `consolidation_scope_raw` sont des dimensions indépendantes. Aucune nouvelle colonne n'est créée.

### Règle renforcée

Les recherches ticker atteignant 100 résultats doivent être considérées comme potentiellement plafonnées. Toujours vérifier par dossiers parents avant de retenir un total SOURCE.

## P1-R — PDF_RECOGNITION_DISCOVERY

**ACTIVE_IN_PARALLEL**

Profils vérifiés :

- `docs/recognition_profiles/BANKING_FINANCIAL_STATEMENTS_BICC_2022.md`
- `docs/recognition_profiles/BANKING_ACTIVITY_BIIC_T2_2025.md`
- `docs/recognition_profiles/TRANSNATIONAL_BANKING_ETIT_2023_FINANCIAL_STATEMENTS.md`

Deep pilots acquis : BOABF, CIEC, NTLC, SNTS.

## P1-FRESH

Design V2 documenté mais non activé. Aucun delta distant n'est téléchargé automatiquement pendant P1.

## Passes transversales encore ouvertes

- hash global ;
- manifeste machine-lisible ;
- versions/doublons ;
- périodes économiques exhaustives ;
- attribution et couverture documentaire ;
- réconciliation BRVM courante.

## Prochaine action exacte

Continuer immédiatement P1 avec :

`SOGC → SLBC → SNTS → SCRC → TTLC`

Puis : `TTLS → PRSC → TRITRAF → UNLC → UNXC → SHEC`.

## Ordre de reprise obligatoire

1. `GOVERNANCE.md`
2. `AGENTS.md`
3. `CLAUDE.md`
4. `ROADMAP.md`
5. `SUIVI.md`
6. `DECISIONS.md`
7. `TODO.md`
8. `SOURCES.md`
9. `docs/PDF_RECOGNITION_STRATEGY.md`
10. inventaires existants

## Point de reprise exact

`P1_BATCH_FAST → INVENTORY_COMPLETE_37_OF_48 → 2271_FILES → NEXT_BATCH = SOGC,SLBC,SNTS,SCRC,TTLC + P1-R ACTIVE`
