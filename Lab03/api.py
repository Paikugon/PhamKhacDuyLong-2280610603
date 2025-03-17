from flask import Flask, request, jsonify
from Cipher.rsa.rsaCipher import RSACipher
from Cipher.ecc.eccCipher import ECCCipher

app = Flask(__name__)

rsa_cipher = RSACipher()

@app.route('/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({"message": "Keys generated successfully"})

@app.route('/rsa/encrypt', methods=['POST'])
def rsa_encrypt():
    data = request.get_json()
    message = data["message"]
    key_type = data["key_type"]
    private_key, public_key = rsa_cipher.load_keys()
    if (key_type == "private"):
        ciphertext = rsa_cipher.encrypt(message, private_key)
    elif (key_type == "public"):
        ciphertext = rsa_cipher.encrypt(message, public_key)
    else :
        return jsonify({"message": "Invalid key type"})
    ciphertext = ciphertext.hex()
    return jsonify({"ciphertext": ciphertext})

@app.route('/rsa/decrypt', methods=['POST'])
def rsa_decrypt():
    data = request.get_json()
    ciphertext = data["ciphertext"]
    key_type = data["key_type"]
    private_key, public_key = rsa_cipher.load_keys()
    ciphertext = bytes.fromhex(ciphertext)
    if (key_type == "private"):
        plaintext = rsa_cipher.decrypt(ciphertext, private_key)
    elif (key_type == "public"):
        plaintext = rsa_cipher.decrypt(ciphertext, public_key)
    else :
        return jsonify({"message": "Invalid key type"})
    return jsonify({"plaintext": plaintext})

@app.route('/rsa/sign', methods=['POST'])
def rsa_sign():
    data = request.get_json()
    message = data["message"]
    private_key, public_key = rsa_cipher.load_keys()
    signature = rsa_cipher.sign(message, private_key)
    signature = signature.hex()
    return jsonify({"signature": signature})

@app.route('/rsa/verify', methods=['POST'])
def rsa_verify():
    try:
        data = request.get_json()
        message = data["message"]
        signature = data["signature"]
        private_key, public_key = rsa_cipher.load_keys()
        signature = bytes.fromhex(signature)
        isVerified = rsa_cipher.verify(message, signature, public_key)
        return jsonify({"verified": isVerified})
    except:
        return jsonify({"verified": False})
    
eccCipher = ECCCipher()

@app.route('/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    try: 
        eccCipher.generateKeys()
        return jsonify({"message": "Keys generated successfully"})
    except:
        return jsonify({"message": "An error occured while generating keys"})
    
@app.route('/ecc/sign', methods=['POST'])
def ecc_sign():
    data = request.get_json()
    message = data["message"]
    sk, vk = eccCipher.loadKeys()
    signature = eccCipher.sign(message, sk)
    return jsonify({"signature": signature.hex()})

@app.route('/ecc/verify', methods=['POST'])
def ecc_verify():
    try:
        data = request.get_json()
        message = data["message"]
        signature = data["signature"]
        sk, vk = eccCipher.loadKeys()
        signature = bytes.fromhex(signature)
        isVerified = eccCipher.verify(message, signature, vk)
        return jsonify({"verified": isVerified})
    except:
        return jsonify({"verified": False})

if (__name__ == "__main__"):
    app.run(port=5000)