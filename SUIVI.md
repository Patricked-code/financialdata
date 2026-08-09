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

### Émetteurs inventoriés

1. SIVC — 53
2. BOABF — 57
3. BOAB — 59
4. BOAC — 60
5. BOAM — 44
6. BOAN — 60
7. BOAS — 43
8. BNBC — 78
9. BICC — 61
10. BIIC — 2
11. AGLC — 60
12. CFAC — 94
13. CIEC — 61
14. CBIBF — 8
15. SEMC — 54
16. ECOC — 32
17. ETIT — 81

**Total : 907 fichiers recensés sur 17/48 émetteurs.**

Restant : **31 émetteurs**.

### Lot 13–17 — anomalies/patterns utiles

- CIEC : 29 dossiers (1998–2025 + `divers`), 61 PDF ; deep pilot conceptuel déjà existant ; EF 2017 révisés ;
- CBIBF : 4 dossiers 2022–2025, 8 PDF ; 2022 vide ;
- SEMC : 25 dossiers, 54 PDF ; 2002 absent, pas de dossier 2024/2025 dans le corpus observé, `divers` CAC ;
- ECOC : 9 dossiers 2017–2025, 32 PDF ; couples T1 2023/T1 rev et T3 2024/T3 rev ;
- ETIT : 23 dossiers 2003–2025, 81 PDF ; collisions historiques importantes et corpus multi-devise/consolidé.

## P1-R — PDF_RECOGNITION_DISCOVERY

**ACTIVE_IN_PARALLEL**

Profils vérifiés :

- `docs/recognition_profiles/BANKING_FINANCIAL_STATEMENTS_BICC_2022.md`
- `docs/recognition_profiles/BANKING_ACTIVITY_BIIC_T2_2025.md`
- `docs/recognition_profiles/TRANSNATIONAL_BANKING_ETIT_2023_FINANCIAL_STATEMENTS.md`

### ETIT 2023 — nouvelles preuves

Le PDF `2023_Etats_Financiers_ETIT.pdf` a été rendu visuellement :

- 6 pages, Excel natif ;
- consolidé IFRS ;
- états détaillés en milliers USD ;
- tableau de synthèse simultanément en milliers USD et millions FCFA ;
- variations publiées distinctes selon la devise ;
- résultat consolidé ventilé entre part du Groupe, autres détenteurs de capitaux propres et intérêts minoritaires.

Décision `D033` : `source_currency` au niveau fact et nouvelle dimension candidate `ownership_attribution_raw`, documentée mais non implémentée SQL.

La même observation a été ajoutée au document Drive canonique `BRVM_RAW_DATABASE — Gouvernance, architecture et observations conceptuelles` avant toute évolution de schéma.

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

`FTSC → MVSC → NEIC → NTLC → NSBC`

Puis poursuivre dans l'ordre V1 sans refaire les deep pilots déjà étudiés.

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

`P1_BATCH_FAST → INVENTORY_COMPLETE_17_OF_48 → 907_FILES → NEXT_BATCH = FTSC,MVSC,NEIC,NTLC,NSBC + P1-R ACTIVE`
