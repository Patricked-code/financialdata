# P1 SOURCE — Ecobank Transnational Incorporated / ETIT

Date : 2026-08-09
Statut : `P1_INVENTORIED / P1-R_PROFILED`

- Ticker : `ETIT`
- Dossier Drive : `183KoqvNUQNaj6kdfw80PkkIGupbvuSia`
- Dossiers directs : **23**, continus de `2003` à `2025`
- PDF ETIT recensés : **81**

## Particularités SOURCE

- corpus historique dense ;
- collisions historiques jusqu'à `_7` observées ;
- familles : rapports annuels, états financiers, T1/S1/T3, CAC/attestations ;
- 2024 contient notamment T1/S1/T3, rapport CAC annuel et attestation CAC annuelle ;
- 2025 contient S1 et T3 dans le corpus observé.

## P1-R — ETIT 2023

Document inspecté : `2023_Etats_Financiers_ETIT.pdf` (Drive ID `1F1SVX_IHyXZjaNrx2cJ5LVfwjE1eAGoj`).

Vérifications :

- 6 pages, PDF Excel natif ;
- états financiers **consolidés IFRS** ;
- compte de résultat et situation financière détaillés en **milliers de dollars US** ;
- page de synthèse publie simultanément **milliers USD** et **millions FCFA** ;
- variations publiées peuvent différer entre USD et FCFA ;
- résultat consolidé ventilé entre `part du Groupe`, `détenteurs autres capitaux propres` et `intérêts minoritaires`.

Conséquence de modélisation : `source_currency` reste au niveau du fact. Nouvelle dimension candidate documentée : `ownership_attribution_raw`. Aucune modification SQL pendant P1.

## Restant transversal

`SHA256 = NOT_COMPLETE` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = NOT_COMPLETE`.
