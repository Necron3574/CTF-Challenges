from Crypto.Util.number import long_to_bytes, inverse
key1 = int('5dcec311ab1a88ff66b69ef46d4aba1aee814fe00a4342055c146533',16)
w = int('9a13ea39f27a12000e083a860f1bd26e4a126e68965cc48bee3fa11b',16)
key3 = key1^w
x = int('996e59a867c171397fc8342b5f9a61d90bda51403ff6326303cb865a',16)
key4 = key3^x
y = int('7b33428eb14e4b54f2f4a3acaeab1c2733e4ab6bebc68436177128eb',16)
temp = y^key1
key5 = temp^key4
z = int('557ce6335808f3b812ce31c7230ddea9fb32bbaeaf8f0d4a540b4f05',16)
temp = z^key5
key2 = temp^key3
enc = int('306d34c5b6dda0f53c7a0f5a2ce4596cfea5ecb676169dd7d5931139',16)
flag = enc ^ key1^ key2^ key3^ key4^ key5
print(long_to_bytes(flag))
#flag = flag{n0t_t00_h4rD_h0p3fully}
