# P1 SOURCE — checkpoint live V8

Date : 2026-08-09
Statut : `INVENTORY_COMPLETE_48_OF_48 / LIVE_REFRESH`

## Total live

- sociétés : **48 / 48** ;
- total PDF live : **3 013** ;
- index machine-lisible : `inventory/p1_issuer_manifest.csv`.

## Historique des snapshots conservés

- initial : **2 950 PDF** ;
- V2 après CBIBF : **2 957 PDF** ;
- V3 après ORAC : **2 964 PDF** ;
- V4 après SICC : **2 981 PDF** ;
- V5 après MVSC : **2 996 PDF** ;
- V6 après UNLC : **2 999 PDF** ;
- V7 après ORGT : **3 011 PDF** ;
- V8 après SHEC : **3 013 PDF**.

## Delta V7 → V8

SHEC est passé de **37 à 39 PDF**, soit **+2**. Le contrôle a été effectué sans filtre de nom, uniquement sur les 10 dossiers parents 2016–2025 et le MIME `application/pdf`.

Les snapshots antérieurs restent conservés dans l'historique Git/GitHub. P1-FRESH continue donc à traiter le corpus SOURCE comme évolutif.

## Suites transversales

Les 3 013 fichiers physiques ne sont pas encore tous hashés/classifiés/résolus en période/version. P1 reste `IN_PROGRESS`.
