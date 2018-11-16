import cirq
import numpy as numpy
from cirq.devices import GridQubit
from cirq.google import XmonSimulator
length = 4
qubits = [cirq.GridQubit(x,y) for x in range(length) for y in range(length)]
print("qubits")

circuit = cirq.Circuit()
H1 = cirq.H(qubits[2])
TOFFOLI = cirq.TOFFOLI(qubits[3], qubits[4], qubits[5])
H2 = cirq.H(qubits[1])
H3 = cirq.H(qubits[2])
H4 = cirq.H(qubits[3])
H5 = cirq.H(qubits[4])
CZ1 = cirq.CZ(qubits[3], qubits[2], qubits[4])
CZ2 = cirq.CZ(qubits[2], qubits[3], qubits[4])
CZ3 = cirq.CZ(qubits[4], qubits[3], qubits[2])
moment1 = cirq.Moment([H1])
moment2 = cirq.Moment([TOFFOLI])
moment3 = cirq.Moment([H1])
moment4 = cirq.Moment([H2, H3, H4, H5])
moment5 = cirq.Moment([CZ1])
moment6 = cirq.Moment([CZ2])
moment7 = cirq.Moment([H2, H3, H4, H5])

circuit = cirq.Circuit((moment1, moment2, moment3, moment4, moment5, moment6, moment7))
print(circuit)
simulator = Xmonsimulator()
result = simulator.simulate(circuit)
print(result)



