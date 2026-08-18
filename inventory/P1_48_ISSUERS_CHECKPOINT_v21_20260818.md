# P1 — CHECKPOINT V21 — 48 ISSUERS — 2026-08-18

## Objet

Versionner le delta SOURCE détecté lors de la revérification live de `ETIT` avant tout calcul SHA-256 sur ce corpus.

## Baseline précédente

- checkpoint précédent : `inventory/P1_48_ISSUERS_CHECKPOINT_v20_20260818.md` ;
- total SOURCE V20 : **3 114 PDF** ;
- ETIT snapshot manifeste V20 : **81 PDF**.

## Revérification live ETIT

- émetteur : Ecobank Transnational Incorporated / `ETIT` ;
- dossier Drive canonique : `183KoqvNUQNaj6kdfw80PkkIGupbvuSia` ;
- dossiers enfants live observés : **23**, continus de `2003` à `2025` ;
- recheck strict : `mimeType = application/pdf` borné aux parent IDs réels ;
- le résultat global atteint le plafond de 100 du connecteur ; le cardinal a donc été recompté par deux sous-périmètres disjoints ;
- `2003–2014` : **51 PDF** ;
- `2015–2025` : **49 PDF** ;
- PDF live ETIT : **100** ;
- delta net : **+19** par rapport au snapshot 81.

Le corpus contient des noms génériques ou identifiant d'autres entités du groupe, par exemple `ra_-_ecobank_tg_-_excercice_2010.pdf`, ce qui confirme que le recheck doit être parent-scoped et non fondé sur le ticker seul. Aucun document n'est exclu sur la seule base de son nom.

## Nouveau total SOURCE

`3 114 + 19 = 3 133 PDF`

Le dénominateur canonique devient donc **V21 = 3 133 PDF** avant tout SHA ETIT.

## Règles de preuve

- le snapshot antérieur n'est pas traité comme vérité live ;
- aucun document n'est exclu à cause de son nom ;
- les suffixes `_2` à `_7` ne déterminent aucune relation sans preuve binaire/sémantique ;
- `EXACT_DUPLICATE` exige un SHA-256 identique ;
- `SUPERSEDES` exige une preuve explicite ;
- SOURCE physique reste immuable.

## Suite immédiate

1. matérialiser les **100/100** PDF ETIT live ;
2. valider signatures PDF et tailles ;
3. calculer SHA-256 exhaustif ;
4. produire `inventory/hashes/ETIT.csv` ;
5. qualifier les collisions exactes et les relations de version prouvables ;
6. revalider le registre GitHub après commit ;
7. mettre à jour ETIT, manifeste, doublons, `SUIVI.md` et `TODO.md`.

## Point de reprise

`SOURCE_VERSION=V21 | LIVE_TOTAL=3133 | ETIT_SNAPSHOT=81 | ETIT_LIVE=100 | ETIT_DELTA=+19 | ETIT_HASH=PENDING`
