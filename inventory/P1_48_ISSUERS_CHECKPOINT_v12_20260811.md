# P1 SOURCE — checkpoint inventaire live V12

Date : 2026-08-11
Dépôt canonique : `Patricked-code/financialdata`
Branche autorisée : `main` uniquement.

## État

- sociétés : **48 / 48** ;
- total live précédent V11 : **3 041 PDF** ;
- TTLS précédent : **45 PDF** ;
- revérification TTLS strictement par ses 11 dossiers parents + `mimeType = application/pdf` : **47 PDF** ;
- delta TTLS : **+2 PDF** ;
- nouveau total live V12 : **3 043 PDF**.

## Règle de preuve

Le delta est enregistré avant tout calcul SHA TTLS. Aucun fichier n'est ajouté ou supprimé sur la base du nom seul. Les 47 objets Drive seront matérialisés et hashés comme sources physiques distinctes.

## Particularités TTLS observées au recheck

- 2016 : trois états financiers `plain/_2/_3` + rapport S1 ;
- 2017 : rapport T1, bilan semestriel de contrat de liquidité, projet de publication des états financiers 2017 et états financiers 2017 ;
- 2018 : deux rapports annuels de même taille **3 058 310 octets**, à départager par SHA ;
- `divers_Rapport_CAC_Annuel_TTLS.pdf` reste à dater depuis son contenu ;
- 2021/2022/2023/2024 contiennent plusieurs variantes/familles financières ;
- 2024 compte 7 objets physiques dans le live recheck ;
- 2025 contient T1/S1/T3.

Statut : `INVENTORY_COMPLETE_48_OF_48_LIVE_REFRESH_V12 / TTLS_HASH_PENDING`.
