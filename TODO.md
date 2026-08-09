# TODO — financialdata

Backlog canonique. Ne pas considérer une tâche terminée tant que le résultat n'est pas vérifié et que `SUIVI.md` n'est pas mis à jour.

## P0 — Gouvernance initiale

**Statut : COMPLETE.**

## P1 — Inventaire documentaire exhaustif

**Statut : IN_PROGRESS / BATCH_FAST**

### Socle P1

- [x] créer le socle `inventory/` ;
- [x] vérifier les 48 dossiers société ;
- [x] identifier/analyser `telecharger_rapports_brvm.py` ;
- [x] documenter le collecteur V2 futur ;
- [x] créer `ROADMAP.md` ;
- [x] activer `P1-R PDF_RECOGNITION_DISCOVERY` ;
- [x] documenter les premières règles de reconnaissance vérifiées sur contenu réel.

### Émetteurs inventoriés au niveau dossiers/fichiers

- [x] SIVC — 53.
- [x] BOABF — 57.
- [x] BOAB — 59.
- [x] BOAC — 60.
- [x] BOAM — 44.
- [x] BOAN — 60.
- [x] BOAS — 43.
- [x] BNBC — 78.
- [x] BICC — 61.
- [x] BIIC — 2.
- [x] AGLC — 60.
- [x] CFAC — 94.
- [x] CIEC — 61.
- [x] CBIBF — 8.
- [x] SEMC — 54.
- [x] ECOC — 32.
- [x] ETIT — 81.
- [x] FTSC — 88.
- [x] MVSC — 20.
- [x] NEIC — 86.
- [x] NTLC — 81.
- [x] NSBC — 38.
- [x] ONTBF — 91.
- [x] ORGT — 23.
- [x] ORAC — 14.
- [x] PALC — 75.
- [x] SAFC — 73.
- [x] SPHC — 28 dossiers 1998–2025, **124** PDF ; total vérifié par deux recherches strictement parentées, car la recherche ticker plafonnait à 100.
- [x] ABJC — 28 dossiers 1998–2025, **82** PDF.
- [x] STAC — 26 dossiers (25 années + `divers`), **38** PDF ; 2004/2007/2009 absents.
- [x] SGBC — 27 dossiers 1999–2025, **87** PDF.
- [x] SIBC — 10 dossiers 2016–2025, **46** PDF.
- [ ] 16 autres émetteurs.

**Total recensé sur les 32 premiers émetteurs : 1 873 fichiers.**

### P1-R — reconnaissance PDF

- [x] stratégie générale : `docs/PDF_RECOGNITION_STRATEGY.md` ;
- [x] profils BICC 2022, BIIC T2 2025, ETIT 2023 ;
- [x] `DOCUMENT_METADATA_MISMATCH` ;
- [x] STOCK vs FLOW selon contexte ;
- [x] variations publiées conservées en RAW ;
- [x] tableau vs narratif conservés séparément ;
- [x] framework comptable vs scope indépendants ;
- [x] `ownership_attribution_raw` documenté comme candidat ;
- [x] T1/T2/T3/T4/S1/S2 confirmés ;
- [x] limites techniques de recherche ≠ total SOURCE ;
- [x] préserver les deep pilots BOABF/CIEC/NTLC/SNTS sans duplication ;
- [ ] ajouter seulement les profils apportant un nouveau pattern réel.

### Passes transversales P1 encore ouvertes

- [ ] produire le manifeste machine-lisible consolidé ;
- [ ] collecter/calculer les SHA-256 ;
- [ ] établir doublons exacts et relations de version ;
- [ ] résoudre les périodes économiques depuis le contenu ;
- [ ] valider l'attribution émetteur/document ;
- [ ] mesurer la couverture documentaire réelle ;
- [ ] réconcilier l'historique avec la BRVM courante.

## P1-FRESH — Collecteur BRVM V2

- [x] analyser la V1 ;
- [x] définir le design incrémental/versionné ;
- [ ] manifeste de référence ;
- [ ] `--dry-run` ;
- [ ] comparaison distante ;
- [ ] SHA-256 / validation PDF ;
- [ ] `first_seen_at` / `last_seen_at` ;
- [ ] gestion révisions/doublons/nouveaux slugs ;
- [ ] tests de non-régression ;
- [ ] téléchargement incrémental seulement après validation.

## P2 — Schéma RAW v1

À figer après couverture P1/P1-R suffisante.

## P3 — Extraction RAW exhaustive

Appliquer les profils/règles à tous les documents SOURCE validés.

## P4 — Contrôle / qualité / lineage

Contrôles sans correction silencieuse de la source.

## P5 — MAPPED

Mapping sémantique explicite et versionné.

## P6 — CANONICAL

Harmonisation multi-sociétés/périodes/unités/scopes.

## P7 — DERIVED

Calculs internes reproductibles avec formule et IDs d'entrée.

## P8 — ANALYTICS

Ratios, valorisation, rankings, screener, alertes, scoring et IA/NLP.

## Rappel permanent

**Ne jamais créer de branche. Tout travail se fait sur `main`.**
