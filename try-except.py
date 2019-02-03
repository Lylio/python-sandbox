# Practicing try/except/finally

print("---Example 1---")

try:
    print("The variable x is: " + x)  # 'x' is NOT defined in this case
except:
    print("Error - something went wrong")

print("\n\n---Example 2---")

x = "apples"

try:
    print("The variable x is: " + x)  # 'x' IS defined in this case
except:
    print("Error - something went wrong")

print("\n\n---Example 3---")

a = 5
b = 0

try:
    total = a / b
    print(total)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("\nTry/except/finally practice is now finished.")
