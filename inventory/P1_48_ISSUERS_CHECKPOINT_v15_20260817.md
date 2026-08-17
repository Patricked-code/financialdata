# P1 SOURCE — checkpoint inventaire live V15

Date : 2026-08-17
Dépôt canonique : `Patricked-code/financialdata`
Branche autorisée : `main` uniquement.

## État

- sociétés : **48 / 48** ;
- total live précédent V14 : **3 060 PDF** ;
- BICC snapshot précédent : **61 PDF** ;
- arborescence BICC revérifiée : **28 dossiers directs `1998–2025`**, sans dossier `divers` observé ;
- revérification BICC strictement par les 28 IDs réels de dossiers parents avec `mimeType = application/pdf` : **70 PDF** ;
- delta BICC : **+9 PDF** ;
- nouveau total live V15 : **3 069 PDF**.

## Preuve de comptage

Le résultat consolidé du connecteur Drive contient **70 objets PDF** appartenant exclusivement aux 28 dossiers annuels BICC `1998–2025`. Le dernier objet retourné appartient au dossier `2025`; aucun dossier hors de l'arborescence BICC n'est inclus dans la requête parent-scoped.

Le snapshot de référence inscrit dans `inventory/BICC.md` était de **61 PDF**. Le présent checkpoint enregistre uniquement le delta physique constaté sur Drive ; il n'infère ni doublon, ni version, ni suppression logique.

## Règle de preuve

Le delta est persisté **avant tout calcul SHA BICC**.

Aucun fichier n'est :

- fusionné ;
- supprimé ;
- ignoré parce que son nom ressemble à une autre source ;
- considéré comme doublon depuis un suffixe `_2`, `_3`, etc. ;
- considéré comme version finale depuis un suffixe `_rev` sans revue du contenu.

Seuls les octets matérialisés et leur SHA-256 pourront établir `EXACT_DUPLICATE`. Les relations de version (`VERSION_OF`, `REVISION`, `SUPERSEDES`) restent séparées du verdict binaire.

## Particularités BICC à contrôler au hash / contenu

- nombreuses variantes historiques, notamment 2003–2014 ;
- `2019_Etats_Financiers_BICC.pdf` et `2019_Etats_Financiers_BICC_rev.pdf` : relation de révision à vérifier depuis le contenu ;
- T2 2022 est une période explicitement présente et doit rester distincte de S1 2022 ;
- `2022_Rapport_T3_BICC.pdf` et `_2` : candidats à comparer, sans inférence préalable ;
- `bilan_et_compte_de_resultat_bicici_31_12_2022_.pdf` reste un profil P1-R utile pour la reconnaissance des états financiers.

## Impact transverse immédiat

- SOURCE live : **3 069 PDF** ;
- SHA déjà validés avant BICC : **995** ;
- couverture temporaire avant hash BICC : **995 / 3 069 = 32,42 %** ;
- restant non hashé avant hash BICC : **2 074 PDF**.

Statut : `INVENTORY_COMPLETE_48_OF_48_LIVE_REFRESH_V15 / BICC_LIVE_SOURCE_DELTA_DETECTED / BICC_HASH_PENDING`.
