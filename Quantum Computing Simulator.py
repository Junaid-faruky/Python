import numpy as np
from typing import List, Union
from functools import reduce

class Qubit:
    def __init__(self, state: np.ndarray = None):
        self.state = state if state is not None else np.array([1, 0], dtype=complex)
        self.state = self.state / np.linalg.norm(self.state)  # Normalize
    
    def measure(self) -> int:
        prob_0 = np.abs(self.state[0]) ** 2
        return 0 if np.random.random() < prob_0 else 1

class QuantumGate:
    @staticmethod
    def hadamard():
        return np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    
    @staticmethod
    def pauli_x():
        return np.array([[0, 1], [1, 0]], dtype=complex)
    
    @staticmethod
    def pauli_y():
        return np.array([[0, -1j], [1j, 0]], dtype=complex)
    
    @staticmethod
    def pauli_z():
        return np.array([[1, 0], [0, -1]], dtype=complex)
    
    @staticmethod
    def cnot():
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ], dtype=complex)
    
    @staticmethod
    def swap():
        return np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ], dtype=complex)

class QuantumCircuit:
    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.state = np.zeros(2 ** num_qubits, dtype=complex)
        self.state[0] = 1  # Initialize to |0...0⟩
        self.gates = []
    
    def apply_gate(self, gate: np.ndarray, qubits: List[int]):
        # Create full operator matrix
        identity = np.eye(2, dtype=complex)
        operators = [identity] * self.num_qubits
        
        for i, qubit in enumerate(qubits):
            operators[qubit] = gate if i == 0 else identity
        
        full_operator = reduce(np.kron, operators)
        self.state = full_operator.dot(self.state)
        self.gates.append((gate, qubits))
    
    def hadamard(self, qubit: int):
        self.apply_gate(QuantumGate.hadamard(), [qubit])
    
    def pauli_x(self, qubit: int):
        self.apply_gate(QuantumGate.pauli_x(), [qubit])
    
    def cnot(self, control: int, target: int):
        self.apply_gate(QuantumGate.cnot(), [control, target])
    
    def swap(self, qubit1: int, qubit2: int):
        self.apply_gate(QuantumGate.swap(), [qubit1, qubit2])
    
    def measure_all(self) -> List[int]:
        probabilities = np.abs(self.state) ** 2
        outcome = np.random.choice(len(self.state), p=probabilities)
        return [int(bit) for bit in format(outcome, f'0{self.num_qubits}b')]
    
    def get_statevector(self) -> np.ndarray:
        return self.state
    
    def get_probabilities(self) -> np.ndarray:
        return np.abs(self.state) ** 2
    
    def run(self, shots: int = 1024) -> dict:
        results = {}
        probabilities = self.get_probabilities()
        
        for _ in range(shots):
            outcome = np.random.choice(len(self.state), p=probabilities)
            binary = format(outcome, f'0{self.num_qubits}b')
            results[binary] = results.get(binary, 0) + 1
        
        return {k: v / shots for k, v in results.items()}

# Example: Bell state creation
circuit = QuantumCircuit(2)
circuit.hadamard(0)
circuit.cnot(0, 1)
print("Bell state probabilities:", circuit.run(shots=1000))
