# Practice with JSON

import json

data = {"people": [
    {"name": "ali",
     "age": "56",
     "city": "Glasgow"},
    {"name": "sammy",
     "age": "45",
     "city": "edinburgh"}]}


print(data)

print('\n------------------')

loaded = json.loads(data)

for name in loaded:
    print(["people"][0]["name"])

