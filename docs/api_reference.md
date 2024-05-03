```markdown
# API Reference

## Simulation Module

### `initialize_system(num_qubits: int) -> QuantumSystem`
Initialize a multipartite quantum system with the specified number of qubits.

- **Parameters:**
  - `num_qubits` (int): The number of qubits in the system.

- **Returns:**
  - `QuantumSystem`: An initialized quantum system object.

### `evolve_system(system: QuantumSystem, unitary: np.ndarray, time: float) -> QuantumSystem`
Evolve the given quantum system using a unitary operator for a specified duration.

- **Parameters:**
  - `system` (QuantumSystem): The quantum system to evolve.
  - `unitary` (np.ndarray): The unitary operator representing the evolution.
  - `time` (float): The duration of the evolution.

- **Returns:**
  - `QuantumSystem`: The evolved quantum system.

### `measure_system(system: QuantumSystem) -> Tuple[float, np.ndarray]`
Measure the state of the quantum system.

- **Parameters:**
  - `system` (QuantumSystem): The quantum system to measure.

- **Returns:**
  - `Tuple[float, np.ndarray]`: A tuple containing the measured value and the corresponding state vector.

## Analysis Module

### `calculate_fidelity(initial_state: np.ndarray, final_state: np.ndarray) -> float`
Calculate the fidelity between two quantum states.

- **Parameters:**
  - `initial_state` (np.ndarray): The initial state vector.
  - `final_state` (np.ndarray): The final state vector.

- **Returns:**
  - `float`: The fidelity between the initial and final states.

### `run_simulation(num_qubits: int, unitary: np.ndarray, time: float) -> float`
Run a simulation of quantum evolution and measure fidelity.

- **Parameters:**
  - `num_qubits` (int): The number of qubits in the system.
  - `unitary` (np.ndarray): The unitary operator representing the evolution.
  - `time` (float): The duration of the evolution.

- **Returns:**
  - `float`: The fidelity between the initial and final states after simulation.

## Visualization Module

### `plot_fidelity_vs_time(times: List[float], fidelities: List[float]) -> None`
Plot the fidelity of the simulation over time.

- **Parameters:**
  - `times` (List[float]): List of time points.
  - `fidelities` (List[float]): List of corresponding fidelities.

- **Returns:**
  - `None`

## Example Usage

```python
import numpy as np
from simulation import initialize_system, evolve_system, measure_system
from analysis import calculate_fidelity, run_simulation
from visualization import plot_fidelity_vs_time

# Initialize a quantum system with 3 qubits
system = initialize_system(3)

# Define a unitary operator for evolution
unitary = np.eye(2**3)  # Identity operator for demonstration

# Evolve the system for 1 unit of time
system = evolve_system(system, unitary, 1.0)

# Measure the system state
measurement, state = measure_system(system)
print("Measured value:", measurement)
print("State vector:", state)

# Calculate fidelity between two states
initial_state = np.array([1, 0, 0, 0])  # Example initial state
final_state = np.array([0.5, 0.5, 0.5, 0.5])  # Example final state
fidelity = calculate_fidelity(initial_state, final_state)
print("Fidelity:", fidelity)

# Run a simulation and measure fidelity
fidelity = run_simulation(3, unitary, 1.0)
print("Simulation Fidelity:", fidelity)

# Plot fidelity vs. time
times = [0.0, 0.5, 1.0]
fidelities = [0.8, 0.6, 0.4]  # Example data
plot_fidelity_vs_time(times, fidelities)
```
```

This API reference provides documentation for the modules and functions involved in the quantum simulation project. Each function is described with its parameters, return values, and usage examples. Let me know if you need further details or modifications!
