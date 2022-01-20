from Crypt_Math import *


# used to filter text to make encryption and decryption easier
def filter_plain_text(text):
    # initialize strings
    n_text = ''
    # filter out spaces and other characters
    t_text = ''.join(c for c in text if c.isalpha())
    t_text = t_text.upper()
    # walk through string and convert to numerical equivalent
    for i in t_text:
        n = ord(i) - ord('A') + 1
        n_text = n_text + str(n) + " "

    return n_text


# main encryption algorithm for rsa
def encrypt(e, n, msg):
    text_e = []
    # uses the main algorithm found in the book
    # walks through the individual characters and encrypts them
    for i in msg.split():
        m = int(i)
        c = (m**e) % n
        text_e.append(c)

    # returns numerical encryption
    return text_e


# main decryption algorithm for rsa
def decrypt(d, n, msg):
    d_text = ''
    for i in msg.split():
        t = int(i)**d % n
        # converts back to text
        c = chr(t + ord('A') - 1)
        d_text = d_text + c

    return d_text


# the main input section of the program
# user can select either rsa or factoring a number
def main():
    e = 0
    # determines what will be run
    print("Would you like to use the RSA algorithm or Factor a number? (R of F)")
    typ = input()
    # rsa module
    if typ == 'R' or typ == 'r':
        # either takes user input or creates its own input
        print("Generate or enter yor primes? (G or E)")
        typ = input()
        if typ == 'E' or typ == 'e':
            print("Enter a prime number p")
            p = int(input())
            print("Enter a prime number q")
            q = int(input())

            i = 0
            while i != 1:
                print("Enter an e with a gcd(e,(p-1)(q-1)) = 1")
                e = int(input())
                t = my_gcd(e, (p - 1) * (q - 1))
                if t == 1:
                    i = 1
                else:
                    print("Your e does not fit the criteria above. Try again")

        # generates user values based off of 2^n size
        elif typ == 'G' or typ == 'g':
            print("What size primes would you like to generate? (2^size)")
            size = int(input())
            print("Generating values......")
            p = random_prime(size)
            print("p is: " + str(p))
            q = random_prime(size)
            print("q is: " + str(q))
            i = 2
            e_list = []
            while i < (p-1)*(q-1):
                t = my_gcd(i, (p - 1) * (q - 1))
                if t == 1:
                    e_list.append(i)
                i += 1

            e = random.choice(e_list)
            print("e is: " + str(e))

        else:
            print("Incorrect input. Program ending....")
            return

        n = p * q

        # generate d
        print("Generating d value.....")
        d = my_mod_inverse(e, (p-1)*(q-1))
        if d == -1:
            print("error finding d")
            return
        print("Your d value is: " + str(d))

        print("Enter the message to encrypt")
        msg = input()
        msg = filter_plain_text(msg)

        # encrypt message
        e_msg = encrypt(e, n, msg)
        msg = ''
        for i in e_msg:
            msg = msg + str(i) + " "

        # print encrypted message
        print("Encrypted message is: " + msg)
        # decrypt message
        msg = decrypt(d, n, msg)
        # print decrypted message
        print("Decrypted message is: " + msg)

    # factorization module
    elif typ == 'F' or typ == 'f':
        f_list = []
        print("Enter the number you would like to factor: ")
        n = int(input())
        # checks if the user input is prime
        if is_prime(n):
            print("This is a prime number")
            return

        # choose factor type
        print("Choose the type of factoring: fermat(f), pollard p-1(p), pollard rho(r), shanks(s)")
        typ = input()

        f_list = factor(n, typ)
        if f_list[0] == -1:
            print("error when factoring")
            return

        print("Some factors for " + str(n) + " are:")
        for i in range(len(f_list)):
            print("Factor #" + str(i) + ": " + str(f_list[i]))

    return


if __name__ == '__main__':
    main()
