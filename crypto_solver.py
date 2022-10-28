import sys
from extended_euclidean_algorithm import extended_euclidean_algo
from fast_powering import fast_pow
from is_prime import is_prime
from chinese_remainder_theorem import chinese_remainder_theorem
from pohlig_hellman import pohlig_hellman


modes = ["gcd", "fast-pow", "is-prime", "crt", "shanks", "pohlig"]


if __name__ == "__main__":
    mode = ""
    try:
        while True:
            if mode == modes[0]:
                print("[GCD] Performing 'Extended Euclidean Algorithm' please enter the two numbers you would like to solve 'au + bv = gcd(a,b)'")
                print("[GCD] Enter 'c' if you would like to go back to the main menu")
                my_input = input("[GCD] Numbers: ")
                if my_input != "c":
                    tuple_input = tuple(my_input.split())
                    extended_euclidean_algo(int(tuple_input[0]), int(tuple_input[1]), True)
                else:
                    mode = ""
            elif mode == modes[1]:
                print("[Fast Pow] Performing 'Fast Powering' please enter the numbers g^x(mod p) in that order to perform the algorithm")
                print("[Fast Pow] Enter 'c' if you would like to go back to the main menu")
                my_input = input("[Fast Pow] Enter g^x(mod p): ")
                if my_input != "c":
                    tuple_input = tuple(my_input.split())
                    fast_pow(int(tuple_input[0]), int(tuple_input[1]), int(tuple_input[2]), True)
                else:
                    mode = ""
            elif mode == modes[2]:
                print("[Is Prime] Performing 'Is Prime' check please enter the a prime to check")
                print("[Is Prime] Enter 'c' if you would like to go back to the main menu")
                my_input = input("[Is Prime] Enter a prime: ")
                if my_input != "c":
                    tuple_input = tuple(my_input.split())
                    is_prime(int(tuple_input[0]), True)
                else:
                    mode = ""
            elif mode == modes[3]:
                print("[CRT] Performing 'Chinese Remainder Theorem' please enter a congruence system to solve.")
                print("[CRT] Format: (h1, n1) (h2, n2) (h3 n3) ...")
                print("[CRT] Enter 'c' if you would like to go back to the main menu")
                my_input = input("[CRT] Enter a system: ")
                if my_input != "c":
                    system_list = my_input.split()
                    system = []
                    for congruence in system_list:
                        congruence = congruence[1:-1]
                        congruence = congruence.split(",")
                        system.append((int(congruence[0]), int(congruence[1])))
                    chinese_remainder_theorem(system, True)
                else:
                    mode = ""
            elif mode == modes[4]:
                pass
            elif mode == modes[5]: 
                print("[POHLIG] Performing 'Pohlig Hellman Algorithm' to solve the discrete log problem g^x = h(mod p)")
                print("[POHLIG] Enter 'c' if you would like to go back to the main menu")
                my_input = input("[POHLIG] Enter g^x = h(mod p): ")
                if my_input != "c":
                    tuple_input = tuple(my_input.split())
                    pohlig_hellman(int(tuple_input[0]), int(tuple_input[1]), int(tuple_input[2]))
                else:
                    mode = ""
            else: # we are not in a mode
                print("")
                print("[Main Menu] Please select a mode to enter:")
                print("[Main Menu] Available modes: ", end="")
                for my_mode in modes:
                    print(my_mode, end=", ")
                print("")
                my_input = input("[Main Menu] Mode: ")
                if my_input == "c":
                    sys.exit("Crypto Solver terminated")
                else:
                    mode = my_input
    except KeyboardInterrupt:
        print("\nCrypto Solver terminated")
