from hashlib import sha512


def sha512_encrypt(password):
    password=sha512(password.encode('utf-8')).hexdigest()
    return password

if __name__=='__main__':
    password=sha512_encrypt('123456')
    print(password)