# P1 — CHECKPOINT V19 — 48 ISSUERS — 2026-08-17

## Objet

Versionner le delta SOURCE détecté lors de la revérification live de `PALC` avant tout calcul SHA-256 sur ce corpus.

## Baseline précédente

- checkpoint précédent : `inventory/P1_48_ISSUERS_CHECKPOINT_v18_20260817.md` ;
- total SOURCE V18 : **3 077 PDF** ;
- PALC snapshot manifeste V18 : **75 PDF**.

## Revérification live PALC

- émetteur : Palm Côte d'Ivoire / `PALC` ;
- dossier Drive canonique : `1w2XGE38g12wfH6Dm0UdZKAraYmg7vzNZ` ;
- recheck : recherche strictement bornée aux dossiers enfants réels avec `mimeType = application/pdf` ;
- dossiers enfants live observés : **25** ;
- dossiers présents : `1999`, `2001`, puis `2003–2025` ;
- dossiers `1998`, `2000`, `2002` non observés ;
- PDF live : **98** ;
- delta net PDF : **+23** par rapport au snapshot 75 ;
- le corpus contient des noms non strictement normalisés, notamment `efp_-_palm_ci_-_2014.pdf` et `190430_rapport_dactivite_2nd_semestre_2018_-_palm_ci.pdf`, confirmant que le recheck doit être parent-scoped et non fondé sur le ticker seul.

Aucun fichier SOURCE n'est supprimé, déplacé ou renommé. Le checkpoint décrit uniquement l'état live actuellement vérifiable.

## Nouveau total SOURCE

`3 077 + 23 = 3 100 PDF`

Le dénominateur canonique devient donc **V19 = 3 100 PDF** avant tout SHA PALC.

## Règles de preuve

- le snapshot antérieur n'est pas traité comme vérité live ;
- aucun document n'est exclu à cause de son nom ;
- les suffixes `_2`, `_3`, `_rev` ne déterminent aucune relation sans preuve binaire/sémantique ;
- `EXACT_DUPLICATE` exige un SHA-256 identique ;
- `SUPERSEDES` exige une preuve explicite ;
- SOURCE physique reste immuable dans le processus de réconciliation.

## Suite immédiate

1. matérialiser les **98/98** PDF PALC live ;
2. valider signatures PDF et tailles ;
3. calculer SHA-256 exhaustif ;
4. produire `inventory/hashes/PALC.csv` ;
5. qualifier les collisions exactes et les relations de version prouvables, notamment `2009_Rapport_Annuel_PALC_rev.pdf` et les nombreuses variantes annuelles historiques ;
6. revalider le registre GitHub après commit ;
7. mettre à jour PALC, manifeste, doublons, `SUIVI.md` et `TODO.md`.

## Point de reprise

`SOURCE_VERSION=V19 | LIVE_TOTAL=3100 | PALC_SNAPSHOT=75 | PALC_LIVE=98 | PALC_DELTA=+23 | PALC_HASH=PENDING`
