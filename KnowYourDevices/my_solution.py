#! /usr/bin/python3

import sys
import pennylane as qml
from pennylane import numpy as np


def matrix_norm(mixed_state, pure_state):
    """Computes the matrix one-norm of the difference between mixed and pure states.

    Args:
        - mixed_state (np.tensor): A density matrix
        - pure_state (np.tensor): A pure state

    Returns:
        - (float): The matrix one-norm
    """

    return np.sum(np.abs(mixed_state - np.outer(pure_state, np.conj(pure_state))))


def compare_circuits(num_wires, params):
    """Function that returns the matrix norm between the mixed- and pure-state versions of the same state.

    Args:
        - num_wires (int): The number of qubits / wires
        - params (list(np.ndarray)): Two arrays with num_wires floats that correspond to angles of y-rotations
        for each wire

    Returns:
        - mat_norm (float): The matrix one-norm
    """

    # QHACK #
    dev0 = qml.device("default.qubit", wires=num_wires)     
    #Decorator for pure circuit
    @qml.qnode(dev0)
    def pure_circuit(wires=num_wires, params=params[0]):
        """A circuit that contains `num_wires` y-rotation gates.
        The argument params[0] are the parameters you should use here to define the y-rotations.

        Returns:
            - (np.tensor): A state vector
        """
        i=0
        for item in range(wires):
            #for i in len(params[0])
            qml.RY(params.item(i), wires=item) #Rotation R_y in wire i. 
            i=i+1
            #Cómo sé que se lo estoy asignando a dev0? Álvaro: Por el "@...dev0"?
        return qml.state()

    dev1 = qml.device("default.mixed", wires=num_wires) #Mixed state 
    #Decorator for pure circuit
    @qml.qnode(dev1)
    def mixed_circuit(wires=num_wires, params=params[1]):
        """A circuit that contains `num_wires` y-rotation gates.
        The argument params[1] are the parameters you should use here to define the y-rotations.

        Returns:
            - (np.tensor): A density matrix
        """
        i=0
        for item in range(wires):
            #for i in len(params[0])
            qml.RY(params.item(i), wires=item) #Rotation R_y in wire i. 
            i=i+1
            #Cómo sé que se lo estoy asignando a dev0? Álvaro: Por el "@...dev0"?
        
        return qml.state()

    # QHACK #

    # DO NOT MODIFY any of the next lines in this scope
    mixed_state = mixed_circuit()
    pure_state = pure_circuit()
    mat_norm = matrix_norm(mixed_state, pure_state)
    
    return mat_norm


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    num_wires = int(inputs[0])
    l = int(len(inputs[1:]) / 2)
    params = [
        np.array(inputs[1 : (l + 1)], dtype=float),  # for pure circuit
        np.array(inputs[(l + 1) :], dtype=float),  # for mixed circuit
    ]

    output = compare_circuits(num_wires, params)
    print(f"{output:.6f}")