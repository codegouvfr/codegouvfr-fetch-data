[![Software License](https://img.shields.io/badge/Licence-MIT-orange.svg?style=flat-square)](https://git.sr.ht/~etalab/codegouvfr-fetch-data/tree/master/item/LICENSE.md) [![goodtables.io](https://goodtables.io/badge/github/etalab/data-codes-sources-fr.svg)](https://goodtables.io/github/etalab/data-codes-sources-fr)

# Presentation

The code in this repository collects data from forges (github.com,
gitlab.com and GitLab instances) about *accounts* (GitHub
organizations or GitLab groups) and their *repositories*.

For example, given [this
list](https://git.sr.ht/~etalab/codegouvfr-sources/tree/master/item/comptes-organismes-publics)
of account URLs and [this
csv](https://git.sr.ht/~etalab/codegouvfr-fetch-data/tree/master/item/platforms.csv)
of supported platforms, we collect the data we need for
[code.gouv.fr](https://code.gouv.fr).

## Todo

We aim at collecting data from more forges:

- [SourceHut](https://sourcehut.org)
- [BitBucket](https://bitbucket.org)
- [Gogs](https://gogs.io) or [Gitea](https://gitea.io) instances

SourceHut is our priority because [Etalab](https://sr.ht/~etalab/)
hosts some of its source code here.

If you are familiar with SourceHut GraphQL APIs and can help with
contributing, feel free to send a patch to
[~etalab/codegouvfr-devel@lists.sr.ht](mailto:~etalab/codegouvfr-devel@lists.sr.ht)
or to [reach us](mailto:logiciels-libres@data.gouv.fr) directly.

# Data models

We use [Table Schema
files](https://frictionlessdata.io/specs/table-schema/) in [the
schemas/ directory](./schemas/) to describe the data.

## Get the data

- Organizations data as [csv](https://code.gouv.fr/data/organizations/csv/all.csv) and [json](https://code.gouv.fr/data/organizations/json/all.json)
- Repositories data as [csv](https://code.gouv.fr//data/repositories/csv/all.csv) and [json](https://code.gouv.fr/data/repositories/json/all.json)

# Contributing

Contributions are welcome!

To send bug reports, patches or to share ideas, please write to the
*public* mailing list: [~etalab/codegouvfr-devel@lists.sr.ht](mailto:~etalab/codegouvfr-devel@lists.sr.ht)

# License

The source code of this repository is published under [MIT](LICENSE.md).

2018-2021 DINSIC, DINUM, Etalab, Antoine Augusti, Bastien Guerry.

2018-2021 Other contributors, as readable in the history of this repository.
