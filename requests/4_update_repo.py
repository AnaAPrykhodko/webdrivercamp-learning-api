import requests
from common import TOKEN, owner, repo


def update_repo(url):
    header = {"Authorization": f"Bearer {TOKEN}"}
    data = {
        "description": "I know Python Requests!"
    }
    response = requests.patch(url, headers=header, json=data)
    repository = response.json()
    print(f"Response status code: {response.status_code}")
    return repository


if __name__ == '__main__':
    url = f'https://api.github.com/repos/{owner}/{repo}'
    repo = update_repo(url)
    assert repo['description'] == 'I know Python Requests!'
