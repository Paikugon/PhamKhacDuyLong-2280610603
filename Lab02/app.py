from flask import Flask, request, jsonify, render_template, json # type: ignore
from Cipher.Caesar.CaesarCipher import CaesarCipher
from Cipher.Vigenere.VigenereCipher import VigenereCipher
from Cipher.PlayFair.PlayFairCipher import PlayFairCipher
from Cipher.RailFence.RailFenceCipher import RailFenceCipher
from Cipher.Transposition.TranspositionCipher import TranspositionCipher

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/vigenere')
def vigenere():
    return render_template('vigenere.html')

@app.route('/playfair')
def playfair():
    return render_template('playfair.html')

@app.route('/railfence')
def railfence():
    return render_template('railfence.html')

@app.route('/transposition')
def transposition():
    return render_template('transposition.html')

# Route Functions
@app.route('/caesar/encrypt', methods=['POST'])
def Caesar_encrypt():
    plaintext = request.form['plaintext']
    key = int(request.form['key'])
    ciphertext = CaesarCipher.encrypt(plaintext, key)  
    return f"<pre>text: {plaintext} <br/>key: {key}<br/>ciphertext: {ciphertext}</pre>"

@app.route('/caesar/decrypt', methods=['POST'])
def Caesar_decrypt():
    ciphertext = request.form['ciphertext']
    key = int(request.form['key'])
    plaintext = CaesarCipher.decrypt(ciphertext, key)
    return f"<pre>ciphertext: {ciphertext} <br/>key: {key}<br/>plaintext: {plaintext}</pre>"

@app.route('/vigenere/encrypt', methods=['POST'])
def Vigenere_encrypt():
    plaintext = request.form['plaintext']
    key = request.form['key']
    ciphertext = VigenereCipher.encrypt(plaintext, key)
    return f"<pre>text: {plaintext} <br/>key: {key}<br/>ciphertext: {ciphertext}</pre>"

@app.route('/vigenere/decrypt', methods=['POST'])
def Vigenere_decrypt():
    ciphertext = request.form['ciphertext']
    key = request.form['key']
    plaintext = VigenereCipher.decrypt(ciphertext, key)
    return f"<pre>ciphertext: {ciphertext} <br/>key: {key}<br/>plaintext: {plaintext}</pre>"

@app.route('/playfair/encrypt', methods=['POST'])
def PlayFair_encrypt():
    plaintext = request.form['plaintext']
    key = request.form['key']
    ciphertext = PlayFairCipher.read(plaintext, key, 1)
    return f"<pre>text: {plaintext} <br/>key: {key}<br/>ciphertext: {ciphertext}</pre>"

@app.route('/playfair/decrypt', methods=['POST'])
def PlayFair_decrypt():
    ciphertext = request.form['ciphertext']
    key = request.form['key']
    plaintext = PlayFairCipher.read(ciphertext, key, -1)
    return f"<pre>ciphertext: {ciphertext} <br/>key: {key}<br/>plaintext: {plaintext}</pre>"

@app.route('/railfence/encrypt', methods=['POST'])
def RailFence_encrypt():
    plaintext = request.form['plaintext']
    key = int(request.form['key'])
    ciphertext = RailFenceCipher.encrypt(plaintext, key)
    return f"<pre>text: {plaintext} <br/>key: {key}<br/>ciphertext: {ciphertext}</pre>"

@app.route('/railfence/decrypt', methods=['POST'])
def RailFence_decrypt():
    ciphertext = request.form['ciphertext']
    key = int(request.form['key'])
    plaintext = RailFenceCipher.decrypt(ciphertext, key)
    return f"<pre>ciphertext: {ciphertext} <br/>key: {key}<br/>plaintext: {plaintext}</pre>"

@app.route('/transposition/encrypt', methods=['POST'])
def Transposition_encrypt():
    plaintext = request.form['plaintext']
    key = int(request.form['key'])
    ciphertext = TranspositionCipher.encrypt(plaintext, key)
    return f"<pre>text: {plaintext} <br/>key: {key}<br/>ciphertext: {ciphertext}</pre>"

@app.route('/transposition/decrypt', methods=['POST'])
def Transposition_decrypt():
    ciphertext = request.form['ciphertext']
    key = int(request.form['key'])
    plaintext = TranspositionCipher.decrypt(ciphertext, key)
    return f"<pre>ciphertext: {ciphertext} <br/>key: {key}<br/>plaintext: {plaintext}</pre>"

if __name__ == '__main__':
    app.run(debug=True);