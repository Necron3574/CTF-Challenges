# Little RSA
## Description
```
The flag.zip contains the flag I am looking for but it is password protected.
The password is the encrypted message which has to be correctly decrypted so I can use it to open the zip file.
I tried using RSA but the zip doesn't open by it. Can you help me get the flag please?
```
## Solution
So this challenge was even easier than the previous rsa challenge.
We are given a text file and password protected zip file.
The question hints that the password of the zip file is encrypted using rsa.
Now the text file had this given.
```
c=32949
n=64741
e=42667
```
Yup. We can quickly factorize the modulus.
We get a factor `101`
And with this we can quickly decrypt it.
Here's a small code to decrypt.
```python
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

c = 32949
n = 64741
e = 42667
p = 101
q = n//p
phi = (p-1)*(q-1)
d = modinv(e,phi)
pin = pow(c,d,n)
print(pin)
```
With this we can decrypt the RSA ciphertext and get the pin `18429`
We can enter this password to unlock the zip file and get the flag.  
