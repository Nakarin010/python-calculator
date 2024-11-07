import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4,2),2)
        self.assertEqual(self.calc.subtract(2,4),-2)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,3),6)
        self.assertEqual(self.calc.multiply(3,2),6)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10,3),1)
        self.assertEqual(self.calc.modulo(3,10),3)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10,2),5)
        self.assertEqual(self.calc.divide(6,2),3)


if __name__ == '__main__':
    unittest.main(verbosity=2)