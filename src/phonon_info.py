
# Quantum Simulation Project - phonon_info.py
# This module calculates the information content based on the quantum states of phonons.

import numpy as np

def calculate_information_content(phonon_states, config):
    # Information content calculation based on entropy measures
    probabilities = np.abs(phonon_states)**2
    probabilities /= np.sum(probabilities)  # Normalize to get probability distribution
    
    # Shannon entropy formula to calculate information content
    entropy = -np.sum(probabilities * np.log2(probabilities + 1e-10))  # Add small epsilon to avoid log(0)
    
    # Information in bits
    information_bits = entropy
    
    return information_bits
