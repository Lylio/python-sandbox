# Useless Trivia
#
# Gets personal information from the user and then
# prints true but useless information about him or her

name = input("Hi, what is your name? ")

age = input("Thanks. What is your age? ")
age = int(age)

weight = int(input("Great. Last question, what is your weight in whole stones? "))

print("\nIf poet ee cummings were to email you, he'd address you as", name.lower())
print("\nBut if he was really angry at you, he would shout", name.upper())

called = name * 5
print("\nIf a small child were trying to get your attention",)
print("your name would become:")
print(called)

seconds = age * 365 * 24 * 60 * 60
print("\nYou’re over", seconds, "seconds old.")

moon_weight = weight / 6
print("\nDid you know that on the moon you would weigh only",
moon_weight, "stone?")
sun_weight = weight * 27.1
print("On the sun, you'd weigh", sun_weight, "(but, ah... not for long).")
