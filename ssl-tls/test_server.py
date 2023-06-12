import socket
import ssl

HOST = '35.209.145.240'
PORT = 4444


def server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('./new.pem', './private.key')

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((HOST, PORT))

    soc.listen(3)
    s_soc = context.wrap_socket(soc, server_side=True)
    conn, add = s_soc.accept()
    print(f"Server is connected to {add}")
    conn.send(f"Welcome to Server ('{HOST}', '{PORT}')...!".encode())
    s_soc.close()


if __name__ == "__main__":
    server()
