# Practice with classes


class Student(object):

    def __init__(self, name, id, degree):
        self.name = name
        self.id = id
        self.degree = degree
        print('A student object has been created')

    def print_details(self):
        print('Name: %s' % self.name)
        print('ID: %s' % self.id)
        print('Degree: %s' % self.degree)

if __name__ == '__main__':
    student558 = Student('Sammy West', '558', 'BSc Biology')
    student735 = Student('Amy Hicks', '735', 'MA History')

    student558.print_details()

