# P1 SOURCE — CFAO Motors Côte d'Ivoire / CFAC

Date : 2026-08-20
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / HASH_PENDING / VERSION_REVIEW`

- Ticker : `CFAC`
- Dossier Drive canonique : `1y_h696cNzQjE9QnGaR8913zVMd9IkA7y`
- sous-dossiers directs live : **26 années** : `1999–2004`, `2006–2025`
- dossiers `1998` et `2005` : non observés dans le root courant ; aucune absence métier n'est inférée sans preuve SOURCE
- snapshot avant recheck : **94 PDF**
- recheck live strict parent-scoped : **114 PDF**
- delta live : **+20**
- SOURCE global : **V23 = 3 157 PDF**
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v23_20260820.md`

## Preuve de cardinal live

Le corpus a été recompté sur deux sous-périmètres disjoints des mêmes parents SOURCE :

- `1999–2012` : **58 PDF** ;
- `2013–2025` : **56 PDF** ;
- total live : **114 PDF**.

Le périmètre SOURCE est défini par les parent IDs Drive réels, jamais par une recherche ticker seule.

## Particularités SOURCE

- fortes familles historiques physiques : 2008 jusqu'à `_8`, 2011 jusqu'à `_11` ;
- ces suffixes ne déterminent ni doublon ni version ; tous les objets restent séparés jusqu'au SHA et à la revue de contenu ;
- 2018 combine états financiers, T1, rapport d'activité juin, communication financière T3 et attestations CAC ; ces rôles documentaires ne sont pas fusionnés ;
- 2023 contient notamment `2023_Etats_Financiers_CFAC_rev.pdf` ;
- 2024 contient T1 et T1_2, plus S1, annuel et états financiers ;
- profil P1-R important : les publications CFAO peuvent mêler faits propres à l'émetteur et données de marché automobile/marques ; conserver `subject_scope_raw` et références externes séparées.

## Règles de preuve

- `EXACT_DUPLICATE` uniquement sur SHA-256 identique ;
- `VERSION_OF` seulement avec preuve sémantique suffisante ;
- `SUPERSEDES` jamais sur suffixe ou ordre de fichiers ; preuve explicite requise ;
- SOURCE physique immuable.

## Passe suivante exacte

1. matérialiser les **114/114 PDF** de la whitelist live V23 ;
2. valider tailles et signatures `%PDF-` ;
3. calculer SHA-256 sur 100 % ;
4. identifier les groupes exacts sans supprimer aucun objet ;
5. revoir seulement les familles sémantiques justifiées lorsque les SHA diffèrent ;
6. créer `inventory/hashes/CFAC.csv` avec sérialisation LF ;
7. calculer le Git blob local et vérifier le blob GitHub post-commit ;
8. finaliser CFAC, manifeste, doublons, `SUIVI.md` et `TODO.md`.

## Restant transversal

`SHA256 = IN_PROGRESS` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = LIVE_RECHECK_COMPLETE_FOR_CURRENT_SCOPE`.
