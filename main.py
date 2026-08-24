import numpy as np
import matplotlib.pyplot as plt

# Step 1:
# Create an Quantum state 
quantum_state = np.array([1, 1], dtype=complex)

# Normailze the Quantum state
norm = np.linalg.norm(quantum_state)
quantum_normalized = quantum_state / norm
print(f"Normalized Quantum State:\n {quantum_normalized}")

# Step 2:
# Measurement Probability
probabilities = np.abs(quantum_normalized) ** 2 
print(f"\nMeasurement Probability: {probabilities}")
print(f"\nTotal Probability: {np.sum(probabilities)}")

# Step 2.1:
# Visualize the Measurement Probability
basis_states = ["|0>", "|1>"]
plt.bar(basis_states, probabilities)
plt.xlabel("Basis States")
plt.ylabel("Probability")
plt.title("Quantum State Measurement Probabilities")
plt.ylim(0, 1)
plt.savefig("measurement_probability.png", dpi=300, bbox_inches="tight")
plt.show()

# Step 3:
# Define the Basis States
state_0 = np.array([1, 0])
state_1 = np.array([0, 1])

# Step 4:
# Apply Pauli-X gate to the state
X_gate = np.array([[0, 1], [1, 0]])
print(f"Pauli_X gate act on the states:")
print(f"\nX|0> = {X_gate @ state_0}")
print(f"\nX|1> = {X_gate @ state_1}")

# Step 5:
# Applying Hadamard gate on the states
H_gate = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
superposition_0 = H_gate @ state_0
superposition_1 = H_gate @ state_1
print(f"\nHadamard gate on the state:")
print(f"\nH|0> = {superposition_0} \nH|1> = {superposition_1}")
print(f"\nHadamard gate probability:\n \n{np.abs(superposition_0) ** 2} \n{np.abs(superposition_1) ** 2}")

# Step 6:
# Stating the Two_qubit basis state
state_00 = np.kron(state_0, state_0)
state_01 = np.kron(state_0, state_1)
state_10 = np.kron(state_1, state_0)
state_11 = np.kron(state_1, state_1)
print(f"\n Two-qubit basis state:")
print(f"\n |00> = {state_00}")
print(f"\n |01> = {state_01}")
print(f"\n |10> = {state_10}")
print(f"\n |11> = {state_11}")

# Step 7:
# Identity matrix 
I = np.eye(2)

# Applying X gate on second qubit state|00>
IX = np.kron(I, X_gate)
result_second = IX @ state_00
print(f"\n Apply X to second qubit:\n I ⊗ X|00> = {result_second}")

# Applying X gate on the first qubit state|00>
XI = np.kron(X_gate, I)
result_first = XI @ state_00
print(f"\n Apply X to first qubit:\n X ⊗ I|00> = {result_first}")

# Step 8:
# Expectation Value
Z_gate = np.array([[1, 0], [0, -1]])
expectation_value = quantum_normalized.conj().T @ Z_gate @ quantum_normalized
print(f"\nExpectation Value of Z: {expectation_value}")