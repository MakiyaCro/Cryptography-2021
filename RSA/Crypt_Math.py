# File to store all the commonly used math functions within cryptography
import math
import random


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


# used to determine if a given number is prime or not
def is_prime(n):
    # smallest prime that is even case
    if n == 2:
        return True
    # other base case for less than two or mod 2
    elif n < 2 or n % 2 == 0:
        return False

    elif n > 2:
        # limits the amount to sqrt(n) + 1
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True


# used to generate a random prime number
def random_prime(b):
    p_list = []
    # boundary
    u_bound = 2**(b+1) - 1
    l_bound = 2**b - 1
    for n in range(l_bound, u_bound):
        if is_prime(n):
            p_list.append(n)

    p_random = random.choice(p_list)
    return p_random


# the Fermat's factorization method
def factor_fermat(n):
    factors = []

    # divides by two case
    if n % 2 == 0:
        factors.append(2)
        factors.append(int(n / 2))
        return factors

    # limit the boundary of a
    a = math.ceil(math.sqrt(n))

    if a * a == n:
        factors.append(a)
        return factors

    # the main algorithm
    while True:
        b1 = a * a - n
        b = int(math.sqrt(b1))
        if b * b == b1:
            break
        else:
            a += 1

    # add to the factors
    factors.append(a-b)
    factors.append(a+b)
    return factors


# pollard roh method. main algorithm is based off wikipedia algorithm
def factor_pollard_r(n):
    factors = []

    # two divides
    if n % 2 == 0:
        factors.append(2)
        factors.append(int(n/2))
        return factors

    x = 2
    y = x
    g = 1

    # base case is 1
    while g == 1:
        # uses base function found on google wikipedia
        x = (x * x - 1) % n
        # nested function
        y = (y * y - 1) % n
        y = (y * y - 1) % n
        # uses the gcd to check if it they are a factor
        g = my_gcd(abs(x - y), n)
    # adding the factors
    factors.append(g)
    factors.append(int(n/g))

    return factors


# pollard p-1 algorithm
def factor_pollard_p(n):
    # base numbers
    factors = []
    a = 2
    i = 2

    # will continue looping until a prime factor is found
    while True:
        a = (a ** i) % n

        # finding gcd of a-1 and n
        d = my_gcd((a - 1), n)

        if d > 1:
            # return the factor
            factors.append(d)
            factors.append(int(n/d))
            return factors
        else:
            i += 1


# checks if a value is a square or not
def is_perf_sqr(x):
    # gets a rounded square root based off floor
    y = math.floor(int(math.sqrt(x)))
    if y*y == x:
        return True
    else:
        return False


# based of of the algorithm found on wikipedia
def factor_shanks(n):
    # initialize values
    factors = []

    p = []
    q = []
    b = []
    temp = int(math.floor(math.sqrt(n)))
    p.append(temp)
    q.append(1)
    q.append(n - temp ** 2)
    # filler value
    b.append(0)

    loop = True
    i = 1

    while loop:
        # sets up the first set of variables
        b.append((temp + p[i-1])/q[i])
        p.append(b[i]*q[i] - p[i-1])
        q.append(q[i-1] + b[i]*(p[i-1] - p[i]))

        # checks if q[i+1] is a perfect square
        if is_perf_sqr(q[i+1]):
            # if it iis initialize values
            d_q = int(math.sqrt(q[i+1]))
            b[0] = (temp - p[i]) / d_q
            p[0] = b[0] * d_q + p[i]
            q[0] = d_q
            q[1] = (n - p[0] ** 2) / d_q

        # checks p array and if values are the same then the gcd of the value and n is a factor
        elif p[i] == p[i - 1]:
            # determines factor based of gcd
            x = my_gcd(n, p[i])
            factors.append(int(x))
            factors.append(int(n/x))
            return factors

        i += 1


# main factor function that selects one of the factor functions
def factor(n, m):
    factors = []

    # returns an error if a negative number or zero is passed in
    if n <= 0:
        return factors.append(-1)

    # goes though and selects which factor method is used
    if m == 'f':
        factors = factor_fermat(n)
    elif m == 'r':
        factors = factor_pollard_r(n)
    elif m == 'p':
        factors = factor_pollard_p(n)
    elif m == 's':
        factors = factor_shanks(n)
    else:
        return factors.append(-1)

    return factors
