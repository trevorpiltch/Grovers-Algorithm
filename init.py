from qiskit import *

def init(qc, n):
    qc.x(n)
    qc.barrier()
    qc.h(range(n+1))
    qc.barrier()
    