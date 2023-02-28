# Grovers Algorithm
## How to use
Download qiskit: `sudo pip install Qiskit==0.24.1` (**MUST BE VERSION 0.24.1**) <br>
Ignore warnings: run with the `-W ignore::DeprecationWarning` command

## Implementation Functions
Credit to Saasha Joshi for their (repo)[https://github.com/SaashaJoshi/grovers-algorithm] that showed the implementations of these functions. <br>
### Oracle
Creates the Grovers oracle based on the target qubit. This is the limiting function here, as it runs in O(n) terms not O(1) as described. Future updates might fix this but limitations in Qiskit prevent it now.

### Amplification
Creates the diffuser gate based on V and V-dagger gates.

### Init
Prepares the given qubits so they're ready for the algorithm.

### Grover
Combines the oracle and amplification gates into a grovers algorithm circuit.

### Run
Combines all the above functions to run the algorithm. <br>

### Target 
Asks for inputs on the command line for the number of qubits to use (must be a power of 2) and target number (must be in the range 0...2^n).

## About
### What is it?
Grover’s Algorithm is an unstructured search algorithm that runs in √N with √N \*log(N) gates on a quantum computer. Lov Grover created the algorithm in 1996 while at Bell Labs.

### How does it work?
For simplification, we’re assuming the database has 2^n terms (which we’ll label N). We’ll label the state we’re searching for x\* and all other states x. From here, Grover’s algorithm is split into two sections: the Oracle and Amplitude Amplification. 

#### Oracle
The oracle is a general gate that is used in the amplitude flip (described below). Its purpose is to flip the sign of the qubit we’re looking for, while leaving all other qubits the same. The oracle can be created in O(1) time, although this implementation was not possible using Qiskit. The best we could get was O(N).<br>
As an example, if we had N = 4 terms and x\* = |11\> then the oracle would look as the first matrix below.
To build a general oracle, we can harness a classical gate f that returns 1 if its input is x\* and 0 otherwise. Then, using a qubit in the superposition 1/√2 (|0\> - |1\>) we can perform an Xor on the two to get the sign. If f = 0, then the bit is unchanged but if f = 1, then the sign becomes the second image below, which can be simplified to the third image, which is the negative of our original gate. Then by multiplying (or to use the proper term tensor product) x, we get the oracle we want. This is summed up by the last expression below.

![](imagesScreen%20Shot%202023-02-28%20at%208.35.01%20AM.png) <br>
![](images/Screen%20Shot%202023-02-28%20at%208.35.55%20AM.png) <br>
![](images/Screen%20Shot%202023-02-28%20at%208.36.08%20AM.png) <br>
![](images/Screen%20Shot%202023-02-28%20at%208.35.43%20AM.png) <br><br>

#### Amplitude Amplification
To start, we initialize N qubits in the super position given in the previous section. Then we apply our oracle to flip the state x\* (labeled W in the images below) which lowers the overall average amplitude. The next step is to apply the diffuser, which lowers the amplitudes to the average, and flips x\* back to positive. The diffuser is a complex quantum gate, made of many H, X, and various control gates. It was proved by Grover that this process converges on the answer in √N times, although this proof is outside the scope of this repo. 

![](images/Screen%20Shot%202023-02-28%20at%208.36.27%20AM.png) <br>
![](images/Screen%20Shot%202023-02-28%20at%208.36.34%20AM.png) <br>
![](images/Screen%20Shot%202023-02-28%20at%208.36.39%20AM.png) <br>

## Sources
[Grovers Algorithm](https://qiskit.org/textbook/ch-algorithms/grover.html#3.-Example:-3-Qubits-) <br>
[Original Paper](https://arxiv.org/pdf/quant-ph/9605043.pdf) <br>
[CMU Lecture Paper](https://www.cs.cmu.edu/~odonnell/quantum15/lecture04.pdf)
