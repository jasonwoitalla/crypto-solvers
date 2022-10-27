import math
def is_prime(p, verbose=False):
    if verbose:
        print("Checking if " + str(p) + " is prime.", end="\\\\\n")
    for i in range(2, int(math.sqrt(p))+1):
        if verbose:
            print("Checking $" + str(p) + " \\mod " + str(i) + " = " + str(p%i) + "$", end="\\\\\n")
        if p%i == 0:
            if verbose:
                print("$" + str(p) + "$ is divisible by $" + str(i) + "$. Therefore $" + str(p) + "$ is not prime.", end="\\\\\n")
            return False
    if verbose:
        print("Verified all numbers $2 \\leq x \\leq " + str(int(math.sqrt(p))) + "$ and not factors of " + str(p) + ". Therefore it is prime.", end="\\\\\n")
    return True

is_prime(123456789, True)