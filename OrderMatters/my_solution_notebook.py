{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4651822e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#! /usr/bin/python3\n",
    "\n",
    "import sys\n",
    "import pennylane as qml\n",
    "from pennylane import numpy as np\n",
    "\n",
    "\n",
    "def compare_circuits(angles):\n",
    "    \"\"\"Given two angles, compare two circuit outputs that have their order of operations flipped: RX then RY VERSUS RY then RX.\n",
    "\n",
    "    Args:\n",
    "        - angles (np.ndarray): Two angles\n",
    "\n",
    "    Returns:\n",
    "        - (float): | < \\sigma^x >_1 - < \\sigma^x >_2 |\n",
    "    \"\"\"\n",
    "\n",
    "    # QHACK #\n",
    "\n",
    "    #Define circuit (of 2 qubits)\n",
    "    dev0 = qml.device(\"default.qubit\", wires=2) #Name of our ciruit 0 (default.qubit is an argument to call a standard qubit)\n",
    "    @qml.qnode(dev0)\n",
    "    #It is mandatory to convert it into a QNode\n",
    "    def circuit(params): #Now, we create the function\n",
    "        qml.RX(params[0], wires=0) #First rotation qubit 0\n",
    "        qml.RY(params[1], wires=0) #Second rotation qubit 0\n",
    "\n",
    "        qml.RY(params[1], wires=1) #Firs rotation qubit 1\n",
    "        qml.RX(params[0], wires=1) #Second rotation qubit 1\n",
    "\n",
    "        return qml.expval(qml.PauliX(0)), qml.expval(qml.PauliX(1)) #Give the expectation value of PauliX in wires/qubits 0 and 1\n",
    "\n",
    "    # QHACK #\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    # DO NOT MODIFY anything in this code block\n",
    "    angles = np.array(sys.stdin.read().split(\",\"), dtype=float)\n",
    "    output = compare_circuits(angles)\n",
    "    print(f\"{output:.6f}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
