from charm.toolbox.integergroup import RSAGroup
from charm.schemes.pkenc.pkenc_paillier99 import Pai99
group = RSAGroup()
pai = Pai99(group)
(public_key, secret_key) = pai.keygen()
msg_1 = 12345678987654321
msg_2 = 12345761234123409
msg_3 = msg_1 + msg_2
cipher_1 = pai.encrypt(public_key, msg_1)
cipher_2 = pai.encrypt(public_key, msg_2)
cipher_3 = cipher_1 + cipher_2
decrypted_msg_3 = pai.decrypt(public_key, secret_key, cipher_3)
print(decrypted_msg_3 == msg_3)
print(pai.decrypt(public_key, secret_key, cipher_1))
