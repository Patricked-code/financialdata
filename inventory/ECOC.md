# P1 SOURCE — Ecobank Côte d'Ivoire / ECOC

Date : 2026-08-11
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / SHA256_COMPLETE / VERSION_REVIEW_COMPLETE_FOR_EXPLICIT_VARIANTS`

- Ticker : `ECOC`
- Dossier Drive : `1L41JW3u29dJu1VSI6XRFeR-97ycVO50x`
- Dossiers directs : **9** (`2017` à `2025`)
- Premier inventaire de session : **32 PDF**
- État Drive live revérifié par parents + MIME : **42 PDF**
- Delta live : **+10 PDF**
- Répartition live : 2017=1 ; 2018=6 ; 2019=4 ; 2020=5 ; 2021=6 ; 2022=5 ; 2023=6 ; 2024=6 ; 2025=3.

## Particularités SOURCE

- 2017 contient bien un PDF T3 (`rapport_dactivites_3e_trimestre_-ecobank_ci_0.pdf`) : l'ancien constat « aucun PDF 2017 » est invalidé par la revérification live ;
- 2018 : `2018_Etats_Financiers_ECOC.pdf` + `_2.pdf` ;
- 2021 : `2021_Etats_Financiers_ECOC.pdf` + `_2.pdf` ;
- 2023 : `2023_Rapport_T1_ECOC.pdf` + `2023_Rapport_T1_ECOC_rev.pdf` ;
- 2024 : `2024_Rapport_T3_ECOC.pdf` + `2024_Rapport_T3_ECOC_rev.pdf` ;
- 2024 : `2024_Rapport_Annuel_ECOC.pdf` + `2024_Rapport_Annuel_ECOC_rev.pdf` ;
- états financiers, T1/S1/T3, rapports annuels et attestations CAC coexistent selon les années.

## Règle

Le total live est obtenu sans filtre de nom, exclusivement par les 9 dossiers parents + `mimeType = application/pdf`. Les couples `_rev` et `_2` restent des objets SOURCE séparés jusqu'à preuve de correction/supersession ou verdict binaire. Aucune relation n'est inférée du suffixe seul.

## SHA-256

- **42 / 42 PDF matérialisés et hashés** ;
- **42 / 42 tailles Drive ↔ fichiers hashés validées** ;
- **41 SHA uniques** ;
- registre : `inventory/hashes/ECOC.csv` ;
- **1 groupe de doublon binaire exact** dans ECOC :
  - `2021_Etats_Financiers_ECOC.pdf` ;
  - `2021_Etats_Financiers_ECOC_2.pdf` ;
  - 333 711 octets chacun ;
  - SHA commun `ca091608d953102461797fb13924c9bfb14357505a149bc20f924e41cde2ce7a` ;
  - groupe `SHA256:ca091608d953102461797fb13924c9bfb14357505a149bc20f924e41cde2ce7a`.

## Revue des variantes

Rapport détaillé : `inventory/reviews/ECOC_VERSION_REVIEW_20260811.md`.

- 2018 EF plain / `_2` : `BINARY_DISTINCT`, aucune fusion ;
- 2021 EF plain / `_2` : `EXACT_DUPLICATE` ;
- 2023 T1 plain → `_rev` : `CORRECTED_VERSION_OF / SUPERSEDES` validé visuellement ; le commentaire PNB est corrigé de 16,9 Md FCFA à 25,8 Md FCFA et la hausse des dépôts de 26,5 % à 14,9 % ;
- 2024 T3 plain / `_rev` : hashes distincts, contenu textuel matériellement identique et différences de mise en page seulement ; `NO_SEMANTIC_SUPERSESSION_PROVEN` ;
- 2024 annuel plain → `_rev` : `CORRECTED_VERSION_OF / SUPERSEDES` ; comparaison des 10 pages : seule la page 9 comporte une correction visible, **(55 320) → (52 320)**.

## État transversal

`DOCUMENT_MANIFEST_ECOC = SOURCE_IDENTIFIERS_COMPLETE_HASH_BACKFILL_AVAILABLE` ; `SHA256_ECOC = COMPLETE_42_OF_42` ; `VERSION_LINKS_EXPLICIT_VARIANTS = REVIEWED` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
