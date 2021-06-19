from Crypto.Util.number import long_to_bytes,inverse
from pwn import *
r = remote("not-really-math.hsc.tf",1337)
print(r.recvline())
check = 0
for _ in range(100):
    if check ==0:
        inp = r.recvline().decode().strip()
        check = 1
    else:
        inp = r.recvline().decode().strip()[2:]
    if 'flag' in inp:
        print(inp)
        break
    parsed_list = inp.split("m")
    added_list = []
    for i in parsed_list:
        if(len(i.split("a")) >1):
            added_list.append(eval(i.replace("a","+")))
        else:
            added_list.append(int(i))
    ans = 1
    for i in added_list:
        ans *= i
    ans = ans%(pow(2,32)-1)
    r.sendline(str(ans))
