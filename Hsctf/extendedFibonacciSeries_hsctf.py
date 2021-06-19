from pwn import *

def solve(n):
    n = int(n)
    ans = 0
    for i in range(1,n+1):
        ans += S[i]
    return str(int(str(ans)[-11:]))

F = [0,1]
for i in range(2,1001):
    F.append(F[i-1]+F[i-2])
S = [""]
for i in range(1,1001):
    S.append(int(str(str(S[i-1])+str(F[i]))[-11:]))

r = remote("extended-fibonacci-sequence.hsc.tf",1337)
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
    r.sendline(solve(x))
