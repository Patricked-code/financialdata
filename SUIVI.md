# SUIVI — financialdata

Dernière mise à jour : 2026-08-09

## Point de reprise courant

Le dépôt `Patricked-code/financialdata` vient d'être initialisé comme mémoire persistante et dépôt canonique du chantier de données financières.

### Règle Git active

- branche autorisée : `main` uniquement ;
- création de branche : interdite ;
- Pull Request : non requise / ne pas en créer pour ce projet ;
- toute écriture future doit respecter `GOVERNANCE.md` et `CLAUDE.md`.

## Ce qui est déjà validé

### Gouvernance

- architecture par couches : SOURCE → RAW → MAPPED → CANONICAL → DERIVED → ANALYTICS ;
- lineage/versioning et data quality sont transversaux ;
- le RAW est immuable/versionné ;
- une observation publiée = une observation RAW ;
- les valeurs publiées et recalculées sont séparées ;
- les périodes sont déterminées par le contenu réel, pas le nom du fichier ;
- les doublons et versions sont conservés ;
- aucune cellule illisible n'est inventée.

### Corpus BRVM

Source documentaire principale explorée : Google Drive `RAPO / Rapport V2`.

- 48 dossiers sociétés ont fait l'objet d'une passe de découverte conceptuelle ;
- cette passe est terminée : `DISCOVERY_PASS_48_ISSUERS_COMPLETE` ;
- l'extraction RAW intégrale de tous les PDF n'est pas terminée : `RAW_EXTRACTION_ALL_DOCUMENTS = NOT_COMPLETE`.

### Pilotes approfondis

- BOABF — banque : audit documentaire détaillé, inventaire 2009–2025 + divers, pilote RAW 2009 dans une base SQLite locale antérieure ;
- NTLC — industrie/SYSCOHADA ;
- SNTS — télécom/IFRS/KPI opérationnels ;
- CIEC — utility/concession/périmètres économiques multiples.

### Particularités transversales déjà détectées

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
- audit vs examen limité ;
- changement de nom d'un émetteur ;
- événements exceptionnels et corporate actions.

## Dernières actions réalisées dans ce dépôt

- `README.md` initialisé ;
- `GOVERNANCE.md` créé ;
- `CLAUDE.md` créé ;
- mémoire persistante en cours de consolidation ;
- aucune branche créée.

## Prochaine étape obligatoire

1. terminer la documentation initiale du dépôt ;
2. consolider le document détaillé de gouvernance BRVM sous `docs/` ;
3. consigner la matrice des 48 sociétés ;
4. seulement ensuite commencer l'inventaire exhaustif et l'extraction RAW société par société ;
5. mettre à jour ce fichier après chaque lot.

## Règle anti-perte de contexte

Avant toute nouvelle session ou reprise :

1. lire ce fichier ;
2. vérifier le dernier commit sur `main` ;
3. vérifier `DECISIONS.md` et `TODO.md` ;
4. ne jamais repartir d'un souvenir de conversation lorsque le dépôt contient un état plus récent.
