import unittest
from arithmetics import *

class TestMonomial(unittest.TestCase):

    def test_monomial_mul(self):
        m1 = Monomial(2, {"a":3, "b":2})
        m2 = Monomial(3, {"b":3, "c":1})
        self.assertEqual(m1 * m2, Monomial(6, {"a":3, "b":5, "c":1}))
    
    def test_monomial_add(self):
        m1 = Monomial(2, {"a":3, "b":2})
        m2 = Monomial(3, {"b":3, "c":1})
        self.assertRaises(Exception, lambda: m1 + m2)

        self.assertEqual(m1 + m1, Monomial(4, {"a":3, "b":2}))
        m3 = m1 + m1
        self.assertEqual(m3 - m1, Monomial(2, {"a":3, "b":2}))

    

if __name__ == '__main__':
    unittest.main()