# BRVM COLLECTOR V2 — Plan d'évolution sans régression

Date : 2026-08-09

Statut : `DESIGN_ONLY / NOT_IMPLEMENTED`

## 1. Rôle de la V1

Le script historique `telecharger_rapports_brvm.py` a servi à constituer le corpus initial par société et par année depuis les pages officielles BRVM.

La V1 doit être conservée comme **référence historique du processus de collecte**. Ne pas la modifier silencieusement ni utiliser une nouvelle implémentation pour réécrire l'ancien corpus.

## 2. Ce que la V1 fait correctement

- mapping explicite des 48 sociétés historiques ;
- parcours des pages BRVM de rapports par slug ;
- pagination ;
- récupération des liens PDF sous `/sites/default/files/` ;
- déduplication des URL pendant un run ;
- classement société/année ;
- normalisation partielle des noms ;
- retries de téléchargement ;
- non-retéléchargement d'un fichier local déjà présent et non vide.

## 3. Limites identifiées

### 3.1 Année/période déduite du nom de fichier

`determine_year()` utilise le nom du fichier et peut utiliser les quatre premiers chiffres comme approximation.

Conséquence : l'année de classement historique ne doit jamais devenir automatiquement la période économique canonique.

### 3.2 Pas de manifeste persistant

La V1 ne conserve pas, dans un registre structuré :

- URL source ;
- date de première découverte ;
- date de dernière observation ;
- hash SHA-256 ;
- ETag / Last-Modified lorsque disponibles ;
- statut de version ;
- lien de supersession ;
- statut de disparition du site ;
- résultat de validation PDF.

### 3.3 Un fichier local existant est automatiquement ignoré

La condition `exists && size > 0` ne permet pas de détecter qu'un PDF distant a été corrigé ou remplacé derrière la même URL / le même nom.

### 3.4 Les collisions de noms ne prouvent pas des doublons

Les suffixes `_2`, `_3`, etc. sont produits par collision de nom dans un run. Ils ne signifient pas nécessairement que les contenus sont identiques.

### 3.5 Mapping statique des sociétés

La liste historique contient 48 sociétés. La V2 devra être capable de détecter les nouveaux émetteurs, changements de dénomination, delistings ou nouveaux slugs sans perdre la correspondance historique.

### 3.6 Classification documentaire basée principalement sur le nom

La BRVM publie sur la page des libellés humains plus fiables que le seul nom du PDF. La V2 devra conserver le titre de publication BRVM et la catégorie affichée.

### 3.7 Sécurité et robustesse HTTP

La V1 désactive la vérification SSL. Une V2 devra utiliser la vérification TLS normale, retries/backoff contrôlés et journaliser les erreurs.

## 4. Observation de fraîcheur vérifiée le 2026-08-09

La page officielle BRVM de BOA Côte d'Ivoire publie actuellement au moins :

- `Rapport des Commissaires Aux Comptes et Etats Financiers annuels - Exercice 2025` ;
- `Rapport d'activités - 1er trimestre 2026`.

Le corpus Drive BOAC inventorié à ce stade possède un dossier 2025 mais pas de dossier 2026 ; le dossier 2025 contient T1/S1/T3 mais l'état financier 2025 n'y est pas encore présent dans l'inventaire Drive.

Conclusion : le collecteur futur doit fonctionner en **mode incrémental de rattrapage**.

## 5. Architecture recommandée V2

### 5.1 Séparer découverte et téléchargement

Pipeline :

`DISCOVER → COMPARE_MANIFEST → DOWNLOAD_DELTA → HASH → VALIDATE → VERSION_LINK → STORE → REPORT`

### 5.2 Manifeste source persistant

Créer un registre SQLite/JSONL/CSV machine-lisible contenant au minimum :

- `issuer_id`
- `ticker`
- `brvm_slug`
- `listing_page_url`
- `publication_title_raw`
- `document_category_raw`
- `remote_pdf_url`
- `remote_filename_raw`
- `publication_date_candidate`
- `classification_year_raw`
- `first_seen_at`
- `last_seen_at`
- `downloaded_at`
- `http_etag`
- `http_last_modified`
- `content_length`
- `sha256`
- `mime_type`
- `pdf_valid`
- `local_path`
- `source_status`
- `version_status`
- `supersedes_document_id`
- `duplicate_of_document_id`
- `issuer_assignment_status`

## 6. Algorithme incrémental

Pour chaque société :

1. charger la page officielle ;
2. suivre la pagination réelle ;
3. capturer titre de publication + URL PDF + contexte/catégorie ;
4. comparer chaque URL au manifeste ;
5. URL jamais vue → `NEW` → télécharger ;
6. URL déjà connue avec métadonnées inchangées → `UNCHANGED` → ne pas télécharger ;
7. même URL mais ETag/Last-Modified/taille différents → télécharger une nouvelle version ;
8. calculer SHA-256 après téléchargement ;
9. hash déjà connu ailleurs → `DUPLICATE` mais conserver la provenance ;
10. même URL et nouveau hash → `REVISED_AT_SAME_URL` ;
11. titre contenant `annule`, `remplace`, `corrige`, `révision` → `VERSION_REVIEW_REQUIRED`, jamais écraser ;
12. ancien document non retrouvé lors d'un run → ne pas supprimer ; mettre `NOT_SEEN_THIS_RUN` puis confirmer sur plusieurs runs avant toute conclusion ;
13. mettre à jour `last_seen_at` ;
14. produire un rapport de delta.

## 7. Modes de fonctionnement recommandés

- `--incremental` : mode normal, ne traite que le delta ;
- `--full-reconcile` : reparcourt tout le catalogue et compare au manifeste ;
- `--company BOAC` : cible un émetteur ;
- `--since YYYY-MM-DD` : limite l'analyse des publications récentes quand possible ;
- `--dry-run` : découvre et compare sans télécharger ;
- `--verify-existing` : hash/validation du corpus déjà présent ;
- `--latest` : vérification rapide des pages les plus récentes de tous les émetteurs.

## 8. Détection de l'univers des émetteurs

La V2 ne doit pas dépendre uniquement de la constante historique `COMPANIES`.

Conserver cette liste comme référentiel historique, mais ajouter une étape de rapprochement avec l'univers courant BRVM :

- nouveau slug → `NEW_ISSUER_REVIEW` ;
- nouveau nom pour ticker existant → alias / changement de dénomination ;
- ticker absent du catalogue courant → ne jamais supprimer l'historique ;
- changement de slug → relation d'alias entre ancien et nouveau slug.

## 9. Nommage et périodes

Toujours conserver séparément :

- `remote_filename_raw` ;
- `publication_title_raw` ;
- nom local normalisé ;
- dossier de classement historique ;
- période économique résolue plus tard depuis le contenu.

Le collecteur peut proposer une période candidate, mais ne doit pas imposer une période canonique.

## 10. Contrôles après téléchargement

- HTTP 200 ;
- `Content-Type` compatible PDF ;
- signature `%PDF-` lorsque applicable ;
- fichier non vide ;
- SHA-256 ;
- taille ;
- nombre de pages lorsque facilement disponible ;
- journaliser les fichiers HTML/erreur enregistrés à tort en `.pdf` ;
- conserver toutes les erreurs dans un journal de run.

## 11. Non-régression

La V2 ne doit jamais :

- supprimer un document V1 ;
- écraser silencieusement un fichier ;
- modifier une provenance historique ;
- remplacer un Drive ID historique ;
- conclure à un doublon uniquement par le nom ;
- conclure à une période économique uniquement par le nom ;
- retirer un émetteur historique parce qu'il n'est plus courant.

## 12. Intégration avec P1

P1 doit d'abord finir l'inventaire du corpus existant. Ce manifeste devient ensuite l'état de référence à comparer au catalogue BRVM courant.

La V2 pourra alors produire trois listes :

- `EXISTING_CONFIRMED` ;
- `NEW_REMOTE_DOCUMENTS` ;
- `REVISED_OR_AMBIGUOUS_DOCUMENTS`.

## 13. Décision d'implémentation

Ne pas remplacer la V1 immédiatement.

Ordre recommandé :

1. terminer P1 ;
2. créer le manifeste machine-lisible du corpus actuel ;
3. implémenter V2 en mode `--dry-run` ;
4. comparer V2 au corpus existant ;
5. valider le delta ;
6. seulement ensuite autoriser le téléchargement incrémental.
