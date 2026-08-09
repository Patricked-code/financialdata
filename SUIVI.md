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
18. FTSC — 88
19. MVSC — 20
20. NEIC — 86
21. NTLC — 81
22. NSBC — 38

**Total : 1 220 fichiers recensés sur 22/48 émetteurs.**

Restant : **26 émetteurs**.

### Lot 18–22 — anomalies/patterns utiles

- FTSC : 28 dossiers 1998–2025, 88 PDF ; historique long et publications modernes T1/S1/T3/EF/CAC ;
- MVSC : 24 dossiers 1998–2020 + `divers`, 20 PDF ; couverture fichier faible par rapport à l'arborescence, `divers` EF ;
- NEIC : 27 dossiers, 86 PDF ; 2015 absent, collisions historiques et double EF 2024 ;
- NTLC : 28 dossiers 1998–2025, 81 PDF ; deep pilot déjà existant, EF 2024 original + révision ;
- NSBC : 10 dossiers 2017–2025 + `divers`, 38 PDF ; EF 2021 original + révision.

Aucune nouvelle dimension conceptuelle n'a été ajoutée pour ce lot : les anomalies observées sont déjà couvertes par les règles de version, lacune SOURCE, périodes depuis contenu et conservation des deep pilots.

## P1-R — PDF_RECOGNITION_DISCOVERY

**ACTIVE_IN_PARALLEL**

Profils vérifiés :

- `docs/recognition_profiles/BANKING_FINANCIAL_STATEMENTS_BICC_2022.md`
- `docs/recognition_profiles/BANKING_ACTIVITY_BIIC_T2_2025.md`
- `docs/recognition_profiles/TRANSNATIONAL_BANKING_ETIT_2023_FINANCIAL_STATEMENTS.md`

Deep pilots déjà acquis et à ne pas refaire : CIEC, NTLC, SNTS, BOABF.

Décision `D033` reste la dernière extension conceptuelle : `ownership_attribution_raw` candidate, documentée dans GitHub et dans le document Drive canonique, non implémentée SQL.

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

`ONTBF → ORGT → ORAC → PALC → SAFC`

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

`P1_BATCH_FAST → INVENTORY_COMPLETE_22_OF_48 → 1220_FILES → NEXT_BATCH = ONTBF,ORGT,ORAC,PALC,SAFC + P1-R ACTIVE`
