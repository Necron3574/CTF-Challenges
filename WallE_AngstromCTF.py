import math
import random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, inverse , long_to_bytes
from gmpy2 import is_prime
from sympy.functions.elementary.miscellaneous import cbrt
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

def find_root(n, x):
    low = 0
    high = n
    while low < high:
        mid = (low+high)//2
        if mid**x < n:
            low = mid+1
        else:
            high = mid
    return low
n = 16930533490098193592341875268338741038205464836112117606904075086009220456281348541825239348922340771982668304609839919714900815429989903238980995651506801223966153299092163805895061846586943843402382398048697158458017696120659704031304155071717980681280735059759239823752407134078600922884956042774012460082427687595370305553669279649079979451317522908818275946004224509637278839696644435502488800296253302309479834551923862247827826150368412526870932677430329200284984145938907415715817446807045958350179492654072137889859861558737138356897740471740801040559205563042789209526133114839452676031855075611266153108409
e = 3
flag = 0
c = 11517346521350511968078082236628354270939363562359338628104189053516869171468429130280219507678669249746227256625771360798579618712012428887882896227522052222656646536694635021145269394726332158046739239080891813226092060005024523599517854343024406506186025829868533799026231811239816891319566880015622494533461653189752596749235331065273556793035000698955959016688177480102004337980417906733597189524580640648702223430440368954613314994218791688337730722144627325417358973332458080507250983131615055175113690064940592354460257487958530863702022217749857014952140922260404696268641696045086730674980684704510707326989
for i in range(87,1,-1):
    print('Trial' + str(i))
    flag_len = i
    pad_num = (255-flag_len)//2
    k = pow(modinv(256,n),e,n)
    k = pow(k,pad_num,n)
    ct = (c*k)%n
    for j in range(10000):
        ct += n
        pt = long_to_bytes(find_root(ct,3))
        if b'actf' in pt:
            print(pt)
            flag = 1
            break
        else:
            print('fail' + str(j))
    if  flag == 0:
        continue
    else:
        break