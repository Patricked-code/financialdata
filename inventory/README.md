# P1 — Inventaire documentaire

Ce dossier contient l'inventaire documentaire vérifié du corpus source.

## Statut général

`P1_DOCUMENT_INVENTORY = IN_PROGRESS`

L'inventaire est construit depuis l'arborescence réelle Google Drive, pas depuis les seuls noms de fichiers ni depuis le script historique de téléchargement.

## Règle d'inventaire

Pour chaque émetteur :

1. inventorier le dossier société ;
2. inventorier tous les sous-dossiers directs (`année`, `divers`, autre) ;
3. inventorier tous les fichiers contenus dans ces sous-dossiers ;
4. conserver au minimum `drive_file_id`, nom, parent, dossier de classement, type MIME, taille et dates lorsque disponibles ;
5. calculer/collecter les hash dans une sous-étape dédiée ;
6. détecter les candidats doublons/révisions sans les fusionner ;
7. ne pas assimiler automatiquement l'année de classement à la période économique ;
8. marquer les dossiers vides ;
9. marquer les noms non standardisés ;
10. documenter toute anomalie.

## Statuts

- `NOT_STARTED`
- `FOLDER_INVENTORIED`
- `FILE_INVENTORIED`
- `HASH_PENDING`
- `HASH_VERIFIED`
- `DUPLICATE_REVIEW_PENDING`
- `COMPLETE_P1`

## Fichiers

- `P1_ROOT_MANIFEST.md` : état de la racine `Rapport V2` et source de collecte.
- un fichier par émetteur : couverture dossiers/fichiers et anomalies.

## Important

P1 ne constitue pas l'extraction des données financières. Il prépare la couche SOURCE et la provenance nécessaires avant l'extraction RAW.
