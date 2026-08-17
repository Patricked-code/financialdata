# P1 SOURCE — Palm Côte d'Ivoire / PALC

Date : 2026-08-17
Statut : `FILE_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / HASH_PENDING / VERSION_REVIEW`

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

## Particularités SOURCE vérifiées au recheck 2026-08-17

- historique long avec nombreuses collisions `_2/_3/_4/_5/_6` ;
- `2009_Rapport_Annuel_PALC_rev.pdf` reste un candidat de révision, sans relation automatique avant SHA/contenu ;
- le corpus live contient des fichiers génériques/non strictement normalisés, notamment `efp_-_palm_ci_-_2014.pdf` et `190430_rapport_dactivite_2nd_semestre_2018_-_palm_ci.pdf` ;
- les périodes S2 sont explicitement présentes, notamment 2016 et 2019 ;
- états financiers, T1/T3, CAC/attestations sont présents selon les années ;
- 2025 contient au moins T1, T3 et attestation CAC S1 dans le corpus live ;
- le périmètre SOURCE est défini par l'arborescence canonique parent-scoped, jamais par la seule présence de `PALC` dans un nom.

## P1-R

Les dimensions agribusiness/production/campagne/prix/volumes envisagées dans la passe conceptuelle sont conservées. Aucun nouveau champ n'est ajouté sans preuve supplémentaire issue du contenu.

## Passe suivante exacte

1. matérialiser les **98/98 PDF** de la liste live parent-scoped ;
2. valider tailles et signatures `%PDF-` ;
3. calculer SHA-256 sur 100 % ;
4. identifier les groupes exacts sans supprimer aucun objet ;
5. revoir les variantes historiques et `2009_Rapport_Annuel_PALC_rev.pdf` par contenu ;
6. créer `inventory/hashes/PALC.csv` et valider son blob GitHub post-commit ;
7. finaliser PALC, manifeste, doublons, `SUIVI.md` et `TODO.md` ;
8. passer ensuite à `BNBC`.

## Restant transversal

`SHA256 = IN_PROGRESS` ; `VERSION_LINKS = IN_PROGRESS` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = NOT_COMPLETE`.
