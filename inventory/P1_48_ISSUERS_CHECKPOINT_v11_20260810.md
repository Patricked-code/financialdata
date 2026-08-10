# P1 — Checkpoint V11 — 48 émetteurs

Date : 2026-08-10
Statut : `INVENTORY_COMPLETE_48_OF_48_LIVE_REFRESH`

## État live

- Émetteurs : **48 / 48**
- Total PDF live : **3 041**
- Snapshot précédent V10 : **3 031 PDF**
- Delta V11 : **+10 PDF**
- Émetteur responsable du delta : **ECOC**, passé de **32 à 42 PDF** après revérification stricte par dossiers parents + MIME.

## ECOC — bornage live

Dossier émetteur : `1L41JW3u29dJu1VSI6XRFeR-97ycVO50x`.
Dossiers directs : 9 (`2017` à `2025`).
Répartition PDF live : 2017=1 ; 2018=6 ; 2019=4 ; 2020=5 ; 2021=6 ; 2022=5 ; 2023=6 ; 2024=6 ; 2025=3.

Particularités de version visibles au niveau SOURCE :
- 2023 : `2023_Rapport_T1_ECOC.pdf` + `2023_Rapport_T1_ECOC_rev.pdf` ;
- 2024 : `2024_Rapport_T3_ECOC.pdf` + `2024_Rapport_T3_ECOC_rev.pdf` ;
- 2024 : `2024_Rapport_Annuel_ECOC.pdf` + `2024_Rapport_Annuel_ECOC_rev.pdf` ;
- 2018 et 2021 : deux états financiers physiques (`plain` + `_2`) à qualifier.

## Méthode de fraîcheur

Le comptage live est réalisé sans filtre de nom de fichier. Seuls les PDF dont le parent appartient à l'arborescence documentaire de l'émetteur sont comptés. Les snapshots antérieurs restent conservés dans Git ; aucun total SOURCE n'est réécrit silencieusement.

## Prochaine passe

- qualifier par contenu les variantes ECOC explicites ;
- conserver séparément chaque objet SOURCE ;
- calcul SHA-256 quand le runtime binaire local sera de nouveau exécutable ;
- poursuivre en parallèle les revérifications live des autres corpus non hashés.
