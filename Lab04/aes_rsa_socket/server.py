from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket 
import threading
import hashlib

#initiate server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

#generate RSA keys
server_key = RSA.generate(2048)
private_key = server_key.export_key()
public_key = server_key.publickey().export_key()
cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key))
cipher_rsa_private = PKCS1_OAEP.new(RSA.import_key(private_key))

#list for incoming connections
clients = []

#function to encrypt data
def encrypt_data(key, data):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    iv = cipher.iv
    return iv + ct_bytes

#function to decrypt data
def decrypt_data(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ct = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

#function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Connection from {client_address} has been established.")
    client_socket.send(server_key.public_key().export_key(format='PEM'))
    client_received_key = client_socket.recv(2048)
    aes_key = get_random_bytes(16)
    
    cipher_rsa = PKCS1_OAEP.new(RSA.import_key(client_received_key))
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    client_socket.send(encrypted_aes_key)
    
    clients.append((client_socket, aes_key))
    
    while True:
        encrypted_Message = client_socket.recv(1024)
        decrypted_Message = decrypt_data(aes_key, encrypted_Message)
        print(f"Received message from {client_address}: {decrypted_Message}")
        for client, key in clients:
            if client != client_socket:
                encrypted_Message = encrypt_data(key, decrypted_Message)
                client.send(encrypted_Message)
        if decrypted_Message == "exit":
            break
    client_socket.close()
    clients.remove((client_socket, aes_key))
    print(f"Connection from {client_address} has been closed.")
    
print("Server is listening for incoming connections...")
while True:
    client_socket, client_address = server_socket.accept()
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()