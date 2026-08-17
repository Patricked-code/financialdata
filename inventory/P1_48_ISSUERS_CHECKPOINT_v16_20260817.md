# P1 SOURCE — checkpoint inventaire live V16

Date : 2026-08-17
Dépôt canonique : `Patricked-code/financialdata`
Branche autorisée : `main` uniquement.

## État

- sociétés : **48 / 48** ;
- total live précédent V15 : **3 069 PDF** ;
- CIEC snapshot précédent : **61 PDF** ;
- arborescence CIEC revérifiée : **29 dossiers directs `1998–2025 + divers`** ;
- revérification CIEC strictement par les 29 IDs réels de dossiers parents avec `mimeType = application/pdf` : **62 PDF** ;
- delta CIEC : **+1 PDF** ;
- nouveau total live V16 : **3 070 PDF**.

## Preuve de comptage

Le résultat consolidé du connecteur Drive contient **62 objets PDF** appartenant exclusivement aux 29 dossiers CIEC ciblés. Le comptage est effectué sur les entrées physiques du résultat parent-scoped, et non sur une recherche textuelle de ticker.

Le snapshot de référence inscrit dans `inventory/CIEC.md` était de **61 PDF**. Le présent checkpoint enregistre uniquement le delta physique observé. Il n'infère ni doublon ni relation de version.

## Règle de preuve

Le delta est persisté **avant tout calcul SHA CIEC**.

- aucune suppression ou fusion SOURCE ;
- suffixe `_2`, `_3`, `_rev` ≠ verdict ;
- même taille ≠ doublon sans SHA identique ;
- `EXACT_DUPLICATE`, `VERSION_OF` et `SUPERSEDES` restent des relations distinctes ;
- tout lien de supersession exige une preuve explicite supplémentaire.

## Particularités CIEC à contrôler

- `2017_Etats_Financiers_CIEC.pdf` / `_rev.pdf` : revue de version par contenu ;
- plusieurs paires/triples historiques d'états financiers et rapports annuels ;
- CIEC est déjà un deep pilot P1-R : préserver les scopes CIE propre vs secteur/autorité concédante, individuel/consolidé, concession, STOCK/FLOW et valeurs physiques/monétaires ;
- `divers` reste une partie du périmètre SOURCE.

## Impact transverse avant hash CIEC

- SOURCE live : **3 070 PDF** ;
- SHA déjà validés avant CIEC : **1 065** ;
- couverture temporaire : **1 065 / 3 070 = 34,69 %** ;
- restant non hashé avant CIEC : **2 005 PDF** ;
- groupes exacts globaux avant CIEC : **12**.

Statut : `INVENTORY_COMPLETE_48_OF_48_LIVE_REFRESH_V16 / CIEC_LIVE_SOURCE_DELTA_DETECTED / CIEC_HASH_PENDING`.
