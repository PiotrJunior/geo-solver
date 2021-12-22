from __future__ import annotations
from copy import copy
from typing import Dict, List, Union

class Monomial:
    """ Monomial class
    """
    def __init__(self, factor = 0, terms = None) -> None:
        if isinstance(terms, dict):
            self.factor = factor
            self.terms = terms.copy()
        elif isinstance(terms, str):
            self.factor = factor
            self.terms = {terms: 1}        
        elif terms is None:
            if isinstance(factor, dict):
                self.factor = 1
                self.terms = factor.copy()
            elif isinstance(factor, str):
                self.factor = 1
                self.terms = {factor:1}
            elif isinstance(factor, (int, float)):
                self.factor = factor
                self.terms = {}
            else:
                raise Exception("Wrong arguments")
        else:
            raise Exception("Wrong arguments")    
    
    def __str__(self) -> str:
        return str(self.factor) + "".join([str(var)+"^"+str(power) for var, power in self.terms.items()])

    def __mul__(self, other : Union[Monomial, int, float]) -> Monomial:
        if not isinstance(other, Monomial):
            other = Monomial(other)
        factor = self.factor * other.factor
        terms = self.terms.copy()
        for var, power in other.terms.items():
            if var in terms:
                terms[var] += power
            else:
                terms[var] = power
            if terms[var] == 0:
                terms.pop(var)
        return Monomial(factor, terms)
    
    def __add__(self, other : Monomial) -> Monomial:
        if not isinstance(other, Monomial):
            other = Monomial(other)
        if self.terms != other.terms:
            raise Exception("Monomials with diffrent terms")
        return Monomial(self.factor + other.factor, self.terms)
    
    def __sub__(self, other : Monomial) -> Monomial:
        if not isinstance(other, Monomial):
            other = Monomial(other)
        if self.terms != other.terms:
            raise Exception("Monomials with diffrent terms")
        return Monomial(self.factor - other.factor, self.terms)
    
    def __eq__(self, other : Monomial) -> bool:
        if not isinstance(other, Monomial):
            other = Monomial(other)
        return self.terms == other.terms
    
    def same(self, other : Monomial) -> bool:
        """Checks if Monomials are the same including factor

        Args:
            other (Monomial): Monomial to check

        Returns:
            bool: True when are the same
        """
        if not isinstance(other, Monomial):
            other = Monomial(other)
        return self.terms == other.terms and self.factor == other.factor

    __rmul__ = __mul__
    __radd__ = __add__
    __rsub__ = __sub__
    __req__ = __eq__

class Polynomial:
    def __init__(self, terms : List[Monomial] = []) -> None:
        if isinstance(terms, list):
            self.terms = [x if isinstance else Monomial(x) for x in terms]
        elif isinstance(terms, Monomial):
            self.terms = [terms]
        else:
            self.terms = [Monomial(terms)]

    def degree(self) -> int:
        """Returns degree (number of elements) of Polynomial

        Returns:
            int: degree of Polynomial
        """
        return len(self.terms)

    def __str__(self) -> str:
        return " + ".join([str(term) for term in self.terms])

    def __add__(self, other : Polynomial) -> Polynomial:
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        terms = self.terms.copy()
        for term in other.terms:
            if term in terms:
                terms[terms.index(term)] += term
                # index = terms.index(term)
                # if terms[index] == Monomial():
                    # terms.pop(index) 
            else:
                terms.append(term)

        return Polynomial(list(filter( lambda term : term.factor != 0, terms )))
    
    def __sub__(self, other : Polynomial) -> Polynomial:
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        terms = self.terms.copy()
        for term in other.terms:
            if term in terms:
                terms[terms.index(term)] -= term
                # index = terms.index(term)
                # if terms[index] == Monomial():
                #     terms.pop(index) 
            else:
                terms.append(term*-1)

        return Polynomial(list(filter( lambda term : term.factor !=0, terms )))

    def __mul__(self, other : Polynomial) -> Polynomial:
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        poly = Polynomial()
        for term1 in self.terms:
            for term2 in other.terms:
                poly += Polynomial([term1*term2])

        return poly

    def __truediv__(self, other : Polynomial) -> Rational:
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        return Rational(self, other)

    def __rtruediv__(self, other : Polynomial) -> Rational:
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        return Rational(other, self)

    def __eq__(self, other : Polynomial) -> bool:
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        if self.degree() != other.degree():
            return False
        
        for term in other.terms:
            if term not in self.terms or self.terms[self.terms.index(term)].factor != term.factor:
                    return False
        return True
        
    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__
    __req__ = __eq__

class Rational:
    def __init__(self, numerator : Polynomial, denominator : Polynomial = 1) -> None:
        """Init Rational function (Polynomial divided by Polynomial)

        Args:
            numerator (Polynomial): numerator of this Rational function
            denominator (Polynomial): denominator of this Rational function
        """
        if isinstance(numerator, Polynomial):
            self.numerator = copy(numerator)
        else:
            self.numerator = Polynomial(numerator)
            
        if isinstance(denominator, Polynomial):
            self.denominator = copy(denominator)
        else:
            self.denominator = Polynomial(denominator)

    def __str__(self) -> str:
        num = str(self.numerator)
        den = str(self.denominator)
        return num + "\n" + "-" * max(len(num), len(den)) + "\n" + den
    
    def __mul__(self, other : Rational) -> Rational:
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )
    
    def __truediv__(self, other : Rational) -> Rational:
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )

    def __rtruediv__(self, other : Rational) -> Rational:
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational(
            other.numerator   * self.denominator,
            other.denominator * self.numerator
        )

    def __add__(self, other : Rational) -> Rational:
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational(
            self.numerator * other.denominator + self.denominator * other.numerator,
            self.denominator * other.denominator
        )

    def __sub__(self, other : Rational) -> Rational:
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational(
            self.numerator * other.denominator - self.denominator * other.numerator,
            self.denominator * other.denominator
        )

    def __eq__(self, other : Rational) -> bool:
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.numerator * other.denominator == self.denominator * other.numerator

    __rmul__ = __mul__
    __radd__ = __add__
    __rsub__ = __sub__
    __req__ = __eq__
    
# a = Rational( Polynomial([Monomial(1, {"a":1})]), Polynomial([Monomial(1, {})]) )
# b = Rational( Polynomial([Monomial(1, {"b":1})]), Polynomial([Monomial(1, {})]) )
# a = Polynomial([ Monomial(1, {"a":1}) ])
# b = Polynomial([ Monomial(1, {"b":1}) ])
# mono2 = Monomial(3, {"c":2, "b":3, "d":-2})
# c = b + b
# print(c + b)