# Grovers Algorithm
## What is it?
Grover’s Algorithm is an unstructured search algorithm that runs in √N with √N \*log(N) gates on a quantum computer. Lov Grover created the algorithm in 1996 while at Bell Labs.

## How does it work?
For simplification, we’re assuming the database has 2^n terms (which we’ll label N). We’ll label the state we’re searching for x\* and all other states x. From here, Grover’s algorithm is split into two sections: the Oracle and Amplitude Amplification. 

### Oracle
The oracle is a diagonal quantum gate that flips the sign of x\* to negative and all other states positive. For example, if we had N = 4 terms and x\* = |11\> then the oracle would look as the first matrix below.
To build a general oracle, we can harness a classical gate f that returns 1 if its input is x\* and 0 otherwise. Then, using a qubit in the superposition 1/√2 (|0\> - |1\>) we can perform an Xor on the two to get the sign. If f = 0, then the bit is unchanged but if f = 1, then the sign becomes the second image below, which can be simplified to the third image, which is the negative of our original gate. Then by multiplying (or to use the proper term tensor product) x, we get the oracle we want. This is summed up by the last expression below.

![](imagesScreen%20Shot%202023-02-28%20at%208.35.01%20AM.png) <br>
![](images/Screen%20Shot%202023-02-28%20at%208.35.55%20AM.png) <br>
![](images/Screen%20Shot%202023-02-28%20at%208.36.08%20AM.png) <br>
![](images/Screen%20Shot%202023-02-28%20at%208.35.43%20AM.png) <br><br>

### Amplitude Amplification
To start, we initialize N qubits in the super position given in the previous section. Then we apply our oracle to flip the state x\* (labeled W in the images below) which lowers the overall average amplitude. The next step is to apply the diffuser, which lowers the amplitudes to the average, and flips x\* back to positive. The diffuser is a complex quantum gate, made of many H, X, and various control gates. It was proved by Grover that this process converges on the answer in √N times, although this proof is outside the scope of this repo. 

![](images/Screen%20Shot%202023-02-28%20at%208.36.27%20AM.png) <br>
![](images/Screen%20Shot%202023-02-28%20at%208.36.34%20AM.png) <br>
![](images/Screen%20Shot%202023-02-28%20at%208.36.39%20AM.png) <br>

## Sources
[Grovers Algorithm](https://qiskit.org/textbook/ch-algorithms/grover.html#3.-Example:-3-Qubits-) <br>
[Original Paper](https://arxiv.org/pdf/quant-ph/9605043.pdf) <br>
[CMU Lecture Paper](https://www.cs.cmu.edu/~odonnell/quantum15/lecture04.pdf)
