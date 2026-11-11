import unittest
from source.square import square

class SquareTestCase(unittest.TestCase):
    def test_positiveNumbers_square(self):
        self.assertEqual(square(5), 25)
        self.assertEqual(square(3), 9)
        self.assertEqual(square(18), 324)
    def test_negativeNumbersAndZero_square(self):
        self.assertEqual(square(0), 0)
        self.assertEqual(square(-3), 9)
        self.assertEqual(square(-10), 100)
        self.assertEqual(square(-67), 4489)
    def test_fractionalNumbers_square(self):
        self.assertAlmostEqual(square(0.1), 0.01)
        self.assertAlmostEqual(square(0.0), 0.0)
        self.assertAlmostEqual(square(-0.14), 0.0196)
    def test_numericStrings_square(self):
        with self.assertRaises(TypeError):
            square('5')
        with self.assertRaises(TypeError):
            square('0.1')
        with self.assertRaises(TypeError):
            square('-12')
    def test_bool_square(self):
        self.assertEqual(square(True), 1)
        self.assertEqual(square(False), 0)
