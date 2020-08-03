# MAFIA
## Description
```
The CTF Mafia wants to remove the competition (i.e.you) to again have monopoly over flags.
Bribe the Mafia to get away unscathed and with the flag.
nc chall.csivit.com 30721
Link to problem - https://ctf.csivit.com/files/35d2b6e2f6112189754d3bf18268aa22/prob.pdftoken=eyJ1c2VyX2lkIjoxMTczLCJ0ZWFtX2lkIjozMzAsImZpbGVfaWQiOjQ4NTJ9.Xxbjeg.h_wQbrfm8UWdJFtdN2aGbSy4aI4
```
## Solution
This was a very interesting challenge.
My idea behind this was to lower the range of potential people from 300 to something lesser and then binary search the amount of cash each person had.
But since we have only 1000 tries the code has to be very efficient so I decided to do it the lazy way.
So first I looped through all 300 people and checked for those who had money > 900000.
I added all those people to a list.
This according to me should be a small number of people.
On checking , the list had 35 potential people which is perfect.
So I binary searched all of them and submitted the highest result among all of them to get the flag.
Here's my code.(It can be more efficient but meh)

```python
import math
from pwn import *

def cash_finder(i,up,down):
    while True:
        mid = (up+down)//2
        r.sendline('1 '+ str(i) + ' ' + str(mid))
        x = r.recvline()
        if b'G' in x:
            down = mid
        elif b'L' in x:
            up = mid
        elif b'E' in x:
            return str(mid)

r = remote('chall.csivit.com',30721,level='debug')
highest = 1000000
list1 = []
for i in range(1,301):
    r.sendline('1 ' + str(i) + ' ' + str(900000))
    x = r.recvline()
    if 'G' in x:
        list1.append(i)
    elif b'L' in x:
        pass
    elif b'E' in c:
        pass
print(list1,len(list1))
highest_cash = 0
for i in list1:
    cash = int(cash_finder(i,1000000,900000))
    if cash > highest_cash:
        highest_cash = cash
r.sendline('2 ' + str(highest_cash))
print(r.recvline())
```
Note that this doesn't work all the time but more like 90% of the time.
Just rerun it incase it didn't work.
