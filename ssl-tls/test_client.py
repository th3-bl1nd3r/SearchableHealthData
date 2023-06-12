import socket
import ssl
import optparse

parser = optparse.OptionParser('usage%prog ' + '-d <domain> ' + '-p <port> ')
parser.add_option('-d', dest='domain', type='string',
                  help='specify the method')
parser.add_option('-p', dest='port', type='string', help='specify the url')
(options, args) = parser.parse_args()
domain = str(options.domain)
port = int(options.port)


def client():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations('new.pem',)

    soc = socket.socket()
    c_soc = context.wrap_socket(soc, server_hostname=domain)
    c_soc.connect((domain, port))

    print("Connection successful...")
    msg = c_soc.recv(1024)
    print(msg.decode())
    c_soc.close()


if __name__ == "__main__":
    client()
