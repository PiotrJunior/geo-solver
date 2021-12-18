from copy import copy

class Monomial:
    def __init__(self, factor = 0, terms = {}):
        self.factor = factor
        self.terms = terms.copy()
    
    def __str__(self):
        return str(self.factor) + "".join([str(var)+"^"+str(power) for var, power in self.terms.items()])

    def __mul__(self, other):
        if isinstance(other, int):
            tmp = copy(self)
            tmp.factor *= other
            return tmp
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

    def __add__(self, other):
        if self.terms != other.terms:
            raise Exception("Monomials with diffrent terms")
        return Monomial(self.factor + other.factor, self.terms)

    def __sub__(self, other):
        if self.terms != other.terms:
            raise Exception("Monomials with diffrent terms")
        return Monomial(self.factor - other.factor, self.terms)

    def __eq__(self, other):
        return self.terms == other.terms
    
    def same(self, other):
        return self.terms == other.terms and self.factor == other.factor

class Polynomial:
    def __init__(self, terms = []):
        self.terms = terms.copy()

    def degree(self):
        return len(self.terms)

    def __str__(self):
        return " + ".join([str(term) for term in self.terms])

    def __add__(self, other):
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

    def __sub__(self, other):
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

    def __mul__(self, other):
        poly = Polynomial()
        for term1 in self.terms:
            for term2 in other.terms:
                poly += Polynomial([term1*term2])

        return poly

    def __div__(self, other):
        return Rational(self, other)

    def __eq__(self, other):
        if self.degree() != other.degree():
            return False
        
        for term in other.terms:
            if term not in self.terms or self.terms[self.terms.index(term)].factor != term.factor:
                    return False
        return True
        

class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = copy(numerator)
        self.denominator = copy(denominator)

    def __str__(self):
        num = str(self.numerator)
        den = str(self.denominator)
        return num + "\n" + "-" * max(len(num), len(den)) + "\n" + den
    
    def __mul__(self, other):
        return Rational(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __div__(self, other):
        return Rational(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )

    def __add__(self, other):
        return Rational(
            self.numerator * other.denominator + self.denominator * other.numerator,
            self.denominator * other.denominator
        )

    def __sub__(self, other):
        return Rational(
            self.numerator * other.denominator - self.denominator * other.numerator,
            self.denominator * other.denominator
        )

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator


# a = Rational( Polynomial([Monomial(1, {"a":1})]), Polynomial([Monomial(1, {})]) )
# b = Rational( Polynomial([Monomial(1, {"b":1})]), Polynomial([Monomial(1, {})]) )
# a = Polynomial([ Monomial(1, {"a":1}) ])
# b = Polynomial([ Monomial(1, {"b":1}) ])
# mono2 = Monomial(3, {"c":2, "b":3, "d":-2})
# c = b + b
# print(c + b)