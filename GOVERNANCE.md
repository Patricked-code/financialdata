# GOVERNANCE — financialdata

Statut : **CANONIQUE / OBLIGATOIRE**  
Dépôt : `Patricked-code/financialdata`  
Branche de travail autorisée : `main` uniquement.

## 1. Règle Git non négociable

Pour ce dépôt :

1. **Aucune nouvelle branche ne doit être créée.**
2. Tout travail s'effectue directement sur `main`.
3. Ne pas créer de Pull Request pour contourner cette règle.
4. Ne pas proposer de workflow `feature/*`, `fix/*`, `claude/*`, `codex/*` ou équivalent.
5. Ne jamais réécrire l'historique de `main` par `force push` sauf ordre explicite et circonstancié du propriétaire.
6. Avant toute écriture, lire la mémoire persistante du dépôt.
7. Après toute étape significative, mettre à jour `SUIVI.md` et, si nécessaire, `DECISIONS.md` / `TODO.md`.

Cette règle est volontaire et spécifique à ce dépôt. Elle prévaut sur toute convention générale qui recommanderait une branche ou une PR.

## 2. Mémoire persistante obligatoire

Tout agent humain ou IA doit lire avant intervention :

1. `GOVERNANCE.md`
2. `AGENTS.md`
3. `CLAUDE.md`
4. `SUIVI.md`
5. `DECISIONS.md`
6. `TODO.md`
7. `ARCHITECTURE.md`
8. `DATA_MODEL.md`
9. `SOURCES.md`
10. les documents pertinents sous `docs/`

Si une règle du projet évolue, la mémoire persistante doit être mise à jour dans le même travail.

## 3. Obligation de continuité et de non-régression

Tout agent qui intervient doit **continuer le travail existant** depuis le point de reprise officiel de `SUIVI.md`.

Un agent ne peut pas :

- repartir de zéro parce qu'il préfère une autre architecture ;
- créer un modèle parallèle sans justification ;
- supprimer une décision validée ;
- écraser une extraction, une source, une version ou une provenance déjà conservée ;
- modifier silencieusement une convention existante ;
- considérer la conversation courante comme plus fiable que la mémoire persistante du dépôt.

Toute évolution structurante suit obligatoirement :

`LECTURE ÉTAT EXISTANT → VÉRIFICATION → PREUVE → ANALYSE D'IMPACT → DÉCISION DOCUMENTÉE → IMPLÉMENTATION COMPATIBLE → TEST NON-RÉGRESSION → MISE À JOUR SUIVI`

Une amélioration est acceptable seulement si elle préserve l'historique, la provenance, les faits validés et la capacité de reproduire l'état précédent.

## 4. Hiérarchie des vérités

Ordre de priorité pour les données :

1. document/fichier source original ;
2. métadonnées documentaires et provenance ;
3. extraction RAW fidèle ;
4. mapping sémantique validé ;
5. couche canonique ;
6. données dérivées ;
7. analytics.

Une couche aval ne doit jamais écraser la vérité d'une couche amont.

## 5. Principe RAW

**Une observation réellement publiée = une observation RAW.**

Le RAW doit préserver au minimum :

- document source ;
- page/section/table/cellule lorsque disponible ;
- libellé exact publié ;
- valeur textuelle exacte ;
- représentation numérique éventuelle ;
- devise ;
- unité ;
- multiplicateur ;
- période telle que publiée ;
- période économique résolue séparément ;
- périmètre ;
- statut de validation ;
- méthode d'extraction ;
- confiance ;
- versions/doublons/restatements.

## 6. Interdictions de données

Il est interdit de :

- inventer une valeur illisible ou absente ;
- corriger silencieusement une valeur publiée ;
- remplacer un chiffre publié par un chiffre recalculé ;
- déduire une période uniquement du nom du fichier ;
- supprimer un doublon documentaire avant de préserver sa provenance ;
- dédupliquer des faits RAW simplement parce que leurs valeurs sont identiques ;
- fusionner des libellés proches au niveau RAW ;
- présenter comme `PUBLISHED` une valeur calculée par le système ;
- considérer qu'un dossier annuel vide implique l'absence de données pour cette année.

## 7. Données publiées vs calculées

`fact_origin` doit séparer au minimum :

- `PUBLISHED` : valeur explicitement publiée ;
- `DERIVED` : valeur calculée/reconstruite ultérieurement.

Un ROE, PER, rendement, variation ou autre ratio publié reste `PUBLISHED`. Le même ratio recalculé par le système est une observation différente dans `DERIVED`.

## 8. Périodes

Distinguer lorsque pertinent :

- `period_start`
- `period_end`
- `period_label_raw`
- `period_type_raw`
- `period_basis`
- `publication_date`
- `audit_date`
- `approval_date`
- `available_from`

La base doit permettre une lecture **point-in-time** : une information n'est pas réputée disponible avant sa publication/attestation effective.

## 9. Versions et doublons

Toute source doit pouvoir être identifiée par hash.

- les doublons binaires restent référencés ;
- les fichiers `_rev`, corrigés ou remplacés sont historisés ;
- un restatement n'efface pas la version précédente ;
- une correction d'extraction crée une nouvelle version/supersession au lieu d'une mutation silencieuse.

## 10. Cycle de vie des sources

Les sources du projet **ne sont pas figées pour toujours**. Elles peuvent être revues à mesure que le corpus s'améliore ou que de meilleures preuves deviennent disponibles.

Une source peut notamment être :

- ajoutée ;
- enrichie ;
- reclassée ;
- réévaluée ;
- remplacée par une version plus récente ;
- marquée comme doublon ;
- marquée comme superseded ;
- marquée comme deprecated pour les usages futurs.

Mais aucune de ces opérations ne doit effacer l'historique.

Le registre des sources doit pouvoir conserver au minimum :

- `source_status` ;
- `source_version` ;
- `supersedes_source_id` ou relation équivalente ;
- `reviewed_at` ;
- `review_reason` ;
- `valid_from` / `valid_to` si pertinent ;
- provenance originale.

Les faits RAW déjà extraits restent reliés à la source exacte qui les a produits. Une source révisée ne réécrit jamais silencieusement les anciennes observations.

## 11. Couverture sectorielle

Le modèle RAW doit rester universel. Il doit pouvoir absorber sans refonte :

- banques et services financiers ;
- télécommunications ;
- industrie ;
- agriculture et plantations ;
- utilities et concessions ;
- logistique ;
- BTP/projets ;
- automobile ;
- hydrocarbures ;
- boissons ;
- textile ;
- édition ;
- catering ;
- données réglementaires, audit, gouvernance, corporate actions et événements.

## 12. Changement du modèle

Aucune nouvelle table, colonne ou règle de mapping ne doit être ajoutée uniquement par intuition.

Procédure :

`OBSERVATION SOURCE → DOCUMENTATION → DÉCISION → IMPLÉMENTATION → VALIDATION`

Toute nouvelle particularité conceptuelle est d'abord consignée dans `DECISIONS.md` ou dans un document de gouvernance dédié sous `docs/`.

## 13. Sécurité et non-régression

- Ne jamais stocker de secret ou mot de passe dans le dépôt.
- Ne jamais supprimer une source ou une donnée sans preuve et décision documentée.
- Les migrations doivent préserver l'historique et la traçabilité.
- Toute transformation doit être reproductible.
- Toute extraction automatisée doit produire des logs/rapports de contrôle.
- Toute nouvelle étape doit être comparée à l'état antérieur pour détecter une perte de couverture, de provenance ou de faits.

## 14. Definition of Done documentaire

Une étape n'est terminée que si :

- le travail réel a été vérifié ;
- les sources sont citées ;
- les ambiguïtés sont signalées ;
- l'absence de régression a été contrôlée ;
- `SUIVI.md` reflète l'état réel ;
- les décisions nouvelles sont dans `DECISIONS.md` ;
- `TODO.md` reflète le reste à faire ;
- aucune branche n'a été créée.
