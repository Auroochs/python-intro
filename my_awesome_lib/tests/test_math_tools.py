import unittest
from my_awesome_lib import math_tools

class TestMathTools(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math_tools.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(math_tools.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(math_tools.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(math_tools.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            math_tools.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
