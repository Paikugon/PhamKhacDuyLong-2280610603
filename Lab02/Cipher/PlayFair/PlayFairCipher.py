from string import ascii_uppercase
class PlayFairCipher:
    @staticmethod
    def CreateMatrix(key):
        key = key.replace("J", "I")
        key = key.upper()
        key_set = set(key)
        alphabet = ''.join(ascii_uppercase)
        remaining = [
            letter for letter in alphabet if letter not in key_set and letter != 'J'
        ]
        matrix = []
        key += ''.join(remaining)
        for i in range(0, 25, 5):
            matrix.append(list(key[i:i+5]))
        return matrix
    
    @staticmethod
    def find_position(matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None

    @staticmethod
    def read(plaintext, key, mode):
        plaintext = ''.join(filter(str.isalpha, plaintext))
        matrix = PlayFairCipher.CreateMatrix(key)
        plaintext = plaintext.upper().replace("J", "I")
        plaintext_pairs = []
        i = 0
        while i < len(plaintext):
            a = plaintext[i]
            b = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'
            if a == b:
                plaintext_pairs.append((a, 'X'))
                i += 1
            else:
                plaintext_pairs.append((a, b))
                i += 2
        if len(plaintext_pairs[-1]) == 1:
            plaintext_pairs[-1] = (plaintext_pairs[-1][0], 'X')

        ciphertext = ''
        for a, b in plaintext_pairs:
            row1, col1 = PlayFairCipher.find_position(matrix, a)
            row2, col2 = PlayFairCipher.find_position(matrix, b)
            if row1 == row2:
                ciphertext += matrix[row1][(col1 + mode) % 5]
                ciphertext += matrix[row2][(col2 + mode) % 5]
            elif col1 == col2:
                ciphertext += matrix[(row1 + mode) % 5][col1]
                ciphertext += matrix[(row2 + mode) % 5][col2]
            else:
                ciphertext += matrix[row1][col2]
                ciphertext += matrix[row2][col1]

        return ciphertext
    