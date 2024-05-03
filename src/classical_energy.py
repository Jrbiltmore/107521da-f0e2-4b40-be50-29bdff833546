
# Quantum Simulation Project - classical_energy.py
# This module calculates the classical energy contributions from phonon modes in a lattice system.

import numpy as np

def calculate_classical_energy(phonon_states, config):
    # Extract classical parameters from config
    mass = config.get('atomic_mass', 1.67e-27)  # Mass of an atom in the lattice (kg)
    k_constant = config.get('spring_constant', 100)  # Spring constant (N/m)

    # Classical energy calculation using harmonic oscillator potential energy formula
    classical_energy = 0.5 * k_constant * np.sum((phonon_states - np.mean(phonon_states))**2)
    
    return classical_energy
