# P1 SOURCE — NSIA Banque Côte d'Ivoire / NSBC

Date : 2026-08-10
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED`

- Ticker : `NSBC`
- Dossier Drive : `1FzP9fR9x025gJw18qziXs2Dxusyv0vP1`
- Dossiers directs : **10** = années `2017` à `2025` + `divers`
- Premier inventaire de session : **38 PDF**
- État Drive live revérifié par parents + MIME : **41 PDF**
- Delta live : **+3 PDF**

## Particularités SOURCE

- corpus récent, centré sur 2017–2025 ;
- `divers_Etats_Financiers_NSBC.pdf` nécessite résolution de période depuis le contenu ;
- 2019 contient `2019_Rapport_T1_NSBC.pdf` et `2019_Rapport_T1_NSBC_rev.pdf` ;
- 2019 contient aussi deux états financiers physiques (`plain` et `_2`) ;
- 2021 contient `2021_Etats_Financiers_NSBC.pdf` et `2021_Etats_Financiers_NSBC_rev.pdf` ;
- T1/S1/T3, états financiers et CAC/attestations présents selon années ;
- 2024 inclut aussi un communiqué distinct.

## Règle

Le total live est obtenu uniquement par les 10 dossiers parents et `mimeType = application/pdf`, sans filtre de nom. Les suffixes `_rev` et `_2` désignent uniquement des candidats de version : aucune supersession ni duplication n'est déduite du nom. Les sources sont conservées séparément jusqu'au verdict SHA-256 et à l'analyse documentaire.

## Restant transversal

`DOCUMENT_MANIFEST_NSBC = IN_PROGRESS` ; `SHA256_NSBC = IN_PROGRESS` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
