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

- [x] SIVC — 53 fichiers.
- [x] BOABF — 57 fichiers.
- [x] BOAB — 59 fichiers.
- [x] BOAC — 60 fichiers.
- [x] BOAM — 44 fichiers.
- [x] BOAN — 60 fichiers.
- [x] BOAS — 43 fichiers.
- [x] BNBC — 78 fichiers.
- [x] BICC — 61 fichiers.
- [x] BIIC — 2 fichiers.
- [x] AGLC — 60 fichiers.
- [x] CFAC — 94 fichiers.
- [x] CIEC — 61 fichiers.
- [x] CBIBF — 8 fichiers.
- [x] SEMC — 54 fichiers.
- [x] ECOC — 32 fichiers.
- [x] ETIT — 81 fichiers.
- [x] FTSC — 88 fichiers.
- [x] MVSC — 20 fichiers.
- [x] NEIC — 86 fichiers.
- [x] NTLC — 81 fichiers.
- [x] NSBC — 38 fichiers.
- [x] ONTBF — 19 dossiers (2008–2025 + `divers`), 91 fichiers.
- [x] ORGT — 8 dossiers (2018–2025), 23 fichiers.
- [x] ORAC — 4 dossiers (2022–2025), 14 fichiers.
- [x] PALC — 25 dossiers, 75 fichiers ; 2000 et 2002 absents.
- [x] SAFC — 27 dossiers, 73 fichiers ; 2015 absent.
- [ ] 21 autres émetteurs.

**Total recensé sur les 27 premiers émetteurs : 1 496 fichiers.**

### P1-R — reconnaissance PDF

- [x] stratégie générale : `docs/PDF_RECOGNITION_STRATEGY.md` ;
- [x] profil BICC 2022 ;
- [x] profil BIIC T2 2025 ;
- [x] profil ETIT 2023 ;
- [x] `DOCUMENT_METADATA_MISMATCH` ;
- [x] STOCK vs FLOW selon contexte ;
- [x] variations publiées conservées en RAW ;
- [x] tableau vs narratif conservés séparément ;
- [x] framework comptable vs scope indépendants ;
- [x] `ownership_attribution_raw` documenté comme candidat ;
- [x] T1/T2/T3/T4/S1/S2 confirmés dans le corpus ;
- [x] préserver les deep pilots BOABF/CIEC/NTLC/SNTS sans duplication ;
- [ ] ajouter seulement les nouveaux profils apportant un pattern réellement nouveau.

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
