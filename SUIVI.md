# SUIVI — financialdata

Dernière mise à jour : 2026-08-09

## Point de reprise courant

Le dépôt `Patricked-code/financialdata` est la mémoire persistante et le dépôt canonique du chantier.

### Règle Git active

- `main` uniquement ;
- aucune branche ;
- aucune PR normale.

## Roadmap canonique

`P0 GOUVERNANCE → P1 SOURCE/INVENTAIRE + P1-R RECOGNITION → P1-FRESH → P2 RAW SCHEMA → P3 RAW EXTRACTION → P4 QUALITY/LINEAGE → P5 MAPPED → P6 CANONICAL → P7 DERIVED → P8 ANALYTICS`.

Architecture : `SOURCE → RAW → MAPPED → CANONICAL → DERIVED → ANALYTICS`.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire société

- sociétés : **48 / 48** ;
- PDF recensés : **2 950** ;
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT.md` ;
- index machine-lisible : `inventory/p1_issuer_manifest.csv`.

L'inventaire dossiers/fichiers 48/48 est terminé. P1 reste ouvert pour les passes transversales.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md` ;
- fichier : `inventory/p1_document_manifest.csv` ;
- couverture actuelle : **12 / 2 950 lignes SOURCE**.

Émetteurs/cas déjà présents :

- BICC 2022 : 1 source ;
- BIIC : **2 / 2 sources** ;
- SNTS : anomalie ONATEL seed ;
- TRITRAF : **8 / 8 sources**.

Le cas SNTS/ONATEL reste `issuer_assignment_status = REVIEW_REQUIRED`.

## P1_TRANSVERSE — SHA256

- SHA-256 calculés : **8 / 2 950** ;
- premier émetteur complet : **TRITRAF 8 / 8**.

Hashes TRITRAF enregistrés dans `inventory/p1_document_manifest.csv` et `inventory/TRITRAF.md`.

### Verdict TRITRAF 2004

- `2004_Rapport_Annuel_TRITRAF.pdf` : 11 000 341 octets ;
- `2004_Rapport_Annuel_TRITRAF_2.pdf` : 49 279 octets ;
- SHA-256 différents.

Conclusion : **pas de doublon binaire**. La relation éventuelle de version/contenu reste à examiner ; `_2` n'est jamais utilisé comme preuve de doublon.

## P1-R — reconnaissance

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023.
Deep pilots acquis : BOABF, CIEC, NTLC, SNTS.

Règles acquises : métadonnées PDF non souveraines ; STOCK/FLOW contextuel ; variations publiées = RAW ; T1/T2/T3/T4/S1/S2 ; framework vs scope indépendants ; recherche plafonnée ≠ total SOURCE ; attribution dossier ≠ attribution émetteur.

## Passes transversales restantes

1. compléter le manifeste jusqu'à **2 950 / 2 950** ;
2. SHA-256 jusqu'à **2 950 / 2 950** ;
3. doublons/versions ;
4. périodes économiques ;
5. attribution émetteur ;
6. couverture ;
7. fraîcheur BRVM / P1-FRESH.

## Prochaine action exacte

Continuer `EXPAND_DOCUMENT_MANIFEST` par les corpus courts, puis calculer leurs hashes :

`CBIBF (8) → ORAC (14) → SICC (19) → MVSC (20) → UNLC (20)`.

Ne pas revenir sur TRITRAF sauf pour la comparaison sémantique des deux documents 2004.

## Point de reprise exact

`INVENTORY_48_OF_48 = COMPLETE | 2950_PDFS | DOCUMENT_MANIFEST = 12/2950 | SHA256 = 8/2950 | NEXT = CBIBF`
