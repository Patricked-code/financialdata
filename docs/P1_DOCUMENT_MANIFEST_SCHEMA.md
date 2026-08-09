# P1 DOCUMENT MANIFEST SCHEMA

Date : 2026-08-09
Statut : `ACTIVE / MACHINE_READABLE_MANIFEST_START`

## Finalité

Définir la ligne canonique du manifeste SOURCE document par document pour les **2 950 PDF** recensés dans `inventory/P1_48_ISSUERS_CHECKPOINT.md`.

Une ligne du manifeste représente **un fichier SOURCE physique**, pas un document économique dédupliqué.

## Champs obligatoires du manifeste

```text
source_file_id
issuer_folder_ticker
issuer_expected_name
issuer_assignment_status
issuer_assignment_evidence
source_drive_file_id
source_drive_parent_id
source_path_raw
source_folder_year_raw
source_filename_raw
mime_type
file_size_bytes
created_time_raw
modified_time_raw
source_url
sha256
hash_status
binary_duplicate_group_id
version_relation_status
version_of_source_file_id
supersedes_source_file_id
period_label_filename_raw
economic_period_status
period_start
period_end
period_type_raw
document_type_status
document_type_raw
pdf_text_layer_status
page_count
metadata_title_raw
metadata_author_raw
metadata_mismatch_status
first_seen_at
last_seen_at
source_status
notes
```

## Valeurs de statut minimales

### issuer_assignment_status

- `VALIDATED`
- `REVIEW_REQUIRED`
- `OUT_OF_SCOPE_CONFIRMED`
- `NOT_REVIEWED`

### hash_status

- `NOT_COMPUTED`
- `COMPUTED`
- `ERROR`

### version_relation_status

- `NOT_REVIEWED`
- `UNIQUE_CONFIRMED`
- `EXACT_DUPLICATE`
- `POSSIBLE_DUPLICATE`
- `REVISION_CANDIDATE`
- `VERSION_LINKED`

### economic_period_status

- `NOT_RESOLVED`
- `FILENAME_ONLY`
- `CONTENT_RESOLVED`
- `AMBIGUOUS`
- `REVIEW_REQUIRED`

### source_status

- `ACTIVE_SOURCE`
- `SUPERSEDED_SOURCE`
- `DUPLICATE_SOURCE`
- `OUT_OF_SCOPE`
- `REVIEW_REQUIRED`

## Règles

1. `source_drive_file_id` est l'identifiant stable primaire de la source Drive ; le nom de fichier n'est jamais une clé.
2. `source_filename_raw` et `source_path_raw` ne sont jamais réécrits silencieusement.
3. `sha256` est nul tant qu'il n'a pas été réellement calculé ; jamais inventé.
4. `_2/_3/...` n'établit aucune relation de doublon.
5. `_rev` signale seulement une révision candidate jusqu'à preuve documentaire/hash/contenu.
6. `source_folder_year_raw` n'est pas la période économique ; la période économique est résolue depuis le contenu.
7. l'attribution émetteur reste indépendante du dossier physique ; le cas ONATEL rangé sous SNTS doit devenir `REVIEW_REQUIRED`.
8. une source supersédée ou dupliquée n'est pas supprimée du manifeste.
9. le manifeste SOURCE doit permettre de remonter sans ambiguïté de chaque future observation RAW au fichier original.

## Fichiers machine-lisibles cibles

- `inventory/p1_issuer_manifest.csv` : index 48 émetteurs, déjà créé ;
- `inventory/p1_document_manifest.csv` : **2 950 lignes attendues**, à construire depuis Drive ;
- `inventory/p1_duplicate_groups.csv` : groupes de hash identiques ;
- `inventory/p1_version_relations.csv` : relations documentaires/version ;
- `inventory/p1_period_resolution.csv` : périodes résolues depuis contenu lorsque nécessaire.

## Contrôle de complétude

Le manifeste document-level ne pourra être marqué `COMPLETE` que si :

```text
COUNT(rows) = 2950
COUNT(distinct source_drive_file_id) = 2950
missing source_drive_file_id = 0
missing issuer_folder_ticker = 0
```

Les champs hash/période peuvent rester temporairement `NOT_COMPUTED` / `NOT_RESOLVED` pendant leur passe dédiée, mais aucune ligne SOURCE ne doit disparaître.
