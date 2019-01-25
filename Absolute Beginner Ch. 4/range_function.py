# Demonstrates the range() function

print("Counting: ")
for i in range(10):
    print(i, end=" ") #end=" " prints numbers on same line


print("\n\nCounting in 5s")
for i in range(0, 50, 5):
    print(i, end=" ")

print("\n\nCounting backwards: ")
for i in range(10, 0, -1):
    print(i, end=" ")