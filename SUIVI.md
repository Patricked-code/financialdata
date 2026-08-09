# SUIVI — financialdata

Dernière mise à jour : 2026-08-09

## Point de reprise courant

Le dépôt `Patricked-code/financialdata` est la **mémoire persistante et le dépôt canonique** du chantier de données financières.

### Règle Git active

- branche autorisée : `main` uniquement ;
- création de branche : interdite ;
- Pull Request : non requise / ne pas en créer pour ce projet ;
- toute écriture future doit respecter `GOVERNANCE.md`, `AGENTS.md` et `CLAUDE.md`.

### Règle universelle des agents

Tout agent qui se connecte au dépôt doit **continuer le travail existant au point de reprise officiel, sans régression**.

Il doit :

1. lire la mémoire persistante ;
2. vérifier `main` et le dernier commit ;
3. reprendre les tâches restantes au lieu de recréer le projet ;
4. préserver les décisions, sources, versions, extractions et structures déjà validées ;
5. documenter toute évolution structurante avant de l'appliquer ;
6. vérifier l'absence de perte de couverture ou de provenance après changement.

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
- aucune évolution de schéma n'est introduite sans observation source documentée ;
- les sources peuvent être revues à la longue mais toute révision doit être historisée ;
- aucune révision de source ne réécrit silencieusement les facts RAW historiques.

### Corpus BRVM

Source documentaire principale explorée : Google Drive `RAPO / Rapport V2`.

- 48 dossiers sociétés ont fait l'objet d'une passe de découverte conceptuelle ;
- cette passe est terminée : `DISCOVERY_PASS_48_ISSUERS_COMPLETE` ;
- l'extraction RAW intégrale de tous les PDF n'est pas terminée : `RAW_EXTRACTION_ALL_DOCUMENTS = NOT_COMPLETE` ;
- la liste exacte des 48 dossiers est conservée dans `docs/ISSUER_DISCOVERY_MATRIX.md`.

### Vérification script Python Drive

Vérification effectuée le 2026-08-09 sur la racine exacte de `RAPO / Rapport V2` :

- aucun fichier `.py` retourné ;
- aucun fichier nommé avec `python` retourné ;
- aucun fichier nommé avec `script` retourné.

**Conclusion actuelle : aucun script Python n'est confirmé à cette racine.**

L'ancienne supposition inverse ne doit plus être propagée. Si un script est découvert ultérieurement dans un sous-dossier ou ajouté au corpus, enregistrer son identifiant exact dans `SOURCES.md`.

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
- règles `main-only` inscrites dans la mémoire persistante ;
- règle universelle de continuité sans régression ajoutée dans `AGENTS.md`, `GOVERNANCE.md` et `CLAUDE.md` ;
- politique de révision/versioning des sources ajoutée à `GOVERNANCE.md`, `SOURCES.md` et `DECISIONS.md` ;
- correction documentée concernant l'absence de script Python confirmé à la racine Drive ;
- source Drive reliée dans `SOURCES.md` ;
- gouvernance BRVM détaillée migrée sous `docs/` ;
- matrice 48 sociétés créée ;
- aucune branche créée pendant ces travaux.

## Prochaine étape obligatoire

La prochaine phase reste **P1 — Inventaire documentaire exhaustif**.

Ordre :

1. inventorier intégralement les dossiers et documents de chaque société ;
2. calculer les hash et détecter versions/doublons ;
3. déterminer les périodes économiques réelles ;
4. classer les familles documentaires ;
5. mesurer la couverture ;
6. enregistrer le statut/version des sources ;
7. seulement ensuite lancer l'extraction RAW exhaustive société par société ;
8. mettre à jour ce fichier après chaque lot.

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
