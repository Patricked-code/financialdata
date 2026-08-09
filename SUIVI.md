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

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_OPEN**

### Inventaire société terminé

- sociétés : **48 / 48** ;
- PDF recensés : **2 950** ;
- checkpoint humain : `inventory/P1_48_ISSUERS_CHECKPOINT.md` ;
- index machine-lisible : `inventory/p1_issuer_manifest.csv`.

Le total 2 950 est vérifié par addition des 48 inventaires. Il ne signifie pas extraction RAW complète.

### Lot final 43–48

`TTLS 45 | PRSC 68 | TRITRAF 8 | UNLC 20 | UNXC 83 | SHEC 37`.

## P1_TRANSVERSE — MACHINE_READABLE_MANIFEST

**STARTED**

- schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md` ;
- fichier : `inventory/p1_document_manifest.csv` ;
- couverture actuelle : **3 / 2 950 fichiers SOURCE**.

Seed initial vérifié :

1. BICC 2022 — états financiers — attribution validée — période annuelle résolue ;
2. BIIC T2 2025 — rapport d'activité — période résolue — `DOCUMENT_METADATA_MISMATCH` confirmé ;
3. SNTS/ONATEL 2017 — fichier physiquement sous Sonatel mais nom ONATEL — `issuer_assignment_status = REVIEW_REQUIRED`.

Les SHA-256 restent `NOT_COMPUTED` tant qu'ils ne sont pas réellement calculés. Les relations de version restent `NOT_REVIEWED` tant qu'elles ne sont pas prouvées.

## P1-R — PDF_RECOGNITION_DISCOVERY

**ACTIVE_IN_PARALLEL**

Profils vérifiés :

- `docs/recognition_profiles/BANKING_FINANCIAL_STATEMENTS_BICC_2022.md`
- `docs/recognition_profiles/BANKING_ACTIVITY_BIIC_T2_2025.md`
- `docs/recognition_profiles/TRANSNATIONAL_BANKING_ETIT_2023_FINANCIAL_STATEMENTS.md`

Deep pilots acquis : BOABF, CIEC, NTLC, SNTS.

## Passes transversales restantes

1. compléter `p1_document_manifest.csv` jusqu'à **2 950 / 2 950** ;
2. SHA-256 ;
3. doublons binaires / versions / révisions ;
4. périodes économiques depuis contenu ;
5. attribution émetteur/document ;
6. couverture documentaire ;
7. fraîcheur BRVM / P1-FRESH.

## P1-FRESH

Le design V2 est documenté mais aucun téléchargement automatique n'est activé avant manifeste/dry-run/validation.

## Prochaine action exacte

`P1_TRANSVERSE → EXPAND_DOCUMENT_MANIFEST_FROM_DRIVE`

Ordre recommandé par lots d'émetteurs, en commençant par les corpus courts/simples pour fiabiliser le mécanisme avant les corpus >100 documents.

## Point de reprise exact

`INVENTORY_COMPLETE_48_OF_48 → 2950_PDFS → DOCUMENT_MANIFEST_3_OF_2950 → EXPAND_MANIFEST`
