from flask import Flask, request, jsonify, render_template, json # type: ignore
from Cipher.Caesar.CaesarCipher import CaesarCipher

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/caesar/encrypt', methods=['POST'])
def Caesar_encrypt():
    plaintext = request.form['plaintext']
    key = int(request.form['key'])
    ciphertext = CaesarCipher.encrypt(plaintext, key)  
    return jsonify({'ciphertext': ciphertext})

@app.route('/caesar/decrypt', methods=['POST'])
def Caesar_decrypt():
    ciphertext = request.form['ciphertext']
    key = int(request.form['key'])
    plaintext = CaesarCipher.decrypt(ciphertext, key)
    return jsonify({'plaintext': plaintext})

if __name__ == '__main__':
    app.run(debug=True);