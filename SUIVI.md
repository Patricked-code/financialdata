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

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_OPEN**

### Checkpoint majeur

- sociétés inventoriées : **48 / 48** ;
- PDF recensés au niveau dossiers/fichiers : **2 950** ;
- inventaires individuels : `inventory/<TICKER>.md` ;
- checkpoint consolidé : `inventory/P1_48_ISSUERS_CHECKPOINT.md`.

`INVENTORY_COMPLETE_48_OF_48` ne signifie pas que P1 est entièrement terminé et ne signifie surtout pas que les 2 950 PDF sont déjà extraits en RAW.

### Lot final 43–48

- TTLS : 11 dossiers 2016–2025 + `divers`, **45 PDF** ;
- PRSC : 28 dossiers 1998–2025, **68 PDF** ;
- TRITRAF : 7 dossiers 1998–2004, **8 PDF** ; corpus historique sparse ;
- UNLC : 9 dossiers 2016–2023 + `divers`, **20 PDF** ; pas de dossier 2024/2025 observé ;
- UNXC : 28 dossiers 1998–2025, **83 PDF** ;
- SHEC : 10 dossiers 2016–2025, **37 PDF**.

### Règles de comptage validées

- une réponse plafonnée à 100 n'est jamais un total SOURCE ;
- les recherches sont bornées par dossiers parents lorsque nécessaire ;
- les résultats hors dossier société sont exclus ;
- `_2/_3/...` et `_rev` restent des documents distincts jusqu'à preuve hash/contenu ;
- dossier vide/corpus court/lacune annuelle = état SOURCE valide ;
- présence physique sous un dossier ≠ attribution émetteur validée.

### Anomalie d'attribution déjà ouverte

SNTS 2017 contient `20170721-resultats_au_premier_semestre_2017_onatel-sa_1.pdf` alors que le fichier est rangé sous Sonatel. À inscrire dans le manifeste document par document avec `issuer_assignment_status = REVIEW_REQUIRED`.

## P1-R — PDF_RECOGNITION_DISCOVERY

**ACTIVE_IN_PARALLEL**

Profils vérifiés :

- `docs/recognition_profiles/BANKING_FINANCIAL_STATEMENTS_BICC_2022.md`
- `docs/recognition_profiles/BANKING_ACTIVITY_BIIC_T2_2025.md`
- `docs/recognition_profiles/TRANSNATIONAL_BANKING_ETIT_2023_FINANCIAL_STATEMENTS.md`

Deep pilots acquis : BOABF, CIEC, NTLC, SNTS.

Aucune nouvelle dimension conceptuelle n'a été requise par le lot final. Les règles existantes couvrent versions, périodes, lacunes, scopes et faits opérationnels.

## P1 — Passes transversales prioritaires

1. **MACHINE_READABLE_MANIFEST** : manifeste document par document des 2 950 PDF ;
2. **SHA256** : hash de chaque fichier ;
3. **DUPLICATES / VERSIONS** : doublons binaires et relations de révision ;
4. **ECONOMIC_PERIODS** : période réellement publiée dans le contenu ;
5. **ISSUER_ASSIGNMENT** : validation de l'émetteur réel ;
6. **COVERAGE** : mesure de la couverture documentaire ;
7. **FRESHNESS** : réconciliation avec la BRVM courante et P1-FRESH.

## P1-FRESH

Le design V2 est documenté mais aucun téléchargement automatique n'est activé avant manifeste/dry-run/validation.

## Prochaine action exacte

Commencer immédiatement :

`P1_TRANSVERSE → MACHINE_READABLE_MANIFEST`

Le manifeste doit devenir la source machine-lisible unique de la couche SOURCE, tout en conservant les inventaires Markdown comme mémoire humaine/audit.

## Point de reprise exact

`P1_TRANSVERSE → INVENTORY_COMPLETE_48_OF_48 → 2950_PDFS → MACHINE_READABLE_MANIFEST_START`
