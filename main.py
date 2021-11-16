class Monomial:
    def __init__(self, factor, terms):
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
    pass

mono1 = Monomial(3, {"a":4, "b":1, "d":2})
mono2 = Monomial(3, {"c":2, "b":3, "d":-2})
print(mono1*mono2)