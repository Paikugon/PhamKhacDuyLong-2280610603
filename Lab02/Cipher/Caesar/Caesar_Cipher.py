from string import ascii_uppercase

Alphabet = list(ascii_uppercase)
len = len(Alphabet)

class CaesarCipher:
   
    @staticmethod
    def encrypt(text: str, key: int) -> str:
        text = text.upper()
        encrypted = []
        for char in text :
            index = Alphabet.index(char)
            res = Alphabet[(index + key) % len]
            encrypted.append(res)
        return "".join(encrypted)
    
    @staticmethod
    def decrypt(text: str, key: int) -> str :
        text = text.upper()
        decrypted = []
        for char in text :
            index = Alphabet.index(char)
            res = Alphabet[(index - key + len) % len]
            decrypted.append(res)
        return "".join(decrypted)
