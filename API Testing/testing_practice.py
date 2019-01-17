import requests, sys, json


# Remember to be on the proxy-less wifi
# A URL outside local/intranet won't work below



# GET test
print("--------------------------------------------")
testURL = requests.get("https://jsonplaceholder.typicode.com/todos/2")

raw_data = testURL

data = json.loads(raw_data.text)

if testURL.status_code == 200:
    print "GET test OK"
    print json.dumps(data) # For fun print out the JSON
else:
    print "GET test FAIL"

# POST web
print("\n\n--------------------------------------------")
#with open('test_data/test.json') as f:
#payload = json.load(f)
payload = {"John":"Lennon", "Ringo":"Starr"}
print json.dumps(payload)
test2 = requests.post("https://postb.in/4c024fFM", data=payload) # Will need recent postb.in URL here

print("status code: "+str(test2.status_code))

if test2.status_code == 200:
    print("POST test OK")
else:
    print "POST test FAIL"

# Go to the postb.in URL and refresh the page



