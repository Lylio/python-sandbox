# Casting practice

x = 5

y = "4"

if __name__ == '__main__':
    #print("I have " + x + " apples.") # Error - x is not a String

    print("I have " + str(x) + " apples.")

    print(9 * y) # Does not multiply: prints '4' nine times

    print(9 * int(y)) # 36