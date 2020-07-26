plaintext = 'GOOGLE'
ciphertext = ''
for i in plaintext:
    ciphertext += chr(((ord(i)*21) +11) % 26)
print(ciphertext)
