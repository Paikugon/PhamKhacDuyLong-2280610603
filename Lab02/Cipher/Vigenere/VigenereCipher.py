from string import ascii_uppercase

Alphabet = list(ascii_uppercase)

class VigenereCipher:

    @staticmethod
    def encrypt(text, key):
        text = text.upper()
        key = key.upper()
        keylen = len(key)
        res = []
        
        for i in range(0, len(text)):
            if text[i].isalpha() :
                shift = Alphabet.index(key[i % keylen])
                encrypted_char = Alphabet[(Alphabet.index(text[i]) + shift) % len(Alphabet)]
                res.append(encrypted_char)
            else:
                res.append(text[i])        
        return ''.join(res)
    
    @staticmethod
    def decrypt(text, key):
        text = text.upper()
        key = key.upper()
        keylen = len(key)
        res = []
        
        for i in range(0, len(text)):
            if text[i].isalpha():
                shift = Alphabet.index(key[i % keylen])
                decrypted_char = Alphabet[(Alphabet.index(text[i]) - shift + 26) % len(Alphabet)]
                res.append(decrypted_char)
            else:
                res.append(text[i])
        return ''.join(res)
