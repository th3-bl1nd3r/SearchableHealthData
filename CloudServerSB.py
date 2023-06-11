import json
import socket
import threading
from traceback import print_exception
from middlewares.Conversion import *
from middlewares.ModifiedPaillier import *
from gmpy2 import *
with open('key/public_key.txt', 'r') as f:
    data = f.read()
    exec(data)
pk = {'n': mpz(n), 'h': mpz(h), 'g': mpz(g)}

with open('key/CloudServerSB_key.txt', 'r') as f:
    data = f.read()
    exec(data)


def recvuntilendl(client):
    res = b''
    while (True):
        ch = client.recv(1)
        if not ch:
            break
        if (ch == b'\n'):
            break
        res += ch
    return res


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen()
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target=self.listenToClient,
                             args=(client, address)).start()

    def listenToClient(self, client, address):
        size = 1024
        try:
            while True:
                data = recvuntilendl(client)
                if data:
                    # Set the response to echo back the recieved data
                    # print(data)
                    if (data.decode() == 'DataUser'):
                        data = recvuntilendl(client).decode()
                        data = json.loads(data)
                        sa = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
                        sa.connect(('localhost', 2808))  # Connect to SA
                        print(type(data))
                        if type(data) == type({}):
                            a = []
                            r = data['r']
                            Esw = data['Esw']
                            for i in range(r + 1):
                                a.append(oppoE(pk, prepare_keyword(i)))
                            query = {'Esw': Esw, 'a': a}
                            # print(query)
                        else:
                            query = data
                            pass

                        sa.sendall(b'CloudServerSB\n')
                        sa.sendall((json.dumps(query) + '\n').encode())
                        result = []
                        while True:
                            Dq = recvuntilendl(sa)
                            if Dq == b'End':
                                break
                            Dq = json.loads(Dq.decode())
                            Dqq = DEp2(pk, skp2, Dq)
                            if Dqq == 0:
                                msg = {'res': 1}
                            else:
                                msg = {'res': 0}
                            sa.sendall((json.dumps(msg) + '\n').encode())
                            # res = json.loads(recvuntilendl(sa).decode())
                            # result.append(res)
                        result = recvuntilendl(sa).decode()
                        client.sendall(
                            (json.dumps(result) + '\n').encode())
                        # print(result)
                        sa.close()

                    else:
                        if data.decode() == 'CloudServerSB':
                            data = recvuntilendl(client)
                else:
                    raise Exception('Client disconnected')
        except Exception as e:
            print('Client disconnected')
            client.close()


if __name__ == "__main__":
    port = int(input("Port? "))
    ThreadedServer('localhost', port).listen()

# data =
# data = json.loads(data)
# if 'r' in data.keys():
#     a = []
#     r = data['r']
#     Esw = data['Esw']
#     for i in range(r + 1):
#         a.append(oppoE(pk, prepare_keyword(i)))
#     query = {'Esw': Esw, 'a': a}
#     print(json.dumps(query))
