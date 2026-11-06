# FD-AUTONOMY-V1 — Qualification automatique P1 et raccordement modèle

## Mandat et responsabilité unique

Cette extension **ne crée pas d'orchestrateur parallèle**. Le seul registre d'exécution demeure `factory/state.json`, projet/programmes/tâches issus de `ROADMAP.md` et `TODO.md`. Le moteur `factory/engine.py` est préservé ; `factory/program_factory.py` est un adaptateur de qualification, comme `tasking.py`, `coder.py`, `provider.py` et `publisher.py`.

L'objectif de la présente version est : **PROGRAMME P1 → SOURCES ATTESTÉES → BLUEPRINTS BORNÉS → UTL → CODE → TESTS → CI → PUBLICATION → ATTESTATION → TÂCHE SUIVANTE**.

## 1. Admission et preuves des tâches

La qualification commence après la réconciliation du run CI antérieur, uniquement si aucune tâche autonome déjà admissible ne doit être exécutée.

Pour chaque règle de programme :
1. Lire l'état actuel de `ROADMAP.md`, `TODO.md` et `factory/state.json`.
2. Exiger une unique tâche historique `BACKLOG` correspondante à P1 ; enregistrer son identifiant parent.
3. Valider l'existence et les en-têtes minimaux des manifestes SOURCE du programme.
4. Enregistrer le nombre de lignes observées et la véritable empreinte SHA-256 de chaque fichier source consulté.
5. Vérifier que les dépendances appartiennent à la base de tâches et que les chemins autorisés se limitent à `src/financialdata/` et `tests/`.
6. Créer additivement les blueprints `READ_ONLY_ENGINEERING` versionnés ; garder les travaux métiers P1 originaux ouverts.
7. Projeter les tâches dans **le registre existant**, puis lancer les UTL selon l'ordre des dépendances.
8. Empêcher l'exécution si un fichier probant a changé depuis sa qualification.

La décision est consignée dans `factory/evidence/program-qualification.json`, avec les chemins et les empreintes vérifiés. Les workflows et les commits GitHub demeurent les sources de preuve de publication.

**Les deux premières règles prédéfinies, dont le code et les tests ont été revus, sont :**

- `FD-AUTO-P1-COVERAGE-DIAGNOSTIC` : comparaison non destructive des documents inscrits par émetteur avec le manifeste documentaire réellement présent, et exposition de la couverture incomplète.
- `FD-AUTO-P1-TEMPORAL-DIAGNOSTIC` : signalement des périodes économiques absentes, invalides ou contradictoires ; aucune interprétation du nom de fichier comme source économique.

Elles sont des **tâches d'ingénierie utiles**, pas la réalisation de l'inventaire exhaustif ni une collecte réelle de documents manquants. Les blueprints ne déclarent jamais les tâches métier P1 parentes terminées.

## 2. Travaux non admissibles sans preuves externes

La consultation en direct de BRVM, la récupération/validation des octets PDF, la synchronisation Drive, les révisions/relations SUPERSEDES et le remplissage définitif des périodes exigent des éléments de source supplémentaires. `program_factory.assessment()` les identifie avec des raisons explicites plutôt que produire une preuve fictive.

Cette version **ne génère pas arbitrairement un exécutable depuis toute ligne TODO** : seules les règles allowlistées, testées et en lecture seule sont promues sans humain. D'autres règles pourront être ajoutées à ce même moteur, avec tests, types de sources et limites attestés.

## 3. Intégration du véritable fournisseur de codage

La route de génération existante `factory/coder.py` délègue désormais à `factory/provider.py` les tâches sans template déterministe. Ce dernier parle à l'API Messages Anthropic et rejette :
- absence de secret `ANTHROPIC_API_KEY` ou de variable `ANTHROPIC_MODEL` ;
- fournisseur ou modèle non reconnu ;
- appel HTTP échoué ou réponse trop volumineuse ;
- `stop_reason` autre que `end_turn` ;
- sortie qui n'est pas un objet JSON strict avec un tableau `files`.

La proposition reçue reste ensuite soumise au validateur `factory/coder.py` : syntaxe Python, chemins bornés, primitives interdites, tests obligatoires, empreinte d'artefact et SHA de base.

L'adaptateur est **implémenté et testable sans secret via mocks**, mais une requête réelle n'est attestée que lorsqu'un secret et un modèle disponibles ont été configurés et qu'un run GitHub a produit une réponse validée. Aucun identifiant fournisseur n'est enregistré dans le dépôt.

Paramètres GitHub Actions :
- Secret `ANTHROPIC_API_KEY` (personnel, jamais commité).
- Variable `ANTHROPIC_MODEL` (modèle Claude réellement activé pour le compte API).
- Facultatif `FD_AUTONOMY_ENABLED=false` pour suspendre le générateur.

Pour diagnostiquer le raccordement sans afficher le secret, exécuter `python -m factory.provider status` depuis le job de génération, où les variables sont effectivement injectées. Cette commande ne garantit pas que le compte dispose de crédits ni qu'une requête modèle réussira.

## 4. Workflow hébergé et continuité

Le job `reconcile` exécute désormais, dans cet ordre :
1. Réconciliation des attestations GitHub en attente.
2. Recherche de tâches READY existantes.
3. Si aucune tâche n'est READY, qualification des règles P1 applicables et création des blueprints autorisés et de leurs preuves.
4. Publication atomique de `factory/blueprints.json`, `factory/state.json` et `factory/evidence/program-qualification.json` lorsque la qualification produit réellement un changement.
5. Génération du code déterministe ou via le modèle, validation dans un job sans secrets, publication gouvernée sur `main` et reprise après l'attestation.

Le workflow réutilise le groupe GitHub Actions de concurrence et les contrôles d'empreintes Git ; aucun nouveau système de planification n'est créé.

## 5. Preuves et jalons à vérifier

- Tests `python -m unittest discover -s factory/tests -v` et `python -m unittest discover -s tests -v`.
- Diagnostics `python -m factory.program_factory` (lecture seule) et `python -m factory.provider status` (lecture seule).
- Premier run automatique contenant un événement `PROGRAM_TASK_QUALIFIED` et les deux nouveaux blueprints.
- Les nouveaux commits de code et leurs résultats `SUCCESS`, puis deux tâches `DONE` attestées avec références CI.
- Absence de modifications des fichiers d'inventaire SOURCE de référence et de perte des décisions, des programmes ou des tâches historiques.

Le point de reprise officiel reste `factory/CONTINUITY.md` et `factory/state.json`. Les opérations futures de déploiement d'applications, d'autres dépôts ou du MCP ne sont pas incluses.
