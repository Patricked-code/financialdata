# ECOC — revue binaire et visuelle des variantes SOURCE

Date : 2026-08-11
Émetteur : Ecobank Côte d'Ivoire (`ECOC`)
Statut : `VERSION_REVIEW_COMPLETE_FOR_EXPLICIT_VARIANTS`

## Règle appliquée

Aucun suffixe `_rev` ou `_2` n'est interprété seul. Chaque objet physique est conservé en SOURCE. La relation entre fichiers est qualifiée uniquement à partir des tailles, SHA-256, texte natif et, lorsque nécessaire, comparaison visuelle des pages rendues.

## 2018 — états financiers plain / `_2`

- `2018_Etats_Financiers_ECOC.pdf` — 736 528 octets — SHA `31dea2d2712a0e586ad412fb21d8187f56fc4cf97980f1eae5ef78a9b78734d0`.
- `2018_Etats_Financiers_ECOC_2.pdf` — 537 162 octets — SHA `60773e13d396db69a685888dc9a21c545cc6f17cc083b8d3ed9c564cee842449`.
- Verdict : `BINARY_DISTINCT` ; aucune fusion. La relation sémantique précise n'est pas déduite du suffixe `_2`.

## 2021 — états financiers plain / `_2`

- les deux fichiers font 333 711 octets ;
- SHA commun : `ca091608d953102461797fb13924c9bfb14357505a149bc20f924e41cde2ce7a` ;
- verdict : `EXACT_DUPLICATE` ; groupe `SHA256:ca091608d953102461797fb13924c9bfb14357505a149bc20f924e41cde2ce7a` ;
- les deux objets Drive restent conservés et reliés, aucune suppression silencieuse.

## 2023 — T1 plain / `_rev`

- plain — 779 465 octets — SHA `266c3ec99a55a19653a443636cc1dbca3b6aa71f3c131870b25374d90b30294e` ;
- `_rev` — 730 440 octets — SHA `6bfa092af971f4d7e37b077d7445f991d67a65af59b54ddd05fe2413bffe977e` ;
- les deux PDF ont 2 pages et ne disposent pas d'une couche texte exploitable suffisante ; une revue visuelle a donc été effectuée ;
- page 1 : contenu financier visible identique ;
- page 2 : la version plain indique dans le commentaire que le PNB s'établit à **16,9 milliards FCFA**, alors que le tableau publie 25 769 millions ; `_rev` corrige le commentaire à **25,8 milliards FCFA** ;
- page 2 : le commentaire relatif aux dépôts passe d'une hausse de **26,5 %** à **14,9 %**, cohérente avec le tableau publié ;
- verdict : `_rev` = `CORRECTED_VERSION_OF` + `SUPERSEDES` le plain. Les deux sources restent conservées dans SOURCE.

## 2024 — T3 plain / `_rev`

- plain — 189 741 octets — SHA `bb292c8cda31b43d4f707504b6649d6f610d3befe37aa25a0c19c2fd511808c1` ;
- `_rev` — 189 006 octets — SHA `ed7322db0acf372790d253dfe1e45dd83193b56246e2326759308d7394472b86` ;
- verdict binaire : `BINARY_DISTINCT` ;
- texte natif : matériellement identique ; seule une différence de retour à la ligne a été observée dans l'avertissement « Les chiffres du présent communiqué ne sont pas audités » ;
- comparaison visuelle : différences de composition/mise en page, sans correction chiffrée ou sémantique démontrée ;
- verdict sémantique : `NO_SEMANTIC_SUPERSESSION_PROVEN`. Conserver les deux objets SOURCE séparés.

## 2024 — rapport annuel plain / `_rev`

- plain — 1 858 788 octets — SHA `7f9b0c850c4bf08d77e81a2cf27cd386658fdcc4958ca5c22262f1b56d60d3f5` ;
- `_rev` — 1 849 613 octets — SHA `4b7492bb1aa96d606fd860aa410325afb6b9592becdf887903fee863beb77d37` ;
- les deux documents ont 10 pages ; leur texte natif extrait est identique ;
- comparaison de rendu pixel à pixel : pages 1–8 et 10 identiques ; seule la page 9 diffère ;
- page 9 : une valeur visible est corrigée de **(55 320)** à **(52 320)** ;
- verdict : `_rev` = `CORRECTED_VERSION_OF` + `SUPERSEDES` le plain. Les deux objets restent conservés en SOURCE.

## Conséquence P1

La présence d'un suffixe `_rev` peut correspondre à une vraie correction (T1 2023, annuel 2024) ou à une variante binaire sans modification sémantique démontrée (T3 2024). La règle permanente reste donc : `suffixe != preuve de supersession`.
