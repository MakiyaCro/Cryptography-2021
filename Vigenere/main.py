# Used to filter out unwanted characters ans spaces
def filter_plain_text(text):
    # filter out spaces and make letters upper case
    t_text = ''.join(c for c in text if c.isalpha())
    t_text = t_text.upper()

    return t_text


# Matches key length to text key length
def build_key(text, key):

    # Makes sure the key is in uppercase
    key = key.upper()

    # Keep adding on key letters for the length of the plain text
    for i in range(len(text) - len(key)):
        key = key + key[i % len(key)]

    return key


# Uses full key to encrypt the the total plain text
def encrypt(text, key):
    t_text = ''

    # Walks through both the key and text at the same time and grab the same [i]
    for i in range(len(text)):
        k_t = key[i]
        t_t = text[i]
        # Add both the text i and key i then take the modulo of it
        t_text = t_text + chr(((ord(t_t) + ord(k_t)) % 26) + ord('A'))

    return t_text


# Very Similar to encrypt just subtracts the to values instead of adds
def decrypt(text, key):
    t_text = ''

    # Walks through both the key and text at the same time and grab the same [i]
    for i in range(len(text)):
        k_t = key[i]
        t_t = text[i]
        t_text = t_text + chr(((ord(t_t) - ord(k_t)) % 26) + ord('A'))

    return t_text


# Attack based on finding key length and key
def attack(text):
    t_text = ''

    return


# Main function used for user input and program output
def main():
    # Provides two different options for the user to use
    print("Would you like to encrypt(e) or decrypt(d): ")
    t = input()
    if t == 'e':
        print("What is your key?")
        key = input()

        print("What is your text?")
        text = input()

        # filters out spaces and any unwanted characters then builds key
        n_text = filter_plain_text(text)
        f_key = build_key(n_text, key)

        c_text = encrypt(n_text, f_key)
        print("The encrypted message is: ", c_text)

        p_text = decrypt(c_text, f_key)
        print("The decrypted message is: ", p_text)

    if t == 'd':
        print("What is your key?")
        key = input()

        print("What is your cipher text?")
        text = input()

        # filters out spaces and any unwanted characters then builds key
        n_text = filter_plain_text(text)
        f_key = build_key(n_text, key)

        p_text = decrypt(n_text, f_key)
        print("The decrypted message is: ", p_text)

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
