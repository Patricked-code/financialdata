# P1 SOURCE — SETAO / STAC

Date : 2026-08-09
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / SHA_COMPLETE`

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

## SHA-256

Les **53 PDF** ont été matérialisés depuis Drive et hashés avec contrôle des tailles.

- `SHA256_STAC = COMPLETE_53_53` ;
- contenus binaires uniques : **53 / 53** ;
- doublons binaires exacts trouvés : **0** ;
- registre : `inventory/hashes/STAC.csv`.

Les séries de variantes 2010, 2012, 2013, 2014 et 2015 ont toutes des SHA distincts. Le couple `2019_Etats_Financiers_STAC.pdf` / `2019_Etats_Financiers_STAC_rev.pdf` a également deux SHA distincts. Aucun ordre de version ou de supersession n'est donc déduit du seul nom.

## Règle

Le total live est obtenu sans filtre de nom, uniquement par les 26 dossiers parents et `mimeType = application/pdf`. Les **53 sources physiques** restent distinctes dans SOURCE. Les relations sémantiques/version éventuelles seront établies ultérieurement par inspection du contenu et non par suffixe de fichier.

## Restant transversal

`DOCUMENT_MANIFEST_STAC = ROW_COVERAGE_53_53 / SHARD_BACKFILL_PENDING` ; `SHA256_STAC = COMPLETE_53_53` ; `BINARY_DUPLICATES = NONE_FOUND` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
