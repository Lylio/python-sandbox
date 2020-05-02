import os

colours = ['blue', 'red', 'yellow', 'green', 'orange']

print(colours[1])

def get_colour():
    print('Enter a colour position (0 - 4):')
    colour_position = input()
    colour_position = int(colour_position)
    if colour_position not in range(0, 4):
        print('Colour position must be between 0 - 4. Please run again')
        exit(0)
    else:
        print('The colour at position ' + str(colour_position) + ' is ' + colours[colour_position])
        exit(0)

if __name__ == '__main__':
    get_colour()