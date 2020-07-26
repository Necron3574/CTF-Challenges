ciphertext = ":<M?TLH8<A:KFBG@V"
def decrypt(c,s):
    pt = ''
    for letter in c:
        pt += chr((ord(letter)-s) % 256)
    return pt
for i in range(0,256):
    print(decrypt(ciphertext,i))
