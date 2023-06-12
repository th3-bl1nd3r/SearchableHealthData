1. Install OpenSSL
2. Create .key, .crt, .pem files 
3. Add certificate.crt to the windows trusted certificates

Commands to run in OpenSSL:
1. openssl genrsa -aes256 -out private.key 2048
2. openssl rsa -in private.key -out private.key
3. openssl req -new -x509 -nodes -sha1 -key private.key -out certificate.crt -days 36500
4. openssl req -x509 -new -nodes -key private.key -sha1 -days 36500 -out new.pem