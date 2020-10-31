import base64

class Key:
    def __init__(self, public_key, private_key, modulus):
        self.public_key = public_key
        self.private_key = private_key
        self.modulus = modulus

    def __repr__(self):
        return f'\nPublic Key: {self.public_key}\n\nPrivate Key: {self.private_key}\n\nModulus: {self.modulus}\n'


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b//a) * x1  
    y = x1  
    return (gcd, x, y)


def modInv(a, b):
    gcd, x, y = extended_euclidean(a, b)
    if gcd != 1:
        print("a and b should be relatively prime")
        return
    return x % b


def fast_modular_exponentiation(a, b, n):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % n
        a = (a * a) % n
        b //= 2
    return res


def generate_public_key(phi_n):
    e_lst = [3, 5, 17, 257, 65537]
    for i in e_lst:
        if gcd(i, phi_n) == 1:
            e = i
            break
    return e   


def generate_private_key(e, phi_n):
    return modInv(e, phi_n)


def generate_key_pairs(p, q):
    n = p*q
    phi_n = (p - 1) * (q - 1) 
    e = generate_public_key(phi_n)
    d = generate_private_key(e, phi_n)
    k = Key(e, d, n)
    return k


def rsa_encrypt(m, public_key, modulus):
    return fast_modular_exponentiation(m, public_key, modulus)


def rsa_decrypt(c, private_key, modulus):
    return fast_modular_exponentiation(c, private_key, modulus)


def encrypt(message, public_key, modulus):
    enc_lst = []
    for ch in message:
        enc_lst.append(rsa_encrypt(ord(ch), public_key, modulus))
    
    encrypted_message = ' '.join(str(x) for x in enc_lst)
    return encrypted_message


def decrypt(buffer, private_key, modulus):
    decoded_message = [int(x) for x in buffer.split(' ')]
    dec_lst = []
    for i in decoded_message:
        dec_lst.append(rsa_decrypt(i, private_key, modulus))
    
    decrypted_message = ''.join(chr(x) for x in dec_lst)
    return decrypted_message


def encode_message(message):
    message_bytes = message.encode()
    encoded_message = base64.b64encode(message_bytes)
    return encoded_message


def decode_message(message):
    decoded_message = base64.b64decode(message)
    msg = decoded_message.decode()
    return msg