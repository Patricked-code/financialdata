# P1 SOURCE — checkpoint live V4

Date : 2026-08-09
Statut : `INVENTORY_COMPLETE_48_OF_48 / LIVE_REFRESH`

## Total live

- sociétés : **48 / 48** ;
- total PDF live : **2 981** ;
- index machine-lisible : `inventory/p1_issuer_manifest.csv`.

## Historique des snapshots conservés

- snapshot initial : **2 950 PDF** ;
- V2 après delta CBIBF : **2 957 PDF** ;
- V3 après delta ORAC : **2 964 PDF** ;
- V4 après delta SICC : **2 981 PDF**.

## Delta V3 → V4

SICC est passé de **19 à 36 PDF**, soit **+17**. Le contrôle a été effectué sans filtre de nom, uniquement sur ses 25 dossiers annuels parents et le MIME `application/pdf`.

Aucun snapshot antérieur n'est supprimé ou réécrit : Git/GitHub conserve l'historique de la croissance du corpus SOURCE.

## Suites transversales

Le total physique n'implique pas que les 2 981 documents soient déjà :

- hashés ;
- classifiés par contenu ;
- résolus sur leur période économique ;
- reliés à leurs doublons/versions ;
- intégrés dans le manifeste document-level consolidé.

Ces passes restent actives sous P1.
