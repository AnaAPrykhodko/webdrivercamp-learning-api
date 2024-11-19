import requests
from common import TOKEN


def get_with_auth(url):
    response = requests.get(url, headers={"Authorization": f"Bearer {TOKEN}"})
    print(f"Response status code: {response.status_code}")
    data = response.json()
    return len(data), response.headers


if __name__ == "__main__":
    url = "https://api.github.com/user/repos"
    num_of_repos, headers = get_with_auth(url)
    print(f"Total Repos: {num_of_repos}")
    print(f"Response headers: {headers}")
