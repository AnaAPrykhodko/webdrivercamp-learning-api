import requests
from common import TOKEN, owner, repo


def get_created_repo(url):
    header = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=header)
    repository = response.json()

    assert repository['has_wiki'] == False
    assert repository['private'] == True
    assert repository['name'] == repo
    assert repository['owner']['login'] == owner

    print(f"Response status code: {response.status_code}")


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{owner}/{repo}"
    get_created_repo(url)
