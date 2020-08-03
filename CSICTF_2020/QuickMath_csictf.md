# Quick Math
## Description
```
Ben has encrypted a message with the same value of 'e' for 3 public moduli - n1 = 86812553978993 n2 = 81744303091421 n3 = 83695120256591
and got the cipher texts - c1 = 8875674977048 c2 = 70744354709710 c3 = 29146719498409.
Find the original message. (Wrap it with csictf{})
```
## Solution
This challenge really had me going nuts.
On reading the challenge description I instantly thought that its some kind of hastads attack.
So I wrote a script for a regular Hastads broadcast for e = 3.
But that gave me some gibberish.
Later I got to know that plaintext was in hex format instead of the usual int format.
Hence `long_to_bytes(pt)` wouldnt work and we would have to do `bytes.fromhex(str(pt))`.
On doing that I got the flag easily enough.
Here's my script.

```python
import math
from sympy.ntheory.modular import crt
from Crypto.Util.number import bytes_to_long, inverse , long_to_bytes

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

n1 = 86812553978993
n2 = 81744303091421
n3 = 83695120256591
c1 = 8875674977048
c2 = 70744354709710
c3 = 29146719498409
m = [n1,n2,n3]
v = [c1,c2,c3]
N = n1*n2*n3
c = crt(m,v)
c = int(c[0])
pt = find_root(c,3)
flag = str(bytes.fromhex(str(pt)))[2:-1]
print('csictf{' + flag + '}')
```
