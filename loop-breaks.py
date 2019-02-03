# Using 'break' in a loop


i = 0
j = 7
while i < 20:
    print(i)
    i += 1
    if i == j:
        print("break at " + str(i))
        break