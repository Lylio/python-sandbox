import sys


a = 6
b = 50
total = a + b

if total != 55:
    print("Total does not equal " + str(total))
    sys.exit(0)
else:
    print("Total equals " + str(total))
    sys.exit(0)