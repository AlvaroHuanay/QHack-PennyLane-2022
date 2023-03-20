#! /usr/bin/python3

import sys
import pennylane as qml
from pennylane import numpy as np

dev = qml.device("default.qubit", wires=3)


def my_finite_diff_grad(params):
    """Function that returns the gradients of the cost function (defined below) with respect 
    to all parameters in params.

    Args:
        - params (np.ndarray): The parameters needed to create the variational circuit.

    Returns:
        - gradients (np.ndarray): the gradient w.r.t. each parameter
    """

    gradients = np.zeros([len(params)]) #store the differentiation for each param given

    for i in range(len(params)):
        
        # QHACK # 
        #f(increase)-f(decrease)
        arg_incr=np.array(params, dtype=float) #First f
        arg_decr=np.array(params, dtype=float) #Second f
        
        delta=params.item(i) #Denominator
        
        increase=arg_incr.item(i)+delta/2 #Increase of first term argument
        decrease=arg_decr.item(i)-delta/2 #Decrease of second term argument
        
        #f(increase)
        arg_incr=np.delete(arg_incr, i)     #Delete the term x_i
        arg_incr=np.insert(arg_incr, i, increase) #Substitute for the new increment
        
        #f(decrease)
        arg_decr=np.delete(arg_decr, i)     #Delete the term x_i
        arg_decr=np.insert(arg_decr, i, decrease) #Substitute for the new decreasing
        
        gradients=np.delete(gradients, i)
        gradients=np.insert(gradients, i, (cost(arg_incr)-cost(arg_decr))/delta)
          
        # QHACK #

    return gradients


def variational_circuit(params):
    """A layered variational circuit. The first layer comprises of x, y, and z rotations on wires
    0, 1, and 2, respectively. The second layer is a ring of CNOT gates. The final layer comprises 
    of x, y, and z rotations on wires 0, 1, and 2, respectively.
    """

    # DO NOT MODIFY anything in this code block
    qml.RX(params[0], wires=0)
    qml.RY(params[1], wires=1)
    qml.RZ(params[2], wires=2)

    qml.broadcast(qml.CNOT, wires=[0, 1, 2], pattern="ring")
    
    #Applies a unitary multiple times to a specific pattern of wires.
    #pattern="ring" applies a two-wire unitary to all M
    #neighbouring pairs of wires, where the last wire is considered
    #to be a neighbour to the first one:

    qml.RX(params[3], wires=0)
    qml.RY(params[4], wires=1)
    qml.RZ(params[5], wires=2)

    qml.broadcast(qml.CNOT, wires=[0, 1, 2], pattern="ring")
    
    #returns an state. This is the circuit
    


@qml.qnode(dev) #in device dev do:
def cost(params):
    """A QNode that pairs the variational_circuit with an expectation value measurement.

    Args:
        - params (np.ndarray): Variational circuit parameters

    Returns:
        - (float): qml.expval(qml.PauliY(0) @ qml.PauliZ(2))
    """

    # DO NOT MODIFY anything in this code block
    variational_circuit(params)

    return qml.expval(qml.PauliY(0) @ qml.PauliZ(2))

    #returns the entangled measurement of
    #the expectation value of PauliY(0)xZ(2)


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    params = np.array(sys.stdin.read().split(","), dtype=float)
    output = my_finite_diff_grad(params)
    print(*output, sep=",")