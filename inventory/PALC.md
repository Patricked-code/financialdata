# P1 SOURCE — Palm Côte d'Ivoire / PALC

Date : 2026-08-17
Statut : `FILE_INVENTORIED / LIVE_SOURCE_DELTA_HASH_COMPLETE / SHA256_COMPLETE / VERSION_REVIEW_COMPLETE`

- Ticker : `PALC`
- Dossier Drive canonique : `1w2XGE38g12wfH6Dm0UdZKAraYmg7vzNZ`
- Dossiers directs live : **25**
- Couverture observée : `1999`, `2001`, puis `2003–2025`
- Dossiers non observés : **1998, 2000, 2002**
- Snapshot manifeste avant recheck : **75 PDF**
- Recheck live strict par les **25 parent IDs réels** + `mimeType='application/pdf'` : **98 PDF**
- Delta live : **+23**
- SOURCE global : **V19 = 3 100 PDF**
- Checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v19_20260817.md`

## Résultat binaire PALC — V19

- **98/98** objets matérialisés ;
- **98/98** signatures `%PDF-` valides ;
- **96 SHA-256 uniques** ;
- **2 groupes de doublons exacts**, tous les objets physiques restant conservés :
  1. `2007_Rapport_Annuel_PALC_2.pdf` / `2007_Rapport_Annuel_PALC_3.pdf` — SHA `5c7b218089532b8275bff06fc0c3e9199fc891b5c12c03cdf373f4c182982c1c` ;
  2. `2018_Rapport_T3_PALC.pdf` / `2018_Rapport_T3_PALC_2.pdf` — SHA `ae8fd065f86a129033728594ecc5162eda448e2a99624c218b2e55c05e24fe00`.
- registre : `inventory/hashes/PALC.csv` ;
- validation post-commit bit-for-bit : blob local = GitHub `5dbe863af2b7b3854b0a6e20d29cb67c6a9f7a35`.

## Revue de version 2009

`2009_Rapport_Annuel_PALC.pdf` et `2009_Rapport_Annuel_PALC_rev.pdf` sont deux binaires distincts correspondant à la même publication économique 2009. La comparaison de contenu met en évidence des corrections de postes, notamment sur la valeur ajoutée, l'EBE et des transferts de charges. Aucune mention explicite de type `annule et remplace` n'a été trouvée.

Verdict conservateur : **`VERSION_OF`**, pas `EXACT_DUPLICATE`, et aucun `SUPERSEDES` automatique.

## Particularités SOURCE confirmées

- les fichiers génériques `efp_-_palm_ci_-_2014.pdf` et `190430_rapport_dactivite_2nd_semestre_2018_-_palm_ci.pdf` font bien partie des 98 objets grâce au périmètre parent-scoped ;
- les suffixes `_2/_3/_4/_5/_6` ne déterminent jamais seuls une relation ;
- S2 est réellement présent en 2016 et 2019 ;
- états financiers, T1/T3, CAC/attestations et rapports annuels sont conservés comme objets documentaires distincts ;
- 2025 contient T1, T3 et attestation CAC S1 dans le corpus observé.

## P1-R

Les dimensions agribusiness/production/campagne/prix/volumes envisagées dans la passe conceptuelle sont conservées. Aucun nouveau champ n'est ajouté sans preuve supplémentaire issue du contenu.

## Suite exacte

1. mettre à jour le registre global des doublons avec les deux groupes PALC ;
2. basculer PALC en `SHA256_COMPLETE` dans le manifeste ;
3. synchroniser `SUIVI.md` et `TODO.md` sur V19 ;
4. passer à **BNBC**, snapshot manifeste 78 PDF, avec recheck live strict avant SHA.

## Restant transversal

`SHA256 = IN_PROGRESS_GLOBAL` ; `VERSION_LINKS = IN_PROGRESS` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = NOT_COMPLETE`.
