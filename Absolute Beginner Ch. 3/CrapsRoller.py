# Craps Roller
# Demonstrates random number generation
import random

die1 = random.randint(1,6)
die2 = random.randint(1,6)
total = die1 + die2

input("Press enter to roll die 1: ")

input("Press enter to roll die 2: ")

print("Die 1 rolled a " + str(die1) + " and die 2 rolled a " + str(die2) + " - your total is " + str(total))
