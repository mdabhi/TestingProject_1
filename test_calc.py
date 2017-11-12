#!/usr/bin/env python2.7

import unittest
import Calc


class TestCalc(unittest.TestCase):

    def test_addition(self):
        """testing the addition method"""

        self.assertEquals(Calc.addition(10, 5), 15)
        self.assertEquals(Calc.addition(-1, 1), 0)
        self.assertEquals(Calc.addition(-1, -1), -2)

    def test_subtract(self):
        """testing the subtraction method"""

        self.assertEquals(Calc.subtract(10, 5), 5)
        self.assertEquals(Calc.subtract(-1, 1), -2)
        self.assertEquals(Calc.subtract(-1, -1), 0)

    def test_multiply(self):
        """testing the multiplication method"""

        self.assertEquals(Calc.multiply(10, 5), 50)
        self.assertEquals(Calc.multiply(-1, 1), -1)
        self.assertEquals(Calc.multiply(-1, -1), 1)

    def test_divide(self):
        """testing the division method"""

        self.assertEquals(Calc.divide(10, 5), 2)
        self.assertEquals(Calc.divide(-1, 1), -1)
        self.assertEquals(Calc.divide(-1, -1), 1)
        self.assertEquals(Calc.divide(5, 2), 2)

        with self.assertRaises(ValueError):
            """raising the value error when denominator is 0"""
            Calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()


