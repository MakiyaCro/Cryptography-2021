# File to store all the commonly used math functions within cryptography

# Basic function to find the greatest common divisor
def my_gcd(a, b):
    # Swaps a and b to if a is greater than b to make function easier
    if a > b:
        t = a
        a = b
        b = t

    # Base return case
    if a == 0:
        # GCD
        return b

    # Takes the modulus of b and a and continues until base case is reached
    return my_gcd(b % a, a)


# Function to find the greatest common divisor along with the X and Y for Extended GCD
def my_extended_gcd(a, b):
    # Swaps a and b to if a is greater than b to make function easier
    if a > b:
        t = a
        a = b
        b = t

    # Base return case
    if a == 0:
        x = 0
        y = 1

        # Returns GCD, and the x and y used in the extended
        return b, x, y

    # Uses returned values to walk back through extended GCD
    g, x1, y1 = my_extended_gcd(b % a, a)
    # walks backwards using extended euclidean
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y


# Function that uses extended GCD to find the Modular inverse
def my_mod_inverse(a, m):
    # used to get both GCD to see if there is even an inverse and x
    g, x, y = my_extended_gcd(a, m)

    # in case no inverse is found return -1
    if g != 1:

        return -1
    else:
        # checks modulo and returns inverse
        res = (x % m)
        return res


# Function used to find the square root of a (mod n)
def my_sqr_roots_find(a, m):
    # First make sure a is within modulo n
    roots = ''
    if a > m:
        a = a % m

    # walk through all the possibilities between 1 and n
    for i in range(1, m):
        # s would be the square of i
        s = i * i
        # If i is a root add it on to the list of roots
        if s % m == a:
            roots = roots + str(i) + ' '

    # If no roots were added to the root list then update message
    if roots == '':
        roots = "No Roots were found for" + str(a) + "(mod" + str(m) + ")"

    return roots
