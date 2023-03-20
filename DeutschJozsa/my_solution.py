import sys
import pennylane as qml
from pennylane import numpy as np


def deutsch_jozsa(oracle):
    """This function will determine whether an oracle defined by a function f is constant or balanced.

    Args:
        - oracle (function): Encoding of the f function as a quantum gate. The first two qubits refer to the input and the third to the output.

    Returns:
        - (str): "constant" or "balanced"
    """

    dev = qml.device("default.qubit", wires=3, shots=1)

    @qml.qnode(dev)
    def circuit():
        """Implements the Deutsch Jozsa algorithm."""

        # QHACK #

        # Insert any pre-oracle processing here
        
        #initial_state=np.zeros(len(numbers)+1, dtype=float) #initial state + ancilliary qubit
        #initial_state[-1]=0  #RY(3.14) comes from here       #last qubit is 1
        #qml.QubitStateVector(initial_state, wires=len(numbers)+1) #num wires=input qubits + 1 axiliary qubit
        
        
        #A:just apply the circuit as in Figure 1
        qml.PauliX(wires=2)
        for i in range(3):
            qml.Hadamard(wires=i)
        
         #A:numbers only goes up to |0>'s, this Hadamard is for |1> (ancciliary qubit)

        oracle()  # DO NOT MODIFY this line

        # Insert any post-oracle processing here
        for i in range(2): #A:in numbers because numbers are the qubits without the ancilliary
            qml.Hadamard(wires=i) #A:just apply the circuit as in Figure 1

        # QHACK #

        return qml.sample(wires=range(2))

    sample = circuit()

    # QHACK #
    drawer = qml.draw(circuit)
    print(drawer())
    # Get the first element
    
    first_element = sample[0]
    # Compares all the elements with the first element
    for element in sample:
       if first_element != element: #the only possible solution is that it is balanced
          output="balanced"
          break
       else: #the only possible solution is that it is constant (all elements are equal)
          output="constant"
      
    
    print("sample is: ", sample)
    # From `sample` (a single call to the circuit), determine whether the function is constant or balanced.
    return output
    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    #inputs=[0]
    inputs = sys.stdin.read().split(",")
    numbers = [int(i) for i in inputs]
    print("input (numbers) is: ", numbers)
    def oracle():
        for i in numbers:
            qml.CNOT(wires=[i, 2])

    output = deutsch_jozsa(oracle)
    print(output)
    #1.ans: balanced
    #2.ans: constant