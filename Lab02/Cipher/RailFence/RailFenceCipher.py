class RailFenceCipher:
    @staticmethod
    def encrypt(text, key):
        if (key == 1):
            return text
        rails = [[] for _ in range(key)]
        cur = 0
        dir = 1
        for char in text:
            rails[cur].append(char)
            if cur == 0:
                dir = 1
            if cur == key - 1:
                dir = -1
            cur += dir
        return ''.join(''.join(rail) for rail in rails)
    
    @staticmethod
    def decrypt(text, key):
        if (key == 1):
            return text
        rail_len = [0] * key
        cur = 0
        dir = 1
        for char in text:
            rail_len[cur] += 1
            if cur == 0:
                dir = 1
            if cur == key - 1:
                dir = -1
            cur += dir

        rails = []
        idx = 0
        for r_len in rail_len:
            rails.append(text[idx:idx + r_len])
            idx += r_len

        result = []
        cur = 0
        dir = 1
        rail_pos = [0] * key
        for _ in text:
            result.append(rails[cur][rail_pos[cur]])
            rail_pos[cur] += 1
            if cur == 0:
                dir = 1
            if cur == key - 1:      
                dir = -1
            cur += dir
        return ''.join(result)
    
