import math
import random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, inverse , long_to_bytes
from gmpy2 import is_prime
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

def find_root(n, x):
    low = 0
    high = n
    while low < high:
        mid = (low+high)//2
        if mid**x < n:
            low = mid+1
        else:
            high = mid
    return low
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
# a=p+q
# b =p-q
c = 41027546415588921135190519817388916847442693284567375482282571314638757544938653824671437300971782426302443281077457253827782026089649732942648771306702020
A = 1780602199528179468577178612383888301611753776788787799581979768613992169436352468580888042155360498830144442282937213247708372597613226926855391934953064
e = 65537
ct = 825531027337680366509171870396193970230179478931882005355846498785843598000659828635030935743236266080589740863128695174980645084614454653557872620514117
X = 2*A
Y = c//2
p = isqrt((X+Y)//2)
q = isqrt(pow(p,2)-(2*A))
n = p*q
phi = (p-1)*(q-1)
d = modinv(e,phi)
pt = long_to_bytes(pow(ct,d,n))
print(pt)
