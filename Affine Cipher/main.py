from Crypt_Math import *


# encryption formula for affine
def encrypt(text, m, o):
    t_text = ''
    # Walk through message
    for i in text.split():
        if i.isdigit():
            # Go through encryption equation
            t_text = t_text + str(((int(m) * int(i) + int(o)) % 26)) + " "

    # Returns numerical encrypted message
    return t_text


# decryption for affine
def decrypt(text, a, b):
    n_text = ''
    t_text = ''

    # Converts Alpha to numeric string
    for i in text.split():
        n = ord(i) - ord('A')
        n_text = n_text + str(n) + " "

    # Finds mod inverse for decrypt equation
    inv = my_mod_inverse(int(a), 26)

    # no inverse for a
    if inv == -1:

        return "no"

    # Walks through numerical string and decrypts using key and mod inverse
    for i in n_text.split():
        if i.isdigit():
            t_text = t_text + str(((int(inv) * (int(i) - int(b))) % 26)) + " "

    return t_text


# converts numerical string to alphabet
def convert_num_to_alpha(text):
    t_text = ''

    # walks through numerical string and outputs alphabetical version
    for i in text.split():
        # Based off of ascii values
        c = int(int(i) + ord('A'))
        t_text = t_text + chr(c) + " "

    return t_text


# used to convert plain text into numerical plain text
def filter_plain_text(text):
    # initialize strings
    n_text = ''
    # filter out spaces and make letters upper case
    t_text = ''.join(c for c in text if c.isalpha())
    t_text = t_text.upper()

    # walk through string and convert to numerical equivalent
    for i in t_text:
        n = ord(i) - ord('A')
        n_text = n_text + str(n) + " "

    return n_text


# Bruteforce Attack
def Brute_Force_Attack(text):
    n_text = ''
    text = text.upper()
    # adding spaces to text
    for i in text:
        n_text = n_text + i + " "

    # walks through all a and b combinations to figure out the text
    for i in range(26):
        for j in range(26):
            t_text = decrypt(n_text, i, j)
            # prints out the text only if a mod inverse was found
            if t_text != "no":
                t_text = convert_num_to_alpha(t_text)
                print(t_text, '\n')

    return


# Know Two Letters Attack
def Known_Letters_Attack(text, c_1, c_2, p_1, p_2):
    # make sure cipher is correctly made
    text = text.upper()
    n_text = ''
    for i in text:
        n_text = n_text + i + " "

    # c_1 = p_1a + b mod 26
    # c_2 = p_2a + b mod 26
    # make sure everything is in upper case and convert to numerical equivalent
    c_1 = c_1.upper()
    c_2 = c_2.upper()
    p_1 = p_1.upper()
    p_2 = p_2.upper()
    c_1 = ord(c_1) - ord('A')
    c_2 = ord(c_2) - ord('A')
    p_1 = ord(p_1) - ord('A')
    p_2 = ord(p_2) - ord('A')

    # start to finding a value
    c = c_1 - c_2
    p = p_1 - p_2

    # if a is not a regular integer then fond modular inverse of fraction
    a = c / p
    if a - int(a) == 0:
        a = a % 26
    else:
        b_inv = my_mod_inverse(p, 26)
        a = (b_inv * c) % 26

    b = -1
    # walks through range of mudulo and finds b
    for i in range(26):
        c_t = (p_1*a + i) % 26
        if c_t == c_1:
            b = i

    if b == -1:
        print("unable to decrypt")

    # if a key was found i will decrypt the message
    else:
        n_text = decrypt(n_text, a, b)
        p_text = convert_num_to_alpha(n_text)
        print("Your attacked cipher is: ", p_text)

    return


# Main function used for user input and program output
def main():
    # Provides two different options for the user to use
    print("Encrypt(e) or Decrypt(d) or Attack(a) message?")
    t = input()

    if t == 'e':
        print("What would you like the multiplier to be (number)?")
        multiplier = input()
        print("What would you like the offset to be (number)?")
        offset = input()
        print("Enter in the text you would like to encrypt")
        p_text = input()

        # filters out spaces and any unwanted characters
        p_text = filter_plain_text(p_text)

        print("Encrypting.......")
        # returns encrypted numerical string
        c_text = encrypt(p_text, multiplier, offset)
        c_text = convert_num_to_alpha(c_text)
        print("The encrypted message is: ", c_text)

        # returns decrypted numerical string
        p_text = decrypt(c_text, multiplier, offset)
        p_text = convert_num_to_alpha(p_text)
        print("The decrypted message is: ", p_text)

    if t == 'd':
        print("What is the multiplier?")
        multiplier = input()
        print("What is the offset?")
        offset = input()
        print("Enter the text you would like to decrypt")
        c_text = input()

        c_text = filter_plain_text(c_text)
        c_text = convert_num_to_alpha(c_text)
        print("Decrypting.......")
        p_text = decrypt(c_text, multiplier, offset)
        p_text = convert_num_to_alpha(p_text)
        print("The decrypted message is: ", p_text)

    if t == 'a':
        print("Would you like to use brute force(b) or known letter attack(k): ")
        a_type = input()
        if a_type == 'b':
            print("Enter the text you would like to attack(upper case no spaces): ")
            c_text = input()
            Brute_Force_Attack(c_text)

        if a_type == 'k':
            print("Enter the text you would like to attack: ")
            c_text = input()
            print("Enter first cipher text character: ")
            c_1 = input()
            print("Enter what letter the first cipher text character maps to: ")
            p_1 = input()
            print("Enter second cipher text character: ")
            c_2 = input()
            print("Enter what letter the second cipher text character maps to: ")
            p_2 = input()

            Known_Letters_Attack(c_text, c_1, c_2, p_1, p_2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
