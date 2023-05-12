import json

data = json.load(open('week1.json', encoding='utf-8'))

print(type(data))


import yaml

with open("data.yaml", "r") as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)

