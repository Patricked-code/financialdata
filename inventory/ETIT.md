# P1 SOURCE — Ecobank Transnational Incorporated / ETIT

Date : 2026-08-18
Statut : `P1_INVENTORIED / P1-R_PROFILED / LIVE_SOURCE_DELTA_DETECTED / HASH_PENDING`

- Ticker : `ETIT`
- Dossier Drive canonique : `183KoqvNUQNaj6kdfw80PkkIGupbvuSia`
- Dossiers directs live : **23**, continus de `2003` à `2025`
- Snapshot avant recheck : **81 PDF**
- Recheck live strict parent-scoped : **100 PDF**
- Delta live : **+19**
- SOURCE global : **V21 = 3 133 PDF**
- Checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v21_20260818.md`

## Preuve de cardinal live

Le résultat global atteint le plafond de 100 du connecteur. Le cardinal a donc été recompté sur deux sous-périmètres disjoints des mêmes dossiers enfants :

- années `2003–2014` : **51 PDF** ;
- années `2015–2025` : **49 PDF** ;
- total live : **100 PDF**.

Le corpus contient des noms non normalisés ou portant des identités de filiales du groupe, notamment `ra_-_ecobank_tg_-_excercice_2010.pdf`. Le périmètre est donc défini par les dossiers SOURCE réels, jamais par une recherche ticker seule.

## Particularités SOURCE

- corpus historique dense ;
- variantes historiques jusqu'à `_7` observées ;
- familles : rapports annuels, états financiers, T1/S1/T3, CAC/attestations ;
- 2024 contient notamment T1/S1/T3, rapport CAC annuel et attestation CAC annuelle ;
- 2025 contient S1 et T3 dans le corpus observé ;
- tous les objets physiques sont conservés ;
- aucun suffixe ne constitue une preuve de doublon ou de version.

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

## Passe suivante exacte

1. matérialiser les **100/100 PDF** de la liste live parent-scoped ;
2. valider tailles et signatures `%PDF-` ;
3. calculer SHA-256 sur 100 % ;
4. identifier les groupes exacts sans supprimer aucun objet ;
5. revoir seulement les familles sémantiques justifiées lorsque les SHA diffèrent ;
6. créer `inventory/hashes/ETIT.csv` avec sérialisation LF ;
7. calculer le Git blob local et vérifier le blob GitHub post-commit ;
8. finaliser ETIT, manifeste, doublons, `SUIVI.md` et `TODO.md`.

## Restant transversal

`SHA256 = IN_PROGRESS` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = NOT_COMPLETE`.
