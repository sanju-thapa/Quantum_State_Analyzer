# Quantum State Analyzer using NumPy

## Overview

This project is a simple **quantum state analyzer** built using Python, NumPy, and Matplotlib.

The goal of the project is to understand how fundamental quantum-computing concepts can be represented using vectors, matrices, tensor products, probability calculations, and linear algebra.

This project covers:

* Quantum state representation
* State normalization
* Measurement probabilities
* Pauli-X gate
* Hadamard gate
* Quantum superposition
* Two-qubit basis states
* Tensor products
* Identity matrices
* Applying gates to individual qubits
* Expectation values
* Probability visualization using Matplotlib

---

## Technologies Used

* Python
* NumPy
* Matplotlib
* Linear Algebra
* Quantum Computing Fundamentals

---

## 1. Creating a Quantum State

A single-qubit quantum state can be represented using a NumPy array.

```python
import numpy as np

quantum_state = np.array([1, 1], dtype=complex)
```

Initially,

$$
\psi =
\begin{bmatrix}
1 \
1
\end{bmatrix}
$$

This state is not normalized yet.

---

## 2. Quantum State Normalization

A valid quantum state must satisfy:

$$
\langle \psi | \psi \rangle = 1
$$

The norm of the state is:

$$
|\psi|
======

# \sqrt{|1|^2 + |1|^2}

\sqrt{2}
$$

The normalized state is:

$$
|\psi\rangle
============

\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 \
1
\end{bmatrix}
$$

or equivalently,

$$
|\psi\rangle
============

\frac{1}{\sqrt{2}}
\left(
|0\rangle + |1\rangle
\right)
$$

Using NumPy:

```python
norm = np.linalg.norm(quantum_state)

quantum_normalized = quantum_state / norm
```

The result is approximately:

```text
[0.70710678+0.j  0.70710678+0.j]
```

---

## 3. Measurement Probabilities

Quantum amplitudes themselves are not probabilities.

The probability of measuring a particular basis state is obtained by taking the squared magnitude of its amplitude.

$$
P(i) = |\psi_i|^2
$$

Using NumPy:

```python
probabilities = np.abs(quantum_normalized) ** 2
```

For the current state:

$$
P(0) = 0.5
$$

$$
P(1) = 0.5
$$

Therefore,

$$
P(0) + P(1) = 1
$$

---

## Measurement Probability Visualization

Matplotlib is used to visualize the probability of measuring the state as `|0>` or `|1>`.

```python
import matplotlib.pyplot as plt

basis_states = ["|0>", "|1>"]

plt.bar(basis_states, probabilities)

plt.xlabel("Basis State")
plt.ylabel("Probability")
plt.title("Quantum State Measurement Probabilities")
plt.ylim(0, 1)

plt.savefig(
    "measurement_probabilities.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
```

### Output

![Measurement Probabilities](measurement_probabilities.png)

---

## 4. Computational Basis States

The two basic single-qubit states are:

$$
|0\rangle =
\begin{bmatrix}
1 \
0
\end{bmatrix}
$$

and

$$
|1\rangle =
\begin{bmatrix}
0 \
1
\end{bmatrix}
$$

In NumPy:

```python
state_0 = np.array([1, 0])
state_1 = np.array([0, 1])
```

---

## 5. Pauli-X Gate

The Pauli-X gate behaves similarly to a classical NOT gate.

Its matrix representation is:

$$
X =
\begin{bmatrix}
0 & 1 \
1 & 0
\end{bmatrix}
$$

In NumPy:

```python
X_gate = np.array([
    [0, 1],
    [1, 0]
])
```

Applying it to the basis states:

$$
X|0\rangle = |1\rangle
$$

and

$$
X|1\rangle = |0\rangle
$$

Using NumPy:

```python
print(X_gate @ state_0)
print(X_gate @ state_1)
```

---

## 6. Hadamard Gate

The Hadamard gate creates a quantum superposition.

Its matrix is:

$$
H =
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \
1 & -1
\end{bmatrix}
$$

In NumPy:

```python
H_gate = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
])
```

Applying the Hadamard gate to `|0>` gives:

$$
H|0\rangle
==========

\frac{1}{\sqrt{2}}
\left(
|0\rangle + |1\rangle
\right)
$$

Applying it to `|1>` gives:

$$
H|1\rangle
==========

\frac{1}{\sqrt{2}}
\left(
|0\rangle - |1\rangle
\right)
$$

Using NumPy:

```python
superposition_0 = H_gate @ state_0
superposition_1 = H_gate @ state_1
```

Both states give measurement probabilities:

$$
[0.5,\ 0.5]
$$

However, the relative phase between the amplitudes is different.

---

## 7. Two-Qubit Basis States

Two-qubit states are created using the tensor product.

NumPy provides:

```python
np.kron()
```

The four computational basis states are:

$$
|00\rangle =
\begin{bmatrix}
1 \
0 \
0 \
0
\end{bmatrix}
$$

$$
|01\rangle =
\begin{bmatrix}
0 \
1 \
0 \
0
\end{bmatrix}
$$

$$
|10\rangle =
\begin{bmatrix}
0 \
0 \
1 \
0
\end{bmatrix}
$$

$$
|11\rangle =
\begin{bmatrix}
0 \
0 \
0 \
1
\end{bmatrix}
$$

Using NumPy:

```python
state_00 = np.kron(state_0, state_0)
state_01 = np.kron(state_0, state_1)
state_10 = np.kron(state_1, state_0)
state_11 = np.kron(state_1, state_1)
```

For two qubits, the state vector contains:

$$
2^2 = 4
$$

amplitudes.

More generally, an `n`-qubit system requires:

$$
2^n
$$

amplitudes.

---

## 8. Identity Matrix

The identity operator for a single qubit is:

$$
I =
\begin{bmatrix}
1 & 0 \
0 & 1
\end{bmatrix}
$$

In NumPy:

```python
I = np.eye(2)
```

The identity matrix leaves a state unchanged.

---

## 9. Applying a Gate to One Qubit

For a two-qubit system, tensor products can be used to apply a gate to only one qubit.

### Apply X to the Second Qubit

The operator is:

$$
I \otimes X
$$

In NumPy:

```python
IX = np.kron(I, X_gate)

result_second = IX @ state_00
```

This performs:

$$
|00\rangle
\rightarrow
|01\rangle
$$

---

### Apply X to the First Qubit

The operator is:

$$
X \otimes I
$$

In NumPy:

```python
XI = np.kron(X_gate, I)

result_first = XI @ state_00
```

This performs:

$$
|00\rangle
\rightarrow
|10\rangle
$$

This demonstrates that the position of an operator in a tensor product determines which qubit it acts on.

---

## 10. Expectation Value

An expectation value represents the average value expected when measuring an observable.

For an operator $A$:

$$
\langle A \rangle
=================

\langle\psi|A|\psi\rangle
$$

For this project, the Pauli-Z operator is used:

$$
Z =
\begin{bmatrix}
1 & 0 \
0 & -1
\end{bmatrix}
$$

In NumPy:

```python
Z_gate = np.array([
    [1, 0],
    [0, -1]
])
```

The expectation value is calculated using:

```python
expectation_value = (
    quantum_normalized.conj().T
    @ Z_gate
    @ quantum_normalized
)
```

For the state

$$
|\psi\rangle
============

\frac{1}{\sqrt{2}}
\left(
|0\rangle + |1\rangle
\right),
$$

the expectation value of $Z$ is:

$$
\langle Z \rangle = 0
$$

Expectation values are especially important in variational quantum algorithms such as **VQE — Variational Quantum Eigensolver**.

---

## NumPy Concepts Practiced

This project uses several important NumPy operations:

```text
np.array()
np.linalg.norm()
np.abs()
np.sum()
np.sqrt()
np.eye()
np.kron()
```

It also uses:

```python
A @ B
```

for matrix multiplication.

For complex quantum states:

```python
psi.conj().T
```

calculates the conjugate transpose of a state vector.

---

## Project Structure

```text
Quantum_State_Analyzer/
│
├── main.py
├── README.md
└── measurement_probabilities.png
```

---

## What I Learned

Through this project, I learned how NumPy can be used to represent fundamental quantum-computing concepts using linear algebra.

The project helped me understand:

* How quantum states are represented using vectors
* Why quantum states must be normalized
* How amplitudes are converted into probabilities
* How quantum gates can be represented using matrices
* How matrix multiplication changes quantum states
* How the Hadamard gate creates superposition
* How tensor products create multi-qubit systems
* How identity matrices help apply gates to selected qubits
* How expectation values are calculated
* How NumPy operations connect directly with quantum mechanics

---

## Future Improvements

Future versions of this project can include:

* Pauli-Y gate
* Pauli-Z gate simulations
* Phase gates
* CNOT gate
* Bell-state generation
* Entanglement
* Multiple quantum-gate sequences
* Bloch-sphere visualization
* Hamiltonian construction
* Eigenvalue and eigenvector calculations
* Ground-state energy calculations
* Variational Quantum Eigensolver implementation
* Comparison with Qiskit or PennyLane

---

## Author

**R.Sanju**

Interested in quantum computing, numerical simulation, Python, and variational quantum algorithms.
