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


# builds the key for each round from predetermined order
def build_key(key, r):
    n_key = ''
    r_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    r_2 = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    r_3 = [2, 3, 4, 5, 6, 7, 8, 0, 1]
    r_4 = [3, 4, 5, 6, 7, 8, 0, 1, 2]
    if r == 1:
        for i in range(9):
            n_key = n_key + key[r_1[i]]
    if r == 2:
        for i in range(9):
            n_key = n_key + key[r_2[i]]
    if r == 3:
        for i in range(9):
            n_key = n_key + key[r_3[i]]
    if r == 4:
        for i in range(9):
            n_key = n_key + key[r_4[i]]

    return n_key


# expands the bits for the algorithm
def r_bit_expand(r_bit):
    exp = [0, 1, 3, 2, 3, 2, 4, 5]
    r_bit_new = ''

    # walk through and place bits from exp array
    for i in range(len(exp)):
        r_bit_new = r_bit_new + r_bit[exp[i]]
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


# finds an stable value for a bitstring passed in
def s_table(result):
    s_1 = [['101', '010', '001', '110', '011', '100', '111', '000'],
           ['001', '100', '110', '010', '000', '111', '101', '011']]

    s_2 = [['100', '000', '110', '101', '111', '001', '011', '010'],
           ['101', '011', '000', '111', '110', '010', '001', '100']]

    sb_1 = result[0:4]
    sb_2 = result[4:8]

    sr_1 = s_1[int(sb_1[0])][int(sb_1[1:4], 2)]
    sr_2 = s_2[int(sb_2[0])][int(sb_2[1:4], 2)]
    result_n = str(sr_1) + str(sr_2)

    return result_n


# encrypt a block of bits for four rounds
def encrypt(bits, key):
    round_c = 1

    # separate the left and right bits
    l_bits = bits[0:6]
    r_bits = bits[6:12]
    # increments the rounds
    for i in range(4):
        # generate key and update the round
        key_n = build_key(key, round_c)
        round_c += 1
        # expand the bits
        er_bits = r_bit_expand(r_bits)
        # xor the key and expanded bits
        result = xor(er_bits, key_n[0:8])
        # find s-table values
        r_bits_n = s_table(result)
        # xor left and right bits
        r_bits_n = xor(r_bits_n, l_bits)
        l_bits = r_bits
        r_bits = r_bits_n

    # after the round connect l and r bits and send back
    bits_e = l_bits + r_bits

    return bits_e


# decrypt a block of bits for four rounds
def decrypt(bits, key):
    round_c = 4

    l_bits = bits[0:6]
    r_bits = bits[6:12]
    # main difference is that everything is happening to the left bit
    for i in range(4):
        # generate key and update the round
        key_n = build_key(key, round_c)
        round_c -= 1
        el_bits = r_bit_expand(l_bits)
        result = xor(el_bits, key_n[0:8])
        l_bits_n = s_table(result)
        l_bits_n = xor(l_bits_n, r_bits)
        r_bits = l_bits
        l_bits = l_bits_n

    bits_p = l_bits + r_bits

    return bits_p


# sends 12 bit blocks of code to encrypt and decrypt and builds the message
def split_bit(msg, key, t):
    msg_e = ''

    # walk through the message and grab every 12 bits
    while msg:
        ml = len(msg)
        # load first 12 bits
        # check to see if there are enough bits
        if ml < 12:
            bits = msg
            for i in range(12 - ml):
                bits = bits + '0'
            msg = ''

        else:
            # take the first 12 characters in a string
            bits = msg[0:12]
            # remove the bits being used
            msg = msg[12:]

        # determines encryption or decryption
        if t == 'e':
            bits_e = encrypt(bits, key)
        else:
            bits_e = decrypt(bits, key)

        msg_e = msg_e + bits_e

    return msg_e


# specific function for getting information for 3 round
def s_table_three_round(result, t):
    s_1 = [['101', '010', '001', '110', '011', '100', '111', '000'],
           ['001', '100', '110', '010', '000', '111', '101', '011']]

    s_2 = [['100', '000', '110', '101', '111', '001', '011', '010'],
           ['101', '011', '000', '111', '110', '010', '001', '100']]

    # determines which s table to use
    if t == 1:
        s_o = s_1[int(result[0])][int(result[1:4], 2)]
    else:
        s_o = s_2[int(result[0])][int(result[1:4], 2)]

    return s_o


# builds the list of pairs for finding the key values
def build_pairs(o_s, i_s, t):
    val = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
           '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    p_list = []
    tp_list = []

    # finds all the pairs for the given input value
    for i in range(16):
        for j in range(16):
            temp = xor(val[i], val[j])
            if temp == i_s:
                p_list.append(val[i])
                p_list.append(val[j])

    while p_list:
        # get the first two values in the list of pairs
        a = p_list.pop(0)
        b = p_list.pop(0)
        # get s-box values and compare
        c = s_table_three_round(a, t)
        d = s_table_three_round(b, t)
        # compare the xor values
        r = xor(c, d)
        if r == o_s:
            tp_list.append(a)
            tp_list.append(b)

    return tp_list


# main analysis function that finds all the values and walks through the main algorithm
def three_round_key_pairs(l1r1, l1sr1s, key):
    round_c = 2
    kl_p = []
    kr_p = []
    # separate the left and right bits
    l1, r1 = l1r1[0:6], l1r1[6:12]

    l1s, r1s = l1sr1s[0:6], l1sr1s[6:12]

    # finds left 1 prime
    l1p = xor(l1, l1s)

    # First determine L4 and L4s which is the basic encryption for both
    for i in range(3):
        # generate key and update the round
        key_n = build_key(key, round_c)
        round_c += 1
        # expand the bits
        er_bits = r_bit_expand(r1)
        # xor the key and expanded bits
        result = xor(er_bits, key_n[0:8])
        # find s-table values
        r_bits_n = s_table(result)
        # xor left and right bits
        r_bits_n = xor(r_bits_n, l1)
        l1 = r1
        r1 = r_bits_n
    round_c = 2
    for i in range(3):
        # generate key and update the round
        key_n = build_key(key, round_c)
        round_c += 1
        # expand the bits
        er_bits = r_bit_expand(r1s)
        # xor the key and expanded bits
        result = xor(er_bits, key_n[0:8])
        # find s-table values
        r_bits_n = s_table(result)
        # xor left and right bits
        r_bits_n = xor(r_bits_n, l1s)
        l1s = r1s
        r1s = r_bits_n

    # builds values
    l4r4, l4sr4s = l1 + r1, l1s + r1s
    l4, r4, l4s, r4s = l4r4[0:6], l4r4[6:12], l4sr4s[0:6], l4sr4s[6:12]

    # determine output values for s-box
    r4p = xor(r4, r4s)
    res = xor(r4p, l1p)
    o_s1, o_s2 = res[0:3], res[3:6]

    # determine the input values for s-box
    e_l4 = r_bit_expand(l4)
    e_l4s = r_bit_expand(l4s)
    e_l4p = xor(e_l4, e_l4s)
    s1, s2 = e_l4p[0:4], e_l4p[4:8]

    # builds list of pairs
    set_pairs1 = build_pairs(o_s1, s1, 1)
    set_pairs2 = build_pairs(o_s2, s2, 2)

    # find the final values for the key and return them
    kl_p.append(xor(set_pairs1[0], e_l4[0:4]))
    kl_p.append(xor(set_pairs1[1], e_l4[0:4]))
    kr_p.append(xor(set_pairs2[0], e_l4[4:8]))
    kr_p.append(xor(set_pairs2[1], e_l4[4:8]))

    return kl_p[0], kl_p[1], kr_p[0], kr_p[1]


# used to build the key from the analysis and guess the last bit
def three_round_build_key(kl, kr, l1r1, key):
    new_key = ['0', '0', '0', '0', '0', '0', '0', '0', '0']

    # map values to correct place
    new_key[3], new_key[4], new_key[5], new_key[6] = kl[0], kl[1], kl[2], kl[3]
    new_key[7], new_key[8], new_key[0], new_key[1] = kr[0], kr[1], kr[2], kr[3]

    # comparing key to the key found by the analysis
    res = encrypt(l1r1, key)
    c_res = encrypt(l1r1, "".join(new_key))
    if res == c_res:
        return "".join(new_key)

    # change the one bit
    new_key[2] = '1'
    c_res = encrypt(l1r1, "".join(new_key))
    if res == c_res:
        return "".join(new_key)
    else:
        return "Error!"


# the primary function for the analysis that feeds in everything that the analysis needs
def three_round_analysis(l1r1, l1sr1s, ll1rr1, ll1srr1s, key):
    kl = '-1'
    kr = '-1'
    # main part of the analysis
    kl_1, kl_2, kr_1, kr_2 = three_round_key_pairs(l1r1, l1sr1s, key)
    kls_1, kls_2, krs_1, krs_2 = three_round_key_pairs(ll1rr1, ll1srr1s, key)

    # comparing values and finding a value that fits for both parts of the key
    if kl_1 == kls_1:
        kl = kl_1
    elif kl_1 == kls_2:
        kl = kl_1
    elif kl_2 == kls_2:
        kl = kl_2
    elif kl_2 == kls_2:
        kl = kl_2

    if kr_1 == krs_1:
        kr = kr_1
    elif kr_1 == krs_2:
        kr = kr_1
    elif kr_2 == krs_2:
        kr = kr_2
    elif kr_2 == krs_2:
        kr = kr_2

    # error checking
    if kl == '-1':
        print("Error finding key")
        return
    if kr == '-1':
        print("Error finding key")
        return

    kn = three_round_build_key(kl, kr, l1r1, key)

    print("The key found after three rounds is: " + kn)

    return


# handles all user inputs and is the primary part of the program
def main():
    print("Would you like to encrypt(e) or decrypt(d) or three round analysis(a): ")
    t = input()
    # encrypt
    if t == 'e':
        print("What is your key in nine bits?")
        key = input()

        print("What is the message you would like to encrypt: ")
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
    if t == 'd':
        print("What is your key in nine bits?")
        key = input()

        print("What is the message you would like to decrypt: ")
        msg = input()
        msg = text_to_bi(msg)
        msg = split_bit(msg, key, 'd')
        print("Decrypted Bit Message: " + msg)
        msg = bi_to_text(msg)
        print("Decrypted Plain Text Message: " + msg)

    # analysis for three round
    if t == 'a':
        print("What is your key in nine bits?")
        key = input()

        print("Enter in first L1R1: ")
        l1r1 = input()

        print("Enter in first L1*R1* where R1* is equal to R1: ")
        l1sr1s = input()

        print("Enter in second L1R1: ")
        ll1rr1 = input()

        print("Enter in second L1*R1* where R1* is equal to R1: ")
        ll1srr1s = input()

        three_round_analysis(l1r1, l1sr1s, ll1rr1, ll1srr1s, key)

    return


if __name__ == '__main__':
    main()
