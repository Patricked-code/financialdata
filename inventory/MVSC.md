# P1 SOURCE — MOVIS Côte d'Ivoire / MVSC

Date : 2026-08-09
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / SHA_COMPLETE`

- Ticker : `MVSC`
- Dossier Drive : `1t7fHRCP2m_dvq5XdVXhNxQSVpjBPlevJ`
- Dossiers directs : **24** = années `1998` à `2020` + `divers`
- Premier inventaire de session : **20 PDF**
- État Drive live revérifié par parents + MIME : **35 PDF**
- Delta live : **+15 PDF**

## Particularités SOURCE

- collisions historiques `_2/_3` nombreuses, notamment 2003, 2005, 2007, 2009, 2011, 2012, 2013 ;
- états financiers 2015/2018/2019 ;
- 2019 comporte deux fichiers d'états financiers ;
- `divers_Etats_Financiers_MVSC.pdf` nécessite résolution de période depuis le contenu ;
- 2020 comporte notamment T1 ;
- plusieurs fichiers ajoutés pendant la session ont des `created_time` Drive autour de 06:35Z.

## SHA-256

Les **35 PDF** ont été matérialisés depuis Drive et hashés avec contrôle des tailles.

- `SHA256_MVSC = COMPLETE_35_35` ;
- contenus binaires uniques : **35 / 35** ;
- doublons binaires exacts trouvés : **0** ;
- registre : `inventory/hashes/MVSC.csv`.

Les trois variantes 2003, les couples 2005/2007/2009/2011/2012/2013 et les deux états financiers 2019 ont tous des SHA différents. Leur relation sémantique éventuelle reste à établir par contenu.

## Règle

Aucun suffixe `_2`/`_3` n'est interprété comme doublon ou révision sans preuve. Le fichier `divers` reste SOURCE avec période économique non résolue.

## P1-R

Les particularités logistiques, de cession et de résultat HAO déjà repérées restent couvertes par les règles existantes ; aucune nouvelle règle de schéma n'est créée ici.

## Restant transversal

`DOCUMENT_MANIFEST_MVSC = ROW_COVERAGE_35_35 / SHARD_BACKFILL_PENDING` ; `SHA256_MVSC = COMPLETE_35_35` ; `BINARY_DUPLICATES = NONE_FOUND` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
