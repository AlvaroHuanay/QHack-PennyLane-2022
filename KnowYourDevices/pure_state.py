#! /usr/bin/python3

import sys
import pennylane as qml
from pennylane import numpy as np


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    num_wires = int(inputs[0])
    l = int(len(inputs[1:]) / 2)
    params = [
        np.array(inputs[1 : (l + 1)], dtype=float),  # for pure circuit
        np.array(inputs[(l + 1) :], dtype=float),  # for mixed circuit
    ]
print("inputs are" ,inputs)
print("number of wires", num_wires)
print("params type: ", type(params))
dev0 = qml.device("default.qubit", wires=num_wires)     
#Decorator for pure circuit
@qml.qnode(dev0)
def pure_circuit(wires, params): 
    i=0
    for item in range(wires):
        #for i in len(params[0])
        qml.RY(params.item(i), wires=item) #Rotation R_y in wire i. 
        i=i+1
        #Cómo sé que se lo estoy asignando a dev0? Álvaro: Por el "@...dev0"?
    print("inputs are" ,inputs)
    print("number of wires", wires)
    print("params are: ", params)
    return qml.state()

pure_state=pure_circuit(wires=num_wires, params=params[0]) #create the pure state and store it into the variable
print(pure_state)