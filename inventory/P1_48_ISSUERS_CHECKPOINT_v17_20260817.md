# P1 — CHECKPOINT V17 — 2026-08-17

## Objet

Versionner le delta SOURCE découvert lors de la revérification live de SOLIBRA / `SLBC` **avant tout calcul SHA-256 du corpus SLBC**.

## Base précédente

- checkpoint précédent : `inventory/P1_48_ISSUERS_CHECKPOINT_v16_20260817.md` ;
- SOURCE global V16 : **3 070 PDF** ;
- SLBC dans le snapshot précédent : **65 PDF**.

## Revérification SLBC

- dossier Drive canonique : `1U41GdtRNU8QYqHYI8WdLJlwv1vFaukVy` ;
- dossiers directs contrôlés : **28 = 1998–2025** ;
- filtre de preuve : parents Drive réels + `mimeType=application/pdf` ;
- live strict : **70 PDF** ;
- delta SLBC : **+5 PDF**.

Le périmètre live inclut toutes les sources PDF physiquement présentes dans les dossiers annuels, y compris les publications non financières au sens strict lorsqu'elles font partie du corpus SOURCE (par exemple l'erratum d'assemblée générale visible dans 2025). Aucun objet n'est exclu silencieusement sur la seule base de son type documentaire.

## Nouveau dénominateur

- SLBC : **70 PDF** ;
- SOURCE global V17 : **3 075 PDF** ;
- variation globale V16 → V17 : **+5 PDF**.

## Règle de reprise

Le nouveau dénominateur est persisté avant SHA. La prochaine étape autorisée est :

`SLBC_70_OF_70_MATERIALIZATION -> PDF/SIZE_VALIDATION -> SHA256 -> COLLISION/VERSION_REVIEW -> HASH_REGISTRY_POST_COMMIT_VALIDATION`

Aucune suppression, déduplication ou relation de version n'est déduite du nom des fichiers.
