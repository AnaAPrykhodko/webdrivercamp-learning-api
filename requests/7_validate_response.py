import json
import requests
from pprint import pprint


def find_mismatched_data(url, file_name):
    response = requests.get(url)
    data = response.json()
    data_result = data["results"]

    with open(file_name, 'r') as reader:
        content = json.load(reader)
        content_result = content["results"]

    mismatches = {}
    if len(data_result) == len(content_result):
        for i in range(len(data_result)):
            for key, value in content["results"][i].items():
                planet_name = content["results"][i]["name"]
                if value != data["results"][i][key]:
                    if planet_name not in mismatches:
                        mismatches.update({planet_name: []})
                    mismatches[planet_name].append({key: {
                        'Expected': value, 'Actual': data["results"][i][key]}})
    return mismatches


if __name__ == "__main__":
    url = "https://swapi.dev/api/planets/"
    file_name = "planets.json"
    pprint(find_mismatched_data(url, file_name))
