
from charm.schemes.pkenc.pkenc_paillier99 import Pai99
from charm.toolbox.integergroup import RSAGroup, lcm, gcd, integer, toInt
import random
import os
group = RSAGroup()
pai = Pai99(group)


public_key, private_key = pai.keygen()
n = public_key['n']
g = public_key['g']
n2 = public_key['n2']
lamda = private_key['lamda']
l = gcd(pai.L(((g % n2) ** lamda), n), n)
t0 = group.random(n)
k = group.random(n)
skp1 = group.random(n)
skp2 = group.random(n)
skp = skp1 + skp2

h = pow(g, skp, n2)

# SE.GenKey
kse = os.urandom(32).hex()
kkw = os.urandom(32).hex()
with open('key/public_key.txt', 'w+') as f:
    f.write("h = " + str(toInt(h)) + '\n')
    f.write("g = " + str(toInt(g)) + '\n')
    f.write("n = " + str(toInt(n)) + '\n')

with open('key/IOTgateway_key.txt', 'w+') as f:
    f.write("kse = " + f"\"{str(kse)}\"" + '\n')
    f.write("kkw = " + f"\"{str(kkw)}\"" + '\n')
    f.write("t0 = " + str(toInt(t0)) + '\n')
    f.write("k = " + str(toInt(k)) + '\n')

with open('key/CloudServerSA_key.txt', 'w+') as f:
    f.write("skp1 = " + str(toInt(skp1)) + '\n')
    f.write("t0 = " + str(toInt(t0)) + '\n')

with open('key/CloudServerSB_key.txt', 'w+') as f:
    f.write("skp2 = " + str(toInt(skp2)) + '\n')

with open('key/DataUser_key.txt', 'w+') as f:
    f.write("kse = " + f"\"{str(kse)}\"" + '\n')
    f.write("k = " + str(toInt(k)) + '\n')
