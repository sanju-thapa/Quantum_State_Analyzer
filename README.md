# Quantum State Analyzer using NumPy

## Overview

This project is a simple quantum-state simulator built using Python and NumPy.

The goal of the project is to understand how fundamental quantum-computing operations can be represented using vectors, matrices, tensor products, and linear algebra.

## Features

The project demonstrates:

* Creation of quantum state vectors
* Quantum-state normalization
* Measurement probability calculation
* Computational basis states `|0>` and `|1>`
* Pauli-X gate
* Hadamard gate
* Quantum superposition
* Two-qubit basis states
* Tensor products using `np.kron()`
* Identity matrices
* Applying gates to individual qubits
* Expectation value calculation

## Technologies Used

* Python
* NumPy
* Linear Algebra
* Quantum Computing Fundamentals

## Example

A quantum state is represented using a NumPy array:

```python
import numpy as np

quantum_state = np.array([1, 1], dtype=complex)
```

The state is normalized using:

```python
norm = np.linalg.norm(quantum_state)
quantum_normalized = quantum_state / norm
```

which produces approximately:

```text
[0.70710678+0.j 0.70710678+0.j]
```

This represents the quantum state:

[
|\psi\rangle =
\frac{1}{\sqrt{2}}
(|0\rangle + |1\rangle)
]

## Quantum Gates

### Pauli-X Gate

The Pauli-X gate behaves similarly to a classical NOT gate.

[
X =
\begin{bmatrix}
0 & 1 \
1 & 0
\end{bmatrix}
]

It performs:

[
X|0\rangle = |1\rangle
]

and

[
X|1\rangle = |0\rangle
]

### Hadamard Gate

The Hadamard gate creates quantum superposition.

[
H =
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \
1 & -1
\end{bmatrix}
]

For example:

[
H|0\rangle =
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
]

## Two-Qubit Systems

Two single-qubit states are combined using the tensor product.

In NumPy:

```python
state_00 = np.kron(state_0, state_0)
```

which represents:

[
|00\rangle
]

The four computational basis states are:

```text
|00> = [1 0 0 0]
|01> = [0 1 0 0]
|10> = [0 0 1 0]
|11> = [0 0 0 1]
```

## Applying Gates to Individual Qubits

The identity matrix is used when one qubit should remain unchanged.

For example:

```python
IX = np.kron(I, X_gate)
```

represents:

[
I \otimes X
]

This applies the Pauli-X gate to the second qubit while leaving the first qubit unchanged.

## Expectation Value

The project also calculates an expectation value using:

[
\langle\psi|Z|\psi\rangle
]

In NumPy:

```python
expectation_value = (
    quantum_normalized.conj().T
    @ Z_gate
    @ quantum_normalized
)
```

Expectation values are particularly important in variational quantum algorithms such as VQE.

## What I Learned

Through this project, I practiced NumPy concepts including:

* `np.array()`
* `np.linalg.norm()`
* `np.abs()`
* `np.sum()`
* `np.sqrt()`
* `np.eye()`
* `np.kron()`
* Matrix multiplication using `@`
* Array transpose
* Complex conjugation

The project also helped connect NumPy linear-algebra operations with fundamental quantum-computing concepts.

## Future Improvements

Possible extensions include:

* Adding Pauli-Y and Pauli-Z gates
* Implementing controlled gates such as CNOT
* Creating Bell states
* Simulating simple quantum circuits
* Adding visualization with Matplotlib
* Implementing simple Hamiltonians
* Comparing exact ground-state energies with VQE

