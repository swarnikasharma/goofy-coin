from Crypto.PublicKey import RSA
from Crypto import Random

def adduser(name):
    random_gen = Random.new().read
    private_key = RSA.generate(1024,random_gen)
    public_key = private_key.publickey()

    return public_key,private_key
