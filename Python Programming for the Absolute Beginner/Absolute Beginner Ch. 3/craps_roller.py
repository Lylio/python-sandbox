# Craps Roller
# Demonstrates random number generation
import random

input("Press enter to roll die one: ")
die1 = random.randint(1,6)

input("Press enter to roll die two: ")
die2 = random.randint(1,6)

total = die1 + die2

print("Die one rolled a " + str(die1) + " and die two rolled a " + str(die2) + " - your total is " + str(total))
