# Count instances of word in a list


days = ['mon', 'fri', 'tue', 'mon', 'wed', 'sun', 'mon', 'sat', 'thur', 'mon']

total = 0

for w in days:
    if(w == 'mon'):
        total += 1

print('Mon appear: ' + str(total) + ' times.')