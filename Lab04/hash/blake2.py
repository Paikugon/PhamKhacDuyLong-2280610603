import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message.encode('utf-8'))
    return blake2_hash.hexdigest()

input_string = input("Enter a string to hash: ")
res = blake2(input_string)
print(f"BLAKE2 hash: {res}")