# P1 INVENTORY — Bernabé Côte d'Ivoire / BNBC

Date : 2026-08-18
Statut : `P1_INVENTORIED / LIVE_RECHECK_COMPLETE / SHA256_COMPLETE / VERSION_REVIEW_PARTIAL`

- Ticker : `BNBC`
- Dossier Drive canonique : `10u65PBoBi1nWppgn1Ttm-r96iCwdzsKs`
- Sous-dossiers directs live : **28**, années `1998–2025`
- Dossier `divers` : non observé
- Snapshot manifeste avant recheck : **78 PDF**
- Recheck live strict par les **28 parent IDs réels** + `mimeType='application/pdf'` : **92 PDF**
- Delta live : **+14**
- SOURCE global : **V20 = 3 114 PDF**
- Checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v20_20260818.md`

## Cardinal annuel live vérifié

`1998–2002: 1/an` ; `2003–2008: 2/an` ; `2009–2011: 4/an` ; `2012: 5` ; `2013: 4` ; `2014: 3` ; `2015: 2` ; `2016: 3` ; `2017: 4` ; `2018: 5` ; `2019: 9` ; `2020: 6` ; `2021: 5` ; `2022: 5` ; `2023: 3` ; `2024: 6` ; `2025: 3`.

## SHA-256 / intégrité

- **92/92** objets live matérialisés ;
- **92/92** signatures `%PDF-` valides ;
- tailles contrôlées ;
- **92 SHA-256 uniques** ;
- **0 groupe `EXACT_DUPLICATE`** dans BNBC ;
- aucun objet SOURCE supprimé, fusionné ou renommé ;
- registre : `inventory/hashes/BNBC.csv` ;
- registre local LF : **15 303 octets** ;
- Git blob local calculé : `fb567fcdbf57af2aa6bb017544d2c29583e8359f` ;
- blob GitHub post-commit : `fb567fcdbf57af2aa6bb017544d2c29583e8359f` ;
- validation bit-for-bit : **OK**.

## Revue de versions / périodes à haute valeur

### États financiers 2019

Les cinq objets physiques restent distincts.

- `2019_Etats_Financiers_BNBC.pdf` et `2019_Etats_Financiers_BNBC_2.pdf` sont deux binaires distincts de 41 pages correspondant à la même publication économique IFRS annuelle 2019. Leur texte est quasi identique, avec notamment une correction de la date d'arrêté/approbation du Conseil (`08 Mai 2020` versus `08 juin 2020`). Relation conservatrice : `VERSION_OF`. Pas `EXACT_DUPLICATE`. Pas `SUPERSEDES` faute de preuve explicite de remplacement.
- `_3` est une publication synthétique des résultats annuels 2019 ;
- `_4` est un état financier de synthèse au 31/12/2019 ;
- `_5` est une publication de résultats annuels provisoires 2019.

Ces trois publications d'une page ne sont pas fusionnées avec les états IFRS complets ni entre elles.

### Rapports S1 2020

- `2020_Rapport_S1_BNBC.pdf` : publication explicitement présentée selon les normes IFRS ;
- `2020_Rapport_S1_BNBC_2.pdf` : autre publication semestrielle, avec présentation et agrégats différents.

Les deux binaires et leurs contenus sont distincts. Aucun doublon exact, aucune relation `SUPERSEDES` et aucun collapse sémantique n'est appliqué sans preuve supplémentaire.

### États financiers 2024 — garde-fou de période

- `2024_Etats_Financiers_BNBC.pdf` porte bien sur l'exercice clos au **31/12/2024** ;
- `2024_Etats_Financiers_BNBC_2.pdf`, malgré son nom physique, porte explicitement dans son contenu sur l'exercice clos au **31/12/2023**.

La période économique de `_2` doit donc être **2023**, et non 2024. Le nom de fichier ne prévaut jamais sur le contenu source.

## Doublons globaux

BNBC n'ajoute aucun groupe exact. `inventory/p1_duplicate_groups.csv` reste inchangé pour cette passe.

## Restant transversal

`SHA256 = COMPLETE` ; `LIVE_RECHECK = COMPLETE` ; `VERSION_LINKS = PARTIAL_REVIEW_COMPLETE` ; `ECONOMIC_PERIODS = PARTIAL` ; `REMOTE_FRESHNESS = NOT_COMPLETE`.

La suite P1 pour BNBC consiste au backfill du manifeste documentaire et des périodes économiques fines, sans remettre en cause le registre SOURCE/SHA désormais verrouillé.
