# P1 SOURCE — checkpoint live V6

Date : 2026-08-09
Statut : `INVENTORY_COMPLETE_48_OF_48 / LIVE_REFRESH`

## Total live

- sociétés : **48 / 48** ;
- total PDF live : **2 999** ;
- index machine-lisible : `inventory/p1_issuer_manifest.csv`.

## Historique des snapshots conservés

- initial : **2 950 PDF** ;
- V2 après CBIBF : **2 957 PDF** ;
- V3 après ORAC : **2 964 PDF** ;
- V4 après SICC : **2 981 PDF** ;
- V5 après MVSC : **2 996 PDF** ;
- V6 après UNLC : **2 999 PDF**.

## Delta V5 → V6

UNLC est passé de **20 à 23 PDF**, soit **+3**. Le contrôle a été effectué sans filtre de nom, uniquement sur ses 9 dossiers parents et le MIME `application/pdf`.

Les snapshots antérieurs restent conservés dans l'historique Git/GitHub. P1 considère le corpus SOURCE comme évolutif jusqu'à la réconciliation de fraîcheur finale.

## Suites transversales

Les 2 999 fichiers physiques ne sont pas encore tous hashés/classifiés/résolus en période/version. P1 reste `IN_PROGRESS`.
