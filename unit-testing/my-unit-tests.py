import unittest
from mathfunctions import adder, subtractor, multiplier, divider

class BigTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_adding(self):
        self.assertEqual(adder(5,3),8)

    def test_multiplying(self):
        self.assertEqual(multiplier(7,7),49)

    def test_divider(self):
        self.assertEqual(divider(35,5),7)

    def test_subtracting(self):
        self.assertEqual(subtractor(175,25),150)

if __name__ == '__main__':
    unittest.main()
