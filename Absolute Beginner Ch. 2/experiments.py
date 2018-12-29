#Experimenting with functions
sentence = "my name is lyle"
sentence_title = (sentence.title())
print(sentence_title)
print(sentence_title.istitle())

#Convert string to uppercase
word = "elephant"
print(word.upper())

#Convert string to lowercase
word2 = "BUTTONS"
print(word2.lower())

#Replace words in a sentence
sentence2 = "I read the news today, oh boy"
print(sentence2.replace("news", "weather"))

print("\n\n----------------------------------")


#Casting strings to integers
print("Please enter the following grocery amounts in whole pounds:")
apples = int(input("Bag of apples: "))
cheese = int(input("Block of cheddar cheese: "))
detergent = int(input("Bottle of detergent: "))
total = apples + cheese + detergent
print("The total is: £", total)

