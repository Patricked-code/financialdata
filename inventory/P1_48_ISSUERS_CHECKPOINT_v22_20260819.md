# P1 — CHECKPOINT V22 — 48 ISSUERS — 2026-08-19

## Objet

Versionner le delta SOURCE détecté lors de la revérification live de `NTLC` avant tout calcul SHA-256 sur ce corpus.

## Baseline précédente

- checkpoint précédent : `inventory/P1_48_ISSUERS_CHECKPOINT_v21_20260818.md` ;
- total SOURCE V21 : **3 133 PDF** ;
- NTLC snapshot manifeste V21 : **81 PDF**.

## Revérification live NTLC

- émetteur : Nestlé Côte d'Ivoire / `NTLC` ;
- dossier Drive canonique : `1LMpOZwGEtDm0cn8TcEPUJbodOPMU3exU` ;
- dossiers enfants live observés : **28**, continus de `1998` à `2025` ;
- recheck strict : `mimeType = application/pdf` borné aux parent IDs réels ;
- pour rendre le cardinal indépendant de la troncature d'affichage du connecteur, le corpus a été recompté par deux sous-périmètres disjoints ;
- `1998–2011` : **33 PDF** ;
- `2012–2025` : **52 PDF** ;
- PDF live NTLC : **85** ;
- delta net : **+4** par rapport au snapshot 81.

Le périmètre est défini par les dossiers SOURCE réels et non par une recherche ticker seule. Les noms historiques, suffixes et variantes physiques sont conservés tels quels.

## Nouveau total SOURCE

`3 133 + 4 = 3 137 PDF`

Le dénominateur canonique devient donc **V22 = 3 137 PDF** avant tout SHA NTLC.

## Règles de preuve

- le snapshot antérieur n'est pas traité comme vérité live ;
- aucun document n'est exclu à cause de son nom ;
- les suffixes `_2`, `_3`, `_rev` ou autres ne déterminent aucune relation sans preuve binaire/sémantique ;
- `EXACT_DUPLICATE` exige un SHA-256 identique ;
- `SUPERSEDES` exige une preuve explicite ;
- SOURCE physique reste immuable ;
- le deep pilot NTLC existant n'est pas refait de zéro : seules les vérifications transversales nécessaires sont complétées.

## Suite immédiate

1. matérialiser les **85/85** PDF NTLC live ;
2. valider signatures PDF et tailles ;
3. calculer SHA-256 exhaustif ;
4. produire `inventory/hashes/NTLC.csv` en LF ;
5. qualifier les collisions exactes et seulement les relations de version prouvables ;
6. revalider le Git blob du registre après commit ;
7. mettre à jour NTLC, manifeste, doublons, `SUIVI.md` et `TODO.md`.

## Point de reprise

`SOURCE_VERSION=V22 | LIVE_TOTAL=3137 | NTLC_SNAPSHOT=81 | NTLC_LIVE=85 | NTLC_DELTA=+4 | NTLC_HASH=PENDING`
