from collections import defaultdict
from io import BytesIO
from urllib.request import urlopen
import yaml
import os

from platforms import Detector as PlatformDetector
from storage import save_repos, save_orgs, save_libraries
from utils import fetch_libraries

def fetch_orgs(detector):
    organizations = []

    resp = urlopen(
        os.getenv("ORGAS_LIST_URL") or "https://git.sr.ht/~codegouvfr/codegouvfr-sources/blob/master/comptes-organismes-publics.yml"
    )
    data = resp.read()

    try:
        data = yaml.safe_load(data)
    except yaml.YAMLError as exc:
        print('YAMLError parsing error',exc)
        return 'error'

    for org in data:
        try:
            organizations.extend(detector.to_orgs(org))
        except Exception as e:
            print(e)

    return organizations


detector = PlatformDetector()
organizations = fetch_orgs(detector)

# Save details about each repo for an org
all_repos = defaultdict(list)
for organization in organizations:
    print("Fetching repos for: ", organization)

    repos = organization.repos_for_org()

    for k, v in repos.items():
        all_repos[k].extend(v)

save_repos(all_repos)

# Save details about each org
all_orgs = defaultdict(list)
for organization in organizations:
    data = organization.get_org()

    if data == {}:
        continue
    print("Fetching details for: ", organization)

    for k, v in data.to_dict().items():
        all_orgs[k].append(v)

save_orgs(all_orgs)

# Save libraries created by each org
all_libs = []

print("Fetching libraries from librairies.io")
libraries = fetch_libraries(all_orgs)

save_libraries(libraries)

detector.save_swh_data()
