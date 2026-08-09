# TODO — financialdata

Backlog canonique. Ne pas considérer une tâche terminée tant que le résultat n'est pas vérifié et que `SUIVI.md` n'est pas mis à jour.

## P0 — Gouvernance initiale

- [x] Initialiser `README.md`.
- [x] Fixer la règle Git `main` uniquement.
- [x] Créer `GOVERNANCE.md`.
- [x] Créer `CLAUDE.md`.
- [x] Créer `SUIVI.md`.
- [x] Créer `DECISIONS.md`.
- [ ] Créer `ARCHITECTURE.md`.
- [ ] Créer `DATA_MODEL.md`.
- [ ] Créer `SOURCES.md`.
- [ ] Créer la gouvernance BRVM détaillée sous `docs/`.
- [ ] Créer la matrice de découverte des sociétés sous `docs/`.
- [ ] Vérifier l'ensemble du kit documentaire sur `main`.

## P1 — Inventaire documentaire exhaustif

Pour chaque société du corpus :

- [ ] inventorier tous les dossiers ;
- [ ] inventorier tous les fichiers ;
- [ ] enregistrer identifiant source, chemin, nom, taille, hash, dates et type ;
- [ ] détecter doublons binaires ;
- [ ] détecter versions/révisions probables ;
- [ ] déterminer les périodes économiques réellement couvertes ;
- [ ] identifier les années couvertes par des fichiers rangés dans `divers` ;
- [ ] mesurer la couverture documentaire réelle.

## P2 — Schéma RAW v1

- [ ] formaliser les tables universelles ;
- [ ] intégrer géométrie des tableaux ;
- [ ] intégrer scopes/dimensions extensibles ;
- [ ] intégrer provenance/versioning ;
- [ ] valider `event_facts_raw` ;
- [ ] valider `regulatory_facts_raw` ;
- [ ] décider si `context_facts_raw` est nécessaire ;
- [ ] décider si `esg_facts_raw` est nécessaire ;
- [ ] écrire migrations SQL ;
- [ ] tester les contraintes d'intégrité.

## P3 — Extraction RAW exhaustive

Ordre recommandé : procéder société par société et document par document, sans sauter directement aux analytics.

- [ ] BOABF : compléter toutes les années/documents après le pilote 2009 ;
- [ ] autres banques ;
- [ ] télécoms ;
- [ ] utilities/concessions ;
- [ ] industrie ;
- [ ] agriculture/plantations ;
- [ ] logistique/BTP/automobile/hydrocarbures/autres secteurs.

Pour chaque document :

- [ ] extraction native ;
- [ ] rendu visuel si nécessaire ;
- [ ] OCR seulement si nécessaire ;
- [ ] extraction exhaustive des tableaux ;
- [ ] extraction des textes/disclosures pertinents ;
- [ ] validation ;
- [ ] issues pour cellules ambiguës ;
- [ ] contrôle des comparatifs ;
- [ ] contrôle unité/devise/multiplicateur ;
- [ ] contrôle période/scope.

## P4 — Contrôles qualité

- [ ] équilibre bilan actif/passif lorsqu'applicable ;
- [ ] contrôles sous-totaux/totaux sans corriger le RAW ;
- [ ] comparaison multi-documents ;
- [ ] détection incohérences publiées ;
- [ ] couverture par période ;
- [ ] couverture par famille d'états ;
- [ ] journal des anomalies.

## P5 — MAPPED / CANONICAL

À ne commencer qu'après couverture RAW suffisante :

- [ ] dictionnaire de métriques ;
- [ ] mapping libellés historiques ;
- [ ] standards comptables ;
- [ ] scopes ;
- [ ] unités normalisées ;
- [ ] référentiel sociétés/titres ;
- [ ] validation multi-sectorielle.

## P6 — DERIVED / ANALYTICS

À traiter ultérieurement :

- [ ] croissance ;
- [ ] trimestres autonomes ;
- [ ] TTM ;
- [ ] CAGR ;
- [ ] marges ;
- [ ] ratios ;
- [ ] valorisations ;
- [ ] classements/screeners ;
- [ ] analyses quantitatives/IA.

## Rappel permanent

**Ne jamais créer de branche. Tout travail de ce dépôt se fait sur `main`.**
