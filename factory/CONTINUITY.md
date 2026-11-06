# FD-AUTONOMY-V1 — mandat, registre et point de reprise canonique

Date de construction : 2026-11-06. Dépôt : Patricked-code/financialdata, branche unique main.

## Mandat immuable

Construire un dispositif autonome de programmes, tâches, unités de travail, codage, validation CI et reprise. Continuer ROADMAP.md, TODO.md, SUIVI.md, DECISIONS.md, GOV...; préserver les documents PDF, les manifestes, la provenance RAW, les versions et les décisions. Aucun Codex, aucune dépendance MCP, aucun système concurrent. La politique main-only demeure obligatoire.

## Autorités et chaîne de continuité

- Gouvernance de premier rang : GOVERNANCE.md, AGENTS.md, CLAUDE.md.
- Mandat métier et programme : README.md, ROADMAP.md, DATA_MODEL.md, ARCHITECTURE.md.
- Travaux existants : TODO.md, SUIVI.md, DECISIONS.md.
- Projection opérationnelle unique : factory/state.json (projet, programmes, tâches, UTL, agents, events).
- Tâches autonomes gouvernées : factory/blueprints.json (version, dépendances, limites d'écriture et critères).
- Moteur unique : factory/engine.py ; extension additive tasking.py ; adaptateurs coder.py et publisher.py.
- Preuves : factory/evidence/, journal événementiel SHA-chaîné dans state.json, GitHub Actions run ID et commit SHA.
- Exécution hébergée : .github/workflows/factory-autonomy.yml, périodique ou manuelle.
- Validation indépendante : .github/workflows/factory-validation.yml.

## Circuit canonique

ADMISSION → IMPORT ROADMAP/TODO → FABRIQUE TASK BLUEPRINT → UTL PLAN/CODE/VALIDATE/PUBLISH/ATTEST → ADMISSIBILITÉ (READY, dépendances DONE, chemins autorisés) → GÉNÉRATION MODÈLE SANS ÉCRITURE → VALIDATION ISOLÉE SANS SECRET → PUBLISH SUR main AVEC SHA ATTENDU → PUBLISHED_PENDING_CI → ATTESTATION DU RUN SUCCÈS/ÉCHEC → DONE/BLOCKED → TÂCHE SUIVANTE.

Les travaux historiques TODO ne sont jamais rendus auto-exécutables implicitement : une carte versionnée explicite est requise. Cela évite d'inventer des données à partir de libellés insuffisants.

## Coordonnées de reprise

Continuity ID : FD-AUTONOMY-V1.
Première base de développement : commit 22deeae0e55d7d5a4c60515d107968444f1b9380.
Premiers travaux gouvernés :
1. FD-AUTO-P1-MANIFEST-CHECKER : validation non destructive des CSV P1.
2. FD-AUTO-P1-HASH-CHECKER : contrôle non destructif des SHA-256 (dépend du précédent).

Pour reprendre : lire cette page et SUIVI.md, vérifier main et state.json, consulter le dernier workflow run et ses artefacts. Si PUBLISHED_PENDING_CI, réconcilier le run GitHub avant tout nouveau travail. Ne jamais marquer DONE à partir d'un simple commit ou d'un test non attesté. En cas d'échec, conserver BLOCKED et les preuves, sans effacer de données.

## Droits et séparation des rôles

- Validate / generated tests : contents:read, sans clé de modèle.
- Generate : contents:read + ANTHROPIC_API_KEY temporaire, sans écriture Git.
- Reconcile : contents:write et actions:read ; uniquement state.json.
- Publish : contents:write et actions:write ; exclusivement chemins Python bornés et preuves.
- Writer global : groupe GitHub Actions de concurrence unique. Git push normal (jamais --force), SHA de base vérifié. Aucun droit admin / secret manager / écriture aux données SOURCE.

## Activation externe indispensable

Le workflow est installé mais ne doit pas être déclaré agent IA actif avant : GitHub Settings > Secrets and variables > Actions.
- Secret : ANTHROPIC_API_KEY, détenue par le propriétaire du compte fournisseur, jamais commitée.
- Variable : ANTHROPIC_MODEL, identifiant d'un modèle Claude encore disponible auprès du fournisseur.
- Variable : FD_AUTONOMY_ENABLED = true, activation explicite après validation et acceptation de la consommation API.
Le scheduler fonctionne toutes les quinze minutes et une continuation est demandée explicitement après publication. GitHub peut retarder les runs de schedule. Les permissions réelles du token doivent permettre à l'agent de pousser sur main selon les règles du dépôt.

Les modèles GitHub Models ne sont pas une solution de repli (service retiré en juillet 2026) ; ni Codex ni Copilot ne sont utilisés.

## Definition of Done à vérifier

Tests unitaires verts, audits P1 verts, génération réelle validée, publication effective sur main, conclusion du run GitHub SUCCESS, état DONE avec preuve, second travail sélectionné automatiquement ; absence de mutation SOURCE comparée à la baseline. Tant qu'une des étapes manque, le statut global est PARTIAL / NOT_RUNTIME_ATTESTED.

## Addendum D036 — Activation du bootstrap sans clé fournisseur

Les deux blueprints initialement admissibles possèdent désormais un exécuteur déterministe versionné factory/templates.py. Ils peuvent être codés automatiquement sans fournisseur IA externe ; leurs tests sont exécutés dans un job séparé de publication. Pour ces deux travaux, ANTHROPIC_API_KEY et ANTHROPIC_MODEL sont facultatifs. Ils demeurent nécessaires pour les nouveaux blueprints sans template. Le workflow se déclenche également lors d'un push sur factory/ ou sur son propre YAML. L'absence de la variable FD_AUTONOMY_ENABLED n'empêche pas le bootstrap ; définir explicitement FD_AUTONOMY_ENABLED=false désactive le job de génération. Le mandat D035 sur la sécurité, les preuves et le contrôle de publication reste inchangé. La réussite réelle en GitHub Actions doit être vérifiée à chaque étape : ne pas déduire DONE de ce texte.

## Preuves runtime établies — 2026-11-06

Manifest checker : run 42283853272, verdict success, GitHub commit ddd6e4dc4116d1163d0cd6269b6c71cc2f11083e, puis status DONE via commit de réconciliation. Hash checker : run 42283964239, verdict success, puis status DONE via commit de réconciliation. Run autonome suivant 42284071869 SUCCESS sans candidat supplémentaire. Ces observations attestent une chaîne réelle de code pour les travaux gouvernés du bootstrap, pas la complétude des données financières P1. Comparaison SOURCE historique : 114 blobs inventory/ inchangés depuis 562dd759. Les nouvelles générations hors templates exigent le secret fournisseur et une qualification explicite en blueprint. En cas d'échec génération/validation, trois tentatives maximales distinctes sont permises ; la troisième bloque la tâche avec preuve par run. Le point d'arrêt réel est le registre factory/state.json, pas une affirmation textuelle.

## Cartographie des agents/UTL — D038

Le registre unique contient cinq identités de rôles fonctionnels : github-actions:planner (sélection), github-actions:coder (génération), github-actions:validator (tests sans secret), github-actions:publisher (écriture bornée sur main), github-actions:reconciler (vérification du run et déverrouillage). Pour chaque UTL autonome effectivement exécutée, agent_id et run_id relient le résultat au job. Le groupe de concurrence GitHub protège l'écriture entre runs ; le SHA attendu protège les changements concurrents par d'autres acteurs. Cette organisation rend la coordination multi-rôles vérifiable sans inventer une seconde autorité.

## Entrée universelle de session — FD-AGENT-ARRIVAL-V1

Le point d'accès opérationnel de toute conversation autorisée est `factory/ARRIVAL.md` ; le diagnostic exécutable associé est `python -m factory.entry --role coder --agent <identifiant-de-session>`. Cette commande est sans mutation et inspecte la continuité, les programmes, le backlog, les tâches READY, les preuves et les éventuels runs en attente. Elle ne remplace ni l'authentification GitHub, ni le moteur `factory/engine.py`, ni l'attestation du workflow. Si les deux premiers blueprints sont DONE et qu'aucune tâche READY ne demeure, la prochaine action est une **qualification documentée** du travail P1 restant, pas une réexécution ni une clôture fictive des phases métiers.

## Attestation FD-AGENT-ARRIVAL-V1

Le run GitHub 42288354186 (commit testé 9f25e95657f533afa1a49c6930fb81d5aa39f396) confirme 21 tests factory, 6 tests métier et la commande d'arrivée réelle sur le dépôt. Verdict : PROGRAM_QUALIFICATION_REQUIRED. Le run du moteur hébergé 42288354189 est SUCCESS, sans nouveau travail admissible. L'entrée universelle est donc exécutable et contrôlée ; l'auto-fabrication générale de nouveaux blueprints n'est pas attestée. La prochaine intervention porte sur la qualification gouvernée d'un travail P1 fondé sur sources réelles, sans expansion des permissions de publication.

## Tranche D040 — Qualification des programmes et fournisseur de code

Le mécanisme `factory/program_factory.py` ajoute une étape au cycle existant **uniquement lorsqu'aucune tâche déjà READY ou run en attente ne doit passer en priorité**. Il qualifie des tâches P1 à partir de la roadmap, du TODO et des CSV SOURCE, crée des blueprints versionnés dans `factory/blueprints.json`, enregistre une preuve `factory/evidence/program-qualification.json` et s'appuie sur `factory/tasking.py` pour étendre le même registre `factory/state.json`. Les dépendances et empreintes SRC sont vérifiées avant admission et avant sélection. Deux travaux de diagnostics en lecture seule sont d'abord ciblés : couverture des documents par émetteur, puis complétude des périodes économiques ; ils ne clôturent pas les tâches de collecte documentaire P1. L'adaptateur Anthropic `factory/provider.py` isole la configuration et les appels au modèle pour des tâches non couvertes par les modèles déterministes. L'activation fournisseur doit rester distincte d'un simple commit. Référence opérationnelle : `factory/PROGRAM_FACTORY.md`. Ne pas commencer le kit de portabilité avant d'attester cette tranche.

## Point de reprise attesté après D040

Le cycle automatique PROGRAMME → QUALIFICATION → CODE → VALIDATION → PUBLICATION → ATTESTATION a produit deux nouvelles tâches P1 `DONE` : `FD-AUTO-P1-COVERAGE-DIAGNOSTIC` (run 42292518351, commit d354abff06e7293046b6db445b5798160424813a), puis `FD-AUTO-P1-TEMPORAL-DIAGNOSTIC` (run 42292599195, commit 7c33ea9b92ebc158a1cc09b4fdd3b3d535646b9e). Run de continuation 42292684545 SUCCESS. Dernière attestation de tâche : 42292599195 ; état `NO_ADMISSIBLE_AUTONOMOUS_TASK`. Les deux échecs de tests précédents demeurent dans les preuves ; CI corrective 42292518247 SUCCESS. Les 114 blobs SOURCE inventory/ de la baseline 562dd759 restent inchangés. Environnement du modèle Claude : `CONFIGURATION_REQUIRED` (aucune clé/modèle présent dans les logs du job de génération 42292599195). Le prochain agent ne doit pas revendiquer d'appel modèle réel ni d'achèvement du P1 métier sans preuves. Il doit continuer l'admission de nouveaux travaux sûrs et le raccordement des sources extérieures lorsque disponibles. Kit autres dépôts : **reporté**, comme demandé.
## D041 — Dualité des voies d'exécution, agent-first sans API

Référence historique vérifiée : PR #95 `Patricked-code/MCP`, `CLAUDE.md` §9.8 `bootstrapCandidateConnection()`/`dispatchCandidateWork()`, et `PROGRAM_AUTO_CONTINUE` de son `CLAUDE.md` actuel. Le mécanisme recherché est documentaire : un agent ChatGPT/Claude disposant déjà de sa capacité de codage se connecte à GitHub, lit les directives `.md`, reprend le travail admissible, réalise des changements et valide sans nécessiter une clé API Anthropic *ajoutée au dépôt*. Le modèle est déjà fourni par le client agent.

**FinancialData conserve son architecture propre :** `factory/state.json` est la projection unique, `factory/entry.py` est une admission/observation sans écriture, `factory/program_factory.py` qualifie les travaux, `tasking.py` sélectionne, et les fichiers `.md` pilotent la continuité d'un agent connecté. Le workflow de génération modèle externe reste une voie **optionnelle** pour du codage non templatisé réellement exécuté par GitHub Actions hors conversation ; l'absence `ANTHROPIC_API_KEY` ne bloque pas la voie agent connecté. Ne pas mettre une condition API dans les gates du programme ou les instructions d'entrée. Ne pas importer les tasks/sessions/locks MCP ni sa gouvernance branches/PR.

**Distinguer la méthode de l'autonomie d'exécution :** `FD_AGENT_AUTO_CONTINUE` implique un agent actif et autorisé ; le travail entre conversations est conservé par les documents et états GitHub. La conversation n'est pas un worker 24/7. Un workflow GitHub Actions ne devient pas automatiquement un agent codeur non templatisé par la simple présence d'instructions Markdown.

## D042 — Précédence de la mémoire historique sur la mémoire opérationnelle

**Ordre avant chaque session, sans exception :** les onze références canoniques sous `README.md` de `GOVERNANCE.md` à `docs/ISSUER_DISCOVERY_MATRIX.md` sont lues en premier. Ensuite seulement `ROADMAP.md`, `factory/CONTINUITY.md`, `factory/HANDOFF.json`, `factory/state.json`, `factory/blueprints.json` et les preuves GitHub. Le diagnostic `factory.entry` expose maintenant cette séquence et un second groupe de documents opérationnels ; le test `factory/tests/test_canonical_docs.py` empêche leur inversion documentaire en CI. Les règles historiques restent intactes dans leur rôle ; seule leur formulation de séquence d'arrivée a été harmonisée.

Le contrôle différentiel officiel `562dd759f768587bc263731a1ea23318dbe4b294...6264f186d7ef6d3d6e525c36aae83466a218628a` a confirmé 0 suppression sur 30 commits et 0 modification de `inventory/`. Les correctifs de séquence postérieurs n'annulent ni les anciennes décisions ni les tâches déjà attestées. Prochain jalon de programme après validation CI : construire/qualifier une nouvelle tâche P1 à partir d'une preuve SOURCE existante, en priorisant la réconciliation documentaire et les critères de collecte BRVM V2. Rester `BLOCKED` sur tout PDF/Drive absent.

## D043 — L'usine n'est pas une deuxième chaîne de développement métier

Mandat propriétaire : préserver et faire évoluer le projet existant, pas créer une structure concurrente. `ROADMAP.md` + `ARCHITECTURE.md` gouvernent les programmes et couches financières. `factory/engine.py`, `tasking.py`, `program_factory.py`, `coder.py`, `publisher.py` et les workflows sont des **outils transversaux du même projet**, soumis aux onze documents canoniques et à la politique main-only. L'ancrage nouvellement ajouté `process_anchor` relie une tâche technique à sa sous-phase métier P1-B ou P1-D ; il ne change ni le statut de la tâche métier d'origine ni les tâches déjà attestées. Blocages locaux source/permission et contrôles de dépendances obligatoires. Prochain jalon : extension incrémentale des capacités utiles aux tâches P1 encore ouvertes, puis vérification CI et preuve SOURCE. Kit de portabilité hors scope.
