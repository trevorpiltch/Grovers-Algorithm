import sys
import random

def get_N():
    """Asks for the number of qubits to use and runs checks on it"""
    print("Specify number of qubits 4...16, or leave blank for a random amount.")
    N = input("N=")

    try:
        N = int(N)

        if (N < 4) | (N > 16):
            print("Must be in the range 4...16. Exiting program.")
            sys.exit(0)
        else:
            return N
    except ValueError:
        if N != "":
            print("Must be an integer. Exiting program.")
            sys.exit(0)
        else:
            N = random.randint(4, 16)
            print("Number of qubits is %i" % N)
            return N

def get_target(N):
    """Asks for target number and runs checks"""
    print("Enter target number (4...%i) or leave blank for random number." % (2**N))
    t = input("Target=")

    try:
        t = int(t)

        if (t < 0) | (t > 2**N):
            print("Must be in the range 4...%i. Exiting program." % (2**N))
            sys.exit(0)
        else:
            return t
    except ValueError:
        if t != "":
            print("Must be an integer. Exiting program.")
            sys.exit(0)
        else:
            t = random.randint(4, 2 ** N)
            print("Target number is %i" % t)
            return t

