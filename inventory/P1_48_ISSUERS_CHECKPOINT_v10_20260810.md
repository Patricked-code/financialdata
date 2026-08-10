# P1 — Checkpoint V10 — 48 émetteurs

Date : 2026-08-10
Statut : `INVENTORY_COMPLETE_48_OF_48_LIVE_REFRESH`

## État live

- Émetteurs : **48 / 48**
- Total PDF live : **3 031**
- Snapshot précédent V9 : **3 028 PDF**
- Delta V10 : **+3 PDF**
- Émetteur responsable du delta : **NSBC**, passé de **38 à 41 PDF** après revérification stricte par dossiers parents + MIME.

## Méthode de fraîcheur

Le comptage live est réalisé sans filtre de nom de fichier. Pour chaque émetteur, seuls les PDF dont le parent appartient à l'arborescence documentaire de l'émetteur sont comptés. Les snapshots antérieurs restent conservés dans Git ; aucun total SOURCE n'est réécrit silencieusement.

## Prochaine passe

- terminer `NSBC` : matérialisation 41/41, taille Drive ↔ taille locale, SHA-256 41/41, détection de doublons exacts et candidats de version ;
- poursuivre ensuite les autres corpus non hashés avec revérification live préalable.
