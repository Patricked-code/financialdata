# P1 INVENTORY — Bank of Africa Mali / BOAM

Date de vérification : 2026-08-11

Drive folder : `127BPCvkfMC25L3hXZ4dKo1NEW_eg0FRK`

Statut : `FILE_INVENTORIED / LIVE_FRESHNESS_RECHECKED / SHA256_COMPLETE / VERSION_REVIEW_COMPLETE / REMOTE_DELTA_IDENTIFIED`

## Sous-dossiers directs

16 dossiers : `2010, 2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, divers`.

Le dossier `2015` n'est pas présent.

## Nombre de fichiers par dossier de classement

Revérification live 2026-08-11, strictement par dossiers parents + MIME PDF :

| Dossier | Fichiers |
|---|---:|
| 2010 | 1 |
| 2011 | 3 |
| 2012 | 2 |
| 2013 | 0 |
| 2014 | 0 |
| 2016 | 1 |
| 2017 | 3 |
| 2018 | 2 |
| 2019 | 4 |
| 2020 | 5 |
| 2021 | 4 |
| 2022 | 5 |
| 2023 | 7 |
| 2024 | 4 |
| 2025 | 2 |
| divers | 1 |
| **TOTAL** | **44** |

Le total live reste **44 PDF** : aucun delta par rapport au snapshot précédent.

## Dossiers vides / lacunes de classement

- dossiers 2013 et 2014 présents mais sans PDF direct ;
- dossier 2015 absent.

Ne pas transformer ces constats de classement en absence économique sans analyse des comparatifs et sources distantes.

## SHA-256

- **44 / 44 PDF matérialisés et hashés** ;
- **44 / 44 tailles Drive ↔ fichiers hashés validées** ;
- **42 SHA uniques** ;
- **2 groupes de doublons binaires exacts** ;
- registre : `inventory/hashes/BOAM.csv` ;
- revue : `inventory/reviews/BOAM_VERSION_REVIEW_20260811.md`.

### Doublons exacts BOAM

1. `2023_Etats_Financiers_BOAM.pdf` = `2023_Rapport_CAC_Annuel_BOAM.pdf`
   - 824 078 octets ;
   - SHA `77f20998d8b1def30299a400bbe4584093fb54a6e40d05f7ab5fa7721896e31e`.
2. `2024_Rapport_CAC_Annuel_BOAM.pdf` = `2024_Rapport_CAC_Annuel_BOAM_2.pdf`
   - 742 080 octets ;
   - SHA `dc403fad3b516f6a94eecefafb56db518987c5fb3097edd0d68a7ffe8077f207`.

Les quatre objets physiques sont conservés ; aucune suppression silencieuse.

### Même taille mais contenus distincts

- `2019_Rapport_T3_BOAM.pdf` et `2019_Rapport_T4_BOAM.pdf` font tous deux 86 241 octets mais ont des SHA différents ; verdict `BINARY_DISTINCT`.

## Version explicitement nommée `_rev`

`2021_Etats_Financiers_BOAM_rev.pdf` :

- Drive ID `1EWdFXD8BAVYdiPDXGPmiTb6nKAhGRYFv` ;
- 946 214 octets ;
- SHA `ab2c020c621d63911d9611d22507931a617b72ac5fdcc0d32dfcd9d00d8c1a82` ;
- PDF image de 4 pages ;
- revue visuelle : états financiers S1 2021 certifiés/signés ;
- aucune mention visible `annule et remplace`, `corrigé` ou `révision` ;
- recherche Drive ciblée : aucun prédécesseur BOAM 2021 distinct retrouvé.

Verdict : `PREDECESSOR_NOT_FOUND / NO_SUPERSESSION_PROVEN`. Le suffixe `_rev` seul ne constitue pas une preuve de supersession.

## Variantes historiques

- 2011 `_2/_3/_4` : tailles et SHA distincts ;
- 2012 `_2/_3` : tailles et SHA distincts ;
- elles restent des sources indépendantes tant qu'une revue sémantique dédiée n'établit pas leur relation.

## Documents de gouvernance/corporate

Le document `rapport_du_conseil_dadministration_-_assemblee_generale_ordinaire_-_boa_mali.pdf` est conservé comme SOURCE corporate distincte et pourra alimenter plus tard `corporate_facts_raw` / `event_facts_raw` selon son contenu.

## Delta BRVM courant

Le delta officiel identifié reste documenté : publications 2025 supplémentaires et T1 2026 visibles côté BRVM mais non représentées par leurs équivalents évidents dans le Drive actuel.

Statut : `REMOTE_DELTA_IDENTIFIED`. Ce delta sera traité par le collecteur V2 ; il n'est pas injecté artificiellement dans le corpus Drive historique.

## Points P1 restant

- consolidation du manifeste document-level dans le maître ;
- périodes économiques fines ;
- éventuelle revue sémantique des anciennes variantes historiques ;
- rapprochement contrôlé du delta BRVM courant.
