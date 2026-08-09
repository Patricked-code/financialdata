# P1 SOURCE — Orange Côte d'Ivoire / ORAC

Date : 2026-08-09
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / MANIFEST_COMPLETE_FOR_ISSUER / SHA256_COMPLETE_FOR_ISSUER`

- Ticker : `ORAC`
- Dossier Drive : `1BgjEsarpAEHdhsD1pzvTgNFrT9q4aRjj`
- Dossiers directs : **4** (`2022`, `2023`, `2024`, `2025`)
- Premier inventaire de session : **14 PDF**
- État Drive live revérifié : **21 PDF**
- Delta live : **+7 PDF**
- manifeste shard : `inventory/manifests/ORAC.csv` — **21 / 21**
- registre hash : `inventory/hashes/ORAC.csv` — **21 / 21**

## État live par année

- 2022 : **3 PDF** — états financiers, annuel, annuel `_rev` ;
- 2023 : **6 PDF** — T1, T3, CAC S1, résultats financiers consolidés, annuel, annuel `_2` ;
- 2024 : **7 PDF** — T1, S1, T3, CAC S1, états financiers, annuel, rapport RSE ;
- 2025 : **5 PDF** — T1, S1, T3, CAC S1, états financiers.

## Delta live observé

Les sept fichiers absents du premier inventaire sont apparus avec des `created_time` Drive autour de 06:33–06:34Z : deux annuels 2022, trois documents 2023 et deux documents 2024.

## Résultat SHA-256

- SHA calculés : **21 / 21** ;
- contenus binaires uniques : **21 / 21** ;
- aucun groupe de doublon exact ORAC.

En particulier :

- `2022_Rapport_Annuel_ORAC.pdf` et `2022_Rapport_Annuel_ORAC_rev.pdf` ont des SHA différents : `_rev` reste `REVISION_CANDIDATE`, sans supersession silencieuse ;
- `2023_Rapport_Annuel_ORAC.pdf` et `_2.pdf` ont des SHA différents : doublon binaire exclu, relation sémantique non revue.

## P1-R

Le rapport RSE 2024 est classé comme famille documentaire `RSE_REPORT` dans le shard SOURCE. Cette classification n'entraîne aucune nouvelle table RAW avant inspection de contenu et preuve conceptuelle.

## Restant transversal ORAC

`VERSION_SEMANTIC_REVIEW = NOT_COMPLETE` ; `ECONOMIC_PERIODS_CONTENT_REVIEW = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
