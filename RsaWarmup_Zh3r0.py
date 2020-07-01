import owiener
import random
import math
from sympy.ntheory import isprime
from sympy.functions.elementary.miscellaneous import cbrt
from sympy.ntheory.modular import crt
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes
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
p = 2633312471
n = 250666113410842170852574328414199919235539292186662828449174991539286942679259596121827313853518698686043398764291343548300944262602003598926221580835156446443161898307815374988301812781895803769484991966337857756795698652210928286990907438232812487522677457962279594093051578672662718176669243944761445846315246433331
e = 65537
q = n//p
phi = (p-1)*(q-1)
d = modinv(e,phi)
c = 221559668604824761014585463452331631093765607112246141161677353784149281156511604352398458721638077822529077274613730136645684808777623306441642173603538608452830543457353659288530192373306921709480100012539200733938462278037837887237167502659113456541780715801735835227187706252935158343402506866175513543348812616820
print(long_to_bytes(pow(c,d,n)))
