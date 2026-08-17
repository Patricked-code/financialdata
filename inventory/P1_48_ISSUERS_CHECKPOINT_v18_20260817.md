# P1 — CHECKPOINT V18 — 48 ISSUERS — 2026-08-17

## Objet

Versionner le delta SOURCE détecté lors de la revérification live de `PRSC` avant tout calcul SHA-256 sur ce corpus.

## Baseline précédente

- checkpoint précédent : `inventory/P1_48_ISSUERS_CHECKPOINT_v17_20260817.md` ;
- total SOURCE V17 : **3 075 PDF** ;
- PRSC snapshot manifeste V17 : **68 PDF**.

## Revérification live PRSC

- émetteur : Tractafric Motors Côte d'Ivoire / `PRSC` ;
- dossier Drive canonique : `1uA4PVTKVuFPpR8uaQ87ORw3mzAIZ3f_h` ;
- recheck : recherche strictement bornée aux dossiers enfants réels avec `mimeType = application/pdf` ;
- dossiers enfants live observés : **25** — `1998–2007`, puis `2011–2025` ;
- les dossiers `2008`, `2009`, `2010` décrits dans l'inventaire initial ne sont pas présents dans l'arborescence live actuellement observable ;
- PDF live : **70** ;
- delta net PDF : **+2** par rapport au snapshot 68 ;
- un objet live dont le nom n'utilise pas le ticker est notamment `tractafric_motors_ci_-_rapport_dactivites_t1_2023.pdf`, ce qui confirme la nécessité du recheck parent-scoped.

Aucun fichier SOURCE n'est supprimé, déplacé ou renommé par cette opération. Le checkpoint décrit uniquement l'état live actuellement vérifiable.

## Nouveau total SOURCE

`3 075 + 2 = 3 077 PDF`

Le dénominateur canonique devient donc **V18 = 3 077 PDF** avant tout SHA PRSC.

## Règles de preuve

- le snapshot antérieur n'est pas traité comme vérité live ;
- un delta de structure de dossiers et un delta de fichiers sont documentés séparément ;
- aucun document n'est exclu à cause de son nom ;
- les suffixes `_2`, `_3`, `_rev` ne déterminent aucune relation sans preuve binaire/sémantique ;
- `EXACT_DUPLICATE` exige un SHA-256 identique ;
- `SUPERSEDES` exige une preuve explicite ;
- SOURCE physique reste immuable dans le processus de réconciliation.

## Suite immédiate

1. matérialiser les **70/70** PDF PRSC live ;
2. valider signature PDF et taille ;
3. calculer SHA-256 exhaustif ;
4. produire `inventory/hashes/PRSC.csv` ;
5. qualifier les collisions exactes et les relations de version prouvables, notamment EF 2023 plain/`_rev`, variantes S1 2023 et EF 2024/2025 ;
6. revalider le registre GitHub après commit ;
7. mettre à jour PRSC, manifeste, doublons, `SUIVI.md` et `TODO.md`.

## Point de reprise

`SOURCE_VERSION=V18 | LIVE_TOTAL=3077 | PRSC_SNAPSHOT=68 | PRSC_LIVE=70 | PRSC_DELTA=+2 | PRSC_HASH=PENDING`
