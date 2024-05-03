
# Quantum Simulation Project - main.py
# This script orchestrates the simulation of quantum and classical energy interactions in a phonon-based system.

import json
import numpy as np
from quantum_energy import calculate_quantum_energy
from classical_energy import calculate_classical_energy
from phonon_info import calculate_information_content
from utils import setup_simulation_environment
from config_manager import load_simulation_config
from logger import setup_logger

def main():
    # Setup logging
    logger = setup_logger()
    
    # Load simulation parameters
    config = load_simulation_config('data/simulation_parameters.json')
    
    # Setup the simulation environment
    setup_simulation_environment(config)
    
    # Initialize system states
    initial_conditions = json.load(open('data/initial_conditions.json', 'r'))
    phonon_states = np.array(initial_conditions['phonon_states'])
    
    # Calculate energies
    quantum_energy = calculate_quantum_energy(phonon_states, config)
    classical_energy = calculate_classical_energy(phonon_states, config)
    
    # Compute information content
    information = calculate_information_content(phonon_states, config)
    
    # Output results
    total_energy = quantum_energy + classical_energy
    logger.info(f"Total Energy: {total_energy}")
    logger.info(f"Information Content (bits): {information}")
    
    # Validate against theoretical model
    expected_energy = information * (3e8 ** 2)  # I*c^2, c = speed of light
    logger.info(f"Expected Energy: {expected_energy}")
    
    # Check for consistency
    if np.isclose(total_energy, expected_energy, atol=1e-6):
        logger.info("Simulation validation successful.")
    else:
        logger.error("Simulation validation failed.")

if __name__ == '__main__':
    main()
