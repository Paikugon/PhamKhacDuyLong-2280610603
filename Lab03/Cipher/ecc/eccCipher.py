import ecdsa, os

if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')
    
class ECCCipher:
    def __init__(self):
        pass
    
    def generateKeys(self):
        sk = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)
        vk = sk.get_verifying_key()
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())
        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())
            
    def loadKeys(self):
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())
        with open('cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())
        return sk, vk
    
    def sign(self, message, sk):
        return sk.sign(message.encode('ascii'))
    
    def verify(self, message, signature, vk):
        try:
            return vk.verify(signature, message.encode('ascii'))
        except:
            return False