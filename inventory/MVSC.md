# P1 SOURCE — MOVIS Côte d'Ivoire / MVSC

Date : 2026-08-09
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED`

- Ticker : `MVSC`
- Dossier Drive : `1t7fHRCP2m_dvq5XdVXhNxQSVpjBPlevJ`
- Dossiers directs : **24** = années `1998` à `2020` + `divers`
- Premier inventaire de session : **20 PDF**
- État Drive live revérifié par parents + MIME : **35 PDF**
- Delta live : **+15 PDF**

## Particularités SOURCE

- couverture documentaire plus dense qu'au premier passage après ajout de nouveaux rapports historiques ;
- collisions historiques `_2/_3` nombreuses, notamment 2003, 2005, 2007, 2009, 2011, 2012, 2013 ;
- états financiers 2015/2018/2019 ;
- 2019 comporte deux fichiers d'états financiers à rapprocher par contenu/hash ;
- `divers_Etats_Financiers_MVSC.pdf` nécessite résolution de période depuis le contenu ;
- 2020 comporte notamment T1 ;
- plusieurs fichiers ajoutés pendant la session ont des `created_time` Drive autour de 06:35Z.

## Règle

Le total live est obtenu sans filtre de nom, uniquement par les 24 dossiers parents et `mimeType = application/pdf`. Aucun suffixe `_2`/`_3` n'est interprété comme doublon avant SHA-256.

## P1-R

Les particularités logistiques, de cession et de résultat HAO déjà repérées restent couvertes par les règles existantes ; aucune nouvelle règle de schéma n'est créée ici.

## Restant transversal

`DOCUMENT_MANIFEST_MVSC = IN_PROGRESS` ; `SHA256_MVSC = NOT_COMPLETE` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
