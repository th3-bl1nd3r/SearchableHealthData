from middlewares.AES_CBC_256 import SE
from middlewares.ModifiedPaillier import E
from middlewares.HMAC_SHA_256 import hmac_sha256, int_to_bytes
import hashlib
import hmac
import os
from time import time
import random
import json
from base64 import b64encode
with open('key/IOTgateway_key.txt', 'r') as f:
    data = f.read()
    exec(data)
with open('key/public_key.txt', 'r') as f:
    data = f.read()
    exec(data)
# Modified Paillier Parameters
pk = {'n': n, 'h': h, 'g': g}

# print(d)
# Secure Symmetric Encryption Parameters
key = bytes.fromhex(kkw)
kkw, iv = key[0:32], key[32:]
key = bytes.fromhex(kse)
kse, iv = key[0:32], key[32:]


f = []
w = []
id = 1
fo = open('DataSet/SA.txt', 'w+')
with open('DataSet/PHI.csv', 'r') as fi:
    for fv in fi.readlines():
        w = [i.encode() for i in fv.strip().split(',')]
        fv = fv.strip().replace(',', '').encode()
        # Tv = str(time()).encode()
        Mac = hmac_sha256(k, fv)
        fvq = Mac + fv
        Cv = SE(iv, kse).Enc(fvq)
        Cw = [SE(iv, kkw).Enc(wi) for wi in w]
        # print(Cw)
        Ew = [E(pk, wi) for wi in w]
        # print(Ew)
        mac = hmac_sha256(t0, Cv + b','.join(Cw) +
                          b','.join(json.dumps(wi).encode() for wi in Ew))
        data = {'Cv': b64encode(Cv).decode(), 'Cw': b64encode(
            b','.join(Cw)).decode(), 'Ew': b64encode(b','.join(json.dumps(wi).encode() for wi in Ew)).decode(), 'id': id, 'mac': b64encode(mac).decode()}
        # print(data)
        fo.write(json.dumps(data) + '\n')
        # break
        # print(H)
        # if (id == 100):
        #     break
        print(id)
        id += 1
# print(w)
