import hashlib

def sha256_hash_string(input_string: str) -> str:
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

input_string = input("Enter a string to hash: ")
res = sha256_hash_string(input_string)
print(f"SHA-256 hash: {res}")