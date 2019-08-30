def test1(*wordlist):
    for word in wordlist:
        print(word + "YEAH ")

if __name__ == '__main__':
    fruits = ["apples", "oranges", "grapes"]
    test1(fruits)