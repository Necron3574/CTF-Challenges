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

n=57772961349879658023983283615621490728299498090674385733830087914838280699121
e=65537
c=36913885366666102438288732953977798352561146298725524881805840497762448828130
p = 285934543893985722871321330457714807993
q = 202049603951664548551555274464815496697
phi = (p-1)*(q-1)
d = modinv(e,phi)
pt = pow(c,d,n)
print(long_to_bytes(pt))
