from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

client_key = RSA.generate(2048)
client_socket.send(client_key.publickey().export_key(format='PEM'))
server_key = RSA.import_key(client_socket.recv(2048))
encrypted_aes_key = client_socket.recv(256)
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

#function to encrypt message using AES
def encrypt_AES(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ct_bytes

#function to decrypt message using AES
def decrypt_AES(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    encrypted = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
    return decrypted.decode('utf-8')

def receive():
    while True:
        data = client_socket.recv(1024)
        decrypted_data = decrypt_AES(data, aes_key)
        print(f"Received: {decrypted_data}")
        
receive_thread = threading.Thread(target=receive)
receive_thread.start()
while True:
    message = input("Enter message('exit' to quit): ")
    encrypted_message = encrypt_AES(message, aes_key)
    client_socket.send(encrypted_message)
    if message == "exit":
        break
    
client_socket.close()
receive_thread.join()