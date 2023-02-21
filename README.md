[![Software License](https://img.shields.io/badge/Licence-MIT-orange.svg?style=flat-square)](https://git.sr.ht/~codegouvfr/codegouvfr-fetch-data/tree/master/item/LICENSE.md)

# Presentation

The code in this repository collects data from forges (github.com, gitlab.com and GitLab instances) about *accounts* (GitHub organizations or GitLab groups), their *repositories* and *libraries*.

Given [this list](https://git.sr.ht/~codegouvfr/codegouvfr-sources/tree/master/item/comptes-organismes-publics.yml) of accounts URLs and [this csv](https://git.sr.ht/~codegouvfr/codegouvfr-fetch-data/tree/master/item/platforms.csv) of platforms, we collect the data we need for [code.gouv.fr](https://code.gouv.fr).

# Installation and configuration

1. Clone this repository: `git clone https://git.sr.ht/~codegouvfr/codegouvfr-fetch-data && cd codegouvfr-fetch-data`
2. Install Python dependencies: `pip install -r requirements.txt`
3. [Create a GitHub Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
4. Create an account on [libraries.io](https://libraries.io/) and create an API key on your [account page](https://libraries.io/account).
5. Set the following environment variables: GITHUB_TOKEN and LIBRARIESIO_API_KEY. Ex: `export GITHUB_TOKEN="your github token" ; export LIBRARIESIO_API_KEY="your libraries.io api key"`
6. Create the folders that will receive the output data: `mkdir -p data/organizations/csv && mkdir -p data/organizations/json && mkdir -p data/repositories/csv && mkdir -p data/repositories/json && mkdir -p data/libraries/csv && mkdir -p data/libraries/json`
7. Check the content of the `platforms.csv` file and update its content if needed.

# Generate JSON and CSV files

Launch the script with `python fetch.py`. The output files will be available in the subfolders of `data`.

## Todo

We aim at collecting data from more forges:

- [SourceHut](https://sourcehut.org)
- [BitBucket](https://bitbucket.org)
- [Gogs](https://gogs.io) or [Gitea](https://gitea.io) instances

SourceHut is our priority because [Etalab](https://sr.ht/~codegouvfr/) hosts some of its source code here.

If you are familiar with SourceHut GraphQL APIs and can help with contributing, feel free to send a patch to [~codegouvfr/codegouvfr-devel@lists.sr.ht](mailto:~codegouvfr/codegouvfr-devel@lists.sr.ht) or to [reach us](mailto:contact@code.gouv.fr) directly.

# Data models

We use [Table Schema files](https://frictionlessdata.io/specs/table-schema/).

Please refer to [the schema files in this directory](./schemas/).

## Get the data

- Organizations data as [csv](https://code.gouv.fr/data/organizations/csv/all.csv) and [json](https://code.gouv.fr/data/organizations/json/all.json)
- Repositories data as [csv](https://code.gouv.fr/data/repositories/csv/all.csv) and [json](https://code.gouv.fr/data/repositories/json/all.json)
- Libraries data as [csv](https://code.gouv.fr/data/libraries/csv/all.csv) and [json](https://code.gouv.fr/data/libraries/json/all.json)

# [Contributing](CONTRIBUTING.md)

# License

The source code of this repository is published under [MIT](LICENSE.md).

2018-2023 DINSIC, DINUM, Etalab, Antoine Augusti, Bastien Guerry.

2018-2023 Other contributors, as readable in the history of this repository.
