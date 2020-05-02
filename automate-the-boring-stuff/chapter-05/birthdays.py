birthdays = {'Sammy': 'Feb 12', 'Ray': 'June 4', 'Mary': 'October 10', 'Donald': 'March 7'}

while True:
    print('Enter a name (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have the birthday information for ' + name)
        print('What is their birthday?')
        new_bday = input()
        birthdays[name] = new_bday
        print('Birthdays database updated.')
