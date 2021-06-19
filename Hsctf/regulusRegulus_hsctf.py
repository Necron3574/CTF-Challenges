import numpy as np
import sympy
from Crypto.Util.number import long_to_bytes,inverse
from pwn import *
import math
ans_list = []

def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

def lcm(p, q):
    return p * q // gcd(p, q)


r = remote("regulus-regulus.hsc.tf",1337)
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
r.sendline("2")
x = r.recvline().decode().strip()
n = x.split("= ")[1]
n = int(n)
e = 65537
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
r.sendline("3")
d = r.recvline().decode().strip()
d = d.split("= ")[1]
d = int(d)
kphi = e*d-1
# https://crypto.stackexchange.com/questions/13113/how-can-i-find-the-prime-numbers-used-in-rsa
for g in range(1,10):
    p = math.gcd(n, pow(g, (kphi // 2 ** 3), n) - 1)
    if p != n:
        break
q = n//p
assert p*q == n
lamb = lcm(p-1,q-1)
d = inverse(e,lamb)
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
r.sendline("4")
print(r.recvline())
r.sendline(str(d))
print(r.recvline())
print(r.recvline().decode())
