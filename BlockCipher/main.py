from Crypt_Math import *
# used some help from https://crypto.interactive-maths.com/hill-cipher.html for the math


# filters out non alphabetical characters and converts the string to uppercase
def filter_plain_text(text):
    # filter out spaces and make letters upper case
    t_text = ''.join(c for c in text if c.isalpha())
    t_text = t_text.upper()

    return t_text


# builds an matrix from a key string
def build_key(key):
    # initializes the array
    key_m = [[0 for x in range(3)] for y in range(3)]
    c = 0
    for i in range(3):
        for j in range(3):
            # converts letter to number
            key_m[i][j] = ord(key[c]) - ord('A')
            c = c + 1
    # returns array
    return key_m


# basic encrypt function that is used for both encrypt and decrypt just with different keys
def encrypt(key, v):
    # calculate the new values with matrix multiplication
    a = ((ord(v[0]) - ord('A')) * key[0][0])+((ord(v[1]) - ord('A')) * key[0][1])+((ord(v[2]) - ord('A')) * key[0][2])
    b = ((ord(v[0]) - ord('A')) * key[1][0])+((ord(v[1]) - ord('A')) * key[1][1])+((ord(v[2]) - ord('A')) * key[1][2])
    c = ((ord(v[0]) - ord('A')) * key[2][0])+((ord(v[1]) - ord('A')) * key[2][1])+((ord(v[2]) - ord('A')) * key[2][2])
    # take mod 26
    a = a % 26
    b = b % 26
    c = c % 26
    # output new string
    v_s = chr(a + ord('A')) + chr(b + ord('A')) + chr(c + ord('A'))

    return v_s


# used to find the det of a 3x3 matrix
def find_det_key(key):
    a, b, c = key[0][0], key[0][1], key[0][2]
    d, e, f = key[1][0], key[1][1], key[1][2]
    g, h, i = key[2][0], key[2][1], key[2][2]
    det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    det = det % 26

    return det


# calculates the adjugate matrix
def calculate_adj_matrix(key, det):
    key_n = [[0 for x in range(3)] for y in range(3)]
    # pulls key values
    a, b, c = key[0][0], key[0][1], key[0][2]
    d, e, f = key[1][0], key[1][1], key[1][2]
    g, h, i = key[2][0], key[2][1], key[2][2]

    # finds the det values for each
    a_n, b_n, c_n = (e * i - h * f), -1 * (b * i - h * c), (b * f - e * c)
    d_n, e_n, f_n = -1 * (d * i - g * f), (a * i - g * c), -1 * (a * f - d * c)
    g_n, h_n, i_n = (d * h - e * g), -1 * (a * h - g * b), (e * a - d * b)

    # mod 26
    a_n, b_n, c_n = a_n % 26, b_n % 26, c_n % 26
    d_n, e_n, f_n = d_n % 26, e_n % 26, f_n % 26
    g_n, h_n, i_n = g_n % 26, h_n % 26, i_n % 26

    # multiply by the det
    a_n, b_n, c_n = a_n * det % 26, b_n * det % 26, c_n * det % 26
    d_n, e_n, f_n = d_n * det % 26, e_n * det % 26, f_n * det % 26
    g_n, h_n, i_n = g_n * det % 26, h_n * det % 26, i_n * det % 26

    # reassign to key
    key_n[0][0], key_n[0][1], key_n[0][2] = a_n, b_n, c_n
    key_n[1][0], key_n[1][1], key_n[1][2] = d_n, e_n, f_n
    key_n[2][0], key_n[2][1], key_n[2][2] = g_n, h_n, i_n

    return key_n


# finds all the required values for decryption then sends the new values to encrypt
def decrypt(key, v):
    det = find_det_key(key)
    det_inv = my_mod_inverse(det, 26)
    # if there is no inverse of the det then send an error message to console
    if det_inv == -1:
        return "-1"
    # = build new key matrix
    key = calculate_adj_matrix(key, det_inv)
    v_s = encrypt(key, v)

    return v_s


# used to walk through a message and send it in blocks to be encrypted or decrypted
def split_msg(key, msg, t):
    msg_e = ''

    # walk through the message and grab every 12 bits
    key_m = build_key(key)
    while msg:
        ml = len(msg)
        # load first 3 characters
        # check to see if there are enough characters
        if ml < 3:
            v = msg
            for i in range(3 - ml):
                v = v + 'A'
            msg = ''

        else:
            # take the first 3 characters in a string
            v = msg[0:3]
            # remove the characters being used
            msg = msg[3:]

        # type being used
        if t == 'e':
            v_c = encrypt(key_m, v)
        else:
            v_c = decrypt(key_m, v)
            # return error
            if v_c == "-1":
                return "-1"

        msg_e = msg_e + v_c

    return msg_e


# main function for user inputs
def main():

    # uses a specific keyword where the key matrix has a guaranteed det and inverse
    print('The Program will used the keyword BACKUPABC')
    key = 'BACKUPABC'
    print("Input Message to encrypt: ")
    msg_p = input()
    msg_p = filter_plain_text(msg_p)

    msg_c = split_msg(key, msg_p, 'e')
    print("The encrypted message is: " + msg_c)

    print("Decrypting....")
    msg_p = split_msg(key, msg_c, 'd')
    if msg_p == -1:
        msg_p = "Key does not have an inverse. Try a different key."
    print("The decrypted message is: " + msg_p)
    return


# runs program
if __name__ == '__main__':
    main()


