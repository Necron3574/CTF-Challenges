import owiener
import random
import math
from sympy.ntheory import isprime
from sympy.functions.elementary.miscellaneous import cbrt


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(
            lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m
def isqrt(x):
    """Return the integer part of the square root of x, even for very
    large integer values."""
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    if x < 150:
        return int(math.sqrt(x))  # use math's sqrt() for small parameters
    n = int(x)
    if n <= 1:
        return n  # handle sqrt(0)==0, sqrt(1)==1
    # Make a high initial estimate of the result (a little lower is slower!!!)
    r = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        newr = (r + n // r) >> 1  # next estimate by Newton-Raphson
        if newr >= r:
            return r
        r = newr
p = 44351
q = 137370696435618856084640883863725908632926255318165893158765700616680079274963985171428773714164760798447183077465658673509223073433753577716568755079053649265075573722227228028635031799698592171154169008891314956421602527255138941882051723217781711550288699401820191708988922460107715393145752278596620233961
n = p*q
e = 65537
c = 1566821472759725457901201701165657719602053050183604743196947628170858485550874405228113585011960866504350789900176548218381744843161741052887544229514277326017496463058030444258507064384610036815238935892705092429078872543659698449206995428080321339931026550639287714262351249014403076522155120108225355860635486
phi = (p-1)*(q-1)
d = modinv(e,phi)
pt = hex(pow(c,d,n))[2:]
flag = bytes.fromhex(pt)
print(flag)
