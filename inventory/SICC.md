# P1 SOURCE — SICOR / SICC

Date : 2026-08-09
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED`

- Ticker : `SICC`
- Dossier Drive : `1VK17v9GP-lKlC3HFOAbZ9zBS1Jd54iyc`
- Dossiers directs : **25**
- Couverture : `1998–2013`, puis `2015–2023`; **2014 absent**, aucun dossier 2024/2025 observé
- Premier inventaire de session : **19 PDF**
- État Drive live revérifié : **36 PDF**
- Delta live : **+17 PDF**

## Contrôle live

Le décompte définitif a été refait sans filtre de nom, uniquement sur les 25 dossiers parents SICC avec `mimeType = application/pdf`.

Le corpus live contient notamment plusieurs variantes historiques à préserver séparément tant que leur relation binaire/sémantique n'est pas prouvée :

- 2007 : annuel + annuel `_2` ;
- 2008 : annuel + annuel `_2` ;
- 2009 : annuel + annuel `_2` ;
- 2010 : annuel + `_2` + `_3` ;
- 2011 : annuel + `_2` ;
- 2012 : annuel + `_2` ;
- 2015 : états financiers + `_2` ;
- 2016 : états financiers + `_2` ;
- 2018 : états financiers + rapport annuel ;
- 2019 : états financiers + S1.

## Règle

Aucun suffixe `_2`, `_3` ni proximité de nom ne vaut verdict de doublon. Les relations exactes seront établies uniquement après matérialisation et SHA-256. Les 36 sources physiques sont conservées dans SOURCE.

## Restant transversal SICC

`DOCUMENT_MANIFEST_SICC = IN_PROGRESS` ; `SHA256_SICC = NOT_COMPLETE` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
