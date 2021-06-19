from pwn import *

def solve(n):
    return F[int(n)+1]%10000

F = [0,1]
for i in range(2,1001):
    F.append(F[i-1]+F[i-2])

r = remote("hopscotch.hsc.tf",1337)
print(r.recvline())
check = 0
for _ in range(100):
    if check ==0:
        x = r.recvline().decode().strip()
        check = 1
    else:
        x = r.recvline().decode().strip()[2:]
    if 'flag' in x:
        print(x)
        break
    r.sendline(str(solve(x)))
