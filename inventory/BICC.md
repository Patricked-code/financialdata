# P1 INVENTORY — BICICI / BICC

Date de vérification initiale : 2026-08-09  
Dernière revérification live : 2026-08-17

Drive folder : `1v9YYGnG5rny3-5CUDLMrgMNY3-84L1x9`

Statut : `FILE_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / HASH_PENDING / VERSION_REVIEW`

## Arborescence live

- sous-dossiers directs : **28 années**, `1998–2025` ;
- dossier `divers` : **non observé** ;
- snapshot précédent : **61 PDF** ;
- revérification stricte des 28 IDs de dossiers parents avec `mimeType = application/pdf` : **70 PDF** ;
- delta : **+9 PDF** ;
- nouveau total SOURCE global : **3 069 PDF** ;
- checkpoint du nouveau dénominateur : `inventory/P1_48_ISSUERS_CHECKPOINT_v15_20260817.md`.

Le delta V15 est persisté avant tout SHA BICC. Aucune conclusion de doublon ou de version n'est tirée des noms.

## Familles documentaires observées

- rapports annuels / états financiers ;
- T1, T2, T3, T4, S1 ;
- attestations CAC ;
- publications de résultats ;
- nombreuses variantes historiques suffixées `_2`, `_3`, etc.

## Points de revue version / qualité

- `2019_Etats_Financiers_BICC.pdf` et `2019_Etats_Financiers_BICC_rev.pdf` : relation de révision à vérifier par SHA puis contenu ;
- `2022_Rapport_T3_BICC.pdf` et `2022_Rapport_T3_BICC_2.pdf` : comparer sans supposer un doublon ;
- présence explicite de **T2 2022**, à préserver séparément de **S1 2022** ;
- `bilan_et_compte_de_resultat_bicici_31_12_2022_.pdf` reste un profil P1-R utile pour la reconnaissance d'états financiers.

## Règles de preuve

- suffixe `_2`, `_3`, etc. ≠ doublon ;
- suffixe `_rev` ≠ preuve suffisante de `SUPERSEDES` ;
- même période ≠ même document ;
- seul un SHA-256 identique sur les octets matérialisés permet `EXACT_DUPLICATE` ;
- les relations de version sont qualifiées séparément depuis le contenu et/ou une mention source explicite.

## P1 restant pour BICC

1. matérialiser **70/70** PDF live ;
2. valider tailles Drive ↔ fichiers locaux ;
3. valider signatures PDF ;
4. calculer SHA-256 exhaustif ;
5. produire `inventory/hashes/BICC.csv` ;
6. qualifier les groupes exacts éventuels ;
7. comparer en profondeur les variantes 2019 plain / `_rev` et T3 2022 plain / `_2` ;
8. revalider le registre après commit ;
9. passer BICC à `SHA256_COMPLETE` seulement après ces contrôles ;
10. poursuivre le backfill manifeste / périodes / P1-R en transverse.

## Point de reprise BICC

`BICC_SNAPSHOT=61 | BICC_LIVE=70 | DELTA=+9 | GLOBAL_SOURCE=3069 | HASH=PENDING`
