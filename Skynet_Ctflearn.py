import math
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

e = 65537

c1 = 5024836662627906750454817701922271080214720765897113783786369197810770999608528443597447448508876214100063962982376037712548944474807897847869334582773452689962992522987755069402952836848501053684233233850594080254869
n1 = 10603199174122839808738169357706062732533966731323858892743816728206914395320609331466257631096646511986506501272036007668358071304364156150345138983648630874220488837685118753574424686204595981514561343227316297317899

c2 = 130884437483098301339042672379318680582507704056215246672305503902799253294397268030727540524911640778691710963573363763216872030631281953772411963153320471648783848323158455504315739311667392161460121273259241311534
n2 = 5613358668671613665566510382994441407219432062998832523305840186970780370368271618683122274081615792349154210168307159475914213081021759597948038689876676892007399580995868266543309872185843728429426430822156211839073

c3 = 40136988332296795741662524458025734893351353026652568277369126873536130787573840288544348201399567767278683800132245661707440297299339161485942455489387697524794283615358478900857853907316854396647838513117062760230880
n3 = 43197226819995414250880489055413585390503681019180594772781599842207471693041753129885439403306011423063922105541557658194092177558145184151460920732675652134876335722840331008185551706229533179802997366680787866083523
p = math.gcd(n1,n2)
n = n1
q = n//p
phi = (p-1)*(q-1)
d = modinv(e,phi)
c = c1
pt = hex(pow(c,d,n))[2:]
flag = bytes.fromhex(pt)
print(flag)