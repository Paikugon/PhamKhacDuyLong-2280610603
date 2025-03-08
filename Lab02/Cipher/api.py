from flask import Flask, request, jsonify
from Caesar import CaesarCipher

app = Flask(__name__)

@app.route('/caesar/encrypt', methods=['POST'])
def Caesar_encrypt():
    data = request.get_json()
    plaintext = data.get('plaintext')
    key = data.get('key')
    ciphertext = CaesarCipher.encrypt(plaintext, key)  
    return jsonify({'ciphertext': ciphertext})

@app.route('/caesar/decrypt', methods=['POST'])
def Caesar_decrypt():
    data = request.get_json()
    ciphertext = data.get('ciphertext')
    key = data.get('key')
    plaintext = CaesarCipher.decrypt(ciphertext, key)
    return jsonify({'plaintext': plaintext})

if __name__ == '__main__':
    app.run(debug=True)