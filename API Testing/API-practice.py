import requests, json, sys, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "https://lylie.free.beeceptor.com"


print("----- TEST GET -----")

test = requests.get(url, verify=False)

if test.status_code == 200:
   print("Test: PASSED", test.status_code)
   print(test.json())
else:
   print("Test: FAIL", test.status_code)
   sys.exit(1)


print("\n")

print("----- TEST POST -----")

payload = {"monday":"blue","tuesday":"green", "wednesday":"purple", "thursday":"orange","friday":"yello"}

test2 = requests.post("https://lylie.free.beeceptor.com", json=payload)

if test2.status_code == 200:
   print("POST test PASSED", test2.status_code)
else:
   print("POST test FAILED", test2.status_code)

print("\n")

print("----- TEST IMPORT JSON FILE -----")

with open("test.json") as f:
   data = json.load(f)
   print(data)
   print("\n")
   data2 = json.dumps(data)
   print(data2)

