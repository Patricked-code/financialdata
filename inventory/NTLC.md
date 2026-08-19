# P1 SOURCE — Nestlé Côte d'Ivoire / NTLC

Date : 2026-08-19
Statut : `P1_INVENTORIED / DEEP_PILOT_ALREADY_EXISTS / LIVE_SOURCE_DELTA_DETECTED / HASH_PENDING`

- Ticker : `NTLC`
- Dossier Drive canonique : `1LMpOZwGEtDm0cn8TcEPUJbodOPMU3exU`
- Dossiers directs live : **28**, continus de `1998` à `2025`
- Snapshot avant recheck : **81 PDF**
- Recheck live strict parent-scoped : **85 PDF**
- Delta live : **+4**
- SOURCE global : **V22 = 3 137 PDF**
- Checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v22_20260819.md`

## Preuve de cardinal live

Le corpus a été recompté sur deux sous-périmètres disjoints des mêmes dossiers enfants pour rendre le cardinal indépendant de la troncature d'affichage du connecteur :

- années `1998–2011` : **33 PDF** ;
- années `2012–2025` : **52 PDF** ;
- total live : **85 PDF**.

Le périmètre SOURCE est défini par les parent IDs Drive réels, jamais par une recherche ticker seule.

## Particularités SOURCE

- historique long avec nombreuses collisions historiques potentielles ;
- familles modernes : T1/S1/T3, états financiers et CAC ;
- 2024 contient notamment `2024_Etats_Financiers_NTLC.pdf` et `2024_Etats_Financiers_NTLC_rev.pdf` : les deux objets physiques sont conservés et la relation ne sera qualifiée qu'après preuve binaire/sémantique ;
- 2023 contient deux fichiers d'états financiers ;
- 2025 contient T1/S1/T3 dans le corpus live ;
- aucun suffixe `_2`, `_3`, `_4` ou `_rev` n'est traité comme preuve de doublon ou de version.

## P1-R

NTLC a déjà servi de deep pilot industrie : stocks, ventes, matières, EBE, dividendes, document annuel original vs révision DocuSign, distinction tableau/narratif et faits corporate/audit. Cette analyse n'est pas refaite de zéro ; seules les vérifications transversales nécessaires à la complétude P1 sont ajoutées.

## Passe suivante exacte

1. matérialiser les **85/85 PDF** de la whitelist live parent-scoped V22 ;
2. valider tailles et signatures `%PDF-` ;
3. calculer SHA-256 sur 100 % ;
4. identifier les groupes exacts sans supprimer aucun objet ;
5. revoir seulement les familles sémantiques justifiées lorsque les SHA diffèrent ;
6. créer `inventory/hashes/NTLC.csv` avec sérialisation LF ;
7. calculer le Git blob local et vérifier le blob GitHub post-commit ;
8. finaliser NTLC, manifeste, doublons, `SUIVI.md` et `TODO.md`.

## Restant transversal

`SHA256 = IN_PROGRESS` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = LIVE_RECHECK_COMPLETE_FOR_CURRENT_SCOPE`.
