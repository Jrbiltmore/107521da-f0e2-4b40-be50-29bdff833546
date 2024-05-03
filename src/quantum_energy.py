
# Quantum Simulation Project - quantum_energy.py
# This module calculates the quantum energy component of phonons in a lattice system.

import numpy as np

def calculate_quantum_energy(phonon_states, config):
    # Extract quantum parameters from config
    hbar = config.get('hbar', 1.0545718e-34)  # Planck's constant (Joule*second)
    omega = config.get('angular_frequency', 1e14)  # Angular frequency of phonons (Hz)

    # Quantum energy calculation
    quantum_energy = 0.5 * hbar * omega * np.sum(phonon_states**2)
    
    return quantum_energy
