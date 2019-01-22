class Car:
    # Car constructor
    def __init__(self, company, colour):
        self.company = company
        self.colour = colour

    # Function to print car company and colour
    def display(self):
        print("The car company is %s and the colour is %s " % (self.company, self.colour))

class Motorcycle:
    # Motorcycle constructor
    def __init__(self, speed, colour):
        self.speed = speed
        self.colour = colour

        # Function to print motorcycle speed and colour
    def display(self):
        print("The motorcycle speed is %d mph and the color is %s" % (self.speed, self.colour))
