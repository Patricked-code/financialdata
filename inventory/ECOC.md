# P1 SOURCE — Ecobank Côte d'Ivoire / ECOC

Date : 2026-08-10
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / VERSION_REVIEW_IN_PROGRESS`

- Ticker : `ECOC`
- Dossier Drive : `1L41JW3u29dJu1VSI6XRFeR-97ycVO50x`
- Dossiers directs : **9** (`2017` à `2025`)
- Premier inventaire de session : **32 PDF**
- État Drive live revérifié par parents + MIME : **42 PDF**
- Delta live : **+10 PDF**
- Répartition live : 2017=1 ; 2018=6 ; 2019=4 ; 2020=5 ; 2021=6 ; 2022=5 ; 2023=6 ; 2024=6 ; 2025=3.

## Particularités SOURCE

- 2017 contient bien un PDF T3 (`rapport_dactivites_3e_trimestre_-ecobank_ci_0.pdf`) : l'ancien constat « aucun PDF 2017 » est donc invalidé par la revérification live ;
- 2018 : `2018_Etats_Financiers_ECOC.pdf` + `_2.pdf` ;
- 2021 : `2021_Etats_Financiers_ECOC.pdf` + `_2.pdf` ;
- 2023 : `2023_Rapport_T1_ECOC.pdf` + `2023_Rapport_T1_ECOC_rev.pdf` ;
- 2024 : `2024_Rapport_T3_ECOC.pdf` + `2024_Rapport_T3_ECOC_rev.pdf` ;
- 2024 : `2024_Rapport_Annuel_ECOC.pdf` + `2024_Rapport_Annuel_ECOC_rev.pdf` ;
- états financiers, T1/S1/T3, rapports annuels et attestations CAC coexistent selon les années.

## Règle

Le total live est obtenu sans filtre de nom, exclusivement par les 9 dossiers parents + `mimeType = application/pdf`. Les couples `_rev` et `_2` restent des objets SOURCE séparés jusqu'à preuve de correction/supersession ou verdict binaire. Aucune relation n'est inférée du suffixe seul.

## Hash / runtime

Le runtime local de calcul de la session est actuellement indisponible. Aucun SHA ECOC n'est déclaré sans calcul réel. Les contrôles de contenu et de métadonnées Drive continuent indépendamment.

## Restant transversal

`DOCUMENT_MANIFEST_ECOC = IN_PROGRESS` ; `SHA256_ECOC = BLOCKED_RUNTIME_NOT_COMPUTED` ; `VERSION_LINKS = IN_PROGRESS` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
