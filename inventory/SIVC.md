# P1 SOURCE — Air Liquide Côte d'Ivoire / ERIUM Côte d'Ivoire / SIVC

Date de vérification : 2026-08-12

Drive folder : `1TkwLDXla5LKvdpQ_KSEFrl_yNz-X1AB2`

Statut : `P1_INVENTORIED / LIVE_SOURCE_RECHECKED_NO_DELTA / SHA256_COMPLETE`

## Identité émetteur

- ticker historique/courant : `SIVC` ;
- le corpus historique Drive est classé sous **Air Liquide Côte d'Ivoire** ;
- les publications récentes 2025 utilisent **ERIUM Côte d'Ivoire** ;
- la fiche officielle BRVM courante identifie le symbole `SIVC` comme **ERIUM Côte d'Ivoire** ;
- l'historique de dénomination doit être conservé dans `issuer_names_history` lors de l'implémentation physique du modèle ; les sources historiques Air Liquide ne sont pas renommées rétroactivement.

## Sous-dossiers directs

22 dossiers annuels :

`2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025`

Constats :

- aucun dossier `2015` observé ;
- aucun dossier `divers` observé ;
- dossier `2024` présent mais vide au recheck live ;
- présence de noms standardisés et de noms source non standardisés.

## Revérification live 2026-08-12

La revérification stricte par les **22 dossiers parents** avec `mimeType = application/pdf` retrouve exactement **53 PDF**, soit le même total que l'inventaire précédent.

- snapshot précédent : **53 PDF** ;
- live courant : **53 PDF** ;
- delta : **0** ;
- total projet V13 inchangé : **3 046 PDF** ;
- dossier 2024 toujours vide ;
- aucun dossier 2015 découvert.

## Nombre de fichiers par dossier de classement

| Dossier | Fichiers |
|---|---:|
| 2003 | 1 |
| 2004 | 1 |
| 2005 | 1 |
| 2006 | 2 |
| 2007 | 2 |
| 2008 | 2 |
| 2009 | 2 |
| 2010 | 3 |
| 2011 | 3 |
| 2012 | 4 |
| 2013 | 4 |
| 2014 | 2 |
| 2016 | 2 |
| 2017 | 4 |
| 2018 | 2 |
| 2019 | 2 |
| 2020 | 4 |
| 2021 | 3 |
| 2022 | 2 |
| 2023 | 2 |
| 2024 | 0 |
| 2025 | 5 |
| **TOTAL** | **53** |

## SHA-256

- **53 / 53 PDF matérialisés et hashés** ;
- **53 / 53 fichiers disponibles localement après téléchargement brut Drive** ;
- tailles locales recalculées et cohérentes avec les tailles transmises par les téléchargements Drive ;
- **53 SHA uniques** ;
- **0 groupe de doublons binaires exacts** dans SIVC ;
- registre : `inventory/hashes/SIVC.csv`.

Les suffixes `_2`, `_3`, `_4`, `_5` historiques ne correspondent donc à aucun doublon binaire exact dans le corpus SIVC actuel. Les relations sémantiques éventuelles entre variantes restent à déterminer par le contenu, sans fusion ni suppression.

Exemples binaires distincts :

- 2010 : plain / `_3` / `_4` ;
- 2011 : `_2` / `_3` / `_4` ;
- 2012 : `_2` à `_5` ;
- 2013 : `_2` à `_5` ;
- 2016 : deux états financiers ;
- 2019 : deux états financiers.

## Version explicitement signalée par la source — T3 2025

Source :

`erium_ci_resultat_3t2025_annule_et_remplace_le_precedent_publie.pdf`

- Drive ID : `1443Ihn5G-NgeGJ-CYFXY-DtLbwICtfwN` ;
- taille : **185 609 octets** ;
- SHA-256 : `890ab3dfb48b58ec48bbe17783576658bd96bb51db83f607517887b6d057dbc2` ;
- PDF : **1 page** ;
- couche texte native exploitable : **absente** ;
- document rendu visuellement et revu ;
- titre visible : **« RAPPORT D’ACTIVITÉ DU TRIMESTRE 3 - ANNÉE 2025 »** ;
- identité visible : **ERIUM Côte d'Ivoire** ;
- date visible : **30/12/2025** ;
- signataire visible : **Alexandre DUFOUR, Directeur Général**.

Le contenu visible publie notamment, en K. FCFA :

| Indicateur | 3e trimestre 2025 | 3e trimestre 2024 | Année 2024 | Variation valeur | Variation % |
|---|---:|---:|---:|---:|---:|
| Chiffre d'affaires | 7 584 696 | 6 730 448 | 9 282 599 | 854 248 | 13 % |
| Résultat des activités ordinaires | 1 121 984 | 670 917 | 247 248 | 451 067 | 67 % |
| Résultat net | 832 519 | 525 539 | 376 957 | 306 980 | 58 % |

Le nom source indique explicitement **« annule et remplace le précédent publié »**. Une recherche Drive ciblée sur le T3 2025 ERIUM/SIVC n'a toutefois retrouvé que ce fichier de remplacement : le document précédent n'est pas présent dans le corpus Drive actuel.

Verdict de version :

`SUPERSEDES_EXPLICIT / TARGET_SOURCE_NOT_FOUND / REVIEW_REQUIRED`

Aucun `supersedes_source_file_id` n'est inventé. Le fichier de remplacement reste une source physique autonome et la cible devra être reliée si elle est retrouvée ultérieurement via P1-FRESH/BRVM.

## Familles de documents observées

- rapports annuels ;
- états financiers ;
- T1 ;
- T3 ;
- S1 ;
- S2 ;
- attestations CAC ;
- rapports CAC ;
- publications avec nom source non standardisé ;
- publication de remplacement explicitement signalée.

## Points restant transversaux

- `SHA256 = COMPLETE_53_OF_53` ;
- `EXACT_DUPLICATES = NONE_53_UNIQUE` ;
- `VERSION_LINKS = PARTIAL`, avec cible du T3 2025 remplacé à retrouver ;
- `ECONOMIC_PERIODS = PARTIAL` ;
- `ISSUER_NAME_HISTORY = AIR_LIQUIDE_TO_ERIUM_CONFIRMED_CURRENT_BRVM_SYMBOL_SIVC` ;
- absence de dossier 2015 et dossier 2024 vide à conserver comme faits SOURCE tant qu'aucune preuve supplémentaire n'est trouvée.
