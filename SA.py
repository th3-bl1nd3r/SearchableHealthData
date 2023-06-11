from middlewares.HMAC_SHA_256 import hmac_sha256, int_to_bytes
from middlewares.VariantBloomFilter import *
from pybloom import BloomFilter
from base64 import b64decode, b64encode
import json

VBF = BloomFilter(capacity=10000)
with open('key/CloudServerSA_key.txt', 'r') as f:
    data = f.read()
    exec(data)
with open('key/public_key.txt', 'r') as f:
    data = f.read()
    exec(data)
TBL = {}
EncodedFile = {}
label = 1
with open('DataSet/SA.txt', 'r') as fi:
    for data in fi.readlines():
        data = json.loads(data)
        # print(data)
        Cv = b64decode(data['Cv'])
        Cw = b64decode(data['Cw']).split(b', ')
        Ew = [json.loads(wi.replace(b". ", b", ").decode())
              for wi in b64decode(data['Ew']).replace(b", ", b". ").split(b',')]
        id = data['id']
        mac = b64decode(data['mac'])
        macq = hmac_sha256(t0, Cv + b', '.join(Cw) +
                           b','.join(json.dumps(wi).encode() for wi in Ew))
        assert (mac == macq)
        # pass
        # print(TBL)

        for i in range(len(Cw)):
            if (VBFVerify(VBF, b64encode(Cw[i]).decode()) == 1):
                TBL[b64encode(Cw[i]).decode()]['fileid'].append(id)
            else:
                TBL[b64encode(Cw[i]).decode()] = {}
                TBL[b64encode(Cw[i]).decode()]['keyword'] = Ew[i]
                TBL[b64encode(Cw[i]).decode()]['fileid'] = [id]
                VBFAdd(VBF, b64encode(Cw[i]).decode())
        # EncodedFile[id] =
        # if (label == 10):
        #     break
        # print(label)
        label += 1
with open('DataSet/TBL.txt', 'w+') as f:
    f.write(json.dumps(TBL))
