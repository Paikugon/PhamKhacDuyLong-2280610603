def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5 (message):
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476
    
    original_byte_len = len(message)
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_byte_len.to_bytes(8, byteorder='little')
    
    for i in range (0, len(message), 64):
        chunk = message[i:i + 64]
        words = [int.from_bytes(chunk[j:j + 4], byteorder='little') for j in range(0, 64, 4)]
        
        a_temp = a
        b_temp = b
        c_temp = c
        d_temp = d
        
        for j in range(64):
            if j < 16:
                f = (b_temp & c_temp) | (~b_temp & d_temp)
                g = j
            elif j < 32:
                f = (d_temp & b_temp) | (~d_temp & c_temp)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b_temp ^ c_temp ^ d_temp
                g = (3 * j + 5) % 16
            else:
                f = c_temp ^ (b_temp | ~d_temp)
                g = (7 * j) % 16

            temp = d
            d = c
            c = b
            b = b + left_rotate((a + f + 0x5A827999 + words[g]) & 0xFFFFFFFF, 3)
        
        a += a_temp & 0xFFFFFFFF
        b += b_temp & 0xFFFFFFFF
        c += c_temp & 0xFFFFFFFF
        d += d_temp & 0xFFFFFFFF
        
        return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)
    
input_string = input("Enter a string to hash: ")
hash_value = md5(input_string.encode('utf-8'))
print(f"MD5 hash: {hash_value}")