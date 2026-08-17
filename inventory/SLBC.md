# P1 SOURCE — SOLIBRA / SLBC

Date de vérification initiale : 2026-08-09  
Dernière revérification live : 2026-08-17

Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / HASH_PENDING`

- Ticker : `SLBC`
- Dossier Drive : `1U41GdtRNU8QYqHYI8WdLJlwv1vFaukVy`
- Dossiers directs : **28 = 1998–2025**
- snapshot précédent : **65 PDF**
- live strict parent-scoped : **70 PDF**
- delta : **+5 PDF**
- total SOURCE global V17 : **3 075 PDF**
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v17_20260817.md`

Le delta V17 est enregistré avant tout SHA SLBC.

## Particularités SOURCE

- historique long avec rapports annuels, états financiers et publications périodiques ;
- nombreuses variantes historiques suffixées `_2`, `_3`, `_4`, `_5` ;
- publications CAC et assemblées générales présentes dans les années récentes ;
- un erratum d'avis de convocation AGO est présent dans 2025 et reste dans SOURCE ;
- aucune variante n'est supprimée ou fusionnée sur la seule base de son nom.

## Règles de preuve

- un suffixe n'implique ni doublon ni ordre de version ;
- `EXACT_DUPLICATE` exige un SHA-256 identique ;
- `VERSION_OF` et `SUPERSEDES` restent distincts ;
- les objets non strictement financiers restent conservés s'ils sont physiquement présents dans le périmètre SOURCE ;
- aucune source physique n'est supprimée lors de la réconciliation.

## P1 restant immédiat

1. matérialiser **70/70** PDF live ;
2. valider signatures et tailles ;
3. calculer SHA-256 exhaustif ;
4. produire `inventory/hashes/SLBC.csv` ;
5. identifier collisions exactes et relations de version prouvables ;
6. revalider le registre GitHub bit-for-bit ;
7. fermer SLBC seulement après ces contrôles.

## Point de reprise

`SLBC_SNAPSHOT=65 | SLBC_LIVE=70 | DELTA=+5 | GLOBAL_SOURCE=3075 | HASH=PENDING`
