# P1 SOURCE — Sucrivoire / SCRC

Date : 2026-08-11
Statut : `P1_INVENTORIED / LIVE_FRESHNESS_RECHECKED / SHA256_COMPLETE / DIVERS_PERIOD_RESOLVED`

- Ticker : `SCRC`
- Dossier Drive : `1m-s-huOspVZl3312kk7WzDHMNZUSq1M_`
- Dossiers directs : **11** = années `2016–2025` + `divers`
- PDF live revérifiés strictement par dossiers parents + MIME : **45**
- Delta live : **0** ; le total projet reste inchangé.

## Répartition live

2016=1 ; 2017=8 ; 2018=4 ; 2019=1 ; 2020=4 ; 2021=6 ; 2022=6 ; 2023=6 ; 2024=6 ; 2025=2 ; divers=1.

## Particularités SOURCE

- 2017 contient T1, deux publications S1 physiques, T3, T4 et trois états financiers ;
- plusieurs états financiers coexistent également en 2018, 2020, 2021, 2022 et 2023 ;
- toutes ces sources restent séparées jusqu'à preuve documentaire de leur relation ;
- 2025 contient T1 et S1 dans le corpus Drive live observé.

## SHA-256

- **45 / 45 PDF matérialisés et hashés** ;
- **45 / 45 tailles Drive ↔ fichiers hashés validées** ;
- **45 SHA uniques** ;
- **zéro doublon binaire exact** ;
- registre : `inventory/hashes/SCRC.csv`.

Conséquences :

- EF 2017 `plain/_2/_3` : tous binaires distincts ;
- EF 2018 `plain/_2` : binaires distincts ;
- EF 2020 `plain/_2` : binaires distincts ;
- EF 2021 `plain/_2` : binaires distincts ;
- EF 2022 `plain/_2/_3` : tous binaires distincts ;
- EF 2023 `plain/_2` : binaires distincts.

Aucune relation de supersession n'est inférée du suffixe seul.

## Résolution du fichier `divers`

`divers_Attestation_CAC_Annuel_SCRC.pdf` :

- Drive ID `1bJk2Q8szZpkKoSGmGVz2bru4sm5k-Vzc` ;
- 240 044 octets ;
- SHA `1017baf64505570b898184dc66475746fc0269e10899e7988b10e62e7434ffdc` ;
- PDF image d'une page, sans couche texte native exploitable ;
- revue visuelle : **Attestation des Commissaires aux Comptes sur le tableau d'activités et de résultat et le rapport d'activité semestriel au 30 juin 2017** ;
- période explicitement couverte : **1er janvier au 30 juin 2017** ;
- date de l'attestation : **20 octobre 2017** ;
- période résolue : `S1_2017`.

Le nom historique contient `Annuel`, mais le contenu prouve qu'il s'agit d'une attestation **semestrielle S1 2017**. La période documentaire est donc déterminée par le contenu et non par le nom ni le dossier `divers`.

## P1-R

Les dimensions agribusiness/production/campagne/volumes sont déjà prévues. T4 est déjà une période reconnue. Aucun nouveau champ conceptuel n'est requis par cette passe.

## Restant transversal

`SHA256 = COMPLETE_45_OF_45` ; `DIVERS_PERIOD = RESOLVED_S1_2017` ; `VERSION_LINKS = CONTENT_REVIEW_REMAINING_FOR_BINARY_DISTINCT_VARIANTS` ; `ECONOMIC_PERIODS = PARTIAL` ; `REMOTE_FRESHNESS = RECHECKED_NO_DELTA`.
