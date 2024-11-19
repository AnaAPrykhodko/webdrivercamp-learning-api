import requests


def get_repos(url):
    response = requests.get(url)
    response.raise_for_status()
    print(f"Response status code: {response.status_code}")
    data = response.json()
    total_count = data["total_count"]
    print(f"Total count of found items: {total_count}")
    items = data.get("items", [])
    sorted_items = sorted(items, key=lambda i: i.get("full_name", ""))
    return sorted_items


if __name__ == "__main__":
    url = "https://api.github.com/search/repositories?q=webdrivercamp-learning-python"
    list_of_items = get_repos(url)
    print()
    for item in list_of_items:
        user = item['owner']['login']
        repo = item['name']
        print(f"{user:15}", repo)
