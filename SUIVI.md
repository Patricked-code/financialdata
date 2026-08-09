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

## P1 — Inventaire SOURCE

**IN_PROGRESS / BATCH_FAST**

### Progression

- émetteurs inventoriés : **42 / 48** ;
- PDF recensés : **2 689** ;
- restant : **6 émetteurs**.

### Lot 38–42

- SOGC : 28 dossiers 1998–2025, **106 PDF**, total vérifié par scission 37 + 69 ;
- SLBC : 28 dossiers 1998–2025, **65 PDF** ;
- SNTS : 27 dossiers, **101 PDF**, 2016 absent ; deep pilot existant ;
- SCRC : 11 dossiers 2016–2025 + `divers`, **45 PDF** ;
- TTLC : 28 dossiers 1998–2025, **101 PDF**, total vérifié par scission 34 + 67.

### Anomalie d'attribution SNTS

Le dossier Sonatel 2017 contient `20170721-resultats_au_premier_semestre_2017_onatel-sa_1.pdf` (Drive ID `1sIl2VvXcjKZA2CFM-9bwGO6EQB-uqX9c`). Le nom indique ONATEL. Le document reste conservé en SOURCE et doit recevoir `issuer_assignment_status = REVIEW_REQUIRED` dans le manifeste futur. Aucune suppression/réattribution silencieuse.

### Règles renforcées

- un plafond de recherche n'est jamais un total SOURCE ;
- présence physique sous un dossier émetteur ≠ attribution validée ;
- `divers` et noms de fichiers ne déterminent jamais seuls la période économique ;
- deep pilots ne sont pas refaits sans nouveau pattern réel.

## P1-R — PDF_RECOGNITION_DISCOVERY

**ACTIVE_IN_PARALLEL**

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023.
Deep pilots acquis : BOABF, CIEC, NTLC, SNTS.

Aucune nouvelle dimension conceptuelle n'a été nécessaire sur le lot 38–42 : attribution, versions, périodes et faits opérationnels sont déjà couverts.

## Passes transversales encore ouvertes

- hash global ;
- manifeste machine-lisible ;
- versions/doublons ;
- périodes économiques exhaustives ;
- attribution et couverture documentaire ;
- réconciliation BRVM courante.

## Prochaine action exacte

Terminer P1 avec les 6 derniers émetteurs :

`TTLS → PRSC → TRITRAF → UNLC → UNXC → SHEC`

Puis verrouiller `INVENTORY_COMPLETE_48_OF_48` avant de lancer les passes transversales P1/P1-FRESH.

## Point de reprise exact

`P1_BATCH_FAST → INVENTORY_COMPLETE_42_OF_48 → 2689_FILES → FINAL_BATCH = TTLS,PRSC,TRITRAF,UNLC,UNXC,SHEC + P1-R ACTIVE`
