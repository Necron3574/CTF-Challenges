from Crypto.Util.number import long_to_bytes,inverse
from pwn import *

def solve(n):
    n = int(n)
    ans = 0
    for i in range(0,n+1):
        ans += S[i]
    return str(ans%pow(10,10))

F = [4,5]
for i in range(2,1001):
    F.append(F[i-1]+F[i-2])
S = [4]
for i in range(1,1001):
    S.append(S[i-1] + F[i])


r = remote("extended-fibonacci-sequence-2.hsc.tf",1337)
print(r.recvline())
for _ in range(100):
    print(r.recvline())
    print(r.recvline())
    x = r.recvline().decode().strip()
    print(x)
    r.sendline(solve(x))
    print(r.recvline())
