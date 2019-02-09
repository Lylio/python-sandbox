class Employee:
    def __init__(self, ID, fname, lname, role):
        self.ID = ID
        self.fname = fname
        self.lname = lname
        self.role = role

    def GetEmployee(self):
        return 'ID: %s\nName: %s %s\nRole: %s' % (self.ID, self.fname, self.lname, self.role)
