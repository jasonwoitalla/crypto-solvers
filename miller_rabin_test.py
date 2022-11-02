from extended_euclidean_algorithm import extended_euclidean_algo
from fast_powering import fast_pow

END_LINE = "\\\\\n"

# Miller-Rabin test
# returns true if a is a composite witness of n
def miller_rabin(n, a, verbose=True):
    if verbose:
        print("Checking if {} is a composite witness of {}".format(a, n), end=END_LINE)

    # CHECK 1
    if n % 2 == 0: # even numbers are not prime
        if verbose:
            print("{} is even, therefore it is composite".format(n), end=END_LINE)
        return True

    if verbose:
        print("Finding $\\text{{gcd}} ({}, {})$".format(n, a), end=END_LINE)
    gcd, u, v = extended_euclidean_algo(n, a, verbose)
    if 1 < gcd < n:
        if verbose:
            print("{} is not prime, because $\\text{{gcd}} ({}, {}) = {}$ is greater than one and less than {}".format(n, n, a, gcd, n), end=END_LINE)
        return True

    # CHECK 2
    # Find q and k such that n-1 = 2^k * q
    q = n - 1
    k = 0
    while q % 2 == 0:
        q //= 2
        k += 1
    if verbose:
        print("Found that $n-1 = 2^{{ {} }} * {}$".format(k, q), end=END_LINE)

    # CHECK 3
    # Compute x^q mod n
    if verbose:
        print("Compute ${}^{{ {} }} \\mod {}$".format(a, q, n), end=END_LINE)
    x = fast_pow(a, q, n, True)

    # CHECK 4
    if x == 1 :
        if verbose:
            print("FAILED! ${}^{{ {} }} \\mod {} = 1$, therefore the test failed.".format(a, q, n), end=END_LINE)
        return False
    
    if x == n - 1:
        if verbose:
            print("FAILED! ${}^{{ {} }} \\mod {} = {}$, therefore the test failed.".format(a, q, n, n-1), end=END_LINE)
        return False

    # CHECK 5
    if verbose:
        print("Looping through $i = 0, 1, \\ldots, {}-1$ to check if ${}^{{ {} * i}} \\mod {} = -1$ for any $i$".format(k, x, q, n), end=END_LINE)
    
    for _ in range(k - 1):
        # CHECK 6
        if x == n - 1:
            if verbose:
                print("FAILED! ${}^{{ {} }} \\mod {} = -1$, therefore the test has failed.".format(a, q, n), end=END_LINE)
            return False
        # CHECK 7
        if verbose:
            print("Compute ${}^{{2 * {} }} \\mod {}$".format(x, q, n), end=END_LINE)
        x = fast_pow(x, 2, n, True)
    if verbose:
        print("${}^{{ {} }} \\mod {} \\neq -1$ for any i, therefore {} is composite".format(a, q, n, n), end=END_LINE)
    return True