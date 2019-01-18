import requests, json

# GET test
print("---- GET TEST ----")
testURL = requests.get("https://jsonplaceholder.typicode.com/todos/2")

raw_data = testURL

json_data = json.loads(raw_data.text)

if testURL.status_code == 200:
    print("GET test OK: " + str(testURL.status_code))
    print(json_data)
else:
    print("GET test FAIL: " + str(testURL.status_code))

# POST test
print("\n---- POST TEST ----")
with open('test.json') as f:
    payload = json.load(f)
    print(json.dumps(payload))
postTest = requests.post("https://postb.in/1bwS9DnP", json=payload)  # Will need recent http://www.postb.in URL here

if postTest.status_code == 200:
    print("POST test OK: " + str(postTest.status_code))
else:
    print("POST test FAIL: " + str(postTest.status_code))

# Go to the http://www.postb.in URL and refresh the page
