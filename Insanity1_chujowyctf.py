from pwn import *

def solver(i):
    r = remote('insanity1.chujowyc.tf',4004)
    r.recvline()
    # Cuz 2+2 = 4
    r.sendline('4')
    r.recvline()
    #Bruteforce
    r.sendline(str(i))
    x = r.recvline()
    if b'Invalid' in x:
        return None
    else:
        #since we run this on the mode debug we can find the number 42123 in the censored part of the question
        r.sendline('42123')
        r.recvuntil(': ')
        k = str(r.recvuntil('}'))
        return k
for i in range(81,100):
    if solver(i) != None:
        print(solver(i))
        break
