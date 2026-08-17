# P1 INVENTORY — Bank of Africa Niger / BOAN

Date de vérification initiale : 2026-08-09  
Dernière revérification live et SHA : 2026-08-17

Drive folder : `1qtb3jsPG28k_C3JNuEU35oKWhK5y41Xa`

Statut : `FILE_INVENTORIED / LIVE_RECHECKED_NO_DELTA / SHA256_COMPLETE / REMOTE_DELTA_IDENTIFIED`

## Sous-dossiers directs

28 dossiers : années `1999` à `2025` incluses + `divers`.

Aucun dossier `1998` n'a été observé dans l'arborescence directe actuelle.

## Nombre de fichiers par dossier de classement — live 2026-08-17

| Dossier | Snapshot | Live | Delta |
|---|---:|---:|---:|
| 1999 | 1 | 1 | 0 |
| 2000 | 1 | 1 | 0 |
| 2001 | 1 | 1 | 0 |
| 2002 | 1 | 1 | 0 |
| 2003 | 2 | 2 | 0 |
| 2004 | 1 | 1 | 0 |
| 2005 | 2 | 2 | 0 |
| 2006 | 2 | 2 | 0 |
| 2007 | 2 | 2 | 0 |
| 2008 | 1 | 1 | 0 |
| 2009 | 0 | 0 | 0 |
| 2010 | 2 | 2 | 0 |
| 2011 | 3 | 3 | 0 |
| 2012 | 4 | 4 | 0 |
| 2013 | 2 | 2 | 0 |
| 2014 | 4 | 4 | 0 |
| 2015 | 0 | 0 | 0 |
| 2016 | 0 | 0 | 0 |
| 2017 | 0 | 0 | 0 |
| 2018 | 4 | 4 | 0 |
| 2019 | 3 | 3 | 0 |
| 2020 | 4 | 4 | 0 |
| 2021 | 5 | 5 | 0 |
| 2022 | 3 | 3 | 0 |
| 2023 | 3 | 3 | 0 |
| 2024 | 4 | 4 | 0 |
| 2025 | 4 | 4 | 0 |
| divers | 1 | 1 | 0 |
| **TOTAL** | **60** | **60** | **0** |

### Règle de preuve du recheck

La revérification du 2026-08-17 a été faite depuis les 28 dossiers parents réels avec filtre strict `mimeType = application/pdf`, en quatre groupes couvrant exhaustivement `1999`–`2025` + `divers`.

Résultat : **60 PDF live**, identique au snapshot. Aucun delta n'est donc ajouté au total global V14, qui reste **3 060 PDF**. Aucun checkpoint de delta supplémentaire n'était requis avant SHA.

## Résultat SHA-256

- fichiers physiques live : **60** ;
- fichiers matérialisés depuis Drive : **60 / 60** ;
- tailles Drive ↔ fichiers locaux concordantes : **60 / 60** ;
- signatures PDF `%PDF` valides : **60 / 60** ;
- SHA-256 calculés : **60 / 60** ;
- SHA-256 uniques : **60** ;
- groupes `EXACT_DUPLICATE` : **0** ;
- registre canonique : `inventory/hashes/BOAN.csv`.

Aucun des suffixes historiques `_2`, `_3`, `_4`, `_5` ne produit une collision SHA dans le corpus BOAN live. Toutes les variantes restent donc des sources binaires distinctes ; une éventuelle relation de version sémantique devra être établie séparément depuis le contenu, jamais depuis le suffixe seul.

## Familles documentaires observées

- rapports annuels historiques ;
- rapports T1/T3 ;
- rapports S1/S2 ;
- états financiers ;
- attestations CAC ;
- rapports CAC annuels ;
- fiche boursière dans `divers` ;
- noms source non standardisés sur certaines périodes.

## Dossiers vides confirmés au live recheck

`2009, 2015, 2016, 2017`.

Règle : ne pas interpréter ces dossiers vides comme absence de données économiques sans revue du contenu des autres documents et du catalogue BRVM.

## `divers` — période résolue depuis le contenu

`fiche_ne_0.pdf` porte explicitement :

- `BANK OF AFRICA-NIGER` ;
- `INFORMATION BOURSIERE S1 2017` ;
- données semestrielles / cours au `30/06/2017`.

Qualification : **fiche d'information boursière S1 2017**.

La période est déterminée depuis le contenu source, non depuis le nom `fiche_ne_0.pdf` ou le dossier `divers`.

## Candidats versions / collisions de nom

Nombreux rapports annuels historiques portent des suffixes `_2`, `_3`, `_4`, `_5` :

- 2003 : rapport annuel + `_2` ;
- 2005 : rapport annuel + `_2` ;
- 2006 : rapport annuel + `_2` ;
- 2007 : rapport annuel + `_3` ;
- 2010 : rapport annuel + `_4` ;
- 2011 : `_2`, `_3`, `_4` ;
- 2012 : `_2`, `_3`, `_4`, `_5` ;
- 2014 : `_2`, `_3`, `_4`, `_5`.

La passe SHA établit qu'aucun de ces 60 objets n'est un doublon binaire exact d'un autre objet BOAN live. Ils doivent tous rester conservés dans SOURCE.

## Delta BRVM courant observé le 2026-08-09

La page officielle BRVM de BOA Niger publie actuellement, entre autres :

- rapport d'activités T1 2026 ;
- rapport d'activités S2 2025 ;
- rapport CAC sur les états financiers annuels 2025 ;
- rapport CAC sur conventions réglementées / crédits dirigeants 2025 ;
- rapport du Conseil d'administration à l'AGO 2025 ;
- rapport T3 2025 ;
- attestation CAC S1 2025 ;
- rapport S1 2025 ;
- rapport T1 2025.

Le dossier Drive 2025 live contient T1, S1, attestation CAC S1 et T3, mais pas les équivalents évidents des publications S2/annuelles/Conseil 2025, et il n'existe pas encore de dossier 2026.

Statut : `REMOTE_DELTA_IDENTIFIED`.

Ces publications ne sont pas téléchargées automatiquement pendant P1. Elles servent à valider le futur collecteur incrémental V2.

## Points P1 restant à faire pour BOAN

- relations de versions sémantiques historiques quand le contenu le justifie ;
- expliquer les trous 2009 et 2015–2017 via revue documentaire/P1-FRESH, sans supposition ;
- backfill du manifeste transverse avec tailles, dates, checksums et métadonnées temporelles ;
- rapprochement contrôlé avec le catalogue BRVM courant via le collecteur V2.

Le live recheck, la matérialisation binaire, la validation taille/PDF, le SHA-256 et la revue des doublons exacts sont terminés.

## Point de reprise BOAN

`BOAN_LIVE=60 | SNAPSHOT=60 | DELTA=0 | SHA=60/60 | UNIQUE_SHA=60 | EXACT_DUPLICATE_GROUPS=0 | STATUS=SHA256_COMPLETE`
