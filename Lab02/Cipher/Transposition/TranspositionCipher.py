class TranspositionCipher:
    
    @staticmethod
    def encrypt(text, key):
        key = int(key)
        res = []
        for i in range(0, key):
            for j in range(i, len(text), key):
                res.append(text[j])
        return ''.join(res)
    
    @staticmethod
    def decrypt(text, key):
        key = int(key)
        res = [''] * len(text)
        index = 0
        for i in range(0, key):
            for j in range(i, len(text), key):
                res[j] = text[index]
                index += 1
        return ''.join(res)
    