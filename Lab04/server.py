from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket 
import threading
import hashlib

#initiate server socker
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(5)

#generate RSA key pair
server_key = RSA.generate(2048)

#list of connected clients
clients = []

#function to encrypt message using AES
def encrypt_AES(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message, AES.block_size))
    return cipher.iv + ct_bytes

#function to decrypt message using AES
def decrypt_AES(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    pt = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return pt.decode('utf-8')

#function to handle client connection
def handle_client(client_socket, client_address):
    print(f"Connected to {client_address}")
    client_key = RSA.import_key(client_socket.recv(2048))

    client_socket.send(server_key.publickey().export_key(format='PEM'))
    aes_key = get_random_bytes(16)
    cipher_rsa = PKCS1_OAEP.new(client_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    client_socket.send(encrypted_aes_key)
    clients.append((client_socket, aes_key))
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            #decrypt message from client
            decrypted_data = decrypt_AES(data, aes_key)
            print(f"Received from {client_address}: {decrypted_data}")
            #broadcast message to all clients
            for client in clients:
                if client != client_socket:
                    client.send(encrypt_AES(decrypted_data, hashlib.sha256(client_key.export_key()).digest()))
            if decrypted_data == "exit":
                break
        except Exception as e:
            print(f"Error: {e}")
            break
    print(f"Disconnected from {client_address}")
    clients.remove((client_socket, aes_key))
    client_socket.close()
    
#main function
while True:
    client_socket, client_address = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()