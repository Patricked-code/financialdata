# P1 INVENTORY — BICICI / BICC

Date de vérification initiale : 2026-08-09  
Dernière revérification live : 2026-08-17

Drive folder : `1v9YYGnG5rny3-5CUDLMrgMNY3-84L1x9`

Statut : `FILE_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / SHA256_COMPLETE / VERSION_REVIEWED`

## Arborescence live

- sous-dossiers directs : **28 années**, `1998–2025` ;
- dossier `divers` : **non observé** ;
- snapshot précédent : **61 PDF** ;
- revérification stricte des 28 IDs de dossiers parents avec `mimeType = application/pdf` : **70 PDF** ;
- delta : **+9 PDF** ;
- nouveau total SOURCE global : **3 069 PDF** ;
- checkpoint du nouveau dénominateur : `inventory/P1_48_ISSUERS_CHECKPOINT_v15_20260817.md`.

Le delta V15 a été persisté avant tout calcul SHA BICC. Aucun fichier n'a été fusionné, supprimé ou considéré comme doublon/version depuis son seul nom.

## Validation binaire / SHA-256

Les **70/70** objets BICC live ont été matérialisés depuis Google Drive puis contrôlés sur les octets réels.

Résultat :

- matérialisation : **70/70** ;
- signatures `%PDF-` : **70/70 valides** ;
- SHA-256 calculés : **70/70** ;
- SHA uniques : **69** ;
- groupes `EXACT_DUPLICATE` BICC : **1** ;
- registre canonique : `inventory/hashes/BICC.csv`.

Contrôle post-commit du registre : le Git blob SHA calculé localement est `25baddade1e9e0366f3bdabfa6cdb2f13a5993ae`, identique au blob SHA retourné par GitHub. Le CSV persisté est donc bit-for-bit identique au registre calculé localement.

## Groupe exact BICC — T3 2022

Les deux objets suivants sont bit-for-bit identiques :

- `2022_Rapport_T3_BICC.pdf` — Drive `1zOqtr-21SLNEMglhF2yFHZcrW9bOYerZ` ;
- `2022_Rapport_T3_BICC_2.pdf` — Drive `1XErrwQrKfqlbdNlhV_LYGBLx5e_VUfit`.

Preuve :

- taille : **123 093 octets** pour chacun ;
- SHA-256 commun : `492df4551aa01c2e97415323331b50a3f4eed65e952d38e2e97b7a524b64fae0`.

Relation : `EXACT_DUPLICATE`. Les deux objets physiques restent conservés dans SOURCE et sont enregistrés dans `inventory/p1_duplicate_groups.csv`.

## Revue de version — états financiers 2019

Deux sources distinctes coexistent :

- `2019_Etats_Financiers_BICC.pdf` — **167 078 octets**, SHA `00e21938c93e2d77fcf845812d18c6057e66eca9fd46db7c7d537480358ebd9b` ;
- `2019_Etats_Financiers_BICC_rev.pdf` — **677 267 octets**, SHA `9f3de16a9334927b813b94804e209c2a68a09f4c8a1bb1827e63b07ff349cd33`.

La comparaison textuelle montre :

- même exercice et mêmes états financiers 2019 ;
- mêmes valeurs économiques principales ;
- la variante `_rev` contient une présentation plus complète et un commentaire explicatif supplémentaire relatif notamment aux provisions liées aux crises cacao/anacarde et à des dysfonctionnements de paramétrage du système d'information ayant influencé les arrêtés de comptes.

Qualification : **versions distinctes de la même publication / `VERSION_OF`**.

Aucune mention explicite `annule et remplace` / `supersedes` n'a été trouvée. En conséquence, `supersedes_source_file_id` ne doit pas être renseigné automatiquement.

## Périodes / familles documentaires à préserver

- T1, T2, T3, T4 et S1 sont des périodes distinctes ;
- la présence de **T2 2022** et **S1 2022** confirme qu'elles ne doivent jamais être assimilées ;
- rapports annuels, états financiers, attestations CAC et publications de résultats restent des types documentaires séparés ;
- `bilan_et_compte_de_resultat_bicici_31_12_2022_.pdf` reste un profil P1-R utile pour la reconnaissance des états financiers.

## Règles de preuve confirmées

- suffixe `_2`, `_3`, etc. ≠ doublon ;
- suffixe `_rev` ≠ preuve suffisante de `SUPERSEDES` ;
- même taille ≠ doublon tant que le SHA n'est pas identique ;
- même période ≠ même document ;
- seul un SHA-256 identique sur les octets matérialisés permet `EXACT_DUPLICATE` ;
- une relation `VERSION_OF` reste distincte d'une relation plus forte `SUPERSEDES`.

## Impact global après BICC

- total SOURCE live V15 : **3 069 PDF** ;
- SHA validés avant BICC : **995** ;
- SHA BICC ajoutés : **70** ;
- SHA validés après BICC : **1 065 / 3 069 = 34,70 %** ;
- PDF restant à hasher : **2 004** ;
- groupes exacts globaux : **12**.

## P1 restant pour BICC

La passe SOURCE/SHA est terminée. Restent les travaux transverses :

- backfill du manifeste documentaire détaillé ;
- propagation de la relation de version EF 2019 plain / `_rev` ;
- qualification fine des périodes/types documentaires ;
- P1-R et reconnaissance PDF ;
- aucune suppression des objets physiques historiques.

## Point de reprise BICC

`BICC_SNAPSHOT=61 | BICC_LIVE=70 | DELTA=+9 | SHA=70/70 | UNIQUE_SHA=69 | EXACT_DUPLICATE_GROUPS=1 | GLOBAL_SOURCE=3069 | GLOBAL_SHA=1065/3069 | NEXT=CIEC_LIVE_RECHECK_AND_SHA`
