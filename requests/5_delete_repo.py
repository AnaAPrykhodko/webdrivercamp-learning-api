import requests
from common import TOKEN, owner, repo


def delete_repo(url):
    header = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.delete(url, headers=header)
    print(f"Response status code: {response.status_code}")


if __name__ == "__main__":
    url = f'https://api.github.com/repos/{owner}/{repo}'
    delete_repo(url)
