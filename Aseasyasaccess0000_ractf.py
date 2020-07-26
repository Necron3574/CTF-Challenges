from pwn import * # pip install pwntools
import json
import binascii
import base64
from Crypto.Util.number import long_to_bytes, bytes_to_long
import codecs
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from datetime import datetime, timedelta
from Crypto.Util.strxor import strxor
#Authentication message = access0000
token = '79e891e84814548d4555235328f0597b7d5a8932e4387aaa694d9fd4ce3abed3d37fa86d41032efb5045d7a4a669a228'
iv = bytes.fromhex(token[:32])
text = b'access=9999;expi'
forge_text = b'access=0000;expi'
xor1 = strxor(iv,text)
new_iv = strxor(xor1,forge_text).hex()
print('Admin token : ' + token[32:])
print("Iv : " + new_iv)
