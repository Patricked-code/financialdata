# P1 SOURCE — Orange Côte d'Ivoire / ORAC

Date : 2026-08-09
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED`

- Ticker : `ORAC`
- Dossier Drive : `1BgjEsarpAEHdhsD1pzvTgNFrT9q4aRjj`
- Dossiers directs : **4** (`2022`, `2023`, `2024`, `2025`)
- Premier inventaire de session : **14 PDF**
- État Drive live revérifié : **21 PDF**
- Delta live : **+7 PDF**

## État live par année

- 2022 : **3 PDF** — états financiers, annuel, annuel `_rev` ;
- 2023 : **6 PDF** — T1, T3, CAC S1, résultats financiers consolidés, annuel, annuel `_2` ;
- 2024 : **7 PDF** — T1, S1, T3, CAC S1, états financiers, annuel, rapport RSE ;
- 2025 : **5 PDF** — T1, S1, T3, CAC S1, états financiers.

## Delta live observé

Les sept fichiers absents du premier inventaire mais présents lors de la revérification sont :

- `2022_Rapport_Annuel_ORAC.pdf` ;
- `2022_Rapport_Annuel_ORAC_rev.pdf` ;
- `resultats_financiers_consolides_2023_-_orange_ci.pdf` ;
- `2023_Rapport_Annuel_ORAC.pdf` ;
- `2023_Rapport_Annuel_ORAC_2.pdf` ;
- `2024_Rapport_Annuel_ORAC.pdf` ;
- `rapport_rse_2024_-_orange_ci.pdf`.

Leurs `created_time` Drive observés se situent autour de `2026-08-09T06:33–06:34Z`, après le premier passage d'inventaire.

## P1-R

Les dimensions télécom/abonnés/data/mobile/technologie sont déjà couvertes par le deep pilot SNTS. La présence d'un rapport RSE est une nouvelle famille documentaire SOURCE à classifier, mais elle ne justifie pas à elle seule une nouvelle table RAW avant inspection de son contenu.

## Restant transversal ORAC

`DOCUMENT_MANIFEST_ORAC = IN_PROGRESS` ; `SHA256_ORAC = NOT_COMPLETE` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
