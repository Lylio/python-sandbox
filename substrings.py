# Practice with substrings

# a[start:end] # items start through end-1
# a[start:]    # items start through the rest of the array
# a[:end]      # items from the beginning through end-1
# a[:]         # a copy of the whole array

s1 = "Hello World!"

s2 = s1[4:] # From the start, move 4 characters in and copy to end

print(s2)

s3 = s1[:-4] # From the end, count 4 characters backwards

print(s3)

s4 = s1[2:-2] # From the start, go two characters in; from the end, go two characters backwards

print(s4)
