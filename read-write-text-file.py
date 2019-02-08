# Practicing reading from and writing to a text file

file = open('lyrics.txt', 'r')

print(file.read()) # Print all of the file

print('\n----------------------')

file2 = open('lyrics.txt', 'r')

print(file2.read(10)) # Print first 10 characters

print('\n----------------------')

file3 = open('lyrics.txt', 'r')

print(file3.readline()) # Print first line

print('\n----------------------')

# Writing to a file

file4 = open('lyrics.txt', 'a')
file4.write('\nA new sentence added to the file!')