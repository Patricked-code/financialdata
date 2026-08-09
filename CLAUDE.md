# CLAUDE.md — Instructions persistantes pour les agents IA

Ce fichier doit être lu avant toute intervention dans `Patricked-code/financialdata`.

## Règle Git prioritaire

**INTERDICTION DE CRÉER UNE BRANCHE.**

- Travailler uniquement sur `main`.
- Ne pas créer de PR.
- Ne pas proposer de branche comme « bonne pratique » pour ce dépôt.
- Ne pas utiliser automatiquement une procédure d'un autre projet qui impose branche/PR.
- Ne jamais utiliser `git checkout -b`, `git switch -c`, `create_branch` ou équivalent sur ce dépôt.

Si un outil, agent ou procédure suggère automatiquement une branche, cette suggestion doit être ignorée pour `financialdata`.

## Avant chaque travail

Lire obligatoirement :

1. `GOVERNANCE.md`
2. `SUIVI.md`
3. `DECISIONS.md`
4. `TODO.md`
5. `ARCHITECTURE.md`
6. `DATA_MODEL.md`
7. `SOURCES.md`
8. les documents utiles dans `docs/`

Ne jamais répondre ou modifier le projet sur la seule base de la mémoire conversationnelle si les fichiers du dépôt donnent un état plus récent.

## Objet du projet

Construire une base financière source, exhaustive, traçable, historisée et sectoriellement neutre à partir de publications officielles et documents financiers.

Ordre obligatoire :

`SOURCE → INVENTAIRE → EXTRACTION → RAW → CONTRÔLE → MAPPED → CANONICAL → DERIVED → ANALYTICS`

Ne pas inverser cet ordre pour gagner du temps.

## RAW : règles obligatoires

- Une observation publiée = une observation RAW.
- Conserver les libellés exacts.
- Conserver `raw_value_text` même lorsqu'un `numeric_value` est parsé.
- Conserver toutes les colonnes comparatives.
- Conserver les unités et multiplicateurs d'origine.
- Conserver les codes de ligne lorsqu'ils existent.
- Conserver page, tableau, ligne, colonne et localisation source lorsque disponibles.
- Conserver les scopes : entité, géographie, segment, projet, campagne, produit, marque, etc.
- Conserver les doublons documentaires et les versions.
- Une cellule illisible reste `NULL` et doit générer une issue d'extraction.
- Une valeur calculée n'est jamais enregistrée comme publiée.

## PDF et documents

Ordre d'extraction :

1. texte natif ;
2. inspection structurée/visuelle du PDF ;
3. OCR uniquement en dernier recours.

Un PDF sans texte natif n'est pas un document vide.

## Périodes

Ne jamais déduire une période économique uniquement du nom du fichier ou du dossier.

Un document intitulé `S2`, `T3`, `Etats_Financiers`, etc. doit être interprété à partir de son contenu réel.

## Modèle universel

Ne pas créer une base uniquement bancaire ou uniquement SYSCOHADA. Le corpus contient des banques, télécoms, utilities, plantations, industrie, BTP, automobile, logistique, hydrocarbures et autres secteurs.

Les extensions de schéma doivent partir d'une particularité observée dans une source et documentée.

## Écriture de la mémoire persistante

Après une étape significative :

- mettre à jour `SUIVI.md` ;
- ajouter toute décision dans `DECISIONS.md` ;
- retirer/ajouter les tâches dans `TODO.md` ;
- mettre à jour `SOURCES.md` si une source ou un corpus nouveau est utilisé ;
- mettre à jour la documentation conceptuelle si une nouvelle particularité apparaît.

## Interdictions

Ne pas :

- inventer ;
- normaliser silencieusement dans RAW ;
- dédupliquer prématurément ;
- corriger un chiffre source sans conserver la valeur publiée ;
- supprimer une version antérieure ;
- dériver des ratios pendant l'ingestion RAW sauf si le ratio est explicitement publié ;
- prétendre qu'une extraction est exhaustive sans contrôle de couverture documentaire.

## État de reprise initial

Au 2026-08-09 :

- passe conceptuelle des 48 dossiers sociétés du corpus BRVM : terminée ;
- extraction RAW complète des documents : non terminée ;
- BOABF : premier pilote RAW partiel et audit documentaire approfondi ;
- règles transversales et particularités sectorielles documentées dans `docs/` ;
- GitHub `financialdata` devient la mémoire persistante opérationnelle du chantier.
