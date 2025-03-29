import hashlib

def md5_hash_string(input_string: str) -> str:
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

input_string = input("Enter a string to hash: ")
res = md5_hash_string(input_string)
print(f"MD5 hash: {res}")