import requests
import sys
import os


class APIClient:
    def __init__(self, token, timeout):
        self.headers = {"Authorization": "Bearer " + token}
        self.timeout = timeout

    def get(self, url, params):
        r = requests.get(url, params=params, headers=self.headers, timeout=self.timeout)
        r.raise_for_status()
        return r


token = os.environ.get("GITHUB_TOKEN")
if token is None:
    sys.exit("Token is missing: set GITHUB_TOKEN")

if len(sys.argv) != 2:
    sys.exit("Usage: python analyzer.py USERNAME")

username = sys.argv[1]
url = "https://api.github.com/users/" + username + "/repos"

client = APIClient(token, 5)

all_repos = []
page = 1

while True:
    try:
        r = client.get(url, {"page": page})
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            sys.exit("GitHub rejected the token: check GITHUB_TOKEN.")
        else:
            sys.exit("GitHub refused the request.")
    except requests.exceptions.Timeout:
        sys.exit("GitHub took too long to respond.")

    repos = r.json()
    if len(repos) == 0:
        break
    all_repos.extend(repos)
    page = page + 1

counts = {}
for repo in all_repos:
    lang = repo["language"]
    if lang is None:
        lang = "Unknown"
    counts[lang] = counts.get(lang, 0) + 1

for lang in counts:
    print(lang, counts[lang])