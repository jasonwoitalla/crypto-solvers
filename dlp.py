def brute_force(g, h, p):
    for i in range(p):
        val = (g ** i) % p
        if val == h:
            print("[FOUND]" + str(i) + ": " + str(g) + "^{" + str(i) + "}(\\text{mod } " + str(p) + ") = " + str(val) + " = " + str(h))
            return i
        print(str(i) + ": " + str(g) + "^{" + str(i) + "}(\\text{mod } " + str(p) + ") = " + str(val) + " \\neq " + str(h) + "\\\\")

if __name__ == "__main__":
    brute_force(2, 893, 1373)
