class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def GetName(self):
        return (self.fname + ' ' + self.lname)
