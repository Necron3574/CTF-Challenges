# Mein Kampf
## Description
```
We have intercepted the enemy's communications, but unfortunately, some data was corrupted during transmission.
Can you recover the message?
M4 UKW $ Gamma 2 4 $ 5 9 $ 14 3 $ 5 20 fv cd hu ik es op yl wq jm
Ciphertext: zkrtwvvvnrkulxhoywoj (Words in the flag are separated by underscores)
```
## Solution
On googling the title we find out that `Mein Kampf` is a book written by Adolf Hitler.
So we can make a fair assumption that it uses the enigma cipher.
Now there is some data given to us but finding the right site to decode is a problem.
I spent a long time trying to decode it using a Bombe machine on Cyberchef but to no avail.
Finally I came across this site `https://cryptii.com/pipes/enigma-machine` which was perfect.
We can enter almost all the data.
What we are missing are the 3 rotor values.
But since there can be only 8 positions for a rotor it leads to a total of 8*8*8 = 512 possibilities.
This implies bruteforce.
However by manually bruteforcing we can get the flag quickly enough for the positions:
```
Rotor1 = 1
Rotor2 = 4
Rotor3 = 7
```
