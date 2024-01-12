"""Unit Test - create test class that inhertis from unittest.TestCase
    # run unit test with the following command:
    #   1. python -m unittest test_calc.py
    #   2. if __name__ == "__main__":
    #       unittest.main()
"""
import unittest

import calc


class TestCalc(unittest.TestCase):
    """test case should prefix with test"""

    def test_add(self):
        """test case for calc.add() method"""
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        """test case for calc.subtract() method"""
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        """test case for calc.multiply() method"""
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        """test case for calc.divide() method"""
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # test the custom exception using assertRaises() method
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # perfer way using context manager to test exception
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
