# P1 SOURCE — CIE / CIEC

Date de vérification initiale : 2026-08-09  
Dernière revérification live / SHA : 2026-08-17

Statut : `FILE_INVENTORIED / LIVE_RECHECK_COMPLETE / SHA256_COMPLETE / DEEP_PILOT_ALREADY_EXISTS`

- Émetteur : CIE
- Ticker : `CIEC`
- Dossier Drive : `1y6IMougiA8lTlwDmGYcjIa_PeT4Nzgz3`
- Dossiers directs : **29** = `1998–2025 + divers`
- snapshot précédent : **61 PDF**
- live strict parent-scoped : **62 PDF**
- delta : **+1 PDF**
- total SOURCE global V16 : **3 070 PDF**
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v16_20260817.md`
- registre SHA : `inventory/hashes/CIEC.csv`

Le delta V16 a été enregistré avant tout SHA CIEC, conformément à la doctrine de versionnement du SOURCE.

## Résultat de la passe SHA

- PDF matérialisés : **62 / 62** ;
- signatures `%PDF-` valides : **62 / 62** ;
- SHA-256 calculés : **62 / 62** ;
- SHA uniques : **61** ;
- groupes exacts CIEC : **1** ;
- validation post-commit du registre : Git blob local = GitHub **`be1e68b95394d3c921adf506af3f0736b8d0c753`**.

### Doublon exact 2016

Les deux objets physiques suivants sont strictement identiques :

- `2016_Etats_Financiers_CIEC.pdf` — Drive `1jtB4CDDdfb5BsVNc3fcjEKgXAoBmpqbI` ;
- `2016_Etats_Financiers_CIEC_2.pdf` — Drive `1WB5HpE5QcsXszAxjy1kgnVcEzOBVFP42`.

SHA commun : `87c568d69a67b3fe08befd474a348ab1e15d5c1ccadc035d2f751eda6cd4d0b8`.

Relation : `EXACT_DUPLICATE`. Les deux sources physiques sont conservées ; aucune suppression silencieuse.

### États financiers 2017 plain / `_rev`

- `2017_Etats_Financiers_CIEC.pdf` : 205 461 octets, 1 page, SHA `e4b995b117d56a7d92af90fdfe118b5c5a599b9e288783fb4223d4aa43a3532a` ;
- `2017_Etats_Financiers_CIEC_rev.pdf` : 603 584 octets, 1 page, SHA `71c4b64cd909364599b59f875ad28713d445d155548a1757c46e3627c7c7e3d1`.

Les binaires sont distincts. L'inspection du contenu montre la même publication économique 2017 et les mêmes valeurs principales, mais sous une représentation physique différente. La relation à retenir est **`VERSION_OF`**, jamais `EXACT_DUPLICATE`.

Aucune formule explicite `annule et remplace` n'a été observée : ne pas renseigner automatiquement `supersedes_source_file_id`.

## Particularités SOURCE préservées

- historique long avec rapports annuels, états financiers, T1/S1/T3 et CAC ;
- attestations et rapports CAC conservés séparément des états financiers ;
- `divers` fait partie du périmètre live ;
- les suffixes `_2`, `_3`, `_4`, `_5`, `_6`, `_rev` ne dictent jamais seuls une relation ;
- plusieurs variantes historiques de même millésime ont des tailles et SHA différents et restent donc des objets SOURCE distincts ;
- même année ≠ même période, scope ou type documentaire.

## P1-R

CIEC est déjà un `DEEP_PILOT` conceptuel : scopes CIE propre vs Secteur/Autorité concédante, valeurs monétaires/physiques, STOCK/FLOW, individuel/consolidé et concession. Cette analyse n'est pas réinitialisée ; la passe SHA complète désormais la couche de preuve binaire qui doit être réutilisée par le futur manifeste RAW.

## Restant transversal CIEC

- backfill du manifeste documentaire maître et des métadonnées temporelles fines ;
- relations sémantiques/version restantes au-delà des cas prouvés ci-dessus ;
- réconciliation P1-FRESH / fraîcheur distante BRVM ;
- aucune extraction P3 exhaustive prématurée.

## Point de reprise

`CIEC_SNAPSHOT=61 | CIEC_LIVE=62 | DELTA=+1 | SHA=62/62 | UNIQUE_SHA=61 | EXACT_DUPLICATE_GROUPS=1 | VERSION_2017=VERSION_OF | GLOBAL_SOURCE=3070 | NEXT=NEXT_UNHASHED_ISSUER_LIVE_RECHECK`
