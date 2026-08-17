# P1 INVENTORY — Africa Global Logistics Côte d'Ivoire / AGLC

Date de vérification initiale : 2026-08-09  
Dernière revérification live : 2026-08-17

Drive folder : `1gqUo-CWEAgwARVyATFA7F0Rgy7NAi2ec`

Statut : `FILE_INVENTORIED / LIVE_RECHECKED_NO_DELTA / SHA256_COMPLETE / VERSION_REVIEWED`

## Arborescence live

- sous-dossiers directs : **28 années**, `1998–2025` ;
- dossier `divers` : **non observé** ;
- contrôle strict : les 28 IDs de dossiers parents ont été regroupés dans une recherche `mimeType = application/pdf` ;
- PDF live : **60** ;
- snapshot précédent : **60** ;
- delta : **0**.

Le recheck consolidé du 2026-08-17 couvre exhaustivement les dossiers annuels 1998–2025 et retourne 60 objets PDF. Aucun nouveau dénominateur n'est donc à versionner ; l'état global V14 reste **3 060 PDF**.

## Validation binaire / SHA-256

Les **60/60** fichiers live ont été matérialisés depuis Google Drive puis contrôlés sur les octets réels.

Résultat :

- matérialisation : **60/60** ;
- tailles Drive ↔ fichiers locaux : **60/60 conformes** ;
- signatures `%PDF-` : **60/60 valides** ;
- SHA-256 calculés : **60/60** ;
- SHA-256 uniques : **60** ;
- collisions exactes : **0** ;
- groupes `EXACT_DUPLICATE` ajoutés par AGLC : **0**.

Registre canonique : `inventory/hashes/AGLC.csv`.

Contrôle post-commit : le Git blob SHA du CSV généré localement est `4c25045ffeb194aad7929b3b106a6fe6b7c7241c`, identique au blob SHA retourné par GitHub après écriture. Le registre persisté est donc bit-for-bit identique au registre calculé localement.

## Caractéristiques documentaires importantes

- nombreuses variantes historiques jusqu'à `_9` ;
- ces variantes présentent des tailles et SHA différents : aucun suffixe `_2`…`_9` n'est assimilé à un doublon ;
- 2020 contient séparément des rapports CAC sur **comptes individuels IFRS** et **comptes consolidés IFRS** ;
- ces deux documents 2020 sont des sources distinctes par scope comptable et ne doivent jamais être fusionnés du seul fait qu'ils concernent le même exercice ;
- 2025 contient `2025_Rapport_T1_AGLC.pdf` et `2025_Rapport_T1_AGLC_rev.pdf` ;
- les deux objets 2025 sont binaires distincts : **550 603 octets / SHA `942c3016…`** pour le plain et **551 567 octets / SHA `d57c1517…`** pour `_rev`.

## Revue de version — T1 2025 plain vs `_rev`

La comparaison textuelle du contenu montre que les deux publications portent sur la même période et conservent les mêmes chiffres T1 2025, mais `_rev` modifie au moins une donnée comparative annuelle : la valeur de référence du **résultat net 2024** passe de **17 138 527 KFCFA** dans le plain à **21 068 974 KFCFA** dans `_rev`.

La combinaison :

- même période T1 2025 ;
- nom explicite `_rev` ;
- contenu quasi identique sur la publication courante ;
- correction substantielle d'une donnée comparative ;

permet de qualifier les deux fichiers comme **versions distinctes de la même publication T1 2025**.

Cependant, aucune formule explicite `annule et remplace` / `supersedes` n'a été observée dans le contenu extrait. En conséquence :

- relation de version : **établie** ;
- doublon exact : **NON** ;
- `supersedes_source_file_id` : **ne pas renseigner automatiquement sans preuve explicite supplémentaire**.

## Dimensions à préserver dans le manifeste documentaire

Pour AGLC, le framework comptable, le scope et la version doivent être modélisés indépendamment :

- `accounting_framework` : ex. IFRS ;
- `reporting_scope` : individuel / consolidé ;
- `period` / `fiscal_year` ;
- `document_type` ;
- `version_status` ;
- relation `VERSION_OF` lorsque prouvée ;
- `supersedes_source_file_id` uniquement sur preuve explicite de supersession.

La coexistence des rapports CAC IFRS individuels et consolidés 2020 confirme qu'un document ne peut pas être identifié uniquement par `(issuer, year, document_type)`.

## Règles de version / doublon confirmées

- suffixe `_2`, `_3`, … `_9` ≠ doublon ;
- suffixe `_rev` seul ≠ preuve suffisante de supersession ;
- même période ≠ même binaire ;
- même exercice + même framework ≠ même scope ;
- seul un SHA-256 identique sur les octets matérialisés permet `EXACT_DUPLICATE` ;
- une relation de version peut être établie par convergence du nom, de la période et d'un delta de contenu cohérent ;
- `SUPERSEDES` reste une relation plus forte et nécessite une preuve explicite supplémentaire.

## Impact global après AGLC

- total SOURCE live : **3 060 PDF** ;
- SHA validés avant AGLC : **935** ;
- SHA AGLC ajoutés : **60** ;
- SHA validés après AGLC : **995 / 3 060 = 32,52 %** ;
- PDF restant à hasher : **2 065** ;
- groupes exacts globaux : **11** (AGLC n'en ajoute aucun).

## P1 restant pour AGLC

La passe SOURCE/SHA est terminée. Restent uniquement les travaux transverses :

- backfill du manifeste documentaire détaillé ;
- propagation de `accounting_framework` et `reporting_scope` pour les documents IFRS ;
- propagation de la relation de version T1 2025 plain / `_rev` sans renseigner `supersedes_source_file_id` sans preuve explicite ;
- qualification fine des périodes économiques et types documentaires ;
- P1-R / reconnaissance PDF lorsque le corpus transverse sera traité.

## Point de reprise AGLC

`AGLC_LIVE=60 | DELTA=0 | SHA=60/60 | UNIQUE_SHA=60 | EXACT_DUPLICATE_GROUPS=0 | STATUS=SHA256_COMPLETE | NEXT=BICC_LIVE_RECHECK_AND_SHA`
