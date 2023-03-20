#! /usr/bin/python3

import sys
import pennylane as qml
from pennylane import numpy as np


def compare_circuits(angles):
    """Given two angles, compare two circuit outputs that have their order of operations flipped: RX then RY VERSUS RY then RX.

    Args:
        - angles (np.ndarray): Two angles

    Returns:
        - (float): | < \sigma^x >_1 - < \sigma^x >_2 |
    """

    # QHACK #

    #Define circuit (of 2 qubits)
    dev0 = qml.device("default.qubit", wires=2) #Name of our ciruit 0 (default.qubit is an argument to call a standard qubit)
    @qml.qnode(dev0)
    #It is mandatory to convert it into a QNode
    def circuit(angles): #Now, we create the function
        qml.RX(angles[0], wires=0) #First rotation qubit 0
        qml.RY(angles[1], wires=0) #Second rotation qubit 0

        qml.RY(angles[1], wires=1) #Firs rotation qubit 1
        qml.RX(angles[0], wires=1) #Second rotation qubit 1

        return qml.expval(qml.PauliX(0)), qml.expval(qml.PauliX(1)) #Give the expectation value of PauliX in wires/qubits 0 and 1
    
    list=circuit(angles) #llama la función para hacerlo store en un tensor (OJO, no es una list)
    
    #No vale list[0] porque eso es un pennylane.numpy.tensor.tensor y en el print del ejercicio hacemos print de float.
    return qml.math.abs(list.item(0)-list.item(1))
    #Ahora hemos hecho una resta de valores absolutos de floats

    #line 41: Only if I put print(outcome) me sale la solución sin problema
    #solution ejercicio 1: 1.177019 y me da: 1.177019
    # QHACK #
    

if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    angles = np.array(sys.stdin.read().split(","), dtype=float)
    output = compare_circuits(angles)
    print(f"{output:.6f}")