from fraction import Fraction
from itertools import zip_longest

class Polynomial:

    @staticmethod
    def monomial(degree):
        coefs = [0]*(degree+1);
        coefs[-1] = 1;
        return Polynomial(*coefs);


    def __init__(self, *coefs):
        # Ingnore null high order terms
        while (len(coefs) != 1 and coefs[-1] == 0):
            coefs = coefs[:-1];

        # Use fraction objects as coefficients
        self.coefs = [Fraction(coef) for coef in coefs];

        # Determine degree of polynomial
        self.degree = len(coefs) - 1;

        # Check for null polynomial
        if (len(coefs) == 1 and coefs[0] == 0):
            self.degree = -1;


    # Implement polynomial addition
    def __add__(self, other):
        sum_coefs = [];
        for coef1,coef2 in zip_longest(self.coefs, other.coefs, fillvalue=Fraction(0)):
            sum_coefs.append(coef1 + coef2);

        return Polynomial(*sum_coefs);


    # Implement polynomial multiplication
    def __mul__(self, other):
        # Check if other input is not a polynomial
        if (not isinstance(other, Polynomial)):
            prod_coefs = [Fraction(other)*coef for coef in self.coefs];
            return Polynomial(*prod_coefs);

        # Check if either input is the null polynomial
        if (self.degree == -1 or other.degree == -1):
            return Polynomial(0);

        # Find degree of resulting polynomial
        prod_degree = self.degree + other.degree;
        prod_coefs = [Fraction(0)]*(prod_degree+1);

        # Compute polynomial
        for exp1,coef1 in enumerate(self.coefs):
            for exp2,coef2 in enumerate(other.coefs):
                prod_coefs[exp1+exp2] += coef1 * coef2;

        return Polynomial(*prod_coefs);


    # Implement polynomial subtraction
    def __sub__(self, other):
        return self + (-other);


    # Implement polynomial division
    # Returns both quotient and remainder (operator /)
    def __truediv__(n, d):
        if (d.degree == -1): return None;

        q = Polynomial(0);
        r = n;

        while(r.degree != -1 and r.degree >= d.degree ):
            t = Polynomial.monomial(r.degree - d.degree) * ( r.lead()/d.lead() );
            q = q + t;
            r = r - t * d;

        return (q,r);


    # Returns quotient (operator //)
    def __floordiv__(n, d):
        q,r = n/d;
        return q;


    # Returns remainder (operator %)
    def __mod__(n, d):
        q,r = n/d;
        return r;

    # Return negative of polynomial
    def __neg__(self):
        return self * (-1);


    # Return leading coefficient of polynomial
    def lead(self):
        return self.coefs[self.degree];


    # Return derivative of polynomial
    # Private method! ( see derivative() )
    def _derivative(self):
        # Derivative of constant polynomial is the null polynomial
        if (len(self.coefs) == 1): return Polynomial(0);

        # Compute derivative
        der_coefs = [self.coefs[exp]*exp for exp in range(1,self.degree+1)];
        return Polynomial(*der_coefs);

    
    # Return nth derivative of polynomial
    def derivative(self,n=1):
        der = self;
        for order in range(n):
            der = der._derivative();
        return der;
    
    # Override __str__ method
    def __str__(self):
        s = '';
        for exp, coef in enumerate(self.coefs):
            if (exp == 0):
                s += f'{coef}';
            else:
                if coef.is_positive():
                    s += f' + {coef if coef != 1 else ""}x^{exp}'
                elif coef.is_negative():
                    s += f' - {-coef if coef != -1 else ""}x^{exp}'
                else:
                    s += '';
        return s;