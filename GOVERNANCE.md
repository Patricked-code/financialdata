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
2. `CLAUDE.md`
3. `SUIVI.md`
4. `DECISIONS.md`
5. `TODO.md`
6. `ARCHITECTURE.md`
7. `DATA_MODEL.md`
8. `SOURCES.md`
9. les documents pertinents sous `docs/`

Si une règle du projet évolue, la mémoire persistante doit être mise à jour dans le même travail.

## 3. Hiérarchie des vérités

Ordre de priorité pour les données :

1. document/fichier source original ;
2. métadonnées documentaires et provenance ;
3. extraction RAW fidèle ;
4. mapping sémantique validé ;
5. couche canonique ;
6. données dérivées ;
7. analytics.

Une couche aval ne doit jamais écraser la vérité d'une couche amont.

## 4. Principe RAW

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

## 5. Interdictions de données

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

## 6. Données publiées vs calculées

`fact_origin` doit séparer au minimum :

- `PUBLISHED` : valeur explicitement publiée ;
- `DERIVED` : valeur calculée/reconstruite ultérieurement.

Un ROE, PER, rendement, variation ou autre ratio publié reste `PUBLISHED`. Le même ratio recalculé par le système est une observation différente dans `DERIVED`.

## 7. Périodes

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

## 8. Versions et doublons

Toute source doit pouvoir être identifiée par hash.

- les doublons binaires restent référencés ;
- les fichiers `_rev`, corrigés ou remplacés sont historisés ;
- un restatement n'efface pas la version précédente ;
- une correction d'extraction crée une nouvelle version/supersession au lieu d'une mutation silencieuse.

## 9. Couverture sectorielle

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

## 10. Changement du modèle

Aucune nouvelle table, colonne ou règle de mapping ne doit être ajoutée uniquement par intuition.

Procédure :

`OBSERVATION SOURCE → DOCUMENTATION → DÉCISION → IMPLÉMENTATION → VALIDATION`

Toute nouvelle particularité conceptuelle est d'abord consignée dans `DECISIONS.md` ou dans un document de gouvernance dédié sous `docs/`.

## 11. Sécurité et non-régression

- Ne jamais stocker de secret ou mot de passe dans le dépôt.
- Ne jamais supprimer une source ou une donnée sans preuve et décision documentée.
- Les migrations doivent préserver l'historique et la traçabilité.
- Toute transformation doit être reproductible.
- Toute extraction automatisée doit produire des logs/rapports de contrôle.

## 12. Definition of Done documentaire

Une étape n'est terminée que si :

- le travail réel a été vérifié ;
- les sources sont citées ;
- les ambiguïtés sont signalées ;
- `SUIVI.md` reflète l'état réel ;
- les décisions nouvelles sont dans `DECISIONS.md` ;
- `TODO.md` reflète le reste à faire ;
- aucune branche n'a été créée.
