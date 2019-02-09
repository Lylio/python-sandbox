# Practice with inheritance


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def GetName(self):
        return("%s %s" % (self.fname, self.lname))


class Employee(Person):
    def __init__(self, fname, lname, ID, role):
        Person.__init__(self, fname, lname)
        self.ID = ID
        self.role = role

    def GetEmployee(self):
        return('Name: ' + (self.GetName()) + '\n' + 'ID: ' + (self.ID) + '\n' + 'Role: ' + self.role)


if __name__ == '__main__':
    marge = Person('Marge', 'Simpson')
    homer = Employee('Homer', 'Simpson', 'HS4343', 'Power Plant Safety')

    print(marge.GetName())

    print('\n---------------------')

    print(homer.GetName())

    print('\n---------------------')

    print(homer.GetEmployee())


