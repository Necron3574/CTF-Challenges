import owiener
import random
import math
from sympy.ntheory import isprime
from sympy.functions.elementary.miscellaneous import cbrt
from sympy.ntheory.modular import crt
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long
import itertools

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(
            lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

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
n = int('97f0c4ccd9034b2e78e4256744363a32f9d8dee4fd02a5ef51ac0b8ef3f1929185be33598175190d7cf877e38cfa4234c028ad1bfa8a2b200b3410915781f515fd37d8c17833cdc365abaff667a40d16131edd64737ca35c68240caadbc31ff9da82b5cf38c3a5d2f7e7ed031ab09532e33a5141a6c142e4b7da70925b5a43b0a72bf983f2bf7f9310af62bb0e75729f1bba1ae8cf23989d8583c288df42bb04d2c1427ac711dfa093d71b7993b610f7c282979104892937f9bec02695785e0c86f1c0a8eed663c1d61a758e5d3bd7b3fb37f3fd7c9de559a62eac6fe5f37796d2dcc5c5e8b0189e9b0f16d95943091e7f48acbfe7c86d17a1081c4e39730e73',16)
e = 3
c = 7066919547636927507340244980094441424652812132317123226789924190494418446384500967980775724696257320410126401360145190228517523562073969106827568659819816530496060643476009851183045587650538954355540092746001144312867817846857566386147074801786496749841635139806005044997156719129545054438596521461689676434989816885186717181220084060907946166257922590617003871064785732650203927258614003414192801276164868015364259622040193061019581208620710288243126010440233152181147585951639865486778861815579561811563637785803978075803528971478549257695495753142142829789867465227764583649219781349653999788144130034037116997731

for i in range(100000):
    p = find_root(c + i*n,3)
    p = long_to_bytes(p)
    if b'zh3r0{' in p:
        print(p)
        break
    else:
        print('fail',i)
