
from charm.schemes.pkenc.pkenc_paillier99 import Pai99
from charm.toolbox.integergroup import RSAGroup, lcm, gcd, i
import random
import os
group = RSAGroup()
pai = Pai99(group)


public_key, private_key = pai.keygen()
n = public_key['n']
r = group.random(n)
g = public_key['g']
n2 = public_key['n2']
lamda = private_key['lamda']
l = gcd(pai.L(((g % n2) ** lamda), n), n)


t0 = group.random(n)
print(type(t0))
k = group.random(n)
while True:
    skp1 = group.random(n)
    skp2 = group.random(n)
    skp = skp1 + skp2
    if integer.Element(1) <= skp < n:
        break
h = pow(g, skp, n2)
print(type(h))
public_key = (h, r, g, n)

# SE.GenKey
kse = os.urandom(32).hex()
kkw = os.urandom(32).hex()
with open('key/public_key.txt', 'w+') as f:
    f.write("h = " + str(h) + '\n')
    f.write("r = " + str(r) + '\n')
    f.write("g = " + str(g) + '\n')
    f.write("n = " + str(n) + '\n')

with open('key/IOTgateway_key.txt', 'w+') as f:
    f.write("kse = " + f"\"{str(kse)}\"" + '\n')
    f.write("kkw = " + f"\"{str(kkw)}\"" + '\n')
    f.write("t0 = " + str(t0) + '\n')
    f.write("k = " + str(k) + '\n')

with open('key/CloudServerSA_key.txt', 'w+') as f:
    f.write("skp1 = " + str(skp1) + '\n')
    f.write("t0 = " + str(t0) + '\n')

with open('key/CloudServerSB_key.txt', 'w+') as f:
    f.write("skp2 = " + str(skp2) + '\n')

with open('key/DataUser_key.txt', 'w+') as f:
    f.write("kse = " + f"\"{str(kse)}\"" + '\n')
    f.write("k = " + str(k) + '\n')
