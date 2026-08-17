# P1 INVENTORY — Africa Global Logistics Côte d'Ivoire / AGLC

Date de vérification initiale : 2026-08-09  
Dernière revérification live : 2026-08-17

Drive folder : `1gqUo-CWEAgwARVyATFA7F0Rgy7NAi2ec`

Statut : `FILE_INVENTORIED / LIVE_RECHECKED_NO_DELTA / HASH_PENDING / VERSION_REVIEW`

## Arborescence live

- sous-dossiers directs : **28 années**, `1998–2025` ;
- dossier `divers` : **non observé** ;
- contrôle strict : les 28 IDs de dossiers parents ont été regroupés dans une recherche `mimeType = application/pdf` ;
- PDF live : **60** ;
- snapshot précédent : **60** ;
- delta : **0**.

Le recheck consolidé du 2026-08-17 couvre exhaustivement les dossiers annuels 1998–2025 et retourne 60 objets PDF. Aucun nouveau dénominateur n'est donc à versionner ; l'état global V14 reste **3 060 PDF**.

## Caractéristiques documentaires importantes

- nombreuses collisions/suffixes historiques jusqu'à `_9` ;
- 2020 contient séparément des rapports CAC sur **comptes individuels IFRS** et **comptes consolidés IFRS** ;
- ces deux documents 2020 sont des sources distinctes par scope comptable et ne doivent jamais être fusionnés du seul fait qu'ils concernent le même exercice ;
- 2025 contient `2025_Rapport_T1_AGLC.pdf` et `2025_Rapport_T1_AGLC_rev.pdf` ;
- les deux objets 2025 restent conservés séparément : le nom `_rev` suggère une version mais ne constitue pas à lui seul une preuve de relation `supersedes` ;
- leurs tailles Drive sont différentes : **550 603 octets** pour le plain et **551 567 octets** pour `_rev`, ce qui exclut déjà un doublon exact par taille, sans préjuger de la relation sémantique.

## Dimensions à préserver dans le manifeste documentaire

Pour AGLC, le framework comptable et le scope doivent être modélisés indépendamment :

- `accounting_framework` : ex. IFRS ;
- `reporting_scope` : individuel / consolidé ;
- `period` / `fiscal_year` ;
- `document_type` ;
- `version_status` / `supersedes_source_file_id` uniquement sur preuve de contenu ou métadonnée explicite.

La coexistence des rapports CAC IFRS individuels et consolidés 2020 confirme qu'un document ne peut pas être identifié uniquement par `(issuer, year, document_type)`.

## Règles de version / doublon

- suffixe `_2`, `_3`, … `_9` ≠ doublon ;
- suffixe `_rev` ≠ preuve suffisante de supersession ;
- même période ≠ même document ;
- même exercice + même framework ≠ même scope ;
- seul un SHA-256 identique sur les octets matérialisés permet `EXACT_DUPLICATE` ;
- les relations `REVISION`, `SUPERSEDES`, `SAME_PERIOD_DIFFERENT_SCOPE` doivent être établies séparément depuis le contenu et/ou les métadonnées source.

## P1 restant pour AGLC

- matérialiser **60/60** fichiers live ;
- valider tailles Drive ↔ fichiers locaux ;
- valider signatures PDF ;
- calculer SHA-256 exhaustif ;
- produire `inventory/hashes/AGLC.csv` ;
- qualifier les éventuels groupes exacts ;
- revoir les variantes historiques `_2`…`_9` ;
- comparer en profondeur `2025_Rapport_T1_AGLC.pdf` et `_rev` pour établir ou non une relation de version ;
- conserver explicitement la distinction IFRS individuel / consolidé en 2020 ;
- backfill du manifeste documentaire transverse.

## Point de reprise AGLC

`AGLC_LIVE=60 | SNAPSHOT=60 | DELTA=0 | HASH=PENDING | T1_2025_PLAIN_AND_REV=PRESERVED`
