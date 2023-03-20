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
print("params are ", params)
print("params type: ", type(params))
dev1 = qml.device("default.mixed", wires=num_wires) #Mixed state 
#Decorator for pure circuit
@qml.qnode(dev1)
def mixed_circuit(wires, params): 
    i=0
    for item in range(wires):
        #for i in len(params[0])
        qml.RY(params.item(i), wires=item) #Rotation R_y in wire i. 
        i=i+1
        #Cómo sé que se lo estoy asignando a dev0? Álvaro: Por el "@...dev0"?
    
    print("inputs are" ,inputs)
    print("number of wires", wires)
    print("params (phis) are: ", params)
    return qml.state()

mixed_state=mixed_circuit(wires=num_wires, params=params[1]) #create the pure state and store it into the variable
print(mixed_state)


