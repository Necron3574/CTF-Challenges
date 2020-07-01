import math

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(
            lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

def L_function(x,n):
    return (x-1)/n

def lcm(a,b):
    return (a*b) / gcd(a,b)

n = 99157116611790833573985267443453374677300242114595736901854871276546481648883
g = 99157116611790833573985267443453374677300242114595736901854871276546481648884
c = 2433283484328067719826123652791700922735828879195114568755579061061723786565164234075183183699826399799223318790711772573290060335232568738641793425546869
p = 310013024566643256138761337388255591613
q = n//p
phi = (p-1)*(q-1)
lamb = lcm(p-1,q-1)
print(lamb)
k = pow(g,lamb,n**2)
u = modinv(L_function(k,n),n)
pt = (L_function(pow(c,lamb,n**2),n)*u)%n
print(pt)
