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

Tout agent doit reprendre le projet au point officiel, préserver l'existant et continuer sans régression.

## P0 — Gouvernance initiale

**STATUT : COMPLETE**

## P1 — Inventaire documentaire exhaustif

**STATUT : IN_PROGRESS**

### Socle P1 terminé

- racine `RAPO / Rapport V2` vérifiée par liste directe ;
- 48 dossiers société confirmés ;
- dossier de gouvernance séparé confirmé ;
- script `telecharger_rapports_brvm.py` confirmé à la racine ;
- script inspecté : mapping de 48 sociétés, collecte depuis BRVM, classement historique par nom de fichier ;
- méthode P1 documentée dans `inventory/README.md` et `inventory/P1_ROOT_MANIFEST.md`.

### Correction importante sur le script

Une recherche Drive textuelle avait initialement manqué le script. La liste directe du dossier l'a ensuite confirmé.

Source de vérité actuelle :

- fichier : `telecharger_rapports_brvm.py`
- Drive ID : `1F1WRVMG4C27EOTMq5Gt9FT9Mosv-Rryz`
- taille : 14546 octets
- MIME : `text/x-python`

La décision erronée historique est conservée comme `D021` mais marquée `SUPERSEDED_BY_D022` dans `DECISIONS.md`.

### Émetteurs P1 déjà inventoriés

#### 1. SIVC — Air Liquide Côte d'Ivoire

- dossier Drive : `1TkwLDXla5LKvdpQ_KSEFrl_yNz-X1AB2`
- 22 dossiers annuels observés ;
- 53 fichiers inventoriés ;
- dossier 2024 présent mais vide ;
- dossier 2015 absent ;
- au moins un document 2025 nommé explicitement `annule et remplace le precedent publie` ;
- hash : en attente ;
- registre : `inventory/SIVC.md`.

#### 2. BOABF — Bank of Africa Burkina Faso

- dossier Drive : `1hQwExoX3z7LZKg89inSre8bKGjFoZ-lP`
- 18 sous-dossiers : 2009–2025 + `divers` ;
- 57 fichiers inventoriés ;
- dossiers directs 2015, 2017, 2018 vides ;
- `divers` contient des sources couvrant notamment 2017 ;
- une paire de doublons binaires `divers_Etats_Financiers_BOABF*.pdf` possède déjà un SHA-256 vérifié ;
- hash global : incomplet ;
- registre : `inventory/BOABF.md`.

### Progression P1

- émetteurs avec inventaire dossiers/fichiers documenté : **2 / 48** ;
- émetteurs restant à inventorier : **46** ;
- hash global : `NOT_COMPLETE` ;
- résolution exhaustive des périodes économiques : `NOT_COMPLETE` ;
- extraction RAW : toujours `NOT_STARTED_AS_P1_OUTPUT` / ne pas confondre avec les pilotes antérieurs.

## Règles de données déjà validées

- architecture : SOURCE → RAW → MAPPED → CANONICAL → DERIVED → ANALYTICS ;
- une observation publiée = une observation RAW ;
- source, version et provenance historisées ;
- périodes déterminées par contenu réel ;
- doublons/versions conservés ;
- source révisable mais historique immuable ;
- aucune évolution de schéma sans observation documentée.

## Prochaine action exacte

**Continuer P1 à partir du 3e émetteur non inventorié.**

Ordre de travail :

1. ouvrir le dossier société ;
2. lister les sous-dossiers directs ;
3. inventorier tous les fichiers de ces parents ;
4. écrire/mettre à jour `inventory/<TICKER>.md` ;
5. ne pas conclure qu'un suffixe `_2/_3` est un doublon sans hash ;
6. mettre à jour `TODO.md` et ce fichier après chaque lot ;
7. ne pas démarrer P2/P3 prématurément.

## Règle anti-perte de contexte

Avant toute nouvelle session ou reprise :

1. lire `GOVERNANCE.md` ;
2. lire `AGENTS.md` ;
3. lire `CLAUDE.md` ;
4. lire ce fichier ;
5. vérifier le dernier commit sur `main` ;
6. vérifier `DECISIONS.md` et `TODO.md` ;
7. lire `inventory/README.md` et les inventaires existants ;
8. ne jamais refaire SIVC/BOABF depuis zéro sauf contrôle ciblé justifié.

## Point de reprise exact

`P1_IN_PROGRESS → INVENTORY_COMPLETE_2_OF_48 → NEXT = THIRD_UNINVENTORIED_ISSUER`
