import json
import requests
import sys

# Task 1: GET an array of JSON objects from a URL and print them

raw_data = requests.get("https://jsonplaceholder.typicode.com/todos")
if raw_data.status_code != 200:
    print("GET data FAILED", raw_data.status_code)
    sys.exit(1)

json_data = json.loads(raw_data.text)

print("\n")

print(json_data)

# Task 2: Loop through the JSON objects
# and add only the 'title' property of each object to a new array of JSON objects

print("\n")

title_array = []

for each in json_data:
    title_array.append({
        "title": each["title"]
    })

print(title_array)

# Task 3: POST specific properties from JSON objects
# (in this case, 'completed' property from https://jsonplaceholder.typicode.com/todos will not be posted)
print("\n----- POST TEST -----")

for each in json_data:
    payload = {
        "userId": each["userId"],
        "id": each["id"],
        "title": each["title"]
    }
    post_JSON = requests.post("https://postb.in/l0rvkese", json=payload)  # Requires new bin from https://postb.in
    if post_JSON.status_code == 200:
        print("POST OK", post_JSON.status_code)
    else:
        print("POST FAIL", post_JSON.status_code)
