from Transposition import TranspositionCipher
from flask import Flask, request, jsonify 
from Caesar import CaesarCipher
from Vigenere import VigenereCipher
from RailFence import RailFenceCipher
from PlayFair import PlayFairCipher

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

@app.route('/vigenere/encrypt', methods=['POST'])
def Vigenere_encrypt():
    data = request.get_json()
    plaintext = data.get('plaintext')
    key = data.get('key')
    ciphertext = VigenereCipher.encrypt(plaintext, key)
    return jsonify({'ciphertext': ciphertext})

@app.route('/vigenere/decrypt', methods=['POST'])
def Vigenere_decrypt():
    data = request.get_json()
    ciphertext = data.get('ciphertext')
    key = data.get('key')
    plaintext = VigenereCipher.decrypt(ciphertext, key)
    return jsonify({'plaintext': plaintext})

@app.route('/railfence/encrypt', methods=['POST'])
def RailFence_encrypt():
    data = request.get_json()
    plaintext = data.get('plaintext')
    key = data.get('key')
    ciphertext = RailFenceCipher.encrypt(plaintext, key)
    return jsonify({'ciphertext': ciphertext})

@app.route('/railfence/decrypt', methods=['POST'])
def RailFence_decrypt():
    data = request.get_json()
    ciphertext = data.get('ciphertext')
    key = data.get('key')
    plaintext = RailFenceCipher.decrypt(ciphertext, key)
    return jsonify({'plaintext': plaintext})

@app.route('/playfair/encrypt', methods=['POST'])
def PlayFair_encrypt():
    data = request.get_json()
    plaintext = data.get('plaintext')
    key = data.get('key')
    ciphertext = PlayFairCipher.read(plaintext, key, 1)
    return jsonify({'ciphertext': ciphertext})

@app.route('/playfair/decrypt', methods=['POST'])
def PlayFair_decrypt():
    data = request.get_json()
    ciphertext = data.get('ciphertext')
    key = data.get('key')
    plaintext = PlayFairCipher.read(ciphertext, key, -1)
    return jsonify({'plaintext': plaintext})

@app.route('/transposition/encrypt', methods=['POST'])
def Transposition_encrypt():
    data = request.get_json()
    plaintext = data.get('plaintext')
    key = data.get('key')
    ciphertext = TranspositionCipher.encrypt(plaintext, key)
    return jsonify({'ciphertext': ciphertext})

@app.route('/transposition/decrypt', methods=['POST'])
def Transposition_decrypt():
    data = request.get_json()
    ciphertext = data.get('ciphertext')
    key = data.get('key')
    plaintext = TranspositionCipher.decrypt(ciphertext, key)
    return jsonify({'plaintext': plaintext})

if __name__ == '__main__':
    app.run(debug=True)