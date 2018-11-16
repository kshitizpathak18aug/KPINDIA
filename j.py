import cirq
import numpy as numpy
from cirq.devices import GridQubit
from cirq.google import XmonSimulator
length = 4
qubits = [cirq.GridQubit(x,y) for x in range(length) for y in range(length)]
print(qubits)