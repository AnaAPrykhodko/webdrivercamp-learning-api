import json
import requests
from pprint import pprint
from common import TOKEN


def create_repo(url):
    header = {"Authorization": f"Bearer {TOKEN}"}
    data = {
        "name": "repo-created-with-api",
        "private": True,
        "has_wiki": False
    }
    response = requests.post(url, data=json.dumps(data), headers=header)
    print(f"Response status code: {response.status_code}")
    return response.json()


if __name__ == '__main__':
    url = 'https://api.github.com/user/repos'
    repo = create_repo(url)
    pprint(repo)
