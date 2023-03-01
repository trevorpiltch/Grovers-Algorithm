from qiskit import *
from oracle import *
from amplifier import *
from init import *
from args import *
import time

def grover(circuit, n, target_binary, oracle, amplifier):
    """Applies the oracle and amplification on the circuit"""
    circuit.append(oracle, range(n+1))
    circuit.h(range(n+1))
    circuit.append(amplifier, range(n))
    circuit.h(range(n))

def run(n, target_binary):
    """Runs grovers algorithm with target binary"""
    print("--Running Algorithm--")
    qc = QuantumCircuit(n + 1, n)

    byte = "{0:0%ib}" % n
    target_binary = byte.format(target_binary)

    start_time = time.time()

    init(qc, n)

    oracle_gate = oracle(n, target_binary)
    amplifier_gate = amplifier(n)

    seconds = (time.time() - start_time)

    grover(qc, n, target_binary, oracle_gate, amplifier_gate)
    grover(qc, n, target_binary, oracle_gate, amplifier_gate)

    qc.barrier()
    qc.measure(range(n), range(n))

    backend = Aer.get_backend('qasm_simulator')

    results = execute(qc, backend, shots = 1024).result()
    counts = results.get_counts()
    print(counts)

    print("\nProgram took %s seconds" % seconds)


#TODO: Add command line args for num and target or use random
#TODO: Add result parsing
print("--Deprecation warnings--")

print("\n--Setup--")
N = get_N()
t = get_target(N)
run(N, t)