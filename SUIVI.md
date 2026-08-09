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
23. ONTBF — 91
24. ORGT — 23
25. ORAC — 14
26. PALC — 75
27. SAFC — 73

**Total : 1 496 fichiers recensés sur 27/48 émetteurs.**

Restant : **21 émetteurs**.

### Lot 23–27 — anomalies/patterns utiles

- ONTBF : 19 dossiers 2008–2025 + `divers`, 91 PDF ; collisions historiques et doubles états financiers ;
- ORGT : 8 dossiers 2018–2025, 23 PDF ; corpus récent T1/S1/T3/EF/CAC ;
- ORAC : 4 dossiers 2022–2025, 14 PDF ; corpus télécom récent ;
- PALC : 25 dossiers, 75 PDF ; 2000/2002 absents, annuel 2009 révisé, S2 présents ;
- SAFC : 27 dossiers, 73 PDF ; 2015 absent, T2 et T4 explicitement présents.

Aucune nouvelle dimension conceptuelle n'a été nécessaire pour ce lot : les règles de période, versions, lacunes SOURCE et faits opérationnels sectoriels couvrent les observations.

## P1-R — PDF_RECOGNITION_DISCOVERY

**ACTIVE_IN_PARALLEL**

Profils vérifiés :

- `docs/recognition_profiles/BANKING_FINANCIAL_STATEMENTS_BICC_2022.md`
- `docs/recognition_profiles/BANKING_ACTIVITY_BIIC_T2_2025.md`
- `docs/recognition_profiles/TRANSNATIONAL_BANKING_ETIT_2023_FINANCIAL_STATEMENTS.md`

Deep pilots acquis : BOABF, CIEC, NTLC, SNTS.

Règles acquises incluent désormais la reconnaissance réelle de T1/T2/T3/T4/S1/S2 dans le corpus.

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

`SPHC → ABJC → STAC → SGBC → SIBC`

Puis poursuivre dans l'ordre V1.

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

`P1_BATCH_FAST → INVENTORY_COMPLETE_27_OF_48 → 1496_FILES → NEXT_BATCH = SPHC,ABJC,STAC,SGBC,SIBC + P1-R ACTIVE`
