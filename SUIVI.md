# SUIVI — financialdata

Dernière mise à jour : 2026-08-09

## Point de reprise courant

Le dépôt `Patricked-code/financialdata` est désormais initialisé comme **mémoire persistante et dépôt canonique** du chantier de données financières.

### Règle Git active

- branche autorisée : `main` uniquement ;
- création de branche : interdite ;
- Pull Request : non requise / ne pas en créer pour ce projet ;
- toute écriture future doit respecter `GOVERNANCE.md`, `AGENTS.md` et `CLAUDE.md`.

## P0 — Gouvernance initiale

**STATUT : COMPLETE**

Fichiers canoniques présents :

- `README.md`
- `GOVERNANCE.md`
- `AGENTS.md`
- `CLAUDE.md`
- `SUIVI.md`
- `DECISIONS.md`
- `TODO.md`
- `ARCHITECTURE.md`
- `DATA_MODEL.md`
- `SOURCES.md`
- `docs/BRVM_RAW_DATABASE_GOVERNANCE.md`
- `docs/ISSUER_DISCOVERY_MATRIX.md`

## Ce qui est déjà validé

### Gouvernance des données

- architecture par couches : SOURCE → RAW → MAPPED → CANONICAL → DERIVED → ANALYTICS ;
- lineage/versioning et data quality sont transversaux ;
- le RAW est immuable/versionné ;
- une observation publiée = une observation RAW ;
- les valeurs publiées et recalculées sont séparées ;
- les périodes sont déterminées par le contenu réel, pas le nom du fichier ;
- les doublons et versions sont conservés ;
- aucune cellule illisible n'est inventée ;
- aucune évolution de schéma n'est introduite sans observation source documentée.

### Corpus BRVM

Source documentaire principale explorée : Google Drive `RAPO / Rapport V2`.

- 48 dossiers sociétés ont fait l'objet d'une passe de découverte conceptuelle ;
- cette passe est terminée : `DISCOVERY_PASS_48_ISSUERS_COMPLETE` ;
- l'extraction RAW intégrale de tous les PDF n'est pas terminée : `RAW_EXTRACTION_ALL_DOCUMENTS = NOT_COMPLETE` ;
- la liste exacte des 48 dossiers est conservée dans `docs/ISSUER_DISCOVERY_MATRIX.md`.

### Pilotes approfondis

- BOABF — banque : audit documentaire détaillé, inventaire 2009–2025 + divers, pilote RAW 2009 dans une base SQLite antérieure ;
- NTLC — industrie/SYSCOHADA ;
- SNTS — télécom/IFRS/KPI opérationnels ;
- CIEC — utility/concession/périmètres économiques multiples.

### Particularités transversales documentées

- codes comptables de ligne ;
- TAFIRE / flux / capitaux propres ;
- ratios publiés ;
- KPI opérationnels physiques ;
- géographies et segments ;
- contrats de concession ;
- stock vs flow ;
- scopes individuels vs consolidés ;
- IFRS individuels possibles ;
- campagnes agricoles et sites ;
- projets/chantiers ;
- produits, marques et données de marché externe ;
- prévisions/guidance distinctes du réalisé ;
- ratios prudentiels ;
- audit vs examen limité vs attestation ;
- changement de nom d'un émetteur ;
- événements exceptionnels et corporate actions ;
- statuts distincts comptes audités / rapport CAC ;
- unités sectorielles : GWh, tonnes, KT, hectares, nombre, transactions, $/baril, etc.

## Dernières actions réalisées

- documentation initiale complète migrée dans GitHub ;
- règles `main-only` inscrites dans `README.md`, `GOVERNANCE.md`, `AGENTS.md`, `CLAUDE.md`, `TODO.md` et la documentation détaillée ;
- source Drive reliée dans `SOURCES.md` ;
- gouvernance BRVM détaillée migrée sous `docs/` ;
- matrice 48 sociétés créée ;
- aucune branche créée pendant cette initialisation.

## Prochaine étape obligatoire

La prochaine phase est **P1 — Inventaire documentaire exhaustif**.

Ordre :

1. inventorier intégralement les dossiers et documents de chaque société ;
2. calculer les hash et détecter versions/doublons ;
3. déterminer les périodes économiques réelles ;
4. classer les familles documentaires ;
5. mesurer la couverture ;
6. seulement ensuite lancer l'extraction RAW exhaustive société par société ;
7. mettre à jour ce fichier après chaque lot.

## Règle anti-perte de contexte

Avant toute nouvelle session ou reprise :

1. lire `GOVERNANCE.md` ;
2. lire `AGENTS.md` ;
3. lire `CLAUDE.md` ;
4. lire ce fichier ;
5. vérifier le dernier commit sur `main` ;
6. vérifier `DECISIONS.md` et `TODO.md` ;
7. lire les documents techniques pertinents ;
8. ne jamais repartir d'un souvenir de conversation lorsque le dépôt contient un état plus récent.

## Point de reprise exact

`P0_GOVERNANCE_COMPLETE → NEXT = P1_DOCUMENT_INVENTORY`
