from polynomial import Polynomial
from math import factorial

def legendre_polynomial(n):
    # return (Polynomial(-1,0,1) ** n).derivative(n) * ( 1/(2**n * factorial(n)) );
    return (Polynomial(-1,0,1) ** n).derivative(n) // (2** n * factorial(n));

for order in range(10):
    print(f'LP({order}): ', legendre_polynomial(order), '\n');