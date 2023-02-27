from qiskit import QuantumCircuit, Aer, assemble, transpile

def initialize_s(qc, qubits):
    """Applies an H gate to every qubit in the circuit, creating the superpositions we need"""
    for q in qubits:
        qc.h(q)

    return qc

def diffuser(nqubits):
    """
    From: https://qiskit.org/textbook/ch-algorithms/grover.html#3.-Example:-3-Qubits-
    What: Flips the sign of x* and lowers other amplitudes
    """
    qc = QuantumCircuit(nqubits)
    # Apply transformation |s> -> |00..0> (H-gates)
    for qubit in range(nqubits):
        qc.h(qubit)
    # Apply transformation |00..0> -> |11..1> (X-gates)
    for qubit in range(nqubits):
        qc.x(qubit)
    # Do multi-controlled-Z gate
    qc.h(nqubits-1)
    qc.mct(list(range(nqubits-1)), nqubits-1)  # multi-controlled-toffoli
    qc.h(nqubits-1)
    # Apply transformation |11..1> -> |00..0>
    for qubit in range(nqubits):
        qc.x(qubit)
    # Apply transformation |00..0> -> |s>
    for qubit in range(nqubits):
        qc.h(qubit)
    # We will return the diffuser as a gate
    U_s = qc.to_gate()
    U_s.name = "U$_s$"
    return U_s

def printResults(qc):
    """Runs the circuit on the simulator 1024 times and returns a dictionary of the results"""
    aer_sim = Aer.get_backend('aer_simulator')
    transpiled_grover_circuit = transpile(qc, aer_sim)
    qobj = assemble(transpiled_grover_circuit)
    results = aer_sim.run(qobj).result()
    counts = results.get_counts()

    return counts