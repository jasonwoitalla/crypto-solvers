import fast_powering
from extended_euclidean_algorithm import extended_euclidean_algo


END_LINE = "\\\\\n"


def chinese_remainder_theorem(system, verbose=True):
    '''Given an input tuple list representing a modular system of of equations, this will solve the system using the chinese remainder theorem'''
    # system = [(h_a, n_a), (h_b, n_b), (h_c, n_c)]
    if verbose:
        print("Computing Chinese Remainder Theorem on system of congruence", end=END_LINE)
        for h, n in system:
            print("$x \\equiv {}(\\text{{mod }} {})$".format(h, n), end=", ")
        print("", end=END_LINE)

    # compute extended euclidean algorithm pairs
    verbose_modulos = []
    gcd_pairs = []
    final_mod = 1

    if verbose:
        print("Compute extended euclidean algorithm on series of pairs", end=END_LINE)
    for i in range(len(system)):
        a = 1
        for j in range(len(system)):
            if i != j:
                a *= system[j][1]
        b = system[i][1]
        if verbose:
            print("Computing with pair $({}, {})$".format(a, b), end=END_LINE)
        final_mod *= system[i][1]
        verbose_modulos.append(system[i][1])
        gcd, u, v = extended_euclidean_algo(a, b, True)
        print("\\\\")
        gcd_pairs.append((a, gcd, u, v))
    
    x = 0
    if verbose:
        print("Back to chinese remainder theorem calculation", end=END_LINE)
        print("Compute new final modulo: $", end="")
        for i in range(len(verbose_modulos)-1):
            print("{}*".format(verbose_modulos[i]), end="")
        print("{} = {}$".format(verbose_modulos[-1], final_mod), end=END_LINE)
    for i in range(len(system)):
        if verbose:
            old_x = x
            x += (system[i][0] * gcd_pairs[i][0] * gcd_pairs[i][2]) % final_mod
            x %= final_mod
            print("Adding to our sum: ${} = {} + [{} * {}](\\text{{mod }} {})$".format(x, old_x, gcd_pairs[i][0], gcd_pairs[i][2], final_mod), end=END_LINE)
        else:
            x += (system[i][0] * gcd_pairs[i][0] * gcd_pairs[i][2]) % final_mod
            x %= final_mod
        
    if verbose:
        print("Answer to system: $x \\equiv {}(\\text{{mod }} {})$".format(x, final_mod), end=END_LINE)
    return x, final_mod

inputs = [
    [(2, 3), (3, 5), (2, 7)]
]

if __name__ == "__main__":
    for system in inputs:
        print("Solution: " + str(chinese_remainder_theorem(system)), end=END_LINE)
        print("\\\\")
        