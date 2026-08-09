# P1 ROOT MANIFEST — RAPO / Rapport V2

Date de vérification : 2026-08-09

## Racine

Drive folder : `RAPO / Rapport V2`

ID : `1dsobS8AStWqa1ds3RAnmNS1jnGZWmJy2`

## Contenu direct vérifié

- 48 dossiers société ;
- 1 dossier de gouvernance : `_GOUVERNANCE_BRVM_RAW_DATABASE` ;
- 1 script Python : `telecharger_rapports_brvm.py`.

Le mapping `COMPANIES` du script contient lui aussi exactement 48 sociétés, ce qui concorde avec les 48 dossiers société actuellement présents à la racine.

## Script de collecte historique

- nom : `telecharger_rapports_brvm.py`
- Drive ID : `1F1WRVMG4C27EOTMq5Gt9FT9Mosv-Rryz`
- taille : 14546 octets
- MIME : `text/x-python`
- source déclarée : `https://www.brvm.org`
- dépendances déclarées : `requests`, `beautifulsoup4` (BeautifulSoup n'est pas utilisé dans la version inspectée ; le script utilise `HTMLParser`)
- nombre de sociétés : 48

### Comportement observé

Le script :

- parcourt des pages `https://www.brvm.org/fr/rapports-societe-cotes/<slug>` ;
- collecte les liens PDF `/sites/default/files/` ;
- tente d'affecter une année depuis le nom du fichier ;
- crée les dossiers société/année ;
- standardise certains noms de fichiers ;
- ajoute des suffixes numériques en cas de collision de nom ;
- marque `_rev` si le nom original contient certains mots de correction ;
- télécharge avec retries.

### Limites pour P1

Le script n'est pas la source de vérité de l'inventaire :

- `determine_year()` peut produire une année approximative ;
- les suffixes `_2`, `_3`, etc. indiquent une collision de nom dans le téléchargement, pas nécessairement un doublon binaire ;
- des noms non standardisés subsistent ;
- il ne calcule pas de hash de contenu ;
- il désactive la vérification SSL.

Conséquence : P1 reconstruit l'inventaire depuis Drive et conserve le script comme provenance du processus historique de collecte.

## Statut P1

- root manifest : `COMPLETE`
- 48 dossiers société identifiés : `COMPLETE`
- inventaire fichier par fichier des 48 sociétés : `IN_PROGRESS`
- hash de tous les fichiers : `NOT_COMPLETE`
- détection de doublons exhaustive : `NOT_COMPLETE`
- résolution des périodes économiques : `NOT_COMPLETE`
