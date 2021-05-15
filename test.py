import unittest

from operaciones import *

class TestOperaciones(unittest.TestCase):
    def setUp(self):
        pass

    def test_suma(self):
        esperado = 3
        actual = suma(1,2)
        self.assertEqual(actual,esperado)

    def test_resta(self):
        esperado = -1
        actual = resta(1,2)
        self.assertEqual(actual,esperado)

    def test_multiplicacion(self):
        esperado = 2
        actual = multiplicacion(1,2)
        self.assertEqual(actual,esperado)

    def test_division(self):
        esperado = 2
        actual = division(4,2)
        self.assertEqual(actual,esperado)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()