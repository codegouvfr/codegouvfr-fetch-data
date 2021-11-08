[![Software License](https://img.shields.io/badge/Licence-MIT-orange.svg?style=flat-square)](https://git.sr.ht/~etalab/codegouvfr-fetch-data/tree/master/item/LICENSE.md)

# Ce que fait codegouvfr-fetch-data

Le but de ce dépôt est de collecter des métadonnées sur les comptes
d'organisation publics et les dépôts qu'ils publient.

Ne sont pour l'instant traités que les comptes présents sur GitHub et
les forges GitLab.

Pour ajouter le compte d'organisation de votre organisme, voir [ce
fichier](https://git.sr.ht/~etalab/codegouvfr-sources/blob/master/comptes-organismes-publics)
ou envoyer un mail à [logiciels-libres@data.gouv.fr](mailto:logiciels-libres@data.gouv.fr).

## Données

[![goodtables.io](https://goodtables.io/badge/github/etalab/data-codes-sources-fr.svg)](https://goodtables.io/github/etalab/data-codes-sources-fr)

- La liste des organisations en [csv](/data/organizations/csv/all.csv) et [json](/data/organizations/json/all.json)
- La liste des dépôts en [csv](/data/repositories/csv/all.csv) et [json](/data/repositories/json/all.json)

## Description des données

Les données sont décrites à l'aide de fichiers [Table Schema](https://frictionlessdata.io/specs/table-schema/) dans [le dossier schemas](./schemas/).

### Métadonnées d'un répertoire Git

#### Modèle de données

- Clé primaire : `repository_url`, `organization_name`

| Nom                      | Type                                | Description                                                                   | Exemple                                  | Propriétés                                     |
|--------------------------|-------------------------------------|-------------------------------------------------------------------------------|------------------------------------------|------------------------------------------------|
| name                     | chaîne de caractères                | Le nom du répertoire                                                          | nom-repertoire                           | Valeur obligatoire                             |
| organization_name        | chaîne de caractères                | Le nom de l'organisation                                                      | etalab                                   | Valeur obligatoire                             |
| platform                 | chaîne de caractères                | La plateforme de dépôt de code                                                | GitHub                                   | Valeur obligatoire, autorisées : GitHub,GitLab |
| repository_url           | chaîne de caractères (format `uri`) | L'URL vers le répertoire                                                      | https://github.com/etalab/nom-repertoire | Valeur obligatoire                             |
| description              | chaîne de caractères                | La description du répertoire                                                  | Ce répertoire est utile                  | Valeur optionnelle                             |
| is_fork                  | booléen                             | Indique si le répertoire est un fork                                          | false                                    | Valeur obligatoire                             |
| is_archived              | booléen                             | Indique si le répertoire est archivé, c'est-à-dire qu'il est en lecture seule | false                                    | Valeur obligatoire                             |
| creation_date            | date et heure                       | La date de création du répertoire                                             | 2018-12-01T20:00:55Z                     | Valeur obligatoire                             |
| last_update              | date et heure                       | La date de dernière mise à jour du répertoire                                 | 2018-12-01T20:00:55Z                     | Valeur obligatoire                             |
| homepage                 | chaîne de caractères                | URL vers la page d'accueil du projet                                          | https://etalab.gouv.fr                   | Valeur optionnelle                             |
| stars_count              | nombre entier                       | Le nombre de fois où le répertoire a été ajouté aux favoris                   | 42                                       | Valeur obligatoire, Valeur minimale : 0        |
| forks_count              | nombre entier                       | Le nombre de fois où le répertoire a été forké                                | 13                                       | Valeur obligatoire, Valeur minimale : 0        |
| license                  | chaîne de caractères                | La licence du répertoire, telle que détectée par la plateforme                | MIT                                      | Valeur optionnelle                             |
| open_issues_count        | nombre entier                       | Le nombre d'issues actuellement ouvertes                                      | 0                                        | Valeur obligatoire, Valeur minimale : 0        |
| language                 | chaîne de caractères                | Le langage principal du répertoire, tel que détecté par la plateforme         | Python                                   | Valeur optionnelle                             |
| topics                   | chaîne de caractères                | Les tags du répertoire                                                        | utile,france,opendata                    | Valeur optionnelle                             |
| software_heritage_exists | booléen                             | Indique si le répertoire a déjà été archivé sur Software Heritage             | false                                    | Valeur obligatoire                             |
| software_heritage_url    | chaîne de caractères (format `uri`) | L'URL vers l'interface web de Software Heritage pour ce répertoire            | https://archive.softwareheritage...      | Valeur obligatoire                             |

### Métadonnées d'une organisation Git

#### Modèle de données

- Clé primaire : `login`

| Nom                | Type                                  | Description                                        | Exemple                                                    | Propriétés                                             |
|--------------------|---------------------------------------|----------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------|
| login              | chaîne de caractères                  | Le pseudo de l'organisation                        | Etalab                                                     | Valeur obligatoire                                     |
| description        | chaîne de caractères                  | La description de l'organisation                   | Observatoire accidentologie plaisance et loisirs nautiques | Valeur optionnelle                                     |
| nom                | chaîne de caractères                  | Le nom complet de l'organisation                   | Ministère de l'Intérieur                                   | Valeur optionnelle                                     |
| organization_url   | chaîne de caractères (format `uri`)   | URL vers l'organisation                            | https://github.com/etalab                                  | Valeur obligatoire                                     |
| website            | chaîne de caractères (format `uri`)   | Site web de l'organisation                         | https://etalab.gouv.fr                                     | Valeur optionnelle                                     |
| location           | chaîne de caractères                  | Adresse physique de l'organisation                 | Paris, France                                              | Valeur optionnelle                                     |
| email              | chaîne de caractères (format `email`) | Adresse e-mail de contact de l'organisation        | contact@etalab.gouv.fr                                     | Valeur optionnelle                                     |
| is_verified        | booléen                               | Indique si l'organisation est vérifiée             | true                                                       | Valeur optionnelle                                     |
| repositories_count | nombre entier                         | Le nombre de répertoires publics de l'organisation | 42                                                         | Valeur obligatoire, Valeur minimale : 0                |
| creation_date      | date et heure                         | La date de création de l'organisation              | 2013-08-26T16:03:40Z                                       | Valeur optionnelle                                     |
| platform           | chaîne de caractères                  | La plateforme utilisée de l'organisation           | GitHub                                                     | Valeur obligatoire, Valeurs autorisées : GitHub,GitLab |

# Contributions

Vos contributions sont les bienvenues !

Pour des retours d'anomalie ou des propositions de contributions sur
l'un de ces dépôts, merci d'écrire à la liste de discussion *publique*
[~etalab/logiciels-libres@lists.sr.ht](mailto:~etalab/logiciels-libres@lists.sr.ht).

# Licence

Le code source du répertoire est publié sous [la licence MIT](LICENSE.md).

2018-2021 Direction interministérielle du numérique et du système d’information et de communication de l’État, Antoine Augusti, Bastien Guerry.

2018-2021 Les autres contributeurs dans la liste est accessible via l’historique du dépôt.
