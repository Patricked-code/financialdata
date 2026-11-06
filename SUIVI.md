# SUIVI — financialdata

Dernière mise à jour : 2026-08-20

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`. Git : `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

- sociétés : **48 / 48** ;
- état live courant : **V22 = 3 137 PDF** ;
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v22_20260819.md` ;
- index : `inventory/p1_issuer_manifest.csv`.

V22 provient de NTLC : snapshot **81** → live strict parent-scoped **85**, delta **+4**, persisté avant SHA. V21 provenait d'ETIT : 81 → 100 (+19), également versionné avant SHA.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- maître : `inventory/p1_document_manifest.csv` ;
- consolidé : **14 / 3 137** à ce stade ;
- les corpus hashés disposent de Drive IDs + tailles + SHA dans `inventory/hashes/*.csv` ;
- backfill temporel/shards toujours requis.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **1 715 / 3 137 = 54,67 %** ;
- restant non hashé : **1 422 PDF** ;
- groupes exacts prouvés : **16**.

### NTLC — V22 terminé

- snapshot **81** → live strict **85**, delta **+4** ;
- cardinal live prouvé par deux sous-périmètres disjoints : `33 + 52 = 85` ;
- **85/85 PDF** matérialisés et signatures `%PDF-` valides ;
- **85 SHA uniques**, **0 groupe exact** ;
- registre `inventory/hashes/NTLC.csv` ;
- sérialisation LF canonique, 14 239 octets ;
- blob local/GitHub validé bit-for-bit : `90cd7791f2a57754ba3a21f873c8f1a18b543cf2` ;
- une première écriture textuelle divergente a été détectée par le garde-fou blob et remplacée avant toute déclaration de complétude ;
- 2024 EF plain / `_rev` : même période 31.12.2024 et mêmes principaux chiffres, mais pagination/représentation différentes (Excel 4 pages vs PDFium/DocuSign 1 page) ; famille de version/représentation conservatrice, aucun `SUPERSEDES` ;
- 2023 EF plain / `_2` : même exercice, formats/contenus comparatifs distincts, deux objets SOURCE conservés ; aucun `SUPERSEDES`.

ETIT reste terminé **100/100** avec registre blob-validé `908ac3c78239e14204ea21849775ed2eb75eb292`.

BNBC reste terminé **92/92** avec 92 SHA uniques et registre blob-validé `fb567fcdbf57af2aa6bb017544d2c29583e8359f`.

TRITRAF reste réconcilié **8/8** avec registre issuer-level blob-validé `c7a9c31558d4a9de5a1bea532d0cc4a2580876e6`, sans double comptage.

### Doublons exacts

Les **16 groupes exacts** prouvés restent tous conservés dans `inventory/p1_duplicate_groups.csv`. NTLC n'ajoute aucun groupe. Aucun objet SOURCE n'est supprimé ou fusionné physiquement.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. revalider le corpus Drive **CFAC** strictement par ses dossiers SOURCE réels ;
2. comparer le live au snapshot manifeste **94** ;
3. si delta, créer le checkpoint V23 avant SHA et corriger le dénominateur ;
4. matérialiser 100 % du périmètre CFAC live ;
5. valider signatures/tailles, SHA-256, doublons exacts et familles de version justifiées ;
6. créer puis blob-valider `inventory/hashes/CFAC.csv` ;
7. finaliser CFAC, manifeste, `SUIVI.md` et `TODO.md`, puis poursuivre le corpus réellement non hashé suivant.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3137 | MASTER_CONSOLIDATED=14/3137 | SHA256_VERIFIED=1715/3137 | SHA_COVERAGE=54.67% | UNHASHED=1422 | EXACT_DUPLICATE_GROUPS=16 | NTLC=85/85_SHA_COMPLETE | NTLC_REGISTRY_BLOB=90cd7791f2a57754ba3a21f873c8f1a18b543cf2 | NEXT=CFAC_LIVE_RECHECK_AND_SHA`

## Addendum contrôlé — 2026-11-06 — Source V23 et usine locale

La première partie de ce fichier reste le checkpoint historique du 2026-08-20 (V22) et n'est pas effacée. Les preuves GitHub plus récentes indiquent le checkpoint SOURCE V23 : **3 157 PDF** au total, dont **114 CFAC** après un delta de +20. Le commit `562dd759f768587bc263731a1ea23318dbe4b294` ajoute `inventory/hashes/CFAC.csv` contenant 114 lignes SHA-256 renseignées, 111 empreintes distinctes et 3 paires de doublons binaires. Le registre maître de documents reste à compléter. Les totaux SHA globaux V23 ne sont pas attestés par une réconciliation globale finale ; ne pas remplacer ce manque par un calcul supposé.

Développement : ajout d'une usine de tâches/projets indépendante du MCP sous `factory/` (code, contrôles, tests, protocole agent et workflow CI read-only). Les vérifications automatiques d'inventaire sont implémentées ; l'agent codeur autonome hébergé et l'écriture automatique de code ne sont pas encore opérationnels. Point de reprise : terminer la cohérence des manifests P1, réconcilier TODO/SUIVI avec les preuves V23, puis continuer P1 sans redémarrage de l'architecture.

## Point de reprise FD-AUTONOMY-V1 — 2026-11-06

Mandat canonique : [factory/CONTINUITY.md](factory/CONTINUITY.md). Projection machine : factory/state.json. Passage aux UTL PLAN/CODE/VALIDATE/PUBLISH/ATTEST et mise en place du workflow hébergé d'orchestration avec génération IA via Claude (clé fournie séparément par le propriétaire), validation isolée sans secrets, publication main gouvernée et contrôle différé du run GitHub. Le workflow de validation indépendant est renforcé (SHA déclencheur, tests, audit et artefacts). Le mécanisme doit rester indépendant du MCP. Les deux premières tâches autonomes, non destructives et dépendantes sont FD-AUTO-P1-MANIFEST-CHECKER puis FD-AUTO-P1-HASH-CHECKER. Point de preuve : consulter les runs Actions et le statut factory/state.json ; aucune réussite du codage IA ne peut être inférée tant que l'activation et les vérifications de bout en bout ne sont pas attestées. Les travaux P1 existants et les sources V23 ne sont ni supprimés ni remplacés.

### Complément de reprise D036

Le bootstrap P1 est désormais raccordé à un codeur déterministe pour les deux premiers travaux d'ingénierie (validation des manifestes et contrôle SHA-256), et le déclenchement push du workflow est ajouté. Les six tests métier des templates ont passé une vérification locale avant publication. La preuve qui détermine l'avancement final reste le run de GitHub Actions, son éventuel commit de code, puis la réconciliation dans factory/state.json. La clé d'un fournisseur IA externe demeure nécessaire pour les futures tâches sans template ; cela ne doit pas être confondu avec l'activation des deux premières tâches.

## Attestation de l'usine autonome — 2026-11-06

**Continuity ID** : FD-AUTONOMY-V1. Preuves GitHub réelles :
- FD-AUTO-P1-MANIFEST-CHECKER — génération, validation, commit ddd6e4dc4116d1163d0cd6269b6c71cc2f11083e, run GitHub 42283853272 SUCCESS, réconciliation et statut DONE.
- FD-AUTO-P1-HASH-CHECKER — génération, validation et publication, run GitHub 42283964239 SUCCESS, réconciliation et statut DONE.
- Le run de continuation 42284071869 SUCCESS a confirmé l'absence d'une troisième tâche automatique qualifiée. Cela ne clôt pas les travaux SOURCE métier restants de P1 ; ils restent dans TODO.md, hors exécution aveugle.
- Le diff vérifié depuis la baseline initiale 562dd759 ne montre aucune modification des 114 fichiers inventory/ SOURCE suivis.
- La validation initiale de l'usine a réussi dans le run 42282675969 et la validation du bootstrap dans 42283853241.

**Prochain point de reprise** : consulter factory/state.json pour les statuts, les unités, les preuves, la continuité et les dépendances ; puis élargir les blueprints sûrs à partir de TODO/ROADMAP et configurer ANTHROPIC_API_KEY/ANTHROPIC_MODEL pour des travaux de code non déterministes. Une tâche nécessitant des octets PDF/Drive ne peut pas être déclarée finie sans la source réelle. Le raccordement au MCP reste reporté et indépendant.

### Continuité multi-rôles D038

Les identités des cinq jobs sont désormais projetées dans state.json et affectées aux unités d'exécution autonomes attestées. Une tâche historique sans preuve de run conserve son absence de provenance opérationnelle. Le nombre de travaux admissibles après le bootstrap attesté reste nul ; le système continue à surveiller les nouvelles tâches approuvées dans factory/blueprints.json et à reprendre via GitHub Actions. Ne pas confondre le moteur local avec celui du MCP, qui reste hors du périmètre de cette mise en œuvre.

### Entrée d'un nouvel agent codeur — 2026-11-06

L'instruction de connexion depuis une autre conversation est traitée par `factory/ARRIVAL.md` (`FD-AGENT-ARRIVAL-V1`) et, lorsqu'un terminal autorisé existe, `python -m factory.entry --role coder --agent agent-session`. Le connecteur GitHub sans terminal doit effectuer les mêmes vérifications en lecture seule. État constaté avant ce raccordement : `main` = `2d963bd1ed8c3b0645697823f31326e94d0c4855`, continuité `FD-AUTONOMY-V1`, dernière attestation 42283964239, deux blueprints DONE, aucun travail autonome encore READY. Après raccordement, consulter les **SHA/runs actuels**, qui prévalent sur ce constat historique. Suite admissible : qualifier une tâche métier P1 effectivement justifiée, sans remplacer la fabrique existante.

## Preuve d'entrée universelle — GitHub Actions 2026-11-06

L'arrivée conversationnelle `FD-AGENT-ARRIVAL-V1` est attestée en exécution CI réelle : run [42288354186](https://github.com/Patricked-code/financialdata/actions/runs/42288354186), SHA testé `9f25e95657f533afa1a49c6930fb81d5aa39f396`, résultat SUCCESS. Logs : **21 tests de la fabrique OK**, **6 tests métier OK**, diagnostic réel `Arrival: PROGRAM_QUALIFICATION_REQUIRED`. La continuation hébergée associée [42288354189](https://github.com/Patricked-code/financialdata/actions/runs/42288354189) s'est terminée SUCCESS sans nouvelle tâche READY. L'instruction « connecte-toi en tant qu'agent codeur » renvoie à `factory/ARRIVAL.md` ; l'agent doit vérifier son compte GitHub, son SHA et les preuves live, puis préparer le prochain blueprint P1 admissible. Ce diagnostic est en lecture seule et n'accorde pas de permission d'écriture.

## FD-AUTONOMY-V1 — Fabrique automatique de travaux P1 — 2026-11-06

À partir de la continuité validée au commit `9c936bf8aa098ae440d1781717748d764b5cc963`, la tranche suivante raccorde `factory/program_factory.py` au cycle existant : analyse de ROADMAP/TODO, vérification de fichiers SOURCE réels, calcul d'empreintes, qualification bornée et création de deux blueprints d'ingénierie non destructifs. La sélection des tâches refuse une preuve modifiée depuis l'admission. Le modèle Claude est raccordé dans `factory/provider.py` sans créer de secret ; la disponibilité réelle du fournisseur n'est pas attestée tant que la configuration GitHub Actions et un appel réussi ne sont pas observés. Les travaux P1 impliquant des sources externes restent ouverts. Voir `factory/PROGRAM_FACTORY.md` pour la règle de qualification et les résultats à vérifier sur GitHub Actions. Aucun changement de gouvernance main-only ni de l'architecture financière.

## FD-AUTONOMY-V1 — Attestation de la qualification automatique P1 — 2026-11-06

La qualification automatique de programme est effectivement en service : après lecture de ROADMAP/TODO et des empreintes des manifests, le run 42292036556 a créé un commit de qualification `b007797ea0e6336bb757011e257897a31fb166be`, ajoutant deux blueprints P1 bornés. Deux échecs de non-régression ont été observés et **conservés** (runs 42292036556 et 42292320826) : contrôle de la provenance TODO courante et fixture de tests supposant le catalogue statique. Les corrections ont été validées par la CI 42292518247 : 31 tests factory et 6 tests métier SUCCESS.

Le cycle autonome a ensuite réalisé :
- `FD-AUTO-P1-COVERAGE-DIAGNOSTIC` : code publié dans `d354abff06e7293046b6db445b5798160424813a`, run 42292518351 SUCCESS, statut et UTL `DONE` attestés.
- `FD-AUTO-P1-TEMPORAL-DIAGNOSTIC` : code publié dans `7c33ea9b92ebc158a1cc09b4fdd3b3d535646b9e`, run 42292599195 SUCCESS, statut et UTL `DONE` attestés.
- Continuation 42292684545 SUCCESS, avec absence de troisième tâche READY ; curseur canonique `NO_ADMISSIBLE_AUTONOMOUS_TASK`.

Comparaison directe de l'arbre Git avec la baseline `562dd759f768587bc263731a1ea23318dbe4b294` : **114 fichiers inventory/ SOURCE comparés et zéro modifié**. La création de diagnostics ne signifie pas que les quelque 3 157 PDF ont été collectés ou que l'inventaire documentaire est exhaustivement consolidé.

Le fournisseur Anthropic est raccordé techniquement via `factory/provider.py`, mais le run 42292599195 atteste `CONFIGURATION_REQUIRED` : `ANTHROPIC_API_KEY` et `ANTHROPIC_MODEL` absents de son environnement GitHub Actions. Aucun appel modèle réel n'a donc été attesté. Prochaine action : configurer ces paramètres dans les Secrets/Variables Actions, ajouter et qualifier des travaux P1 techniquement admissibles nécessitant un vrai modèle, puis confirmer leur première exécution CI de bout en bout. Les tâches nécessitant PDF/Drive/BRVM externes restent en attente de sources vérifiables.
