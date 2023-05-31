from middlewares.SE import SE
import os
kkw = ""
kse = ""
with open('key/IOTgateway_key.txt', 'r') as f:
    data = f.read()
    exec(data)
print(k)
with open('DataSet/PHI.csv', 'r') as f:
    print(f.readlines()[1].strip().split(','))
kkw = bytes.fromhex(kkw)
kse = bytes.fromhex(kse)
iv = os.urandom(16)
SE = SE(iv, kse)
