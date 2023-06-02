
# from charm.schemes.pkenc.pkenc_paillier99 import Pai99
# from charm.toolbox.integergroup import RSAGroup, lcm, gcd, integer, toInt
import random
import os
# group = RSAGroup()
# pai = Pai99(group)
# public_key, private_key = pai.keygen()
from Crypto.Util.number import getPrime

p = getPrime(1024)
q = getPrime(1024)
n = p * q
n2 = n * n
g = random.randint(1, n - 1)
# n2 = public_key['n2']
# lamda = private_key['lamda']
# l = gcd(pai.L(((g % n2) ** lamda), n), n)
t0 = random.randint(1, n - 1)
k = random.randint(1, n - 1)
while True:
    skp1 = random.randint(1, n - 1)
    skp2 = random.randint(1, n - 1)
    skp = skp1 + skp2
    if 1 <= skp < n:
        break

h = pow(g, skp, n)

# SE.GenKey
kse = random.randbytes(32).hex()
kkw = random.randbytes(32).hex()
iv = random.randbytes(16).hex()
with open('key/public_key.txt', 'w+') as f:
    f.write("h = " + str(h) + '\n')
    f.write("g = " + str(g) + '\n')
    f.write("n = " + str(n) + '\n')

with open('key/IOTgateway_key.txt', 'w+') as f:
    f.write("kse = " + f"\"{kse + iv}\"" + '\n')
    f.write("kkw = " + f"\"{kkw + iv}\"" + '\n')
    f.write("t0 = " + str(t0) + '\n')
    f.write("k = " + str(k) + '\n')

with open('key/CloudServerSA_key.txt', 'w+') as f:
    f.write("skp1 = " + str(skp1) + '\n')
    f.write("t0 = " + str(t0) + '\n')

with open('key/CloudServerSB_key.txt', 'w+') as f:
    f.write("skp2 = " + str(skp2) + '\n')

with open('key/DataUser_key.txt', 'w+') as f:
    f.write("kse = " + f"\"{kse + iv}\"" + '\n')
    f.write("k = " + str(k) + '\n')
