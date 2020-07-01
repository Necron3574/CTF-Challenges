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

c_list = [309117097659990665453,
125675338953457551017,
524099092120785248852,
772538252438953530955,
547462544172248492882,
28215860448757441963,
543018082275730030658,
585936545563088067075,
131807465077304821584]
n = 783340156742833416191
e = 653
p = 28188776653
q = 27789079547
phi = (p-1)*(q-1)
d = modinv(e,phi)
flag = ''
for i in c_list:
    x = pow(i,d,n)
    x = hex(x)[2:]
    flag += str(bytes.fromhex(x))[2:-1]
print(flag)
