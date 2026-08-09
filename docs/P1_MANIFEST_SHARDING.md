# P1 — DOCUMENT MANIFEST SHARDING

Date : 2026-08-09
Statut : `ACTIVE_IMPLEMENTATION_STRATEGY`

## Pourquoi

Le manifeste SOURCE final doit contenir une ligne par fichier physique et atteindra désormais **2 957 lignes live**. Réécrire intégralement `inventory/p1_document_manifest.csv` à chaque petit lot augmente inutilement le risque de conflit Git ou de régression.

Cette stratégie ne change **aucun champ** du schéma défini dans `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md`.

## Méthode

Chaque émetteur peut être construit et vérifié dans :

`inventory/manifests/<TICKER>.csv`

Chaque shard utilise exactement le même en-tête et la même sémantique que le manifeste global.

Le fichier global :

`inventory/p1_document_manifest.csv`

reste la **cible canonique consolidée**.

## Règles de consolidation

1. concaténer les shards par `source_drive_file_id` ;
2. refuser tout `source_drive_file_id` dupliqué entre shards ;
3. préserver toutes les sources physiques, y compris les doublons binaires ;
4. ne jamais dédupliquer des lignes sur le seul nom de fichier ;
5. contrôler : `COUNT(distinct source_drive_file_id) = COUNT(rows)` ;
6. le dénominateur live est celui du dernier checkpoint SOURCE, actuellement **2 957** ;
7. tout delta Drive ultérieur crée un nouveau snapshot/version de référence au lieu d'effacer l'historique.

## Statuts de progression

Deux compteurs sont suivis séparément :

- `CAPTURED_DOCUMENT_RECORDS` : lignes déjà capturées soit dans le maître, soit dans un shard complet ;
- `MASTER_CONSOLIDATED_ROWS` : lignes déjà intégrées dans `p1_document_manifest.csv`.

Cette distinction empêche de présenter une ligne capturée en shard comme déjà consolidée dans le maître.

## Contrôle avant P2/P3

Avant clôture P1 :

- tous les shards doivent être consolidés ;
- le maître doit contenir exactement le nombre live de sources ;
- aucun identifiant Drive ne doit manquer ni apparaître deux fois ;
- les hashes/périodes/versions peuvent porter leurs statuts intermédiaires explicites, mais aucune source ne doit disparaître.
