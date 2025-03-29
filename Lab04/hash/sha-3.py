from Crypto.Hash import SHA3_256

def sha3_256_hash_string(input_string: str) -> str:
    sha3_256_hash = SHA3_256.new()
    sha3_256_hash.update(input_string.encode('utf-8'))
    return sha3_256_hash.hexdigest()

input_string = input("Enter a string to hash: ")
res = sha3_256_hash_string(input_string)
print(f"SHA3-256 hash: {res}")