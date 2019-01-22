phonebook = {
    "John": 1415467656,
    "Sally": 54375475,
    "Alfie": 43724323
}

print(phonebook["Sally"])  # 54375475

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
