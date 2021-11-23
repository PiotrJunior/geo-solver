class Monomial:
    def __init__(self, factor = 0, terms = {}):
        self.factor = factor
        self.terms = terms
    
    def __str__(self):
        return str(self.factor) + "".join([str(var)+"^"+str(power) for var, power in self.terms.items()])

    def __mul__(self, other):
        factor = self.factor * other.factor
        terms = self.terms
        for var, power in other.terms.items():
            if var in terms:
                terms[var] += power
            else:
                terms[var] = power
            if terms[var] == 0:
                terms.pop(var)
        return Monomial(factor, terms)



class Polynomial:
    def __init__(self, terms = []):
        self.terms = terms

    def degree(self):
        return len(self.terms)

    def __str__(self):
        return " + ".join([str(term) for term in self.terms])

    def __add__(self, other):
        terms = self.terms
        for term in other.terms:
            if term in terms:
                index = terms.index(term)
                terms[index] += term
                if terms[index] == Monomial():
                    terms.pop(index) 
            else:
                terms.append(term)

        return Polynomial(terms)

    def __sub__(self, other):
        terms = self.terms
        for term in other.terms:
            if term in terms:
                index = terms.index(term)
                terms[index] -= term
                if terms[index] == Monomial():
                    terms.pop(index) 
            else:
                terms.append(-term)

        return Polynomial(terms)

    def __mul__(self, other):
        poly = Polynomial()
        for term1 in self.terms:
            for term2 in other.terms:
                poly += term1*term2

        return poly

    def __div__(self, other):
        return Rational(self, other)

    def __eq__(self, other):
        if self.degree != other.degree:
            return False
        
        for term in other.terms:
            if term not in self.terms:
                return False
        return True
        

class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

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


mono1 = Monomial(3, {"a":4, "b":1, "d":2})
mono2 = Monomial(3, {"c":2, "b":3, "d":-2})
print(mono1*mono2)