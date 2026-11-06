# CLAUDE.md — Instructions persistantes pour les agents IA

## Priorité D041 — boucle de l'agent connecté, sans API externe de codage

**Premier passage obligatoire :** lire les onze fichiers de la liste canonique `README.md`, de `GOVERNANCE.md` à `docs/ISSUER_DISCOVERY_MATRIX.md`, avant de consulter les registres techniques `factory/` ou de coder. Le lien vers `factory/ARRIVAL.md` ne déroge pas à cet ordre.

Tout agent ChatGPT/Claude **déjà connecté et autorisé sur GitHub** doit utiliser ses capacités de génération et d'édition de code pour appliquer `factory/ARRIVAL.md`. Cette voie n'exige **aucune clé Anthropic supplémentaire**. La commande `factory.entry` est un diagnostic de lecture ; elle n'est pas un générateur de code, ni la preuve que l'agent est authentifié. Si le connecteur GitHub permet d'écrire, l'agent peut coder et apporter les changements gouvernés sans appeler `factory/provider.py` : vérifier l'état live, le travail, la portée autorisée et les conflits, produire tests/preuves exact-head, publier selon la politique `main`, puis enregistrer un checkpoint et passer au travail admissible suivant.

`PROGRAM_AUTO_CONTINUE` de la PR #95 du MCP constitue une **référence historique de méthode** et non une importation de son moteur runtime. Pour FinancialData, appliquer `FD_AGENT_AUTO_CONTINUE` et la source d'autorité du présent dépôt. Ne pas s'arrêter après une tâche DONE prouvée si un travail compatible est immédiatement sélectionnable. Ne pas prétendre à une exécution autonome en arrière-plan après la fin de la conversation.



## Entrée conversationnelle immédiate — FD-AGENT-ARRIVAL-V1

Lorsqu'un assistant (ChatGPT, Claude ou agent de développement autorisé) reçoit « connecte-toi à financialdata en tant qu'agent codeur », **lire et appliquer [factory/ARRIVAL.md](factory/ARRIVAL.md)** puis les autorités listées ci-dessous. Vérifier le dépôt `Patricked-code/financialdata`, l'identité GitHub et `main`, le dernier run CI et `factory/state.json`. Utiliser `python -m factory.entry --role coder --agent agent-session` si un runner existe ; sinon reproduire le diagnostic depuis les outils GitHub. En l'absence de travail READY, sélectionner le programme prioritaire et préparer sa prochaine qualification gouvernée, sans transformer une tâche historique en exécution non autorisée. Toute écriture doit rester compatible avec la politique main-only, les tests et les preuves.


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
2. `AGENTS.md`
3. `CLAUDE.md`
4. `SUIVI.md`
5. `DECISIONS.md`
6. `TODO.md`
7. `ARCHITECTURE.md`
8. `DATA_MODEL.md`
9. `SOURCES.md`
10. `docs/BRVM_RAW_DATABASE_GOVERNANCE.md`
11. `docs/ISSUER_DISCOVERY_MATRIX.md`

**Ensuite seulement**, lire `ROADMAP.md`, le point de reprise `factory/CONTINUITY.md`, `factory/HANDOFF.json`, le registre `factory/state.json`, le catalogue `factory/blueprints.json` et les documents de tâche. L'ordre des onze premières lectures est celui de `README.md` et `GOVERNANCE.md`.

Ne jamais répondre ou modifier le projet sur la seule base de la mémoire conversationnelle si les fichiers du dépôt donnent un état plus récent.

## Continuité obligatoire / zéro régression

Tout agent doit reprendre exactement au point indiqué par `SUIVI.md`.

Avant de proposer ou d'appliquer une modification :

- vérifier ce qui existe déjà ;
- vérifier le dernier commit `main` ;
- vérifier les décisions actives ;
- vérifier le backlog restant ;
- déterminer si le besoin est déjà couvert ;
- mesurer l'impact sur l'historique, la provenance, le RAW et les interfaces existantes.

Ne jamais :

- redémarrer le projet de zéro ;
- créer un deuxième modèle parallèle ;
- effacer une décision antérieure ;
- écraser une extraction ou une version précédente ;
- réduire la couverture documentaire déjà obtenue ;
- perdre des champs, des sources, des relations ou des preuves lors d'une évolution.

Toute évolution suit :

`ÉTAT EXISTANT → PREUVE → IMPACT → DÉCISION DOCUMENTÉE → MODIFICATION COMPATIBLE → VÉRIFICATION NON-RÉGRESSION → SUIVI`

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

## Sources révisables

Les sources peuvent être réévaluées ou remplacées par de meilleures versions au fil du projet.

Mais toute révision doit être historisée :

- conserver l'ancienne source ;
- enregistrer la nouvelle source/version ;
- documenter le motif ;
- préserver les facts RAW liés à l'ancienne source ;
- utiliser une relation de version/supersession plutôt qu'un écrasement.

Consulter `SOURCES.md` avant de modifier le statut ou la priorité d'une source.

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
- mettre à jour `SOURCES.md` si une source ou un corpus nouveau est utilisé ou révisé ;
- mettre à jour la documentation conceptuelle si une nouvelle particularité apparaît.

## Interdictions

Ne pas :

- inventer ;
- normaliser silencieusement dans RAW ;
- dédupliquer prématurément ;
- corriger un chiffre source sans conserver la valeur publiée ;
- supprimer une version antérieure ;
- dériver des ratios pendant l'ingestion RAW sauf si le ratio est explicitement publié ;
- prétendre qu'une extraction est exhaustive sans contrôle de couverture documentaire ;
- propager une information non vérifiée comme vérité persistante.

## État de reprise initial

Au 2026-08-09 :

- passe conceptuelle des 48 dossiers sociétés du corpus BRVM : terminée ;
- extraction RAW complète des documents : non terminée ;
- BOABF : premier pilote RAW partiel et audit documentaire approfondi ;
- règles transversales et particularités sectorielles documentées dans `docs/` ;
- GitHub `financialdata` est la mémoire persistante opérationnelle du chantier ;
- prochaine phase : `P1_DOCUMENT_INVENTORY` ;
- vérification Drive : aucun script `.py` confirmé à la racine de `RAPO / Rapport V2` au 2026-08-09.

## D043 — Usine de codage comme composant de l'architecture actuelle

À chaque entrée d'agent, `FD_AGENT_AUTO_CONTINUE` réutilise le processus documentaire et financier de `ROADMAP.md` et `ARCHITECTURE.md`. L'usine agit **sur les travaux de développement nécessaires à ce processus**, jamais comme une nouvelle couche de données, un nouveau backlog métier ou un orchestrateur indépendant. Vérifier l'ancrage `process_anchor` au programme et aux sources, les dépendances ainsi que les preuves. Les phases P1/P1-FRESH/P1-R/P2–P8 conservent leur identité historique ; toute évolution est additive, non destructive et attestée.
