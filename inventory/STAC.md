# P1 SOURCE — SETAO / STAC

Date : 2026-08-09
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED`

- Ticker : `STAC`
- Dossier Drive : `143H1ht6fKOIMzcjDqoQAFQ7XfsqRxZwH`
- Dossiers directs : **26** = 25 années + `divers`
- Années observées : 1998–2003, 2005–2006, 2008, 2010–2025
- Années absentes : **2004, 2007, 2009**
- Premier inventaire de session : **38 PDF**
- État Drive live revérifié par parents + MIME : **53 PDF**
- Delta live : **+15 PDF**

## Particularités SOURCE

- `divers_Etats_Financiers_STAC.pdf` : période économique à résoudre depuis le contenu ;
- 2010 : rapport annuel plain + `_2` ;
- 2012 : quatre rapports annuels physiques (`plain`, `_2`, `_3`, `_4`) ;
- 2013 : trois rapports annuels physiques (`plain`, `_2`, `_3`) ;
- 2014 : trois rapports annuels physiques (`plain`, `_2`, `_3`) ;
- 2015 : deux rapports annuels physiques ;
- 2019 : états financiers plain + `_rev` ;
- états financiers, S1/T3 et CAC/attestations modernes ;
- 2024 : S1, T3, CAC S1, états financiers ;
- 2025 : S1 + T3 observés.

## Règle

Le total live est obtenu sans filtre de nom, uniquement par les 26 dossiers parents et `mimeType = application/pdf`. Les collisions `_2/_3/_4` et `_rev` restent des sources physiques distinctes jusqu'au verdict SHA-256 ; aucun ordre de version n'est déduit du nom.

## Restant transversal

`DOCUMENT_MANIFEST_STAC = IN_PROGRESS` ; `SHA256_STAC = NOT_COMPLETE` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
