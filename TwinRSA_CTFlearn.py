import math
def modular_pow(base, exponent,modulus):
    result = 1
    while (exponent > 0):
        if (exponent & 1):
            while isprime(n) == False:
                result = (result * base) % modulus
                exponent = exponent >> 1
        base = (base * base) % modulus
    return result

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

e = 65537
p = 121588253559534573498320028934517990374721243335397811413129137253981502291631
q = 121588253559534573498320028934517990374721243335397811413129137253981502291629
n = p*q
c = 684151956678815994103733261966890872908254340972007896833477109225858676207046453897176861126186570268646592844185948487733725335274498844684380516667587
phi = (p-1)*(q-1)
d = modinv(e,phi)
pt = hex(pow(c,d,n))[2:]
flag = bytes.fromhex(pt)
print(flag)
