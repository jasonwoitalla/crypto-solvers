def euclidean_algo_rec(a, b, a0, b0, verbose=False):
    # Base Case
    if a == 0 :
        if verbose:
            print("Found GCD = " + str(b), end="\\\\\n")
        return b,0,1

    if verbose and a != a0 and b != b0: # print gcd calculation table
        print("$\\text{gcd}(" + str(b) + ", " + str(a) + ") = " + str(a) + "(" + str(b//a) + ")" + " + " + str(b%a) + "$", end="\\\\\n")         
    gcd,x1,y1 = euclidean_algo_rec(b%a, a, a0, b0, verbose)
     
    x = y1 - (b//a) * x1
    y = x1
    if verbose: # print the return back up to solutions u, v
        print("$" + str(gcd) + " = " + str(b) + "(" + str(y) + ")" + " + " + str(a) + "(" + str(x) + ")$", end="\\\\\n")

    return gcd,x,y


def extended_euclidean_algo(a, b, verbose=False):
    gcd,u,v = euclidean_algo_rec(a, b, a, b, verbose)
    if verbose: 
        print("Extended euclidean algorithm: $" + str(gcd) + " = " + str(a) + "(" + str(u) + ") + " + str(b) + "(" + str(v) + ")$\\\\")
    return gcd, u, v


def gcd_euclidean_algo(a, b, verbose=False):
    last_r = a
    q = a // b
    r = a % b

    stack = []
    stack.append((a,b,r))

    while r != 0:
        if verbose:
            print("({}, {})    {} = {} * {} + {}".format(a, b, a, b, q, r))
        a = b
        b = r
        q = a // b
        last_r = r
        r = a % b
        stack.append((a,b,r))
    
    if verbose:
        print("({}, {})    {} = {} * {} + {}".format(a, b, a, b, q, r))
        print("GCD = {}".format(last_r))
    gcd = last_r

    while len(stack) > 0:
        (my_a, my_b) = stack.pop()
        if verbose:
            print("au + bv = gcd")

    return gcd


if __name__ == "__main__":
    inputs = [
        ((7*43), 8),
        ((8*43), 7),
        ((8*7), 43)
    ]

    for m,n in inputs:
        print("Begin extended euclidean algorithm\\\\")
        print(extended_euclidean_algo(m, n, True), end="\\\\\n")
        print("\\\\")
