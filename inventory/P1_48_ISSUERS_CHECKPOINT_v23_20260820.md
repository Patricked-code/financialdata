# P1 — CHECKPOINT V23 — 48 ISSUERS — 2026-08-20

## Objet

Versionner le delta SOURCE détecté lors de la revérification live de `CFAC` avant tout calcul SHA-256 sur ce corpus.

## Baseline précédente

- checkpoint précédent : `inventory/P1_48_ISSUERS_CHECKPOINT_v22_20260819.md` ;
- total SOURCE V22 : **3 137 PDF** ;
- CFAC snapshot manifeste V22 : **94 PDF**.

## Revérification live CFAC

- émetteur : CFAO Motors Côte d'Ivoire / `CFAC` ;
- dossier Drive canonique : `1y_h696cNzQjE9QnGaR8913zVMd9IkA7y` ;
- dossiers enfants live observés : **26** : `1999–2004` et `2006–2025` ;
- dossiers `1998` et `2005` non observés dans le root courant ; aucune absence métier n'est inférée sans preuve SOURCE ;
- recheck strict : `mimeType = application/pdf` borné aux parent IDs réels ;
- le cardinal est recompté par deux sous-périmètres disjoints ;
- `1999–2012` : **58 PDF** ;
- `2013–2025` : **56 PDF** ;
- PDF live CFAC : **114** ;
- delta net : **+20** par rapport au snapshot 94.

Le périmètre est défini par les dossiers SOURCE réels et non par une recherche ticker seule. Les nombreuses variantes historiques (`_2`…`_11`) et les rôles modernes (T1/S1/T3, états financiers, CAC, communications) sont tous conservés comme objets physiques jusqu'à preuve binaire/sémantique.

## Nouveau total SOURCE

`3 137 + 20 = 3 157 PDF`

Le dénominateur canonique devient donc **V23 = 3 157 PDF** avant tout SHA CFAC.

## Règles de preuve

- le snapshot antérieur n'est pas traité comme vérité live ;
- aucun document n'est exclu à cause de son nom ;
- les suffixes `_2` à `_11`, `_rev` ou autres ne déterminent aucune relation sans preuve binaire/sémantique ;
- `EXACT_DUPLICATE` exige un SHA-256 identique ;
- `SUPERSEDES` exige une preuve explicite ;
- SOURCE physique reste immuable.

## Suite immédiate

1. matérialiser les **114/114** PDF CFAC live ;
2. valider signatures PDF et tailles ;
3. calculer SHA-256 exhaustif ;
4. produire `inventory/hashes/CFAC.csv` en LF ;
5. qualifier les collisions exactes et seulement les relations de version prouvables ;
6. revalider le Git blob du registre après commit ;
7. mettre à jour CFAC, manifeste, doublons, `SUIVI.md` et `TODO.md`.

## Point de reprise

`SOURCE_VERSION=V23 | LIVE_TOTAL=3157 | CFAC_SNAPSHOT=94 | CFAC_LIVE=114 | CFAC_DELTA=+20 | CFAC_HASH=PENDING`
