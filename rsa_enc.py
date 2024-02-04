import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_keypair():
    p = int(input("Enter first prime number: "))
    q = int(input("Enter second prime number: "))
    n = p * q
    phi_n = (p-1) * (q-1)
    e = 65537  # public exponent
    d = pow(e, -1, phi_n)  # private exponent
    key = RSA.construct((n, e, d))
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def base_enc(data):
    encoded_data = base64.b64encode(data.encode())
    return encoded_data

def call_rsa(public_key, private_key, encoded_data):
    public_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher_rsa.encrypt(data.encode())
    return encrypted_message

if __name__ == "__main__":
    data = input("Enter data to be Encoded and Encrypted: ")
    encoded_data = base_enc(data)
    private_key, public_key = generate_keypair()
    encrypted_data = call_rsa(public_key, private_key, encoded_data)
    print("Encrypted data: ", encrypted_data)


# This is updated code of the previous one