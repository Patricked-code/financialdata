# SUIVI — financialdata

Dernière mise à jour : 2026-08-09

## Point de reprise courant

Le dépôt `Patricked-code/financialdata` est la mémoire persistante et le dépôt canonique du chantier.

### Règle Git active

- `main` uniquement ;
- aucune branche ;
- aucune PR normale.

### Règle universelle des agents

Tout agent doit reprendre le projet au point officiel, préserver l'existant et continuer sans régression.

## Roadmap canonique

`P0 GOUVERNANCE → P1 SOURCE/INVENTAIRE + P1-R RECOGNITION → P1-FRESH COLLECTEUR → P2 RAW SCHEMA → P3 RAW EXTRACTION → P4 QUALITY/LINEAGE → P5 MAPPED → P6 CANONICAL → P7 DERIVED → P8 ANALYTICS`.

Architecture : `SOURCE → RAW → MAPPED → CANONICAL → DERIVED → ANALYTICS`.

## P0 — Gouvernance

**COMPLETE**

## P1 — Inventaire SOURCE

**IN_PROGRESS / BATCH_FAST**

Méthode : inventorier par lots, réserver la revue détaillée aux anomalies et faire progresser P1-R en parallèle.

### Émetteurs inventoriés

1. SIVC — 53
2. BOABF — 57
3. BOAB — 59
4. BOAC — 60
5. BOAM — 44
6. BOAN — 60
7. BOAS — 43
8. BNBC — 78
9. BICC — 61
10. BIIC — 2
11. AGLC — 60
12. CFAC — 94

**Total : 671 fichiers recensés sur 12/48 émetteurs.**

Restant : **36 émetteurs**.

### Lot 8–12 — anomalies/patterns utiles

- BNBC : 28 dossiers 1998–2025, nombreuses collisions historiques ;
- BICC : 28 dossiers 1998–2025, `2019_Etats_Financiers_BICC_rev.pdf`, T2 présent ;
- BIIC : seulement dossiers 2024/2025 et 2 PDF en 2025 ; 2024 vide ;
- AGLC : 28 dossiers 1998–2025, comptes IFRS individuels/consolidés distincts, T1 2025 + T1 2025 rev ;
- CFAC : 26 dossiers, 94 PDF, collisions jusqu'à `_11`, EF 2023 rev, faits émetteur + contexte marché à distinguer.

## P1-R — PDF_RECOGNITION_DISCOVERY

**ACTIVE_IN_PARALLEL**

Premiers profils vérifiés sur contenu réel :

- `docs/recognition_profiles/BANKING_FINANCIAL_STATEMENTS_BICC_2022.md`
- `docs/recognition_profiles/BANKING_ACTIVITY_BIIC_T2_2025.md`

### Règles de reconnaissance désormais vérifiées

- BICC 2022 : ACTIF/PASSIF côte à côte + hors-bilan + résultat ; géométrie de tableau nécessaire ;
- BIIC : le contenu visible confirme `DEUXIEME TRIMESTRE 2025` ; T2 est supporté ;
- PDF BIIC : métadonnée interne `Title` incohérente avec le contenu visible → `DOCUMENT_METADATA_MISMATCH` ;
- `juin-25` peut être STOCK dans le bilan et FLOW/cumul dans le résultat ;
- variations valeur/% explicitement publiées = RAW `PUBLISHED` ;
- tableau en millions et narratif en milliards/arrondi = observations documentaires distinctes avant réconciliation ;
- `_2/_3/...` = collision, pas doublon ; `_rev` = version à revoir ;
- framework IFRS et scope individuel/consolidé sont indépendants ;
- un corpus court/lacunaire est un état SOURCE valide, jamais à compléter artificiellement.

Référence complète : `docs/PDF_RECOGNITION_STRATEGY.md` et décision `D032`.

## P1-FRESH

Design V2 documenté mais non activé. Aucun delta distant n'est téléchargé automatiquement pendant P1.

## Passes transversales encore ouvertes

- hash global ;
- manifeste machine-lisible ;
- versions/doublons ;
- périodes économiques exhaustives ;
- attribution et couverture documentaire ;
- réconciliation BRVM courante.

## Prochaine action exacte

Continuer P1 en mode batch à partir du **13e émetteur : CIE - CIEC**.

Important : CIEC a déjà servi de deep pilot conceptuel. Ne pas refaire l'analyse de zéro. Faire son inventaire SOURCE P1 rapidement puis utiliser un PDF utility représentatif seulement si cela apporte un pattern P1-R non encore documenté.

Puis poursuivre dans l'ordre V1 :

`CIEC → CBIBF → SEMC → ECOC → ETIT ...`

## Ordre de reprise obligatoire

1. `GOVERNANCE.md`
2. `AGENTS.md`
3. `CLAUDE.md`
4. `ROADMAP.md`
5. `SUIVI.md`
6. `DECISIONS.md`
7. `TODO.md`
8. `SOURCES.md`
9. `docs/PDF_RECOGNITION_STRATEGY.md`
10. inventaires existants

## Point de reprise exact

`P1_BATCH_FAST → INVENTORY_COMPLETE_12_OF_48 → 671_FILES → NEXT = CIEC + P1-R ACTIVE`
