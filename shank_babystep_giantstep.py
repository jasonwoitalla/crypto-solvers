import math
from fast_powering import fast_pow


def print_list(list):
    for pair in list:
        print(pair, end="\\\\\n")


def sorted_append(list, babystep, i):
    if len(list) == 0: # empty
        list.append((babystep, i))
    elif babystep < list[0][0]: # new first
        list.insert(0, (babystep, i))
    elif babystep > list[-1][0]: # new last
        list.append((babystep, i))
    else: # somewhere in the middle
        for k in range(1, len(list)):
            if list[k - 1][0] < babystep < list[k][0]:
                list.insert(k, (babystep, i))
                return


# Algorithm was got from: https://www.geeksforgeeks.org/python-program-for-binary-search/
def binary_search(list, bigstep):
    low = 0
    high = len(list) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if list[mid][0] < bigstep:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif list[mid][0] > bigstep:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1


# Developed based on the book's algorithm and this page https://en.wikipedia.org/wiki/Baby-step_giant-step
# solves g^x = h (mod p) also written log_g(h) (mod p)
def sbsgs_list(g, h, p, verbose=False):
    n = math.ceil(math.sqrt(p - 1))

    if verbose:
        print("First will use compute a table of baby steps. We will store all results into a sorted list using a sorted put function.", end="\\\\\n")
    list = []
    baby_power = 1
    if verbose:
        print("Adding: $1$ to our table.", end="\\\\\n")
    for i in range(n):
        sorted_append(list, baby_power, i)
        if verbose:
            print("Adding: $" + str(baby_power) + "*" + str(g) + "(\\text{mod }" + str(p) + ") = " + str(baby_power*g%p) + "$ to our table.", end="\\\\\n")
        baby_power = baby_power * g % p

    if verbose: 
        print("", end="\\\\\n")
        print("Computed Pair List", end="\\\\\n")
        print_list(list)
        print("Finally, check for collisions by using fast powering to calculate $(j, hg^{-jn})$ and check against our pair list")
        print("", end="\\\\\n")
        print("Compute $" + str(g) + "^{-" + str(n) + "}(\\text{mod } " + str(p) + ") = ", end="")
        print(str(g) + "^{" + str(p) + "-1-" + str(n) + "}(\\text{mod } " + str(p) + ")$", end="\\\\\n")

    g_inverse = fast_pow(g, p-1-n, p, verbose) # this is true because p is prime
    if verbose:
        print("", end="\\\\\n")
    power = 1

    for j in range(n):
        if verbose: print("Computing giantstep: $" + str(h) + "*" + str(power) + "(\\text{mod } " + str(p) + ") = " + str((h * power) % p) + "$", end="\\\\\n")
        giantstep = (h * power) % p
        if verbose: print("Checking pair: $(" + str(j) + ", " + str(giantstep) + ")$ for a collision", end="\\\\\n")
        idx = binary_search(list, giantstep)
        if idx >= 0: # There has been a collision
            pair = list[idx]
            x = pair[1] + (j * n)
            if verbose: 
                print("There was a collision on " + str(giantstep) + " with j = " + str(j) + " and i = " + str(pair[1]), end="\\\\\n")
                print("Solution the discrete log is: " + str(x), end="\\\\\n")
            return x
        power = (power * g_inverse) % p
    
    return None
    

if __name__ == "__main__":
    sbsgs_list(131, 3, 137, True)
