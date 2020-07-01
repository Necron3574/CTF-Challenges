import hashlib
passhash = '9326ea0931baf5786cde7f280f965ebb'
with open('titanic.txt') as fp:
    text = fp.readlines()
    for line in text:
        for word in line.split():
            word = word.lower()
            m = hashlib.md5(("tjctf{"+ str(word) +"}").encode())
            hash = m.hexdigest()
            if hash == passhash:
                print('tgctf{' + word + '}')
                break
