import unittest
from main import fibonacci_mas_optimo

class TestStringMethods(unittest.TestCase):

    def test_negativo(self):
        self.assertRaises(ValueError)
        fibonacci_mas_optimo(5)

if __name__ == '__main__':
    unittest.main()

