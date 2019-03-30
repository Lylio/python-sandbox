from unittest import TestCase
from unittest.mock import patch
from mock_main import Calculator


class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    #This is the unpatched test which will take 10 seconds
    def test_sum1(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)


    #This is the patched test which will mock the sum function and without the 10 second wait
    @patch('mock_main.Calculator.sum', return_value=9)
    def test_sum2(self, sum):
        self.assertEqual(sum(2,3), 9)