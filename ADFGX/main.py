import numpy as np


# filters out non alphabetical characters and converts the string to uppercase
def filter_plain_text(text):
    # filter out spaces and make letters upper case
    t_text = ''.join(c for c in text if c.isalpha())
    t_text = t_text.upper()

    return t_text


# this function is used to determine the new order of the key when sorted alphabetically
# the max key length for this program would be 13 characters long
def sort_key(key):
    key_s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    key_l = []

    # builds a list from the key string
    for i in key:
        key_l.append(i)

    # walks through and sorts the key alphabetically
    for i in range(len(key_l)):
        j = i
        while j > 0:
            # swaps both the key and the position values
            if ord(key_l[j]) < ord(key_l[j-1]):
                a = key_s[j-1]
                b = key_s[j]
                key_s[j - 1] = b
                key_s[j] = a

                a = key_l[j-1]
                b = key_l[j]
                key_l[j - 1] = b
                key_l[j] = a
            j = j - 1

    # returns the key positions
    return key_s


# used for the building the 2D arrays and swapping cols based off of sort functions
def text_key_encrypt(key, text):
    text_t = text
    text_c = ''

    # initialize sizes of arrays
    w = len(key)

    if len(text) % len(key) == 0:
        h = int(len(text) / len(key))
    else:
        h = int(len(text) / len(key)) + 1
    # build arrays
    text_m = [["" for x in range(w)] for y in range(h)]
    text_sm = [["" for x in range(w)] for y in range(h)]

    # builds the non sorted matrix
    r = 0
    c = 0
    while text_t:
        text_m[r][c] = text_t[0]
        # remove the front of th text
        text_t = text_t[1:]
        c = c+1
        if c == len(key):
            c = 0
            r = r + 1

    # sort key alphabetically
    key_num = sort_key(key)

    # build new cipher matrix
    for i in range(len(key)):
        for j in range(len(text_m[0])-1):
            text_sm[j][i] = text_m[j][key_num[i]]

    # convert the matrix into a string
    for i in range(len(key)):
        for j in range(len(text_sm[0])-1):
            text_c = text_c + text_sm[j][i]

    return text_c


# converts plain text into cypher values
def encrypt(m_plain, m_code, key, text):

    text_c = ''
    c_char = ''
    # walk through the string and find the equivalent in m_plain to m_code then
    # sort for key word
    for i in range(len(text)):
        flag = 'c'
        p_char = text[i]

        # find the value on the two key tables
        # breaks are to reduce the time going through loops
        for j in range(5):
            for k in range(5):
                # Check the single exception
                if p_char == 'J':
                    p_char = 'I'

                if p_char == m_plain[j][k]:
                    c_char = m_code[j][k]
                    flag = 'd'
                    break
            if flag == 'd':
                break

        # build cypher string
        text_c = text_c + c_char

    # go into swap encryption section
    text_c = text_key_encrypt(key, text_c)

    return text_c


# determines the number of rows for each col for decryption based off of the key and message length
def determine_row_length(key, message):
    row_length = []
    # if there is no remainder it makes life easier
    if len(message) % len(key) == 0:
        for i in range(len(key)):
            # finds number of rows
            rows = int(len(message) / len(key))
            # adds them all the list
            row_length.append(rows)
    else:
        # find remainder
        r = len(message) % len(key)
        for i in range(len(key)):
            # add one to each col until there are no remainders
            if r != 0:
                rows = int(len(message) / len(key) + 1)
            else:
                rows = int(len(message) / len(key))

            row_length.append(rows)
            r = r - 1

    return row_length


# similar to sort key but is used to build the encrypted matrix that was sorted alphabetically
def sort_row(key, row_l):
    t_row_l = row_l
    key_l = []

    # builds a list from the key string
    for i in key:
        key_l.append(i)

    # walks through and sorts the key alphabetically while swapping row locations
    for i in range(len(key_l)):
        j = i
        while j > 0:
            # general swap
            if ord(key_l[j]) < ord(key_l[j - 1]):
                a = t_row_l[j - 1]
                b = t_row_l[j]
                t_row_l[j - 1] = b
                t_row_l[j] = a

                a = key_l[j - 1]
                b = key_l[j]
                key_l[j - 1] = b
                key_l[j] = a
            j = j - 1

    return t_row_l


# takes care of un-swapping rows within the arrays and outputs a un-sorted string
def text_key_decrypt(key, text):
    text_c = ''
    text_t = text
    w = len(key)

    if len(text) % len(key) == 0:
        h = int(len(text) / len(key))
    else:
        h = int(len(text) / len(key)) + 1
    # build arrays
    text_m = [["" for x in range(w)] for y in range(h)]
    text_sm = [["" for x in range(w)] for y in range(h)]
    # determine the length of each row
    row_l = determine_row_length(key, text)
    row_l = sort_row(key, row_l)
    # get the sorted key
    key_num = sort_key(key)

    # builds sorted array based off of number of rows for each col
    r = 0
    c = 0
    while text_t:
        text_sm[r][c] = text_t[0]
        # remove the front of th text
        text_t = text_t[1:]
        r = r + 1
        if r == row_l[c]:
            r = 0
            c = c + 1

    # builds unsorted table based off of the sorted key
    for i in range(len(key)):
        for j in range(len(text_m[0]) - 1):
            text_m[j][key_num[i]] = text_sm[j][i]

    # converts array into string
    for i in range(len(key) - 1):
        for j in range(len(text_sm[0])):
            text_c = text_c + text_m[i][j]

    return text_c


# converts cypher text into plain text
def decrypt(m_plain, m_code, key, text):
    msg = ''
    # sends to un-sort the arrays based off key and text
    text_c = text_key_decrypt(key, text)

    # walk through the string and find the equivalent in m_code to m_plain
    for i in range(0, len(text_c), 2):
        flag = 'c'
        c_char = text_c[i] + text_c[i+1]
        p_char = ''

        for j in range(5):
            for k in range(5):
                if c_char == m_code[j][k]:
                    p_char = m_plain[j][k]
                    flag = 'd'
                    break
            if flag == 'd':
                break

        msg = msg + p_char

    # decrypted message
    return msg


# The primary function that accepts user inputs
def main():
    # m_plain is a matrix that can be defined by a user but for this example it will be simpler if it is predefined
    m_plain = [['P', 'H', 'Q', 'G', 'M'],
               ['E', 'A', 'Y', 'N', 'O'],
               ['F', 'D', 'X', 'K', 'R'],
               ['C', 'V', 'S', 'Z', 'W'],
               ['B', 'U', 'T', 'I', 'L']]
    # general conversion matrix
    m_code = [['AA', 'AD', 'AF', 'AG', 'AM'],
              ['DA', 'DD', 'DF', 'DG', 'DX'],
              ['FA', 'FD', 'FF', 'FG', 'FX'],
              ['GA', 'GD', 'GF', 'GG', 'GX'],
              ['XA', 'XD', 'XF', 'XG', 'XX']]

    # can use a custom key word but for simplicity and it not being specified MONKEY will be used
    print("This Program will be using the keyword: MONKEY")
    key_word = 'MONKEY'

    print("The Encryption table that is used is: ")
    print(np.matrix(m_plain))

    print("Input Message to encrypt: ")
    msg_p = input()
    msg_p = filter_plain_text(msg_p)

    msg_c = encrypt(m_plain, m_code, key_word, msg_p)
    print("The encrypted message is: " + msg_c)

    print("Decrypting.......")
    msg_p = decrypt(m_plain, m_code, key_word, msg_c)
    print("The decrypted message is: " + msg_p)

    return


if __name__ == '__main__':
    main()
