from qiskit import *
from oracle import *
from amplifier import *
from init import *
from args import *
from results import *
import time


def grover(circuit, n, target_binary, oracle, amplifier):
    """Applies the oracle and amplification on the circuit"""
    circuit.append(oracle, range(n+1))
    circuit.h(range(n+1))
    circuit.append(amplifier, range(n))
    circuit.h(range(n))

def run(n, target_binary):
    """Runs grovers algorithm with target binary"""
    qc = QuantumCircuit(n + 1, n)

    byte = "{0:0%ib}" % n
    target_binary = byte.format(target_binary)

    start_time = time.time()

    init(qc, n)

    oracle_gate = oracle(n, target_binary)
    amplifier_gate = amplifier(n)

    seconds = (time.time() - start_time)

    for  _ in range(0, int(N ** (1/2))):
        grover(qc, n, target_binary, oracle_gate, amplifier_gate)

    qc.barrier()
    qc.measure(range(n), range(n))

    result = get_result(qc)
    max = parse_result(result, p=False)

    print("\n--Results--")

    print("Most probable result was: " + str(max[0]) + " with " + str(max[1]) + " occurences.")

    print("Program took %s seconds\n" % seconds)

print("--Deprecation warnings--")

print("\n--Setup--")
N = get_N()
t = get_target(N)
run(N, t)