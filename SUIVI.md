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

Émetteurs inventoriés : **32 / 48**.

Fichiers recensés : **1 873**.

Restant : **16 émetteurs**.

### Totaux individuels 1–32

`SIVC 53 | BOABF 57 | BOAB 59 | BOAC 60 | BOAM 44 | BOAN 60 | BOAS 43 | BNBC 78 | BICC 61 | BIIC 2 | AGLC 60 | CFAC 94 | CIEC 61 | CBIBF 8 | SEMC 54 | ECOC 32 | ETIT 81 | FTSC 88 | MVSC 20 | NEIC 86 | NTLC 81 | NSBC 38 | ONTBF 91 | ORGT 23 | ORAC 14 | PALC 75 | SAFC 73 | SPHC 124 | ABJC 82 | STAC 38 | SGBC 87 | SIBC 46`.

### Lot 28–32 — anomalies/patterns utiles

- SPHC : 28 dossiers 1998–2025, **124 PDF**. La recherche ticker plafonnait à 100 ; total corrigé par deux recherches strictement filtrées sur les parents (32 + 92). Variantes nombreuses EF/CAC 2019–2024 ;
- ABJC : 28 dossiers 1998–2025, **82 PDF** ; S1 2023 plain/_2/_rev et double EF 2023 ;
- STAC : 26 dossiers = 25 années + `divers`, **38 PDF** ; 2004/2007/2009 absents ; `divers_Etats_Financiers_STAC.pdf` à résoudre par contenu ;
- SGBC : 27 dossiers 1999–2025, **87 PDF** ; nombreuses variantes historiques/S1 ;
- SIBC : 10 dossiers 2016–2025, **46 PDF** ; corpus bancaire récent.

Règle renforcée : **une limite technique de recherche n'est jamais un total SOURCE**.

## P1-R — PDF_RECOGNITION_DISCOVERY

**ACTIVE_IN_PARALLEL**

Profils vérifiés :

- `docs/recognition_profiles/BANKING_FINANCIAL_STATEMENTS_BICC_2022.md`
- `docs/recognition_profiles/BANKING_ACTIVITY_BIIC_T2_2025.md`
- `docs/recognition_profiles/TRANSNATIONAL_BANKING_ETIT_2023_FINANCIAL_STATEMENTS.md`

Deep pilots acquis : BOABF, CIEC, NTLC, SNTS.

Aucune nouvelle dimension de schéma pour le lot 28–32 : versions, lacunes, métadonnées incohérentes et géométrie sont déjà couvertes.

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

Continuer immédiatement P1 en mode batch avec :

`CABC → SICC → STBC → SMBC → SDCC`

Puis poursuivre : `SOGC → SLBC → SNTS → SCRC → TTLC → TTLS → PRSC → TRITRAF → UNLC → UNXC → SHEC`.

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

`P1_BATCH_FAST → INVENTORY_COMPLETE_32_OF_48 → 1873_FILES → NEXT_BATCH = CABC,SICC,STBC,SMBC,SDCC + P1-R ACTIVE`
