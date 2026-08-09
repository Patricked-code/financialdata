# Matrice de découverte — 48 dossiers sociétés BRVM

Date : 2026-08-09  
Corpus : `RAPO / Rapport V2`  
Statut global : `DISCOVERY_PASS_48_ISSUERS_COMPLETE`  
Extraction RAW intégrale : `NOT_COMPLETE`

Cette matrice signifie que chaque dossier société a été parcouru pour détecter les familles de documents et particularités conceptuelles. Elle **ne signifie pas** que chaque page de chaque PDF a déjà été extraite.

| # | Société / dossier | Ticker | Profil observé | Statut | Particularité / règle principale |
|---:|---|---|---|---|---|
| 1 | Africa Global Logistics Côte d'Ivoire | AGLC | Logistique | DISCOVERY_VALIDATED | Tonnages, manutention, transit, entreposage et activités logistiques → KPI physiques dans `operating_facts_raw`. |
| 2 | Bank of Africa Mali | BOAM | Banque | DISCOVERY_VALIDATED | Patron bancaire : PNB, RBE, coût du risque, bilan, dépôts/crédits, comparatifs. |
| 3 | Bank of Africa Niger | BOAN | Banque | DISCOVERY_VALIDATED | Rapports annuels/AG et données bancaires compatibles avec le modèle banque. |
| 4 | Bank of Africa Côte d'Ivoire | BOAC | Banque | DISCOVERY_VALIDATED | Fichiers périodiques + `divers`; la complétude doit être mesurée par contenu. |
| 5 | BICICI | BICC | Banque | DISCOVERY_VALIDATED | Un tableau intermédiaire peut juxtaposer période courante, période comparative et FY précédent. |
| 6 | Crown SIEM Côte d'Ivoire | SEMC | Industrie / emballage | DISCOVERY_VALIDATED | Changement de dénomination publié (Eviosys Packaging SIEM) → historique des noms. |
| 7 | Bank of Africa Bénin | BOAB | Banque | DISCOVERY_VALIDATED | Attestations et rapports CAC distincts; audit/document type à conserver. |
| 8 | Air Liquide Côte d'Ivoire | SIVC | Industrie | DISCOVERY_VALIDATED | Continuité historique de dénomination à gérer avec les publications récentes Erium. |
| 9 | Bank of Africa Burkina Faso | BOABF | Banque | DEEP_PILOT | Formats historiques, codes de ligne, hors-bilan, périodes ambiguës, doublons binaires, documents dans `divers`. |
| 10 | Ecobank Côte d'Ivoire | ECOC | Banque | DISCOVERY_VALIDATED | Rapports d'activité et annuels avec indicateurs bancaires et commentaires. |
| 11 | Bank of Africa Sénégal | BOAS | Banque | DISCOVERY_VALIDATED | États financiers et rapports CAC; modèle bancaire compatible. |
| 12 | BIIC Bénin | BIIC | Banque | DISCOVERY_VALIDATED | Rapports périodiques récents avec PNB, crédits, résultats et commentaires. |
| 13 | Bernabé Côte d'Ivoire | BNBC | Distribution / industrie | DISCOVERY_VALIDATED | Faits exceptionnels pouvant fausser les comparaisons; conserver commentaires et événements. |
| 14 | CIE | CIEC | Utility / concession | DEEP_PILOT | Périmètre propre vs secteur/autorité concédante, GWh, branchements, stock/flow, individual/consolidated. |
| 15 | CFAO Motors Côte d'Ivoire | CFAC | Automobile | DISCOVERY_VALIDATED | Séparer données émetteur, marché automobile et marques via `subject_scope_raw`/références. |
| 16 | Coris Bank International | CBIBF | Banque | DISCOVERY_VALIDATED | Patron bancaire compatible avec les dimensions existantes. |
| 17 | Ecobank Transnational Incorporated | ETIT | Groupe bancaire | DISCOVERY_VALIDATED | Consolidé, audits internationaux et données groupe; importance du scope. |
| 18 | Palm Côte d'Ivoire | PALC | Agro-industrie | DISCOVERY_VALIDATED | SYSCOHADA, TFT, affectation, dividende, prix de l'huile comme facteur explicatif. |
| 19 | Nestlé Côte d'Ivoire | NTLC | Industrie | DEEP_PILOT | SYSCOHADA, TAFIRE, codes de rubriques, affectation, versions révisées, données boursières. |
| 20 | MOVIS Côte d'Ivoire | MVSC | Logistique | DISCOVERY_VALIDATED | Résultat exceptionnel lié à une cession de site → besoin d'`event_facts_raw`. |
| 21 | Filtisac | FTSC | Industrie | DISCOVERY_VALIDATED | Sensibilité aux campagnes cacao/anacarde; contexte métier à conserver avec les résultats. |
| 22 | NSIA Banque Côte d'Ivoire | NSBC | Banque | DISCOVERY_VALIDATED | Banque; rapports d'activité et communiqués à conserver par type documentaire. |
| 23 | Oragroup | ORGT | Holding / groupe financier | DISCOVERY_VALIDATED | Consolidé, examen limité, augmentation de capital décidée → assurance et statut d'événement. |
| 24 | ONATEL Burkina Faso | ONTBF | Télécom | DISCOVERY_VALIDATED | KPI télécom; compatible avec le patron opérationnel SNTS/ORAC. |
| 25 | Orange Côte d'Ivoire | ORAC | Télécom groupe | DISCOVERY_VALIDATED | IFRS consolidé, multi-pays, eCapex, Parc FMI, définitions propriétaires, mentions documentaires internes. |
| 26 | NEI-CEDA Côte d'Ivoire | NEIC | Édition | DISCOVERY_VALIDATED | Saisonnalité et activité éditoriale; conserver commentaires/perspectives avec les facts. |
| 27 | SAFCA Côte d'Ivoire | SAFC | Finance | DISCOVERY_VALIDATED | Ratios prudentiels, CET1/levier, changement de contrôle/dénomination → réglementaire + événements. |
| 28 | SICOR | SICC | Agriculture / coco | DISCOVERY_VALIDATED | Production, tonnes, noix en unités, prix moyen, montant, sites, investissements, dette et événements opérationnels. |
| 29 | Servair Abidjan | ABJC | Catering / services | DISCOVERY_VALIDATED | États individuels IFRS → IFRS ≠ consolidé. |
| 30 | SICABLE | CABC | Industrie / câbles | DISCOVERY_VALIDATED | Rapports annuels, états et rapports CAC; modèle industriel compatible. |
| 31 | SETAO | STAC | BTP / projets | DISCOVERY_VALIDATED | Projet/chantier, avance de démarrage et prévision annuelle → `project_raw` + `fact_nature_raw`. |
| 32 | SAPH | SPHC | Plantation / hévéa | DISCOVERY_VALIDATED | Surfaces matures/immatures, hectares, contrats/conventions réglementées et contexte sectoriel. |
| 33 | SITAB | STBC | Tabac | DISCOVERY_VALIDATED | Volumes/références commerciales et changement de régime TVA/prix → contexte fiscal à préserver. |
| 34 | SOGB | SOGC | Plantation / hévéa | DISCOVERY_VALIDATED | États SYSCOHADA, TFT/CAFG; données agricoles compatibles avec dimensions plantation. |
| 35 | Société Générale Côte d'Ivoire | SGBC | Banque | DISCOVERY_VALIDATED | Indicateurs bancaires, parts/position de marché publiées et ratios; distinguer faits émetteur/contexte. |
| 36 | SODECI | SDCC | Utility / eau | DISCOVERY_VALIDATED | Convention/part dans le prix de l'eau, KPI opérationnels et logique de concession proche de CIEC. |
| 37 | SMB | SMBC | Bitume / hydrocarbures | DISCOVERY_VALIDATED | Kilotonnes et marge en $/baril en plus du financier → unités sectorielles universelles. |
| 38 | Société Ivoirienne de Banque | SIBC | Banque | DISCOVERY_VALIDATED | Plusieurs fichiers `_rev` → versioning/restatement obligatoire. |
| 39 | Total Côte d'Ivoire | TTLC | Distribution hydrocarbures | DISCOVERY_VALIDATED | Volumes vendus, HSEQ et changement Total → TotalEnergies; historique de nom. |
| 40 | Sonatel Sénégal | SNTS | Télécom groupe | DEEP_PILOT | KPI massifs, géographie, segments, IFRS, mouvements, KPI propriétaires, ESG. |
| 41 | Sucrivoire | SCRC | Sucre / agro-industrie | DISCOVERY_VALIDATED | Ventes en tonnes, campagnes chevauchant les années civiles et sites Zuénoula/Borotou. |
| 42 | Vivo Energy Côte d'Ivoire | SHEC | Distribution hydrocarbures | DISCOVERY_VALIDATED | Statut des comptes audités vs rapport CAC en finalisation → deux statuts distincts. |
| 43 | SOLIBRA | SLBC | Boissons | DISCOVERY_VALIDATED | États financiers, ressources/emplois, affectation et certification; modèle industriel compatible. |
| 44 | Uniwax Côte d'Ivoire | UNXC | Textile | DISCOVERY_VALIDATED | Nouveaux marchés/produits, événements de cession et effets exceptionnels à conserver. |
| 45 | Unilever Côte d'Ivoire | UNLC | Biens de consommation | DISCOVERY_VALIDATED | Rapports annuels et états; modèle industriel/SYSCOHADA compatible. |
| 46 | Tractafric Motors Côte d'Ivoire | PRSC | Automobile | DISCOVERY_VALIDATED | États système normal, notes/références comptables, distribution automobile. |
| 47 | Total Sénégal | TTLS | Distribution hydrocarbures | DISCOVERY_VALIDATED | Rapports annuels, HSE, activités et changements de marque; patron hydrocarbures. |
| 48 | Tritraf Côte d'Ivoire | TRITRAF | Corpus historique | DISCOVERY_VALIDATED | Corpus ancien observé jusqu'en 2004 dans la passe; secteur détaillé à confirmer par extraction exhaustive plutôt que l'inventer. |

## Règles de lecture de la matrice

### `DEEP_PILOT`

Le dossier a fait l'objet d'une lecture conceptuelle approfondie couvrant plusieurs familles de documents et périodes.

### `DISCOVERY_VALIDATED`

Le dossier a été parcouru pour identifier ses familles documentaires et vérifier sa compatibilité avec le modèle conceptuel initial. Cela n'implique pas une extraction exhaustive.

## Prochaine étape

Pour transformer cette matrice de découverte en matrice de couverture documentaire :

1. lister tous les sous-dossiers année + `divers` ;
2. lister tous les documents ;
3. hasher ;
4. classifier ;
5. déterminer périodes réelles ;
6. extraire document par document ;
7. enregistrer taux de couverture et anomalies.

## Règle Git

Ce registre est maintenu directement sur `main`. **Aucune branche ne doit être créée.**
