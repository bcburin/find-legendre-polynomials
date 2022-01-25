from math import gcd

class Fraction:

    def __init__(self, numerator, denominator = 1):
        # Find numerator and denominator if either input is not integer
        if (not isinstance(numerator, int)):
            while (not float.is_integer(numerator)):
                numerator *= 10;
                denominator *= 10;

        # Find greatest common divisor
        divisor = gcd(int(numerator), int(denominator));

        # Store sign information on numerator
        if (denominator < 0):
            denominator = -denominator;
            numerator = -numerator;

        # Set properties
        self.numerator = int(numerator / divisor);
        self.denominator = int(denominator / divisor);
        

    # Implement multiplication of fractions
    def __mul__(self, other):
        num = self.numerator * other.numerator;
        den = self.denominator * other.denominator;

        return Fraction(num, den);


    # Implement sum of fractions
    def __add__(self, other):
        num = self.numerator * other.denominator + self.denominator * other.numerator;
        den = self.denominator * other.denominator;
        
        return Fraction(num, den);


    # Implement difference of fractions
    def __sub__(self, other):
        return ( self + (-other) );


    # Implement division of fractions
    def __truediv__(self,other):
        return self * other.inverse();


    # Find negative of fraction
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator);

    
    # Override __str__
    def __str__(self):
        if (self.denominator == 1):
            return f'{self.numerator}';
        
        return f'{self.numerator}/{self.denominator}';


    # Find inverse of fraction
    def inverse(self):
        return Fraction(self.denominator, self.numerator);

    
    # Determine whether fraction is negative
    def is_negative(self):
        return self.numerator < 0;

    
    # Determine whether fraction is positive
    def is_positive(self):
        return self.numerator > 0;