# SUIVI — financialdata

Dernière mise à jour : 2026-08-09

## Point de reprise courant

Le dépôt `Patricked-code/financialdata` est la **mémoire persistante et le dépôt canonique** du chantier de données financières.

### Règle Git active

- branche autorisée : `main` uniquement ;
- création de branche : interdite ;
- Pull Request : non requise / ne pas en créer pour ce projet.

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
- script inspecté : mapping de 48 sociétés et collecte historique depuis BRVM ;
- méthode P1 documentée dans `inventory/README.md` et `inventory/P1_ROOT_MANIFEST.md` ;
- règle d'attribution émetteur ajoutée via `D024`.

### Script Python — vérité actuelle

- fichier : `telecharger_rapports_brvm.py`
- Drive ID : `1F1WRVMG4C27EOTMq5Gt9FT9Mosv-Rryz`
- taille : 14546 octets
- MIME : `text/x-python`
- `D021` = ancien constat erroné, conservé mais superseded ;
- `D022` = correction canonique.

### Émetteurs P1 déjà inventoriés

#### 1. SIVC — Air Liquide Côte d'Ivoire

- 22 dossiers annuels ;
- 53 fichiers ;
- 2024 présent mais vide ;
- 2015 absent ;
- document 2025 explicitement `annule et remplace` ;
- hash : en attente ;
- registre : `inventory/SIVC.md`.

#### 2. BOABF — Bank of Africa Burkina Faso

- 18 sous-dossiers : 2009–2025 + `divers` ;
- 57 fichiers ;
- 2015, 2017, 2018 vides directement ;
- `divers` contient des sources couvrant notamment 2017 ;
- une paire de doublons binaires déjà vérifiée ;
- registre : `inventory/BOABF.md`.

#### 3. BOAB — Bank of Africa Bénin

- 29 sous-dossiers : 1998–2025 + `divers` ;
- 59 fichiers ;
- dossiers vides observés : 1999, 2000, 2001, 2002, 2005, 2015, 2016 ;
- présence de noms source non standardisés ;
- anomalie P1 : un avis `TPCI 5,90% 2021-2031` est classé dans le dossier BOAB sans lien émetteur démontré ;
- statut de ce fichier : `OUT_OF_SCOPE_REVIEW` ;
- registre : `inventory/BOAB.md`.

### Progression P1

- émetteurs avec inventaire dossiers/fichiers documenté : **3 / 48** ;
- émetteurs restant à inventorier : **45** ;
- hash global : `NOT_COMPLETE` ;
- résolution exhaustive des périodes économiques : `NOT_COMPLETE` ;
- extraction RAW : ne pas démarrer comme suite normale de P1 avant couverture suffisante.

## Nouvelle règle P1 issue de BOAB

Un fichier physiquement rangé sous une société n'est pas automatiquement validé comme document de cette société.

Le registre SOURCE devra permettre une validation d'attribution (`VALIDATED`, `REVIEW_REQUIRED`, `OUT_OF_SCOPE_CONFIRMED` ou équivalent) tout en conservant le chemin historique.

## Prochaine action exacte

**Continuer P1 avec le 4e émetteur non inventorié, sans refaire SIVC, BOABF ou BOAB.**

Dans l'ordre du mapping historique, le prochain émetteur est : **BOAC — Bank of Africa Côte d'Ivoire**.

Procédure :

1. lister le dossier BOAC ;
2. inventorier tous les sous-dossiers directs ;
3. inventorier tous les fichiers rattachés ;
4. créer `inventory/BOAC.md` ;
5. signaler dossiers vides, `divers`, collisions de noms et anomalies d'attribution ;
6. mettre à jour `TODO.md` et `SUIVI.md`.

## Règle anti-perte de contexte

Avant toute reprise : lire `GOVERNANCE.md`, `AGENTS.md`, `CLAUDE.md`, ce fichier, `DECISIONS.md`, `TODO.md`, puis `inventory/README.md` et les inventaires déjà créés.

## Point de reprise exact

`P1_IN_PROGRESS → INVENTORY_COMPLETE_3_OF_48 → NEXT = BOAC`
