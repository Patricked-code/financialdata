# P1 — CHECKPOINT 48 ÉMETTEURS — V3 LIVE REFRESH

Date : 2026-08-09
Statut : `INVENTORY_COMPLETE_48_OF_48 / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE`

## Historique des snapshots de la session

- V1 : **2 950 PDF** ;
- V2 : **2 957 PDF** après delta CBIBF `+7` ;
- V3 courant : **2 964 PDF** après delta ORAC `+7` supplémentaire.

Les snapshots précédents restent conservés dans Git et ne sont jamais écrasés silencieusement.

## Delta ORAC

Premier inventaire ORAC : **14 PDF**.

État live revérifié : **21 PDF** :

- 2022 : 3 ;
- 2023 : 6 ;
- 2024 : 7 ;
- 2025 : 5.

Sept documents supplémentaires sont apparus lors de la revérification, avec des `created_time` Drive autour de 06:33–06:34Z :

1. `2022_Rapport_Annuel_ORAC.pdf`
2. `2022_Rapport_Annuel_ORAC_rev.pdf`
3. `resultats_financiers_consolides_2023_-_orange_ci.pdf`
4. `2023_Rapport_Annuel_ORAC.pdf`
5. `2023_Rapport_Annuel_ORAC_2.pdf`
6. `2024_Rapport_Annuel_ORAC.pdf`
7. `rapport_rse_2024_-_orange_ci.pdf`

## État live courant

- sociétés : **48 / 48** ;
- PDF SOURCE : **2 964** ;
- delta cumulé depuis V1 : **+14 PDF** ;
- émetteurs ayant muté pendant la passe observée : CBIBF et ORAC.

## Leçon opérationnelle renforcée

Le corpus Drive peut être modifié pendant une passe longue. Le contrôle `P1-FRESH` ne doit donc pas être conçu uniquement comme une opération future ponctuelle : le manifeste doit conserver `first_seen_at`, `last_seen_at` et des snapshots de référence permettant d'expliquer tout changement de total.

## Prochain état

`LIVE_TOTAL = 2964 → COMPLETE_ORAC_MANIFEST_AND_SHA → CONTINUE_SHORT_CORPORA`
