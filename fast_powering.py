def fast_pow(g, x, p, verbose=False):
    # Checks if left-most bit is active and then multiply
    # our answer by the corresponding power of 2
    # if g == 2:
    #     if verbose:
    #         print("Performing Fast Powering Algorithm on $" + str(g) + "^{" + str(x) + "}(\\text{mod }" + str(p) + ")$", end="\\\\\n")
    #     res =  2 ** x % p
    #     if verbose:
    #         print("$" + str(g) + "^{" + str(x) + "}(\\text{mod }" + str(p) + ") = " + str(res) + "$", end="\\\\\n")
    #     return res

    res = 1
    count = 0
    exp = x
    base = g

    if verbose:
        print("Performing Fast Powering Algorithm on $" + str(g) + "^{" + str(exp) + "}(\\text{mod }" + str(p) + ")$", end="\\\\\n")
        print("Binary expansion of $" + str(exp) + "$: $" + bin(exp)[2:] + "$", end="\\\\\n")

    while x:
        if x & 1:
            if verbose:
                print("$2^{" + str(count) + "}$ is in our binary expansion.", end=" ")
                print("Our power is now $" + str(res) + "*" + str(base) + "(\\text{mod }" + str(p) + ") =", end=" ")
                print(str((res * base) % p) + "(\\text{mod }" + str(p) + ")$", end="\\\\\n")
            res = (res * base) % p
        elif verbose:
            print("$2^{" + str(count) + "}$ is not in our binary expansion. Squaring $" + str(base) + "$ for future use.", end=" ")
            print("$" + str(base) + "*" + str(base) + "(\\text{mod }" + str(p) + ") = " + str(base*base%p), end="$\\\\\n")
        x >>= 1
        base *= base # square our base
        base %= p
        count += 1
    
    if verbose:
        print("$" + str(g) + "^{" + str(exp) + "}(\\text{mod }" + str(p) + ") = " + str(res) + "$", end="\\\\\n")
    return res

inputs = [
    (614, 577, 1159)
]

if __name__ == "__main__":
    for g,x,p in inputs:
        fast_pow(g, x, p, True)
        print("\\\\")
    