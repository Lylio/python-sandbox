# List functions: copy, append, count, insert, pop, etc


if __name__ == '__main__':
    # Copy & Pop
    colours = ['orange', 'blue', 'green', 'brown', 'red', 'yellow']

    newColours = colours  # Only copies reference to 'colours'

    colours.pop(4)  # If you print 'newColours', red will be gone

    realCopyColours = colours.copy()  # Creates brand new array

    colours.pop(0)

    print(realCopyColours)  # Orange should still be in the list
    print('\n-----------------')
    print(colours)  # Orange should be popped out

# Append

days = ['mon', 'tue', 'wed']
print(days)
print('\n-----------------')
days.append('thur')
print(days)

# Count (occurrences of item in list)

vowels = ['a', 'e', 'i', 'o', 'u', 'o', 'a', 'i', 'e', 'u', 'u', 'e', 'a', 'o', 'e']
print(vowels.count('e'))  # 4

# Insert

people = ['sarah', 'james', 'alfie', 'gordon']
print(people)
print('\n-----------------')
people.insert(1, 'mary')
print(people)

# Reverse

cities = ['Glasgow', 'Dundee', 'Aberdeen', 'Stirling', 'Edinburgh']
print(cities)
print('\n--------------')
cities.reverse()
print(cities)

# Sort

numbers = [5,8,2,5,1,2,4,0,8,9,3]
print(numbers)
numbers.sort()
print(numbers)

