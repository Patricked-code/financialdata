# P1 SOURCE — checkpoint inventaire live V13

Date : 2026-08-11
Dépôt canonique : `Patricked-code/financialdata`
Branche autorisée : `main` uniquement.

## État

- sociétés : **48 / 48** ;
- total live précédent V12 : **3 043 PDF** ;
- SIBC précédent : **46 PDF** ;
- revérification SIBC strictement par ses 10 dossiers parents + `mimeType = application/pdf` : **49 PDF** ;
- delta SIBC : **+3 PDF** ;
- nouveau total live V13 : **3 046 PDF**.

## Règle de preuve

Le delta est persisté avant tout calcul SHA SIBC. Aucun fichier n'est fusionné ou supprimé sur la base du nom, du suffixe ou de la taille seule.

## Particularités SIBC observées au recheck

- 2016 : deux états financiers physiques ;
- 2017 : trois rapports T1 physiques (`plain`, `_2`, `_3`) de même taille **60 027 octets** + CAC S1 + T3 + états financiers ;
- 2018 : T1, deux CAC annuels, S1, T3, deux états financiers nommés `_rev` / `_rev_2`, rapport annuel ;
- 2020 : T1, deux S1, T3, deux états financiers ;
- 2021 : T1, CAC annuel, S1, T3, états financiers ;
- 2022 : T1, deux S1, T3 et un rapport d'activité supplémentaire ;
- 2023 : T1/S1/CAC S1/T3/annuel ;
- 2024 : T1/S1/CAC S1/T3/annuel ;
- 2025 : T1/S1/T3.

Statut : `INVENTORY_COMPLETE_48_OF_48_LIVE_REFRESH_V13 / SIBC_HASH_PENDING`.
