from fast_powering import fast_pow
from shank_babystep_giantstep import sbsgs_list
from chinese_remainder_theorem import chinese_remainder_theorem

END_LINE = "\\\\\n"


# Function to generate a list of prime factors of p
def find_prime_factors(p):
    prime_factors = {}
    c = 2
    while p > 1:
        if p % c == 0:
            if c in prime_factors:
                prime_factors[c] += 1
            else:
                prime_factors[c] = 1
            p /= c
        else:
            c += 1
    return prime_factors

# Solves discrete log g^x = h(mod p)
def pohlig_hellman(g, h, p, verbose=True):
    # Find all the prime factors of p-1
    print("Calculate prime factors of $p-1$", end=END_LINE)
    prime_factors = find_prime_factors(p-1)
    # print prime_factors in latex format
    print("Prime factors of $p-1$:", end=END_LINE)
    for key, value in prime_factors.items():
        print("${}^{}$,".format(key, value), end=" ")
    print("", end=END_LINE)
    print("", end=END_LINE)

    # Find the order of g mod p
    print("Find the order of $g$ mod $p$", end=END_LINE)
    order = p - 1
    for key, value in prime_factors.items():
        for i in range(value):
            power = fast_pow(key, i, p, True)
            if fast_pow(g, power, p, True) == 1:
                order = power
                break
    print("Order of $g$ mod $p$ is $r = {}$".format(order), end=END_LINE)
    print("", end=END_LINE)

    i = 1
    system = []
    for key, value in prime_factors.items():
        print("For $q_{} = {}$:".format(i, key), end=END_LINE)
        r = 1
        print("Computing $r_{}$:".format(i), end=END_LINE)
        for key2, value2 in prime_factors.items():
            if key != key2:
                r *= fast_pow(key2, value2, p, True) % p
        print("Let $r_{} = {}$".format(i, order // key), end=END_LINE)

        print("Computing $g_{}$:".format(i), end=END_LINE)
        my_g = fast_pow(g, r, p, True)

        print("Computing $h_{}$:".format(i), end=END_LINE)
        my_h = fast_pow(h, r, p, True)

        print("Computing $x_{0} = log_{{g_{{ {0} }} }}(h_{{ {0} }})$:".format(i), end=END_LINE)
        my_x = sbsgs_list(my_g, my_h, p, True)
        print("Let $x_{} = {}$".format(i, my_x), end=END_LINE)

        print("Finally compute the modulo $x_{}$:".format(i), end=END_LINE)
        modulo = fast_pow(key, value, p, True)

        system.append((my_x, modulo))
        print("", end=END_LINE)

        i += 1
    
    print("Solve the system of congruences using the chinese remainder theorem:", end=END_LINE)
    x, mod = chinese_remainder_theorem(system, True)
    print("$x = {} \\mod {}$".format(x, mod), end=END_LINE)
