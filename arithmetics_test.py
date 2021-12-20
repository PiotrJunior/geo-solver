import unittest
from arithmetics import *

class TestMonomial(unittest.TestCase):

    def test_monomial_mul(self):
        m1 = Monomial(2, {"a":3, "b":2})
        m2 = Monomial(3, {"b":3, "c":1})
        self.assertEqual(m1 * m2, Monomial(6, {"a":3, "b":5, "c":1}))
        self.assertEqual(m1 * 2, Monomial(2, {"a":3, "b":2}))
    
    def test_monomial_add(self):
        m1 = Monomial(2, {"a":3, "b":2})
        m2 = Monomial(3, {"b":3, "c":1})
        self.assertRaises(Exception, lambda: m1 + m2)

        self.assertEqual(m1 + m1, Monomial(4, {"a":3, "b":2}))
        m3 = m1 + m1
        self.assertEqual(m3 - m1, Monomial(2, {"a":3, "b":2}))


class TestPolynomail(unittest.TestCase):

    def test_polynomial_add(self):
        m1 = Monomial(2, {"a":3, "b":2})
        m2 = Monomial(3, {"b":3, "c":1})
        p1 = Polynomial([m1])
        p2 = Polynomial([m2])
        
        self.assertEqual(p1 + p1, Polynomial([ Monomial(4, {"a":3, "b":2}) ]))
        self.assertEqual(p1 - p1, Polynomial([ ]))
        self.assertEqual(p1 + p2, Polynomial([m2, m1]))
        p1 += p2
        self.assertEqual(p1 - p2, Polynomial([m1]))
        self.assertEqual(p2 - p1, Polynomial([ m1*-1 ]))

    def test_polynomial_mul(self):
        m1 = Monomial(2, {"a":3, "b":2})
        m2 = Monomial(3, {"b":3, "c":1})
        p1 = Polynomial([m1])
        p2 = Polynomial([m2])

        self.assertEqual((p1 - p2) * (p1 + p2), Polynomial([ m1 * m1, m2 * m2 * Monomial(-1,{}) ]) )
        p3 = p1 + p2
        self.assertEqual( (p3 + p1) * p3, Polynomial([ m1*m1*2, m1*m2*3, m2*m2]))

if __name__ == '__main__':
    unittest.main()