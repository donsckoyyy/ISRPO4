import unittest
from source.add_binary import add_binary

class AddBinaryTestCase(unittest.TestCase):
    def test_positiveNumbers_add_binary(self):
        self.assertEqual(add_binary(7, 8), '1111')
        self.assertEqual(add_binary(1, 1), '10')
        self.assertEqual(add_binary(5, 0), '101')
    def test_ifSumIsZero_add_binary(self):
        self.assertEqual(add_binary(0, 0), '0')
        self.assertEqual(add_binary(-3, 3), '0')
        self.assertEqual(add_binary(5, -5), '0')
    def test_positiveAndNegativeNumbers_add_binary(self):
        self.assertEqual(add_binary(-2, 5), '11')
        self.assertEqual(add_binary(10, -3), '111')
    @unittest.expectedFailure
    def test_ifSumIsNegative_add_binary(self):
        self.assertEqual(add_binary(-5, 2), '-11')
        self.assertEqual(add_binary(-10, 3), '-111')
    def test_fractionalNumbers_add_binary(self):
        with self.assertRaises(TypeError):
            add_binary(1.5, 1)
        with self.assertRaises(TypeError):
            add_binary(0.5, 0.5)
    def test_numericStrings_add_binary(self):
        with self.assertRaises(TypeError):
            add_binary('1', '1')
        with self.assertRaises(TypeError):
            add_binary('7', '8')
    def test_bool_add_binary(self):
        self.assertEqual(add_binary(True, True), '10')
        self.assertEqual(add_binary(True, False), '1')
        self.assertEqual(add_binary(False, False), '0')