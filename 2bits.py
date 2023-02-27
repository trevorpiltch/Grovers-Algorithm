from internal import *
from qiskit import QuantumCircuit

"""
Say we have two qubits, then the possible bit combinations are:
[00, 10, 01, 11]

Our marked state is x* = 11

Oracle gate is:
[ 1 0 0 0
  0 1 0 0
  0 0 1 0
  0 0 0 -1]
which is called a controlled-z gate
"""

n = 2
N = 2 ** n

# Creates circuit
qc = QuantumCircuit(n)

# Initializes qubits in superposition
qc = initialize_s(qc, [0,1])

# Apply the oracle gate
qc.cs(0, 1)

# Apply the diffuser operator
qc.append(diffuser(n), [0, 1])

# Measure the results
qc.measure_all()

# Displays the ascii text representation of the circuit
print(qc.draw('text'))

# Runs and prints results of the circuit
print(printResults(qc))