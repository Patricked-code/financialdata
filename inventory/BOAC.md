# P1 INVENTORY — Bank of Africa Côte d'Ivoire / BOAC

Date de vérification initiale : 2026-08-09  
Dernière revérification live et SHA : 2026-08-17

Drive folder : `1GNIORLdGneVshpR3oOBmq2_xDxKAu86g`

Statut : `FILE_INVENTORIED / LIVE_SOURCE_DELTA_HASH_COMPLETE / REMOTE_DELTA_IDENTIFIED`

## Sous-dossiers directs

19 dossiers : années `2008` à `2025` incluses + `divers`.

## Nombre de fichiers par dossier — live V14

| Dossier | V13 | Live V14 | Delta |
|---|---:|---:|---:|
| 2008 | 0 | 1 | +1 |
| 2009 | 0 | 2 | +2 |
| 2010 | 2 | 4 | +2 |
| 2011 | 3 | 4 | +1 |
| 2012 | 4 | 5 | +1 |
| 2013 | 3 | 4 | +1 |
| 2014 | 2 | 4 | +2 |
| 2015 | 3 | 3 | 0 |
| 2016 | 2 | 2 | 0 |
| 2017 | 4 | 4 | 0 |
| 2018 | 5 | 6 | +1 |
| 2019 | 7 | 7 | 0 |
| 2020 | 5 | 5 | 0 |
| 2021 | 3 | 5 | +2 |
| 2022 | 4 | 5 | +1 |
| 2023 | 4 | 4 | 0 |
| 2024 | 4 | 4 | 0 |
| 2025 | 3 | 3 | 0 |
| divers | 2 | 2 | 0 |
| **TOTAL** | **60** | **74** | **+14** |

Checkpoint du delta : `inventory/P1_48_ISSUERS_CHECKPOINT_v14_20260817.md`.

Le delta a été persisté avant tout calcul SHA BOAC. Aucun objet n'a été supprimé, déplacé, fusionné ou dédupliqué.

## Résultat SHA-256

- fichiers physiques live : **74** ;
- fichiers matérialisés et contrôlés : **74 / 74** ;
- signatures PDF valides : **74 / 74** ;
- SHA-256 calculés : **74 / 74** ;
- SHA-256 uniques : **73** ;
- groupes `EXACT_DUPLICATE` : **1** ;
- registre : `inventory/hashes/BOAC.csv`.

### Groupe exact BOAC

`2021_Rapport_S1_BOAC.pdf` et `2021_Rapport_S1_BOAC_2.pdf` sont binaires identiques :

- taille : **1 559 400 octets** chacun ;
- SHA-256 : `7e69b8618e901a4bb72442989a23913f47f268b9093c0a380461d5626ede0c97` ;
- statut : `EXACT_DUPLICATE` ;
- les deux objets physiques restent conservés dans SOURCE ;
- groupe enregistré dans `inventory/p1_duplicate_groups.csv`.

### Paire de même taille mais non identique

`2019_Etats_Financiers_BOAC.pdf` et `2019_Etats_Financiers_BOAC_2.pdf` font tous deux **314 350 octets**, mais leurs SHA sont différents :

- plain : `367077d13d7bc67231c4614bf104f6618ad0acc14d3177eee4e47f71b1a7fa68` ;
- `_2` : `b801a64942b0611e6a24a39ce7800990d648817bfbfc3465565e69f9f835d044`.

Conclusion : `NOT_EXACT_DUPLICATE`. Cette paire confirme que la taille ou le suffixe de nom ne constituent jamais une preuve de doublon.

## Familles observées

- rapports annuels historiques ;
- états financiers ;
- rapports T1/T3 ;
- rapports S1 ;
- attestations CAC ;
- rapports CAC annuels ;
- publications avec noms source non standardisés ;
- fiche boursière dans `divers`.

## Dossiers anciennement vides

L'inventaire du 2026-08-09 indiquait `2008` et `2009` comme vides. La revérification du 2026-08-17 constate désormais :

- `2008` : 1 PDF ;
- `2009` : 2 PDF.

Plusieurs objets nouvellement visibles dans les dossiers historiques ont un `createdTime` Drive du 2026-08-09 vers 06:36–06:37, postérieur à l'inventaire initial effectué plus tôt ce jour-là.

Règle : dossier vide ≠ absence de période économique ; l'état live doit être revérifié avant chaque passe transverse.

## `divers` — périodes résolues depuis le contenu

Deux fichiers observés :

- `fiche_ci_0.pdf` : fiche d'information boursière **S1 2017** de BANK OF AFRICA - CÔTE D'IVOIRE ;
- `divers_Rapport_S1_BOAC.pdf` : rapport d'activité du **1er semestre 2022**, période confirmée depuis le contenu.

La période n'est pas déduite du dossier ou du nom ; le contenu source prévaut.

## Candidats versions / collisions de noms

Les nombreux suffixes `_2`, `_3`, `_4`, `_5` sur les rapports annuels historiques ont été conservés comme sources physiques distinctes. La passe SHA ne permet de qualifier `EXACT_DUPLICATE` que lorsqu'une égalité binaire est réellement démontrée.

Pour BOAC, un seul groupe exact est prouvé : la paire S1 2021 décrite ci-dessus. Les autres variantes restent distinctes au niveau binaire et peuvent encore nécessiter une revue sémantique/versionnelle ultérieure.

## Delta BRVM courant identifié le 2026-08-09

La page officielle courante BOA Côte d'Ivoire publie notamment :

- `Rapport des Commissaires Aux Comptes et Etats Financiers annuels - Exercice 2025` ;
- `Rapport d'activités - 1er trimestre 2026`.

URLs PDF observées :

- `https://www.brvm.org/sites/default/files/20260612_-_rapport_des_commissaires_aux_comptes_et_etats_financiers_annuels_-_exercice_2025_-_boa_ci.pdf`
- `https://www.brvm.org/sites/default/files/20260601_-_rapport_dactivites_-_1er_trimestre_2026_-_boa_ci.pdf`

Dans le corpus Drive live V14 :

- le dossier 2025 contient T1, S1 et T3 ;
- aucun dossier 2026 n'est présent ;
- l'état financier 2025 courant et le T1 2026 ne sont donc toujours pas représentés dans le Drive inventorié.

Statut : `REMOTE_DELTA_IDENTIFIED`.

Important : ce delta BRVM externe est distinct du delta Drive interne +14 constaté en V14. P1 documente le delta distant ; il ne télécharge pas automatiquement ces documents tant que le collecteur V2 et le manifeste incrémental ne sont pas validés.

## Conséquence pour le collecteur

BOAC confirme le besoin de :

- `first_seen_at` / `last_seen_at` ;
- comparaison du catalogue courant au manifeste local ;
- téléchargement incrémental ;
- détection de nouvelle version ;
- suivi des documents distants absents localement.

Voir `docs/BRVM_COLLECTOR_V2_PLAN.md`.

## Points P1 restant à faire pour BOAC

- validation sémantique détaillée des types/versionnements historiques quand nécessaire ;
- rapprochement contrôlé avec le delta BRVM courant ;
- backfill du manifeste documentaire avec tailles/dates/checksums et métadonnées temporelles ;
- intégration dans les shards du manifeste transverse.

Le live recheck, la matérialisation binaire, le SHA-256 et la revue des doublons exacts sont terminés.

## Point de reprise BOAC

`BOAC_LIVE=74 | V13=60 | DELTA=+14 | CHECKPOINT=V14 | SHA=74/74 | UNIQUE_SHA=73 | EXACT_DUPLICATE_GROUPS=1 | STATUS=SHA256_COMPLETE`
