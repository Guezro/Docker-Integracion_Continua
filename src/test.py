import unittest
import xmlrunner

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
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/var/jenkins_home/cker_Integraci_n_Continua_master/test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)

