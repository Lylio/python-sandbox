# Read in numbers and save to an array

s = []
while True:
    s = input('Enter 10 numbers: ')
    if len(s) == 10:
        break
    else:
        print('Re-type your 10 numbers!')

print('Done. Your 4th number is ' + str(s[3]))
