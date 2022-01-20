# define global values
ip = [[58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4],
      [62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8],
      [57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3],
      [61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]]

ip_inv = [[40, 8, 48, 16, 56, 24, 64, 32],
          [39, 7, 47, 15, 55, 23, 63, 31],
          [38, 6, 46, 14, 54, 22, 62, 30],
          [37, 5, 45, 13, 53, 21, 61, 29],
          [36, 4, 44, 12, 52, 20, 60, 28],
          [35, 3, 43, 11, 51, 19, 59, 27],
          [34, 2, 42, 10, 50, 18, 58, 26],
          [33, 1, 41, 9, 49, 17, 57, 25]]

# SBox Declaration
s_1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
       [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
       [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
       [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
s_2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
       [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
       [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
       [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
s_3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
       [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
       [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
       [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
s_4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
       [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
       [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
       [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
s_5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
       [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
       [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
       [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
s_6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
       [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
       [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
       [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
s_7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
       [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
       [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
       [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
s_8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
       [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
       [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
       [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

# Expansion Permutation box
exp = [[32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9],
       [8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17],
       [16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25],
       [24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]]

# key shift box
key_shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Key Permutation
key_permutation = [[57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18],
                   [10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36],
                   [63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22],
                   [14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]]

key_choose = [[14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10],
              [23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2],
              [41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48],
              [44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]]

# keys to be updated in program
list_keys = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

permute_table = [[16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10],
                 [2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]]


# converts text characters to binary
def text_to_bi(text):
    # simple conversion
    t_text = ''.join(format(ord(i), '08b') for i in text)

    return t_text


# converts binary to text
def bi_to_text(text):
    msg = ''
    t_text = text
    # convert in blocks of 8
    while t_text:
        # if there are less than 8 then ignore the rest
        if len(t_text) < 8:
            return msg
        byte = t_text[0:8]
        n = int(byte, 2)
        c = chr(n)
        msg = msg + c
        # slice msg
        t_text = t_text[8:]

    return msg


#  used to go through the key permutation for the 48 bit key segment
def key_extra(t):
    t_key = ''

    # walk though and get the values and put them into a string
    for i in range(4):
        for j in range(12):
            t_key = t_key + t[key_choose[i][j] - 1]
    return t_key


# used to do left shifts on the key and will either left shift one or two values
def pop_func(c, d, ln, num):
    f = []
    # left shift one value in both c and d
    if num == 1:
        a = c.pop(0)
        c.append(a)
        a = d.pop(0)
        d.append(a)
        # rejoin c and d lists
        f.extend(c), f.extend(d)
        t = "".join(f)
        # add the key to the key list index passed in
        list_keys[ln] = key_extra(t)
        f.clear()
    else:
        # left shift two values in both c and d
        a, b = c.pop(0), c.pop(0)
        c.append(a), c.append(b)
        a, b = d.pop(0), d.pop(0)
        d.append(a), d.append(b)
        # rejoin the list and add to key list
        f.extend(c), f.extend(d)
        t = "".join(f)
        list_keys[ln] = key_extra(t)
        f.clear()

    return


# builds the key for each round and will add them to the key list
def build_key(key):
    n_key = []
    c = []
    d = []
    # discards parity bits
    for i in range(4):
        for j in range(14):
            # possibly sub 1
            a = key_permutation[i][j]
            a = a - 1
            n_key.append(key[a])

    # split the key into c and d
    for i in range(28):
        a = n_key.pop(0)
        c.append(a)
    for i in range(28):
        a = n_key.pop(0)
        d.append(a)

    # shift and pop handler determines each key
    for i in range(16):
        pop_func(c, d, i, key_shift[i])

    return


# expands the bits for the algorithm
def r_bit_expand(r_bit):
    r_bit_new = ''

    # walk through and place bits from exp array
    for i in range(4):
        for j in range(12):
            r_bit_new = r_bit_new + r_bit[exp[i][j] - 1]
    return r_bit_new


# simple xor function for strings of bits
def xor(bits_a, bits_b):
    # a is smaller of the two
    result = ''
    for i in range(len(bits_a)):
        # compares
        if bits_a[int(i)] == bits_b[int(i)]:
            bit = '0'
        else:
            bit = '1'
        result = result + bit

    return result


# checks to make sure the s-box output values are the correct length
def check_length(val):
    a = len(val)
    # if their length is less than 4 add a zero to the front
    if a < 4:
        for i in range(4-a):
            val = '0' + val

    return val


# finds an s-table value for a bitstring passed in
def s_table(result):
    p_string = ''

    # split up the bitstring for the s-boxes
    sb_1 = result[0:6]
    sb_2 = result[6:12]
    sb_3 = result[12:18]
    sb_4 = result[18:24]
    sb_5 = result[24:30]
    sb_6 = result[30:36]
    sb_7 = result[36:42]
    sb_8 = result[42:48]

    # get the output value for the s-boxes
    sr_1 = str(format(s_1[int(str(sb_1[0] + sb_1[5]), 2)][int(sb_1[1:5], 2)], "b"))
    sr_2 = str(format(s_2[int(str(sb_2[0] + sb_2[5]), 2)][int(sb_2[1:5], 2)], "b"))
    sr_3 = str(format(s_3[int(str(sb_3[0] + sb_3[5]), 2)][int(sb_3[1:5], 2)], "b"))
    sr_4 = str(format(s_4[int(str(sb_4[0] + sb_4[5]), 2)][int(sb_4[1:5], 2)], "b"))
    sr_5 = str(format(s_5[int(str(sb_5[0] + sb_5[5]), 2)][int(sb_5[1:5], 2)], "b"))
    sr_6 = str(format(s_6[int(str(sb_6[0] + sb_6[5]), 2)][int(sb_6[1:5], 2)], "b"))
    sr_7 = str(format(s_7[int(str(sb_7[0] + sb_7[5]), 2)][int(sb_7[1:5], 2)], "b"))
    sr_8 = str(format(s_8[int(str(sb_8[0] + sb_8[5]), 2)][int(sb_8[1:5], 2)], "b"))

    # make sure the bit stings a 4 characters long
    sr_1 = check_length(sr_1)
    sr_2 = check_length(sr_2)
    sr_3 = check_length(sr_3)
    sr_4 = check_length(sr_4)
    sr_5 = check_length(sr_5)
    sr_6 = check_length(sr_6)
    sr_7 = check_length(sr_7)
    sr_8 = check_length(sr_8)

    # build value with s-box outputs
    result_n = sr_1 + sr_2 + sr_3 + sr_4 + sr_5 + sr_6 + sr_7 + sr_8

    # walk through s-box value permutation
    for i in range(2):
        for j in range(16):
            p_string = p_string + result_n[permute_table[i][j] - 1]

    return p_string


# encrypt a block of bits for four rounds
def encrypt(bits):
    # starting round index
    round_c = 0
    bits_n = ''

    # initial permutation
    for i in range(4):
        for j in range(16):
            bits_n = bits_n + bits[ip[i][j] - 1]

    bits = bits_n
    bits_n = ''

    # separate the left and right bits
    l_bits = bits[0:32]
    r_bits = bits[32:64]
    # increments the rounds
    for i in range(16):
        # expand the bits
        er_bits = r_bit_expand(r_bits)
        # xor the key and expanded bits
        result = xor(er_bits, list_keys[round_c][0:48])
        round_c += 1
        # find s-table values
        r_bits_n = s_table(result)
        # xor left and right bits
        r_bits_n = xor(r_bits_n, l_bits)
        l_bits = r_bits
        r_bits = r_bits_n

    # after the round connect l and r bits and send back
    bits_e = r_bits + l_bits

    # inverse table permutation
    for i in range(8):
        for j in range(8):
            bits_n = bits_n + bits_e[ip_inv[i][j] - 1]
    return bits_n


# decrypt a block of bits for four rounds
def decrypt(bits):
    round_c = 15
    bits_n = ''

    # initial permutation
    for i in range(4):
        for j in range(16):
            bits_n = bits_n + bits[ip[i][j] - 1]

    bits = bits_n
    bits_n = ''

    # separate the left and right bits
    l_bits = bits[0:32]
    r_bits = bits[32:64]
    # increments the rounds
    for i in range(16):
        # expand the bits
        er_bits = r_bit_expand(r_bits)
        # xor the key and expanded bits
        result = xor(er_bits, list_keys[round_c][0:48])
        round_c -= 1
        # find s-table values
        r_bits_n = s_table(result)
        # xor left and right bits
        r_bits_n = xor(r_bits_n, l_bits)
        l_bits = r_bits
        r_bits = r_bits_n

    # after the round connect l and r bits and send back
    bits_p = r_bits + l_bits

    # inverse permutation table
    for i in range(8):
        for j in range(8):
            bits_n = bits_n + bits_p[ip_inv[i][j] - 1]

    return bits_n


# sends 64 bit blocks of code to encrypt and decrypt and builds the message
def split_bit(msg, key, t):
    msg_e = ''
    build_key(key)
    # walk through the message and grab every 12 bits
    while msg:
        ml = len(msg)
        # load first 12 bits
        # check to see if there are enough bits
        if ml < 64:
            bits = msg
            for i in range(64 - ml):
                bits = bits + '0'
            msg = ''

        else:
            # take the first 12 characters in a string
            bits = msg[0:64]
            # remove the bits being used
            msg = msg[64:]

        # determines encryption or decryption
        if t == 'e':
            bits_e = encrypt(bits)
        else:
            bits_e = decrypt(bits)

        msg_e = msg_e + bits_e

    return msg_e


# handles all user inputs and is the primary part of the program
def main():

    print("Would you like to encrypt(e) or decrypt(d): ")
    t = input()
    # encrypt
    if t == 'e':
        # can use predetermined key and message. Just comment out input.
        # uncomment key to add your own key
        print("What is your key in 64 bits?")
        key = '0001001100110100010101110111100110011011101111001101111111110001'
        # key = input()

        print("What is the message you would like to encrypt: ")
        msg = '0000000100100011010001010110011110001001101010111100110111101111'
        msg = input()
        msg = text_to_bi(msg)
        print("Bit Conversion: " + msg)
        msg = split_bit(msg, key, 'e')
        print("Bit Encryption: " + msg)
        msg = bi_to_text(msg)
        print("Encrypted Text Message: " + msg)

        msg = text_to_bi(msg)
        msg = split_bit(msg, key, 'd')
        print("Decrypted Bit Message: " + msg)
        msg = bi_to_text(msg)
        print("Decrypted Plain Text Message: " + msg)

    # decrypt
    # uncomment key input to add your own if you want
    if t == 'd':
        print("What is your key in nine bits?")
        key = '0001001100110100010101110111100110011011101111001101111111110001'
        # key = input()

        print("What is the message you would like to decrypt: ")
        msg = input()
        msg = text_to_bi(msg)
        msg = split_bit(msg, key, 'd')
        print("Decrypted Bit Message: " + msg)
        msg = bi_to_text(msg)
        print("Decrypted Plain Text Message: " + msg)

    return


if __name__ == '__main__':
    main()
