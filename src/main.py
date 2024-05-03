
# Quantum Simulation Project - main.py
# This is the main execution script for the quantum simulation project.

import numpy as np
import logging
from classical_energy.py import calculate_classical_energy
from quantum_energy.py import calculate_quantum_energy
from phonon_info.py import calculate_information_content
from utils.py import setup_simulation_environment
from config_manager.py import load_config, save_config

def main():
    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Load configuration
    config_path = 'config.json'
    config = load_config(config_path)
    
    # Setup the simulation environment
    setup_simulation_environment(config)
    
    # Initialize phonon states
    phonon_states = np.random.normal(0, 1, size=100)  # Example: 100 phonon modes with normal distribution
    
    # Calculate classical energy
    classical_energy = calculate_classical_energy(phonon_states, config)
    logging.info(f'Classical Energy: {classical_energy}')
    
    # Calculate quantum energy
    quantum_energy = calculate_quantum_energy(phonon_states, config)
    logging.info(f'Quantum Energy: {quantum_energy}')
    
    # Calculate information content
    information_content = calculate_information_content(phonon_states, config)
    logging.info(f'Information Content: {information_content}')

if __name__ == '__main__':
    main()
