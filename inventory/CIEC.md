# P1 SOURCE — CIE / CIEC

Date de vérification initiale : 2026-08-09  
Dernière revérification live : 2026-08-17

Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / HASH_PENDING / DEEP_PILOT_ALREADY_EXISTS`

- Émetteur : CIE
- Ticker : `CIEC`
- Dossier Drive : `1y6IMougiA8lTlwDmGYcjIa_PeT4Nzgz3`
- Dossiers directs : **29** = `1998–2025 + divers`
- snapshot précédent : **61 PDF**
- live strict parent-scoped : **62 PDF**
- delta : **+1 PDF**
- nouveau total SOURCE global : **3 070 PDF**
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v16_20260817.md`

Le delta V16 est enregistré avant tout SHA CIEC.

## Particularités SOURCE

- historique long avec rapports annuels, états financiers, T1/S1/T3 et CAC ;
- présence de `2017_Etats_Financiers_CIEC.pdf` et `2017_Etats_Financiers_CIEC_rev.pdf` ;
- attestations et rapports CAC ;
- `divers` fait partie du périmètre ;
- suffixes/collisions à réconcilier par octets, SHA et contenu, jamais par nom seul.

## P1-R

CIEC est déjà un `DEEP_PILOT` conceptuel : scopes CIE propre vs Secteur/Autorité concédante, valeurs monétaires/physiques, STOCK/FLOW, individuel/consolidé et concession. Ne pas refaire cette analyse de zéro ; la passe SHA doit préserver ces dimensions pour le futur manifeste RAW.

## Règles de preuve

- `_2`, `_3`, `_rev` ≠ doublon automatique ;
- `EXACT_DUPLICATE` exige SHA identique ;
- `VERSION_OF` et `SUPERSEDES` restent distincts ;
- même année ≠ même période, scope ou type documentaire ;
- aucune source physique n'est supprimée lors de la réconciliation.

## P1 restant immédiat

1. matérialiser **62/62** PDF live ;
2. valider tailles/signatures ;
3. calculer SHA-256 exhaustif ;
4. produire `inventory/hashes/CIEC.csv` ;
5. identifier collisions exactes ;
6. comparer en profondeur les variantes 2017 plain / `_rev` ;
7. revalider le registre GitHub bit-for-bit ;
8. fermer CIEC seulement après ces contrôles.

## Point de reprise

`CIEC_SNAPSHOT=61 | CIEC_LIVE=62 | DELTA=+1 | GLOBAL_SOURCE=3070 | HASH=PENDING`
