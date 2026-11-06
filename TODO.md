# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées ; état live **V22 = 3 137 PDF**.
- [x] checkpoint `inventory/P1_48_ISSUERS_CHECKPOINT_v22_20260819.md` ; index `inventory/p1_issuer_manifest.csv`.
- [x] ETIT : **81 → 100**, delta **+19**, versionné avant SHA (V21), puis SHA 100/100 terminé.
- [x] NTLC : **81 → 85**, delta **+4**, versionné avant SHA (V22), puis SHA 85/85 terminé.

### Document manifest

- [x] schéma/sharding/maître créés ; maître consolidé **14 / 3 137** à ce stade.
- [x] registres SHA avec Drive IDs + tailles disponibles pour les corpus hashés.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs jusqu'à consolidation complète du manifeste.

### SHA-256

- [x] NTLC **85/85**, 85 SHA uniques, 0 groupe exact.
- [x] NTLC registre `inventory/hashes/NTLC.csv` blob-validé : `90cd7791f2a57754ba3a21f873c8f1a18b543cf2`.
- [x] total SHA vérifiés : **1 715 / 3 137 = 54,67 %**.
- [x] restant non hashé : **1 422 PDF**.
- [x] groupes exacts globaux : **16**.
- [ ] CFAC : recheck live strict du snapshot **94**, puis SHA exhaustif du périmètre confirmé.

### Doublons / versions

- [x] seize groupes exacts documentés dans `inventory/p1_duplicate_groups.csv` ; NTLC n'en ajoute aucun.
- [x] NTLC 2024 EF plain / `_rev` : même période et mêmes principaux chiffres mais représentation/pagination différentes ; famille de version/représentation conservatrice, aucun `SUPERSEDES`.
- [x] NTLC 2023 EF plain / `_2` : même exercice, formats/contenus comparatifs distincts ; deux objets SOURCE conservés, aucun `SUPERSEDES`.
- [ ] aucune relation `SUPERSEDES` sans preuve explicite.

### Identité / périodes / qualité

- [x] règle : noms/dossiers/suffixes ne dictent jamais seuls période, scope, version ou doublon ; contenu et octets prévalent.
- [x] NTLC : périmètre live défini par 28 parent IDs réels 1998–2025 et non par ticker seul.
- [ ] périodes économiques fines pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`CFAC_LIVE_RECHECK_AND_SHA`, avec checkpoint préalable V23 si le live diffère du snapshot 94, puis validation blob et poursuite des corpus réellement non hashés.

## Addendum contrôlé — 2026-11-06

Les chiffres V22 plus haut décrivent une baseline antérieure. Le checkpoint V23 et le manifeste des émetteurs attestent **3 157 PDF SOURCE** après CFAC +20 ; le dernier commit a ajouté 114 SHA CFAC et 3 paires de doublons binaires. La couverture SHA globale finale et le maître documentaire demeurent à réconcilier, sans supprimer l'historique antérieur.

Usine locale : moteur de planification et suivi créé sous `factory/`, audits déterministes, contrôles non-régression, entrée agent et preuves. Travaux suivants : mécanisme distant de claims multi-runner, raccordement d'un agent codeur réellement exécutable (sans dépendance MCP), validation CI effective sur GitHub, puis enchaînement gouverné après code et validation. Ne jamais considérer ces travaux futurs comme déjà réalisés.

## Fil conducteur autonome FD-AUTONOMY-V1 — 2026-11-06

Les tâches historiques restent celles des sections précédentes et de factory/state.json. L'usine doit reprendre de façon déterministe dans cet ordre : attester les nouveaux tests GitHub CI ; vérifier la présence/autorisation du secret ANTHROPIC_API_KEY et des variables ANTHROPIC_MODEL et FD_AUTONOMY_ENABLED ; exécuter FD-AUTO-P1-MANIFEST-CHECKER, confirmer le run CI, puis FD-AUTO-P1-HASH-CHECKER ; élargir ensuite le registre des blueprints aux travaux P1 restants sans inventer ni transformer automatiquement les tâches non admissibles. Après interruption, lire factory/CONTINUITY.md, factory/HANDOFF.json et factory/state.json plutôt que repartir de zéro.

### Bootstrap autonome suivant D036

Première chaîne sans clé : exécuteur déterministe de FD-AUTO-P1-MANIFEST-CHECKER, puis FD-AUTO-P1-HASH-CHECKER, validation séparée, publication main, vérification CI, puis prochain travail. Pour d'autres tâches, une clé et un modèle Claude autorisés seront nécessaires. Consulter le journal et les runs GitHub avant d'inscrire une tâche terminée.

### Preuves de clôture technique et reste métier

Les deux tâches de bootstrap autonome FD-AUTO-P1-MANIFEST-CHECKER (run 42283853272) et FD-AUTO-P1-HASH-CHECKER (run 42283964239) ont été exécutées, testées, publiées et attestées DONE. Le run 42284071869 confirme la continuité automatique, sans troisième tâche actuellement admissible. Ne pas changer les cases des tâches P1 historiques sans preuve métier. Le reste de l'usine comprend l'extension du catalogue de blueprints approuvés, la configuration du fournisseur de modèles pour les tâches non templatisées, et l'attestation de nouvelles tâches réelles avant toute déclaration de couverture générale. Les essais d'échec de génération/validation sont bornés à trois avec statut BLOCKED et référence GitHub. Ne pas importer la gouvernance MCP.

### Prochaine progression programmatique FD-AGENT-ARRIVAL-V1

Entrée conversationnelle documentée dans `factory/ARRIVAL.md`, commande de diagnostic `factory/entry.py`, tests unitaires dédiés et référence de portabilité `factory/PORTABILITY.md`. Une nouvelle session disposant d'un accès GitHub doit vérifier l'identité du compte, l'état courant, les runs CI, puis qualifier une prochaine tâche P1 à partir des preuves réelles si le catalogue READY est vide. Ne pas lancer les étapes nécessitant un PDF externe ou une clé de modèle absente en prétendant à un résultat. La fabrique de qualification générale et les accès fournisseurs au-delà des deux templates restent à renforcer.
