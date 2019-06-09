import logging

logging.basicConfig(level=logging.INFO)

def my_method():
    name = 'John'
    logging.debug('%s is the name', name)

def my_second_method():
    a = 8
    b = 6
    total = a + b
    logging.info('%d is the total', total)

def my_third_method(x, y):
    logging.critical('coordinates are %d %d', x, y)

if __name__ == '__main__':
    my_method()
    my_second_method()
    my_third_method(56, 143)

